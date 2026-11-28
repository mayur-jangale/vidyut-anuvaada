"""A fast path from verse text to the analysis the translator reads (data preparation).

The full pipeline (proofs, roles, prose order, English) takes one to two seconds a verse. The
translator's input needs only the trained split ranker, the word analyses, the tagger's choice of
one analysis per word and the gloss lookup, so this module runs just those. The result is a
``Reading`` whose words carry ``form``, ``in_compound``, the chosen analysis and ``gloss``.
``dump_reading`` / ``load_reading`` keep it as plain JSON in the data shards.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Any, Optional

from mayur.model import Morph, Reading, Word

_MORPH_KEYS = ("kind", "lemma", "stem", "linga", "vibhakti", "vacana", "purusha", "lakara", "prayoga", "krt")


def _line_words(line: str, index: int) -> list[Word]:
    """Words of one half-verse: the decoder's best split, each word with its dictionary analyses."""
    from mayur import decoder, lexicon

    splits = decoder.decode(line, 1)
    if not splits:  # nothing the lattice accepts: the written words, unanalysed
        return [Word(form=t, line=index, start=0, end=0) for t in line.split()]
    words = []
    for seg in splits[0].words:
        found = lexicon.stems(seg.form) if seg.in_compound else lexicon.padas(seg.form)
        analyses = list(found or lexicon.generated(seg.form))
        words.append(Word(form=seg.form, line=index, start=seg.start, end=seg.end,
                          in_compound=seg.in_compound, analyses=analyses))
    return words


def _choose(words: list[Word]) -> list[Word]:
    """The tagger's choice (``shabdabodha.choose``) set as ``chosen`` on each word."""
    from mayur import shabdabodha

    picks = shabdabodha.choose(words)
    return [replace(w, chosen=c) if w.analyses else w for w, c in zip(words, picks)]


def _with_gloss(reading: Reading) -> Reading:
    from mayur import gloss

    words = []
    for i, w in enumerate(reading.words):
        text, source = gloss.lookup_in_context(reading, i)
        words.append(replace(w, gloss=text, gloss_source=source))
    return replace(reading, words=words)


def fast_reading(text: str, script: Optional[str] = None) -> Reading:
    """The words of ``text`` (a verse in Devanagari or IAST) with chosen analysis and gloss."""
    from mayur import pipeline

    words: list[Word] = []
    for index, line in enumerate(pipeline.to_lines(text, script)):
        words.extend(_line_words(line, index))
    if not words:
        return Reading(words=[])
    return _with_gloss(Reading(words=_choose(words)))


def dump_reading(reading: Reading) -> list[list[Any]]:
    """Plain JSON of a fast reading: per word [form, line, in_compound, gloss, morph values or None]."""
    out = []
    for w in reading.words:
        m = w.morph
        values = None if m is None else [getattr(m, k) for k in _MORPH_KEYS]
        out.append([w.form, w.line, int(w.in_compound), w.gloss, values])
    return out


def load_reading(rows: list[list[Any]]) -> Reading:
    """The inverse of ``dump_reading`` (only the fields the translator's input reads)."""
    words = []
    for form, line, member, gloss_text, values in rows:
        analyses = []
        if values is not None:
            known = dict(zip(_MORPH_KEYS, values))
            analyses = [Morph(form=form, **known)]
        words.append(Word(form=form, line=line, start=0, end=0, in_compound=bool(member),
                          analyses=analyses, gloss=gloss_text))
    return Reading(words=words)

