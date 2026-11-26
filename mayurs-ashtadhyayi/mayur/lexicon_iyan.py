"""Monosyllabic ई / ऊ feminines (श्री, धी, ह्री, भी, भू) that take इयङ् / उवङ् before vowels.

6.4.77 अचि श्नुधातुभ्रुवां य्वोरियङुवङौ. vidyut derives भ्रू correctly but applies the plain
यण् rule to these stems (श्र्यौ for श्रियौ), so their paradigm is built here on the model of
vidyut's own forward derivation of भ्रू. Such analyses are marked ``source="special"`` and are
not claimed as derived by vidyut.
"""

from __future__ import annotations

from dataclasses import replace
from functools import lru_cache

from mayur import bridge, lipi
from mayur.model import Morph

MODEL = "भ्रू"
STEMS = ("श्री", "धी", "ह्री", "भी", "भू")
NOTE = ("इयङ्/उवङ् before a vowel ending by 6.4.77 (अचि श्नुधातुभ्रुवां य्वोरियङुवङौ); vidyut does not apply "
        "it to this stem, so the form is built on the model of its derivation of भ्रू")
_GLIDE = {"ई": ("इ", "य्"), "ऊ": ("उ", "व्")}
_RETROFLEXING = frozenset({"र्", "ष्", "ऋ", "ॠ"})


def _transfer(model_form: str, stem: str) -> str:
    """The form of ``stem`` that corresponds to ``model_form`` of भ्रू."""
    sounds, head, target = lipi.varnas(model_form), lipi.varnas(MODEL), lipi.varnas(stem)
    weak = head[:-1] + _GLIDE[head[-1]]
    if sounds[: len(weak)] == weak:
        return lipi.from_varnas(target[:-1] + _GLIDE[target[-1]] + sounds[len(weak):])
    ending = sounds[len(head):]
    if not _RETROFLEXING & set(target):  # the ण of भ्रूणाम् is caused by its र् (8.4.2)
        ending = tuple("न्" if v == "ण्" else v for v in ending)
    return lipi.from_varnas(target + ending)


@lru_cache(maxsize=1)
def _table() -> dict[str, tuple[Morph, ...]]:
    table: dict[str, list[Morph]] = {}
    for handle, template in bridge.subanta_paradigm(MODEL, "स्त्रीलिङ्ग"):
        for model_form in bridge.derived_texts(handle):
            for stem in STEMS:
                form = _transfer(model_form, stem)
                morph = replace(template, form=form, lemma=stem, source="special", quality=3,
                                handle=("special", NOTE))
                table.setdefault(form, []).append(morph)
    return {form: tuple(dict.fromkeys(morphs)) for form, morphs in table.items()}


def iyan_uvan(form: str) -> tuple[Morph, ...]:
    """Analyses of ``form`` as a case form of श्री, धी, ह्री, भी or भू."""
    return _table().get(form, ())
