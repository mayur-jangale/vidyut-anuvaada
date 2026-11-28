"""Denominative verbs (नामधातु): a noun made into a root by क्यच्, क्यङ् or णिच्, derived forward by vidyut.

    नमस्यति   नमस् + क्यच्   3.1.19 नमोवरिवश्चित्रङः क्यच्
    पुत्रीयति   पुत्र + क्यच्   3.1.8 सुप आत्मनः क्यच् (7.4.33 क्यचि च: अ -> ई)
    श्येनायते   श्येन + क्यङ्   3.1.11 कर्तुः क्यङ् सलोपश्च
    उत्सुकयति  उत्सुक + णिच्  3.1.21 / 3.1.26 (तत्करोति तदाचष्टे)

The noun is guessed from what stands before the य of the form, kept only if the lexicon lists it,
and the form is accepted only when vidyut's forward derivation from noun + suffix gives exactly
that form. The analysis carries the vidyut handle, so the proof gate re-derives it.
All strings Devanagari.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Callable

from mayur import bridge, lipi
from mayur.model import Morph

_SUFFIXES = (("kyac", "क्यच्"), ("kyaN", "क्यङ्"), ("Ric", "णिच्"))
# what may stand before the य of a denominative stem -> the endings the noun may have had
_BEFORE_YA = {"ई": ("अ", "आ", "इ", "ई"), "आ": ("अ", "आ", "अस्", "अन्"), "ऊ": ("उ", "ऊ"), "अ": ("अ",), "स्": ("स्",)}
_VERB_FINALS = frozenset({"इ", "ए", "त्", "न्", "म्", "उ", "स्", "अ", "ऐ"})


def _bases(form: str) -> list[str]:
    """Noun stems that ``form`` may be a denominative of: the sounds before its last य, re-ended."""
    sounds = lipi.varnas(form)
    if len(sounds) < 5 or sounds[-1] not in _VERB_FINALS:
        return []
    out: list[str] = []
    for i in range(len(sounds) - 2, 1, -1):
        if sounds[i] != "य्":
            continue
        before = sounds[i - 1]
        for ending in _BEFORE_YA.get(before, ()):
            head = sounds[:i] if before == "स्" else sounds[: i - 1] + lipi.varnas(ending)
            out.append(lipi.from_varnas(head))
        break  # only the last य: the suffix stands right before the endings
    return list(dict.fromkeys(out))


@lru_cache(maxsize=2048)
def _paradigm(base: str) -> dict[str, tuple[Morph, ...]]:
    """form -> analyses for every active finite form of ``base`` + क्यच् / क्यङ् / णिच्."""
    from vidyut.prakriya import Dhatu, Lakara, Pada, Pratipadika, Prayoga, Purusha, Sanadi, Vacana

    table: dict[str, list[Morph]] = {}
    lakaras = (Lakara.Lat, Lakara.Lot, Lakara.Lan, Lakara.VidhiLin, Lakara.Lrt)
    for code, name in _SUFFIXES:
        try:
            dhatu = Dhatu.nama(Pratipadika.basic(lipi.to_code(base)), nama_sanadi=getattr(Sanadi, code))
        except Exception:  # noqa: BLE001 - vidyut rejects the stem
            continue
        present = bridge.derived_texts(Pada.Tinanta(dhatu=dhatu, prayoga=Prayoga.Kartari, lakara=Lakara.Lat,
                                                    purusha=Purusha.Prathama, vacana=Vacana.Eka))
        if not present:
            continue
        stem = present[0][: -len("ति")] if present[0].endswith("ति") else present[0][: -len("ते")]
        lemma = stem + "्"  # नमस्य -> नमस्य्, as the corpus cites denominatives
        for lak in lakaras:
            for pur in Purusha.choices():
                for vac in Vacana.choices():
                    pada = Pada.Tinanta(dhatu=dhatu, prayoga=Prayoga.Kartari, lakara=lak, purusha=pur, vacana=vac)
                    m = Morph(form="", lemma=lemma, kind="tinanta", purusha=bridge._term(bridge._PURUSHA, pur),
                              vacana=bridge._term(bridge._VACANA, vac), lakara=bridge._term(bridge._LAKARA, lak),
                              prayoga="कर्तरि", root=lemma, dhatu=f"{base} + {name}", gana="नामधातु",
                              root_gloss=None, source="generated", quality=2, handle=pada)
                    for text in bridge.derived_texts(pada):
                        table.setdefault(text, []).append(m)
    return {k: tuple(v) for k, v in table.items()}


def denominatives(form: str, listed: Callable[[str], bool]) -> tuple[Morph, ...]:
    """Finite forms of a denominative of a listed noun; () when the form is none."""
    from dataclasses import replace

    out: list[Morph] = []
    bases = _bases(form) + (_bases(form[1:]) if form[:1] == "अ" else [])  # अनमस्यत्: the augment is not the noun's
    for base in dict.fromkeys(bases):
        if listed(base):
            out += [replace(m, form=form) for m in _paradigm(base).get(form, ())]
    return tuple(dict.fromkeys(out))
