"""End-to-end analysis of one verse: split -> grammar -> proof -> ranking -> anvaya -> English."""

from __future__ import annotations

import heapq
import math
import re
from dataclasses import replace
from typing import Iterator, Sequence

from mayur import (anvaya, artha, compounds, decoder, fluent, gloss, lexicon, lipi, metre, proof, segmenter,
                   shabdabodha, siblings, translate)
from mayur.model import UNVERIFIED, VERIFIED, Junction, Reading, VerseAnalysis, Word

LINE_BREAK = re.compile(r"[।॥|/\n]+")
NOISE = re.compile(r"[0-9०-९.,;:!?\"“”‘’()\[\]-]+")
SPLITS_PER_LINE = 12
MAX_CANDIDATES = 24
# Scale of a split-score difference that should matter when readings are compared. The rule-based
# ranking scores are log-probabilities; the trained decoder's are raw linear scores whose top-two
# gap has a median of about 250 on dev verses. Measured on 150 dev-pool verses: with the old
# scale (5) for decoder scores the split evidence vanished and words-identified F1 was 0.934; with
# this one it is 0.942 (decoder's own first choice: 0.942).
TEMPERATURE_RULES = 5.0
TEMPERATURE_DECODER = 1000.0
# A proof-verified reading wins a near tie; it is not preferred outright, because words vidyut
# cannot derive (मे, महा-) occur in right readings (measured: outright preference costs 0.5 F1).
VERIFIED_BONUS = 0.02


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
    ruled = _distinct(seg.splits)[:SPLITS_PER_LINE]
    if seg.tier != 0 or not decoder.enabled():
        return ruled
    decoded = _distinct(decoder.decode(seg.line, top_k=SPLITS_PER_LINE))
    seen = {_key(split) for split in decoded}
    floor = min((split.score for split in decoded), default=0.0)
    extra = [replace(split, score=floor - rank - 1.0) for rank, split in enumerate(ruled) if _key(split) not in seen]
    return decoded + extra


def _key(split: segmenter.Split) -> tuple:
    return tuple((w.form, w.in_compound) for w in split.words)


def _distinct(splits: Sequence[segmenter.Split]) -> list[segmenter.Split]:
    """Splits with different words, best first (the same words reached through another junction
    rule are one split, so they do not crowd out real alternatives)."""
    seen: set[tuple] = set()
    out = []
    for split in splits:
        if _key(split) not in seen:
            seen.add(_key(split))
            out.append(split)
    return out


# Prefixes that are never a word of their own: before a written space the form is something else
# (स before a consonant is सस् with its ending dropped, 6.1.132).
BOUND_PREFIXES = frozenset({"स", "सु", "अ", "अन्", "दुस्", "दुर्", "कु"})


def _analyses(seg: segmenter.SegWord, space_after: bool = False) -> list:
    found = lexicon.stems(seg.form) if seg.in_compound else lexicon.padas(seg.form)
    if space_after and seg.form in BOUND_PREFIXES:
        free = [m for m in found if m.kind != "avyaya"]
        found = free or found
    return list(found or lexicon.generated(seg.form))


def _reading(splits: Sequence[segmenter.Split], best: float, temperature: float,
             spaces_by_line: Sequence[frozenset] = ()) -> Reading:
    words: list[Word] = []
    junctions: list[Junction] = []
    for line, split in enumerate(splits):
        offset = len(words)
        spaces = spaces_by_line[line] if spaces_by_line else frozenset()
        for seg in split.words:
            spaced = seg.end in spaces
            words.append(Word(form=seg.form, line=line, start=seg.start, end=seg.end, in_compound=seg.in_compound,
                              space_after=spaced if spaces_by_line else None, analyses=_analyses(seg, spaced)))
        junctions.extend(replace(j, left=j.left + offset) for j in split.junctions)
    score = sum(split.score for split in splits)
    frequency = 0.0 if math.isinf(score) else math.exp((score - best) / temperature)
    scores = {"frequency": round(frequency, 4), "split_logprob": round(score, 3)}
    return Reading(words=words, junctions=junctions, scores=scores)


def _label_unproven(reading: Reading) -> Reading:
    """Say why a word is unproven. Only words unknown to the dictionary are labelled ārṣa."""
    words, notes = [], list(reading.notes)
    for w in reading.words:
        unproven = not w.analyses or (w.proof is not None and not w.proof.derivable)
        listed = bool(w.morph) and w.morph.source in ("kosha", "special")  # (source "arsha" is labelled ārṣa)
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


def candidate_readings(lines: Sequence[str]) -> tuple[list[segmenter.Segmentation], list[Reading], list[str]]:
    """(segmentations, candidate readings, notes) for the half-verses ``lines``: every candidate is
    analysed, given roles and proof-checked, but not yet ranked."""
    segmentations = [segmenter.segment_line(line, top_k=SPLITS_PER_LINE) for line in lines]
    notes = [f"line {i + 1}: no dictionary-only split; fallback tier {seg.tier} used"
             for i, seg in enumerate(segmentations) if seg.tier]
    per_line = [_best_splits(seg) for seg in segmentations]
    empty = [i + 1 for i, splits in enumerate(per_line) if not splits]
    if empty:
        return segmentations, [], notes + [f"line {i}: no split found" for i in empty]
    # Split score of a line: the trained decoder's score for its own choices; a rule-ranked split
    # the decoder did not return sits below all of them (see _best_splits).
    best = sum(splits[0].score for splits in per_line)
    decoded = decoder.enabled() and any(seg.tier == 0 for seg in segmentations)
    # the trained decoder stores the scale of its own scores (4 x the median gap between its two best
    # splits on development lines); TEMPERATURE_DECODER stands in for a model file without one
    scale = decoder.score_scale() if decoded else 0.0
    temperature = (scale if scale > 1.0 else TEMPERATURE_DECODER) if decoded else TEMPERATURE_RULES
    candidates = []
    spaces = [segmenter.spaces_of(line) for line in lines]
    for idx in _combinations(per_line, MAX_CANDIDATES):
        reading = _reading([per_line[i][j] for i, j in enumerate(idx)], best, temperature, spaces)
        reading = shabdabodha.resolve(compounds.annotate(siblings.apply(reading)))
        candidates.append(_label_unproven(proof.check(reading, lines)))
    return segmentations, candidates, notes


# A short free word (at most SCRAP_SYLLABLES syllables) that the corpus never has as a word, whose chosen
# analysis is of a stem or root the corpus never shows (in its masculine citation either), is a dictionary
# scrap: पुनस् of a stem पुन beside the indeclinable पुनर्, the vocative म beside the enclitic मा. A reading
# pays SCRAP_PENALTY for each. A frequency judgement, not a grammar rule.
SCRAP_SYLLABLES = 2
SCRAP_PENALTY = 0.08


def _scrap(w: Word) -> bool:
    from mayur import freq, sandhi, segmenter

    m = w.morph
    if w.in_compound or m is None or m.source != "kosha" or freq.analysis_count(m) or segmenter._form_count(w.form):
        return False
    if sum(map(sandhi.is_vowel, sandhi.varnas(w.form))) > SCRAP_SYLLABLES:
        return False
    lemma = m.root or m.lemma
    cited = (lemma, lemma[:-1]) if lemma.endswith(("ा", "ी")) else (lemma,)  # वंशी / वंश (4.1.4, 4.1.41)
    return not any(freq.lemma_count(x) for x in cited)


def _rank_key(r: Reading) -> tuple[float, int]:
    total = r.scores.get("total", 0.0) + VERIFIED_BONUS * (r.status == VERIFIED)
    return -(total - SCRAP_PENALTY * sum(map(_scrap, r.words))), len(r.words)


def choose(candidates: list[Reading]) -> list[Reading]:
    """Candidates best first by total score; proof-verified readings win near ties; dictionary scraps
    cost a little. Nothing is dropped."""
    return sorted(candidates, key=_rank_key)


def machine_translation(reading: Reading) -> str:
    """English of ``reading`` from the optional trained translator; "" when torch, the weights or the
    module are absent, or when it fails. It never affects the analysis."""
    try:
        from mayur import translator

        return translator.translate(reading) if translator.available() else ""
    except Exception:  # noqa: BLE001 - an optional extra must not break the interpreter
        return ""


def analyze_verse(text: str, verse_id: str = "", script: str | None = None,
                  max_readings: int = 5, translator: bool = False) -> VerseAnalysis:
    """Analyse one verse. ``readings[0]`` is the chosen reading; the rest are kept alternatives.
    ``translator``: also run the optional trained translator on the chosen reading."""
    if max_readings < 1:
        raise ValueError("max_readings must be at least 1")
    lines = to_lines(text, script)
    if not lines:
        return VerseAnalysis(id=verse_id, input=text, notes=["empty input"])
    segmentations, candidates, notes = candidate_readings(lines)
    if not candidates:
        return VerseAnalysis(id=verse_id, input=text, lines=lines, metre=metre.identify(lines), notes=notes)
    ranked = choose(candidates)
    readings = [_finish(r) for r in ranked[:max_readings]] + ranked[max_readings:]
    if translator and readings:
        readings[0] = replace(readings[0], machine_translation=machine_translation(readings[0]))
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
