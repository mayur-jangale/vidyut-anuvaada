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
            or "BhaGī 1-" in n or "BhaGī 2-" in n)


def _text_of(entry: dict) -> str:
    return Path(entry["file"]).parent.name


def _lines(entries: list[dict], limit: int | None = None, seed: int = 0) -> list[tuple[str, list[dict]]]:
    return [(g["compact"], [{"form": w["form"], "lemma": w["lemma"], "compound_member": w["compound_member"]}
                            for w in g["words"]])
            for g in dcs.gold_lines(entries, limit=limit, seed=seed) if g["words"]]


def held_sets(per_pool_text: int = 60) -> dict[str, list[tuple[str, list[dict]]]]:
    """DEV per text (old DEV sets + dev_pool sample) and TEST per text. Never touches sealed_test."""
    out: dict[str, list] = {}
    for split, prefix, limit in (("dev", "dev", None), ("dev_pool", "dev", per_pool_text), ("test", "test", None)):
        by_text: dict[str, list[dict]] = {}
        for e in dcs.split_files(split):
            by_text.setdefault(_text_of(e), []).append(e)
        for text, es in sorted(by_text.items()):
            out.setdefault(f"{prefix}_{text}", []).extend(_lines(es, limit))
    return out


def train_lines(n: int, seed: int = 0) -> list[tuple[str, list[dict]]]:
    """``n`` TRAIN half-verses stratified by text (equal share per text, sampled across its chapters)."""
    by_text: dict[str, list[dict]] = {}
    for e in dcs.split_files("train"):
        if not _held_out(Path(e["file"])):
            by_text.setdefault(_text_of(e), []).append(e)
    rng = random.Random(seed)
    share = max(1, n // max(1, len(by_text)))
    pool: list = []
    for text, es in sorted(by_text.items()):
        rng.shuffle(es)
        pool.extend(_lines(es[: max(3, share // 20)], limit=share, seed=seed))
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
        ours = [(w.form, w.in_compound, ranker.lemma_of(w.form, w.in_compound)) for w in s.words]
        f1 = prf(len(align_words(ours, gold)), len(ours), len(gold))["f1"]
        rows.append((s, split_equal(ours, gold), f1))
    return [line, gold, rows]


def candidates(name: str, data: list, k: int, workers: int) -> list:
    import hashlib
    code = [p.stat().st_mtime_ns for p in sorted((ROOT / "mayur").glob("*.py")) if p.name != "ranker.py"]
    key = hashlib.sha1(repr(([l for l, _ in data], code)).encode()).hexdigest()[:10]
    path = CACHE / f"{name}_{len(data)}_{k}_{key}.pkl"
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
    exact = f1 = oracle = oracle_f1 = 0.0
    for rows in lists:
        if not rows:
            continue
        idx = 0 if model is None else max(range(len(rows)), key=lambda i: (ranker.score(rows[i][0], model), -i))
        exact += rows[idx][1]
        f1 += rows[idx][2]
        oracle += any(r[1] for r in rows)
        oracle_f1 += max(r[2] for r in rows)
    n = max(1, len(lists))
    return {"exact": exact / n, "f1": f1 / n, "oracle": oracle / n, "oracle_f1": oracle_f1 / n, "n": len(lists)}


def perceptron(train: list, dev: list, mean: dict, std: dict, epochs: int) -> tuple[dict, float]:
    w, total, stamp, t = Counter(), Counter(), Counter(), 0
    model = {"weights": w, "mean": mean, "std": std}
    best, best_w = -1.0, {}
    norm = [[{k: (v - mean[k]) / std[k] for k, v in f.items()} for f, _, _ in rows] for rows in train]
    targets = [max(range(len(rows)), key=lambda i: (rows[i][2], rows[i][1], -i)) if rows else 0 for rows in train]
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
        dm = metrics(dev, {"weights": avg, "mean": mean, "std": std})
        score = dm["f1"]
        print(f"  epoch dev F1 {score:.4f} exact {dm['exact']:.3f}")
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
        cov = metrics([rows[:kk] for rows in train_f], None)
        print(f"oracle TRAIN @K={kk}: exact {cov['oracle']:.3f}  best-F1 {cov['oracle_f1']:.4f}")
    mean, std = scaling(train_f)
    dev = [r for n, rows in held_f.items() if n.startswith("dev_") for r in rows]
    weights, _ = perceptron(train_f, dev, mean, std, a.epochs)
    model = {"source": SOURCE, "k": a.k, "train_lines": len(train_f), "weights": weights,
             "mean": mean, "std": std, "tag_bigram": table}
    base_dev, new_dev = metrics(dev, None), metrics(dev, model)
    model["enabled"] = new_dev["f1"] > base_dev["f1"]
    for n, rows in held_f.items():
        b, r = metrics(rows, None), metrics(rows, model)
        print(f"{n[:28]:28s} n={b['n']:4d} exact {b['exact']:.3f} -> {r['exact']:.3f}  "
              f"F1 {b['f1']:.4f} -> {r['f1']:.4f}  oracle@{a.k} exact {b['oracle']:.3f} F1 {b['oracle_f1']:.4f}")
    print(f"DEV overall exact {base_dev['exact']:.3f} -> {new_dev['exact']:.3f}  F1 {base_dev['f1']:.4f} -> "
          f"{new_dev['f1']:.4f}  oracle F1 {base_dev['oracle_f1']:.4f}; enabled={model['enabled']}")
    ranker.MODEL_FILE.parent.mkdir(exist_ok=True)
    ranker.MODEL_FILE.write_text(json.dumps(model, ensure_ascii=False, sort_keys=True, indent=0), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
