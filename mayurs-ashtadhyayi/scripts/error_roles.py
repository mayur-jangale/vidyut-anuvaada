"""Dev tool: gold and our roles side by side, on the reference words (the sentence layer alone).

    python scripts/error_roles.py eval/review/claude/dev_pool_001_060_A.json [--verses 1-20] [--all]

Never run it on Rāmāyaṇa 1.1–20 or the *_B files: those are kept out of tuning.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "eval"))

import gold_words  # noqa: E402
from mayur import compounds, lipi, shabdabodha  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--verses", default="")
    ap.add_argument("--all", action="store_true", help="also print the words that agree")
    args = ap.parse_args()
    lo, _, hi = args.verses.partition("-")
    doc = json.loads(Path(args.file).read_text(encoding="utf-8"))
    ok = n = hok = 0
    for v in doc["verses"]:
        if args.verses and not int(lo) <= v["key"] <= int(hi or lo):
            continue
        r = shabdabodha.resolve(compounds.annotate(gold_words.reading_of(v)[0]))
        g = v["words"]
        name = lambda i: "-" if i is None else lipi.pausa(g[i]["form"])  # noqa: E731
        rows = []
        for gw, w in zip(g, r.words):
            if gw["compound_member"]:
                continue
            n += 1
            same_role, same_head = gw["role"] == w.role, gw["head"] == w.head
            ok += same_role
            hok += same_head
            if args.all or not (same_role and same_head):
                rows.append(f"   {'  ' if same_role and same_head else '✗ '}{gw['index']:>2} {lipi.pausa(gw['form']):<14} "
                            f"gold {gw['role']}>{name(gw['head']):<12} ours {w.role or '∅'}>{name(w.head)}")
        if rows:
            print(f"[{v['key']}] {v['text']}\n      {v.get('english', '')}")
            print("\n".join(rows))
            notes = [x for x in r.notes if "कारक check" not in x]
            if notes:
                print("      notes:", " ¦ ".join(notes)[:300])
    print(f"role {ok}/{n} = {ok / n:.1%}; head {hok}/{n} = {hok / n:.1%}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
