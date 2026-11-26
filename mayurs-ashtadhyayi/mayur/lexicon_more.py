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


def arsha_voice(form: str, padas: Lookup) -> tuple[Morph, ...]:
    """Finite forms and शानच् participles with the other voice's endings (see the module docstring)."""
    sounds = lipi.varnas(form)
    out: list[Morph] = []
    for atmane, parasmai in _PAIRS:
        for old, new, got, want in ((atmane, parasmai, "आत्मनेपद", "परस्मैपद"), (parasmai, atmane, "परस्मैपद", "आत्मनेपद")):
            if len(sounds) > len(old) + 1 and sounds[-len(old):] == old:
                regular = _swap(sounds, old, new)
                for m in _finite(regular):
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


def more(form: str, found: Sequence[Morph], padas: Lookup, generated: Lookup) -> tuple[Morph, ...]:
    """Extra analyses for ``form`` given what the lexicon already ``found``."""
    out: list[Any] = []
    if not any(m.kind == "tinanta" for m in found):
        out += augmentless(form, padas)
    have = {(m.lemma, m.lakara, m.purusha, m.vacana, m.prayoga) for m in found if m.kind == "tinanta"}
    out += [m for m in arsha_voice(form, padas) if (m.lemma, m.lakara, m.purusha, m.vacana, m.prayoga) not in have]
    if not any(m.quality >= 2 for m in found):
        out += arsha_participle(form, generated, padas)
    return tuple(out)
