"""Train the analysis tagger (averaged perceptron) on DCS gold half-verses with gold splits.

    python scripts/train_tagger.py [--max-train 12000] [--epochs 5]

TRAIN: a per-text stratified sample of ``mayur.dcs.split_files("train")`` (all texts).
DEV:   Rām Bā 1 verses 21-79, KumSaṃ 1 verses 21-60, and the "dev_pool" split when present.
TEST (report only): verses 1-20 of Rām Bā 1 and KumSaṃ 1.  The sealed_test pool is never read.
Writes mayur/models/tagger.json.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from mayur import dcs, lexicon, shabdabodha, tagger, ud  # noqa: E402
from mayur.model import Word  # noqa: E402

FILES = ROOT / "data/dcs/sanskrit/dcs/data/conllu/files"
HELD_OUT = {"Rāmāyaṇa-0000-", "Kumārasaṃbhava-0000-"}
KEYS = ("Case", "Number", "Gender", "Person", "Tense", "Mood", "VerbForm")


def correct(m, tok: dict) -> bool:
    """Candidate ``m`` is the gold analysis (citation conventions of ``mayur.ud``)."""
    if tok["compound_member"]:
        return m.kind == "stem" and ud.same_lemma(m, tok["lemma"], tok["upos"])
    return ud.same_lemma(m, tok["lemma"], tok["upos"]) and ud.same_feats(m, tok["upos"], tok["feats"])


def feature_ok(m, tok: dict, key: str) -> bool:
    return ud.feats(m).get(key) == tok["feats"].get(key)


def analyse(sent: dict):
    """(words, candidate morph lists, gold index or None per word)."""
    words, cands, gold = [], [], []
    for k, t in enumerate(sent["tokens"]):
        c = t["compound_member"]
        w = Word(form=t["form"], line=0, start=k, end=k + 1, in_compound=c,
                 analyses=list(lexicon.stems(t["form"]) if c else lexicon.padas(t["form"])))
        idx = shabdabodha.candidates(w)
        ms = [w.analyses[i] for i in idx]
        words.append(w)
        cands.append(ms)
        gold.append(tuple(j for j, m in enumerate(ms) if correct(m, t)))  # every matching candidate
    return words, cands, gold


def chapter_files(book: str) -> list[Path]:
    return sorted((FILES / book).glob("*.conllu"))


def _book(path: str) -> str:
    return Path(path).parent.name


def _sentences(entry: dict):
    span = entry.get("verses")
    for s in dcs.iter_sentences(entry["file"]):
        if not span or span[0] <= s["sent_counter"] <= span[1]:
            yield s


def load_train(max_train: int, per_text: int) -> list[tuple[str, dict]]:
    """Stratified sample of ``split_files("train")``: up to ``per_text`` half-verses from each text."""
    by_text: dict[str, list[dict]] = {}
    for e in dcs.split_files("train"):
        by_text.setdefault(_book(e["file"]), []).append(e)
    rng = random.Random(0)
    out: list[tuple[str, dict]] = []
    for book in sorted(by_text):
        files = by_text[book][:]
        rng.shuffle(files)
        taken: list[dict] = []
        for e in files:
            taken.extend(_sentences(e))
            if len(taken) >= per_text:
                break
        out.extend((book, s) for s in taken[:per_text])
    rng.shuffle(out)
    return out[:max_train]


def load_sets(max_train: int, per_text: int = 1500):
    """TRAIN from the train split; DEV = old DEV verses + dev_pool; TEST = verses 1-20 (report only).
    The sealed_test pool is never read."""
    dev, test = [], []
    for book, dev_range in (("Rāmāyaṇa", (21, 79)), ("Kumārasaṃbhava", (21, 60))):
        for path in chapter_files(book):
            if not any(path.name.startswith(h) for h in HELD_OUT):
                continue
            for s in dcs.iter_sentences(path):
                n = s["sent_counter"]
                if n <= 20:
                    test.append((book, s))
                elif dev_range[0] <= n <= dev_range[1]:
                    dev.append((book, s))
    pool: dict[str, list] = {}
    for e in dcs.split_files("dev_pool"):
        pool.setdefault(_book(e["file"]), []).extend(_sentences(e))
    for book, sents in sorted(pool.items()):  # at most 300 half-verses per text (memory, speed)
        dev.extend(("pool:" + book, s) for s in random.Random(1).sample(sents, min(300, len(sents))))
    return load_train(max_train, per_text), dev, test


def leave_one_out(cands, toks) -> list[list[tuple[float, float]]]:
    """The training token itself is counted in the corpus tables: remove it (jackknife)."""
    return [[(1.0 if correct(m, t) else 0.0, 1.0 if ud.same_lemma(m, t["lemma"], t["upos"]) else 0.0) for m in c]
            for c, t in zip(cands, toks)]


def train(data, epochs: int) -> dict[str, float]:
    w: dict[str, float] = {}
    total: dict[str, float] = {}
    stamp: dict[str, int] = {}
    t = 0
    for _ in range(epochs):
        for cands, gold, minus in data:
            t += 1
            pred = tagger.decode(cands, w, minus)
            # a word with no matching candidate, or already predicted correctly, causes no update
            g = [p if (not gi or p in gi) else gi[0] for gi, p in zip(gold, pred)]
            if g == pred:
                continue
            diff = tagger.features(cands, g, minus)
            for k, v in tagger.features(cands, pred, minus).items():
                diff[k] = diff.get(k, 0.0) - v
            for k, v in diff.items():
                if v:
                    total[k] = total.get(k, 0.0) + (t - stamp.get(k, 0)) * w.get(k, 0.0)
                    stamp[k] = t
                    w[k] = w.get(k, 0.0) + v
    for k in w:
        total[k] = total.get(k, 0.0) + (t - stamp.get(k, 0)) * w[k]
    return {k: round(v / t, 4) for k, v in total.items() if abs(v / t) > 1e-4}


def evaluate(items, choose) -> dict[str, dict[str, float]]:
    """items: (book, tokens, cands, gold, words); choose(words, cands) -> index per word."""
    stats: dict[str, dict[str, float]] = {}
    for book, toks, cands, gold, words in items:
        pick = choose(words, cands)
        s = stats.setdefault(book, {"n": 0, "all": 0, "Case": 0, "Gender": 0, "oracle": 0})
        for t, c, g, p in zip(toks, cands, gold, pick):
            if t["compound_member"] or not c:
                continue
            s["n"] += 1
            m = c[p]
            s["all"] += correct(m, t)
            s["Case"] += feature_ok(m, t, "Case")
            s["Gender"] += feature_ok(m, t, "Gender")
            s["oracle"] += bool(g)
    return {b: {k: round(v / s["n"], 4) if k != "n" else v for k, v in s.items()} for b, s in stats.items()}


def write_missing(items) -> None:
    """Classes of gold analyses absent from the candidates (for the lexicon audit)."""
    from collections import Counter, defaultdict
    counts: Counter = Counter()
    examples: dict[str, list[str]] = defaultdict(list)
    for _b, toks, cands, gold, _w in items:
        for t, g in zip(toks, gold):
            if not g and not t["compound_member"]:
                f = t["feats"]
                key = "|".join([t["upos"]] + [f"{k}={f[k]}" for k in ("VerbForm", "Tense", "Case") if k in f])
                counts[key] += 1
                if len(examples[key]) < 6:
                    examples[key].append(f"{t['form']} ({t['lemma']})")
    total = sum(counts.values())
    lines = [f"# gold analyses missing from the candidates on DEV: {total} tokens", ""]
    lines += [f"{n:5}  {k}: {', '.join(examples[k])}" for k, n in counts.most_common(40)]
    (ROOT / "data/derived/audit_tagger_missing.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-train", type=int, default=12000)
    ap.add_argument("--epochs", type=int, default=5)
    ap.add_argument("--per-text", type=int, default=1500)
    args = ap.parse_args()
    t0 = time.time()
    tr, dev, test = load_sets(args.max_train, args.per_text)
    prep = lambda sets: [(b, s["tokens"], *(lambda a: (a[1], a[2], a[0]))(analyse(s))) for b, s in sets]
    tr_items, dev_items, test_items = prep(tr), prep(dev), prep(test)
    unmatched = sum(not g for *_, cands, gold, _w in tr_items for g in gold)
    print(f"train {len(tr_items)} half-verses ({unmatched} tokens without a matching candidate), "
          f"dev {len(dev_items)}, test {len(test_items)}; {time.time() - t0:.0f}s", file=sys.stderr)
    data = []
    for _b, t, c, g, _w in tr_items:  # words without candidates are left out of the sequence
        keep = [i for i, x in enumerate(c) if x]
        if keep:
            cc, tt = [c[i] for i in keep], [t[i] for i in keep]
            data.append((cc, [g[i] for i in keep], leave_one_out(cc, tt)))
    w = train(data, args.epochs)

    def learned(words, cands):
        keep = [i for i, x in enumerate(cands) if x]
        out = [0] * len(cands)
        for i, k in zip(keep, tagger.decode([cands[i] for i in keep], w)):
            out[i] = k
        return out

    def baseline(words, cands):
        chosen = shabdabodha.choose_rules(words)
        out = []
        for word, c, k in zip(words, cands, chosen):
            m = word.analyses[k] if word.analyses else None
            out.append(next((j for j, x in enumerate(c) if x is m), 0))
        return out

    write_missing(dev_items)
    report = {name: {"before": evaluate(items, baseline), "after": evaluate(items, learned)}
              for name, items in (("dev", dev_items), ("test", test_items))}
    before, after = report["dev"]["before"], report["dev"]["after"]
    enabled = sum(after[b]["all"] for b in after) > sum(before[b]["all"] for b in before)
    out = {"source": "trained on Digital Corpus of Sanskrit annotations (Oliver Hellwig), CC BY 4.0",
           "command": "python scripts/train_tagger.py " + " ".join(sys.argv[1:]),
           "train_half_verses": len(data), "epochs": args.epochs, "enabled": enabled,
           "report": report, "weights": w}
    (ROOT / "mayur/models").mkdir(exist_ok=True)
    (ROOT / "mayur/models/tagger.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for split, r in report.items():
        for book in r["before"]:
            b, a = r["before"][book], r["after"][book]
            print(f"{split:5} {book:15} n={b['n']:4} all {b['all']:.3f}->{a['all']:.3f}  Case {b['Case']:.3f}->"
                  f"{a['Case']:.3f}  Gender {b['Gender']:.3f}->{a['Gender']:.3f}  oracle {b['oracle']:.3f}")
    for split, r in report.items():
        for when in ("before", "after"):
            n = sum(x["n"] for x in r[when].values())
            acc = {k: sum(x[k] * x["n"] for x in r[when].values()) / n for k in ("all", "Case", "Gender", "oracle")}
            print(f"{split:5} OVERALL {when:6} n={n} " + "  ".join(f"{k} {v:.3f}" for k, v in acc.items()))
    print("enabled" if enabled else "NOT enabled (not better on DEV)")
    print(f"done in {time.time() - t0:.0f}s", file=sys.stderr)


if __name__ == "__main__":
    main()
