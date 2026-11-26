"""Short English glosses for lemmas: own table, then DCS senses, DCS dictionary, vidyut."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

from . import resources
from .model import Morph

_OWN = Path(__file__).parent / "annotations" / "gloss.json"
_MAX_WORDS = 5
_MARKER = re.compile(r"\s*\((?:p|a|n|s|r|v)\)\s*$")
_BRACKETED = re.compile(r"[\[\(][^\])]*[\]\)]")
_GRAMMAR_ONLY = re.compile(r"^(?:m|f|n|mfn|adj|ind|indecl|ifc|cf|see|vb)\.?$", re.I)


@lru_cache(maxsize=1)
def _own() -> dict[str, str]:
    try:
        return json.loads(_OWN.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def first_sense(text: str) -> str:
    """First usable sense of a ';'/','-separated meaning string, bare and at most 5 words."""
    for part in re.split(r"[;,]", text or ""):
        part = _MARKER.sub("", part)
        if part.strip().startswith(("[", "(")):
            continue
        part = _BRACKETED.sub("", part).strip(" .:-")
        if part.lower().startswith("to "):
            part = part[3:]
        if not part or _GRAMMAR_ONLY.match(part):
            continue
        return " ".join(part.split()[:_MAX_WORDS])
    return ""


def _keys(m: Morph) -> list[str]:
    keys = [m.lemma]
    if m.prefixes and m.root:
        keys.insert(0, "".join(m.prefixes) + m.root)
    for extra in (m.stem, m.root):
        if extra and extra not in keys:
            keys.append(extra)
    return [k for k in keys if k]


def lookup(m: Morph) -> tuple[str, str]:
    """(gloss, source) for one analysis; ("", "none") when nothing is known."""
    keys = _keys(m)
    own = _own()
    for k in keys:
        if k in own:
            return own[k], "own"
    senses = resources.derived("dcs_senses.json") or {}
    for k in keys:
        g = first_sense(str(senses.get(k, "")))
        if g:
            return g, "dcs-sense"
    dictionary = resources.derived("dcs_dict.json") or {}
    for k in keys:
        for entry in dictionary.get(k, []) or []:
            g = first_sense(str(entry.get("meanings", "")))
            if g:
                return g, "dcs-dictionary"
    g = first_sense(m.root_gloss or "")
    if g:
        return g, "vidyut-dhatupatha"
    return "", "none"
