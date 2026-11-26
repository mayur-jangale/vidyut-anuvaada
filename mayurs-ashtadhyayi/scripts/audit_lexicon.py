"""Audit mayur.lexicon against the DCS corpus.

    python scripts/audit_lexicon.py [--books Rāmāyaṇa,Kumārasaṃbhava] [--max-files N]

For every distinct (form, lemma, UPOS, feats, compound member) of the chosen books: is the form
analysed, is the gold analysis among ours (mayur.ud), is that analysis proven by vidyut.
Prints token- and type-weighted rates and failure classes; writes the top failures to
data/derived/audit_lexicon_failures.txt.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import dcs, lexicon, ud  # noqa: E402
from mayur.resources import data_dir, derived_dir  # noqa: E402

FILES = data_dir() / "dcs" / "sanskrit" / "dcs" / "data" / "conllu" / "files"


def collect(books: list[str], max_files: int) -> Counter:
    counts: Counter = Counter()
    for book in books:
        for path in sorted((FILES / book).glob("*.conllu"))[: max_files or None]:
            for sent in dcs.iter_sentences(path):
                for t in sent["tokens"]:
                    if not t["form"] or t["form"] == "_":
                        continue
                    feats = tuple(sorted(t["feats"].items()))
                    counts[(t["form"], t["lemma"], t["upos"], feats, t["compound_member"])] += 1
    return counts


def judge(form: str, lemma: str, feats: dict[str, str], cpd: bool) -> str:
    """"ok" | "unproved" | "wrong" (analysed, gold analysis missing) | "none"."""
    ms = lexicon.stems(form) if cpd else lexicon.padas(form)
    if not ms and not cpd:
        ms = lexicon.generated(form)
    if not ms:
        return "none"
    good = [m for m in ms if ud.lemma(m) == lemma and (cpd or ud.feats_agree(ud.feats(m), feats))]
    if not good:
        return "wrong"
    return "ok" if any(lexicon.prove(m).derivable for m in good[:4]) else "unproved"


def _pattern(upos: str, feats: dict[str, str], cpd: bool) -> str:
    if cpd:
        return "Cpd"
    keys = ("VerbForm", "Tense", "Mood", "Case", "Number")
    return upos + ":" + ",".join(feats[k] for k in keys if k in feats)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--books", default="Rāmāyaṇa")
    ap.add_argument("--max-files", type=int, default=0)
    ap.add_argument("--top", type=int, default=300)
    ap.add_argument("--out", default=str(derived_dir() / "audit_lexicon_failures.txt"))
    args = ap.parse_args()
    counts = collect(args.books.split(","), args.max_files)
    tok = Counter()
    typ = Counter()
    classes: dict[str, Counter] = {}
    examples: dict[str, list[str]] = {}
    fails: list[tuple[int, str]] = []
    for (form, lemma, upos, feats_t, cpd), n in counts.items():
        feats = dict(feats_t)
        verdict = judge(form, lemma, feats, cpd)
        for r in ("analysed", "correct", "proven"):
            hit = {"analysed": verdict != "none", "correct": verdict in ("ok", "unproved"),
                   "proven": verdict == "ok"}[r]
            tok[r] += n * hit
            typ[r] += hit
        if verdict != "ok":
            for key in (f"{verdict} {_pattern(upos, feats, cpd)}", f"{verdict} ending -{form[-2:]}"):
                classes.setdefault(key, Counter())[form] += n
            fails.append((n, f"{n}\t{verdict}\t{'C:' if cpd else ''}{form}\t{lemma}\t{upos}\t"
                             + "|".join(f"{k}={v}" for k, v in feats_t)))
    ntok, ntyp = sum(counts.values()), len(counts)
    print(f"tokens {ntok}, types {ntyp}")
    for r in ("analysed", "correct", "proven"):
        print(f"  {r:9s} tokens {100 * tok[r] / ntok:5.1f}%   types {100 * typ[r] / ntyp:5.1f}%")
    ranked = sorted(classes.items(), key=lambda kv: -sum(kv[1].values()))
    print("failure classes (tokens, examples):")
    for key, c in ranked[:40]:
        print(f"  {sum(c.values()):6d}  {key:32s} {' '.join(f for f, _ in c.most_common(6))}")
    fails.sort(key=lambda x: -x[0])
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text("\n".join(line for _, line in fails[: args.top]) + "\n", encoding="utf-8")
    print("wrote", args.out)


if __name__ == "__main__":
    main()
