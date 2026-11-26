"""Evaluate mayur against DCS gold verses (default: Ramayana, Balakanda sarga 1).

    python eval/eval_dcs.py [--verses 1-20] [--json eval/results.json]
    python eval/eval_dcs.py --conllu <DCS chapter file of any book> --label "मनुस्मृति १" --verses 1-20

Every number is printed as n/N. The metric functions are pure and unit-tested.
Normalisation used when comparing word forms: an internal nasal consonant with virama before a
consonant of its own varga is written as anusvara (साम्प्रतम् == सांप्रतम्), and a compound member
counts as correct if its form or lemma equals the gold form or lemma (DCS writes some members as
the lemma: वाच् where the text has वाक्). That is the strict "split exact" number. A second,
lenient number ("same words") also accepts any word whose lemma equals the gold lemma, because
DCS sometimes reconstructs a different surface form than the text has (मम for मे, विद्वास् for विद्वान्).
"""

from __future__ import annotations

import argparse
import json
import sys
import traceback
from pathlib import Path
from typing import Any, Callable, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import gold, ud  # noqa: E402
from mayur.model import VERIFIED  # noqa: E402

FEATURES = ("Case", "Number", "Gender", "Tense", "Mood", "Person", "VerbForm")
_VARGA = {"ङ्": "कखगघ", "ञ्": "चछजझ", "ण्": "टठडढ", "न्": "तथदधन", "म्": "पफबभम"}


def normalize(form: str) -> str:
    """Anusvara for a nasal + virama followed by a consonant of its own varga."""
    out, i = [], 0
    while i < len(form):
        pair = form[i:i + 2]
        if pair in _VARGA and i + 2 < len(form) and form[i + 2] in _VARGA[pair]:
            out.append("ं")
            i += 2
        else:
            out.append(form[i])
            i += 1
    return "".join(out)


def word_matches(form: str, gold_form: str, gold_lemma: str = "", compound_member: bool = False,
                 lemma: str = "", lenient: bool = False) -> bool:
    f = normalize(form)
    if f == normalize(gold_form):
        return True
    same_lemma = bool(lemma and gold_lemma and normalize(lemma) == normalize(gold_lemma))
    if compound_member and gold_lemma and (f == normalize(gold_lemma) or same_lemma):
        return True
    return lenient and same_lemma


def _parts(ours_word: Sequence[Any]) -> tuple[str, str]:
    """(form, lemma) of one of our words given as (form, in_compound[, lemma])."""
    return ours_word[0], (ours_word[2] if len(ours_word) > 2 else "")


def our_word(w: Any) -> tuple[str, bool, str]:
    return w.form, w.in_compound, (ud.lemma(w.morph) if w.morph is not None else "")


def lcs_pairs(a: Sequence[Any], b: Sequence[Any], eq: Callable[[Any, Any], bool]) -> list[tuple[int, int]]:
    """Index pairs (i, j) of one longest common subsequence of ``a`` and ``b`` under ``eq``."""
    n, m = len(a), len(b)
    table = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            table[i][j] = table[i + 1][j + 1] + 1 if eq(a[i], b[j]) else max(table[i + 1][j], table[i][j + 1])
    pairs, i, j = [], 0, 0
    while i < n and j < m:
        if eq(a[i], b[j]):
            pairs.append((i, j))
            i, j = i + 1, j + 1
        elif table[i + 1][j] >= table[i][j + 1]:
            i += 1
        else:
            j += 1
    return pairs


def prf(matched: int, n_ours: int, n_gold: int) -> dict[str, float]:
    p = matched / n_ours if n_ours else 0.0
    r = matched / n_gold if n_gold else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return {"precision": p, "recall": r, "f1": f}


def split_equal(ours: Sequence[Sequence[Any]], gold_words: Sequence[dict], lenient: bool = False) -> bool:
    """Our (form, in_compound[, lemma]) sequence equals the gold word sequence (after normalisation)."""
    return len(ours) == len(gold_words) and all(
        word_matches(_parts(o)[0], g["form"], g["lemma"], g["compound_member"], _parts(o)[1], lenient)
        for o, g in zip(ours, gold_words))


def align_words(ours: Sequence[Sequence[Any]], gold_words: Sequence[dict]) -> list[tuple[int, int]]:
    return lcs_pairs(ours, gold_words, lambda o, g: word_matches(
        _parts(o)[0], g["form"], g["lemma"], g["compound_member"], _parts(o)[1]))


def morphology_counts(pairs: Sequence[tuple[Any, dict]]) -> dict[str, int]:
    """Counts over (Morph | None, gold word) pairs of non-compound words."""
    c = {"words": 0, "lemma": 0, "all_features": 0, **{f"feat_{k}_total": 0 for k in FEATURES},
         **{f"feat_{k}": 0 for k in FEATURES}}
    for morph, g in pairs:
        c["words"] += 1
        ours = ud.feats(morph) if morph is not None else {}
        c["lemma"] += int(morph is not None and ud.lemma(morph) == g["lemma"])
        ok = True
        for k in FEATURES:
            if k in g["feats"]:
                c[f"feat_{k}_total"] += 1
                c[f"feat_{k}"] += int(ours.get(k) == g["feats"][k])
            ok = ok and ours.get(k) == g["feats"].get(k)
        c["all_features"] += int(ok)
    return c


def add_counts(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    return {k: a.get(k, 0) + b.get(k, 0) for k in {*a, *b}}


def line_words(reading: Any, line: int) -> list[Any]:
    return [w for w in reading.words if w.line == line]


def evaluate_verse(g: dict[str, Any], analyze: Callable[..., Any]) -> dict[str, Any]:
    """Metrics of one gold verse ``g``; ``analyze(text, verse_id=...)`` is ``pipeline.analyze_verse``."""
    number = g["number"]
    gold_lines = [[w for w in ln["words"]] for ln in g["lines"]]
    res: dict[str, Any] = {"verse": number, "id": g["id"], "n_lines": len(gold_lines),
                           "gold_words": sum(map(len, gold_lines)), "error": ""}
    analysis = analyze(gold.text_of(g), verse_id=g["id"])
    if not analysis.readings:
        raise ValueError("analysis has no readings")
    reading = analysis.readings[0]
    ours_lines = [[our_word(w) for w in line_words(reading, i)] for i in range(len(gold_lines))]
    res["our_words"] = sum(map(len, ours_lines))
    res["lines_exact"] = [split_equal(o, gl) for o, gl in zip(ours_lines, gold_lines)]
    res["verse_exact"] = all(res["lines_exact"])
    res["lines_same_words"] = [split_equal(o, gl, lenient=True) for o, gl in zip(ours_lines, gold_lines)]
    res["gold_in_readings"] = any(
        all(split_equal([our_word(w) for w in line_words(r, i)], gl) for i, gl in enumerate(gold_lines))
        for r in analysis.readings)
    matched, pairs, mismatches = 0, [], []
    for i, (o, gl) in enumerate(zip(ours_lines, gold_lines)):
        al = align_words(o, gl)
        matched += len(al)
        words = line_words(reading, i)
        pairs += [(words[a].morph, gl[b]) for a, b in al if not words[a].in_compound and not gl[b]["compound_member"]]
        if not res["lines_exact"][i]:
            mismatches.append({"line": i, "ours": " ".join(x[0] for x in o), "gold": " ".join(x["form"] for x in gl)})
    res["matched"] = matched
    res["morphology"] = morphology_counts(pairs)
    res["proof_words"] = len(reading.words)
    res["proof_verified"] = sum(1 for w in reading.words if w.proof is not None and w.proof.derivable)
    res["status"] = analysis.status
    res["verified"] = analysis.status == VERIFIED
    res["mismatches"] = mismatches
    return res


def failed_result(g: dict[str, Any], exc: BaseException) -> dict[str, Any]:
    number = g["number"]
    return {"verse": number, "id": g["id"], "n_lines": len(g["lines"]),
            "gold_words": sum(len(ln["words"]) for ln in g["lines"]), "our_words": 0, "matched": 0,
            "lines_exact": [False] * len(g["lines"]), "lines_same_words": [False] * len(g["lines"]),
            "verse_exact": False, "gold_in_readings": False,
            "morphology": {}, "proof_words": 0, "proof_verified": 0, "status": "error", "verified": False,
            "mismatches": [], "error": "".join(traceback.format_exception_only(type(exc), exc)).strip()}


def summarize(results: Sequence[dict[str, Any]]) -> dict[str, Any]:
    """Totals over per-verse results (failed verses count as misses)."""
    n = len(results)
    lines = sum(r["n_lines"] for r in results)
    mc: dict[str, int] = {}
    for r in results:
        mc = add_counts(mc, r["morphology"])
    gw, ow, mt = (sum(r[k] for r in results) for k in ("gold_words", "our_words", "matched"))
    pw, pv = sum(r["proof_words"] for r in results), sum(r["proof_verified"] for r in results)
    return {
        "verses": n, "failures": sum(1 for r in results if r["error"]),
        "lines": lines, "lines_exact": sum(sum(r["lines_exact"]) for r in results),
        "lines_same_words": sum(sum(r.get("lines_same_words", [])) for r in results),
        "verses_exact": sum(r["verse_exact"] for r in results),
        "gold_in_readings": sum(r["gold_in_readings"] for r in results),
        "verses_verified": sum(r["verified"] for r in results),
        "gold_words": gw, "our_words": ow, "matched_words": mt, **prf(mt, ow, gw),
        "proof_words": pw, "proof_verified": pv, "morphology": mc,
    }


def _frac(a: int, b: int) -> str:
    return f"{a}/{b} = {100 * a / b:.1f}%" if b else f"{a}/{b}"


def report(results: Sequence[dict[str, Any]], s: dict[str, Any]) -> str:
    out = [f"verses evaluated: {s['verses']}  (exceptions: {s['failures']})",
           f"split exact, half-verses: {_frac(s['lines_exact'], s['lines'])}",
           f"split exact, verses:      {_frac(s['verses_exact'], s['verses'])}",
           f"same words (lemma match), half-verses: {_frac(s['lines_same_words'], s['lines'])}",
           f"gold split among readings: {_frac(s['gold_in_readings'], s['verses'])}",
           f"tokens: precision {_frac(s['matched_words'], s['our_words'])}, recall "
           f"{_frac(s['matched_words'], s['gold_words'])}, F1 {s['f1']:.3f}"]
    m = s["morphology"]
    out.append(f"morphology on aligned non-compound words (N={m.get('words', 0)}):")
    out.append(f"  lemma: {_frac(m.get('lemma', 0), m.get('words', 0))}")
    for k in FEATURES:
        out.append(f"  {k}: {_frac(m.get(f'feat_{k}', 0), m.get(f'feat_{k}_total', 0))}")
    out.append(f"  all features correct: {_frac(m.get('all_features', 0), m.get('words', 0))}")
    out.append(f"words proof-verified: {_frac(s['proof_verified'], s['proof_words'])}")
    out.append(f"verses with status verified: {_frac(s['verses_verified'], s['verses'])}")
    out.append("\nper verse: verse  lines-exact  matched/gold/ours  status")
    for r in results:
        out.append(f"{r['verse']:>3}  {sum(r['lines_exact'])}/{r['n_lines']}  "
                   f"{r['matched']}/{r['gold_words']}/{r['our_words']}  {r.get('status', '')}"
                   + (f"  ERROR {r['error']}" if r["error"] else ""))
    out.append("\nmismatches (ours | gold):")
    for r in results:
        for mm in r.get("mismatches", []):
            out.append(f"{r['verse']}.{mm['line'] + 1}  {mm['ours']}  |  {mm['gold']}")
    return "\n".join(out)


def parse_range(spec: Optional[str], last: int) -> list[int]:
    if not spec:
        return list(range(1, last + 1))
    lo, _, hi = spec.partition("-")
    return list(range(int(lo), int(hi or lo) + 1))


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verses", default=None, help="e.g. 1-20 (default: all)")
    ap.add_argument("--json", default=None, help="write the numbers to this file")
    ap.add_argument("--conllu", default=None, help="evaluate on this DCS chapter file instead (any book)")
    ap.add_argument("--label", default="ग्रन्थ", help="verse id prefix used with --conllu")
    args = ap.parse_args(argv)
    from mayur.pipeline import analyze_verse

    doc = gold.from_conllu(Path(args.conllu), args.label) if args.conllu else gold.load()
    by_number = {v["number"]: v for v in doc["verses"]}
    wanted = parse_range(args.verses, max(by_number))
    print(f"gold: {doc['source']}")
    results = []
    for g in (by_number[n] for n in wanted if n in by_number):
        try:
            results.append(evaluate_verse(g, analyze_verse))
        except Exception as exc:  # noqa: BLE001 - counted as a failure and printed, never hidden
            results.append(failed_result(g, exc))
            print(f"verse {g['number']}: FAILED {exc!r}", file=sys.stderr)
    summary = summarize(results)
    print(report(results, summary))
    if args.json:
        Path(args.json).write_text(json.dumps({"summary": summary, "verses": results}, ensure_ascii=False, indent=1),
                                   encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
