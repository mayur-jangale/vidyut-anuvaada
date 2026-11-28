"""Read a corrected review sheet back and write the human corrections as gold.

    python scripts/import_review.py eval/review/ramayana_bala_1.tsv [--out eval/review/gold_roles.json]
                                    [--accept-unreviewed]

Input: the TSV written by scripts/export_review.py (see its header for the columns). Rule: an EMPTY
correction cell means "our value is right"; a verse whose five correction columns are all empty is
treated as not reviewed and skipped (counted), unless --accept-unreviewed.

Output (UTF-8 JSON, Devanagari, the sentence format of mayur/treebank.py):
  {"annotator": "human review", "sheet": <file name>, "skipped_unreviewed": [verse ids],
   "sentences": [{"id", "source", "text": "" (the evaluation re-reads it from mayur.gold by id),
                  "words": [{"form", "lemma", "head_index" (0-based, null = clause head), "relation", "role",
                             "compound_member", "line"}],
                  "compounds": [{"members": [0-based word indices], "type", "vigraha": ""}],
                  "anvaya": [0-based word indices in prose order]}]}
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.export_review import REVIEW_COLUMNS  # noqa: E402


def read_rows(text: str) -> list[dict[str, str]]:
    """Rows of a sheet: '#' lines skipped, the first other line is the header."""
    lines = [ln for ln in text.splitlines() if ln.strip() and not ln.startswith("#")]
    if not lines:
        return []
    header = lines[0].split("\t")
    return [dict(zip(header, ln.split("\t") + [""] * (len(header) - ln.count("\t") - 1))) for ln in lines[1:]]


def _int(value: str, what: str, row: dict[str, str]) -> Optional[int]:
    if not value.strip():
        return None
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"{row.get('श्लोक', '?')} word {row.get('शब्दसङ्ख्या', '?')}: {what} {value!r} is not a number") from None


def sentence_of(rows: list[dict[str, str]]) -> dict[str, Any]:
    """Gold sentence of the rows of ONE verse: the correction where given, otherwise our value."""
    words, comp_rows = [], {}
    for r in rows:
        head = _int(r.get("शुद्धं_शीर्ष", ""), "head", r)
        head = head if head is not None else _int(r.get("शीर्ष_सं", "") or "0", "head", r)
        role = r.get("शुद्धं_कारकम्", "").strip() or r.get("कारकम्", "")
        i = len(words)
        words.append({"form": r["शब्द"], "lemma": r.get("धातु_प्रातिपदिक", ""), "head_index": None if not head else head - 1,
                      "relation": role, "role": role, "compound_member": False, "line": int(r.get("पङ्क्तिः") or 1) - 1})
        if r.get("समास_सं", "").strip():
            c = comp_rows.setdefault(r["समास_सं"], {"members": [], "type": r.get("समासः", "")})
            c["members"].append(i)
            c["type"] = r.get("शुद्धः_समासः", "").strip() or c["type"]
    for c in comp_rows.values():
        for i in c["members"][:-1]:
            words[i]["compound_member"] = True
    order = []
    for i, r in enumerate(rows):
        pos = _int(r.get("शुद्धा_अन्वय_सं", ""), "anvaya position", r) or _int(r.get("अन्वय_सं", ""), "anvaya position", r)
        order.append((pos if pos is not None else 10 ** 6, i))
    vid = rows[0]["श्लोक"]
    return {"id": vid, "source": "human review", "text": "", "words": words,
            "compounds": [dict(c, vigraha="") for c in comp_rows.values()], "anvaya": [i for _, i in sorted(order)]}


def reviewed(rows: list[dict[str, str]]) -> bool:
    return any(r.get(c, "").strip() for r in rows for c in REVIEW_COLUMNS)


def import_sheet(text: str, accept_unreviewed: bool = False) -> dict[str, Any]:
    by_verse: dict[str, list[dict[str, str]]] = {}
    for r in read_rows(text):
        if r.get("शब्दसङ्ख्या", "").strip():  # failed-analysis placeholder rows carry no word number
            by_verse.setdefault(r["श्लोक"], []).append(r)
    skipped = [v for v, rows in by_verse.items() if not (accept_unreviewed or reviewed(rows))]
    return {"annotator": "human review", "skipped_unreviewed": skipped,
            "sentences": [sentence_of(rows) for v, rows in by_verse.items() if v not in skipped]}


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("sheet")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent / "eval" / "review" / "gold_roles.json"))
    ap.add_argument("--accept-unreviewed", action="store_true")
    args = ap.parse_args(argv)
    doc = import_sheet(Path(args.sheet).read_text(encoding="utf-8"), args.accept_unreviewed)
    doc["sheet"] = Path(args.sheet).name
    Path(args.out).write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(doc['sentences'])} verses imported, {len(doc['skipped_unreviewed'])} unreviewed skipped -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
