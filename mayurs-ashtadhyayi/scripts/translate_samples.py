"""Translate sample sentences or picked verses with each translator variant, for reading.

    python scripts/translate_samples.py simple [--variant scratch|t5|both]
    python scripts/translate_samples.py pick --eval-file <eval json> [--per-class 20]

``simple`` runs the 46 plain sentences of eval/samples/simple_sentences.json through the fast
analysis path and prints each next to the hand-written English. ``pick`` takes the hypotheses
saved by scripts/eval_translator.py and prints verses in three length classes (by the number of
Sanskrit words: short, medium, long) with the model's English and the reference.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import translator, translator_data as td, translator_prep as prep, translator_t5  # noqa: E402

SIMPLE = Path(__file__).resolve().parent.parent / "eval" / "samples" / "simple_sentences.json"


def simple(variant: str) -> list[dict]:
    sentences = json.loads(SIMPLE.read_text(encoding="utf-8"))["sentences"]
    readings = [prep.fast_reading(s["text"]) for s in sentences]
    out = [{"text": s["text"], "reference": s.get("english", "")} for s in sentences]
    start = time.time()
    if variant in ("scratch", "both"):
        for row, hyp in zip(out, translator.translate_many(readings)):
            row["scratch"] = hyp
    if variant in ("t5", "both"):
        for row, hyp in zip(out, translator_t5.translate_many(readings)):
            row["t5"] = hyp
    sys.stdout.write(f"{len(out)} sentences, {(time.time() - start) / len(out):.2f} s each (decoding only)\n")
    return out


def pick(path: Path, per_class: int) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    sanskrit = td.read_lines(data["split"], "sn")
    rows = [{"id": i, "words": len(sanskrit[i].split()), "text": sanskrit[i], "model": h, "reference": r}
            for i, h, r in zip(data["ids"], data["hyps"], data["refs"])]
    rows.sort(key=lambda r: r["words"])
    third = len(rows) // 3
    classes = {"short": rows[:third], "medium": rows[third:2 * third], "long": rows[2 * third:]}
    step = {k: max(len(v) // per_class, 1) for k, v in classes.items()}
    return [{**row, "class": k} for k, v in classes.items() for row in v[::step[k]][:per_class]]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mode", choices=("simple", "pick"))
    ap.add_argument("--variant", choices=("scratch", "t5", "both"), default="scratch")
    ap.add_argument("--eval-file", type=Path)
    ap.add_argument("--per-class", type=int, default=20)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args(argv)
    rows = simple(args.variant) if args.mode == "simple" else pick(args.eval_file, args.per_class)
    text = json.dumps(rows, ensure_ascii=False, indent=1)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
