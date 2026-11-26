"""Script handling. The whole package works in Devanagari.

Text is handled as a sequence of varnas (sounds) written in Devanagari: vowels as
``अ आ इ``, consonants with virama ``क् ख्``, plus anusvara, visarga and avagraha.
Roman sound codes exist only inside this module and ``mayur.bridge``, because
vidyut's engines require them; nothing else in the package reads or writes them.
"""

from __future__ import annotations

import re
from functools import lru_cache

from vidyut.lipi import Scheme, transliterate

_DEVANAGARI = re.compile(r"[ऀ-ॿ]")
_SPECIAL = {"M": "ं", "H": "ः", "'": "ऽ", "~": "ँ", " ": " "}


class AmbiguousScript(ValueError):
    """Plain ASCII input: it could be any of several romanisations."""


def devanagari(text: str, script: str | None = None) -> str:
    """``text`` in Devanagari. Accepts Devanagari or IAST; plain ASCII is refused as ambiguous."""
    if script == "devanagari" or (script is None and _DEVANAGARI.search(text)):
        return text
    if script == "iast" or (script is None and not text.isascii()):
        return transliterate(text, Scheme.Iast, Scheme.Devanagari)
    raise AmbiguousScript("plain ASCII input is ambiguous; write the verse in Devanagari or IAST")


def iast(deva: str) -> str:
    return transliterate(deva, Scheme.Devanagari, Scheme.Iast) if deva else ""


def to_code(deva: str) -> str:
    """Roman sound code for vidyut. For ``mayur.bridge`` only."""
    return transliterate(deva, Scheme.Devanagari, Scheme.Slp1) if deva else ""


def from_code(code: str) -> str:
    """Devanagari for a vidyut sound-code string. For ``mayur.bridge`` only."""
    return transliterate(code, Scheme.Slp1, Scheme.Devanagari) if code else ""


@lru_cache(maxsize=None)
def _varna_of(code_char: str) -> str:
    return _SPECIAL.get(code_char) or from_code(code_char)


@lru_cache(maxsize=200_000)
def varnas(deva: str) -> tuple[str, ...]:
    """The sounds of ``deva`` in order: ``varnas("रामस्") == ("र्", "आ", "म्", "अ", "स्")``."""
    return tuple(_varna_of(ch) for ch in to_code(deva))


def from_varnas(sounds) -> str:
    """Inverse of :func:`varnas`."""
    return from_code("".join(_code_of(v) for v in sounds))


@lru_cache(maxsize=None)
def _code_of(varna: str) -> str:
    for code_char, special in _SPECIAL.items():
        if varna == special:
            return code_char
    return to_code(varna)


def pausa(pada: str) -> str:
    """A pada as it is written in isolation: final स् or र् becomes visarga (8.3.15)."""
    sounds = varnas(pada)
    if sounds and sounds[-1] in ("स्", "र्"):
        return from_varnas(sounds[:-1] + ("ः",))
    return pada
