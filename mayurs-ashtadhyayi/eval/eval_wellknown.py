"""Pada split of well-known lines outside the corpus (eval/samples/wellknown.json).

    python eval/eval_wellknown.py [--show]

A line counts as right when the chosen reading's padas (compound members joined) equal the
hand-written padas; "kept" when one of the kept readings does. This is a regression set of
everyday Sanskrit, not a statistical sample.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from mayur import lipi, sandhi  # noqa: E402
from mayur.model import Reading  # noqa: E402
from mayur.pipeline import analyze_verse  # noqa: E402

SAMPLE = ROOT / "eval" / "samples" / "wellknown.json"
# स / एष before a consonant (6.1.132): the corpus convention writes them as they stand; the pada is सः / एषः
_SU_LOPA = {"स": "सस्", "एष": "एषस्"}


def groups(reading: Reading) -> list[list[str]]:
    """The reading's padas, each as the list of its members (one member for a simple word)."""
    out: list[list[str]] = []
    group: list[str] = []
    for w in reading.words:
        group.append(w.form)
        if not w.in_compound:
            out.append(group)
            group = []
    return out


def shown(group: list[str]) -> str:
    return "-".join(lipi.pausa(m) if i == len(group) - 1 else m for i, m in enumerate(group))


def same(ours: list[list[str]], gold: list[str]) -> bool:
    """Same padas: a simple word equals the gold pada; a compound's members re-join to it by sandhi."""
    if len(ours) != len(gold):
        return False
    for group, want in zip(ours, gold):
        if len(group) == 1:
            if sandhi.canon(lipi.pausa(_SU_LOPA.get(group[0], group[0]))) != sandhi.canon(lipi.pausa(want)):
                return False
        elif sandhi.rejoin_matching(group, [True] * (len(group) - 1), lipi.pausa(want)) is None:
            return False
    return True


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--show", action="store_true", help="print every wrong line")
    args = ap.parse_args(argv)
    lines = json.loads(SAMPLE.read_text(encoding="utf-8"))["lines"]
    right = kept = verified = 0
    for item in lines:
        analysis = analyze_verse(item["text"])
        splits = [groups(r) for r in analysis.readings]
        ok = bool(splits) and same(splits[0], item["padas"])
        right += ok
        kept += any(same(s, item["padas"]) for s in splits)
        verified += analysis.status == "verified"
        if args.show and not ok:
            print(f"✗ {item['text']}\n    ours: {' '.join(shown(g) for g in splits[0]) if splits else '—'}\n    want: {' '.join(item['padas'])}")
    n = len(lines)
    print(f"well-known lines: {n}; chosen split right {right}/{n} = {right / n:.1%}; "
          f"right split among kept readings {kept}/{n} = {kept / n:.1%}; verified {verified}/{n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
