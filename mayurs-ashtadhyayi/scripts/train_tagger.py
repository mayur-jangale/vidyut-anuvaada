"""Train the lexicalised analysis tagger (averaged perceptron, beam search over whole verses).

    python scripts/train_tagger.py [--max-words 150000] [--epochs 4] [--eval-only]

TRAIN: whole verses from ``mayur.dcs.split_files("train")``, stratified over all texts.
DEV:   ``split_files("dev")`` plus a fixed sample of ``split_files("dev_pool")`` (early stopping).
TEST (report only): ``split_files("test")``. The sealed_test pool is never read.
Writes mayur/models/tagger.json.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Callable, Optional, Sequence

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from mayur import dcs, lexicon, shabdabodha, tagger, tagger_siblings, terms, ud  # noqa: E402
from mayur.model import Word  # noqa: E402

MODEL = ROOT / "mayur/models/tagger.json"
SIBLINGS = True  # candidates of sibling pada forms (मूढा / मूढास्) at the eligible words
TABLES: dict = {}  # corpus-structure tables of the model being trained or evaluated
_GENDER = {v: k for k, v in terms.UD_GENDER.items()}


def build_tables(items, min_count: int = 3, acc: Optional[tuple] = None) -> dict:
    """From TRAIN gold: P(gender | lemma), P(gender | last two sounds of the lemma), and per verb lemma
    the share of its half-verses with an accusative / a dative."""
    gl, gs, verbs = acc if acc is not None else ({}, {}, {})
    for it in items:
        for line in sorted({w.line for w in it["words"]}):
            toks = [t for t, w in zip(it["toks"], it["words"]) if w.line == line and not t["compound_member"]]
            cases = {t["feats"].get("Case") for t in toks}
            for t in toks:
                lem = ud.canonical_lemma(t["lemma"])
                g = _GENDER.get(t["feats"].get("Gender", ""))
                if g and t["upos"] == "NOUN":
                    gl.setdefault(lem, Counter())[g] += 1
                    gs.setdefault("".join(tagger._sounds(lem)[-2:]), Counter())[g] += 1
                if t["upos"] == "VERB" and "Mood" in t["feats"]:
                    c = verbs.setdefault(lem, Counter())
                    c["n"] += 1
                    c["acc"] += "Acc" in cases
                    c["dat"] += "Dat" in cases
    norm = lambda c: {k: round(v / sum(c.values()), 2) for k, v in c.items()}
    return {"g": {k: norm(c) for k, c in gl.items() if sum(c.values()) >= min_count},
            "gs": {k: norm(c) for k, c in gs.items() if sum(c.values()) >= 20},
            "acc": {k: round(c["acc"] / c["n"], 2) for k, c in verbs.items() if c["n"] >= min_count},
            "dat": {k: round(c["dat"] / c["n"], 2) for k, c in verbs.items() if c["n"] >= min_count}}


def phi(v: tagger.Verse, path: Sequence[int]) -> dict[tuple[str, str], float]:
    """Feature counts of a (prefix) path."""
    out: dict[tuple[str, str], float] = {}
    for i, k in enumerate(path):
        if k < 0:
            continue
        ks = tagger.keys(v.cands[i][k])
        for o in v.static[i][k] + v.history(i, k, path):
            for key in ks:
                out[(o, key)] = out.get((o, key), 0.0) + 1.0
    return out


class Perceptron:
    """Averaged perceptron over nested weights (avg = w - u / t)."""

    def __init__(self) -> None:
        self.w: dict = {}
        self.u: dict = {}
        self.t = 1

    def update(self, v: tagger.Verse, gold: Sequence[tuple[int, ...]]) -> bool:
        pred, gpath = tagger.decode(v, self.w, gold)
        self.t += 1
        if pred == gpath:
            return False
        diff = phi(v, gpath)
        for f, x in phi(v, pred).items():
            diff[f] = diff.get(f, 0.0) - x
        for (o, key), x in diff.items():
            if x:
                d, du = self.w.setdefault(o, {}), self.u.setdefault(o, {})
                d[key] = d.get(key, 0.0) + x
                du[key] = du.get(key, 0.0) + self.t * x
        return True

    def averaged(self, min_abs: float = 1e-3, ndigits: int = 3) -> dict:
        out: dict = {}
        for o, d in self.w.items():
            du = self.u[o]
            row = {k: round(x - du[k] / self.t, ndigits) for k, x in d.items()}
            row = {k: x for k, x in row.items() if abs(x) >= min_abs}
            if row:
                out[o] = row
        return out


def train(data: Sequence[tuple[tuple, Sequence[tuple[int, ...]]]], epochs: int, seed: int = 0,
          on_epoch: Optional[Callable[[int, dict], None]] = None) -> dict:
    """Averaged perceptron with early update over ``(Verse arguments, gold index sets)`` pairs.
    Verses are rebuilt on each pass (their feature strings are not kept, to bound memory)."""
    p = Perceptron()
    order = list(range(len(data)))
    for epoch in range(epochs):
        random.Random(seed + epoch).shuffle(order)
        for j in order:
            args, gold, kw = data[j] if len(data[j]) == 3 else (*data[j], {})
            p.update(tagger.Verse(*args, tables=TABLES, **kw), gold)
        if on_epoch is not None:
            on_epoch(epoch, p.averaged())
    return p.averaged()


def correct(m, tok: dict) -> bool:
    """Candidate ``m`` is the gold analysis (citation conventions of ``mayur.ud``)."""
    if tok["compound_member"]:
        return m.kind == "stem" and ud.same_lemma(m, tok["lemma"], tok["upos"])
    return ud.same_lemma(m, tok["lemma"], tok["upos"]) and ud.same_feats(m, tok["upos"], tok["feats"])


def feature_ok(m, tok: dict, key: str) -> bool:
    return ud.feats(m).get(key) == tok["feats"].get(key)


def _book(path: str) -> str:
    return Path(path).parent.name


def _sentences(entry: dict):
    span = entry.get("verses")
    for s in dcs.iter_sentences(entry["file"]):
        if not span or span[0] <= s["sent_counter"] <= span[1]:
            yield s


def verses_of(sents: list[dict]) -> list[list[dict]]:
    """Half-verses grouped into verses (same chapter and verse number), in text order."""
    groups: dict[tuple, list[dict]] = {}
    for s in sents:
        groups.setdefault((s["chapter"], s["sent_counter"]), []).append(s)
    return [sorted(g, key=lambda s: s["sent_subcounter"] or 0) for g in groups.values()]


def analyse(verse: list[dict]) -> dict:
    """Words (one ``Word`` per token, ``line`` = half-verse), candidates and gold index sets."""
    words, toks, cands, gold = [], [], [], []
    for line, sent in enumerate(verse):
        for k, t in enumerate(sent["tokens"]):
            c = t["compound_member"]
            w = Word(form=t["form"], line=line, start=k, end=k + 1, in_compound=c,
                     analyses=list(lexicon.stems(t["form"]) if c else lexicon.padas(t["form"])))
            idx = shabdabodha.candidates(w) if w.analyses else []
            ms = [w.analyses[i] for i in idx]
            words.append(w)
            toks.append(t)
            cands.append(ms)
            ok = tuple(j for j, m in enumerate(ms) if correct(m, t))
            exact = tuple(j for j in ok if all(feature_ok(ms[j], t, key) for key in ("Case", "Gender")))
            gold.append(exact or ok)  # prefer the readings whose case and gender are also the gold ones
    item = {"words": words, "toks": toks, "cands": cands, "gold": gold, "own": [len(c) for c in cands]}
    return with_siblings(item) if SIBLINGS else item


def with_siblings(item: dict) -> dict:
    """Add the sibling forms' candidates (``mayur.tagger_siblings``) and recompute the gold sets."""
    w = item["words"]
    cands, own, obs, var = tagger_siblings.extend(item["cands"], [x.form for x in w], [x.in_compound for x in w],
                                                  tagger.sibling_candidates)
    gold = []
    for c, t, g, n in zip(cands, item["toks"], item["gold"], own):
        extra = tuple(n + j for j, m in enumerate(c[n:]) if correct(m, t))
        gold.append(g or extra)  # the own form's reading wins a tie: the gold form is the pada
    return {**item, "cands": cands, "own": own, "obs": obs, "var": var, "gold": gold}


def verse_kw(item: dict) -> dict:
    return {"obs_forms": item.get("obs"), "variants": item.get("var")}


def minus_of(item: dict) -> list[list[tuple[float, float]]]:
    """The training token itself is counted in the corpus tables: remove it (jackknife)."""
    return [[(1.0 if correct(m, t) else 0.0, 1.0 if ud.same_lemma(m, t["lemma"], t["upos"]) else 0.0) for m in c]
            for c, t in zip(item["cands"], item["toks"])]


def verse_args(item: dict, minus=None) -> tuple:
    w = item["words"]
    return (item["cands"], [x.line for x in w], [x.in_compound for x in w], [x.form for x in w], minus)


def load_train(max_words: int, seed: int = 0):
    """Stratified stream of TRAIN verses: round-robin over texts, files shuffled within a text."""
    by_text: dict[str, list[dict]] = {}
    for e in dcs.split_files("train"):
        by_text.setdefault(_book(e["file"]), []).append(e)
    rng = random.Random(seed)
    iters = {}
    for book, files in sorted(by_text.items()):
        files = files[:]
        rng.shuffle(files)
        iters[book] = (v for e in files for v in verses_of(list(_sentences(e))))
    words = 0
    while iters and words < max_words:
        for book in list(iters):
            v = next(iters[book], None)
            if v is None:
                del iters[book]
                continue
            item = analyse(v)
            words += len(item["toks"])
            yield book, item


def load_eval() -> tuple[list, list]:
    dev, test = [], []
    for e in dcs.split_files("dev"):
        dev += [(_book(e["file"]), v) for v in verses_of(list(_sentences(e)))]
    pool: dict[str, list] = {}
    for e in dcs.split_files("dev_pool"):
        pool.setdefault(_book(e["file"]), []).extend(_sentences(e))
    for book, sents in sorted(pool.items()):  # the fixed sample of the earlier DEV (300 half-verses per text)
        sample = random.Random(1).sample(sents, min(300, len(sents)))
        dev += [("pool:" + book, v) for v in verses_of(sample)]
    for e in dcs.split_files("test"):
        test += [(_book(e["file"]), v) for v in verses_of(list(_sentences(e)))]
    return [(b, analyse(v)) for b, v in dev], [(b, analyse(v)) for b, v in test]


def learned_choice(item: dict, weights, use_enforce: bool = True, bonus=None) -> list[int]:
    """``weights``: first-pass weights, or a pair (first pass, second pass)."""
    w1, w2 = weights if isinstance(weights, tuple) else (weights, None)
    pick = tagger.choose_indices(*verse_args(item)[:4], weights=w1, weights2=w2, tables=TABLES,
                                 neural_bonus=bonus, **verse_kw(item))
    if not use_enforce:
        return pick
    words, own = item["words"], item.get("own") or [len(c) for c in item["cands"]]
    idx = [shabdabodha.candidates(x) if x.analyses else [] for x in words]
    chosen = tagger.enforce(words, [ix[k] if ix and k < n else 0 for ix, k, n in zip(idx, pick, own)], force=True)
    return [k if k >= n else (ix.index(c) if c in ix else 0) for ix, c, k, n in zip(idx, chosen, pick, own)]


def rules_choice(item: dict) -> list[int]:
    out = []
    words = item["words"]
    for line in sorted({w.line for w in words}):
        pos = [i for i, w in enumerate(words) if w.line == line]
        ws = [words[i] for i in pos]
        for i, w, k in zip(pos, ws, shabdabodha.choose_rules(ws)):
            m = w.analyses[k] if w.analyses else None
            out.append((i, next((j for j, x in enumerate(item["cands"][i]) if x is m), 0)))
    return [k for _, k in sorted(out)]


def evaluate(items, choose, confusions: Counter | None = None) -> dict[str, dict[str, float]]:
    stats: dict[str, dict[str, float]] = {}
    for book, it in items:
        pick = choose(it)
        s = stats.setdefault(book, {"n": 0, "all": 0, "Case": 0, "Gender": 0, "oracle": 0})
        for t, c, g, p in zip(it["toks"], it["cands"], it["gold"], pick):
            if t["compound_member"] or not c:
                continue
            m = c[p]
            ok = correct(m, t)
            s["n"] += 1
            s["all"] += ok
            s["Case"] += feature_ok(m, t, "Case")
            s["Gender"] += feature_ok(m, t, "Gender")
            s["oracle"] += bool(g)
            if confusions is not None and not ok and g:
                confusions[(tagger.tag(c[g[0]]), tagger.tag(m))] += 1
    return {b: {k: round(v / s["n"], 4) if k != "n" else v for k, v in s.items()} for b, s in stats.items()}


def micro(r: dict, key: str = "all") -> float:
    return sum(x[key] * x["n"] for x in r.values()) / max(1, sum(x["n"] for x in r.values()))


def prune(w: dict, max_bytes: int) -> dict:
    """Drop the smallest weights until the JSON fits in ``max_bytes``."""
    thr = 0.001
    while True:
        out = {o: {k: x for k, x in d.items() if abs(x) >= thr} for o, d in w.items()}
        out = {o: d for o, d in out.items() if d}
        if len(json.dumps(out, ensure_ascii=False).encode("utf-8")) <= max_bytes:
            return out
        thr *= 1.6


def report_rows(report: dict) -> None:
    for split, r in report.items():
        for book in r["before"]:
            b, a = r["before"][book], r["after"][book]
            print(f"{split:5} {book:28} n={b['n']:5} all {b['all']:.3f}->{a['all']:.3f}  Case {b['Case']:.3f}->"
                  f"{a['Case']:.3f}  Gender {b['Gender']:.3f}->{a['Gender']:.3f}  oracle {b['oracle']:.3f}")
    for split, r in report.items():
        for when in ("before", "raw", "after"):
            n = sum(x["n"] for x in r[when].values())
            acc = "  ".join(f"{k} {micro(r[when], k):.3f}" for k in ("all", "Case", "Gender", "oracle"))
            print(f"{split:5} OVERALL {when:6} n={n} {acc}")


def train_early(data, epochs: int, dev, wrap, log, name: str):
    """Train, evaluating DEV after each epoch; returns the best weights and their epoch."""
    best = {"acc": -1.0, "w": {}, "epoch": 0}

    def on_epoch(epoch: int, w: dict) -> None:
        acc = micro(evaluate(dev, lambda it: learned_choice(it, wrap(w), False)))
        log(f"{name} epoch {epoch + 1}: DEV all {acc:.4f}")
        if acc > best["acc"]:
            best.update(acc=acc, w=w, epoch=epoch + 1)

    train(data, epochs, on_epoch=on_epoch)
    return best["w"], best["acc"]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-words", type=int, default=150_000)
    ap.add_argument("--epochs", type=int, default=4)
    ap.add_argument("--eval-only", action="store_true", help="re-evaluate the saved weights")
    ap.add_argument("--max-mb", type=float, default=14.0)
    ap.add_argument("--passes", type=int, default=1, choices=(1, 2))
    ap.add_argument("--no-siblings", action="store_true", help="no sibling-form candidates (मूढा / मूढास्)")
    ap.add_argument("--out", default=str(MODEL), help="where to write the model")
    args = ap.parse_args()
    global SIBLINGS
    model_in, model_out = MODEL, Path(args.out)
    if args.eval_only:
        model_in = model_out
        SIBLINGS = bool(json.loads(model_in.read_text(encoding="utf-8")).get("siblings"))
    else:
        SIBLINGS = not args.no_siblings
    t0 = time.time()
    dev, test = load_eval()
    log = lambda msg: print(f"[{time.time() - t0:5.0f}s] {msg}", file=sys.stderr, flush=True)
    log(f"dev {sum(len(i['toks']) for _, i in dev)} words, test {sum(len(i['toks']) for _, i in test)} words")
    if args.eval_only:
        saved = json.loads(model_in.read_text(encoding="utf-8"))
        w = (saved["weights"], saved.get("weights2"))
        TABLES.update(saved.get("tables", {}))
        meta = {k: v for k, v in saved.items() if k not in ("weights", "weights2", "report", "enabled")}
    else:
        data, unmatched, nwords = [], 0, 0
        counts: tuple = ({}, {}, {})
        for _book_name, item in load_train(args.max_words):
            build_tables([item], acc=counts)
            data.append((verse_args(item, minus_of(item)), item["gold"], verse_kw(item)))
            unmatched += sum(1 for g in item["gold"] if not g)
            nwords += len(item["toks"])
        TABLES.update(build_tables([], acc=counts))
        log(f"tables: {', '.join(f'{k} {len(v)}' for k, v in TABLES.items())}")
        log(f"train {len(data)} verses, {nwords} words ({unmatched} without a matching candidate)")
        w1, e1 = train_early(data, args.epochs, dev, lambda w: w, log, "pass 1")
        w = (w1, None)
        if args.passes == 2:
            priors: list = [None] * len(data)
            for fold in (0, 1):  # jackknifed first-pass choices for the second pass's training data
                wf = train([d for k, d in enumerate(data) if k % 2 != fold], args.epochs)
                for k in range(fold, len(data), 2):
                    priors[k] = [max(x, 0) for x in tagger.decode(tagger.Verse(*data[k][0], tables=TABLES, **data[k][2]), wf)]
                log(f"fold {fold} done")
            data2 = [((*a, p), g, kw) for (a, g, kw), p in zip(data, priors)]
            w2, e2 = train_early(data2, args.epochs, dev, lambda w: (w1, w), log, "pass 2")
            w = (w1, w2) if e2 > e1 else (w1, None)  # keep the second pass only when it helps on DEV
        limit = int(args.max_mb * 1e6 / (2 if w[1] else 1))
        w = (prune(w[0], limit), prune(w[1], limit) if w[1] else None)
        meta = {"source": "trained on Digital Corpus of Sanskrit annotations (Oliver Hellwig), CC BY 4.0",
                "command": "python scripts/train_tagger.py " + " ".join(sys.argv[1:]),
                "train_verses": len(data), "train_words": nwords, "passes": args.passes}
    conf: Counter = Counter()
    report = {}
    for name, items in (("dev", dev), ("test", test)):
        report[name] = {"before": evaluate(items, rules_choice),
                        "raw": evaluate(items, lambda it: learned_choice(it, w, False),
                                        conf if name == "dev" else None),
                        "after": evaluate(items, lambda it: learned_choice(it, w, True))}
    enforce = micro(report["dev"]["after"]) >= micro(report["dev"]["raw"])
    enabled = max(micro(report["dev"]["after"]), micro(report["dev"]["raw"])) > micro(report["dev"]["before"])
    report_rows(report)
    print("top confusions on DEV (gold -> predicted):")
    for (g, p), n in conf.most_common(20):
        print(f"{n:5}  {g}  ->  {p}")
    print("enabled" if enabled else "NOT enabled (not better on DEV)", "| enforce helps" if enforce else "")
    if not args.eval_only:
        out = {**meta, "enabled": enabled, "enforce": enforce, "siblings": SIBLINGS, "report": report,
               "tables": TABLES, "weights": w[0]}
        if w[1]:
            out["weights2"] = w[1]
        model_out.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
        log(f"wrote {model_out} ({model_out.stat().st_size / 1e6:.1f} MB)")
    log("done")


if __name__ == "__main__":
    main()
