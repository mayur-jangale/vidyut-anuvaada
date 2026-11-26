"""क्त participles the kosha lists only as plain adjectives (छन्न, उद्यत, विषण्ण, प्रहृष्ट).

The kosha's basic stem is looked up in an index of vidyut's own forward क्त derivations of every
kosha dhātu (plain and ṇic, built once by the bridge); upasargas are split off first. The
analysis is kept only when vidyut, deriving the prefixed dhātu + क्त in the same case, yields
the exact form (for a compound member: the exact stem). All strings Devanagari.
"""

from __future__ import annotations

from functools import lru_cache

from mayur import bridge
from mayur.model import Morph

# last sound of a क्त stem: त (कृत, इत), न/ण (छन्न, क्षीण), ढ (मूढ), ध/ट (बुद्ध, दृष्ट)
_KTA_FINAL = ("त", "न", "ण", "ढ", "ध", "ट")


@lru_cache(maxsize=50_000)
def _analyses(stem: str) -> tuple[tuple[tuple[str, ...], object, object], ...]:
    """(upasargas, dhātu entry, prefixed क्त pratipadika) whose derivation yields ``stem``."""
    from mayur.lexicon_gen import _splits

    if not stem.endswith(_KTA_FINAL) or len(stem) < 3:
        return ()
    cands: list[tuple[tuple[str, ...], str]] = [((), stem)]
    for u1, rem1 in _splits(stem):
        cands.append(((u1,), rem1))
        cands.extend(((u1, u2), rem2) for u2, rem2 in _splits(rem1))
    out = []
    for ups, rem in cands:
        for de in bridge.kta_candidates(rem):
            prati = bridge.kta_pratipadika(de, ups)
            if prati is not None and stem in bridge.derived_texts(prati):
                out.append((ups, de, prati))
    return tuple(out)


def _morph(form: str, kind: str, ups: tuple[str, ...], de: object, handle: object, **case: object) -> Morph:
    f = bridge.kta_fields(de)
    prefixes = ups + f["prefixes"]
    return Morph(form=form, lemma="".join(prefixes) + f["root"], kind=kind, root=f["root"], dhatu=f["dhatu"],
                 gana=f["gana"], prefixes=prefixes, krt="क्त", root_gloss=f["root_gloss"], source="generated",
                 quality=3, handle=handle, **case)  # type: ignore[arg-type]


def kta_padas(form: str, entries: tuple[bridge.Entry, ...]) -> tuple[Morph, ...]:
    """क्त readings of the kosha ``entries`` of ``form`` that are basic a/ā-stems."""
    out: list[Morph] = []
    for entry in entries:
        if entry.entry != "basic" or entry.is_avyaya:
            continue
        stem = entry.pratipadika[:-1] if entry.pratipadika.endswith("ा") else entry.pratipadika
        for ups, de, prati in _analyses(stem):
            pada = bridge.subanta_like(prati, entry)
            if pada is not None and form in bridge.derived_texts(pada):
                m = entry.morph
                out.append(_morph(form, "subanta", ups, de, pada, stem=stem, linga=m.linga,
                                  vibhakti=m.vibhakti, vacana=m.vacana))
    return tuple(dict.fromkeys(out))


def kta_stems(form: str) -> tuple[Morph, ...]:
    """``form`` as a compound member that is a क्त stem (stem = form)."""
    return tuple(dict.fromkeys(_morph(form, "stem", ups, de, ("stem", prati), stem=form)
                               for ups, de, prati in _analyses(form)))
