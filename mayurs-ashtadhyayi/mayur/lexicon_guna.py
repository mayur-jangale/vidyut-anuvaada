"""Older imperatives: द्विषावहै for द्वेषावहै (मा विद्विषावहै), ब्रवीहि for ब्रूहि.

3.4.92 आडुत्तमस्य पिच्च makes the first-person endings of लोट् पित्, so a light penultimate vowel
takes guṇa before them (7.3.86 पुगन्तलघूपधस्य च): द्वेषाणि, द्वेषावहै. The older language also has the
form without guṇa. It is found here by the rule form: the vowel is strengthened, and the form is
accepted only if the lexicon lists the result as a first-person imperative. Labelled ārṣa, not derived.

7.3.93 ब्रुव ईट् gives ई only before a consonant-initial पित् ending (ब्रवीति, ब्रवीतु); हि is not पित् (3.4.87
सेर्ह्यपिच्च), so the rule form is ब्रूहि. The epic ब्रवीहि is labelled with it.
All strings Devanagari.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Callable, Sequence

from mayur import lipi
from mayur.model import Morph

Lookup = Callable[[str], Sequence[Morph]]
ARSHA = "arsha"
NOTE = ("ārṣa: a first-person imperative without guṇa; 3.4.92 आडुत्तमस्य पिच्च makes the ending पित्, so 7.3.86 gives "
        "the rule form {regular}. Older usage, labelled and not derived")
_ENDINGS = tuple(lipi.varnas(e) for e in ("आवहै", "आमहै", "आनि", "आणि", "आव", "आम", "ऐ"))
_GUNA = {"इ": ("ए",), "उ": ("ओ",), "ऋ": ("अ", "र्")}


BRAVIHI_NOTE = ("ārṣa: ब्रू with ई before हि; 7.3.93 ब्रुव ईट् gives ई only before a पित् ending and हि is not one "
                "(3.4.87), so the rule form is ब्रूहि. Epic usage, labelled and not derived")
_EPIC = {"ब्रवीहि": ("ब्रूहि", BRAVIHI_NOTE)}


def epic_imperative(form: str, padas: Lookup) -> tuple[Morph, ...]:
    """ब्रवीहि: the labelled reading of a listed epic imperative, with the analysis of its rule form."""
    if form not in _EPIC:
        return ()
    regular, note = _EPIC[form]
    return tuple(dict.fromkeys(replace(m, form=form, source=ARSHA, quality=1, handle=("special", note))
                               for m in padas(regular) if m.kind == "tinanta" and m.lakara == "लोट्"))


def first_imperative(form: str, padas: Lookup) -> tuple[Morph, ...]:
    """The labelled reading of ``form`` as a first-person imperative whose rule form has guṇa; () otherwise."""
    sounds = lipi.varnas(form)
    for ending in _ENDINGS:
        n = len(sounds) - len(ending)
        if n < 2 or sounds[n:] != ending or sounds[n - 2] not in _GUNA:
            continue  # the vowel must be light: one consonant between it and the ending
        regular = lipi.from_varnas(sounds[: n - 2] + _GUNA[sounds[n - 2]] + sounds[n - 1:])
        hits = [m for m in padas(regular) if m.kind == "tinanta" and m.lakara == "लोट्" and m.purusha == "उत्तमपुरुष"
                and m.quality >= 2]
        note = NOTE.format(regular=lipi.pausa(regular))
        return tuple(dict.fromkeys(replace(m, form=form, source=ARSHA, quality=1, handle=("special", note)) for m in hits))
    return ()
