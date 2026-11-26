"""Train the in-lattice decoder (mayur/decoder.py): averaged structured perceptron, gold path forced.

    python scripts/train_decoder.py [--lines 6000] [--epochs 3] [--dev-per-text 20] [--unknown]

TRAIN = split_files("train") (stratified by text). DEV = split_files("dev") + dev_pool sample
(early stopping on DEV lenient word F1). TEST = split_files("test") (report only). sealed_test is
never read. Streaming: each line's compact lattice is built once and written to pickle shards in
data/derived/decoder_cache/; epochs stream the shards, so memory stays bounded.
"""

from __future__ import annotations

import argparse
import json
import pickle
import random
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable, Iterator

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "eval"))

from eval_dcs import lcs_pairs, prf, split_equal, word_matches  # noqa: E402
from decoder_data import code_key, digest, held_sets, prefix_table, tag_table, train_lines  # noqa: E402
from mayur import decoder, lexicon, ud  # noqa: E402
from mayur import decoder_words as dw  # noqa: E402

CACHE = ROOT / "data/derived/decoder_cache"
AUDIT = ROOT / "data/derived/audit_decoder_missing.txt"
SOURCE = "trained on Digital Corpus of Sanskrit annotations (CC BY 4.0)"
CHUNK = 200


def _morphs(form: str, samasa: bool) -> tuple:
    return (lexicon.stems(form) if samasa else ()) + lexicon.padas(form)


def matches(form: str, samasa: bool, g: dict, lenient: bool) -> bool:
    """Same compound-member flag, and forms agree after ``normalize`` (strict), or (lenient) any
    analysis has the gold lemma. The flag matters (a member edge for तथा is not the corpus's free
    तथा), except for an indeclinable followed by another word (``either``: glued prefixes स-, सु-,
    अन्- are free words in the corpus but members in our lattice)."""
    if samasa != bool(g["compound_member"]) and not g.get("either"):
        return False
    lemma = dw.lemma_of(form, samasa)
    if word_matches(form, g["form"], g["lemma"], g["compound_member"], lemma, False):
        return True
    return lenient and any(ud.same_lemma(m, g["lemma"], g.get("upos", "")) for m in _morphs(form, samasa))


def oracle(g, match: tuple, n_gold: int, skip_unknown: bool = False) -> tuple[tuple[int, ...], float, bool]:
    """Lattice path with the most gold words matched in order (LCS); (path, F1, gold exactly in lattice)."""
    best: dict[int, dict[int, tuple]] = {0: {0: (0, 0, -1, -1)}}
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
                if skip_unknown and g.edges[eid].unknown:
                    continue
                dst = g.edges[eid].dst
                for g2, m2 in [(gi, m)] + [(j + 1, m + 1) for j in match[eid] if j >= gi]:
                    cur = best.setdefault(dst, {}).get(g2)
                    if cur is None or (m2, -(n + 1)) > (cur[0], -cur[1]):
                        best[dst][g2] = (m2, n + 1, eid, gi)
    ends = [(gi, v) for (node, gi), v in back.items() if node == g.end]
    if not ends:
        return (), 0.0, False
    gi, (m, n, _, _) = max(ends, key=lambda t: prf(t[1][0], t[1][1], n_gold)["f1"])
    path, node, cur_g = [], g.end, gi
    while node != 0:
        _, _, eid, src_g = back[(node, cur_g)]
        path.append(eid)
        node, cur_g = g.edges[eid].src, src_g
    return tuple(reversed(path)), prf(m, n, n_gold)["f1"], m == n == n_gold


def _item(line: str, gold: list[dict], table: dict) -> dict | None:
    try:
        lat = decoder.lattice(line, unknown=UNKNOWN)
        if lat is None:
            return {"line": line, "gold": gold, "g": None}
        g, _ = decoder.build_graph(lat, table, PREFIX)
    except (Exception, MemoryError):  # noqa: BLE001 - a line the lattice cannot handle is skipped
        return None
    match = tuple(tuple(i for i, gw in enumerate(gold) if matches(e.form, e.samasa, gw, True)) for e in g.edges)
    path, f1, exact = oracle(g, match, len(gold))
    bpath, bf1, bexact = oracle(g, match, len(gold), skip_unknown=True)
    present = {j for m, e in zip(match, g.edges) if not e.unknown for j in m}
    return {"line": line, "gold": gold, "g": g, "target": path, "oracle_f1": f1, "covered": exact,
            "target_base": bpath, "oracle_f1_base": bf1, "covered_base": bexact,
            "missing": [w["form"] for j, w in enumerate(gold) if j not in present]}


UNKNOWN = False  # unknown-word edges (round 3: no DEV gain, off by default)
PREFIX: dict = {}


def shards(name: str, data: list, table: dict) -> list[Path]:
    """Pickle shards of compact lattices. The file name carries a key over the lines, the lattice and
    feature code, the corpus tables and the tag/prefix tables, so a stale shard is never loaded."""
    base = digest(code_key(), sorted(table.items()), sorted((k, sorted(v.items())) for k, v in PREFIX.items()),
                  UNKNOWN)
    out = []
    for c in range(0, len(data), CHUNK):
        part = data[c:c + CHUNK]
        path = CACHE / f"{name}_{c}_{digest(base, [l for l, _ in part])}.pkl"
        if not path.exists():
            items = [x for x in (_item(l, g, table) for l, g in part) if x is not None]
            CACHE.mkdir(parents=True, exist_ok=True)
            path.write_bytes(pickle.dumps(items))
            print(f"  {name}: {c + len(part)} lines", flush=True)
        out.append(path)
    return out


def items(paths: list[Path], rng: random.Random | None = None) -> Iterator[dict]:
    order = list(paths)
    if rng:
        rng.shuffle(order)
    for p in order:
        xs = pickle.loads(p.read_bytes())
        if rng:
            rng.shuffle(xs)
        yield from xs


def stat_tables(train: list[Path]) -> dict:
    """Sound-level boundary counts and junction-class counts from TRAIN lines whose gold is in the lattice."""
    bnd: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
    junc: dict[str, Counter] = defaultdict(Counter)
    for it in items(train):
        g = it["g"]
        if g is None or not it["covered"]:
            continue
        for eid in it["target"]:
            e = g.edges[eid]
            for p in range(e.start + 1, e.end):
                for key in decoder.boundary_keys(g.text, g.spaces, p):
                    bnd[key][0] += 1
            if e.kind != "end":
                for key in decoder.boundary_keys(g.text, g.spaces, e.end):
                    bnd[key][2 if e.kind == "cpd" else 1] += 1
                junc[e.jsurf][e.jcls] += 1
    return {"boundary": {k: v for k, v in bnd.items() if sum(v) >= decoder.BOUNDARY_MIN},
            "junction": {s: dict(c) for s, c in junc.items() if sum(c.values()) >= 2}}


def scores(g, path: tuple, gold: list[dict]) -> tuple[float, float, bool]:
    ours = [(g.edges[i].form, g.edges[i].samasa) for i in path]
    strict = len(lcs_pairs(ours, gold, lambda o, w: matches(o[0], o[1], w, False)))
    lenient = len(lcs_pairs(ours, gold, lambda o, w: matches(o[0], o[1], w, True)))
    exact = split_equal([(f, s, dw.lemma_of(f, s)) for f, s in ours], gold)
    return prf(strict, len(ours), len(gold))["f1"], prf(lenient, len(ours), len(gold))["f1"], exact


def evaluate(paths: list[Path], w: dict, tid: int, tables: dict) -> dict[str, float]:
    tot = Counter()
    for it in items(paths):
        tot["n"] += 1
        g = it["g"]
        if g is None:
            continue
        res = decoder.viterbi(g, w, tid, 1, extra=decoder.dynamic_features(g, tables))
        if res:
            s, l, x = scores(g, res[0][1], it["gold"])
            tot["strict"], tot["lenient"], tot["exact"] = tot["strict"] + s, tot["lenient"] + l, tot["exact"] + x
    n = max(1, tot["n"])
    return {"strict": tot["strict"] / n, "lenient": tot["lenient"] / n, "exact": tot["exact"] / n, "n": tot["n"]}


def train(train_p: list[Path], dev_p: list[Path], tid: int, tables: dict, epochs: int,
          allow: Callable[[str], bool], target: str = "target", fixed: dict | None = None) -> tuple[dict, dict]:
    fixed = fixed or {}
    w: Counter = Counter({"base": 1.0, **fixed})
    total, stamp, t = Counter(), Counter(), 0
    best, best_w, rng = None, dict(w), random.Random(1)
    for ep in range(epochs):
        for it in items(train_p, rng):
            g = it["g"]
            if g is None or not it[target]:
                continue
            t += 1
            extra = decoder.dynamic_features(g, tables)
            pred = decoder.viterbi(g, w, tid, 1, extra=extra)
            if not pred or pred[0][1] == it[target]:
                continue
            fg = decoder.path_features(g, it[target], tid, extra)
            fp = decoder.path_features(g, pred[0][1], tid, extra)
            for k in set(fg) | set(fp):
                if not allow(k) or k in fixed:
                    continue
                total[k] += (t - stamp[k]) * w[k]
                stamp[k] = t
                w[k] += fg.get(k, 0.0) - fp.get(k, 0.0)
        avg = {k: (total[k] + (t - stamp[k]) * w[k]) / t for k in w if w[k] or total[k]}
        avg.update(fixed)
        m = evaluate(dev_p, avg, tid, tables)
        print(f"  epoch {ep + 1}: DEV strict {m['strict']:.4f} lenient {m['lenient']:.4f} exact {m['exact']:.3f}",
              flush=True)
        if best is None or m["lenient"] > best["lenient"]:
            best, best_w = m, avg
    return best_w, best


def audit(dev_p: list[Path]) -> tuple[float, float, list[str]]:
    n = covered = 0
    f1s, reasons, examples = 0.0, Counter(), []
    for it in items(dev_p):
        n += 1
        if it["g"] is None:
            reasons["no lattice"] += 1
            continue
        covered += it["covered"]
        f1s += it["oracle_f1"]
        reasons["(without unknown edges) covered"] += it.get("covered_base", 0)
        reasons["(without unknown edges) oracle F1 x100"] += round(100 * it.get("oracle_f1_base", 0))
        if not it["covered_base"]:
            why = "unknown word (no edge)" if it["missing"] else "junction / path (all words have edges)"
            reasons[why] += 1
            examples.append(f"{why}\t{it['line']}\tgold: {' '.join(x['form'] for x in it['gold'])}"
                            f"\tmissing: {' '.join(it['missing'])}")
    return covered / max(1, n), f1s / max(1, n), [f"{k}: {v}" for k, v in reasons.most_common()] + [""] + examples


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lines", type=int, default=6000)
    ap.add_argument("--epochs", type=int, default=5)
    ap.add_argument("--dev-per-text", type=int, default=20)
    ap.add_argument("--build-only", action="store_true", help="only build the lattice shards")
    ap.add_argument("--unknown", action="store_true", help="offer unknown-word edges (round 3: no gain)")
    ap.add_argument("--table-lines", type=int, default=40000, help="TRAIN lines for the prefix table")
    a = ap.parse_args(argv)
    global UNKNOWN, PREFIX
    UNKNOWN = a.unknown
    t0 = time.time()
    raw_train = train_lines(a.lines, seed=7)
    table = tag_table(raw_train)
    PREFIX = prefix_table(train_lines(a.table_lines, seed=11))
    print(f"prefix table: {len(PREFIX)} prefixes {sorted(PREFIX)[:20]}", flush=True)
    tid = decoder.register_table(table, PREFIX)
    held = {n: shards(n, d, table) for n, d in held_sets(a.dev_per_text).items()}
    dev_p = [p for n, ps in held.items() if n.startswith("dev_") for p in ps]
    cov, ora, lines = audit(dev_p)
    AUDIT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"DEV coverage (gold path in lattice) {cov:.3f}; oracle-path F1 {ora:.4f}; {lines[:3]}", flush=True)
    train_p = shards("train", raw_train, table)
    n_tr = sum(1 for it in items(train_p) if it["g"] is not None)
    n_miss = sum(1 for it in items(train_p) if it["g"] is not None and not it["covered"])
    print(f"TRAIN lattices {n_tr}; gold not in lattice (max-overlap target) {n_miss}  [{time.time() - t0:.0f}s]")
    if a.build_only:
        return 0
    stats = stat_tables(train_p)
    print(f"boundary contexts {len(stats['boundary'])}, junction surfaces {len(stats['junction'])}", flush=True)
    full = {"tag_bigram": table, "prefix": PREFIX, **stats}
    fixed = {} if UNKNOWN else {"unknown": -1e6}
    configs = {"without neural boundary": full}
    if decoder.neural_available():
        configs["with neural boundary"] = {**full, "neural": True}
    else:
        print("WARNING: neural boundary model unavailable: training without it", flush=True)
    results = {}
    for name, tabs in configs.items():
        print(f"config: {name}", flush=True)
        results[name] = train(train_p, dev_p, tid, tabs, a.epochs, lambda k: True, "target", fixed)
    for name, (_, m) in results.items():
        print(f"ABLATION {name:26s} DEV strict {m['strict']:.4f} lenient {m['lenient']:.4f} exact {m['exact']:.3f}")
    base = {"base": 1.0, "unknown": -1e6}
    b_dev = evaluate(dev_p, base, tid, {})
    for name, (w, m) in results.items():
        tabs = configs[name]
        model = {"source": SOURCE, "enabled": m["lenient"] > b_dev["lenient"], "train_lines": n_tr,
                 "weights": {k: v for k, v in w.items() if v}, "config": name, "unknown_edges": UNKNOWN,
                 "neural": bool(tabs.get("neural")), "score_scale": 4 * median_gap(dev_p, w, tid, tabs),
                 **tabs, "dev": {"before": b_dev, "after": m, "coverage": cov, "oracle_f1": ora}}
        path = decoder.MODEL_FILE if name == max(results, key=lambda n: results[n][1]["lenient"]) else None
        if not tabs.get("neural"):
            decoder.FALLBACK_FILE.write_text(json.dumps(model, ensure_ascii=False, sort_keys=True), encoding="utf-8")
        if path:
            path.write_text(json.dumps(model, ensure_ascii=False, sort_keys=True), encoding="utf-8")
            print(f"chosen: {name}; score_scale {model['score_scale']:.1f}; enabled={model['enabled']}")
            for hname, ps in held.items():
                b, r = evaluate(ps, base, tid, {}), evaluate(ps, w, tid, tabs)
                print(f"{hname[:26]:26s} n={b['n']:4d} strict {b['strict']:.4f} -> {r['strict']:.4f}  lenient "
                      f"{b['lenient']:.4f} -> {r['lenient']:.4f}  exact {b['exact']:.3f} -> {r['exact']:.3f}",
                      flush=True)
            print(f"DEV all strict {b_dev['strict']:.4f} -> {m['strict']:.4f}  lenient {b_dev['lenient']:.4f} -> "
                  f"{m['lenient']:.4f}  exact {b_dev['exact']:.3f} -> {m['exact']:.3f}")
    print(f"wrote {decoder.MODEL_FILE} and {decoder.FALLBACK_FILE} [{time.time() - t0:.0f}s]")
    return 0


def median_gap(paths: list[Path], w: dict, tid: int, tables: dict) -> float:
    """Median score gap between the best and second-best distinct word sequences on DEV."""
    gaps = []
    for it in items(paths):
        g = it["g"]
        if g is None:
            continue
        res = decoder.order_alternatives(g, decoder.viterbi(g, w, tid, 6, extra=decoder.dynamic_features(g, tables)), 2)
        if len(res) == 2:
            gaps.append(res[0][0] - res[1][0])
    gaps.sort()
    return gaps[len(gaps) // 2] if gaps else 1.0


if __name__ == "__main__":
    raise SystemExit(main())
