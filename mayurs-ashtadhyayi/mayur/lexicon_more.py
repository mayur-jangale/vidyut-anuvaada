"""Verb forms and agent nouns the kosha lacks, found by lookup of a sibling form and forward
generation; never by running a rule backward. All strings Devanagari.

* Augmentless past after मा (6.4.74 न माङ्योगे): मा भूत्. The augmented form (अभूत्) is looked up,
  and vidyut derives the same form without the augment.
* ārṣa voice endings: त्यजामहे, क्षमेत्, क्रोशमानम्. Epic Sanskrit often uses the आत्मनेपद endings on
  a परस्मैपद root and the reverse, against 1.3.12–93. vidyut will not derive these, so the form
  is related to its regular sibling (त्यजामस्) by the two sets of endings and LABELLED ārṣa: it is
  an analysis, not a proof, and the word stays unverified.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Any, Callable, Sequence

from mayur import bridge, lipi
from mayur.model import Morph

Lookup = Callable[[str], Sequence[Morph]]

ARSHA = "arsha"
AUGMENT_NOTE = "without the augment, as after मा (6.4.74 न माङ्योगे)"
ARSHA_NOTE = ("ārṣa: the {got} ending on a root that takes {want} by 1.3.12–93 (regular form {regular}); "
              "epic usage, labelled and not derived")
# (आत्मनेपद ending, परस्मैपद ending) as sounds, longest first
_PAIRS = tuple((lipi.varnas(a), lipi.varnas(p)) for a, p in (
    ("आमहे", "आमस्"), ("आवहे", "आवस्"), ("अन्ताम्", "अन्तु"), ("अन्ते", "अन्ति"), ("अध्वम्", "अत"),
    ("अध्वे", "अथ"), ("अन्त", "अन्"), ("अताम्", "अतु"), ("अते", "अति"), ("असे", "असि"), ("एत", "एत्"),
    ("अत", "अत्"), ("ए", "आमि")))
_PARTICIPLE = (lipi.varnas("अमान"), lipi.varnas("आन"))  # शानच् stems: क्रोशमान, दर्शयान


def _swap(sounds: tuple[str, ...], old: tuple[str, ...], new: tuple[str, ...]) -> str:
    return lipi.from_varnas(sounds[: len(sounds) - len(old)] + new)


def augmentless(form: str, padas: Lookup) -> tuple[Morph, ...]:
    """भूत् of अभूत्: the augmented लुङ्/लङ् form is in the kosha; vidyut derives it without the augment."""
    from vidyut.prakriya import Pada

    sounds = lipi.varnas(form)
    if not sounds or lipi.varnas("अ")[0] == sounds[0] or len(sounds) < 3:
        return ()
    out = []
    for entry in bridge.lookup("अ" + form):
        e = entry.morph.handle
        if entry.entry != "tinanta" or entry.morph.lakara not in ("लुङ्", "लङ्"):
            continue
        pada = Pada.Tinanta(dhatu=e.dhatu_entry.dhatu, prayoga=e.prayoga, lakara=e.lakara, purusha=e.purusha,
                            vacana=e.vacana, skip_at_agama=True)
        if form in bridge.derived_texts(pada):
            out.append(replace(entry.morph, form=form, source="generated", quality=2, handle=pada))
    return tuple(dict.fromkeys(out))


def _finite(form: str) -> list[Morph]:
    """Finite analyses of ``form`` in the kosha (a dictionary probe: cheap enough for every word)."""
    return [e.morph for e in bridge.lookup(form) if e.entry == "tinanta"]


def _has_prefix(form: str) -> bool:
    from mayur.lexicon_gen import _splits

    return bool(_splits(form))


def _prefixed_finite(form: str, padas: Lookup) -> list[Morph]:
    """Finite analyses of a prefixed verb form (forward-generated with its upasargas)."""
    return [m for m in padas(form) if m.kind == "tinanta" and m.quality >= 2]


def arsha_voice(form: str, padas: Lookup) -> tuple[Morph, ...]:
    """Finite forms and शानच् participles with the other voice's endings (see the module docstring)."""
    sounds = lipi.varnas(form)
    out: list[Morph] = []
    for atmane, parasmai in _PAIRS:
        for old, new, got, want in ((atmane, parasmai, "आत्मनेपद", "परस्मैपद"), (parasmai, atmane, "परस्मैपद", "आत्मनेपद")):
            if len(sounds) > len(old) + 1 and sounds[-len(old):] == old:
                regular = _swap(sounds, old, new)
                siblings = _finite(regular) or (_prefixed_finite(regular, padas) if _has_prefix(form) else [])
                for m in siblings:
                    note = ARSHA_NOTE.format(got=got, want=want, regular=lipi.pausa(regular))
                    out.append(replace(m, form=form, source=ARSHA, quality=1, handle=("special", note)))
    return tuple(dict.fromkeys(out))


def arsha_participle(form: str, generated: Lookup, padas: Lookup) -> tuple[Morph, ...]:
    """क्रोशमानम्: a शानच् participle of a परस्मैपद root; its stem + न्ति is the regular present."""
    out: list[Morph] = []
    for g in generated(form):
        stem = lipi.varnas(g.stem or g.lemma)
        for suffix in _PARTICIPLE:
            if len(stem) > len(suffix) + 1 and stem[-len(suffix):] == suffix:
                regular = lipi.from_varnas(stem[: len(stem) - len(suffix)] + lipi.varnas("अन्ति"))
                for m in _finite(regular):
                    note = ARSHA_NOTE.format(got="आत्मनेपद (शानच्)", want="परस्मैपद (शतृ)", regular=lipi.pausa(regular))
                    out.append(replace(g, lemma=m.lemma, root=m.root, dhatu=m.dhatu, gana=m.gana, prefixes=m.prefixes,
                                       krt="शानच्", root_gloss=m.root_gloss, source=ARSHA, quality=1,
                                       handle=("special", note)))
    return tuple(dict.fromkeys(out))


# Words that join a verb as गति: प्रादुस्, आविस्, नमस् … before कृ, भू, अस् (1.4.61 ऊर्यादिच्विडाचश्च,
# 1.4.74 साक्षात्प्रभृतीनि च); तिरस्, अन्तर् also before धा (1.4.71), अस्तम् before गम्/इ (1.4.68).
GATI_ROOTS = {"प्रादुस्": ("कृ", "भू", "अस्"), "आविस्": ("कृ", "भू", "अस्"), "नमस्": ("कृ",), "अलम्": ("कृ",),
              "सत्": ("कृ",), "साक्षात्": ("कृ",), "तिरस्": ("कृ", "भू", "धा"), "अन्तर्": ("धा", "भू", "इ", "गम्"),
              "अस्तम्": ("गम्", "इ", "या"), "पुरस्": ("कृ",)}
CVI_ROOTS = ("कृ", "भू", "अस्")
GATI_NOTE = "{gati} is a गति ({rule}) joined to the verb form {verb} by sandhi; the verb form is derived by vidyut"


def _verbal(form: str, roots: Sequence[str], padas: Lookup) -> list[Morph]:
    return [m for m in padas(form) if m.root in roots and m.quality >= 2 and (m.kind == "tinanta" or m.krt)]


def gati_verbs(form: str, padas: Lookup, is_stem: Callable[[str], bool]) -> tuple[Morph, ...]:
    """प्रादुरासीत्, नमश्चकार, आविर्भूत; च्वि: वशीकृत, शुक्लीभवति (5.4.50, 7.4.32 अस्य च्वौ)."""
    from mayur import sandhi

    sounds = lipi.varnas(form)
    out: list[Morph] = []
    for gati, roots in GATI_ROOTS.items():
        gv = lipi.varnas(gati)
        if sounds[: len(gv) - 1] != gv[:-1]:
            continue
        for n in (len(gv) - 1, len(gv), len(gv) + 1):
            rest = lipi.from_varnas(sounds[n:]) if 1 < n < len(sounds) - 1 else ""
            if rest and sandhi.rejoin_matching([gati, rest], [True], form) is not None:
                for m in _verbal(rest, roots, padas):
                    note = GATI_NOTE.format(gati=gati, rule="1.4.61, 1.4.74", verb=rest)
                    out.append(replace(m, form=form, prefixes=(gati,) + tuple(m.prefixes), source="generated",
                                       quality=2, handle=("gati", note, m)))
    for i, v in enumerate(sounds):
        if v != "ई" or i < 2 or i > len(sounds) - 3:
            continue
        base = [lipi.from_varnas(sounds[:i] + (end,)) for end in ("अ", "आ", "इ", "ई")]
        stem = next((b for b in base if is_stem(b)), None)
        if stem is None:
            continue
        rest = lipi.from_varnas(sounds[i + 1:])
        for m in _verbal(rest, CVI_ROOTS, padas):
            cvi = lipi.from_varnas(sounds[: i + 1])
            note = GATI_NOTE.format(gati=f"{cvi} ({stem} + च्वि, 5.4.50, 7.4.32)", rule="1.4.61", verb=rest)
            out.append(replace(m, form=form, prefixes=(cvi,) + tuple(m.prefixes), source="generated", quality=2,
                               handle=("gati", note, m)))
    return tuple(dict.fromkeys(out))


def more(form: str, found: Sequence[Morph], padas: Lookup, generated: Lookup) -> tuple[Morph, ...]:
    """Extra analyses for ``form`` given what the lexicon already ``found``."""
    out: list[Any] = []
    if not any(m.kind == "tinanta" for m in found):
        out += augmentless(form, padas)
    have = {(m.lemma, m.lakara, m.purusha, m.vacana, m.prayoga) for m in found if m.kind == "tinanta"}
    out += [m for m in arsha_voice(form, padas) if (m.lemma, m.lakara, m.purusha, m.vacana, m.prayoga) not in have]
    if not any(m.quality >= 2 for m in found):
        out += arsha_participle(form, generated, padas)
        from mayur import lexicon

        out += gati_verbs(form, padas, lexicon.is_stem)
    return tuple(out)
