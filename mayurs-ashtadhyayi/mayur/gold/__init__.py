"""Gold data: Ramayana, Balakanda sarga 1, from the Digital Corpus of Sanskrit (CC BY 4.0)."""

from __future__ import annotations

import json
from functools import lru_cache
from itertools import groupby
from pathlib import Path
from typing import Any, Iterable

from mayur import dcs
from mayur.lipi import devanagari

GOLD_FILE = Path(__file__).with_name("ramayana_bala_1.json")
CHAPTER_ID = "1067"
SOURCE = "Digital Corpus of Sanskrit (Oliver Hellwig), Rāmāyaṇa, Bālakāṇḍa 1"
LICENSE = "CC BY 4.0"
LINE_SEP, VERSE_END = " । ", " ॥"


def _num(n: int) -> str:
    return devanagari(str(n), "iast")


def build(sentences: Iterable[dict]) -> dict[str, Any]:
    """Gold document from the DCS sentences of the chapter (pure)."""
    sents = [s for s in sentences if s["chapter_id"] == CHAPTER_ID]
    verses = []
    for number, group in groupby(sents, key=lambda s: s["sent_counter"]):
        lines = [{
            "text": s["text"],
            "compact": dcs.compact(s["text"]),
            "iast": s["iast"],
            "words": [{"form": t["form"], "lemma": t["lemma"], "upos": t["upos"], "feats": t["feats"],
                       "compound_member": t["compound_member"]} for t in s["tokens"]],
        } for s in group]
        verses.append({"id": f"रामायण १.१.{_num(number)}", "number": number, "lines": lines})
    return {"source": SOURCE, "license": LICENSE, "verses": verses}


@lru_cache(maxsize=1)
def load() -> dict[str, Any]:
    return json.loads(GOLD_FILE.read_text(encoding="utf-8"))


def verse(n: int) -> dict[str, Any]:
    for v in load()["verses"]:
        if v["number"] == n:
            return v
    raise KeyError(n)


def verse_text(n: int) -> str:
    """Compact Devanagari half-verses of verse ``n`` joined by " । " and ending " ॥"."""
    return LINE_SEP.join(line["compact"] for line in verse(n)["lines"]) + VERSE_END


def write(conllu_files: Iterable[Path], dest: Path = GOLD_FILE) -> int:
    doc = build(s for f in conllu_files for s in dcs.iter_sentences(f))
    dest.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(doc["verses"])
