"""Short English glosses for lemmas: own table, then DCS senses, DCS dictionary, vidyut."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

from . import resources, ud
from .model import Morph, Reading

_OWN = Path(__file__).parent / "annotations" / "gloss.json"
_MARKER = re.compile(r"\s*\((?:p|a|n|s|r|v)\)\s*$")
_BRACKETED = re.compile(r"[\[\(][^\])]*[\]\)]")
_GRAMMAR_ONLY = re.compile(r"^(?:m|f|n|mfn|adj|ind|indecl|ifc|cf|see|vb)\.?$", re.I)


@lru_cache(maxsize=1)
def _own() -> dict[str, str]:
    try:
        return json.loads(_OWN.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


_ARTICLES = ("the ", "a ", "an ")
_TRAILING = {"or", "to", "of", "and", "the", "a", "an", "in", "on", "with", "for", "by", "as"}
_CUT = re.compile(r"\s+(?:that|which|who|whose|having)\s+|\s+or\s+|\s+and\s+|[;,/]|\s+-\s+")
_MAX_CLEAN = 3


def _base_verb(word: str) -> str:
    """Best-effort bare verb from a participle ("addressed" -> "address")."""
    if word.endswith("ied") and len(word) > 4:
        return word[:-3] + "y"
    if word.endswith("ed") and len(word) > 4:
        stem = word[:-2]
        if len(stem) > 2 and stem[-1] == stem[-2] and stem[-1] not in "lsfz":
            return stem[:-1]
        if stem[-1] in "vcuz" or (stem[-1] in "gt" and stem[-2] in "aeiou" and stem[-3:-2] not in "aeiou"):
            return stem + "e"
        return stem
    return word


def clean(text: str, verb: bool = False) -> str:
    """A clean head of a dictionary sense: no articles, cut at 'or'/','/';', at most 3 words."""
    text = _BRACKETED.sub(" ", text or "")
    head = _CUT.split(text)[0].strip(" .:-")
    for art in _ARTICLES:
        if head.lower().startswith(art):
            head = head[len(art):]
    if head.lower().startswith("to "):
        head = head[3:]
    words = head.split()
    if verb:
        if words and words[0] in ("be", "become", "being") and len(words) > 1:
            words = [_base_verb(words[1])] + words[2:]
        words = words[:1] if words and len(words) > 1 and words[1] in _TRAILING else words
    words = words[:_MAX_CLEAN]
    while words and words[-1].lower() in _TRAILING:
        words.pop()
    return " ".join(words)


def first_sense(text: str, verb: bool = False) -> str:
    """First usable sense of a ';'/','-separated meaning string, cleaned (see ``clean``)."""
    for part in re.split(r"[;,]", text or ""):
        part = _MARKER.sub("", part)
        if part.strip().startswith(("[", "(")):
            continue
        g = clean(part, verb)
        if not g or _GRAMMAR_ONLY.match(g) or any(x in g for x in ('"', "ifc", "°", "=")):
            continue
        return g
    return ""


def _keys(m: Morph) -> list[str]:
    keys = [m.lemma]
    if m.prefixes and m.root:
        keys.insert(0, "".join(m.prefixes) + m.root)
    for extra in (m.stem, m.root):
        if extra and extra not in keys:
            keys.append(extra)
    return [k for k in keys if k]


def _common(entries: list, verb: bool) -> str:
    for entry in entries or []:
        for part in str(entry.get("meanings", "")).split(";"):
            g = first_sense(part, verb)
            if g and not g.lower().startswith("name") and not g[:1].isupper():
                return g
    return ""


def lookup(m: Morph) -> tuple[str, str]:
    """(gloss, source) for one analysis; ("", "none") when nothing is known."""
    keys = _keys(m)
    verb = m.root is not None
    own = _own()
    if m.krt in ("ण्यत्", "यत्", "क्यप्", "तव्य", "अनीयर्") and m.stem in own:
        return own[m.stem], "own"  # a noun that only looks like a gerundive: वाक्य "speech"
    for k in keys:
        if k in own:
            return own[k], "own"
    senses = resources.derived("dcs_senses.json") or {}
    dictionary = resources.derived("dcs_dict.json") or {}
    for k in keys:
        g = first_sense(str(senses.get(k, "")), verb)
        if g.lower().startswith("name") or g[:1].isupper():  # proper-noun reading: prefer a common sense
            common = _common(dictionary.get(k, []), verb)
            if common:
                return common, "dcs-dictionary"
            continue
        if g:
            return g, "dcs-sense"
    for k in keys:
        for entry in dictionary.get(k, []) or []:
            for part in str(entry.get("meanings", "")).split(";"):
                g = first_sense(part, verb)
                if g and not g.lower().startswith("name"):
                    return g, "dcs-dictionary"
    g = first_sense(m.root_gloss or "", verb)
    if g:
        return g, "vidyut-dhatupatha"
    return "", "none"


MIN_SENSE_CONFIDENCE = 0.5


def lookup_in_context(reading: Reading, index: int) -> tuple[str, str]:
    """(gloss, source) of ``reading.words[index]``: our own table first, then the sense the DCS
    sense model picks from the context ("dcs-sense-context"), else the context-free ``lookup``."""
    m = reading.words[index].morph
    if m is None:
        return "", "none"
    plain = lookup(m)
    if plain[1] == "own":
        return plain
    from . import senses  # lazy: senses -> ud -> lexicon

    label, confidence = senses.choose(ud.lemma(m), senses.context_of(reading, index))
    if label and confidence >= MIN_SENSE_CONFIDENCE:
        text = senses.gloss_of(label)
        if text:
            return text, "dcs-sense-context"
    return plain
