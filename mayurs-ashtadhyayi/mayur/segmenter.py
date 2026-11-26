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
from mayur.sandhi import from_varnas

Varnas = tuple[str, ...]
MAX_WORD = 30  # varnas
_END = ("<END>",)
_START = (0, (), False)  # (position, pending initial sounds, previous junction compound-internal)


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
        if c in sd.STOPS and sd.VARGA_OF[c][1] != 0 and c not in sd.PALATAL_FINAL:
            continue  # a pada-final stop is indexed in its unvoiced form; 8.2.39 voices it as needed
        if c in ("स्", "र्", "न्"):
            ctx.extend(((p, c), "") for p in sd.VOWELS)
        else:
            ctx.append(((c,), ""))
    ctx.extend((tuple(sd.varnas(w)), w) for w in sd.SPECIAL_PRONOUNS)
    return ctx


def _strip(ctx: Varnas, out: Varnas, right: Varnas) -> tuple[Varnas, Varnas, Varnas]:
    """(left_tail, right_head, surface): strip the unchanged right part first, then the left part.

    Suffix first, so that सस् + सुखी → ससुखी (6.1.132) keeps the right word's स्.
    """
    rs = 0
    while rs < len(right) and rs < len(out) and right[-1 - rs] == out[-1 - rs]:
        rs += 1
    rest = out[: len(out) - rs]
    lp = 0
    while lp < len(ctx) and lp < len(rest) and ctx[lp] == rest[lp]:
        lp += 1
    return ctx[lp:], right[: len(right) - rs], rest[lp:]


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
                    out = sd.canon_varnas(from_varnas(out) + "य")[:-2] if out else out  # sentinel: not a stop
                    tail, head, surf = _strip(ctx, out, (r,))
                    key = (ctx, tail, head, surf, samasa, whole, sutras)
                    acc.setdefault(key, {}).setdefault(r, sutras)
    index: dict[Varnas, list[_Jn]] = {}
    for (ctx, tail, head, surf, samasa, whole, sutras), rs in acc.items():
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
    # A half-verse may end inside a sandhi with the next half-verse: अस् before a voiced sound → ओ.
    jn = _Jn(("अ", "स्"), ("अ", "स्"), (), ("ओ",), frozenset(), ("६.१.११४", "६.१.८७"), False)
    index.setdefault(("ओ",), []).append(jn)
    return {k: tuple(v) for k, v in index.items()}


# ---------------------------------------------------------------- word scoring

# Weights tuned on Bala-kanda 1.21-79 (see module docstring); log-probability units.
# Seen corpus counts dominate: an unseen whole form gets only a tiny lemma pseudo-count, while
# compound members back off generously to their lemma counts (which include member uses).
W = {"lemma_w": 0.005, "lemma_w_stem": 1.0, "q0": 9.0, "q1": 2.0, "word": -1.0, "stem": 0.0, "samasa": 0.0,
     "elide": 3.0, "vocative": 1.5, "unseen": 0.00003, "aas": 3.0,
     "inner": 1.0, "short": 1.5, "q3len": 0.0}


# Particles that never stand as the first member of a compound.
_PARTICLES = frozenset(("हि", "च", "वा", "तु", "इव", "एव", "नु", "ह", "अपि", "इति", "न", "स्म", "खलु", "किल"))


def resources_derived(name: str):
    from mayur import resources

    return resources.derived(name)


@lru_cache(maxsize=100_000)
def _gendered_stem(form: str) -> bool:
    """The kosha lists ``form`` itself as a nominal stem with a gender."""
    from mayur import bridge

    from mayur.lexicon_dict import genders

    from mayur.lexicon import nasal_variants

    spellings = nasal_variants(form)  # सन्धि = संधि: the kosha and the dictionary write one of the two
    listed = any(e.entry == "basic" and e.lingas and e.pratipadika in spellings for e in bridge.lookup(form)) \
        or any(genders(f) for f in spellings) or (form.endswith("ि") and bool(genders(form + "न्")))  # उपवासि- of उपवासिन्
    if not listed:
        return False
    # a homograph the corpus knows as a finite verb but never as a compound member is the verb (अस्ति)
    from mayur import freq

    as_verb = sum(n for _, upos, feats, n in freq._parsed(form) if upos == "VERB" and "Person" in feats)
    members = resources_derived("member_counts.json")
    return any(int(members.get(f, 0)) > 0 for f in spellings) or as_verb == 0


def _stem_ok(form: str, ms: tuple) -> bool:
    """A finite verb or a particle is never a compound member, even if the kosha lists the form as a stem.

    Forms that are also nominal padas (सर्व, राम, वन ...) stay allowed.
    """
    if any(m.source == "special" for m in ms):
        return True
    if form in _PARTICLES:
        return False
    if form.endswith("न्") and form != "अन्":  # (अन् is नञ् before a vowel, 6.3.74)
        return False  # a stem in -न् loses the न् inside a compound (8.2.7): राज-, आत्म-, never राजन्-
    if _gendered_stem(form):
        return True  # a nominal stem that happens to look like a verb form too: कुरु-, आदि- (not अस्ति)
    padas = [m for m in _analyses(form, False) if m.quality >= 2]
    verb = any(m.kind == "tinanta" for m in padas)
    return not verb or any(m.kind == "subanta" and m.quality >= 3 for m in padas)


# Particles that denote no thing (1.4.57 चादयोऽसत्त्वे) do not end a compound: a compound is made of
# inflected nominals (2.1.4 सह सुपा). In 39,094 compounds of the training corpus none ends in one of these.
# An absolutive or infinitive does not end a compound of nominals either (2.1.4): तद् दृष्ट्वा is two
# words. (ल्यप् after a prefix or gati is one word already, not a compound final.) Corpus: 4 in 39,094.
NONFINITE_KRT = frozenset({"क्त्वा", "ल्यप्", "तुमुन्"})
NIPATA_NEVER_FINAL = frozenset("च वा ह एव न अपि तु हि खलु किल स्म इव उ नु वै मा चेत् ननु".split())


@lru_cache(maxsize=300_000)
def _can_follow_samasa(form: str, as_stem: bool) -> bool:
    """The word after a compound-internal junction must be able to be nominal (not only a finite verb)."""
    if as_stem:
        return True
    if form in NIPATA_NEVER_FINAL:
        return False
    return any(m.kind != "tinanta" and m.krt not in NONFINITE_KRT for m in _analyses(form, False))


@lru_cache(maxsize=300_000)
def _form_count(form: str) -> int:
    """Corpus count of ``form`` under any spelling of its nasals (पुङ्गवम् = पुंगवम्)."""
    from mayur import freq, lexicon

    return max((freq.form_count(v) for v in {form, *lexicon.nasal_variants(form)}), default=0)

@lru_cache(maxsize=300_000)
def _analyses(form: str, stem: bool) -> tuple:
    from mayur import lexicon

    found = lexicon.stems(form) if stem else lexicon.padas(form)
    v = sd.varnas(form)
    if not found and v and v[-1] in sd.STOPS and sd.VARGA_OF[v[-1]][1] == 0:
        # pada-final stops are indexed unvoiced; the kosha may list the voiced spelling (युगपद्)
        g = sd.VARGA_OF[v[-1]][0]
        voiced = from_varnas(v[:-1] + (sd.VARGAS[g][2],))
        found = lexicon.stems(voiced) if stem else lexicon.padas(voiced)
    return found


@lru_cache(maxsize=1)
def _total() -> float:
    from mayur import freq

    return float(max(freq.total_tokens(), 1_000_000))


@lru_cache(maxsize=300_000)
def word_score(form: str, stem: bool, tier_used: int = 0) -> Optional[tuple[float, bool]]:
    """(log-score, plain) for a word edge, or None if the word is not valid at this tier."""
    from mayur import freq

    if not any(sd.is_vowel(v) for v in sd.varnas(form)):
        return None  # a word has a vowel: the kosha's vowelless entries (क्, प्) are not words of a text
    ms = _analyses(form, stem)
    if stem and not _stem_ok(form, ms):
        return None
    penalty = 0.0
    if not ms and tier_used >= 1 and not stem and len(sd.varnas(form)) >= 4:
        from mayur import lexicon

        ms = lexicon.generated(form)
        penalty = -14.0
    if not ms:
        return None
    best = max(m.quality for m in ms)
    n = _total()
    c = _form_count(form) if not stem else 0
    lc = max((freq.lemma_count(m.lemma) for m in ms[:3]), default=0)
    if c > 0:
        s = math.log((c + 0.5) / n)
    else:
        # Unseen form: lemma counts, plus a pseudo-count growing with length for a quality-3 word,
        # so that a long well-formed word not in this corpus is not chopped into frequent scraps.
        syll = sum(1 for v in sd.varnas(form) if sd.is_vowel(v))
        pseudo = W["unseen"] + (W["q3len"] * syll if best >= 3 and not stem else 0.0)
        s = math.log((W["lemma_w_stem" if stem else "lemma_w"] * lc + pseudo) / n)
    if best <= 1:
        s -= W["q0"] if best == 0 else W["q1"]
    good = [m for m in ms if m.quality >= 2]
    if not stem and good and all(m.vibhakti == "सम्बोधन" for m in good):
        s -= W["vocative"]
    return s - W["word"] + penalty - (W["stem"] if stem else 0.0), best >= 2


# ---------------------------------------------------------------- lattice

def _unmarked_elision(jn: _Jn) -> bool:
    """ए/ओ + अ with the अ elided (6.1.109) but no avagraha written: legal, but rare in our texts."""
    return jn.right_head == ("अ",) and sd.AVAGRAHA not in jn.surface and "६.१.१०९" in jn.sutras

SPACE_BLOCKS_MERGE = True
# Some editions print the members of a compound apart (रत्न भाजः, सर्व भूत हिते). A bare stem before a
# space is no pada (1.4.14 सुप्तिङन्तं पदम्) unless it is a vocative, so it is read as a member when the
# corpus knows the stem as a member at least SPACED_MIN times and SPACED_RATIO times more often than as a
# word of its own (राम, वेद, द्वादश stay words).
SPACED_MEMBERS = True
SPACED_MIN, SPACED_RATIO = 5, 20
SPACED = 2  # the lattice state's "after a compound member" flag when that member was printed apart


@lru_cache(maxsize=100_000)
def _plain_nominal(form: str) -> bool:
    """``form`` has a case form other than the vocative among its analyses and no finite verb."""
    ms = [m for m in _analyses(form, False) if m.quality >= 2]
    from mayur import freq

    listed_verb = any(m.kind == "tinanta" and m.source == "kosha" for m in ms)
    case_form = any(m.kind == "subanta" and m.vibhakti != "सम्बोधन" and freq.lemma_class(m.lemma) != "pronoun" for m in ms)
    return case_form and not listed_verb  # (a pronoun does not end such a compound: never अहि मे)


@lru_cache(maxsize=100_000)
def _spaced_member(form: str) -> bool:
    from mayur.lexicon import nasal_variants

    table = resources_derived("member_counts.json")
    members = sum(int(table.get(f, 0)) for f in nasal_variants(form))
    return members >= SPACED_MIN and (_form_count(form) - members) * SPACED_RATIO <= members
CHUNK_TIER = 1  # the fallback tier from which a whole written chunk may stand as one unknown word


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
                if jn.samasa and inner and not (SPACED_MEMBERS and length == 0 and not jn.left_tail and not jn.right_head):
                    continue  # (a plain join at a written space may be a printed-apart compound: see edges)
                if sd.PADA_HIATUS in jn.sutras and (jn.samasa or not inner):
                    continue
                if SPACE_BLOCKS_MERGE and jn.right_head and j in self.sp and not _unmarked_elision(jn):
                    continue  # a vowel that merges two words cannot be followed by a written space
                out.append((jn, j))
        return out

    def edges(self, state) -> list:
        if state in self._edges:
            return self._edges[state]
        i, head, after_samasa = state
        res = []
        nxt_space = min((s for s in self.sp if s > i), default=self.n)
        for k in range(i, min(nxt_space, self.n, i + MAX_WORD) + 1):
            core = head + self.t[i:k]
            for jn, j in self.cands[k]:
                if k == i and j <= k and j >= 0 and not head:
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
                if after_samasa and not _can_follow_samasa(form, jn.samasa):
                    continue
                # (the member must be the written chunk itself: it starts at a space with nothing carried over)
                spaced = jn.samasa and j == k and k in self.sp and not head and (i == 0 or i in self.sp)
                if jn.samasa and j == k and k in self.sp and not spaced:
                    continue
                if spaced and not _spaced_member(form):
                    continue  # रत्न भाजः: a space inside a compound only after a stem that is hardly ever a word
                if after_samasa == SPACED and not jn.samasa and not _plain_nominal(form):
                    continue  # ... and only before a word that is a case form and no verb (never सर्व गच्छ)
                nxt = _END if j < 0 else (j, jn.right_head, SPACED if spaced else jn.samasa)
                pen = (W["samasa"] if jn.samasa else 0.0) + (W["elide"] if _unmarked_elision(jn) else 0.0)
                if "८.३.२२" in jn.sutras:
                    pen += W["aas"]
                if not jn.samasa:
                    pen += self._inner_penalty(word, i, k, j, after_samasa)
                res.append((form, k, jn, sc[0] - pen, sc[1], nxt))
        if self.tier >= CHUNK_TIER:
            res.extend(self._chunk_edges(i, head))
        self._edges[state] = res
        return res

    def _inner_penalty(self, word: Varnas, i: int, k: int, j: int, after_samasa: bool) -> float:
        """Opening a pada boundary inside a chunk the text writes solid needs evidence.

        A boundary inside a written chunk costs ``inner``; a short pada (≤ 2 syllables) carved out
        next to such a boundary costs ``short`` more, so particles and pronouns are not cut out of
        the middle of a rare but well-formed word.
        """
        left_inner = i > 0 and i not in self.sp and not after_samasa
        right_inner = j >= 0 and not any(k <= s <= j for s in self.sp)
        pen = W["inner"] if right_inner else 0.0
        if (left_inner or right_inner) and sum(1 for v in word if sd.is_vowel(v)) <= 2:
            pen += W["short"]
        return pen

    def _chunk_edges(self, i: int, head: Varnas) -> list:
        res = []
        for a, b in self.chunks:
            if a == i and b > i:
                form = from_varnas(head + self.t[a:b])
                jn = _Jn((), (), (), (), frozenset(), (), False)
                nxt = _END if b == self.n else (b, (), False)
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
        start = _START
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
        for idx, ((i, head, _), (form, k, jn, _, _, nxt)) in enumerate(path):
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


def spaces_of(line: str) -> frozenset:
    """Positions in the line's varna sequence (as in ``SegWord.start``/``end``) before which the text has a space."""
    return _prepare(line)[1]


def segment_line(line: str, top_k: int = 12) -> Segmentation:
    """All valid splits of ``line`` (a half-verse), the best ``top_k`` listed."""
    text, spaces = _prepare(line)
    lat = None
    tier = 0
    for tier in (0, 1, 2):
        lat = _Lattice(text, spaces, tier)
        if lat.best(_START) > -math.inf:
            break
    start = _START
    splits = list(itertools.islice(lat.iter_paths(), top_k))
    return Segmentation(line=line, count=lat.count(start, False), count_plain=lat.count(start, True),
                        splits=splits, tier=tier, _iter=lat.iter_paths)


def contains(line: str, forms, flags) -> bool:
    """Whether the split ``forms`` (with compound flags) is a path of the line's lattice, at any tier ≤ 1.
    A flag of None accepts the word either as a compound member or as a free word (the corpus
    tags glued prefixes such as स-, अन्- as free words)."""
    text, spaces = _prepare(line)
    forms, flags = [_norm(f) for f in forms], list(flags)
    for tier in (0, 1):
        lat = _Lattice(text, spaces, tier)
        frontier = {_START}
        for n, form in enumerate(forms):
            last = n == len(forms) - 1
            nxt = set()
            for state in frontier:
                for e in lat.edges(state):
                    if _norm(e[0]) == form and (flags[n] is None or e[2].samasa == bool(flags[n])) \
                            and ((e[5] == _END) == last):
                        nxt.add(e[5])
            frontier = nxt
            if not frontier:
                break
        if _END in frontier:
            return True
    return False


def _norm(form: str) -> str:
    """Comparison key for a word: canon spelling, final stop unvoiced (8.2.39/8.4.56 make both)."""
    v = sd.canon_varnas(form)
    if v and v[-1] in sd.STOPS:
        v = v[:-1] + (sd.VARGAS[sd.VARGA_OF[v[-1]][0]][0],)
    return from_varnas(v)
