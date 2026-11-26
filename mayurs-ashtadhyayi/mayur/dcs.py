"""Parser for Digital Corpus of Sanskrit (DCS) CoNLL-U files, plus form normalisation.

DCS data: Oliver Hellwig, CC BY 4.0. All outputs of this module are SLP1 except
where a field name says otherwise.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterator, Optional

from mayur.translit import iast_to_slp1

# Indeclinables that keep a final r in padapatha / vidyut-kosha.
R_FINAL_AVYAYA = frozenset({"punar", "antar", "prAtar", "svar"})
_VOWELS = set("aAiIuUfFxXeEoO")


def _slp1(iast: str) -> str:
    return iast_to_slp1(iast.replace("ṁ", "ṃ"))


def _int(line: str) -> Optional[int]:
    v = line.split("=", 1)[1].strip()
    return int(v) if v.isdigit() else None


def _parse_feats(s: str) -> dict[str, str]:
    if not s or s == "_":
        return {}
    out: dict[str, str] = {}
    for part in s.split("|"):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k] = v
    return out


def _parse_misc(s: str) -> dict[str, str]:
    return _parse_feats(s)


def pada_form(unsandhied_slp1: str, lemma_slp1: str = "") -> str:
    """Convert a DCS unsandhied form to vidyut-kosha style.

    Final ``H`` becomes ``s`` (``rAmaH`` -> ``rAmas``), or ``r`` when the lemma ends in
    ``r``/``f`` (vocatives such as ``pitaH`` of ``pitf``) or is an r-final indeclinable
    (``punaH`` of ``punar``). Final ``M`` becomes ``m``.
    """
    f = unsandhied_slp1
    if not f:
        return f
    if f.endswith("H"):
        if lemma_slp1 in R_FINAL_AVYAYA or lemma_slp1.endswith(("r", "f")):
            return f[:-1] + "r"
        return f[:-1] + "s"
    if f.endswith("M"):
        return f[:-1] + "m"
    return f


_NO_SPACE_AFTER = set("MH")


def compact_orthography(text_slp1: str) -> str:
    """Turn DCS's spaced text into conventional compact writing.

    A space after a chunk ending in a consonant (other than ``M``/``H``) is deleted;
    spaces after vowels, ``M`` and ``H`` stay.
    """
    chunks = text_slp1.split()
    out: list[str] = []
    for i, ch in enumerate(chunks):
        out.append(ch)
        if i + 1 < len(chunks):
            last = ch[-1]
            if last in _VOWELS or last in _NO_SPACE_AFTER or not last.isalpha():
                out.append(" ")
    return "".join(out)


def _token(cols: list[str], mwt: Optional[tuple[int, int]]) -> dict[str, Any]:
    misc = _parse_misc(cols[9])
    form = _slp1(cols[1])
    lemma = _slp1(cols[2])
    unsand = _slp1(misc["Unsandhied"]) if misc.get("Unsandhied") else form
    feats = _parse_feats(cols[5])
    return {
        "id": int(cols[0]),
        "surface": form,
        "form": form,
        "lemma": lemma,
        "upos": cols[3],
        "feats": feats,
        "unsandhied": unsand,
        "is_compound_member": feats.get("Case") == "Cpd",
        "mwt": mwt,
        "lemma_id": misc.get("LemmaId"),
        "word_sem": misc.get("WordSem", ""),
    }


def iter_sentences(path: str | Path) -> Iterator[dict[str, Any]]:
    """Yield sentence dicts: text, sent_counter, sent_subcounter, chapter, tokens."""
    chapter = ""
    cur: Optional[dict[str, Any]] = None
    mwts: list[tuple[int, int]] = []

    def finish() -> Optional[dict[str, Any]]:
        return cur if cur and cur["tokens"] else None

    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if line.startswith("## chapter:"):
                chapter = line.split(":", 1)[1].strip()
            elif line.startswith("# text ="):
                done = finish()
                if done:
                    yield done
                cur = {"text": line.split("=", 1)[1].strip(), "sent_counter": None,
                       "sent_subcounter": None, "chapter": chapter, "tokens": []}
                mwts = []
            elif line.startswith("# sent_counter") and cur is not None:
                cur["sent_counter"] = _int(line)
            elif line.startswith("# sent_subcounter") and cur is not None:
                cur["sent_subcounter"] = _int(line)
            elif line and line[0].isdigit() and cur is not None:
                cols = line.split("\t")
                if len(cols) < 10:
                    continue
                if "-" in cols[0]:
                    a, b = cols[0].split("-")
                    mwts.append((int(a), int(b)))
                    continue
                n = int(cols[0])
                span = next(((a, b) for a, b in mwts if a <= n <= b), None)
                cur["tokens"].append(_token(cols, span))
    done = finish()
    if done:
        yield done
