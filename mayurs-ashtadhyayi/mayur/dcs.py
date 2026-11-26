"""Reader for the Digital Corpus of Sanskrit (CoNLL-U, IAST). Everything it returns is Devanagari.

The IAST of the corpus is converted exactly once, here, with ``mayur.lipi.devanagari``.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import random
from typing import Any, Iterator, Optional

from mayur.lipi import devanagari

VIRAMA = "्"
_VISARGA = "ः"
_ANUSVARA = "ं"
_R_LEMMAS = frozenset({"पुनर्", "अन्तर्", "प्रातर्"})


@lru_cache(maxsize=500_000)
def _deva(text: str) -> str:
    return devanagari(text, "iast") if text and text != "_" else ""


def _visarga_is_r(unsandhied: str, lemma: str, feats: dict[str, str]) -> bool:
    """The final visarga stands for र्: र्-final words (पुनर्, गिर्), and of ऋ-stems the forms in
    -उः (पितुर्, 6.1.111 with 8.2.24) and the vocative singular (पितर्)."""
    if lemma.endswith("र्") or lemma in _R_LEMMAS:
        return True
    if lemma.endswith(("ऋ", "ृ")):
        vocative = feats.get("Case") == "Voc" and feats.get("Number") == "Sing"
        return unsandhied.endswith("ु" + _VISARGA) or vocative
    return False


def pada_form(unsandhied: str, lemma: str, feats: dict[str, str] | None = None) -> str:
    """Grammatical (padapatha) form: final visarga -> स् or र् (see ``_visarga_is_r``), ं -> म्."""
    if not unsandhied:
        return unsandhied
    if unsandhied.endswith(_VISARGA):
        return unsandhied[:-1] + ("र्" if _visarga_is_r(unsandhied, lemma, feats or {}) else "स्")
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
        "form": pada_form(unsandhied, lemma, feats),
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


def split_files(name: str) -> list[dict[str, Any]]:
    """Entries ``{"file": absolute path, "verses": [first, last] | None}`` of the split ``name``
    ("train" | "dev" | "test") from data/derived/splits.json; ``[]`` when the manifest is missing."""
    from mayur.resources import data_dir, derived

    root = data_dir() / "dcs" / "sanskrit" / "dcs" / "data" / "conllu"
    return [{"file": str(root / e["file"]), "verses": e["verses"]} for e in derived("splits.json").get(name, [])]


def gold_lines(files: Any, limit: Optional[int] = None, seed: int = 0) -> Iterator[dict[str, Any]]:
    """Gold half-verses in the format of ``mayur.gold`` lines (text, compact, iast, words, ...).

    ``files``: paths or ``split_files`` entries. With ``limit`` a seeded random sample is yielded.
    """
    lines = []
    for entry in files:
        path, span = (entry["file"], entry.get("verses")) if isinstance(entry, dict) else (entry, None)
        for sent in iter_sentences(path):
            if span and not span[0] <= sent["sent_counter"] <= span[1]:
                continue
            lines.append({
                "text": sent["text"], "compact": compact(sent["text"]), "iast": sent["iast"],
                "chapter": sent["chapter"], "verse": sent["sent_counter"],
                "words": [{"form": t["form"], "lemma": t["lemma"], "upos": t["upos"], "feats": t["feats"],
                           "compound_member": t["compound_member"]} for t in sent["tokens"]],
            })
    if limit is not None and limit < len(lines):
        lines = random.Random(seed).sample(lines, limit)
    yield from lines
