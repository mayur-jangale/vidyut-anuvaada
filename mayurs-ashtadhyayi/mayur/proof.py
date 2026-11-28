"""The hard gate: a reading is VERIFIED only if sandhi re-joins it to the text and every word derives."""

from __future__ import annotations

from dataclasses import replace
from typing import Sequence

from mayur import proof_context, sandhi
from mayur.model import UNVERIFIED, VERIFIED, Reading, Word, WordProof


def _prove(word: Word) -> WordProof:
    from mayur import lexicon

    if word.morph is None:
        return WordProof(False, note=f"{word.form}: no grammatical analysis")
    try:
        return lexicon.prove(word.morph)
    except Exception as exc:  # a failed derivation must not crash the gate
        return WordProof(False, note=f"{word.form}: derivation failed ({type(exc).__name__})")


def _line_rejoin(words: Sequence[Word], line: str) -> tuple[bool, str]:
    forms = [w.form for w in words]
    flags = [w.in_compound for w in words]
    text = line.replace("।", "").replace("॥", "")
    found = sandhi.rejoin_matching(forms, flags, text)
    if found is not None:
        return True, found
    return False, " ".join(forms)


def check(reading: Reading, lines: Sequence[str]) -> Reading:
    """A new Reading with word proofs, per-line re-joins, ``sandhi_ok`` and ``status`` filled in."""
    notes: list[str] = []
    words = []
    for i, w in enumerate(reading.words):
        proof = _prove(w)
        if not proof.derivable:  # a form a rule gives only in context (मे, स, महा-): see proof_context
            proof = proof_context.prove(reading.words, i, reading.compounds, proof) or proof
        if not proof.derivable:
            notes.append(f"word {w.form} (line {w.line + 1}) is not derivable: {proof.note or 'no matching derivation'}")
        words.append(replace(w, proof=proof))
    rejoined: list[str] = []
    ok = True
    for n, line in enumerate(lines):
        line_words = [w for w in words if w.line == n]
        good, text = _line_rejoin(line_words, line)
        rejoined.append(text)
        if not good:
            ok = False
            notes.append(f"line {n + 1}: the words do not re-join by sandhi to the text {line}")
    status = VERIFIED if ok and all(w.proof.derivable for w in words) else UNVERIFIED
    return replace(reading, words=words, rejoined=rejoined, sandhi_ok=ok, status=status,
                   notes=list(reading.notes) + notes)
