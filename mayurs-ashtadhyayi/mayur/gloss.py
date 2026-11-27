"""Short English glosses for lemmas: own table, then DCS senses, DCS dictionary, vidyut."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Sequence

from . import lipi, resources, ud
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


_DRAFT = Path(__file__).parent / "annotations" / "gloss_draft.json"
_VERBAL_KINDS = frozenset({"verb"})


@lru_cache(maxsize=1)
def _draft() -> dict[str, list[str]]:
    """lemma -> [gloss, kind]: the Claude-drafted table for frequent lemmas (not human-verified)."""
    try:
        return json.loads(_DRAFT.read_text(encoding="utf-8"))["glosses"]
    except (OSError, ValueError, KeyError):
        return {}


_ROOTS = Path(__file__).parent / "annotations" / "gloss_roots.json"
_CELL = ("kind", "prayoga", "lakara", "purusha", "vacana", "krt", "vibhakti", "linga", "prefixes")


@lru_cache(maxsize=1)
def _roots() -> dict[str, list[str]]:
    """root|gaṇa (or the root as taught) -> [gloss, Dhātupāṭha sense]: roots whose classes differ in meaning."""
    try:
        return json.loads(_ROOTS.read_text(encoding="utf-8"))["roots"]
    except (OSError, ValueError, KeyError):
        return {}


def _by_class(m: Morph, rivals: Sequence[Morph]) -> str:
    """The gloss of the root in the class this form belongs to (पाति "protect", पिबति "drink"), or ''.

    Where the same form in the same cell also comes from the root's other class (पास्यति, कीर्ण) the form
    does not decide the class: the root's usual sense in the table, else nothing (the lemma's gloss stands)."""
    if m.root is None or not m.gana:
        return ""
    hit = _roots().get(m.dhatu or "") or _roots().get(f"{m.root}|{m.gana}")
    if not hit:
        return ""
    cell = tuple(getattr(m, f) for f in _CELL)
    if any(r.root == m.root and (r.gana, r.dhatu) != (m.gana, m.dhatu) and tuple(getattr(r, f) for f in _CELL) == cell
           for r in rivals):
        return _roots().get(m.root, [""])[0]  # the root's usual sense, where the table gives one
    return hit[0]


def _from_draft(m: Morph, keys: list[str]) -> str:
    """The drafted gloss whose kind fits the analysis: a root's gloss for verbal forms, a nominal
    or indeclinable gloss otherwise (मद् is "I" as a pronoun and "rejoice" as a root)."""
    draft = _draft()
    for k in keys:
        hit = draft.get(k)
        if hit and (hit[1] in _VERBAL_KINDS) == (m.root is not None and k != m.stem):
            return hit[0]
    return ""


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


_VOWELS = "अआइईउऊऋॠएऐओऔ"


def _composed(m: Morph, keys: list[str]) -> str:
    """A gloss built from the base word's own entry, for a nominal the tables lack:
    अशस्त्र "without weapon" (नञ्, 2.2.6; of a noun, as a बहुव्रीहि 2.2.24), अप्रिय "not dear",
    क्षेमतर "greater safety", प्रियतम "most dear" (5.3.55 अतिशायने तमबिष्ठनौ, 5.3.57 द्विवचनविभज्योपपदे तरबीयसुनौ).
    The corpus dictionary's first sense of such a word is often a rare one."""
    if m.root is not None:
        return ""
    own, draft = _own(), _draft()

    def entry(word: str) -> tuple[str, str]:
        row = draft.get(word) or ["", ""]
        return own.get(word) or row[0], row[1]

    for k in keys:
        sounds = lipi.varnas(k)
        rest = ""
        if len(sounds) > 3 and sounds[0] == "अ" and sounds[1] not in _VOWELS:
            rest = lipi.from_varnas(sounds[1:])
        elif len(sounds) > 4 and sounds[:2] == ("अ", "न्") and sounds[2] in _VOWELS:
            rest = lipi.from_varnas(sounds[2:])
        base, kind = entry(rest) if rest else ("", "")
        if base:
            return ("not " if kind == "adj" else "without ") + base
        for suffix, adjective, noun in (("तर", "more", "greater"), ("तम", "most", "greatest")):
            base, kind = entry(k[: -len(suffix)]) if k.endswith(suffix) and len(k) > 3 else ("", "")
            if base:
                return f"{adjective if kind == 'adj' else noun} {base}"
    return ""


def lookup(m: Morph, rivals: Sequence[Morph] = ()) -> tuple[str, str]:
    """(gloss, source) for one analysis; ("", "none") when nothing is known.

    ``rivals``: the word's other analyses, so that a root is glossed by its class only where the form decides it."""
    keys = _keys(m)
    verb = m.root is not None
    own = _own()
    by_class = _by_class(m, rivals)
    if m.krt in ("ण्यत्", "यत्", "क्यप्", "तव्य", "अनीयर्") and m.stem in own:
        return own[m.stem], "own"  # a noun that only looks like a gerundive: वाक्य "speech"
    for k in keys:
        if k == m.root and by_class and not m.prefixes:
            return (_from_draft(m, [m.stem]) if m.stem and m.stem != k else "") or by_class, "own-draft"
        if k in own and not (verb and k == m.root and _draft().get(k, ["", ""])[1] == "verb"):
            return own[k], "own"  # (an agent noun of the table, हन् "slayer", is not the gloss of the verb हन्)
    cited = ud.lemma(m)  # the corpus's citation form: समवे for सम् + अव + इ
    senses = resources.derived("dcs_senses.json") or {}
    dictionary = resources.derived("dcs_dict.json") or {}
    if by_class and m.prefixes and cited != keys[0]:
        # the corpus cites विकॄ "scatter" as विकृ: the entry of another verb (विकृ "change") is not its gloss
        return _from_draft(m, keys[:1]) or by_class, "own-draft"
    drafted = _from_draft(m, [cited])
    if drafted:
        return drafted, "own-draft"
    if m.prefixes and cited != m.root:
        # a prefixed verb the drafted table lacks: the dictionary entry of the prefixed verb itself
        # comes before the bare root's gloss (समवे "come together", not इ "go")
        g = _common(dictionary.get(cited, []), verb)
        if g:
            return g, "dcs-dictionary"
    if by_class:  # a prefixed verb without its own entry: its root in this class (निरस् from अस् "throw")
        return _from_draft(m, keys[:1]) or by_class, "own-draft"
    drafted = _from_draft(m, keys)
    if drafted:
        return drafted, "own-draft"
    for k in keys:
        g = first_sense(str(senses.get(k, "")), verb)
        if g.lower().startswith("name") or g[:1].isupper():  # proper-noun reading: prefer a common sense
            common = _common(dictionary.get(k, []), verb)
            if common:
                return common, "dcs-dictionary"
            continue
        if g:
            return g, "dcs-sense"
    composed = _composed(m, keys)
    if composed:
        return composed, "own-draft (composed)"
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
    plain = lookup(m, reading.words[index].analyses)
    if plain[1] in ("own", "own-draft"):  # a gloss written for the lemma comes before a corpus sense label
        return plain
    from . import senses  # lazy: senses -> ud -> lexicon

    label, confidence = senses.choose(ud.lemma(m), senses.context_of(reading, index))
    if label and confidence >= MIN_SENSE_CONFIDENCE:
        text = senses.gloss_of(label)
        if text:
            return text, "dcs-sense-context"
    return plain
