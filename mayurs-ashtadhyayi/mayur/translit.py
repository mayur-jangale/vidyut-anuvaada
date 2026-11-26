"""Script conversion via vidyut-lipi. SLP1 is the internal encoding."""

from __future__ import annotations

from vidyut.lipi import Scheme, detect, transliterate


def to_slp1(text: str) -> str:
    scheme = detect(text) or Scheme.Slp1
    if scheme == Scheme.Slp1:
        return text
    return transliterate(text, scheme, Scheme.Slp1)


def to_deva(slp1: str) -> str:
    return transliterate(slp1, Scheme.Slp1, Scheme.Devanagari)


def to_iast(slp1: str) -> str:
    return transliterate(slp1, Scheme.Slp1, Scheme.Iast)


def iast_to_slp1(iast: str) -> str:
    return transliterate(iast, Scheme.Iast, Scheme.Slp1)
