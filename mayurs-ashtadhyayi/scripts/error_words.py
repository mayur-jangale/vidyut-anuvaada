"""Dev tool: word-level error breakdown on a dev sample (never the sealed pool): which feature is
wrong for each aligned word, and whether the right analysis was among the candidates.

    python scripts/error_words.py [--sample eval/samples/dev300b.json] [--first 0 --last 300]
"""
import argparse
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "eval"))

import eval_dcs as E  # noqa: E402
from mayur import gold, lipi, pipeline, ud  # noqa: E402


def _verses():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sample", default=str(ROOT / "eval" / "samples" / "dev300b.json"), help="a dev sample file")
    ap.add_argument("--first", type=int, default=0)
    ap.add_argument("--last", type=int, default=300)
    a = ap.parse_args()
    return json.loads(Path(a.sample).read_text(encoding="utf-8"))["verses"][a.first:a.last]


doc = _verses()
kinds = collections.Counter(); avail = collections.Counter(); examples = collections.defaultdict(list); n = 0
unaligned_gold = collections.Counter(); ug_ex = []
for g in doc:
    a = pipeline.analyze_verse(gold.text_of(g), verse_id=g["id"]); r = a.readings[0]
    for i, ln in enumerate(g["lines"]):
        gl = ln["words"]; words = E.line_words(r, i); o = [E.our_word(w) for w in words]
        al = E.align_words(o, gl, lenient=True)
        got = {b for _, b in al}
        for b, gw in enumerate(gl):
            if b not in got:
                unaligned_gold["member" if gw["compound_member"] else gw.get("upos", "")] += 1
                if len(ug_ex) < 60: ug_ex.append((gw["form"], " ".join(x[0] for x in o), " ".join(x["form"] for x in gl)))
        for x, b in al:
            w, gw = words[x], gl[b]
            if w.in_compound or gw["compound_member"]: continue
            n += 1
            c = E.morphology_counts([(w.morph, gw)])
            if c["lemma"] and c["all_features"]: continue
            ours = ud.feats(w.morph) if w.morph is not None else {}
            wrong = [k for k, v in gw["feats"].items() if ours.get(k) != v] if c["lemma"] else ["LEMMA"]
            key = "+".join(sorted(wrong)) or "other"
            if key == "Case": key = f"Case {gw['feats'].get('Case')}->{ours.get('Case')}" + (" neut" if gw["feats"].get("Gender") == "Neut" else "")
            kinds[key] += 1
            ok = any(E.morphology_counts([(m, gw)])["lemma"] and E.morphology_counts([(m, gw)])["all_features"] for m in w.analyses)
            avail["right analysis among candidates" if ok else "right analysis NOT among candidates"] += 1
            if len(examples[key]) < 6: examples[key].append((lipi.pausa(w.form), gw["lemma"], dict(gw["feats"]), ours, ok))
tot = sum(kinds.values())
print("aligned non-compound words", n, "errors", tot, f"= {tot/n:.1%}")
print(avail)
for k, c in kinds.most_common(28):
    print(f"{c:4d}  {k}"); 
    for ex in examples[k][:3]: print("        ", ex)
print("UNALIGNED GOLD WORDS by class:", unaligned_gold.most_common())
for e in ug_ex[:45]: print("   miss:", e[0], "| ours:", e[1], "| gold:", e[2])
