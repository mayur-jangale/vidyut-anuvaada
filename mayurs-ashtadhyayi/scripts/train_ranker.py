"""Train the split reranker (mayur/ranker.py) on DCS gold half-verses.

    python scripts/train_ranker.py [--lines 5000] [--k 50] [--epochs 10] [--workers 4]

TEST (never trained/tuned on): Rām Bā 1 v1-20, KumSaṃ 1 v1-20, MBh 6.23/6.24 (BhG 1-2).
DEV (early stopping): Rām Bā 1 v21-79, KumSaṃ 1 v21-60. TRAIN: every other chapter on disk.
"""

from __future__ import annotations

import argparse
import json
import math
import pickle
import random
import sys
from collections import Counter
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "eval"))

from eval_dcs import align_words, prf, split_equal  # noqa: E402
from mayur import dcs, ranker  # noqa: E402
from mayur.segmenter import segment_line  # noqa: E402

FILES = ROOT / "data/dcs/sanskrit/dcs/data/conllu/files"
CACHE = ROOT / "data/derived/ranker_cache"
SOURCE = "trained on Digital Corpus of Sanskrit annotations (CC BY 4.0)"


def _held_out(path: Path) -> bool:
    n = path.name
    return ("Rāmāyaṇa-0000-" in n or n.startswith("Kumārasaṃbhava-0000-")
            or "MBh, 6, 23-" in n or "MBh, 6, 24-" in n)


def _lines(path: Path, lo: int = 0, hi: int = 10 ** 9) -> list[tuple[str, list[dict]]]:
    out = []
    for s in dcs.iter_sentences(path):
        if lo <= s["sent_counter"] <= hi and s["tokens"]:
            words = [{"form": t["form"], "lemma": t["lemma"], "compound_member": t["compound_member"]}
                     for t in s["tokens"]]
            out.append((dcs.compact(s["text"]), words))
    return out


def held_sets() -> dict[str, list[tuple[str, list[dict]]]]:
    ram = next(FILES.glob("Rāmāyaṇa/Rāmāyaṇa-0000-*"))
    kum = next(FILES.glob("Kumārasaṃbhava/Kumārasaṃbhava-0000-*"))
    bhg = sorted(p for p in FILES.glob("Mahābhārata/*") if "MBh, 6, 23-" in p.name or "MBh, 6, 24-" in p.name)
    return {"dev_ram": _lines(ram, 21, 79), "dev_kum": _lines(kum, 21, 60),
            "test_ram": _lines(ram, 1, 20), "test_kum": _lines(kum, 1, 20),
            "test_bhg": [x for p in bhg for x in _lines(p)]}


def train_lines(n: int, seed: int = 0) -> list[tuple[str, list[dict]]]:
    files = sorted(p for p in FILES.glob("*/*.conllu") if not _held_out(p))
    rng = random.Random(seed)
    rng.shuffle(files)
    pool: list = []
    for p in files[: max(40, n // 15)]:
        pool.extend(rng.sample(ls, min(len(ls), 30)) if (ls := _lines(p)) else [])
    rng.shuffle(pool)
    return pool[:n]


def _cand(item: tuple[str, list[dict], int]) -> list | None:
    line, gold, k = item
    try:
        seg = segment_line(line, k)
        splits = list(seg.splits)[:k]
    except Exception:  # noqa: BLE001 - a line the segmenter cannot handle is skipped
        return None
    rows = []
    for s in splits:
        ours = [(w.form, w.in_compound) for w in s.words]
        f1 = prf(len(align_words(ours, gold)), len(ours), len(gold))["f1"]
        rows.append((s, split_equal(ours, gold), f1))
    return [line, gold, rows]


def candidates(name: str, data: list, k: int, workers: int) -> list:
    path = CACHE / f"{name}_{len(data)}_{k}.pkl"
    if path.exists():
        return pickle.loads(path.read_bytes())
    with Pool(workers) as pool:
        out = [c for c in pool.map(_cand, [(l, g, k) for l, g in data], chunksize=4) if c]
    CACHE.mkdir(parents=True, exist_ok=True)
    path.write_bytes(pickle.dumps(out))
    return out


def tag_table(train: list) -> dict[str, float]:
    """log P(tag_i | tag_{i-1}) from TRAIN gold (add-one smoothed), tags via ranker.word_tag."""
    big, uni = Counter(), Counter()
    for _, gold, _ in train:
        seq = [ranker._START_TAG, *(ranker.word_tag(g["form"], g["compound_member"]) for g in gold), ranker._END_TAG]
        for a, b in zip(seq, seq[1:]):
            big[(a, b)] += 1
            uni[a] += 1
    v = len({t for pair in big for t in pair})
    table = {f"{a}|{b}": math.log((c + 1) / (uni[a] + v)) for (a, b), c in big.items()}
    table["<unk>"] = math.log(1 / (max(uni.values()) + v))
    return table


def featurize(cands: list, table: dict) -> list:
    return [[(ranker.features(line, s, table), eq, f1) for s, eq, f1 in rows] for line, _, rows in cands]


def scaling(lists: list) -> tuple[dict, dict]:
    sums, sq, n = Counter(), Counter(), 0
    for rows in lists:
        for f, _, _ in rows:
            n += 1
            for k, x in f.items():
                sums[k] += x
                sq[k] += x * x
    mean = {k: sums[k] / n for k in sums}
    std = {k: math.sqrt(max(sq[k] / n - mean[k] ** 2, 1e-9)) for k in sums}
    return mean, std


def metrics(lists: list, model: dict | None) -> dict[str, float]:
    exact = f1 = oracle = 0.0
    for rows in lists:
        if not rows:
            continue
        idx = 0 if model is None else max(range(len(rows)), key=lambda i: (ranker.score(rows[i][0], model), -i))
        exact += rows[idx][1]
        f1 += rows[idx][2]
        oracle += any(r[1] for r in rows)
    n = max(1, len(lists))
    return {"exact": exact / n, "f1": f1 / n, "oracle": oracle / n, "n": len(lists)}


def perceptron(train: list, dev: list, mean: dict, std: dict, epochs: int) -> tuple[dict, float]:
    w, total, stamp, t = Counter(), Counter(), Counter(), 0
    model = {"weights": w, "mean": mean, "std": std}
    best, best_w = -1.0, {}
    norm = [[{k: (v - mean[k]) / std[k] for k, v in f.items()} for f, _, _ in rows] for rows in train]
    targets = [max(range(len(rows)), key=lambda i: (rows[i][1], rows[i][2], -i)) if rows else 0 for rows in train]
    order = list(range(len(train)))
    rng = random.Random(1)
    for _ in range(epochs):
        rng.shuffle(order)
        for i in order:
            rows = norm[i]
            if len(rows) < 2:
                continue
            t += 1
            pred = max(range(len(rows)), key=lambda j: (sum(w[k] * v for k, v in rows[j].items()), -j))
            gold = targets[i]
            if pred != gold:
                for k in set(rows[pred]) | set(rows[gold]):
                    total[k] += (t - stamp[k]) * w[k]
                    stamp[k] = t
                    w[k] += rows[gold].get(k, 0.0) - rows[pred].get(k, 0.0)
        avg = {k: (total[k] + (t - stamp[k]) * w[k]) / max(t, 1) for k in w}
        score = metrics(dev, {"weights": avg, "mean": mean, "std": std})["exact"]
        print(f"  epoch dev exact {score:.3f}")
        if score > best:
            best, best_w = score, avg
    model["weights"] = best_w
    return best_w, best


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lines", type=int, default=5000)
    ap.add_argument("--k", type=int, default=50)
    ap.add_argument("--epochs", type=int, default=10)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args(argv)
    held = {name: candidates(name, d, a.k, a.workers) for name, d in held_sets().items()}
    train_c = candidates("train", train_lines(a.lines), a.k, a.workers)
    table = tag_table(train_c)
    train_f = featurize(train_c, table)
    held_f = {n: featurize(c, table) for n, c in held.items()}
    for kk in (1, 5, 10, 20, a.k):
        cov = metrics([rows[:kk] for rows in train_f], None)["oracle"]
        print(f"oracle coverage TRAIN @K={kk}: {cov:.3f}")
    mean, std = scaling(train_f)
    dev = held_f["dev_ram"] + held_f["dev_kum"]
    weights, _ = perceptron(train_f, dev, mean, std, a.epochs)
    model = {"source": SOURCE, "k": a.k, "train_lines": len(train_f), "weights": weights,
             "mean": mean, "std": std, "tag_bigram": table}
    base_dev, new_dev = metrics(dev, None), metrics(dev, model)
    model["enabled"] = new_dev["exact"] > base_dev["exact"]
    for n, rows in held_f.items():
        b, r = metrics(rows, None), metrics(rows, model)
        print(f"{n:9s} n={b['n']:4d} exact {b['exact']:.3f} -> {r['exact']:.3f}  "
              f"F1 {b['f1']:.3f} -> {r['f1']:.3f}  oracle@{a.k} {b['oracle']:.3f}")
    print(f"DEV overall exact {base_dev['exact']:.3f} -> {new_dev['exact']:.3f}; enabled={model['enabled']}")
    ranker.MODEL_FILE.parent.mkdir(exist_ok=True)
    ranker.MODEL_FILE.write_text(json.dumps(model, ensure_ascii=False, sort_keys=True, indent=0), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
