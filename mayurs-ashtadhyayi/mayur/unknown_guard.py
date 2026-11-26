"""Decode-time guard: a written chunk that is not Sanskrit we know comes out whole, not shredded.

When the decoder's best split covers one written chunk (text between spaces) with two or more
words the corpus has never seen (form count 0 and lemma count 0 for every analysis), and such
words are at least half of the chunk's words, the chunk is put back as ONE word (its pada form:
final ः -> स्, ं -> म्) with the junctions around it unchanged. That reading goes first; the
decoder's own readings follow. This is a guard, not a learned feature: it is never trained.
Only the junctions inside the chunk are dropped; the chunk starts after a written space, so the
junction before it and the junction after its last word stay as the lattice proved them.
"""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from mayur import dcs, freq, model
from mayur import decoder_words as dw
from mayur import segmenter as sg
from mayur.lipi import from_varnas
from mayur.segmenter import SegWord, Split

MIN_UNSEEN = 2


def never_seen(form: str, in_compound: bool) -> bool:
    """The corpus has never seen ``form`` as a form, nor any of its analyses' lemmas."""
    if freq.form_count(form) > 0:
        return False
    return all(freq.lemma_count(m.lemma) == 0 and freq.lemma_count(dw.ud.lemma(m)) == 0
               for m in dw.analyses(form, in_compound))


def _chunks(line: str) -> tuple[tuple, list[tuple[int, int]]]:
    text, spaces = sg._prepare(line)
    cuts = [0, *sorted(spaces), len(text)]
    return text, list(zip(cuts, cuts[1:]))


def _regions(line: str, split: Split) -> list[tuple[list[tuple[int, int]], list[int]]]:
    """Groups of written chunks joined by words that straddle a space, with their word indices."""
    _, bounds = _chunks(line)
    regions: list[tuple[list[tuple[int, int]], list[int]]] = []
    for n, w in enumerate(split.words):
        touched = ([c for c in bounds if w.start < c[1] and w.end > c[0]]
                   or [c for c in bounds if c[0] <= w.start < c[1]])
        if regions and touched and touched[0] in regions[-1][0]:
            chunks, idx = regions[-1]
            chunks.extend(c for c in touched if c not in chunks)
            idx.append(n)
        else:
            regions.append((list(touched), [n]))
    return regions


def unknown_chunks(line: str, split: Split) -> list[tuple[list[tuple[int, int]], list[int]]]:
    """(chunks, word indices) of the regions the guard rewrites."""
    out = []
    for chunks, idx in _regions(line, split):
        if len(idx) < MIN_UNSEEN:
            continue
        unseen = [n for n in idx if never_seen(split.words[n].form, split.words[n].in_compound)]
        if len(unseen) >= MIN_UNSEEN and 2 * len(unseen) >= len(idx):
            out.append((chunks, idx))
    return out


def rewrite(line: str, split: Split) -> Split:
    """``split`` with each guarded region replaced by one word per written chunk."""
    text, _ = _chunks(line)
    regions = unknown_chunks(line, split)
    if not regions:
        return split
    drop = {n for _, idx in regions for n in idx}
    first = {idx[0]: (chunks, idx) for chunks, idx in regions}
    words, juncs, last_of = [], [], {}
    for n, w in enumerate(split.words):
        if n in first:
            chunks, idx = first[n]
            for c, (a, b) in enumerate(chunks):
                words.append(SegWord(dcs.pada_form(from_varnas(text[a:b]), ""), a, b, False))
                if c < len(chunks) - 1:
                    juncs.append(model.Junction(left=len(words) - 1))
            last_of[idx[-1]] = len(words) - 1
        elif n not in drop:
            words.append(w)
            last_of[n] = len(words) - 1
    for j in split.junctions:
        if j.left in last_of:
            juncs.append(model.Junction(left=last_of[j.left], sutras=j.sutras,
                                        in_compound=j.in_compound and j.left not in drop, surface=j.surface))
    return Split(tuple(words), split.score, tuple(sorted(juncs, key=lambda j: j.left)))


def guard(line: str, splits: Sequence[Split], top_k: int, m: Mapping[str, Any]) -> list[Split]:
    """The decoder's readings, with a whole-chunk reading first when the best one shreds a chunk."""
    if not splits:
        return list(splits)
    fixed = rewrite(line, splits[0])
    if fixed is splits[0]:
        return list(splits)
    return [fixed, *splits][:top_k]
