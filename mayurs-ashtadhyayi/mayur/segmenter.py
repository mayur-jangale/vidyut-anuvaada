"""All valid sandhi splits of one line, as a lattice, with best-first enumeration.

Candidate junctions are proposed by matching the *output* side of the forward rule
table (:func:`mayur.sandhi.rules`) against the line.  A path through the lattice is a
valid split iff every word is a kosha pada (or a compound stem, for a non-final
compound member) and :func:`mayur.sandhi.rejoin` of the words reproduces the line
under :func:`mayur.sandhi.canon`.  The lattice is built so that the second condition
holds by construction; :func:`is_valid` re-checks it forward for any split.

Lattice node ``(p, r)``: the next word is ``r + c[p:...]`` where ``c`` is the canonical
(compact) line and ``r`` is an underlying letter restored by the junction before it.
"""

from __future__ import annotations

import heapq
import itertools
import math
from bisect import bisect_right
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Iterator, Optional

from mayur import lexicon, sandhi

MAX_WORD = 28
END = (-1, "")

# Ranking parameters (log-domain).  Tuned on DCS Ramayana Bala 1, verses 21+.
ADD_K = 0.5
QUALITY_PENALTY = {0: -9.0, 1: -5.0, 2: -0.7, 3: 0.0}
WORD_PENALTY = -2.0
COMPOUND_PENALTY = -1.0
UNSEEN_PENALTY = 0.0  # extra cost of a form never seen in the corpus
MARKED_RULE_PENALTY = -3.0  # junction licensed only by an optional chandas rule


@dataclass(frozen=True)
class SegWord:
    form: str
    start: int
    end: int
    in_compound: bool


@dataclass(frozen=True)
class Split:
    words: tuple[SegWord, ...]
    score: float
    junction_sutras: tuple[tuple[str, ...], ...]  # one entry per word: its right boundary

    @property
    def forms(self) -> tuple[str, ...]:
        return tuple(w.form for w in self.words)


@dataclass(frozen=True)
class _Edge:
    target: tuple[int, str]
    form: str
    in_compound: bool
    sutras: tuple[str, ...]
    start: int  # compact span of the word's realisation
    end: int
    score: float


@dataclass
class Segmentation:
    surface: str
    count: int
    splits: list[Split]
    _lattice: "_Lattice" = field(repr=False, default=None)

    def iter_splits(self) -> Iterator[Split]:
        """All valid splits, best first (exact: A* with the exact best-suffix heuristic)."""
        if self._lattice is None:
            return iter(())
        return self._lattice.iter_splits()


# ------------------------------------------------------------------ word model

def _freq():
    try:
        from mayur import freq
    except ImportError:  # frequency tables are optional
        return None
    return freq


@lru_cache(maxsize=1)
def _totals() -> tuple[float, float]:
    fq = _freq()
    try:
        tokens = float(fq.total_tokens()) if fq else 0.0
        types = float(len(fq._table().get("forms", {}))) if fq else 0.0
    except Exception:  # defensive: a malformed table must not break segmentation
        tokens, types = 0.0, 0.0
    return tokens, max(types, 1.0) + 50_000.0


def _count(form: str) -> int:
    fq = _freq()
    try:
        return fq.form_count(form) if fq else 0
    except Exception:
        return 0


@lru_cache(maxsize=200_000)
def word_score(form: str, in_compound: bool) -> float:
    tokens, vocab = _totals()
    count = _count(form)
    logp = math.log((count + ADD_K) / (tokens + ADD_K * vocab)) + (UNSEEN_PENALTY if count == 0 else 0.0)
    if in_compound:
        best_q = 3
    else:
        best_q = max((lexicon.quality(m) for m in lexicon.analyses(form)), default=0)
    return logp + QUALITY_PENALTY[best_q] + WORD_PENALTY + (COMPOUND_PENALTY if in_compound else 0.0)


@lru_cache(maxsize=200_000)
def lexical_form(text: str, in_compound: bool) -> Optional[str]:
    """The kosha spelling of ``text`` (nasal variants tried) if it is a pada / stem."""
    test = lexicon.is_stem if in_compound else lexicon.is_pada
    for variant in sandhi.nasal_variants(text):
        try:
            if test(variant):
                return variant
        except Exception:  # a lexicon failure on one candidate must not abort the line
            continue
    return None


def _rule_penalty(rule: sandhi.Rule) -> float:
    return MARKED_RULE_PENALTY if sandhi.MARKED_SUTRAS.intersection(rule.sutras) else 0.0


# ------------------------------------------------------------------ rule index

@dataclass(frozen=True)
class _JRule:
    rule: sandhi.Rule
    t: str  # canonical text of left+right
    left_len: int  # canonical length of left
    right_kept: bool  # right == rs: the next word re-reads it from the line


@lru_cache(maxsize=1)
def _medial_index() -> dict[str, tuple[_JRule, ...]]:
    idx: dict[str, dict[tuple, _JRule]] = {}
    for r in sandhi.rules():
        if r.rs == "":
            continue
        t = sandhi.canon_with_map(r.left + r.right, final=False)[0]
        left = sandhi.canon_with_map(r.left, final=False)[0]
        right_kept = r.right == r.rs
        if right_kept and left + r.rs != t:  # canon changed the left (nasal): keep exact
            left = t[: len(t) - 1]
        jr = _JRule(r, t, len(left), right_kept)
        idx.setdefault(t, {}).setdefault((r.le, r.rs, t, r.only, r.exclude), jr)
    return {t: tuple(d.values()) for t, d in idx.items()}


@lru_cache(maxsize=1)
def _pausa_index() -> dict[str, tuple[sandhi.Rule, ...]]:
    idx: dict[str, dict[tuple, sandhi.Rule]] = {}
    for r in sandhi.rules():
        if r.rs == "":
            t = sandhi.canon_with_map(r.left)[0]
            idx.setdefault(t, {}).setdefault((r.le, t), r)
    return {t: tuple(d.values()) for t, d in idx.items()}


# ------------------------------------------------------------------ lattice

class _Lattice:
    def __init__(self, surface: str):
        self.surface = surface
        self.c, self.cmap = sandhi.canon_with_map(surface)
        self.spaces = self._space_positions()
        self.edges: dict[tuple[int, str], list[_Edge]] = {}
        self.count: dict[tuple[int, str], int] = {END: 1}
        self.best: dict[tuple[int, str], float] = {END: 0.0}
        self._medial = _medial_index()
        self._pausa = _pausa_index()
        self._tlens = sorted({len(t) for t in self._medial}, reverse=True)
        self._plens = sorted({len(t) for t in self._pausa}, reverse=True)
        self._solve((0, ""))

    def _space_positions(self) -> list[int]:
        """Compact positions k such that a space stands between c[k-1] and c[k]."""
        out, k = [], 0
        for ch in self.surface:
            if ch.isspace():
                if k and (not out or out[-1] != k):
                    out.append(k)
            elif ch != "'":
                k += 1
        return out

    def _no_space(self, lo: int, hi: int, allowed: Optional[int] = None) -> bool:
        """True if no space position lies in (lo, hi], except ``allowed``."""
        i = bisect_right(self.spaces, lo)
        while i < len(self.spaces) and self.spaces[i] <= hi:
            if self.spaces[i] != allowed:
                return False
            i += 1
        return True

    def _solve(self, node: tuple[int, str]) -> None:
        """Memoised DFS: number of complete paths and best suffix score per node."""
        if node in self.count:
            return
        edges = self._expand(node)
        for e in edges:
            self._solve(e.target)
        live = [e for e in edges if self.count[e.target] > 0]
        self.edges[node] = live
        self.count[node] = sum(self.count[e.target] for e in live)
        self.best[node] = max((e.score + self.best[e.target] for e in live), default=-math.inf)

    def _expand(self, node: tuple[int, str]) -> list[_Edge]:
        p, r = node
        c, n = self.c, len(self.c)
        out: list[_Edge] = []
        start = p - 1 if (r and p > 0) else p  # merged vowel: the word shares it
        for q in range(p, min(n, p + MAX_WORD) + 1):
            if not self._no_space(p, q - 1):
                break
            body = r + c[p:q]
            self._pausa_edges(body, p, q, start, out)
            for tl in self._tlens:
                t = c[q:q + tl]
                if len(t) == tl:
                    for jr in self._medial.get(t, ()):
                        self._medial_edges(jr, body, p, q, start, out)
        return out

    def _pausa_edges(self, body: str, p: int, q: int, start: int, out: list[_Edge]) -> None:
        tail = self.c[q:]
        if not self._no_space(p, len(self.c)):
            return
        for rule in self._pausa.get(tail, ()):
            form = body + rule.le
            if sandhi.final_of(form) != rule.le:
                continue
            lex = lexical_form(form, False)
            if lex:
                out.append(_Edge(END, lex, False, rule.sutras, start, len(self.c),
                                 word_score(lex, False) + _rule_penalty(rule)))

    def _medial_edges(self, jr: _JRule, body: str, p: int, q: int, start: int, out: list[_Edge]) -> None:
        rule = jr.rule
        form = body + rule.le
        if not form or sandhi.final_of(form) != rule.le or not rule.applies_to(form):
            return
        split_at = q + jr.left_len
        nxt = (split_at, "") if jr.right_kept else (q + len(jr.t), rule.rs)
        end = max(split_at, start + 1)
        hi = nxt[0]
        if self._no_space(p, hi, allowed=split_at):
            lex = lexical_form(form, False)
            if lex:
                out.append(_Edge(nxt, lex, False, rule.sutras, start, end, word_score(lex, False) + _rule_penalty(rule)))
        if self._no_space(p, hi) and rule.only is None:
            lex = lexical_form(form, True)
            if lex:
                out.append(_Edge(nxt, lex, True, rule.sutras, start, end, word_score(lex, True) + _rule_penalty(rule)))

    def _split(self, path: tuple[_Edge, ...]) -> Split:
        words = tuple(SegWord(e.form, self.cmap[e.start], self.cmap[e.end - 1] + 1, e.in_compound)
                      for e in path)
        return Split(words, sum(e.score for e in path), tuple(e.sutras for e in path))

    def iter_splits(self) -> Iterator[Split]:
        root = (0, "")
        if self.count.get(root, 0) == 0:
            return
        tie = itertools.count()
        heap = [(-self.best[root], next(tie), 0.0, root, ())]
        while heap:
            _, _, g, node, path = heapq.heappop(heap)
            if node == END:
                yield self._split(path)
                continue
            for e in self.edges[node]:
                g2 = g + e.score
                heapq.heappush(heap, (-(g2 + self.best[e.target]), next(tie), g2, e.target, path + (e,)))


def segment_line(surface: str, top_k: int = 25) -> Segmentation:
    lat = _Lattice(surface)
    count = lat.count.get((0, ""), 0)
    splits = list(itertools.islice(lat.iter_splits(), top_k))
    return Segmentation(surface=surface, count=count, splits=splits, _lattice=lat)


def is_valid(forms: tuple[str, ...], flags: tuple[bool, ...], surface: str) -> bool:
    """Forward check: the words re-join to ``surface`` and each is a pada / stem."""
    for i, (form, flag) in enumerate(zip(forms, flags)):
        if flag and i == len(forms) - 1:
            return False
        if not (lexicon.is_stem(form) if flag else lexicon.is_pada(form)):
            return False
    return sandhi.matches(forms, flags, surface) is not None
