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
_OM = "ॐ"


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
    """The sounds of ``deva`` in order: ``varnas("रामस्") == ("र्", "आ", "म्", "अ", "स्")``.

    The syllable ॐ is kept as one unit.
    """
    if _OM in deva:
        head, _, tail = deva.partition(_OM)
        return varnas(head) + (_OM,) + varnas(tail)
    return tuple(_varna_of(ch) for ch in to_code(deva))


_MATRA = {"अ": "", "आ": "ा", "इ": "ि", "ई": "ी", "उ": "ु", "ऊ": "ू", "ऋ": "ृ", "ॠ": "ॄ", "ऌ": "ॢ",
          "ॡ": "ॣ", "ए": "े", "ऐ": "ै", "ओ": "ो", "औ": "ौ"}
_VIRAMA = "्"


def from_varnas(sounds) -> str:
    """Inverse of :func:`varnas`, composed directly in Devanagari.

    A vowel after a consonant becomes its matra; a vowel after a vowel stays an independent
    letter, so a hiatus such as ते + आ is written तेआ and never lost.
    """
    out: list[str] = []
    after_consonant = False
    for v in sounds:
        if after_consonant and v in _MATRA:
            out[-1] = out[-1][: -len(_VIRAMA)] + _MATRA[v]
            after_consonant = False
        else:
            out.append(v)
            after_consonant = len(v) > 1 and v.endswith(_VIRAMA)
    return "".join(out)


def pausa(pada: str) -> str:
    """A pada as it is written in isolation: final स् or र् becomes visarga (8.3.15)."""
    sounds = varnas(pada)
    if sounds and sounds[-1] in ("स्", "र्"):
        return from_varnas(sounds[:-1] + ("ः",))
    return pada
