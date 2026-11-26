"""Dev tool: pada-level disagreements with the corpus on a dev sample (never the sealed pool).

    python scripts/error_padas.py [--sample eval/samples/dev300b.json] [--first 0 --last 300]
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
miss = []; tot = 0
for g in doc:
    r = pipeline.analyze_verse(gold.text_of(g), verse_id=g["id"]).readings[0]
    for i, ln in enumerate(g["lines"]):
        gl = ln["words"]; o = [E.our_word(w) for w in E.line_words(r, i)]
        pu, gu = E.pada_units(o), E.gold_pada_units(gl)
        pairs = E.lcs_pairs(pu, gu, E.pada_match); tot += len(gu)
        gm = {b for _, b in pairs}; om = {a for a, _ in pairs}
        if len(gm) < len(gu):
            miss.append((ln.get("text", ""), [gu[b][0] for b in range(len(gu)) if b not in gm], [pu[a][0] for a in range(len(pu)) if a not in om]))
print("gold padas", tot, "lines with misses", len(miss), "missed padas", sum(len(m[1]) for m in miss))
for t, gmiss, omiss in miss[:110]:
    print(f"{t}\n    gold-only: {' | '.join(gmiss)}\n    ours-only: {' | '.join(omiss)}")
