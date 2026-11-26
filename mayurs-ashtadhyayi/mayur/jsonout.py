"""Public JSON for a verse: model.to_jsonable plus derived convenience fields."""

from __future__ import annotations

from typing import Any, Optional

from mayur.model import Morph, Reading, VerseAnalysis, Word, to_jsonable
from mayur.translit import to_deva, to_iast

MAX_ALTERNATIVE_ANALYSES = 5


def scripts(slp1: str) -> dict[str, str]:
    return {"slp1": slp1, "devanagari": to_deva(slp1) if slp1 else "", "iast": to_iast(slp1) if slp1 else ""}


def _english(value: Any) -> str:
    try:
        from mayur import labels

        return str(labels.english(value))
    except Exception:
        return str(value)


def describe(morph: Morph) -> str:
    try:
        from mayur import labels

        return str(labels.describe(morph))
    except Exception:
        pass
    keys = ("kind", "linga", "vibhakti", "vacana", "purusha", "lakara", "prayoga")
    return " ".join(str(getattr(morph, k)) for k in keys if getattr(morph, k))


def _analysis_json(m: Optional[Morph]) -> dict[str, Any]:
    if m is None:
        return {"lemma": "", "kind": "unknown", "description": ""}
    out: dict[str, Any] = {
        "lemma": m.lemma, "lemma_iast": to_iast(m.lemma) if m.lemma else "", "kind": m.kind,
        "gender": m.linga, "case": m.vibhakti, "number": m.vacana, "person": m.purusha,
        "tense_mood": m.lakara, "voice": m.prayoga, "root": m.root, "prefixes": list(m.prefixes),
        "krt": m.krt, "source": m.source, "description": describe(m),
    }
    return out


def _join(words: list[Word], indices: list[int]) -> list[str]:
    """SLP1 forms for the given word indices; compound members joined by '-'."""
    out: list[str] = []
    glue = False
    for pos, i in enumerate(indices):
        w = words[i]
        if glue and out:
            out[-1] += "-" + w.form
        else:
            out.append(w.form)
        nxt = words[indices[pos + 1]] if pos + 1 < len(indices) else None
        glue = bool(w.in_compound and nxt is not None and nxt.compound == w.compound)
    return out


def _padaccheda(r: Reading, n_lines: int) -> list[dict[str, str]]:
    res = []
    for line in range(n_lines):
        idx = [i for i, w in enumerate(r.words) if w.line == line]
        joined = " ".join(_join(r.words, idx))
        res.append({"devanagari": " ".join(to_deva(f) for f in _join(r.words, idx)), "iast": to_iast(joined),
                    "slp1": joined})
    return res


def _word_json(i: int, w: Word, full: bool) -> dict[str, Any]:
    proof = w.proof
    verified = bool(proof and proof.derivable)
    others = [a for k, a in enumerate(w.analyses) if k != w.chosen]
    if not full:
        others = others[:MAX_ALTERNATIVE_ANALYSES]
    return {
        "index": i, "form": scripts(w.form), "line": w.line, "span": [w.start, w.end],
        "in_compound": w.in_compound, "compound": w.compound,
        "analysis": _analysis_json(w.morph),
        "other_analyses": [_analysis_json(a) for a in others],
        "verified": verified,
        "verified_reason": (proof.note if proof and proof.note else
                            ("derived by " + proof.method if verified else "no derivation found")),
        "sutra_trace": [to_jsonable(s) for s in (proof.trace if proof else [])],
        "role": w.role, "head": w.head, "gloss": w.gloss, "gloss_source": w.gloss_source,
        "arsha": w.arsha,
    }


def _compound_json(r: Reading, c: Any) -> dict[str, Any]:
    return {"id": c.id, "members": [scripts(r.words[i].form) for i in c.members], "member_indices": c.members,
            "stem": scripts(c.stem), "type": c.samasa, "vigraha": scripts(c.vigraha), "basis": c.basis}


def _anvaya(r: Reading) -> dict[str, Any]:
    forms = _join(r.words, [i for i in r.anvaya if 0 <= i < len(r.words)])
    return {"order": list(r.anvaya), "devanagari": " ".join(to_deva(f) for f in forms),
            "iast": " ".join(to_iast(f) for f in forms)}


def _gloss(r: Reading) -> list[dict[str, str]]:
    return [{"word": w.form, "iast": to_iast(w.form), "devanagari": to_deva(w.form), "gloss": w.gloss}
            for w in r.words]


def _alignment(r: Reading) -> list[dict[str, Any]]:
    return [{"word": a.word, "start": a.start, "end": a.end, "text": r.translation[a.start:a.end]}
            for a in r.alignment]


def _alternative(rank: int, r: Reading, n_lines: int, full: bool) -> dict[str, Any]:
    alt: dict[str, Any] = {
        "rank": rank, "padaccheda": _padaccheda(r, n_lines), "scores": dict(r.scores), "status": r.status,
        "sandhi_ok": r.sandhi_ok, "notes": list(r.notes), "translation": r.translation,
    }
    if full:
        alt["words"] = [_word_json(i, w, True) for i, w in enumerate(r.words)]
    return alt


def to_json(analysis: VerseAnalysis, *, full: bool = False) -> dict[str, Any]:
    """Public JSON for ``analysis``. ``full=False`` trims alternates and other readings' traces."""
    n = len(analysis.lines)
    out: dict[str, Any] = {
        "id": analysis.id, "input": analysis.input,
        "lines": [scripts(s) for s in analysis.lines], "metre": to_jsonable(analysis.metre),
        "split_counts": list(analysis.split_counts), "status": analysis.status,
        "notes": list(analysis.notes),
    }
    if analysis.readings:
        r = analysis.readings[0]
        out.update({
            "reading_status": r.status, "sandhi_ok": r.sandhi_ok, "scores": dict(r.scores),
            "padaccheda": _padaccheda(r, n),
            "words": [_word_json(i, w, full) for i, w in enumerate(r.words)],
            "compounds": [_compound_json(r, c) for c in r.compounds],
            "anvaya": _anvaya(r), "gloss": _gloss(r), "translation": r.translation,
            "alignment": _alignment(r), "reading_notes": list(r.notes),
        })
    else:
        out.update({"reading_status": "unverified", "sandhi_ok": False, "scores": {}, "padaccheda": [],
                    "words": [], "compounds": [], "anvaya": {"order": [], "devanagari": "", "iast": ""},
                    "gloss": [], "translation": "", "alignment": [], "reading_notes": []})
    out["alternatives"] = [_alternative(k, r, n, full) for k, r in enumerate(analysis.readings[1:], start=1)]
    return out
