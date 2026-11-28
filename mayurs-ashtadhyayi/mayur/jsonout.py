"""The public JSON of a verse analysis, Devanagari first.

Every Sanskrit value is ``{"devanagari": ..., "iast": ...}``; every grammatical value is
``{"devanagari": term, "english": name}``. Pure functions only.
"""

from __future__ import annotations

import re
from functools import lru_cache
from typing import Any, Optional

from . import lipi, terms
from .model import Compound, Junction, Morph, Reading, VerseAnalysis, Word

ASHTADHYAYI = "अष्टाध्यायी"
MAX_OTHER = 5

SAMASA = {
    "तत्पुरुष": "determinative", "कर्मधारय": "descriptive", "द्वन्द्व": "copulative",
    "बहुव्रीहि": "possessive", "अव्ययीभाव": "adverbial", "नञ्-तत्पुरुष": "negative determinative",
    "नञ्-बहुव्रीहि": "negative possessive", "उपपद-तत्पुरुष": "determinative with a verbal final member",
    "द्विगु": "numeral determinative", "तद्धित": "secondary suffix, not a compound", "अज्ञात": "unknown", "": "unknown",
}
KIND_EN = {"subanta": "nominal", "tinanta": "finite verb", "avyaya": "indeclinable", "stem": "stem", "unknown": "unknown"}


# ---------------------------------------------------------------- small value builders

def sk(deva: Optional[str]) -> dict[str, str]:
    """A Sanskrit value: Devanagari with its IAST reading."""
    deva = deva or ""
    return {"devanagari": deva, "iast": lipi.iast(deva)}


def sk_opt(deva: Optional[str]) -> Optional[dict[str, str]]:
    return sk(deva) if deva else None


def term(value: Optional[str]) -> Optional[dict[str, str]]:
    return {"devanagari": value, "english": terms.english(value)} if value else None


def display(form: str) -> str:
    """A pada as written in isolation (final स्/र् as visarga)."""
    return lipi.pausa(form)


@lru_cache(maxsize=1)
def rule_texts() -> dict[tuple[str, str], str]:
    """(source, code) -> rule text, all in Devanagari. Empty when the data is not installed."""
    try:
        from . import resources

        raw = resources.sutra_texts()
    except Exception:  # missing data must not break the output
        return {}
    return {(lipi.from_code(src), code): lipi.from_code(text) for (src, code), text in raw.items()}


_CODE = re.compile(r"^(.*?)[\s:]*(\d+(?:\.\d+)*)$")


def split_rule(ref: str) -> tuple[str, str]:
    """``"6.1.87"`` or ``"वार्त्तिक 6.1.87"`` -> (source, code)."""
    m = _CODE.match(ref.strip())
    if not m:
        return ASHTADHYAYI, ref.strip()
    return (m.group(1).strip() or ASHTADHYAYI), m.group(2)


_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")


def rule_text(source: str, code: str) -> str:
    code = code.translate(_DIGITS)
    table = rule_texts()
    hit = table.get((source, code))
    if hit is None:
        hit = table.get((ASHTADHYAYI, code), "") if source == ASHTADHYAYI or not source else ""
    return hit


_TO_DEVA_DIGITS = str.maketrans("0123456789", "०१२३४५६७८९")


def rule_number(code: str) -> dict[str, str]:
    """A rule number in both numeral systems: {"devanagari": "६.१.८७", "arabic": "6.1.87"}."""
    arabic = code.translate(_DIGITS)
    return {"devanagari": arabic.translate(_TO_DEVA_DIGITS), "arabic": arabic}


def rule_entry(source: str, code: str) -> dict[str, Any]:
    number = rule_number(code)
    return {"code": number["devanagari"], "number": number, "source": sk(source),
            "text": sk(rule_text(source, code))}


# ---------------------------------------------------------------- words

def describe(m: Optional[Morph]) -> str:
    """English one-liner built from the grammar terms."""
    if m is None:
        return "no analysis"
    en = terms.english
    lemma = m.lemma or m.form
    if m.kind == "tinanta":
        parts = [en(m.purusha), en(m.vacana), en(m.lakara), en(m.prayoga)]
        return " ".join(p for p in parts if p) + f" of {lemma}"
    if m.kind == "avyaya":
        return f"indeclinable {lemma}"
    if m.kind == "unknown":
        return f"unanalysed form {m.form}"
    parts = [en(m.linga), en(m.vibhakti), en(m.vacana)]
    text = " ".join(p for p in parts if p) or "stem"
    text += f" of {m.stem or lemma}"
    if m.krt:
        text += f" ({en(m.krt)} from {m.root or lemma})"
    return text


def grammar(m: Optional[Morph]) -> dict[str, Any]:
    if m is None:
        m = Morph(form="", lemma="", kind="unknown")
    return {
        "lemma": sk_opt(m.lemma), "stem": sk_opt(m.stem), "root": sk_opt(m.root),
        "prefixes": [sk(p) for p in m.prefixes],
        "kind": {"devanagari": terms.KIND.get(m.kind, terms.KIND["unknown"]), "english": KIND_EN.get(m.kind, "unknown")},
        "gender": term(m.linga), "case": term(m.vibhakti), "number": term(m.vacana),
        "person": term(m.purusha), "tense_mood": term(m.lakara), "voice": term(m.prayoga),
        "krt": term(m.krt),
    }


def _analysis(m: Morph) -> dict[str, Any]:
    return {"form": sk(m.form), "grammar": grammar(m), "description": describe(m), "source": m.source}


def _steps(trace) -> list[dict[str, Any]]:
    """Derivation steps for readers: rule number, rule text and resulting state."""
    return [
        {"code": rule_number(s.code)["devanagari"], "number": rule_number(s.code), "source": sk(s.source),
         "sutra": sk(rule_text(s.source, s.code)), "result": sk(s.result)}
        for s in trace
    ]


def _trace(word: Word) -> list[dict[str, Any]]:
    return _steps(word.proof.trace) if word.proof is not None else []


def word_json(reading: Reading, index: int, full: bool) -> dict[str, Any]:
    w = reading.words[index]
    m = w.morph
    proof = w.proof
    others = [_analysis(a) for i, a in enumerate(w.analyses) if i != w.chosen]
    return {
        "index": index, "form": sk(display(w.form)), "pada_form": sk(w.form), "line": w.line,
        "in_compound": w.in_compound, "compound": w.compound,
        "grammar": grammar(m), "description": describe(m),
        "other_analyses": others if full else others[:MAX_OTHER],
        "verified": bool(proof and proof.derivable),
        "verified_reason": (proof.note or proof.method) if proof else "not attempted",
        "derivation_method": proof.method if proof else "",
        "sutra_trace": _trace(w),
        "role": {"devanagari": w.role, "english": terms.english(w.role)},
        "role_rules": [rule_entry(*split_rule(ref)) for ref in w.role_sutras],
        "head": w.head, "gloss": w.gloss, "gloss_source": w.gloss_source,
        "derived_meaning": w.derived_meaning, "arsha": w.arsha,
    }


# ---------------------------------------------------------------- reading parts

def _group(reading: Reading, order: list[int]) -> list[str]:
    """Display forms for the words in ``order``; consecutive members of one compound joined by '-'."""
    out: list[str] = []
    prev: Optional[int] = None
    for i in order:
        w = reading.words[i]
        shown = display(w.form)
        if out and w.compound is not None and w.compound == prev:
            out[-1] += "-" + shown
        else:
            out.append(shown)
        prev = w.compound
    return out


def padaccheda(reading: Reading, n_lines: int) -> list[list[dict[str, str]]]:
    lines = max(n_lines, max((w.line for w in reading.words), default=-1) + 1)
    result = []
    for ln in range(lines):
        order = [i for i, w in enumerate(reading.words) if w.line == ln]
        result.append([sk(t) for t in _group(reading, order)])
    return result


def junction_json(reading: Reading, j: Junction) -> dict[str, Any]:
    words = reading.words
    right = j.left + 1 if j.left + 1 < len(words) else None
    return {
        "left": j.left, "right": right,
        "between": [sk(display(words[j.left].form)) if j.left < len(words) else sk(""),
                    sk(display(words[right].form)) if right is not None else sk("")],
        "in_compound": j.in_compound, "surface": sk(j.surface),
        "sutras": [rule_entry(*split_rule(s)) for s in j.sutras],
    }


def compound_json(reading: Reading, c: Compound) -> dict[str, Any]:
    deva, eng = c.samasa or "अज्ञात", SAMASA.get(c.samasa, "unknown")
    return {
        "id": c.id, "members": list(c.members),
        "member_forms": [sk(display(reading.words[i].form)) for i in c.members if i < len(reading.words)],
        "stem": sk(c.stem), "type": {"devanagari": deva, "english": eng},
        "vigraha": sk(" ".join(display(w) for w in c.vigraha.split())), "basis": c.basis,
        "derivable": c.derivable, "note": c.note, "sutra_trace": _steps(c.trace),
    }


def anvaya_json(reading: Reading) -> dict[str, Any]:
    order = [i for i in reading.anvaya if 0 <= i < len(reading.words)]
    tokens = _group(reading, order)
    return {"order": order, "words": [sk(t) for t in tokens], "text": sk(" ".join(tokens))}


def _reading_core(reading: Reading, n_lines: int) -> dict[str, Any]:
    return {
        "padaccheda": padaccheda(reading, n_lines), "scores": dict(reading.scores),
        "status": reading.status, "translation": reading.translation, "notes": list(reading.notes),
    }


def _alignment(reading: Reading) -> list[dict[str, Any]]:
    t = reading.translation
    return [{"word": a.word, "start": a.start, "end": a.end, "text": t[a.start:a.end]} for a in reading.alignment]


def _fluent(reading: Reading) -> dict[str, Any]:
    """Fluent English made by fixed rules from the literal one; empty text when a check failed."""
    t = reading.reworded
    return {"text": t, "note": reading.reworded_note,
            "alignment": [{"word": a.word, "start": a.start, "end": a.end, "text": t[a.start:a.end]}
                          for a in reading.reworded_alignment]}


def _gloss(reading: Reading) -> list[dict[str, Any]]:
    return [
        {"index": i, "word": sk(display(w.form)), "gloss": w.gloss, "source": w.gloss_source}
        for i, w in enumerate(reading.words)
    ]


def _input_text(text: str) -> dict[str, str]:
    try:
        return sk(lipi.devanagari(text))
    except lipi.AmbiguousScript:
        return {"devanagari": text, "iast": ""}


def to_json(analysis: VerseAnalysis, *, full: bool = False) -> dict[str, Any]:
    """The public JSON for one verse; ``full`` adds complete word lists for the alternatives."""
    n_lines = len(analysis.lines)
    out: dict[str, Any] = {
        "id": analysis.id, "input": _input_text(analysis.input),
        "lines": [sk(x) for x in analysis.lines], "metre": dict(analysis.metre),
        "status": analysis.status, "split_counts": list(analysis.split_counts),
        "split_counts_plain": list(analysis.split_counts_plain), "notes": list(analysis.notes),
    }
    best = analysis.readings[0] if analysis.readings else Reading(words=[])
    out.update({
        "padaccheda": padaccheda(best, n_lines),
        "junctions": [junction_json(best, j) for j in best.junctions],
        "words": [word_json(best, i, full) for i in range(len(best.words))],
        "compounds": [compound_json(best, c) for c in best.compounds],
        "anvaya": anvaya_json(best), "gloss": _gloss(best), "translation": best.translation,
        "alignment": _alignment(best), "fluent": _fluent(best), "scores": dict(best.scores),
        "machine_translation": best.machine_translation,
    })
    alts = []
    for rank, r in enumerate(analysis.readings[1:], start=2):
        alt = {"rank": rank, **_reading_core(r, n_lines)}
        if full:
            alt["words"] = [word_json(r, i, True) for i in range(len(r.words))]
        alts.append(alt)
    out["alternatives"] = alts
    return out
