"""Test fixtures: build Readings directly from (form, in_compound) pairs."""

from __future__ import annotations

from mayur import lexicon
from mayur.model import Reading, Word

VERSE1 = [
    ("tapas", True), ("svADyAya", True), ("niratam", False), ("tapasvI", False),
    ("vAc", True), ("vidAm", False), ("varam", False), ("nAradam", False),
    ("paripapracCa", False), ("vAlmIkis", False), ("muni", True), ("puMgavam", False),
]

VERSE2 = [
    ("kas", False), ("nu", False), ("asmin", False), ("sAmpratam", False), ("loke", False),
    ("guRavAn", False), ("kas", False), ("ca", False), ("vIryavAn", False),
    ("Darma", True), ("jYas", False), ("ca", False), ("kftajYas", False), ("ca", False),
    ("satya", True), ("vAkyas", False), ("dfQa", True), ("vratas", False),
]

SVETAS = [("Svetas", False), ("DAvati", False)]
SVA_ITAS = [("SvA", False), ("itas", False), ("DAvati", False)]


def reading_from_forms(pairs: list[tuple[str, bool]], line: int = 0) -> Reading:
    words: list[Word] = []
    pos = 0
    for form, in_cpd in pairs:
        analyses = list(lexicon.stem_analyses(form) if in_cpd else lexicon.analyses(form))
        words.append(Word(form=form, line=line, start=pos, end=pos + len(form),
                          in_compound=in_cpd, analyses=analyses))
        pos += len(form) + (0 if in_cpd else 1)
    return Reading(words=words)


def with_glosses(reading: Reading) -> Reading:
    """Fill word.gloss as the pipeline would (empty string if the gloss module fails)."""
    from dataclasses import replace

    try:
        from mayur.gloss import lookup
    except Exception:  # gloss module is another agent's; tests must not depend on it
        return reading
    words = [replace(w, gloss=lookup(w.morph)[0] if w.morph else "") for w in reading.words]
    return replace(reading, words=words)


def analysed(pairs: list[tuple[str, bool]]) -> Reading:
    """compounds.annotate -> shabdabodha.resolve -> anvaya.order (no translation)."""
    from mayur import anvaya, compounds, shabdabodha

    return anvaya.order(shabdabodha.resolve(compounds.annotate(reading_from_forms(pairs))))


def rendered(pairs: list[tuple[str, bool]]) -> Reading:
    from mayur import translate

    return translate.render(with_glosses(analysed(pairs)))
