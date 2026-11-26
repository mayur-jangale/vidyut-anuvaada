"""Evaluate the pipeline against DCS gold for Ramayana Bala 1 (held out of the frequency tables).

    python eval/eval_dcs.py [--verses 1-20] [--json eval/results.json]

Normalisation (applied to both sides before comparing forms and lemmas): a final or
pre-consonantal anusvara M is rewritten as the homorganic nasal (final M -> m), so
``puMgava`` == ``puNgava``; compound members are compared as stems on both sides.
Split quality is measured per half-verse on the exact sequence of forms, and on the
token level via LCS alignment (precision = LCS/ours, recall = LCS/gold, F1).
Morphology is scored on LCS-aligned non-compound words only.
"""

from __future__ import annotations

import argparse
import json
import sys
import traceback
from pathlib import Path
from typing import Any, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

FEATURES = ("Case", "Number", "Gender", "Tense", "Mood", "Person", "VerbForm")
_STOPS = {"k": "N", "K": "N", "g": "N", "G": "N", "c": "Y", "C": "Y", "j": "Y", "J": "Y",
          "w": "R", "W": "R", "q": "R", "Q": "R", "t": "n", "T": "n", "d": "n", "D": "n",
          "p": "m", "P": "m", "b": "m", "B": "m"}


def normalise(s: str) -> str:
    """Anusvara/nasal normalisation described in the module docstring."""
    out = []
    for i, ch in enumerate(s):
        if ch == "M":
            nxt = s[i + 1] if i + 1 < len(s) else ""
            out.append(_STOPS.get(nxt, "m") if nxt else "m")
        else:
            out.append(ch)
    return "".join(out)


def lcs_pairs(a: Sequence[str], b: Sequence[str]) -> list[tuple[int, int]]:
    """Index pairs (i, j) of one longest common subsequence of a and b."""
    n, m = len(a), len(b)
    t = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            t[i][j] = t[i + 1][j + 1] + 1 if a[i] == b[j] else max(t[i + 1][j], t[i][j + 1])
    i = j = 0
    pairs = []
    while i < n and j < m:
        if a[i] == b[j]:
            pairs.append((i, j))
            i += 1
            j += 1
        elif t[i + 1][j] >= t[i][j + 1]:
            i += 1
        else:
            j += 1
    return pairs


# --- feature mapping -------------------------------------------------------------

_CASE = {"praTamA": "Nom", "dvitIyA": "Acc", "tftIyA": "Ins", "caturTI": "Dat",
         "paYcamI": "Abl", "zazWI": "Gen", "saptamI": "Loc", "samboDana": "Voc"}
_GENDER = {"puM": "Masc", "strI": "Fem", "napuMsaka": "Neut"}
_NUMBER = {"eka": "Sing", "dvi": "Dual", "bahu": "Plur"}
_PERSON = {"praTama": "3", "maDyama": "2", "uttama": "1"}
_LAKARA = {"la~w": ("Pres", "Ind"), "li~w": ("Past", "Ind"), "lu~w": ("Fut", "Ind"),
           "lf~w": ("Fut", "Cond"), "le~w": ("", "Sub"), "lo~w": ("Pres", "Imp"),
           "la~N": ("Past", "Ind"), "li~N": ("", "Pot"), "ASIrli~N": ("", "Prec"),
           "lu~N": ("Past", "Ind"), "lf~N": ("Fut", "Cond")}


def _fallback_feats(m: Any) -> dict[str, str]:
    f: dict[str, str] = {}
    if getattr(m, "vibhakti", None) in _CASE:
        f["Case"] = _CASE[m.vibhakti]
    if getattr(m, "linga", None) in _GENDER:
        f["Gender"] = _GENDER[m.linga]
    if getattr(m, "vacana", None) in _NUMBER:
        f["Number"] = _NUMBER[m.vacana]
    if getattr(m, "purusha", None) in _PERSON:
        f["Person"] = _PERSON[m.purusha]
    if getattr(m, "lakara", None) in _LAKARA:
        t, mood = _LAKARA[m.lakara]
        if t:
            f["Tense"] = t
        f["Mood"] = mood
    if getattr(m, "krt", None):
        f["VerbForm"] = "Part"
    return f


def our_lemma(m: Any) -> str:
    try:
        from mayur.labels import ud_lemma

        return ud_lemma(m)
    except Exception:  # noqa: BLE001 - labels may be absent or incomplete
        return m.lemma


def our_feats(m: Any) -> dict[str, str]:
    try:
        from mayur.labels import ud_feats

        r = ud_feats(m)
        if isinstance(r, str):
            r = dict(p.split("=", 1) for p in r.split("|") if "=" in p)
        return dict(r)
    except Exception:  # noqa: BLE001
        return _fallback_feats(m)


# --- metrics on plain data -------------------------------------------------------

def line_forms(words: Sequence[dict], line: int) -> list[str]:
    return [normalise(w["form"]) for w in words if w["line"] == line]


def compare_verse(ours: Sequence[dict], gold_lines: Sequence[Sequence[dict]]) -> dict[str, Any]:
    """Compare one reading (list of word dicts with form/line/in_compound/morph/proof_ok)
    with gold lines (lists of gold word dicts). Returns counts only."""
    r: dict[str, Any] = {"lines": len(gold_lines), "lines_exact": 0, "tp": 0, "ours": 0, "gold": 0,
                         "mismatches": [], "lemma_n": 0, "lemma_ok": 0, "all_n": 0, "all_ok": 0,
                         "feat_n": {k: 0 for k in FEATURES}, "feat_ok": {k: 0 for k in FEATURES},
                         "words": len(ours), "proof_ok": sum(1 for w in ours if w.get("proof_ok"))}
    for li, gl in enumerate(gold_lines):
        ow = [w for w in ours if w["line"] == li]
        of = [normalise(w["form"]) for w in ow]
        gf = [normalise(w["form"]) for w in gl]
        pairs = lcs_pairs(of, gf)
        r["tp"] += len(pairs)
        r["ours"] += len(of)
        r["gold"] += len(gf)
        if of == gf:
            r["lines_exact"] += 1
        else:
            r["mismatches"].append({"line": li, "ours": of, "gold": gf})
        for i, j in pairs:
            g, o = gl[j], ow[i]
            m = o.get("morph")
            if g.get("compound_member") or o.get("in_compound"):
                continue
            r["lemma_n"] += 1
            if m is None:
                if g["feats"]:
                    r["all_n"] += 1
                for k in FEATURES:
                    if k in g["feats"]:
                        r["feat_n"][k] += 1
                continue
            if normalise(our_lemma(m)) == normalise(g["lemma"]):
                r["lemma_ok"] += 1
            of_ = our_feats(m)
            tracked = [k for k in FEATURES if k in g["feats"]]
            for k in tracked:
                r["feat_n"][k] += 1
                if of_.get(k) == g["feats"][k]:
                    r["feat_ok"][k] += 1
            if tracked:
                r["all_n"] += 1
                if all(of_.get(k) == g["feats"][k] for k in tracked):
                    r["all_ok"] += 1
    r["verse_exact"] = r["lines_exact"] == r["lines"] and all(
        not [w for w in ours if w["line"] >= r["lines"]] for _ in [0])
    return r


def _pct(a: int, b: int) -> Optional[float]:
    return round(100.0 * a / b, 2) if b else None


def aggregate(per_verse: Sequence[dict]) -> dict[str, Any]:
    ok = [v for v in per_verse if not v.get("error")]
    s = lambda k: sum(v[k] for v in ok)  # noqa: E731
    tp, no, ng = s("tp"), s("ours"), s("gold")
    p, rc = (tp / no if no else 0.0), (tp / ng if ng else 0.0)
    f1 = 2 * p * rc / (p + rc) if p + rc else 0.0
    return {
        "verses_total": len(per_verse), "verses_failed": len(per_verse) - len(ok),
        "lines_exact": [s("lines_exact"), s("lines")],
        "lines_exact_pct": _pct(s("lines_exact"), s("lines")),
        "verses_exact": [sum(1 for v in ok if v["verse_exact"]), len(per_verse)],
        "verses_exact_pct": _pct(sum(1 for v in ok if v["verse_exact"]), len(per_verse)),
        "verses_gold_in_alternatives": [sum(1 for v in ok if v.get("gold_in_alts")), len(per_verse)],
        "verses_gold_in_alternatives_pct": _pct(sum(1 for v in ok if v.get("gold_in_alts")), len(per_verse)),
        "token_precision": round(100 * p, 2), "token_recall": round(100 * rc, 2), "token_f1": round(100 * f1, 2),
        "token_counts": {"tp": tp, "ours": no, "gold": ng},
        "lemma_acc": [s("lemma_ok"), s("lemma_n")], "lemma_acc_pct": _pct(s("lemma_ok"), s("lemma_n")),
        "feature_acc": {k: [sum(v["feat_ok"][k] for v in ok), sum(v["feat_n"][k] for v in ok)] for k in FEATURES},
        "feature_acc_pct": {k: _pct(sum(v["feat_ok"][k] for v in ok), sum(v["feat_n"][k] for v in ok))
                            for k in FEATURES},
        "all_features_acc": [s("all_ok"), s("all_n")], "all_features_acc_pct": _pct(s("all_ok"), s("all_n")),
        "words_proof_verified": [s("proof_ok"), s("words")], "words_proof_verified_pct": _pct(s("proof_ok"), s("words")),
        "verses_status_verified": [sum(1 for v in ok if v.get("status") == "verified"), len(per_verse)],
        "verses_status_verified_pct": _pct(sum(1 for v in ok if v.get("status") == "verified"), len(per_verse)),
    }


# --- driving the pipeline -------------------------------------------------------

def reading_words(reading: Any) -> list[dict]:
    out = []
    for w in reading.words:
        out.append({"form": w.form, "line": w.line, "in_compound": w.in_compound, "morph": w.morph,
                    "proof_ok": bool(w.proof and w.proof.derivable)})
    return out


def parse_range(s: str, available: Sequence[int]) -> list[int]:
    if not s:
        return list(available)
    a, _, b = s.partition("-")
    lo, hi = int(a), int(b or a)
    return [n for n in available if lo <= n <= hi]


def evaluate_verse(number: int, gold_verse: dict) -> dict[str, Any]:
    from mayur import gold
    from mayur.pipeline import analyze_verse

    glines = [ln["words"] for ln in gold_verse["lines"]]
    an = analyze_verse(gold.verse_text(number), verse_id=gold_verse["id"])
    if not an.readings:
        raise RuntimeError("pipeline returned no readings")
    res = compare_verse(reading_words(an.readings[0]), glines)
    res["gold_in_alts"] = any(
        compare_verse(reading_words(rd), glines)["verse_exact"] for rd in an.readings)
    res["status"] = an.readings[0].status
    res["number"] = number
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verses", default="", help="e.g. 1-20 (default: all)")
    ap.add_argument("--json", default="eval/results.json")
    a = ap.parse_args()
    from mayur import gold

    verses = {v["number"]: v for v in gold.load()["verses"]}
    nums = parse_range(a.verses, sorted(verses))
    per: list[dict] = []
    for n in nums:
        try:
            per.append(evaluate_verse(n, verses[n]))
        except Exception as e:  # noqa: BLE001 - counted as failure, printed below
            print(f"verse {n}: FAILED {type(e).__name__}: {e}", file=sys.stderr)
            traceback.print_exc(limit=3, file=sys.stderr)
            per.append({"number": n, "error": f"{type(e).__name__}: {e}"})
    agg = aggregate(per)
    print(f"{'verse':>5} {'lines':>6} {'F1-ish tp/gold':>15} {'status':>10}  note")
    for v in per:
        if v.get("error"):
            print(f"{v['number']:>5} {'-':>6} {'-':>15} {'ERROR':>10}  {v['error']}")
        else:
            print(f"{v['number']:>5} {v['lines_exact']}/{v['lines']:>4} {v['tp']:>6}/{v['gold']:<8} "
                  f"{v['status']:>10}  {'exact' if v['verse_exact'] else 'split differs'}")
    print("\nMISMATCHES (ours vs gold)")
    for v in per:
        for mm in v.get("mismatches", []):
            print(f"  verse {v['number']} line {mm['line'] + 1}\n    ours: {' '.join(mm['ours'])}\n    gold: {' '.join(mm['gold'])}")
    print("\nSUMMARY")
    for k, val in agg.items():
        print(f"  {k}: {val}")
    Path(a.json).parent.mkdir(parents=True, exist_ok=True)
    Path(a.json).write_text(json.dumps({"summary": agg, "verses": per}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nwrote {a.json}")
    return 0 if agg["verses_failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
