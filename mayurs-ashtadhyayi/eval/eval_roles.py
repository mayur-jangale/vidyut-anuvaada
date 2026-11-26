"""Evaluate sentence structure (heads, roles, prose order) against gold treebanks and reference files.

    python eval/eval_roles.py --source ufal|dcs|vedic [--limit 300] [--json out.json]
    python eval/eval_roles.py --claude eval/review/claude/<file>.json [--limit N] [--json out.json]
    python eval/eval_roles.py --gold eval/review/gold_roles.json        (human corrections)
    python eval/eval_roles.py --agreement fileA.json fileB.json         (two annotators, no pipeline run)
    python eval/eval_roles.py --claude <file> --gold-words [--verses 21-40] [--matrix]

``--gold-words`` isolates the sentence layer: the Reading is built from the reference file's own words
(gold split and lemma; each word gets the lexicon analysis matching the gold feats, else a Morph built
from the feats: eval/gold_words.py) and only compounds.annotate -> shabdabodha.resolve -> anvaya.order
run. Without it the whole pipeline runs on the raw text (split and tagging errors included).
``--matrix`` prints the gold-role x predicted-role confusion matrix and the 40 most frequent wrong links.

For each gold sentence the pipeline (``mayur.pipeline.analyze_verse``) is run on its Devanagari text
(exceptions are caught and counted); our words are aligned to the gold words with the lemma-tolerant
alignment of eval/eval_dcs.py. Everything is reported on ALIGNED words that are not compound members
(gold words without a counterpart are counted):
  * head attachment (unlabelled): our head, with heads inside a compound moved to its final member, is
    the aligned counterpart of the gold head (both "clause head" counts as equal);
  * role accuracy and per-role precision/recall on words whose gold label maps to a role
    (mayur/treebank.py documents the mapping; unmapped labels are counted, not forced);
  * anvaya agreement where the gold has a prose order: share of word pairs in the same relative order
    (and Kendall tau = 2*share - 1).
  * a LENIENT role accuracy in which विशेषण and विधेय count as one class: annotators disagree on a word
    qualifying an unexpressed subject (विशेषण>verb, विधेय>verb or विधेय>none), so it is printed next to
    the strict number, never instead of it.
Every number is printed as n/N. Metric functions are pure and unit-tested (tests/test_eval_roles.py).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import traceback
from pathlib import Path
from typing import Any, Callable, Iterable, Optional, Sequence

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from mayur import treebank  # noqa: E402


def _load_dcs_eval() -> Any:
    spec = importlib.util.spec_from_file_location("eval_dcs", ROOT / "eval" / "eval_dcs.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ev = _load_dcs_eval()


def our_view(reading: Any) -> dict[str, Any]:
    """Our analysis as plain data: words with role and head (a head inside a compound is moved to the
    compound's final member), compounds (member indices, type), and the prose order."""
    final = {i: max(c.members) for c in reading.compounds for i in c.members}
    words = [{"form": w.form, "in_compound": w.in_compound, "lemma": ev.our_word(w)[2], "role": w.role,
              "head": None if w.head is None else final.get(w.head, w.head)} for w in reading.words]
    return {"words": words, "compounds": [{"members": sorted(c.members), "type": c.samasa} for c in reading.compounds],
            "anvaya": list(reading.anvaya)}


def align(ours: Sequence[dict], gold: Sequence[dict]) -> dict[int, int]:
    """Our word index -> gold word index."""
    pairs = ev.align_words([(w["form"], w["in_compound"], w["lemma"]) for w in ours], gold, lenient=True)
    return dict(pairs)


def pairwise_agreement(order_a: Sequence[Any], order_b: Sequence[Any]) -> tuple[int, int]:
    """(pairs in the same relative order, all pairs) over the items both orders contain."""
    common = [x for x in order_a if x in set(order_b)]
    pos_b = {x: i for i, x in enumerate(order_b)}
    agree = total = 0
    for i in range(len(common)):
        for j in range(i + 1, len(common)):
            total += 1
            agree += pos_b[common[i]] < pos_b[common[j]]
    return agree, total


LENIENT = {"विधेय": "विशेषण"}


def score_sentence(ours: dict[str, Any], gold: dict[str, Any], sid: str = "") -> dict[str, Any]:
    """Counts of one sentence. ``ours`` as from ``our_view``; ``gold`` a sentence of mayur.treebank."""
    gw = gold["words"]
    mapping = align(ours["words"], gw)
    gold_final = {i: max(c["members"]) for c in gold.get("compounds", []) for i in c["members"]}
    c: dict[str, Any] = {"gold_words": len(gw), "aligned": len(mapping), "unaligned_gold": len(gw) - len(mapping),
                         "members_skipped": 0, "evaluated": 0, "head_ok": 0, "role_eval": 0, "role_ok": 0,
                         "unmapped_gold_role": 0, "role_ok_lenient": 0, "roles": {}, "confusion": {}, "wrong": {}}

    def form_of(gi: Optional[int]) -> str:
        return gw[gi]["form"] if gi is not None and 0 <= gi < len(gw) else "-"
    for o, g in mapping.items():
        gwd, owd = gw[g], ours["words"][o]
        if gwd["compound_member"] or owd["in_compound"]:
            c["members_skipped"] += 1
            continue
        c["evaluated"] += 1
        h, gh = owd["head"], gwd["head_index"]
        gh = gold_final.get(gh, gh)
        head_ok = (h is None and gh is None) or (h is not None and gh is not None and mapping.get(h) == gh)
        c["head_ok"] += head_ok
        if not head_ok or owd["role"] != gwd["role"]:
            ours_head = ours["words"][h]["form"] if h is not None else "-"
            key = f"{gwd['role'] or '?'}>{form_of(gh)} | ours {owd['role'] or '-'}>{ours_head}"
            c["wrong"][f"{sid}: {gwd['form']}: {key}"] = 1
        if not gwd["role"]:
            c["unmapped_gold_role"] += 1
            continue
        c["role_eval"] += 1
        c["role_ok"] += owd["role"] == gwd["role"]
        c["role_ok_lenient"] += LENIENT.get(owd["role"], owd["role"]) == LENIENT.get(gwd["role"], gwd["role"])
        pair = f"{gwd['role']}|{owd['role'] or '-'}"
        c["confusion"][pair] = c["confusion"].get(pair, 0) + 1
        for role, key in ((gwd["role"], "gold"), (owd["role"], "pred")):
            if role:
                c["roles"].setdefault(role, {"gold": 0, "pred": 0, "tp": 0})[key] += 1
        if owd["role"] == gwd["role"]:
            c["roles"][gwd["role"]]["tp"] += 1
    if gold.get("anvaya") and ours.get("anvaya"):
        ours_order = [mapping[i] for i in ours["anvaya"] if i in mapping]
        c["anvaya_agree"], c["anvaya_pairs"] = pairwise_agreement(ours_order, list(gold["anvaya"]))
    return c


def add_counts(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    out = dict(a)
    for k, v in b.items():
        if k in ("confusion", "wrong"):
            merged = dict(a.get(k, {}))
            for key, n in v.items():
                merged[key] = merged.get(key, 0) + n
            out[k] = merged
        elif k == "roles":
            roles = {r: dict(d) for r, d in a.get("roles", {}).items()}
            for r, d in v.items():
                cur = roles.setdefault(r, {"gold": 0, "pred": 0, "tp": 0})
                for key, n in d.items():
                    cur[key] += n
            out["roles"] = roles
        else:
            out[k] = out.get(k, 0) + v
    return out


def frac(a: int, b: int) -> str:
    return f"{a}/{b} = {100 * a / b:.1f}%" if b else f"{a}/0"


def per_role(roles: dict[str, dict[str, int]]) -> list[dict[str, Any]]:
    rows = []
    for role, d in sorted(roles.items(), key=lambda kv: -kv[1]["gold"]):
        p = d["tp"] / d["pred"] if d["pred"] else 0.0
        r = d["tp"] / d["gold"] if d["gold"] else 0.0
        rows.append({"role": role, "gold": d["gold"], "pred": d["pred"], "tp": d["tp"], "precision": round(p, 3),
                     "recall": round(r, 3), "f1": round(2 * p * r / (p + r), 3) if p + r else 0.0})
    return rows


def report(total: dict[str, Any], sentences: int, errors: int, label: str) -> str:
    lines = [f"{label}: {sentences} sentences, {errors} pipeline exceptions (counted, not scored)",
             f"gold words {total.get('gold_words', 0)}; aligned {frac(total.get('aligned', 0), total.get('gold_words', 0))};"
             f" not aligned {total.get('unaligned_gold', 0)}; compound members skipped {total.get('members_skipped', 0)}",
             f"head attachment: {frac(total.get('head_ok', 0), total.get('evaluated', 0))}",
             f"role accuracy: {frac(total.get('role_ok', 0), total.get('role_eval', 0))}"
             f" (gold label unmapped: {total.get('unmapped_gold_role', 0)});"
             f" lenient (विशेषण = विधेय): {frac(total.get('role_ok_lenient', 0), total.get('role_eval', 0))}"]
    if total.get("anvaya_pairs"):
        a, n = total["anvaya_agree"], total["anvaya_pairs"]
        lines.append(f"anvaya pair order: {frac(a, n)}; Kendall tau {2 * a / n - 1:.3f}")
    lines.append("role            gold  pred    tp  precision  recall")
    lines += [f"{r['role']:<14}{r['gold']:>6}{r['pred']:>6}{r['tp']:>6}{r['precision']:>11.3f}{r['recall']:>8.3f}"
              for r in per_role(total.get("roles", {}))]
    return "\n".join(lines)


def matrix(total: dict[str, Any], top: int = 40) -> str:
    """Gold-role x predicted-role counts, then the most frequent wrong links (role or head)."""
    conf = total.get("confusion", {})
    golds = sorted({k.split("|")[0] for k in conf}, key=lambda r: -sum(n for k, n in conf.items() if k.startswith(r + "|")))
    preds = sorted({k.split("|")[1] for k in conf})
    head = "gold \\ pred".ljust(16) + "".join(p[:7].rjust(8) for p in preds)
    rows = [head] + [g[:15].ljust(16) + "".join(str(conf.get(f"{g}|{p}", "")).rjust(8) for p in preds) for g in golds]
    wrong = total.get("wrong", {})
    pattern: dict[str, list[str]] = {}
    for key in wrong:
        sid, rest = key.split(": ", 1)
        form, link = rest.split(": ", 1)
        kind = link.split(" | ours ")
        pat = f"{kind[0].split('>')[0]} -> {kind[1].split('>')[0]}{'' if kind[0].split('>')[0] != kind[1].split('>')[0] else ' (head)'}"
        pattern.setdefault(pat, []).append(f"{sid} {form} [{link}]")
    rows.append(f"wrong links by pattern (gold role -> ours), {len(wrong)} words:")
    for pat, items in sorted(pattern.items(), key=lambda kv: -len(kv[1]))[:top]:
        rows.append(f"{len(items):>4}  {pat}:  " + "; ".join(items[:3]))
    return "\n".join(rows)


def run_gold_words(verses: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Sentence layer alone on the reference words (see eval/gold_words.py)."""
    import gold_words
    from mayur import anvaya, compounds, shabdabodha

    total: dict[str, Any] = {}
    n = errors = built = 0
    for v in verses:
        n += 1
        try:
            r, k = gold_words.reading_of(v)
            built += k
            r = anvaya.order(shabdabodha.resolve(compounds.annotate(r)))
            s = treebank.verse_to_sentence(v, "reference")
            total = add_counts(total, score_sentence(our_view(r), s, s["id"]))
        except Exception:
            errors += 1
            if errors <= 3:
                traceback.print_exc(file=sys.stderr)
    total["morphs_from_feats"] = built
    return {"sentences": n, "exceptions": errors, "failures": [], "counts": total}


def run(sentences: Iterable[dict[str, Any]], analyze: Callable[..., Any], limit: Optional[int] = None) -> dict[str, Any]:
    total: dict[str, Any] = {}
    n = errors = 0
    failures: list[dict[str, str]] = []
    for s in sentences:
        if limit is not None and n >= limit:
            break
        n += 1
        try:
            analysis = analyze(s["text"], verse_id=str(s["id"]))
            total = add_counts(total, score_sentence(our_view(analysis.readings[0]), s, str(s["id"])))
        except BaseException as exc:  # counted (a Rust panic in vidyut is a BaseException)
            if isinstance(exc, (KeyboardInterrupt, SystemExit)):
                raise
            errors += 1
            failures.append({"id": str(s["id"]), "error": f"{type(exc).__name__}: {exc}"[:200]})
            if errors <= 3:
                traceback.print_exc(file=sys.stderr)
    return {"sentences": n, "exceptions": errors, "failures": failures[:20], "counts": total}


# Two annotators on the same verses (no pipeline).

def agreement_view(s: dict[str, Any]) -> dict[str, Any]:
    words = [{"form": w["form"], "in_compound": w["compound_member"], "lemma": w["lemma"], "role": w["role"],
              "head": w["head_index"]} for w in s["words"]]
    comps = [{"members": sorted(c["members"]), "type": c["type"]} for c in s.get("compounds", [])]
    return {"words": words, "compounds": comps, "anvaya": list(s.get("anvaya", []))}


def agreement(a_sents: Sequence[dict], b_sents: Sequence[dict]) -> dict[str, Any]:
    """Score annotator A against B on the verses (same id) both cover."""
    b_by_id = {s["id"]: s for s in b_sents}
    total: dict[str, Any] = {}
    shared = 0
    for a in a_sents:
        b = b_by_id.get(a["id"])
        if b is not None:
            shared += 1
            total = add_counts(total, score_sentence(agreement_view(a), b))
    return {"sentences": shared, "exceptions": 0, "failures": [], "counts": total}


def load_sentences(args: argparse.Namespace) -> tuple[list[dict[str, Any]], str]:
    if args.claude:
        return treebank.read_claude(args.claude), f"reference {Path(args.claude).name}"
    if args.gold:
        return treebank.read_gold_roles(args.gold), f"human gold {Path(args.gold).name}"
    return list(_take(treebank.iter_source(args.source), args.limit)), f"gold {args.source}"


def _take(it: Iterable[dict], limit: Optional[int]) -> Iterable[dict]:
    for i, s in enumerate(it):
        if limit is not None and i >= limit:
            return
        yield s


def _wanted(verses: list[dict[str, Any]], spec: Optional[str]) -> list[dict[str, Any]]:
    if not spec:
        return verses
    lo, _, hi = spec.partition("-")
    return [v for v in verses if int(lo) <= int(v.get("number", 0)) <= int(hi or lo)]


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--source", choices=("ufal", "dcs", "vedic"), default="dcs")
    ap.add_argument("--claude", default=None)
    ap.add_argument("--gold", default=None)
    ap.add_argument("--agreement", nargs=2, metavar=("A", "B"), default=None)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--json", default=None)
    ap.add_argument("--gold-words", action="store_true", help="sentence layer alone on the reference words")
    ap.add_argument("--verses", default=None, help="verse numbers of a --claude file, e.g. 21-40")
    ap.add_argument("--matrix", action="store_true", help="confusion matrix and most frequent wrong links")
    args = ap.parse_args(argv)
    sys.path.insert(0, str(ROOT / "eval"))
    if args.agreement:
        a, b = (treebank.read_claude(p) for p in args.agreement)
        result, label = agreement(a, b), f"agreement {Path(args.agreement[0]).name} vs {Path(args.agreement[1]).name}"
    elif args.gold_words:
        verses = _wanted(json.loads(Path(args.claude).read_text(encoding="utf-8"))["verses"], args.verses)
        result = run_gold_words(verses[: args.limit])
        label = f"reference {Path(args.claude).name}, gold words ({result['counts'].get('morphs_from_feats', 0)}"\
                " Morphs built from feats)"
    else:
        from mayur.pipeline import analyze_verse

        sentences, label = load_sentences(args)
        if args.verses and args.claude:
            keep = {str(v["id"]) for v in _wanted(json.loads(Path(args.claude).read_text(encoding="utf-8"))["verses"],
                                                  args.verses)}
            sentences = [s for s in sentences if str(s["id"]) in keep]
        result = run(sentences, analyze_verse, args.limit)
    print(report(result["counts"], result["sentences"], result["exceptions"], label))
    if args.matrix:
        print(matrix(result["counts"]))
    if args.json:
        result["per_role"] = per_role(result["counts"].get("roles", {}))
        Path(args.json).write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
