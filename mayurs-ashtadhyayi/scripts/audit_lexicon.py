"""Audit mayur.lexicon against the DCS corpus.

    python scripts/audit_lexicon.py [--split train] [--per-text N] [--books A,B] [--max-files N]

With --split (default "train") the files come from ``mayur.dcs.split_files`` only (never the sealed
pools); --per-text caps the files sampled from each text, so every text is represented.

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


def _text_of(path: str) -> str:
    return Path(path).parent.name


def choose_files(split: str, books: list[str], max_files: int, per_text: int, seed: int) -> list[dict]:
    if books:
        return [{"file": str(p), "verses": None} for b in books
                for p in sorted((FILES / b).glob("*.conllu"))[: max_files or None]]
    import random

    by_text: dict[str, list[dict]] = {}
    for e in dcs.split_files(split):
        by_text.setdefault(_text_of(e["file"]), []).append(e)
    rng = random.Random(seed)
    out = []
    for text in sorted(by_text):
        entries = by_text[text]
        out.extend(rng.sample(entries, min(per_text, len(entries))) if per_text else entries)
    return out


def collect(entries: list[dict]) -> dict[str, Counter]:
    """text -> Counter of (form, lemma, upos, feats, compound member)."""
    out: dict[str, Counter] = {}
    for e in entries:
        counts = out.setdefault(_text_of(e["file"]), Counter())
        lo, hi = e["verses"] or (None, None)
        for sent in dcs.iter_sentences(e["file"]):
            if lo is not None and not lo <= sent["sent_counter"] <= hi:
                continue
            for t in sent["tokens"]:
                if not t["form"] or t["form"] == "_":
                    continue
                feats = tuple(sorted(t["feats"].items()))
                counts[(t["form"], t["lemma"], t["upos"], feats, t["compound_member"])] += 1
    return out


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
    ap.add_argument("--split", default="train")
    ap.add_argument("--per-text", type=int, default=20)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--books", default="")
    ap.add_argument("--max-files", type=int, default=0)
    ap.add_argument("--top", type=int, default=300)
    ap.add_argument("--out", default=str(derived_dir() / "audit_lexicon_failures.txt"))
    ap.add_argument("--verbal-lemma", action="store_true",
                    help="experiment: cite verbal lemmas with lexicon.verbal_lemma (sandhi-joined)")
    args = ap.parse_args()
    if args.verbal_lemma:
        original = ud.lemma
        ud.lemma = lambda m: lexicon.verbal_lemma(m) if (m.kind == "tinanta" or ud.is_verbal_noun(m)) else original(m)
    entries = choose_files(args.split, [b for b in args.books.split(",") if b], args.max_files, args.per_text,
                           args.seed)
    per_text = collect(entries)
    counts: Counter = Counter()
    for c in per_text.values():
        counts.update(c)
    verdicts = {key: judge(key[0], key[1], dict(key[3]), key[4]) for key in counts}
    print("per text (tokens: analysed / correct / proven):")
    for text, c in sorted(per_text.items(), key=lambda kv: -sum(kv[1].values())):
        n = sum(c.values())
        rates = [sum(k2 for key, k2 in c.items() if verdicts[key] in ok) / n * 100
                 for ok in (("ok", "unproved", "wrong"), ("ok", "unproved"), ("ok",))]
        print(f"  {text:24s} {n:7d}  " + "  ".join(f"{r:5.1f}%" for r in rates))
    tok = Counter()
    typ = Counter()
    classes: dict[str, Counter] = {}
    examples: dict[str, list[str]] = {}
    fails: list[tuple[int, str]] = []
    for (form, lemma, upos, feats_t, cpd), n in counts.items():
        feats = dict(feats_t)
        verdict = verdicts[(form, lemma, upos, feats_t, cpd)]
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
