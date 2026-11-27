"""Genitive owners decided by position (part of mayur.vakya; षष्ठी शेषे 2.3.50 licenses the link).

* ते, मे, नः, वः — the enclitic forms of युष्मद्/अस्मद् (8.1.20–22) never open a pāda (8.1.18
  अनुदात्तं सर्वमपादादौ) and lean on the word before them: अधिकारः ते 'your right'. Directly after a
  noun they belong to it.
* a pronoun in the षष्ठी right before another genitive noun is that noun's owner: मम मित्रस्य पुत्रः.

Taking the neighbouring word is a choice among the readings 2.3.50 allows, not a rule.
"""

from __future__ import annotations

from typing import Optional

from mayur.model import Word
from mayur.shabdabodha import (FIRST_PERSON, PRATHAMA, PRONOUNS, SAMBODHANA, SECOND_PERSON, SHASHTHI, is_finite,
                               lemma_class)

ENCLITIC_PRONOUN = {"ते", "मे", "नः", "वः", "नस्", "वस्"}


def _noun(words: list[Word], j: int) -> bool:
    m = words[j].morph
    return m is not None and not words[j].in_compound and m.kind == "subanta" and not m.krt \
        and lemma_class(m.lemma) == "noun"


def enclitic_owner(words: list[Word], g: int) -> Optional[int]:
    """The noun right before an enclitic ते/मे of the षष्ठी (no particle between)."""
    if words[g].form not in ENCLITIC_PRONOUN or g == 0 or words[g - 1].line != words[g].line:
        return None
    m = words[g - 1].morph
    return g - 1 if _noun(words, g - 1) and m.vibhakti not in (SHASHTHI, SAMBODHANA) else None


def genitive_after(words: list[Word], g: int, group: list[int]) -> Optional[int]:
    """मम मित्रस्य: the genitive noun right after a genitive pronoun, outside its own phrase."""
    m = words[g].morph
    j = g + 1
    if not (m.lemma in FIRST_PERSON | SECOND_PERSON | PRONOUNS) or j >= len(words) or j in group \
            or words[j].line != words[g].line:
        return None
    return j if _noun(words, j) and words[j].morph.vibhakti == SHASHTHI else None


def _adjacent_nominal(words: list[Word], g: int, over_verb: bool = False,
                      span: Optional[tuple[int, int]] = None) -> Optional[int]:
    """Non-genitive nominal next to the genitive phrase (skipping particles), following first; with
    ``over_verb`` an oblique noun standing after the verb counts too (सिंहस्य प्रविशन्ति मुखे). ``span``:
    first and last word of the genitive phrase (मम भोक्तुकामस्य विघ्नम्: the noun after the whole phrase)."""
    first, last = span or (g, g)
    for step in (1, -1):
        j = (last if step == 1 else first) + step
        crossed = False
        while 0 <= j < len(words) and words[j].line == words[g].line and words[j].morph is not None \
                and (words[j].morph.kind == "avyaya" or (over_verb and is_finite(words[j].morph))
                     or words[j].in_compound or words[j].morph.vibhakti == SAMBODHANA):  # (the address stands
            # outside the clause, 2.3.47 / 8.1.19: नाघम् प्रजेश बालानाम्; a compound is reached at its final member)
            crossed = crossed or is_finite(words[j].morph)
            j += step
        if crossed and step == 1 and 0 <= j < len(words) and words[j].morph is not None \
                and words[j].morph.vibhakti == PRATHAMA:
            continue  # कस्य बिभ्यति देवास्: the nominative after the verb is its subject, not the genitive's noun
        # (कालः गच्छति धीमताम्: with nothing after it, a verse-final genitive reaches back over the verb)
        if 0 <= j < len(words) and words[j].line == words[g].line and not words[j].in_compound \
                and words[j].morph is not None and words[j].morph.kind == "subanta" \
                and words[j].morph.vibhakti not in (SHASHTHI, SAMBODHANA):
            return j
    return None
