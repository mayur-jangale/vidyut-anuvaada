"""Train the analysis tagger (averaged perceptron) on DCS gold half-verses with gold splits.

    python scripts/train_tagger.py [--max-train 12000] [--epochs 5]

TRAIN: Rāmāyaṇa and Kumārasaṃbhava chapters except the held-out ones (Rām Bā 1, KumSaṃ 1).
DEV:   Rām Bā 1 verses 21-79, KumSaṃ 1 verses 21-60.  TEST (report only): verses 1-20 of both.
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
    """Candidate ``m`` matches the gold token: lemma and every gold feature we can state."""
    if ud.lemma(m) != tok["lemma"]:
        return False
    ours, gold = ud.feats(m), tok["feats"]
    if tok["compound_member"]:
        return m.kind == "stem"
    return ud.feats_agree(ours, gold) and all(k in ours for k in ("Case", "Number", "Person") if k in gold)


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
        gold.append(next((j for j, m in enumerate(ms) if correct(m, t)), None))
    return words, cands, gold


def chapter_files(book: str) -> list[Path]:
    return sorted((FILES / book).glob("*.conllu"))


def load_sets(max_train: int):
    train, dev, test = [], [], []
    for book, dev_range in (("Rāmāyaṇa", (21, 79)), ("Kumārasaṃbhava", (21, 60))):
        for path in chapter_files(book):
            held = any(path.name.startswith(h) for h in HELD_OUT)
            for s in dcs.iter_sentences(path):
                if held:
                    n = s["sent_counter"]
                    if n <= 20:
                        test.append((book, s))
                    elif dev_range[0] <= n <= dev_range[1]:
                        dev.append((book, s))
                else:
                    train.append((book, s))
    random.Random(0).shuffle(train)
    return train[:max_train], dev, test


def train(data, epochs: int) -> dict[str, float]:
    w: dict[str, float] = {}
    total: dict[str, float] = {}
    stamp: dict[str, int] = {}
    t = 0
    for _ in range(epochs):
        for cands, gold in data:
            t += 1
            pred = tagger.decode(cands, w)
            g = [gi if gi is not None else p for gi, p in zip(gold, pred)]
            if g == pred:
                continue
            diff = tagger.features(cands, g)
            for k, v in tagger.features(cands, pred).items():
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
            s["oracle"] += g is not None
    return {b: {k: round(v / s["n"], 4) if k != "n" else v for k, v in s.items()} for b, s in stats.items()}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-train", type=int, default=12000)
    ap.add_argument("--epochs", type=int, default=5)
    args = ap.parse_args()
    t0 = time.time()
    tr, dev, test = load_sets(args.max_train)
    prep = lambda sets: [(b, s["tokens"], *(lambda a: (a[1], a[2], a[0]))(analyse(s))) for b, s in sets]
    tr_items, dev_items, test_items = prep(tr), prep(dev), prep(test)
    unmatched = sum(g is None for *_, cands, gold, _w in tr_items for g in gold)
    print(f"train {len(tr_items)} half-verses ({unmatched} tokens without a matching candidate), "
          f"dev {len(dev_items)}, test {len(test_items)}; {time.time() - t0:.0f}s", file=sys.stderr)
    data = [(c, g) for _b, _t, c, g, _w in tr_items if c and all(c)]
    w = train(data, args.epochs)

    def learned(words, cands):
        return tagger.decode(cands, w) if all(cands) else [0] * len(cands)

    def baseline(words, cands):
        chosen = shabdabodha.choose_rules(words)
        out = []
        for word, c, k in zip(words, cands, chosen):
            m = word.analyses[k] if word.analyses else None
            out.append(next((j for j, x in enumerate(c) if x is m), 0))
        return out

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
    print("enabled" if enabled else "NOT enabled (not better on DEV)")
    print(f"done in {time.time() - t0:.0f}s", file=sys.stderr)


if __name__ == "__main__":
    main()
