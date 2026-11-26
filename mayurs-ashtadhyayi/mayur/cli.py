"""Command line: ``mayur analyze | verse | html``. Pipeline and gold text are imported lazily."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from . import jsonout, lipi
from .model import VerseAnalysis

DEFAULT_OUT = "docs/index.html"


# ---------------------------------------------------------------- seams (patched in tests)

def run_pipeline(text: str, verse_id: str = "", script: str | None = None, max_readings: int = 5) -> VerseAnalysis:
    from .pipeline import analyze_verse

    return analyze_verse(text, verse_id=verse_id, script=script, max_readings=max_readings)


def gold_text(n: int) -> str:
    from .gold import verse_text

    return verse_text(n)


# ---------------------------------------------------------------- parsing

def parse_range(spec: str) -> list[int]:
    """``"1-20"`` -> [1..20]; ``"3"`` -> [3]; ``"1-5,9"`` -> [1,2,3,4,5,9]."""
    numbers: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        lo, _, hi = part.partition("-")
        try:
            a, b = int(lo), int(hi or lo)
        except ValueError:
            raise ValueError(f"bad verse range: {spec!r}") from None
        if a < 1 or b < a:
            raise ValueError(f"bad verse range: {spec!r}")
        numbers.extend(range(a, b + 1))
    return numbers


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mayur", description="Sanskrit verse analysis grounded in Panini's rules.")
    sub = p.add_subparsers(dest="command", required=True)
    for name, help_ in (("analyze", "analyze a verse given as text"), ("verse", "analyze Ramayana 1.N from the bundled text")):
        s = sub.add_parser(name, help=help_)
        if name == "analyze":
            s.add_argument("text", help="verse; half-verses separated by । or a newline")
            s.add_argument("--script", choices=["devanagari", "iast"], default=None)
            s.add_argument("--id", default="", dest="verse_id")
        else:
            s.add_argument("n", type=int, help="verse number in Bala-kanda 1")
        s.add_argument("--full", action="store_true", help="full word lists for alternatives, all other analyses")
        s.add_argument("--max-readings", type=_positive, default=5)
        s.add_argument("--compact", action="store_true", help="single-line JSON")
        s.add_argument("--fluent", action="store_true", help="accepted for compatibility; fluent English is always included")
    h = sub.add_parser("html", help="write the static page")
    h.add_argument("--verses", default="1-20", help="range such as 1-20")
    h.add_argument("--out", default=DEFAULT_OUT)
    h.add_argument("--max-readings", type=_positive, default=5)
    return p


def _positive(value: str) -> int:
    n = int(value)
    if n < 1:
        raise argparse.ArgumentTypeError("must be 1 or more")
    return n


def _dump(analysis: VerseAnalysis, args: argparse.Namespace) -> str:
    data: dict[str, Any] = jsonout.to_json(analysis, full=args.full)
    return json.dumps(data, ensure_ascii=False, indent=None if args.compact else 2)


def _write_stdout(text: str) -> None:
    out = sys.stdout
    try:
        out.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass
    out.write(text + "\n")


def _cmd_html(args: argparse.Namespace) -> int:
    from .render_html import render

    analyses = [run_pipeline(gold_text(n), verse_id=f"1.{n}", script="devanagari", max_readings=args.max_readings)
                for n in parse_range(args.verses)]
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(analyses), encoding="utf-8")
    _write_stdout(f"{path} ({len(analyses)} verses)")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "analyze":
            _write_stdout(_dump(run_pipeline(args.text, args.verse_id, args.script, args.max_readings), args))
        elif args.command == "verse":
            text = gold_text(args.n)
            _write_stdout(_dump(run_pipeline(text, f"1.{args.n}", "devanagari", args.max_readings), args))
        else:
            return _cmd_html(args)
    except lipi.AmbiguousScript as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except (ValueError, KeyError, IndexError, OSError, ImportError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
