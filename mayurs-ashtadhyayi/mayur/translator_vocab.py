"""A byte-pair subword vocabulary in plain Python, stored as JSON (no sentencepiece, no tokenizers).

The vocabulary is shared by the source side (stems, tags, glosses) and the English side. A source
token is one unit: atomic tags (``N3pm``, ``<C>``) get one id each, any other unit is split into
subwords. English text is cut into pre-tokens that carry their own leading space (``▁who``), so
that ``decode`` gives the text back exactly.
"""

from __future__ import annotations

import heapq
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, Sequence

PAD, BOS, EOS, UNK = 0, 1, 2, 3
SPECIALS = ("<pad>", "<s>", "</s>", "<unk>")
SPACE = "▁"
ATOMIC = re.compile(r"^(<[^<>]+>|N[0-8x][sdpx][mfnx]|V\.[a-z]+\.[123x][sdpx](\.[a-z]+)?|K\..+)$")


def _is_wordchar(ch: str) -> bool:
    return ch.isalnum() or unicodedata.category(ch).startswith("M") or ch in "'’-"


def pretokens(text: str) -> list[str]:
    """English text as pre-tokens: words and single punctuation marks, each with its leading space as ▁."""
    out: list[str] = []
    i, n = 0, len(text)
    while i < n:
        space = ""
        while i < n and text[i].isspace():
            space, i = SPACE, i + 1
        if i >= n:
            break
        j = i + 1
        if _is_wordchar(text[i]):
            while j < n and _is_wordchar(text[j]):
                j += 1
        out.append(space + text[i:j])
        i = j
    return out


def is_atomic(token: str) -> bool:
    return bool(ATOMIC.match(token))


def _symbols(word: str) -> tuple[str, ...]:
    return tuple(word)


def _merge_word(symbols: tuple[str, ...], pair: tuple[str, str]) -> tuple[str, ...]:
    out, i = [], 0
    while i < len(symbols):
        if i + 1 < len(symbols) and (symbols[i], symbols[i + 1]) == pair:
            out.append(symbols[i] + symbols[i + 1])
            i += 2
        else:
            out.append(symbols[i])
            i += 1
    return tuple(out)


def learn_merges(counts: Counter, size: int, min_count: int = 2) -> list[tuple[str, str]]:
    """Byte-pair merges (most frequent pair first) until ``size`` merges or no pair is frequent enough."""
    words = {w: _symbols(w) for w in counts}
    pairs: Counter = Counter()
    where: dict[tuple[str, str], set[str]] = defaultdict(set)
    for w, sym in words.items():
        for p in zip(sym, sym[1:]):
            pairs[p] += counts[w]
            where[p].add(w)
    heap = [(-n, p) for p, n in pairs.items()]
    heapq.heapify(heap)
    merges: list[tuple[str, str]] = []
    while len(merges) < size and heap:
        negative, best = heapq.heappop(heap)
        if pairs.get(best, 0) != -negative:
            continue  # stale entry: the pair's count has changed since it was pushed
        if -negative < min_count:
            break
        merges.append(best)
        touched: set[tuple[str, str]] = set()
        for w in list(where.pop(best, ())):
            old = words[w]
            for p in zip(old, old[1:]):
                pairs[p] -= counts[w]
                touched.add(p)
            words[w] = _merge_word(old, best)
            for p in zip(words[w], words[w][1:]):
                pairs[p] += counts[w]
                where[p].add(w)
                touched.add(p)
        for p in touched:
            if pairs[p] > 0:
                heapq.heappush(heap, (-pairs[p], p))
            else:
                del pairs[p]
    return merges


class Vocab:
    """Subword vocabulary: ``encode_source`` / ``encode_text`` to ids, ``decode`` back to text."""

    def __init__(self, pieces: Sequence[str], merges: Sequence[Sequence[str]]):
        self.pieces = list(pieces)
        self.index = {p: i for i, p in enumerate(self.pieces)}
        self.merges = [tuple(m) for m in merges]
        self.rank = {m: i for i, m in enumerate(self.merges)}
        self._cache: dict[str, tuple[str, ...]] = {}

    def __len__(self) -> int:
        return len(self.pieces)

    def split(self, word: str) -> tuple[str, ...]:
        """The subword pieces of one pre-token."""
        hit = self._cache.get(word)
        if hit is None:
            hit = self._cache[word] = self._bpe(word)
        return hit

    def _bpe(self, word: str) -> tuple[str, ...]:
        sym = _symbols(word)
        while len(sym) > 1:
            ranked = [(self.rank[p], p) for p in zip(sym, sym[1:]) if p in self.rank]
            if not ranked:
                break
            sym = _merge_word(sym, min(ranked)[1])
        return sym

    def _ids(self, pieces: Iterable[str]) -> list[int]:
        return [self.index.get(p, UNK) for p in pieces]

    def encode_source(self, tokens: Iterable[str]) -> list[int]:
        """Ids of source tokens (units from ``translator_input``); an atomic tag is one id."""
        out: list[int] = []
        for tok in tokens:
            out.extend(self._ids([tok]) if is_atomic(tok) else self._ids(self.split(SPACE + tok)))
        return out

    def encode_text(self, text: str) -> list[int]:
        out: list[int] = []
        for pre in pretokens(text):
            out.extend(self._ids(self.split(pre)))
        return out

    def decode(self, ids: Iterable[int]) -> str:
        text = "".join(self.pieces[i] for i in ids if i >= len(SPECIALS))
        return text.replace(SPACE, " ").strip()

    def to_json(self) -> dict:
        return {"pieces": self.pieces, "merges": [list(m) for m in self.merges]}

    @classmethod
    def from_json(cls, data: dict) -> "Vocab":
        return cls(data["pieces"], data["merges"])

    def save(self, path: Path) -> None:
        Path(path).write_text(json.dumps(self.to_json(), ensure_ascii=False), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "Vocab":
        return cls.from_json(json.loads(Path(path).read_text(encoding="utf-8")))


def train_vocab(sources: Iterable[Sequence[str]], texts: Iterable[str], size: int = 8000,
                extra_words: Iterable[str] = ()) -> Vocab:
    """A joint vocabulary from source token lists and English texts; ``extra_words`` are further
    source-side words (such as the surface words of verses not yet analysed)."""
    counts: Counter = Counter(SPACE + w for w in extra_words)
    atomic: Counter = Counter()
    for tokens in sources:
        for tok in tokens:
            (atomic if is_atomic(tok) else counts).update([tok if is_atomic(tok) else SPACE + tok])
    for text in texts:
        counts.update(pretokens(text))
    chars = sorted({c for w in counts for c in w})
    budget = max(size - len(SPECIALS) - len(atomic) - len(chars), 0)
    merges = learn_merges(counts, budget)
    pieces = [*SPECIALS, *sorted(atomic), *chars, *("".join(m) for m in merges)]
    return Vocab(list(dict.fromkeys(pieces)), merges)
