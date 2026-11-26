"""Anvaya: prose word order built by rule from the karaka links of a resolved Reading.

Per clause (in text order of the clause root): vocatives; karta group; adhikarana,
apadana, sampradana, karana groups; karma group; adverbs; non-finite verbals; `na`;
finite verb. A group is: genitive dependents, adjectives, then the noun, then particles
(`ca`, `nu` ...) attached to it. Compound members are emitted contiguously in text
order. Nominal sentences: subject group, other karakas, adverbs, then the predicate
adjectives (each with its own particles). Unlinked words go before the clause verb.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from mayur.model import Reading, Word

CLAUSE_ORDER = ("sambodhana", "karta", "adhikarana", "apadana", "sampradana", "karana", "karma")
NEGATION = frozenset({"na", "mA"})


def _children(words: list[Word]) -> dict[int, list[int]]:
    kids: dict[int, list[int]] = {i: [] for i in range(len(words))}
    for i, w in enumerate(words):
        if w.head is not None and w.head != i and 0 <= w.head < len(words):
            kids[w.head].append(i)
    return kids


def _root_of(words: list[Word], i: int) -> Optional[int]:
    seen = set()
    while i not in seen:
        seen.add(i)
        h = words[i].head
        if h is None:
            return i
        i = h
    return None


def _is_root(w: Word) -> bool:
    return w.head is None and w.role in ("kriya", "karta")


def _lemma(w: Word) -> str:
    return w.morph.lemma if w.morph else w.form


class _Builder:
    def __init__(self, words: list[Word]):
        self.words = words
        self.kids = _children(words)
        self.out: list[int] = []
        self.done: set[int] = set()

    def emit(self, i: int) -> None:
        if i not in self.done:
            self.done.add(i)
            self.out.append(i)

    def _by_role(self, i: int, *roles: str) -> list[int]:
        return [k for k in self.kids[i] if self.words[k].role in roles and k not in self.done]

    def _particles(self, i: int) -> list[int]:
        return [k for k in self._by_role(i, "avyaya") if _lemma(self.words[k]) not in NEGATION]

    def unit(self, i: int) -> None:
        """Emit word i with its compound members (contiguous, in text order)."""
        cid = self.words[i].compound
        members = [j for j, w in enumerate(self.words) if cid is not None and w.compound == cid]
        for j in members or [i]:
            self.emit(j)

    def group(self, i: int) -> None:
        for k in self._by_role(i, "sambandha"):
            self.group(k)
        for k in self._by_role(i, "visheshana"):
            self.group(k)
        self.unit(i)
        for k in self._particles(i):
            self.group(k)

    def clause(self, root: int, leftovers: list[int]) -> None:
        nominal = self.words[root].role == "karta"
        if nominal:
            self._nominal_clause(root, leftovers)
            return
        for role in CLAUSE_ORDER:
            for k in self._by_role(root, role):
                self.group(k)
        for k in self._particles(root):
            self.group(k)
        for k in self._by_role(root, "kriya"):
            self.group(k)
        for k in leftovers:
            self.group(k)
        for k in self._by_role(root, "avyaya"):
            self.emit(k)  # negation directly before the verb
        self.unit(root)

    def _nominal_clause(self, root: int, leftovers: list[int]) -> None:
        for k in self._by_role(root, "sambodhana"):
            self.group(k)
        for k in self._by_role(root, "sambandha"):
            self.group(k)
        self.unit(root)
        for k in self._particles(root):
            if k < root + 2:  # enclitic directly after the subject (kas nu)
                self.group(k)
        for role in CLAUSE_ORDER[2:]:
            for k in self._by_role(root, role):
                self.group(k)
        for k in self._by_role(root, "avyaya"):
            self.group(k)
        for k in leftovers:
            self.group(k)
        for k in self._by_role(root, "visheshana"):
            self.group(k)
        for k in self._by_role(root, "avyaya", "kriya"):
            self.group(k)


def clauses(words: list[Word]) -> list[tuple[int, list[int]]]:
    """(root, members) per clause, roots in text order; unlinked words join the nearest."""
    roots = [i for i, w in enumerate(words) if _is_root(w)]
    members: dict[int, list[int]] = {r: [] for r in roots}
    stray: list[int] = []
    for i in range(len(words)):
        r = _root_of(words, i)
        if r in members:
            members[r].append(i)
        else:
            stray.append(i)
    for i in stray:
        if roots:
            members[min(roots, key=lambda r: abs(r - i))].append(i)
    if not roots:
        return [(-1, stray)]
    return [(r, sorted(members[r])) for r in roots]


def order(reading: Reading) -> Reading:
    words = reading.words
    b = _Builder(words)
    for root, mem in clauses(words):
        linked = {i for i in mem if _root_of(words, i) == root}
        leftovers = [i for i in mem if i not in linked and words[i].head is None]
        if root < 0:
            for i in mem:
                b.unit(i)
            continue
        b.clause(root, leftovers)
        for i in mem:  # anything the rules missed keeps its text position at clause end
            b.unit(i)
    for i in range(len(words)):
        b.unit(i)
    return replace(reading, anvaya=list(b.out))
