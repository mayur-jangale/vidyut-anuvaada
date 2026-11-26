"""Nominal stems the kosha lacks but the corpus dictionary lists (names above all: हेहय, जटायुस्).

The Digital Corpus of Sanskrit ships a dictionary of its lemmas (CC BY 4.0; built locally into
data/derived/dcs_dict.json by scripts/build_tables.py). A stem listed there with a nominal
gender is accepted as a word; its inflection is derived forward by vidyut, never guessed. Such
an analysis has source "dictionary" and says so in its proof. All strings Devanagari.
"""

from __future__ import annotations

from dataclasses import replace
from functools import lru_cache

from mayur import bridge, resources
from mayur.model import Morph

M, F, N = "पुंलिङ्ग", "स्त्रीलिङ्ग", "नपुंसकलिङ्ग"
_GENDERS = {"m": (M,), "f": (F,), "n": (N,), "adj": (M, F, N), "mn": (M, N), "mf": (M, F), "fn": (F, N), "mfn": (M, F, N)}
NOTE = "the stem {stem} is not in vidyut's kosha; it is listed in the corpus dictionary (DCS), and vidyut derives the form"


@lru_cache(maxsize=200_000)
def genders(stem: str) -> tuple[str, ...]:
    """Genders the corpus dictionary gives the nominal stem ``stem``; () when it is not listed as one."""
    out: list[str] = []
    for entry in resources.derived("dcs_dict.json").get(stem, ()):
        out.extend(_GENDERS.get(str(entry.get("grammar", "")).strip(), ()))
    return tuple(dict.fromkeys(out))


def dictionary_stems(form: str) -> tuple[Morph, ...]:
    """``form`` as a compound member: a stem the corpus dictionary lists."""
    if not genders(form) or any(e.entry == "tinanta" for e in bridge.lookup(form)):
        return ()  # (a finite verb form is not taken as a stem on the dictionary's word alone)
    return (Morph(form=form, lemma=form, kind="stem", stem=form, source="dictionary", quality=2,
                  handle=("stem", bridge.basic_pratipadika_handle(form))),)


@lru_cache(maxsize=4096)
def _paradigm(stem: str, linga: str) -> dict[str, tuple[Morph, ...]]:
    table: dict[str, list[Morph]] = {}
    nyap = linga == F and stem.endswith(("ा", "ी"))  # बालिका, नदी: feminines in आप् / ङी (4.1.4, 4.1.5)
    for pada, template in bridge.subanta_paradigm(stem, linga, nyap=nyap):
        for text in bridge.derived_texts(pada):
            table.setdefault(text, []).append(replace(template, form=text, lemma=stem, stem=stem,
                                                      source="dictionary", quality=2))
    return {k: tuple(v) for k, v in table.items()}


def dictionary_padas(form: str) -> tuple[Morph, ...]:
    """``form`` as a pada of a stem the corpus dictionary lists: each stem the form's ending allows
    is looked up first (a dictionary probe), and only a listed stem is inflected by vidyut."""
    from mayur import lipi
    from mayur.lexicon_gen import _ENDINGS

    sounds = lipi.varnas(form)
    out: list[Morph] = []
    for ending, stem_end, lingas in _ENDINGS:
        ev = lipi.varnas(ending)
        if len(sounds) <= len(ev) + 1 or sounds[-len(ev):] != ev:
            continue
        stem = lipi.from_varnas(sounds[:-len(ev)] + lipi.varnas(stem_end))
        for linga in genders(stem):
            if linga in lingas:
                out.extend(_paradigm(stem, linga).get(form, ()))
    return tuple(dict.fromkeys(out))
