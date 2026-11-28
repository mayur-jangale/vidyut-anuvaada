"""Dev tool: does the rule system PRODUCE the corpus's reading? (The formula part: no ranking involved.)

    python scripts/coverage_rules.py [--lines 1500] [--seed 5] [--show 60]

For gold lines of the dev pool whose own words re-join to the text by the sandhi rules (a gold
line that does not is a corpus artefact or a sandhi-rule gap, counted separately):
  * split coverage: the gold split is a path of the lattice;
  * analysis coverage: each gold word's lemma and features are among the lexicon's analyses.
Every miss is a rule or lexicon gap to fix; the target for both is 100%.
"""

from __future__ import annotations

import argparse
import collections
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from mayur import dcs, lexicon, sandhi, segmenter, ud  # noqa: E402


INDECLINABLE = ("ADV", "PART", "CONJ", "CCONJ", "SCONJ", "ADP", "INTJ")


def analysis_available(w: dict) -> bool:
    form = w["form"]
    if form.endswith("र्") and not w["compound_member"] and not lexicon.padas(form):
        form = form[:-2] + "स्"  # the corpus sometimes writes the visarga of गीर्भिः as it sounds before a voiced sound
    w = {**w, "form": form}
    ms = lexicon.stems(w["form"]) if w["compound_member"] else lexicon.padas(w["form"])
    if w["compound_member"]:
        return bool(ms)
    ms = ms or lexicon.generated(w["form"])
    return any(ud.same_lemma(m, w["lemma"], w.get("upos", "")) and ud.same_feats(m, w.get("upos", ""), w["feats"]) for m in ms)


def miss_reason(w: dict) -> str:
    """Why a gold word is not covered: no analysis at all, or only the lemma / the features differ."""
    if w["compound_member"]:
        return "no stem analysis"
    ms = lexicon.padas(w["form"]) or lexicon.generated(w["form"])
    if not ms:
        return "no analysis"
    same = [m for m in ms if ud.same_lemma(m, w["lemma"], w.get("upos", ""))]
    ours = ", ".join(dict.fromkeys(m.lemma for m in ms))[:60]
    return f"features differ (lemma found)" if same else f"lemma differs (ours: {ours})"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lines", type=int, default=1500)
    ap.add_argument("--seed", type=int, default=5)
    ap.add_argument("--show", type=int, default=60)
    args = ap.parse_args()
    lines = [g for g in dcs.gold_lines(dcs.split_files("dev_pool"), limit=args.lines, seed=args.seed) if g["words"]]
    valid = covered = 0
    words = words_ok = 0
    not_rejoin, no_path, no_analysis = [], [], collections.Counter()
    for g in lines:
        forms = [w["form"] for w in g["words"]]
        flags = [w["compound_member"] for w in g["words"]]
        if sandhi.rejoin_matching(forms, flags[:-1], g["text"]) is None:
            not_rejoin.append(g)
            continue
        valid += 1
        loose = [None if w.get("upos") in INDECLINABLE and k + 1 < len(flags) else c
                 for k, (w, c) in enumerate(zip(g["words"], flags))]  # the corpus's flag convention
        if segmenter.contains(g["text"], forms, loose):
            covered += 1
        else:
            unknown = [w["form"] for w in g["words"] if segmenter.word_score(w["form"], w["compound_member"], 1) is None]
            no_path.append((g["text"], " ".join(f + ("-" if c else "") for f, c in zip(forms, flags)), unknown))
        for w in g["words"]:
            words += 1
            if analysis_available(w):
                words_ok += 1
            else:
                no_analysis[(w["form"], w["lemma"], w.get("upos", ""), "member" if w["compound_member"] else
                             " ".join(f"{k}={v}" for k, v in w["feats"].items()), miss_reason(w))] += 1
    print(f"gold lines {len(lines)}; own words re-join to the text {valid} = {valid / len(lines):.1%} "
          f"(not: {len(not_rejoin)})")
    print(f"SPLIT COVERAGE (gold split is a lattice path, of re-joining lines): {covered}/{valid} = {covered / valid:.1%}")
    print(f"ANALYSIS COVERAGE (gold lemma+features among our analyses): {words_ok}/{words} = {words_ok / words:.1%}")
    kinds = collections.Counter("unknown word" if u else "junction or path" for _, _, u in no_path)
    print("split misses by kind:", dict(kinds))
    for text, gold, unknown in no_path[: args.show]:
        print(f"  SPLIT  {text}\n         gold: {gold}\n         no edge for: {' '.join(unknown) or '— (all words known)'}")
    reasons = collections.Counter()
    for key, n in no_analysis.items():
        reasons[key[4].split(" (")[0]] += n
    print("analysis misses by kind:", dict(reasons))
    for (form, lemma, upos, feats, why), n in no_analysis.most_common(args.show):
        print(f"  ANALYSIS {n:3d}  {form}  lemma {lemma}  {upos} {feats}  | {why}")
    for g in not_rejoin[: args.show // 3]:
        print(f"  NO-REJOIN {g['text']}\n         gold: {' '.join(w['form'] for w in g['words'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
