"""Sibling pada forms that one surface spelling stands for, so that the tagger can choose between them.

Before a voiced sound -आः loses its visarga (8.3.17 भोभगोअघोअपूर्वस्य योऽशि, 8.3.22 हलि सर्वेषाम्), so the
text's मूढा is मूढास् (masc. nom. pl.) as well as मूढा (fem. nom. sg.). Before a vowel both -अः and -ए
end in -अ with hiatus (8.3.17 / 6.1.78 एचोऽयवायावः, then 8.3.19 लोपः शाकल्यस्य), so the text's भीष्म उवाच
is भीष्मस् as well as भीष्मे. The segmenter picks one; the tagger sees the analyses of both and the
pipeline swaps the word's form when a sibling's analysis wins (``mayur.tagger.sibling_forms``).

Every string is Devanagari.
"""

from __future__ import annotations

from typing import Callable, Optional, Sequence

from mayur.model import Morph

_VOWELS = frozenset("अआइईउऊऋॠऌएऐओऔ")
_VOICED = frozenset("गघङजझञडढणदधनबभमयरलवह") | _VOWELS
_CONSONANTS = frozenset("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह")


def sibling_forms(form: str, next_form: str) -> tuple[str, ...]:
    """The other pada forms the same surface spelling stands for before ``next_form``."""
    nxt = next_form[:1]
    if not form or not nxt:
        return ()
    if nxt in _VOICED and form.endswith("ा") and len(form) > 2:
        return (form + "स्",)  # मूढा -> मूढास्
    if nxt in _VOICED and form.endswith("ास्") and len(form) > 3:
        return (form[:-2],)  # मूढास् -> मूढा
    if nxt in _VOWELS and nxt != "अ":
        # भीष्म उवाच: भीष्मस् (8.3.17, 8.3.19), भीष्मे (6.1.78, 8.3.19) or the vocative भीष्म itself
        if form.endswith("े") and len(form) > 2 and form[-2] in _CONSONANTS:
            return (form[:-1] + "स्", form[:-1])
        if form.endswith("स्") and len(form) > 3 and form[-3] in _CONSONANTS:
            return (form[:-2] + "े", form[:-2])
        if form[-1] in _CONSONANTS and len(form) > 1:
            return (form + "स्", form + "े")
    return ()


def sibling_form(form: str, next_form: str) -> Optional[str]:
    """The first of :func:`sibling_forms`, or None."""
    return next(iter(sibling_forms(form, next_form)), None)


def surface(form: str, sibling: str) -> str:
    """One spelling for both members of a pair (for the word's observation features): the shorter stem."""
    a, b = sorted((form, sibling))
    common = 0
    while common < min(len(a), len(b)) and a[common] == b[common]:
        common += 1
    return form[:common]


def variant(form: str) -> str:
    """Which member of a pair ``form`` is: its ending."""
    if form.endswith("ास्"):
        return "आस्"
    if form.endswith("ा"):
        return "आ"
    if form.endswith("े"):
        return "ए"
    if form.endswith("स्"):
        return "अस्"
    return "अ"  # the bare stem form: a vocative


def extend(cands: Sequence[Sequence[Morph]], forms: Sequence[str], cpd: Sequence[bool],
           sibling_candidates: Callable[[str], list[Morph]]):
    """Candidates with the sibling form's analyses appended at every eligible word.

    Returns ``(cands, own, obs_forms, variants)``: ``own[i]`` = number of the word's own candidates
    (a chosen index ≥ ``own[i]`` is a sibling's), the forms to use for observation features, and per
    candidate the variant label ("" where the word has no sibling).
    """
    out, own, obs, var = [], [], [], []
    for i, c in enumerate(cands):
        sibs: tuple[str, ...] = ()
        if not cpd[i] and i + 1 < len(forms) and c:
            sibs = sibling_forms(forms[i], forms[i + 1])
        extra, labels = [], []
        for sib in sibs:
            new = [m for m in sibling_candidates(sib) if m not in c and m not in extra]
            extra += new
            labels += [variant(sib)] * len(new)
        out.append(list(c) + extra)
        own.append(len(c))
        if extra:
            obs.append(surface(forms[i], sibs[0]))
            var.append([variant(forms[i])] * len(c) + labels)
        else:
            obs.append(forms[i])
            var.append([""] * len(c))
    return out, own, obs, var
