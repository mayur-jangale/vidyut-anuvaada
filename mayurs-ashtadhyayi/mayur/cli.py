"""Command line interface: ``mayur analyze | html | verse``."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional, Sequence

from mayur.model import VerseAnalysis


class CliError(Exception):
    """A user-facing error; reported on stderr with exit code 1."""


def normalize_input(text: str) -> str:
    """Make ASCII bars into danda/double danda; keep everything else as given."""
    return text.replace("||", "॥").replace("|", "।").strip()


def parse_range(spec: str) -> list[int]:
    """'1-5,8' -> [1,2,3,4,5,8]."""
    out: list[int] = []
    try:
        for part in spec.split(","):
            lo, _, hi = part.strip().partition("-")
            a = int(lo)
            b = int(hi) if hi else a
            if a < 1 or b < a:
                raise ValueError(part)
            out.extend(range(a, b + 1))
    except ValueError as exc:
        raise CliError(f"invalid verse range: {spec!r}") from exc
    return out


def _analyze(text: str, verse_id: str = "", max_readings: int = 5) -> VerseAnalysis:
    """Seam for tests: lazily call the real pipeline."""
    from mayur.pipeline import analyze_verse

    return analyze_verse(text, verse_id=verse_id, max_readings=max_readings)


def _gold_text(n: int) -> str:
    from mayur import gold

    try:
        return gold.verse_text(n)
    except Exception as exc:
        raise CliError(f"no gold text for verse {n}: {exc}") from exc


def _dump(data: dict, pretty: bool) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2 if pretty else None)


def cmd_analyze(args: argparse.Namespace) -> int:
    from mayur.jsonout import to_json

    if not args.verse.strip():
        raise CliError("empty verse")
    analysis = _analyze(normalize_input(args.verse), args.id, args.max_readings)
    print(_dump(to_json(analysis, full=args.full), args.pretty))
    return 0


def cmd_verse(args: argparse.Namespace) -> int:
    from mayur.jsonout import to_json

    analysis = _analyze(_gold_text(args.number), f"1.{args.number}", args.max_readings)
    print(_dump(to_json(analysis, full=args.full), args.pretty))
    return 0


def cmd_html(args: argparse.Namespace) -> int:
    from mayur.render_html import render

    analyses = [_analyze(_gold_text(n), f"1.{n}", args.max_readings) for n in parse_range(args.verses)]
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(analyses), encoding="utf-8")
    print(f"wrote {out} ({len(analyses)} verses)")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mayur", description="Verifiable Sanskrit verse interpreter.")
    sub = p.add_subparsers(dest="command", required=True)

    def common(sp: argparse.ArgumentParser) -> None:
        sp.add_argument("--full", action="store_true", help="keep all analyses and traces")
        sp.add_argument("--max-readings", type=int, default=5, metavar="N")
        sp.add_argument("--pretty", action=argparse.BooleanOptionalAction, default=True,
                        help="indent JSON (default) or --compact")
        sp.add_argument("--compact", dest="pretty", action="store_false", help=argparse.SUPPRESS)

    a = sub.add_parser("analyze", help="analyze a verse (Devanagari, IAST or SLP1) and print JSON")
    a.add_argument("verse")
    a.add_argument("--id", default="", help="verse identifier")
    common(a)
    a.set_defaults(func=cmd_analyze)

    h = sub.add_parser("html", help="analyze gold verses and write a static HTML page")
    h.add_argument("--verses", default="1-20", help="e.g. 1-20 or 1-5,8")
    h.add_argument("--out", default="docs/index.html")
    h.add_argument("--max-readings", type=int, default=5, metavar="N")
    h.set_defaults(func=cmd_html)

    v = sub.add_parser("verse", help="analyze Ramayana Bala-kanda 1.N from the bundled gold text")
    v.add_argument("number", type=int)
    common(v)
    v.set_defaults(func=cmd_verse)
    return p


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except CliError as exc:
        print(f"mayur: error: {exc}", file=sys.stderr)
    except ImportError as exc:
        print(f"mayur: error: missing component: {exc}", file=sys.stderr)
    except Exception as exc:  # last-resort: user-facing message, no traceback
        print(f"mayur: error: {type(exc).__name__}: {exc}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
