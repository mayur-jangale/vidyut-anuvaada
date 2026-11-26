"""Which words form a compound: the segmenter's member flags, checked.

A run of words flagged ``in_compound`` followed by a pada is a compound, with two corrections:
  * a bound prefix that stands as a word of its own (स, सु, अ, अन्, अति, दुस्, कु: none of
    them is a free pada in this form; सह only when the next word is not in the तृतीया it would
    govern as a free word) is joined to the following word;
  * a run is cut where a member cannot be a compound member: a finite verb or an indeclinable
    (absolutive, particle, adverb) as the final member, or a non-final member that is itself a
    complete indeclinable or pronoun pada (ततस्, पुनर्, तत्र, तत्, यत्, किम्) other than the
    prefixes the type rules use. Those words are returned as free words (``in_compound`` False).
Both are heuristics about the segmenter's output, not grammar rules; ``notes`` says what was done.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from mayur import samasa_type as st
from mayur.model import Morph, Word

BOUND = {"स", "सु", "अ", "अन्", "अति", "दुस्", "दुर्", "कु"}
MEMBER_INDECLINABLES = st.SAHA | st.NAN | st.PRADI | set(st.AVYAYIBHAVA_FIRST) | {
    "सदा", "सर्वदा", "स्वयम्", "अन्तर्", "बहिस्", "पुरस्", "सह", "प्राक्", "अधस्", "उपरि", "ईषत्", "सकृत्"}
PRONOUN_PADAS = {"तत्", "यत्", "एतत्", "किम्", "इदम्", "अदस्", "त्यत्"}


def _morph(w: Word) -> Optional[Morph]:
    return w.morph


def _free_bound(words: list[Word], i: int) -> bool:
    """Is word ``i`` a bound prefix written as a word of its own, to be joined to the next?"""
    w, m = words[i], words[i].morph
    if w.in_compound or i + 1 >= len(words) or (m is not None and m.kind in ("subanta", "tinanta")):
        return False
    nxt = words[i + 1].morph
    if w.form == "सह":  # free सह governs a तृतीया on either side (2.3.19): रामेण सह, सह रामेण
        governs = any(o.line == w.line and o.morph is not None and o.morph.vibhakti == "तृतीया" for o in words)
        return not governs and nxt is not None and nxt.kind == "subanta" and nxt.vibhakti is not None
    return w.form in BOUND and nxt is not None and nxt.kind in ("subanta", "stem")


def _nominal_final(w: Word, k: int) -> bool:
    """Analysis ``k`` of ``w`` can end a compound: an inflected nominal that is not अस्मद्/युष्मद्."""
    a = w.analyses[k]
    return a.kind == "subanta" and st.stem_of(replace(w, chosen=k)) not in st.PERSONAL


def _bad_final(w: Word) -> bool:
    """No analysis of the word can end a compound (it is only a finite verb, an indeclinable or a
    personal pronoun). स्थस् (also "you two are") and त्वम् (also "you") can: they stay finals."""
    if w.form.endswith(("चित्", "चन")):
        return True
    return bool(w.analyses) and not any(_nominal_final(w, k) for k in range(len(w.analyses)))


def _as_final(w: Word) -> Word:
    """The final word of a kept compound, with only the analyses that can end one."""
    keep = [a for k, a in enumerate(w.analyses) if _nominal_final(w, k)]
    return w if len(keep) == len(w.analyses) or not keep else replace(w, analyses=keep, chosen=0, proof=None)


def _bad_member(w: Word) -> bool:
    if w.form in MEMBER_INDECLINABLES:
        return False
    if w.form in PRONOUN_PADAS:
        return True
    m = w.morph
    if m is not None and m.kind == "avyaya":
        return True
    try:
        from mayur import lexicon
        return w.form.endswith(("स्", "र्", "म्")) and any(a.kind == "avyaya" and a.quality >= 2
                                                          for a in lexicon.padas(w.form)) \
            and not lexicon.stems(w.form)
    except Exception:  # noqa: BLE001 - lexicon unavailable: trust the flags
        return False


def _reflag(word: Word, in_compound: bool) -> Word:
    """``word`` with the other compound flag and the analyses that go with it: stems inside a
    compound, padas outside. The flag stays as it was when the form has no such analysis."""
    if word.in_compound == in_compound:
        return word
    from mayur import lexicon

    found = lexicon.stems(word.form) if in_compound else (lexicon.padas(word.form) or lexicon.generated(word.form))
    if not found:
        return word
    return replace(word, in_compound=in_compound, analyses=list(found), chosen=0, proof=None)


def regroup(words: list[Word]) -> tuple[list[Word], list[list[int]], list[str]]:
    """(words with corrected flags, compound runs as index lists, notes)."""
    out = list(words)
    notes: list[str] = []
    for i in range(len(out)):
        if _free_bound(out, i):
            out[i] = _reflag(out[i], True)
            notes.append(f"{out[i].form} is a bound prefix: joined to {out[i + 1].form} as a compound member")
    runs = _runs(out)
    kept = []
    for run in runs:
        for k, i in enumerate(run):
            last = k == len(run) - 1
            if (last and _bad_final(out[i])) or (not last and _bad_member(out[i])):
                for j in run[: k + 1] if not last else run:
                    out[j] = _reflag(out[j], False)
                notes.append(f"{'-'.join(out[j].form for j in run)}: {out[i].form} cannot be a compound "
                             f"{'final member' if last else 'member'}; read as free words")
                rest = [] if last else run[k + 1:]
                run = rest
                break
        if len(run) >= 2 or (run and out[run[-1]].in_compound):
            if not out[run[-1]].in_compound:
                out[run[-1]] = _as_final(out[run[-1]])
            kept.append(run)
    return out, kept, notes


def _runs(words: list[Word]) -> list[list[int]]:
    runs: list[list[int]] = []
    current: list[int] = []
    for i, w in enumerate(words):
        if w.in_compound:
            current.append(i)
            continue
        if current:
            runs.append(current + [i])
            current = []
    if current:  # a dangling run with no final pada: keep it as a compound anyway
        runs.append(current)
    return runs
