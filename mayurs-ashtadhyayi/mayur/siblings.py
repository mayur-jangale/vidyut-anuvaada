"""One spelling, two padas: the reading takes the pada whose analysis the tagger prefers.

Before a voiced sound the text's मूढा is मूढा or मूढास् (8.3.17, 8.3.22); before a vowel other than अ
the text's भीष्म is भीष्मस् or भीष्मे (8.3.17 / 6.1.78, then 8.3.19). Both are valid sandhi, so the
segmenter's lattice holds both, and the split ranker picks one without seeing the sentence. Here
the tagger, which does see it, may take the other (``mayur.tagger.sibling_forms``).

A swap is made only inside a line, and only when the forward sandhi rules give the new pada and
the next word the same text as before; the junction then carries the rules of the new pair, and
the pada not taken is named in the reading's notes. All strings Devanagari.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from mayur import lexicon, lipi, sandhi
from mayur.model import Junction, Reading, Word


def _same_text(old: str, new: str, nxt: str) -> Optional[sandhi.Outcome]:
    """The sandhi outcome of ``new`` + ``nxt`` that is also an outcome of ``old`` + ``nxt``."""
    before = {sandhi.canon(o.text) for o in sandhi.outcomes(old, nxt)}
    return next((o for o in sandhi.outcomes(new, nxt) if sandhi.canon(o.text) in before), None)


def apply(reading: Reading) -> Reading:
    """``reading`` with each word the tagger reads as its sibling pada replaced by that pada."""
    from mayur import tagger

    words: list[Word] = list(reading.words)
    swaps = tagger.sibling_forms(words)
    if not swaps:
        return reading
    junctions: list[Junction] = list(reading.junctions)
    notes = list(reading.notes)
    for i, form in sorted(swaps.items()):
        w = words[i]
        if i + 1 >= len(words) or words[i + 1].line != w.line or w.in_compound:
            continue
        analyses = list(lexicon.padas(form))
        outcome = _same_text(w.form, form, words[i + 1].form)
        if not analyses or outcome is None:
            continue
        words[i] = replace(w, form=form, analyses=analyses, chosen=0, proof=None)
        junctions = [replace(j, sutras=outcome.sutras) if j.left == i and not j.in_compound else j for j in junctions]
        notes.append(f"{lipi.pausa(form)}: the text also allows {lipi.pausa(w.form)} here (the same spelling by "
                     f"sandhi); {lipi.pausa(form)} is taken because its analysis fits the sentence better")
    return replace(reading, words=words, junctions=junctions, notes=notes)
