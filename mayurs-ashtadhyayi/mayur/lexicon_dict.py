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
    """Genders the corpus dictionary gives the nominal stem ``stem``; () when it is not listed as one.
    The dictionary cites stems in -मत् / -वत् in their strong form (काक्षीवन्त्, हनुमन्त्)."""
    out: list[str] = []
    table = resources.derived("dcs_dict.json")
    strong = stem[: -len("त्")] + "न्त्" if stem.endswith(("मत्", "वत्")) else ""
    for entry in [*table.get(stem, ()), *(table.get(strong, ()) if strong else ())]:
        out.extend(_GENDERS.get(str(entry.get("grammar", "")).strip(), ()))
    return tuple(dict.fromkeys(out))


def dictionary_stems(form: str) -> tuple[Morph, ...]:
    """``form`` as a compound member: a stem the corpus dictionary lists."""
    stem = form if genders(form) else form + "न्" if form.endswith("ि") and genders(form + "न्") else ""
    if not stem:  # (उपवासि- is the member form of उपवासिन्: 8.2.7 नलोपः प्रातिपदिकान्तस्य)
        return ()
    return (Morph(form=form, lemma=stem, kind="stem", stem=stem, source="dictionary", quality=2,
                  handle=("stem", bridge.basic_pratipadika_handle(stem))),)


# what a nominal stem may end in, after the sounds it shares with its forms (गन्धवाहि|न्, दस्युम|त्, सुसंध|इ)
_STEM_TAILS = (
    (), ("अ",), ("आ",), ("इ",), ("ई",), ("उ",), ("ऊ",), ("ऋ",), ("न्",), ("त्",), ("द्",), ("स्",), ("च्",), ("ज्",),
    ("श्",), ("ष्",), ("ध्",), ("भ्",), ("र्",), ("क्",), ("ह्",), ("अ", "न्"), ("इ", "न्"), ("अ", "स्"), ("इ", "स्"),
    ("उ", "स्"), ("अ", "त्"))
_MAX_CUT = 6  # the longest ending (…आभ्याम्) in sounds, plus a changed stem final
_MATUP = ("मत्", "वत्")


@lru_cache(maxsize=4096)
def _paradigm(stem: str, linga: str) -> dict[str, tuple[Morph, ...]]:
    table: dict[str, list[Morph]] = {}
    nyap = linga == F and stem.endswith(("ा", "ी"))  # बालिका, नदी: feminines in आप् / ङी (4.1.4, 4.1.5)
    cells = bridge.subanta_paradigm(stem, linga, nyap=nyap)
    if stem.endswith(_MATUP) and linga != F and len(stem) > 4:
        # दस्युमत्: base + मतुप् (5.2.94), which vidyut needs for the strong forms (दस्युमान्, 7.1.70, 6.4.14)
        cells = bridge.subanta_paradigm(stem[: -len("मत्")], linga, taddhita="मतुप्") or cells
    for pada, template in cells:
        for text in bridge.derived_texts(pada):
            table.setdefault(text, []).append(replace(template, form=text, lemma=stem, stem=stem,
                                                      source="dictionary", quality=2))
    return {k: tuple(v) for k, v in table.items()}


_SIGNS = "ािीुूृॄॢेैोौ"
_VOWELS = "अआइईउऊऋॠऌएऐओऔ"


def _drop(text: str) -> str:
    """``text`` without its last sound (plain string work: this runs for every unknown substring)."""
    last = text[-1:]
    if last == "्":
        return text[:-2]
    if last in _SIGNS:
        return text[:-1] + "्"
    if last in _VOWELS or last in "ंः":
        return text[:-1]
    return text + "्" if text else text


@lru_cache(maxsize=1)
def _bodies() -> frozenset[str]:
    """Every nominal stem of the dictionary, whole and without its last one or two sounds."""
    out: set[str] = set()
    for stem, entries in resources.derived("dcs_dict.json").items():
        if any(str(e.get("grammar", "")).strip() in _GENDERS for e in entries):
            one = _drop(stem)
            out.update((stem, one, _drop(one), _drop(_drop(one))))  # (three for the strong -न्त् citations)
    out.discard("")
    return frozenset(out)


def dictionary_padas(form: str) -> tuple[Morph, ...]:
    """``form`` as a pada of a stem the corpus dictionary lists. The stem shares the form's first
    sounds and ends in one of a closed set of stem finals; each such candidate is looked up first
    (a dictionary probe), and only a listed stem is inflected by vidyut. The form is accepted only
    when that forward derivation gives exactly it."""
    from mayur import lipi
    from mayur.lexicon import nasal_variants

    sounds = lipi.varnas(form)
    out: list[Morph] = []
    tried: set[str] = set()
    bodies, text = _bodies(), form
    for cut in range(min(_MAX_CUT, len(sounds) - 2) + 1):
        if cut:
            text = _drop(text)
        if text not in bodies:
            continue  # no listed stem begins like this: nothing to inflect
        body = sounds[: len(sounds) - cut]
        for tail in _STEM_TAILS:
            stem = lipi.from_varnas(body + tail)
            if stem in tried:
                continue
            tried.add(stem)
            for linga in genders(stem):
                table = _paradigm(stem, linga)
                for spelling in nasal_variants(form):  # vidyut writes the class nasal (सुसन्धेस् for सुसंधेस्)
                    out.extend(replace(m, form=form) for m in table.get(spelling, ()))
    return tuple(dict.fromkeys(out))
