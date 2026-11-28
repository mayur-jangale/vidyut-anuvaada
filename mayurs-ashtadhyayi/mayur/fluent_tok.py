"""Tokens of the rule-based fluent layer and the small predicates its rules share."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from . import english
from .model import Reading, Word

PUNCT = {",", ";", ".", "?", "!", ":"}


@dataclass(frozen=True)
class Tok:
    text: str
    word: Optional[int] = None
    glue: bool = False  # written against the previous token with no space ("great" + "ness")




def _w(reading: Reading, t: Tok) -> Optional[Word]:
    return reading.words[t.word] if t.word is not None else None


def _is_name(w: Optional[Word]) -> bool:
    return bool(w and w.gloss and w.gloss[0].isupper())


def _pronoun(w: Optional[Word]) -> bool:
    return bool(w and w.morph and english.is_pronoun(w.morph.lemma))
