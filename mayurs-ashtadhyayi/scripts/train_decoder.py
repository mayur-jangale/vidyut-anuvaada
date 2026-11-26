"""Train the in-lattice decoder (mayur/decoder.py): averaged structured perceptron, gold path forced.

    python scripts/train_decoder.py [--lines 3000] [--epochs 6] [--dev-per-text 20]

TRAIN = split_files("train") (stratified by text). DEV = split_files("dev") + dev_pool sample
(early stopping). TEST = split_files("test") (report only). sealed_test is never read.
One process; compact lattices are cached in data/derived/decoder_cache/ in chunks.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pickle
import random
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "eval"))

from eval_dcs import lcs_pairs, normalize, prf, split_equal, word_matches  # noqa: E402
from mayur import decoder, ranker, ud  # noqa: E402
from train_ranker import held_sets, tag_table, train_lines  # noqa: E402

CACHE = ROOT / "data/derived/decoder_cache"
AUDIT = ROOT / "data/derived/audit_decoder_missing.txt"
SOURCE = "trained on Digital Corpus of Sanskrit annotations (CC BY 4.0)"
CHUNK = 250


def _canon(x: str) -> str:
    fn = getattr(ud, "canonical_lemma", None)
    return normalize(fn(x) if fn else x)


def matches(form: str, samasa: bool, g: dict, lenient: bool) -> bool:
    lemma = ranker.lemma_of(form, samasa)
    if word_matches(form, g["form"], g["lemma"], g["compound_member"], lemma, lenient):
        return True
    return lenient and bool(lemma) and _canon(lemma) == _canon(g["lemma"])


def _graph_item(line: str, gold: list[dict], table: dict) -> tuple | None:
    try:
        lat = decoder.lattice(line)
        if lat is None:
            return (line, gold, None, None)
        g, _ = decoder.build_graph(lat, table)
    except (Exception, MemoryError):  # noqa: BLE001 - a line the lattice cannot handle is skipped
        return None
    match = tuple(tuple(i for i, gw in enumerate(gold) if matches(e.form, e.samasa, gw, True)) for e in g.edges)
    return (line, gold, g, match)


def graphs(name: str, data: list, table: dict) -> list:
    code = [p.stat().st_mtime_ns for p in sorted((ROOT / "mayur").glob("*.py")) if p.name != "decoder.py"]
    out = []
    for c in range(0, len(data), CHUNK):
        part = data[c:c + CHUNK]
        key = hashlib.sha1(repr(([l for l, _ in part], code, sorted(table.items())[:50])).encode()).hexdigest()[:12]
        path = CACHE / f"{name}_{c}_{key}.pkl"
        if path.exists():
            out.extend(pickle.loads(path.read_bytes()))
            continue
        items = [x for x in (_graph_item(l, g, table) for l, g in part) if x is not None]
        CACHE.mkdir(parents=True, exist_ok=True)
        path.write_bytes(pickle.dumps(items))
        out.extend(items)
        print(f"  {name}: {len(out)} lattices", flush=True)
    return out


def oracle(g, match: tuple, n_gold: int) -> tuple[tuple[int, ...], float, bool]:
    """Lattice path with the most gold words matched in order (LCS); (path, F1, gold exactly in lattice)."""
    best: dict[int, dict[int, tuple]] = {0: {0: (0, 0, -1, -1)}}  # node -> gold idx -> (m, n, eid, src_g)
    back: dict[tuple[int, int], tuple] = {}
    for node in g.order:
        here = best.pop(node, None)
        if here is None:
            continue
        for gi, val in here.items():
            back[(node, gi)] = val
        if node == g.end:
            break
        for gi, (m, n, _, _) in here.items():
            for eid in g.out[node]:
                e = g.edges[eid]
                opts = [(gi, m)] + [(j + 1, m + 1) for j in match[eid] if j >= gi]
                for g2, m2 in opts:
                    cur = best.setdefault(e.dst, {}).get(g2)
                    cand = (m2, n + 1, eid, gi)
                    if cur is None or (m2, -(n + 1)) > (cur[0], -cur[1]):
                        best[e.dst][g2] = cand
    ends = [(gi, v) for (node, gi), v in back.items() if node == g.end]
    if not ends:
        return (), 0.0, False
    gi, (m, n, _, _) = max(ends, key=lambda t: prf(t[1][0], t[1][1], n_gold)["f1"])
    path, node, cur_g = [], g.end, gi
    while node != 0:
        m_, n_, eid, src_g = back[(node, cur_g)]
        path.append(eid)
        node, cur_g = g.edges[eid].src, src_g
    return tuple(reversed(path)), prf(m, n, n_gold)["f1"], m == n == n_gold


def scores(g, path: tuple, gold: list[dict]) -> tuple[float, float, bool]:
    ours = [(g.edges[i].form, g.edges[i].samasa) for i in path]
    strict = len(lcs_pairs(ours, gold, lambda o, w: matches(o[0], o[1], w, False)))
    lenient = len(lcs_pairs(ours, gold, lambda o, w: matches(o[0], o[1], w, True)))
    exact = split_equal([(f, s, ranker.lemma_of(f, s)) for f, s in ours], gold)
    return prf(strict, len(ours), len(gold))["f1"], prf(lenient, len(ours), len(gold))["f1"], exact


def evaluate(items: list, w: dict, tid: int) -> dict[str, float]:
    tot = Counter()
    for _, gold, g, _ in items:
        tot["n"] += 1
        if g is None:
            continue
        res = decoder.viterbi(g, w, tid, 1)
        if res:
            s, l, x = scores(g, res[0][1], gold)
            tot["strict"] += s
            tot["lenient"] += l
            tot["exact"] += x
    n = max(1, tot["n"])
    return {"strict": tot["strict"] / n, "lenient": tot["lenient"] / n, "exact": tot["exact"] / n, "n": tot["n"]}


def train(items: list, dev: list, tid: int, epochs: int) -> dict[str, float]:
    targets = [(g, oracle(g, m, len(gold))[0]) for _, gold, g, m in items if g is not None]
    targets = [(g, p) for g, p in targets if p]
    w: Counter = Counter({"base": 1.0})
    total, stamp, t = Counter(), Counter(), 0
    best, best_w, rng = -1.0, dict(w), random.Random(1)
    for ep in range(epochs):
        rng.shuffle(targets)
        for g, gold_path in targets:
            t += 1
            pred = decoder.viterbi(g, w, tid, 1)
            if not pred or pred[0][1] == gold_path:
                continue
            fg, fp = decoder.path_features(g, gold_path, tid), decoder.path_features(g, pred[0][1], tid)
            for k in set(fg) | set(fp):
                total[k] += (t - stamp[k]) * w[k]
                stamp[k] = t
                w[k] += fg.get(k, 0.0) - fp.get(k, 0.0)
        avg = {k: (total[k] + (t - stamp[k]) * w[k]) / t for k in w}
        m = evaluate(dev, avg, tid)
        print(f"  epoch {ep + 1}: DEV strict F1 {m['strict']:.4f} lenient {m['lenient']:.4f} exact {m['exact']:.3f}",
              flush=True)
        if m["strict"] > best:
            best, best_w = m["strict"], avg
    return best_w


def audit(items: list) -> tuple[float, float, list[str]]:
    covered, f1s, reasons, examples = 0, 0.0, Counter(), []
    for line, gold, g, match in items:
        if g is None:
            reasons["no lattice"] += 1
            continue
        path, f1, exact = oracle(g, match, len(gold))
        covered += exact
        f1s += f1
        if not exact:
            present = {j for m in match for j in m}
            missing = [gw["form"] for j, gw in enumerate(gold) if j not in present]
            why = "unknown word (no edge)" if missing else "junction / path (all words have edges)"
            reasons[why] += 1
            if len(examples) < 200:
                examples.append(f"{why}\t{line}\tgold: {' '.join(x['form'] for x in gold)}\tmissing: {' '.join(missing)}")
    n = max(1, len(items))
    head = [f"{k}: {v}" for k, v in reasons.most_common()]
    return covered / n, f1s / n, head + [""] + examples


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lines", type=int, default=3000)
    ap.add_argument("--epochs", type=int, default=6)
    ap.add_argument("--dev-per-text", type=int, default=20)
    a = ap.parse_args(argv)
    t0 = time.time()
    raw_train = train_lines(a.lines, seed=7)
    held_raw = held_sets(a.dev_per_text)
    table_src = [(l, g, None) for l, g in raw_train]
    table = tag_table(table_src)
    tid = decoder.register_table(table)
    held = {n: graphs(n, d, table) for n, d in held_raw.items()}
    dev = [x for n, xs in held.items() if n.startswith("dev_") for x in xs]
    cov, ora, lines = audit(dev)
    AUDIT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"DEV lattice coverage (gold path in lattice) {cov:.3f}; oracle-path F1 {ora:.4f}; reasons: {lines[:3]}")
    tr = graphs("train", raw_train, table)
    missing = sum(1 for _, gold, g, m in tr if g is None or not oracle(g, m, len(gold))[2])
    print(f"TRAIN lattices {len(tr)}; gold not in lattice (max-overlap target used) {missing}  [{time.time() - t0:.0f}s]")
    w = train(tr, dev, tid, a.epochs)
    base = {"base": 1.0}
    b_dev, n_dev = evaluate(dev, base, tid), evaluate(dev, w, tid)
    on = n_dev["strict"] > b_dev["strict"]
    for name, xs in held.items():
        b, r = evaluate(xs, base, tid), evaluate(xs, w, tid)
        print(f"{name[:26]:26s} n={b['n']:4d} strict {b['strict']:.4f} -> {r['strict']:.4f}  lenient "
              f"{b['lenient']:.4f} -> {r['lenient']:.4f}  exact {b['exact']:.3f} -> {r['exact']:.3f}")
    print(f"DEV all strict {b_dev['strict']:.4f} -> {n_dev['strict']:.4f}  lenient {b_dev['lenient']:.4f} -> "
          f"{n_dev['lenient']:.4f}  exact {b_dev['exact']:.3f} -> {n_dev['exact']:.3f}; enabled={on}")
    model = {"source": SOURCE, "enabled": on, "train_lines": len(tr), "weights": w, "tag_bigram": table,
             "dev": {"before": b_dev, "after": n_dev, "coverage": cov, "oracle_f1": ora}}
    decoder.MODEL_FILE.write_text(json.dumps(model, ensure_ascii=False, sort_keys=True, indent=0), encoding="utf-8")
    print(f"wrote {decoder.MODEL_FILE} [{time.time() - t0:.0f}s]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
