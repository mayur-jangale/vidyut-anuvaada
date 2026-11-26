"""Roles and heads on plain prose sentences (eval/samples/simple_sentences.json), through the whole
pipeline from raw text.

    python eval/eval_simple.py [--show]

Each listed word must be found in the chosen reading (compound members joined), with the expected
role and head. A regression set of everyday sentences, not a statistical sample.
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

SAMPLE = ROOT / "eval" / "samples" / "simple_sentences.json"
_SU_LOPA = {"स": "सस्", "एष": "एषस्"}  # written without the ending before a consonant (6.1.132)


def padas(reading: Reading) -> list[tuple[str, int]]:
    """(written pada, index of its final word) for every pada of the reading."""
    out, group = [], []
    for i, w in enumerate(reading.words):
        group.append(w.form)
        if not w.in_compound:
            text = group[0] if len(group) == 1 else next(iter(sandhi.rejoin(group, [True] * (len(group) - 1))), "")
            out.append((sandhi.canon(lipi.pausa(_SU_LOPA.get(text, text))), i))
            group = []
    return out


def check(reading: Reading, expect: list[dict]) -> list[str]:
    """Problems with the expected words of one sentence (empty when all are right)."""
    index = {form: i for form, i in padas(reading)}
    final_of = {}
    last = None
    for i in range(len(reading.words) - 1, -1, -1):  # a head inside a compound counts as its final word
        if not reading.words[i].in_compound:
            last = i
        final_of[i] = last
    problems = []
    for e in expect:
        i = index.get(sandhi.canon(e["form"]))
        if i is None:
            problems.append(f"{e['form']}: not a word of the chosen reading")
            continue
        w = reading.words[i]
        head = None if w.head is None else final_of[w.head]
        want = None if e["head"] is None else index.get(sandhi.canon(e["head"]))
        if w.role != e["role"] or head != want:
            got = "-" if head is None else lipi.pausa(reading.words[head].form)
            problems.append(f"{e['form']}: expected {e['role']}>{e['head'] or '-'}, got {w.role or '∅'}>{got}")
    return problems


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--show", action="store_true", help="print the problems and the English of every sentence")
    args = ap.parse_args(argv)
    sentences = json.loads(SAMPLE.read_text(encoding="utf-8"))["sentences"]
    right = words = words_ok = 0
    for s in sentences:
        reading = analyze_verse(s["text"]).readings[0]
        problems = check(reading, s["expect"])
        right += not problems
        words += len(s["expect"])
        words_ok += len(s["expect"]) - len(problems)
        if args.show:
            print(f"{'✓' if not problems else '✗'} {s['text']}\n     {reading.reworded or reading.translation}")
            for p in problems:
                print(f"     {p}")
    n = len(sentences)
    print(f"simple sentences: {n}; all listed words right {right}/{n} = {right / n:.1%}; "
          f"words {words_ok}/{words} = {words_ok / words:.1%}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
