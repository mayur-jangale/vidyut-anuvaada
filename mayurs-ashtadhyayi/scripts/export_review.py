"""Write a review sheet (TSV) of our analysis, one row per word, for a Sanskrit reader to correct.

    python scripts/export_review.py --verses 1-79 --out eval/review/ramayana_bala_1.tsv

Sheet format (UTF-8, tab separated, Devanagari). Lines starting with '#' are comments; the first other
line is the column header:

  श्लोक         verse id (as in mayur.gold)           | पङ्क्तिः   half-verse number, from 1
  शब्दसङ्ख्या    word number in the verse, from 1      | शब्द       the word (non-final compound members as stems)
  धातु_प्रातिपदिक  lemma                                | व्याकरणम्   grammar in Devanagari terms
  कारकम्         our role (a key of mayur.terms.ROLES)| शीर्ष_सं    our head: word number, 0 = clause head
  शीर्षशब्दः      the head word                         | समासः      our compound type (on every member)
  समास_सं        compound number in the verse (members share it)
  अन्वय_सं       our position in the prose order, from 1 | अर्थः    our English gloss of the word
  then the columns the REVIEWER fills (leave empty = our value is right):
  शुद्धं_कारकम्, शुद्धं_शीर्ष (word number, 0 = clause head), शुद्धः_समासः, शुद्धा_अन्वय_सं, टिप्पणी
A verse whose correction columns are ALL empty is treated as not reviewed by scripts/import_review.py.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

COLUMNS = ("श्लोक", "पङ्क्तिः", "शब्दसङ्ख्या", "शब्द", "धातु_प्रातिपदिक", "व्याकरणम्", "कारकम्", "शीर्ष_सं",
           "शीर्षशब्दः", "समासः", "समास_सं", "अन्वय_सं", "अर्थः")
REVIEW_COLUMNS = ("शुद्धं_कारकम्", "शुद्धं_शीर्ष", "शुद्धः_समासः", "शुद्धा_अन्वय_सं", "टिप्पणी")
HEADER = __doc__.split("\n\n", 1)[1].rstrip("\n").splitlines()


def clean(value: Any) -> str:
    return " ".join(str(value if value is not None else "").replace("\t", " ").split())


def grammar_of(word: Any) -> str:
    """Grammar of a word in Devanagari terms (the terms the analysis itself uses)."""
    m = word.morph
    if m is None:
        return "अज्ञातम्"
    if word.in_compound:
        return "समासपूर्वपद"
    parts: list = []
    if m.kind == "tinanta":
        parts += [m.lakara, m.purusha, m.vacana, m.prayoga]
    elif m.kind == "subanta":
        parts += [m.linga, m.vibhakti, m.vacana, m.krt]
    else:
        parts += [m.kind]
    return " ".join(p for p in parts if p)


def rows_for(reading: Any, verse_id: str) -> list[dict[str, str]]:
    """Sheet rows of one reading (pure). Word numbers are 1-based; head 0 means the clause head."""
    comp_of = {i: c for c in reading.compounds for i in c.members}
    comp_no = {c.id: n + 1 for n, c in enumerate(reading.compounds)}
    position = {w: p + 1 for p, w in enumerate(reading.anvaya)}
    rows = []
    for i, w in enumerate(reading.words):
        c = comp_of.get(i)
        head = w.head
        row = {
            "श्लोक": verse_id, "पङ्क्तिः": w.line + 1, "शब्दसङ्ख्या": i + 1, "शब्द": w.form,
            "धातु_प्रातिपदिक": w.morph.lemma if w.morph else "", "व्याकरणम्": grammar_of(w), "कारकम्": w.role,
            "शीर्ष_सं": 0 if head is None else head + 1,
            "शीर्षशब्दः": reading.words[head].form if head is not None and head < len(reading.words) else "",
            "समासः": c.samasa if c else "", "समास_सं": comp_no[c.id] if c else "",
            "अन्वय_सं": position.get(i, ""), "अर्थः": w.gloss,
        }
        rows.append({k: clean(v) for k, v in row.items()} | {k: "" for k in REVIEW_COLUMNS})
    return rows


def failed_row(verse_id: str, error: str) -> dict[str, str]:
    return {k: "" for k in COLUMNS + REVIEW_COLUMNS} | {"श्लोक": verse_id, "शब्द": "(विश्लेषणं न सिद्धम्)",
                                                       "टिप्पणी": clean(error)[:120]}


def to_tsv(rows: Sequence[dict[str, str]], comments: Sequence[str] = ()) -> str:
    cols = COLUMNS + REVIEW_COLUMNS
    lines = [f"# {c}" for c in list(HEADER) + list(comments)] + ["\t".join(cols)]
    lines += ["\t".join(clean(r.get(c, "")) for c in cols) for r in rows]
    return "\n".join(lines) + "\n"


def parse_range(spec: str) -> list[int]:
    lo, _, hi = spec.partition("-")
    return list(range(int(lo), int(hi or lo) + 1))


def export(verses: Sequence[int], analyze: Any, gold: Any) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for n in verses:
        vid = gold.verse(n)["id"]
        try:
            rows += rows_for(analyze(gold.verse_text(n), verse_id=vid).readings[0], vid)
        except BaseException as exc:  # one failing verse (even a Rust panic) must not lose the sheet
            if isinstance(exc, (KeyboardInterrupt, SystemExit)):
                raise
            rows.append(failed_row(vid, f"{type(exc).__name__}: {exc}"))
    return rows


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--verses", default="1-79")
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    from mayur import gold
    from mayur.pipeline import analyze_verse

    rows = export(parse_range(args.verses), analyze_verse, gold)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(to_tsv(rows, [f"verses {args.verses}; {gold.load()['source']}"]), encoding="utf-8")
    print(f"{len(rows)} rows -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
