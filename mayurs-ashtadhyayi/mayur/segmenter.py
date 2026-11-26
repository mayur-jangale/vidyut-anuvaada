"""All valid sandhi splits of one line, as a lattice over its varnas, ranked best first.

Junction candidates come from a reverse index built once by running ``sandhi`` FORWARD over
every (word-final context x word-initial varna) pair, so the two directions cannot disagree.
A split is valid when every word is a known pada (or a compound stem before a compound-internal
junction) and every junction is one of those forward outcomes.
"""

from __future__ import annotations

import heapq
import itertools
import math
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Callable, Iterator, Optional

from mayur import model
from mayur import sandhi as sd
from mayur.lipi import from_varnas

Varnas = tuple[str, ...]
MAX_WORD = 30  # varnas
_END = ("<END>",)


@dataclass(frozen=True)
class SegWord:
    form: str
    start: int
    end: int
    in_compound: bool = False


@dataclass(frozen=True)
class Split:
    words: tuple[SegWord, ...]
    score: float
    junctions: tuple[model.Junction, ...]


@dataclass
class Segmentation:
    line: str
    count: int
    count_plain: int
    splits: list[Split]
    tier: int
    _iter: Optional[Callable[[], Iterator[Split]]] = field(default=None, repr=False, compare=False)

    def iter_splits(self) -> Iterator[Split]:
        return self._iter() if self._iter else iter(self.splits)


@dataclass(frozen=True)
class _Jn:
    left_ctx: Varnas  # the left word must end with these
    left_tail: Varnas  # the part of left_ctx not literally in the text
    right_head: Varnas  # initial sounds of the right word not literally in the text
    surface: Varnas  # what stands in the text at the junction
    rights: frozenset  # allowed right-initial varnas (when right_head is empty)
    sutras: tuple[str, ...]
    samasa: bool
    whole: str = ""  # left word must be exactly this (6.1.132)


def _contexts() -> list[tuple[Varnas, str]]:
    ctx: list[tuple[Varnas, str]] = [((v,), "") for v in sd.VOWELS]
    for c in sd.CONSONANTS:
        if c in sd.STOPS and sd.VARGA_OF[c][1] != 0:
            continue  # a pada-final stop is indexed in its unvoiced form; 8.2.39 voices it as needed
        if c in ("स्", "र्", "न्"):
            ctx.extend(((p, c), "") for p in sd.VOWELS)
        else:
            ctx.append(((c,), ""))
    ctx.extend((tuple(sd.varnas(w)), w) for w in sd.SPECIAL_PRONOUNS)
    return ctx


def _strip(ctx: Varnas, out: Varnas, right: Varnas) -> tuple[Varnas, Varnas, Varnas]:
    lp = 0
    while lp < len(ctx) and lp < len(out) and ctx[lp] == out[lp]:
        lp += 1
    rest = out[lp:]
    rs = 0
    while rs < len(right) and rs < len(rest) and right[-1 - rs] == rest[-1 - rs]:
        rs += 1
    return ctx[lp:], right[: len(right) - rs], rest[: len(rest) - rs]


@lru_cache(maxsize=1)
def junction_index() -> dict[Varnas, tuple[_Jn, ...]]:
    """surface -> junctions; built once from forward sandhi."""
    acc: dict[tuple, dict] = {}
    for ctx, whole in _contexts():
        for r in sd.VOWELS + sd.CONSONANTS:
            right = (r,) if sd.is_vowel(r) else (r, "अ")
            for samasa in (False, True):
                if samasa and whole:
                    continue
                for seq, sutras in sd._outcomes_v(ctx, right, whole, samasa):
                    out = seq[:-1] if not sd.is_vowel(r) and seq[-1:] == ("अ",) else seq
                    out = sd.canon_varnas(from_varnas(out) + "क") [:-2] if out else out
                    tail, head, surf = _strip(ctx, out, (r,))
                    key = (ctx, tail, head, surf, samasa, whole)
                    acc.setdefault(key, {}).setdefault(r, sutras)
    index: dict[Varnas, list[_Jn]] = {}
    for (ctx, tail, head, surf, samasa, whole), rs in acc.items():
        sutras = next(iter(rs.values()))
        index.setdefault(surf, []).append(_Jn(ctx, tail, head, surf, frozenset(rs), sutras, samasa, whole))
    return {k: tuple(v) for k, v in index.items()}


@lru_cache(maxsize=1)
def pausa_index() -> dict[Varnas, tuple[_Jn, ...]]:
    index: dict[Varnas, list[_Jn]] = {}
    for ctx, whole in _contexts():
        if whole:
            continue
        for p in sd.pausa_forms(from_varnas(ctx)):
            out = sd.canon_varnas(p)
            tail, _, surf = _strip(ctx, out, ())
            jn = _Jn(ctx, tail, (), surf, frozenset(), ("८.३.१५",) if ctx[-1] in ("स्", "र्") else (), False)
            if jn not in index.get(surf, []):
                index.setdefault(surf, []).append(jn)
    return {k: tuple(v) for k, v in index.items()}


# ---------------------------------------------------------------- word scoring

# Weights tuned on Bala-kanda 1.21-79 (see module docstring); log-probability units.
W = {"lemma_w": 0.08, "lemma_w_stem": 0.08, "q0": 9.0, "q1": 5.0, "word": 1.0, "stem": 0.6, "samasa": 0.4}

@lru_cache(maxsize=300_000)
def _analyses(form: str, stem: bool) -> tuple:
    from mayur import lexicon

    return lexicon.stems(form) if stem else lexicon.padas(form)


@lru_cache(maxsize=1)
def _total() -> float:
    from mayur import freq

    return float(max(freq.total_tokens(), 1_000_000))


@lru_cache(maxsize=300_000)
def word_score(form: str, stem: bool, tier_used: int = 0) -> Optional[tuple[float, bool]]:
    """(log-score, plain) for a word edge, or None if the word is not valid at this tier."""
    from mayur import freq

    ms = _analyses(form, stem)
    penalty = 0.0
    if not ms and tier_used >= 1 and not stem and len(sd.varnas(form)) >= 4:
        from mayur import lexicon

        ms = lexicon.generated(form)
        penalty = -14.0
    if not ms:
        return None
    best = max(m.quality for m in ms)
    n = _total()
    c = freq.form_count(form) if not stem else 0
    lc = max((freq.lemma_count(m.lemma) for m in ms[:3]), default=0)
    if c > 0:
        s = math.log((c + 0.5) / n)
    else:
        s = math.log((W["lemma_w_stem" if stem else "lemma_w"] * lc + 0.05) / n)
    if best <= 1:
        s -= W["q0"] if best == 0 else W["q1"]
    return s - W["word"] + penalty - (W["stem"] if stem else 0.0), best >= 2


# ---------------------------------------------------------------- lattice

class _Lattice:
    def __init__(self, text: Varnas, spaces: frozenset, tier: int):
        self.t, self.sp, self.tier, self.n = text, spaces, tier, len(text)
        self.cands = [self._cands(k) for k in range(self.n + 1)]
        self._edges: dict = {}
        self._best: dict = {}
        self._count: dict = {}
        self.chunks = self._chunk_bounds()

    def _chunk_bounds(self) -> list[tuple[int, int]]:
        cuts = [0] + sorted(self.sp) + [self.n]
        return list(zip(cuts, cuts[1:]))

    def _cands(self, k: int) -> list[tuple[_Jn, int]]:
        out = []
        for length in range(0, 4):
            if k + length > self.n:
                break
            surf = self.t[k:k + length]
            j = k + length
            if j == self.n:
                out.extend((jn, -1) for jn in pausa_index().get(surf, ()))
            for jn in junction_index().get(surf, ()):
                if j >= self.n:
                    continue
                if not jn.right_head and self.t[j] not in jn.rights:
                    continue
                inner = [s for s in self.sp if k <= s <= j]
                if jn.samasa and inner:
                    continue
                out.append((jn, j))
        return out

    def edges(self, state) -> list:
        if state in self._edges:
            return self._edges[state]
        i, head = state
        res = []
        nxt_space = min((s for s in self.sp if s > i), default=self.n)
        for k in range(i, min(nxt_space, self.n, i + MAX_WORD) + 1):
            core = head + self.t[i:k]
            for jn, j in self.cands[k]:
                if k == i and j <= k and j >= 0:
                    continue  # no progress: a word wholly absent from the text
                word = core + jn.left_tail
                if not word or word[-len(jn.left_ctx):] != jn.left_ctx or len(word) < len(jn.left_ctx):
                    continue
                form = from_varnas(word)
                if jn.whole and form != jn.whole:
                    continue
                sc = word_score(form, jn.samasa, self.tier)
                if sc is None:
                    continue
                nxt = _END if j < 0 else (j, jn.right_head)
                res.append((form, k, jn, sc[0] - (W["samasa"] if jn.samasa else 0.0), sc[1], nxt))
        if self.tier >= 2:
            res.extend(self._chunk_edges(i, head))
        self._edges[state] = res
        return res

    def _chunk_edges(self, i: int, head: Varnas) -> list:
        res = []
        for a, b in self.chunks:
            if a == i and b > i:
                form = from_varnas(head + self.t[a:b])
                jn = _Jn((), (), (), (), frozenset(), (), False)
                nxt = _END if b == self.n else (b, ())
                res.append((form, b, jn, -40.0, False, nxt))
        return res

    def best(self, state) -> float:
        if state == _END:
            return 0.0
        if state not in self._best:
            self._best[state] = -math.inf
            self._best[state] = max((e[3] + self.best(e[5]) for e in self.edges(state)), default=-math.inf)
        return self._best[state]

    def count(self, state, plain: bool) -> int:
        if state == _END:
            return 1
        key = (state, plain)
        if key not in self._count:
            self._count[key] = sum(self.count(e[5], plain) for e in self.edges(state) if e[4] or not plain)
        return self._count[key]

    def iter_paths(self) -> Iterator[Split]:
        start = (0, ())
        if self.best(start) == -math.inf:
            return
        tie = itertools.count()
        heap = [(-self.best(start), next(tie), start, 0.0, ())]
        while heap:
            _, _, state, g, path = heapq.heappop(heap)
            if state == _END:
                yield self._split(path, g)
                continue
            for e in self.edges(state):
                h = self.best(e[5])
                if h == -math.inf:
                    continue
                g2 = g + e[3]
                heapq.heappush(heap, (-(g2 + h), next(tie), e[5], g2, path + ((state, e),)))

    def _split(self, path, score: float) -> Split:
        words, juncs = [], []
        for idx, ((i, head), (form, k, jn, _, _, nxt)) in enumerate(path):
            start = max(i - len(head), 0) if head else i
            words.append(SegWord(form, start, k + len(jn.surface) if jn.surface else k, jn.samasa))
            if nxt != _END:
                juncs.append(model.Junction(left=idx, sutras=jn.sutras, in_compound=jn.samasa,
                                            surface=from_varnas(jn.surface)))
        fixed = [SegWord(w.form, w.start, words[n + 1].start if n + 1 < len(words) else self.n, w.in_compound)
                 for n, w in enumerate(words)]
        return Split(tuple(fixed), score, tuple(juncs))


def _prepare(line: str) -> tuple[Varnas, frozenset]:
    with_spaces = sd.canon_varnas(line, keep_spaces=True)
    text, spaces = [], set()
    for v in with_spaces:
        if v == " ":
            spaces.add(len(text))
        elif v not in ("।", "॥", "|"):
            text.append(v)
    return tuple(text), frozenset(s for s in spaces if 0 < s < len(text))


def segment_line(line: str, top_k: int = 12) -> Segmentation:
    """All valid splits of ``line`` (a half-verse), the best ``top_k`` listed."""
    text, spaces = _prepare(line)
    lat = None
    tier = 0
    for tier in (0, 1, 2):
        lat = _Lattice(text, spaces, tier)
        if lat.best((0, ())) > -math.inf:
            break
    start = (0, ())
    splits = list(itertools.islice(lat.iter_paths(), top_k))
    return Segmentation(line=line, count=lat.count(start, False), count_plain=lat.count(start, True),
                        splits=splits, tier=tier, _iter=lat.iter_paths)
