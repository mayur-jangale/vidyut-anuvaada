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

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from mayur import dcs, lexicon, shabdabodha, tagger, ud  # noqa: E402
from mayur.model import Word  # noqa: E402

MODEL = ROOT / "mayur/models/tagger.json"


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
            gold.append(tuple(j for j, m in enumerate(ms) if correct(m, t)))
    return {"words": words, "toks": toks, "cands": cands, "gold": gold}


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


def learned_choice(item: dict, weights, use_enforce: bool = True) -> list[int]:
    pick = tagger.choose_indices(*verse_args(item)[:4], weights=weights)
    if not use_enforce:
        return pick
    words = item["words"]
    idx = [shabdabodha.candidates(x) if x.analyses else [] for x in words]
    chosen = tagger.enforce(words, [ix[k] if ix else 0 for ix, k in zip(idx, pick)])
    return [ix.index(c) if c in ix else 0 for ix, c in zip(idx, chosen)]


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
        if len(json.dumps(out, ensure_ascii=False)) <= max_bytes:
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


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-words", type=int, default=150_000)
    ap.add_argument("--epochs", type=int, default=4)
    ap.add_argument("--eval-only", action="store_true", help="re-evaluate the saved weights")
    ap.add_argument("--max-mb", type=float, default=14.0)
    args = ap.parse_args()
    t0 = time.time()
    dev, test = load_eval()
    log = lambda msg: print(f"[{time.time() - t0:5.0f}s] {msg}", file=sys.stderr, flush=True)
    log(f"dev {sum(len(i['toks']) for _, i in dev)} words, test {sum(len(i['toks']) for _, i in test)} words")
    if args.eval_only:
        saved = json.loads(MODEL.read_text(encoding="utf-8"))
        w, meta = saved["weights"], {k: v for k, v in saved.items() if k not in ("weights", "report", "enabled")}
    else:
        data, unmatched, nwords = [], 0, 0
        for _book_name, item in load_train(args.max_words):
            data.append((verse_args(item, minus_of(item)), item["gold"]))
            unmatched += sum(1 for g in item["gold"] if not g)
            nwords += len(item["toks"])
        log(f"train {len(data)} verses, {nwords} words ({unmatched} without a matching candidate)")
        best = {"acc": -1.0, "w": {}, "epoch": 0}

        def on_epoch(epoch: int, w: dict) -> None:
            acc = micro(evaluate(dev, lambda it: learned_choice(it, w, False)))
            log(f"epoch {epoch + 1}: DEV all {acc:.4f}")
            if acc > best["acc"]:
                best.update(acc=acc, w=w, epoch=epoch + 1)

        tagger.train(data, args.epochs, on_epoch=on_epoch)
        w = prune(best["w"], int(args.max_mb * 1e6))
        meta = {"source": "trained on Digital Corpus of Sanskrit annotations (Oliver Hellwig), CC BY 4.0",
                "command": "python scripts/train_tagger.py " + " ".join(sys.argv[1:]),
                "train_verses": len(data), "train_words": nwords, "epochs_kept": best["epoch"]}
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
        MODEL.write_text(json.dumps({**meta, "enabled": enabled, "report": report, "weights": w},
                                    ensure_ascii=False), encoding="utf-8")
        log(f"wrote {MODEL} ({MODEL.stat().st_size / 1e6:.1f} MB)")
    log("done")


if __name__ == "__main__":
    main()
