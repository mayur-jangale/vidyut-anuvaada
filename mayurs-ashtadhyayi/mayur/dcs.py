"""Reader for the Digital Corpus of Sanskrit (CoNLL-U, IAST). Everything it returns is Devanagari.

The IAST of the corpus is converted exactly once, here, with ``mayur.lipi.devanagari``.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterator

from mayur.lipi import devanagari

VIRAMA = "्"
_VISARGA = "ः"
_ANUSVARA = "ं"
_R_LEMMAS = frozenset({"पुनर्", "अन्तर्", "प्रातर्"})


def _deva(text: str) -> str:
    return devanagari(text, "iast") if text and text != "_" else ""


def pada_form(unsandhied: str, lemma: str) -> str:
    """Grammatical (padapatha) form: final visarga -> स् (र् after a lemma in र्/ऋ or पुनर् ...), ं -> म्."""
    if not unsandhied:
        return unsandhied
    if unsandhied.endswith(_VISARGA):
        r_final = lemma.endswith(("र्", "ऋ")) or lemma in _R_LEMMAS
        return unsandhied[:-1] + ("र्" if r_final else "स्")
    if unsandhied.endswith(_ANUSVARA):
        return unsandhied[:-1] + "म्"
    return unsandhied


_MATRA = {"अ": "", "आ": "ा", "इ": "ि", "ई": "ी", "उ": "ु", "ऊ": "ू", "ऋ": "ृ", "ॠ": "ॄ", "ए": "े",
          "ऐ": "ै", "ओ": "ो", "औ": "ौ"}


def compact(text: str) -> str:
    """Conventional compact writing: no space after a chunk ending in a consonant other than ं/ः.

    A final consonant meeting an initial vowel is written together (न्व् अस्मिन् -> न्वस्मिन्).
    """
    out = ""
    for chunk in text.split():
        if not out:
            out = chunk
        elif out.endswith(VIRAMA):
            if chunk[0] in _MATRA:
                out = out[:-1] + _MATRA[chunk[0]] + chunk[1:]
            else:
                out += chunk
        else:
            out += " " + chunk
    return out


def _int(text: str) -> int:
    text = text.strip()
    return int(text) if text.isdigit() else 0


def _parse_feats(raw: str) -> dict[str, str]:
    if not raw or raw == "_":
        return {}
    return dict(p.split("=", 1) for p in raw.split("|") if "=" in p)


def _parse_token(cols: list[str]) -> dict:
    misc = _parse_feats(cols[9]) if len(cols) > 9 else {}
    feats = _parse_feats(cols[5])
    lemma = _deva(cols[2])
    unsandhied = _deva(misc.get("Unsandhied", "")) or _deva(cols[1])
    return {
        "form": pada_form(unsandhied, lemma),
        "lemma": lemma,
        "upos": cols[3],
        "feats": {k: v for k, v in feats.items() if k != "Case" or v != "Cpd"},
        "unsandhied": unsandhied,
        "compound_member": feats.get("Case") == "Cpd",
        "word_sem": misc.get("WordSem", ""),
    }


def parse_sentences(lines: Iterator[str] | list[str]) -> Iterator[dict]:
    """Sentences (half-verses) of CoNLL-U ``lines``."""
    chapter, chapter_id, text_id = "", "", ""
    cur: dict | None = None
    for raw in list(lines) + [""]:
        line = raw.rstrip("\n")
        if line.startswith("## chapter_id:"):
            chapter_id = line.split(":", 1)[1].strip()
        elif line.startswith("## text_id:"):
            text_id = line.split(":", 1)[1].strip()
        elif line.startswith("## chapter:"):
            chapter = line.split(":", 1)[1].strip()
        elif line.startswith("# text ="):
            cur = {"iast": line.split("=", 1)[1].strip(), "chapter": _deva(chapter.lower()), "chapter_id": chapter_id, "text_id": text_id,
                   "sent_counter": 0, "sent_subcounter": 0, "tokens": []}
            cur["text"] = _deva(cur["iast"])
        elif cur is not None and line.startswith("# sent_counter ="):
            cur["sent_counter"] = _int(line.split("=", 1)[1])
        elif cur is not None and line.startswith("# sent_subcounter ="):
            cur["sent_subcounter"] = _int(line.split("=", 1)[1])
        elif cur is not None and line and not line.startswith("#"):
            cols = line.split("\t")
            if len(cols) >= 4 and cols[0].isdigit():
                cur["tokens"].append(_parse_token(cols))
        elif not line and cur is not None:
            yield cur
            cur = None


def iter_sentences(path: str | Path) -> Iterator[dict]:
    """Sentences of one CoNLL-U file: text, chapter, sent_counter, sent_subcounter, tokens."""
    with open(path, encoding="utf-8") as fh:
        yield from parse_sentences(fh.readlines())
