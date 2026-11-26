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
Lemmas and features are compared under the citation conventions documented in ``mayur/ud.py``
(``same_lemma``, ``same_feats``): strong-stem citations (हनुमन्त् = हनुमत्), and no feature scoring
for words the corpus classes as indeclinable.

Two more conventions of the corpus are followed when its split is compared with ours:

* The corpus never marks an indeclinable as a compound member: the prefixes स-, सु-, अ-, अति- and
  adverbs standing first in a compound (पुनर्-, तथा-) are tagged as free words (0 of 166 frequent
  indeclinables ever carry the member flag in the training chapters). Our analysis keeps them as
  members; for scoring, such a member is counted the corpus's way (``scored_member``).
* A pada is compared as it is written: the members are joined by sandhi (नख + आघातस् = नखाघातस्),
  not by gluing their letters, so a compound we keep whole equals the corpus's two members.
"""

from __future__ import annotations

import argparse
import json
import sys
import traceback
from pathlib import Path
from typing import Any, Callable, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import freq, gold, lipi, sandhi, ud  # noqa: E402
from mayur.model import VERIFIED  # noqa: E402

FEATURES = ("Case", "Number", "Gender", "Tense", "Mood", "Person", "VerbForm")
_VARGA = {"ङ्": "कखगघ", "ञ्": "चछजझ", "ण्": "टठडढ", "न्": "तथदधन", "म्": "पफबभम"}


_FINAL_STOP = {"द्": "त्", "ग्": "क्", "ड्": "ट्", "ब्": "प्"}


def normalize(form: str) -> str:
    """Spelling differences that are not analysis differences, removed before comparing forms.

    * anusvara for a nasal + virama followed by a consonant of its own varga (साम्प्रतम् = सांप्रतम्);
    * a pada-final voiced stop as its unvoiced partner (the corpus writes both काचिद् and काचित्);
    * ण as न: the corpus often undoes retroflexion in its reconstructed forms (ब्रह्मना for ब्रह्मणा).
    """
    for voiced, plain in _FINAL_STOP.items():
        if form.endswith(voiced):
            form = form[: -len(voiced)] + plain
    form = form.replace("ण", "न")
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
    same_lemma = same_lexeme(lemma, gold_lemma)
    if compound_member and gold_lemma and (f == normalize(gold_lemma) or same_lemma):
        return True
    return lenient and same_lemma


def _lexeme(lemma: str) -> str:
    return normalize(ud.canonical_lemma(lemma))


def same_lexeme(ours: str, gold_lemma: str) -> bool:
    """Same lemma under the citation conventions of ``mayur.ud`` (strong stems, feminine stems)."""
    if not ours or not gold_lemma:
        return False
    a, b = _lexeme(ours), _lexeme(gold_lemma)
    return a == b or ud._feminine_of(a, b)


def scored_member(w: Any) -> bool:
    """Whether our word counts as a compound member when compared with the corpus, which tags
    indeclinable members and glued prefixes as free words (see the module docstring)."""
    if not w.in_compound:
        return False
    lemma = ud.lemma(w.morph) if w.morph is not None else w.form
    return freq.lemma_class(lemma) != "indeclinable"


def _parts(ours_word: Sequence[Any]) -> tuple[str, str]:
    """(form, lemma) of one of our words given as (form, in_compound[, lemma])."""
    return ours_word[0], (ours_word[2] if len(ours_word) > 2 else "")


def our_word(w: Any) -> tuple[str, bool, str]:
    return w.form, scored_member(w), (ud.lemma(w.morph) if w.morph is not None else "")


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


def align_words(ours: Sequence[Sequence[Any]], gold_words: Sequence[dict],
                lenient: bool = False) -> list[tuple[int, int]]:
    """LCS alignment; ``lenient`` also pairs words with the same lemma but a differently
    reconstructed form (the corpus has मम where the text has मे)."""
    return lcs_pairs(ours, gold_words, lambda o, g: word_matches(
        _parts(o)[0], g["form"], g["lemma"], g["compound_member"], _parts(o)[1], lenient))


def morphology_counts(pairs: Sequence[tuple[Any, dict]]) -> dict[str, int]:
    """Counts over (Morph | None, gold word) pairs of non-compound words."""
    c = {"words": 0, "lemma": 0, "all_features": 0, "analysis": 0, **{f"feat_{k}_total": 0 for k in FEATURES},
         **{f"feat_{k}": 0 for k in FEATURES}}
    for morph, g in pairs:
        c["words"] += 1
        ours = ud.feats(morph) if morph is not None else {}
        upos = g.get("upos", "")
        lemma_ok = morph is not None and ud.same_lemma(morph, g["lemma"], upos)
        c["lemma"] += int(lemma_ok)
        c["analysis"] += int(lemma_ok and ud.same_feats(morph, upos, g["feats"]))  # lemma AND every feature
        for k in ud.compared_features(upos, g["feats"]):
            if k in FEATURES:
                c[f"feat_{k}_total"] += 1
                c[f"feat_{k}"] += int(ours.get(k) == g["feats"][k])
        c["all_features"] += int(morph is not None and ud.same_feats(morph, upos, g["feats"]))
    return c


def add_counts(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    return {k: a.get(k, 0) + b.get(k, 0) for k in {*a, *b}}


def pada_units(words: Sequence[Sequence[Any]]) -> list[tuple[str, str, tuple[str, ...]]]:
    """Group (form, in_compound[, lemma]) words into padas: a run of compound members plus its final
    word is ONE unit ``(glued forms, lemma of the final word, member forms)``."""
    units, run = [], []
    for w in words:
        run.append(w[0])
        if not w[1]:
            units.append(("".join(run), w[2] if len(w) > 2 else "", tuple(run)))
            run = []
    if run:
        units.append(("".join(run), "", tuple(run)))
    return units


def gold_pada_units(gold_words: Sequence[dict]) -> list[tuple[str, str, tuple[str, ...]]]:
    return pada_units([(w["form"], w["compound_member"], w["lemma"]) for w in gold_words])


def written(members: Sequence[str]) -> frozenset[str]:
    """The ways a pada made of ``members`` is written: joined by compound sandhi, cited in isolation."""
    if len(members) == 1:
        return frozenset({normalize(lipi.pausa(members[0]))})
    try:
        return frozenset(normalize(x) for x in sandhi.rejoin(list(members), [True] * (len(members) - 1)))
    except Exception:  # noqa: BLE001 - a corpus form the sandhi rules cannot read
        return frozenset()


def pada_match(ours: Sequence[Any], gold_unit: Sequence[Any]) -> bool:
    """Same pada: the same glued forms, the same written word after sandhi, or failing that the
    same lemma of the final member."""
    if normalize(ours[0]) == normalize(gold_unit[0]) or same_lexeme(ours[1], gold_unit[1]):
        return True
    return len(ours) > 2 and len(gold_unit) > 2 and bool(written(ours[2]) & written(gold_unit[2]))


def pada_line_equal(ours: Sequence[Sequence[Any]], gold_words: Sequence[dict]) -> bool:
    a, b = pada_units(ours), gold_pada_units(gold_words)
    return len(a) == len(b) and all(pada_match(x, y) for x, y in zip(a, b))


def end_to_end_ok(ours: Any, gold_word: dict) -> bool:
    """An aligned word counts as end-to-end correct when the form matches AND, for a pada, the lemma and
    all features are right; a non-final compound member needs the form (and to be one of our members) only."""
    if gold_word["compound_member"] or ours.in_compound:
        return bool(gold_word["compound_member"] and ours.in_compound)
    c = morphology_counts([(ours.morph, gold_word)])
    return bool(c["lemma"] and c["all_features"])


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
    res["pada_lines_exact"] = [pada_line_equal(o, gl) for o, gl in zip(ours_lines, gold_lines)]
    res["pada_gold"] = sum(len(gold_pada_units(gl)) for gl in gold_lines)
    res["pada_ours"] = sum(len(pada_units(o)) for o in ours_lines)
    res["pada_matched"] = sum(len(lcs_pairs(pada_units(o), gold_pada_units(gl), pada_match))
                              for o, gl in zip(ours_lines, gold_lines))
    res["gold_in_readings"] = any(
        all(split_equal([our_word(w) for w in line_words(r, i)], gl) for i, gl in enumerate(gold_lines))
        for r in analysis.readings)
    matched, same, pairs, mismatches, e2e = 0, 0, [], [], 0
    for i, (o, gl) in enumerate(zip(ours_lines, gold_lines)):
        matched += len(align_words(o, gl))
        al = align_words(o, gl, lenient=True)
        same += len(al)
        words = line_words(reading, i)
        pairs += [(words[a].morph, gl[b]) for a, b in al if not words[a].in_compound and not gl[b]["compound_member"]]
        e2e += sum(end_to_end_ok(words[a], gl[b]) for a, b in al)
        if not res["lines_exact"][i]:
            mismatches.append({"line": i, "ours": " ".join(x[0] for x in o), "gold": " ".join(x["form"] for x in gl)})
    res["matched"] = matched
    res["matched_same"] = same
    res["e2e_correct"] = e2e
    res["book"] = g.get("book", "")
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
            "e2e_correct": 0, "book": g.get("book", ""),
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
        "pada_lines_exact": sum(sum(r.get("pada_lines_exact", [])) for r in results),
        "pada_gold": sum(r.get("pada_gold", 0) for r in results),
        "pada_ours": sum(r.get("pada_ours", 0) for r in results),
        "pada_matched": sum(r.get("pada_matched", 0) for r in results),
        "verses_exact": sum(r["verse_exact"] for r in results),
        "gold_in_readings": sum(r["gold_in_readings"] for r in results),
        "verses_verified": sum(r["verified"] for r in results),
        "gold_words": gw, "our_words": ow, "matched_words": mt, **prf(mt, ow, gw),
        "same_word": prf(sum(r.get("matched_same", 0) for r in results), ow, gw),
        "e2e_correct": sum(r.get("e2e_correct", 0) for r in results),
        "pada": prf(sum(r.get("pada_matched", 0) for r in results), sum(r.get("pada_ours", 0) for r in results),
                    sum(r.get("pada_gold", 0) for r in results)),
        "proof_words": pw, "proof_verified": pv, "morphology": mc,
    }


def _frac(a: int, b: int) -> str:
    return f"{a}/{b} = {100 * a / b:.1f}%" if b else f"{a}/{b}"


def report(results: Sequence[dict[str, Any]], s: dict[str, Any]) -> str:
    out = [f"verses evaluated: {s['verses']}  (exceptions: {s['failures']})",
           f"PADA level (compound = one unit): half-verses exact {_frac(s['pada_lines_exact'], s['lines'])}; "
           f"padas P {_frac(s['pada_matched'], s['pada_ours'])}, R {_frac(s['pada_matched'], s['pada_gold'])}, "
           f"F1 {s['pada']['f1']:.3f}",
           "MEMBER level (compound members separate):",
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


TEST_LABELS = {"1067": "रामायण १.१", "7305": "कुमारसम्भव १", "7242": "गीता १", "7243": "गीता २"}


def test_set_docs() -> list[tuple[str, dict[str, Any]]]:
    """(label, gold document restricted to the test verse range) for each entry of splits.json["test"]."""
    from mayur import dcs

    docs = []
    for e in dcs.split_files("test"):
        cid = Path(e["file"]).stem.rsplit("-", 1)[-1]
        label = TEST_LABELS.get(cid, cid)
        doc = gold.from_conllu(Path(e["file"]), label)
        if e["verses"]:
            doc["verses"] = [v for v in doc["verses"] if e["verses"][0] <= v["number"] <= e["verses"][1]]
        docs.append((label, doc))
    return docs


def run_verses(docs: Sequence[dict[str, Any]], analyze: Callable[..., Any]) -> list[dict[str, Any]]:
    results = []
    for g in docs:
        try:
            results.append(evaluate_verse(g, analyze))
        except Exception as exc:  # noqa: BLE001 - counted as a failure and printed, never hidden
            results.append(failed_result(g, exc))
            print(f"verse {g['id']}: FAILED {exc!r}", file=sys.stderr)
    return results


def table_row(label: str, s: dict[str, Any]) -> str:
    m = s["morphology"]
    return (f"{label:<14}{s['verses']:>7}{s['failures']:>6}  {_frac(s['pada_lines_exact'], s['lines']):<18}"
            f"{_frac(s['lines_exact'], s['lines']):<18}{_frac(s['lines_same_words'], s['lines']):<18}"
            f"{s['pada']['f1']:.3f}  {s['f1']:.3f}  {_frac(m.get('lemma', 0), m.get('words', 0))}")


def all_tests(analyze: Callable[..., Any]) -> tuple[str, dict[str, Any]]:
    """Run the test sets of splits.json; one summary table (and the numbers as a dict)."""
    head = (f"{'test set':<14}{'verses':>7}{'fail':>6}  {'pada half-verse':<18}{'member half-verse':<18}"
            f"{'same words':<18}padaF1  memF1  lemma")
    rows, per_set, everything = [head], {}, []
    for label, doc in test_set_docs():
        res = run_verses(doc["verses"], analyze)
        per_set[label] = summarize(res)
        everything += res
        rows.append(table_row(label, per_set[label]))
    per_set["all"] = summarize(everything)
    rows.append(table_row("all", per_set["all"]))
    return "\n".join(rows), per_set


def headline(s: dict[str, Any]) -> str:
    m = s["morphology"]
    return "\n".join([
        "HEADLINE (word level):",
        f"  words identified (same boundaries and lexeme) F1: {s['same_word']['f1']:.3f}"
        f"  (P {s['same_word']['precision']:.3f}, R {s['same_word']['recall']:.3f})",
        f"  padas identified (a compound is one pada, compared as written) F1: {s['pada']['f1']:.3f}",
        f"  segmentation F1 on exact forms, member level: {s['f1']:.3f}",
        f"  lemma accuracy: {_frac(m.get('lemma', 0), m.get('words', 0))}",
        f"  all-features accuracy: {_frac(m.get('all_features', 0), m.get('words', 0))}",
        f"  full analysis (lemma and every feature) right: {_frac(m.get('analysis', 0), m.get('words', 0))}",
        f"  END-TO-END word accuracy: {_frac(s['e2e_correct'], s['gold_words'])}"])


def per_text_table(results: Sequence[dict[str, Any]]) -> str:
    books: dict[str, list[dict[str, Any]]] = {}
    for r in results:
        books.setdefault(r.get("book", ""), []).append(r)
    rows = [f"{'text':<22}{'verses':>7}{'F1':>8}  {'all-features':<20}{'end-to-end'}"]
    for book, rs in sorted(books.items()):
        s = summarize(rs)
        m = s["morphology"]
        rows.append(f"{book:<22}{s['verses']:>7}{s['f1']:>8.3f}  "
                    f"{_frac(m.get('all_features', 0), m.get('words', 0)):<20}{_frac(s['e2e_correct'], s['gold_words'])}")
    return "\n".join(rows)


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
    ap.add_argument("--sample", default=None, help="evaluate a file made by scripts/sample_test.py")
    ap.add_argument("--all-tests", action="store_true", help="run the test sets of data/derived/splits.json")
    args = ap.parse_args(argv)
    from mayur.pipeline import analyze_verse

    if args.all_tests:
        table, per_set = all_tests(analyze_verse)
        print(table)
        if args.json:
            Path(args.json).write_text(json.dumps(per_set, ensure_ascii=False, indent=1), encoding="utf-8")
        return 0
    if args.sample:
        doc = json.loads(Path(args.sample).read_text(encoding="utf-8"))
        results = run_verses(doc["verses"], analyze_verse)
        summary = summarize(results)
        print(f"sample: {doc['label']} ({doc['pool']}), {len(results)} verses")
        print(headline(summary))
        print(per_text_table(results))
        print(report(results, summary))
        if args.json:
            Path(args.json).write_text(json.dumps({"summary": summary, "verses": results}, ensure_ascii=False,
                                                  indent=1), encoding="utf-8")
        return 0
    doc = gold.from_conllu(Path(args.conllu), args.label) if args.conllu else gold.load()
    by_number = {v["number"]: v for v in doc["verses"]}
    wanted = parse_range(args.verses, max(by_number))
    print(f"gold: {doc['source']}")
    results = run_verses([by_number[n] for n in wanted if n in by_number], analyze_verse)
    summary = summarize(results)
    print(report(results, summary))
    if args.json:
        Path(args.json).write_text(json.dumps({"summary": summary, "verses": results}, ensure_ascii=False, indent=1),
                                   encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
