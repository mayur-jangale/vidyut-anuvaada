"""End-to-end analysis of one verse: split -> grammar -> proof -> ranking -> anvaya -> English."""

from __future__ import annotations

import heapq
import math
import re
from dataclasses import replace
from typing import Iterator, Sequence

from mayur import anvaya, compounds, gloss, lexicon, metre, proof, segmenter, shabdabodha, translate, translit
from mayur.model import UNVERIFIED, VERIFIED, Reading, VerseAnalysis, Word

LINE_BREAK = re.compile(r"[।॥|/\n]+")
NOISE = re.compile(r"[0-9०-९.,;:!?\"“”‘’()\[\]-]+")
SPLITS_PER_LINE = 12
MAX_CANDIDATES = 16
FREQUENCY_TEMPERATURE = 5.0


def to_lines(text: str) -> list[str]:
    """Half-verses of ``text`` in SLP1. ASCII input is taken to be SLP1 already."""
    parts = (NOISE.sub(" ", part).strip() for part in LINE_BREAK.split(text))
    return [" ".join(_to_slp1(part).split()) for part in parts if part]


def _to_slp1(text: str) -> str:
    if any("ऀ" <= ch <= "ॿ" for ch in text):
        return translit.to_slp1(text)
    return text if text.isascii() else translit.iast_to_slp1(text)


def _fallback_split(line: str) -> segmenter.Split:
    """One unanalysed word per chunk, used when a line has no valid split at all."""
    words, pos = [], 0
    for chunk in line.split(" "):
        words.append(segmenter.SegWord(form=chunk, start=pos, end=pos + len(chunk), in_compound=False))
        pos += len(chunk) + 1
    return segmenter.Split(words=tuple(words), score=float("-inf"), junction_sutras=())


def _combinations(per_line: Sequence[Sequence[segmenter.Split]], limit: int) -> Iterator[tuple[int, ...]]:
    """Index tuples (one split per line) in decreasing order of total score."""

    def total(idx: tuple[int, ...]) -> float:
        return sum(per_line[i][j].score for i, j in enumerate(idx))

    start = tuple(0 for _ in per_line)
    heap, seen, produced = [(-total(start), start)], {start}, 0
    while heap and produced < limit:
        _, idx = heapq.heappop(heap)
        yield idx
        produced += 1
        for i in range(len(idx)):
            nxt = idx[:i] + (idx[i] + 1,) + idx[i + 1 :]
            if nxt[i] < len(per_line[i]) and nxt not in seen:
                seen.add(nxt)
                heapq.heappush(heap, (-total(nxt), nxt))


def _word(seg: segmenter.SegWord, line: int) -> Word:
    found = lexicon.stem_analyses(seg.form) if seg.in_compound else lexicon.analyses(seg.form)
    return Word(form=seg.form, line=line, start=seg.start, end=seg.end,
                in_compound=seg.in_compound, analyses=list(found))


def _reading(splits: Sequence[segmenter.Split], best: float) -> Reading:
    words = [_word(seg, line) for line, split in enumerate(splits) for seg in split.words]
    score = sum(split.score for split in splits)
    frequency = 0.0 if math.isinf(score) else math.exp((score - best) / FREQUENCY_TEMPERATURE)
    return Reading(words=words, scores={"frequency": round(frequency, 4), "split_logprob": round(score, 3)})


def _label_unproven(reading: Reading) -> Reading:
    """Mark words that could not be analysed or derived; they are never forced into a parse."""
    words, notes = [], list(reading.notes)
    for w in reading.words:
        unproven = not w.analyses or (w.proof is not None and not w.proof.derivable)
        if unproven:
            reason = "no analysis found" if not w.analyses else w.proof.note
            notes.append(f"{w.form}: not derivable by vidyut-prakriya ({reason}); possibly Arza, left unverified")
        words.append(replace(w, arsha=unproven))
    return replace(reading, words=words, notes=notes)


def _with_gloss(reading: Reading) -> Reading:
    words = []
    for w in reading.words:
        text, source = gloss.lookup(w.morph) if w.morph else ("", "none")
        words.append(replace(w, gloss=text, gloss_source=source))
    return replace(reading, words=words)


def _finish(reading: Reading) -> Reading:
    return translate.render(anvaya.order(_with_gloss(reading)))


def analyze_verse(text: str, verse_id: str = "", max_readings: int = 5) -> VerseAnalysis:
    """Analyse one verse. ``readings[0]`` is the chosen reading; the rest are kept alternatives."""
    lines = to_lines(text)
    if not lines:
        return VerseAnalysis(id=verse_id, input=text, notes=["empty input"])
    segmentations = [segmenter.segment_line(line, top_k=SPLITS_PER_LINE) for line in lines]
    notes = [f"line {i + 1}: no valid split found; passed through unanalysed"
             for i, seg in enumerate(segmentations) if not seg.splits]
    per_line = [seg.splits or [_fallback_split(line)] for seg, line in zip(segmentations, lines)]
    best = sum(splits[0].score for splits in per_line)

    candidates = []
    for idx in _combinations(per_line, MAX_CANDIDATES):
        reading = _reading([per_line[i][j] for i, j in enumerate(idx)], best)
        reading = shabdabodha.resolve(compounds.annotate(reading))
        candidates.append(_label_unproven(proof.check(reading, lines)))

    ranked = shabdabodha.rank(candidates)
    ranked = sorted(ranked, key=lambda r: r.status != VERIFIED)  # stable: verified readings first
    readings = [_finish(r) for r in ranked[:max_readings]] + ranked[max_readings:]
    status = readings[0].status if readings else UNVERIFIED
    return VerseAnalysis(
        id=verse_id,
        input=text,
        lines=lines,
        metre=metre.identify(lines),
        split_counts=[seg.count for seg in segmentations],
        readings=readings,
        status=status,
        notes=notes,
    )


def analyze_text(text: str, max_readings: int = 5) -> list[VerseAnalysis]:
    """Analyse several verses separated by a double danda or blank lines."""
    verses = [v.strip() for v in re.split(r"॥[^।॥\n]*|\n\s*\n", text) if v.strip()]
    return [analyze_verse(v, verse_id=str(i + 1), max_readings=max_readings) for i, v in enumerate(verses)]
