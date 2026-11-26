"""End-to-end analysis of one verse: split -> grammar -> proof -> ranking -> anvaya -> English."""

from __future__ import annotations

import heapq
import math
import re
from dataclasses import replace
from typing import Iterator, Sequence

from mayur import (anvaya, artha, compounds, decoder, fluent, gloss, lexicon, lipi, metre, proof, segmenter,
                   shabdabodha, translate)
from mayur.model import UNVERIFIED, VERIFIED, Junction, Reading, VerseAnalysis, Word

LINE_BREAK = re.compile(r"[।॥|/\n]+")
NOISE = re.compile(r"[0-9०-९.,;:!?\"“”‘’()\[\]-]+")
SPLITS_PER_LINE = 12
MAX_CANDIDATES = 24
FREQUENCY_TEMPERATURE = 5.0


def to_lines(text: str, script: str | None = None) -> list[str]:
    """Half-verses of ``text`` in Devanagari, without verse numbers or punctuation."""
    parts = (NOISE.sub(" ", part).strip() for part in LINE_BREAK.split(text))
    return [" ".join(lipi.devanagari(part, script).split()) for part in parts if part]


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
            nxt = idx[:i] + (idx[i] + 1,) + idx[i + 1:]
            if nxt[i] < len(per_line[i]) and nxt not in seen:
                seen.add(nxt)
                heapq.heappush(heap, (-total(nxt), nxt))


def _best_splits(seg: segmenter.Segmentation) -> list[segmenter.Split]:
    """The best valid splits of a line: the trained lattice decoder's choices first, then the
    rule-based ranking's own best ones, so that neither system's readings are dropped."""
    ruled = list(seg.splits[:SPLITS_PER_LINE])
    if seg.tier != 0 or not decoder.enabled():
        return ruled
    decoded = list(decoder.decode(seg.line, top_k=SPLITS_PER_LINE))
    seen = {tuple((w.form, w.in_compound) for w in split.words) for split in decoded}
    floor = min((split.score for split in decoded), default=0.0)
    extra = [replace(split, score=floor - rank - 1.0) for rank, split in enumerate(ruled)
             if tuple((w.form, w.in_compound) for w in split.words) not in seen]
    return decoded + extra


def _analyses(seg: segmenter.SegWord) -> list:
    found = lexicon.stems(seg.form) if seg.in_compound else lexicon.padas(seg.form)
    return list(found or lexicon.generated(seg.form))


def _reading(splits: Sequence[segmenter.Split], best: float) -> Reading:
    words: list[Word] = []
    junctions: list[Junction] = []
    for line, split in enumerate(splits):
        offset = len(words)
        words.extend(Word(form=seg.form, line=line, start=seg.start, end=seg.end,
                          in_compound=seg.in_compound, analyses=_analyses(seg)) for seg in split.words)
        junctions.extend(replace(j, left=j.left + offset) for j in split.junctions)
    score = sum(split.score for split in splits)
    frequency = 0.0 if math.isinf(score) else math.exp((score - best) / FREQUENCY_TEMPERATURE)
    scores = {"frequency": round(frequency, 4), "split_logprob": round(score, 3)}
    return Reading(words=words, junctions=junctions, scores=scores)


def _label_unproven(reading: Reading) -> Reading:
    """Say why a word is unproven. Only words unknown to the dictionary are labelled ārṣa."""
    words, notes = [], list(reading.notes)
    for w in reading.words:
        unproven = not w.analyses or (w.proof is not None and not w.proof.derivable)
        listed = bool(w.morph) and w.morph.source in ("kosha", "special")
        if unproven and listed:
            notes.append(f"{lipi.pausa(w.form)}: listed in the dictionary, but vidyut did not derive it "
                         f"({w.proof.note}); left unverified")
        elif unproven:
            reason = "no analysis found" if not w.analyses else w.proof.note
            notes.append(f"{lipi.pausa(w.form)}: not derived by Panini's rules as implemented in vidyut "
                         f"({reason}); possibly ārṣa; left unverified")
        words.append(replace(w, arsha=unproven and not listed))
    return replace(reading, words=words, notes=notes)


def _with_gloss(reading: Reading) -> Reading:
    """Gloss per word; a word with several dictionary senses takes the one its context selects."""
    words = []
    for i, w in enumerate(reading.words):
        text, source = gloss.lookup_in_context(reading, i)
        words.append(replace(w, gloss=text, gloss_source=source))
    return replace(reading, words=words)


def _finish(reading: Reading) -> Reading:
    """Gloss, meaning read off the derivation, prose order, literal English, then fluent English."""
    literal = translate.render(anvaya.order(artha.annotate(_with_gloss(reading))))
    fluent_reading, spans = fluent.rewrite(literal)
    return replace(fluent_reading, reworded_alignment=spans)


def analyze_verse(text: str, verse_id: str = "", script: str | None = None,
                  max_readings: int = 5) -> VerseAnalysis:
    """Analyse one verse. ``readings[0]`` is the chosen reading; the rest are kept alternatives."""
    if max_readings < 1:
        raise ValueError("max_readings must be at least 1")
    lines = to_lines(text, script)
    if not lines:
        return VerseAnalysis(id=verse_id, input=text, notes=["empty input"])
    segmentations = [segmenter.segment_line(line, top_k=SPLITS_PER_LINE) for line in lines]
    notes = [f"line {i + 1}: no dictionary-only split; fallback tier {seg.tier} used"
             for i, seg in enumerate(segmentations) if seg.tier]
    per_line = [_best_splits(seg) for seg in segmentations]
    empty = [i + 1 for i, splits in enumerate(per_line) if not splits]
    if empty:
        return VerseAnalysis(id=verse_id, input=text, lines=lines, metre=metre.identify(lines),
                             notes=notes + [f"line {i}: no split found" for i in empty])
    # Split score of a line: the trained decoder's score for its own choices; a rule-ranked split
    # the decoder did not return sits below all of them (see _best_splits). The sum over lines is
    # reported as the "frequency" score of a reading, relative to the best combination.
    best = sum(splits[0].score for splits in per_line)

    candidates = []
    for idx in _combinations(per_line, MAX_CANDIDATES):
        reading = _reading([per_line[i][j] for i, j in enumerate(idx)], best)
        reading = shabdabodha.resolve(compounds.annotate(reading))
        candidates.append(_label_unproven(proof.check(reading, lines)))

    ranked = sorted(shabdabodha.rank(candidates), key=lambda r: r.status != VERIFIED)  # stable
    readings = [_finish(r) for r in ranked[:max_readings]] + ranked[max_readings:]
    return VerseAnalysis(
        id=verse_id,
        input=text,
        lines=lines,
        metre=metre.identify(lines),
        split_counts=[seg.count for seg in segmentations],
        split_counts_plain=[seg.count_plain for seg in segmentations],
        readings=readings,
        status=readings[0].status if readings else UNVERIFIED,
        notes=notes,
    )


def analyze_text(text: str, script: str | None = None, max_readings: int = 5) -> list[VerseAnalysis]:
    """Analyse several verses separated by a double danda or blank lines."""
    verses = [v.strip() for v in re.split(r"॥[^।॥\n]*|\n\s*\n", text) if v.strip()]
    return [analyze_verse(v, str(i + 1), script, max_readings) for i, v in enumerate(verses)]
