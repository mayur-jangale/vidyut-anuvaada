"""Prose order (anvaya) built by rule from the karaka links set by ``shabdabodha.resolve``.

Order inside a clause: vocatives, particles, karta group, अधिकरण, अपादान, सम्प्रदान, करण
groups, karma group, non-finite verbals (each after its own objects), विधेय, न, verb.
A group is: genitive dependents, qualifiers, then the head. च follows the item it
joins. Compound members stay together in their original order. Clauses follow text order.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from mayur.model import Reading, Word

PRIORITY = {
    "सम्बोधन": 0, "अव्यय": 1, "कर्ता": 2, "सम्बन्ध": 3, "विशेषण": 4, "अधिकरण": 5, "अपादान": 6,
    "सम्प्रदान": 7, "करण": 8, "कर्म": 9, "पूर्वकालक्रिया": 10, "तुमर्थ": 10,
}
NEGATION = "न"
CONJUNCTION = "च"
_LAST = 12


def _priority(word: Word) -> int:
    if word.role == "अव्यय" and word.form == NEGATION:
        return _LAST
    return PRIORITY.get(word.role, _LAST - 1)


def _members(words: list[Word], i: int) -> list[int]:
    """The word with its preceding compound members (original order)."""
    start = i
    while start > 0 and words[start - 1].in_compound:
        start -= 1
    return list(range(start, i + 1))


def _root(words: list[Word], i: int) -> int:
    seen = {i}
    while words[i].head is not None and words[i].head not in seen and 0 <= words[i].head < len(words):
        i = words[i].head
        seen.add(i)
    return i


def _emit(words: list[Word], i: int, deps: dict[int, list[int]], out: list[int], done: set[int]) -> None:
    if i in done:
        return
    done.add(i)
    children = [d for d in deps.get(i, []) if not words[d].in_compound]
    trailing = [d for d in children if words[d].role == "विधेय"
                or (words[d].role == "अव्यय" and words[d].form == CONJUNCTION and d > i)]
    before = sorted((d for d in children if d not in trailing), key=lambda d: (_priority(words[d]), d))
    for d in before:
        _emit(words, d, deps, out, done)
    for m in _members(words, i):
        if m not in out:
            out.append(m)
            done.add(m)
    for d in trailing:
        _emit(words, d, deps, out, done)


def prose_order(words: list[Word]) -> list[int]:
    deps: dict[int, list[int]] = {}
    for i, w in enumerate(words):
        if w.head is not None and w.head != i and 0 <= w.head < len(words):
            deps.setdefault(w.head, []).append(i)
    roots: list[int] = []
    for i in range(len(words)):
        r = _root(words, i)
        if r not in roots and not words[r].in_compound:
            roots.append(r)
    roots.sort(key=lambda r: min(j for j in range(len(words)) if _root(words, j) == r))
    out: list[int] = []
    done: set[int] = set()
    for r in roots:
        _emit(words, r, deps, out, done)
    out.extend(i for i in range(len(words)) if i not in out)  # safety: every index once
    return out


def order(reading: Reading) -> Reading:
    """New Reading with ``anvaya`` set."""
    return replace(reading, anvaya=prose_order(reading.words))


def head_of(words: list[Word], i: int) -> Optional[int]:
    return words[i].head
