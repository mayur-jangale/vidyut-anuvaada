"""Evaluate compound grouping and compound types.

    python eval/eval_compounds.py --claude eval/review/claude/<file>.json [--json out.json]
    python eval/eval_compounds.py --gold eval/review/gold_roles.json          (human corrections)
    python eval/eval_compounds.py --source ufal dcs vedic [--max-compounds 500]   (UD proxy, see below)
    python eval/eval_compounds.py --agreement fileA.json fileB.json
    python eval/eval_compounds.py --claude <file> --gold-words [--verses 21-40] [--wrong-groups]

``--gold-words`` isolates the compound layer: the Reading is built from the reference file's own words
(gold split, lemma, feats, compound_member flags; the shared helper eval/gold_words.py, also used by
eval/eval_roles.py) and only compounds.annotate runs, so type accuracy excludes split errors.
``--verses`` keeps only those verse numbers of a --claude file (normal mode too).
``--wrong-groups`` lists the most frequent kinds of our compounds whose members match no gold compound.

NO open compound-TYPE dataset could be fetched (scripts/fetch_gold_external.py lists why: the Hyderabad
samasa data forbids redistribution, SaCTI has no licence). The only machine-readable gold is therefore
  * reference files / human corrections (types written by annotators), and
  * a WEAK PROXY from the UD treebanks: a compound unit (members flagged Compound=Yes / Case=Cpd) whose
    member tokens are attached with conj or compound:coord is a द्वन्द्व; every other unit has NO proxy
    type (UD does not say तत्पुरुष/कर्मधारय/बहुव्रीहि) and is only used for grouping.
Grouping: a gold compound counts as found if one of our compounds has exactly its member words (after
alignment). Type is scored only on found compounds that carry a gold type, strictly and by family
(तत्पुरुष family = तत्पुरुष कर्मधारय नञ्-तत्पुरुष उपपद-तत्पुरुष; बहुव्रीहि family = बहुव्रीहि नञ्-बहुव्रीहि).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Optional, Sequence

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from mayur import treebank  # noqa: E402


def _load(name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, ROOT / "eval" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


er = _load("eval_roles")

# Label sets, explicit. Ours: mayur/compounds.py constants (अज्ञात = could not decide).
OUR_TYPES = ("तत्पुरुष", "कर्मधारय", "द्वन्द्व", "बहुव्रीहि", "अव्ययीभाव", "नञ्-तत्पुरुष", "नञ्-बहुव्रीहि",
             "उपपद-तत्पुरुष", "द्विगु", "अज्ञात")
GOLD_TYPES = OUR_TYPES[:-1]
FAMILY = {"तत्पुरुष": "तत्पुरुष", "कर्मधारय": "तत्पुरुष", "नञ्-तत्पुरुष": "तत्पुरुष", "उपपद-तत्पुरुष": "तत्पुरुष",
          "द्विगु": "तत्पुरुष",
          "बहुव्रीहि": "बहुव्रीहि", "नञ्-बहुव्रीहि": "बहुव्रीहि", "द्वन्द्व": "द्वन्द्व", "अव्ययीभाव": "अव्ययीभाव"}
COORD_RELATIONS = {"conj", "compound:coord"}


def family(label: str) -> str:
    return FAMILY.get(label, label)


def proxy_compounds(sentence: dict[str, Any]) -> list[dict[str, Any]]:
    """Compound units of a UD sentence: members (indices incl. the final one) and the proxy type."""
    units: dict[int, list[int]] = {}
    for i, w in enumerate(sentence["words"]):
        if w["compound_member"] and w["role"] == treebank.MEMBER:
            units.setdefault(w["head_index"], []).append(i)
    out = []
    for final, members in sorted(units.items()):
        coord = any(sentence["words"][i]["relation"] in COORD_RELATIONS for i in members)
        out.append({"members": sorted(members + [final]), "type": "द्वन्द्व" if coord else "", "vigraha": ""})
    return out


def score_compounds(ours: dict[str, Any], gold: dict[str, Any]) -> dict[str, Any]:
    """Counts of one sentence; ``ours`` from ``eval_roles.our_view``, ``gold`` a sentence with "compounds"."""
    mapping = er.align(ours["words"], gold["words"])
    gold_sets = {frozenset(c["members"]): c for c in gold.get("compounds", [])}
    c: dict[str, Any] = {"gold_compounds": len(gold_sets), "our_compounds": len(ours["compounds"]), "found": 0,
                         "our_correct_group": 0, "typed": 0, "type_ok": 0, "family_ok": 0, "by_type": {}, "confusion": {}}
    c["wrong_groups"] = {}
    for oc in ours["compounds"]:
        mapped = {mapping[i] for i in oc["members"] if i in mapping}
        if len(mapped) != len(oc["members"]) or frozenset(mapped) not in gold_sets:
            kind = wrong_group_kind(mapped, len(oc["members"]), list(gold_sets), gold["words"])
            forms = "-".join(ours["words"][i]["form"] for i in oc["members"])
            c["wrong_groups"][f"{kind} || {gold.get('id', '')}: {forms}"] = 1
            continue
        gc = gold_sets[frozenset(mapped)]
        c["found"] += 1
        c["our_correct_group"] += 1
        if gc["type"]:
            t = c["by_type"].setdefault(gc["type"], {"n": 0, "ok": 0, "family_ok": 0})
            t["n"] += 1
            t["ok"] += oc["type"] == gc["type"]
            t["family_ok"] += family(oc["type"]) == family(gc["type"])
            c["typed"] += 1
            c["type_ok"] += oc["type"] == gc["type"]
            c["family_ok"] += family(oc["type"]) == family(gc["type"])
            key = f"{gc['type']} -> {oc['type']}"
            c["confusion"][key] = c["confusion"].get(key, 0) + 1
    return c


def wrong_group_kind(mapped: set[int], n: int, gold_sets: list[frozenset], gold_words: Sequence[dict]) -> str:
    """Why one of our compounds matches no gold compound (a short Devanagari-free label)."""
    if len(mapped) != n:
        return "unaligned member"
    over = [g for g in gold_sets if g & mapped]
    if not over:
        flagged = sum(bool(gold_words[i].get("compound_member")) for i in mapped)
        return "no gold compound (gold: separate words)" if not flagged else "gold flags members but lists no compound"
    if len(over) > 1:
        return "spans several gold compounds"
    g = over[0]
    if mapped < g:
        return "part of a longer gold compound"
    if mapped > g:
        return "longer than the gold compound"
    return "overlaps a gold compound"


def wrong_group_table(total: dict[str, Any], top: int = 30) -> str:
    kinds = Counter(k.split(" || ")[0] for k in total.get("wrong_groups", {}))
    rows = [f"wrong groups: {sum(kinds.values())}"]
    for kind, n in kinds.most_common(top):
        ex = [k.split(" || ")[1] for k in total["wrong_groups"] if k.startswith(kind + " ||")][:4]
        rows.append(f"{n:>4}  {kind}:  " + "; ".join(ex))
    return "\n".join(rows)


def run_gold_words(verses: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """The compound layer alone on the reference's own words (see eval/gold_words.py)."""
    sys.path.insert(0, str(ROOT / "eval"))
    import gold_words
    from mayur import compounds

    total: dict[str, Any] = {}
    n = errors = built = 0
    for v in verses:
        n += 1
        try:
            r, k = gold_words.reading_of(v)
            built += k
            s = treebank.verse_to_sentence(v, "reference")
            total = add(total, score_compounds(er.our_view(compounds.annotate(r)), s))
        except Exception:  # counted, like pipeline exceptions
            errors += 1
    total["morphs_from_feats"] = built
    return {"sentences": n, "exceptions": errors, "counts": total}


def wanted(verses: list[dict[str, Any]], spec: Optional[str]) -> list[dict[str, Any]]:
    if not spec:
        return verses
    lo, _, hi = spec.partition("-")
    return [v for v in verses if int(lo) <= int(v.get("number", 0)) <= int(hi or lo)]


def add(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    out = dict(a)
    for k, v in b.items():
        if isinstance(v, dict):
            cur = {kk: (dict(vv) if isinstance(vv, dict) else vv) for kk, vv in out.get(k, {}).items()}
            for kk, vv in v.items():
                if isinstance(vv, dict):
                    slot = cur.setdefault(kk, {x: 0 for x in vv})
                    for x, n in vv.items():
                        slot[x] += n
                else:
                    cur[kk] = cur.get(kk, 0) + vv
            out[k] = cur
        else:
            out[k] = out.get(k, 0) + v
    return out


def report(total: dict[str, Any], sentences: int, errors: int, label: str) -> str:
    f = er.frac
    lines = [f"{label}: {sentences} sentences, {errors} pipeline exceptions",
             f"gold compounds found with exactly the same members (recall): {f(total.get('found', 0), total.get('gold_compounds', 0))}",
             f"our compounds with a correct grouping (precision): {f(total.get('our_correct_group', 0), total.get('our_compounds', 0))}",
             f"type accuracy on found, typed compounds: strict {f(total.get('type_ok', 0), total.get('typed', 0))};"
             f" by family {f(total.get('family_ok', 0), total.get('typed', 0))}"]
    for t, d in sorted(total.get("by_type", {}).items(), key=lambda kv: -kv[1]["n"]):
        lines.append(f"  gold {t}: strict {f(d['ok'], d['n'])}; family {f(d['family_ok'], d['n'])}")
    for k, n in sorted(total.get("confusion", {}).items(), key=lambda kv: -kv[1])[:30]:
        lines.append(f"  {k}: {n}")
    return "\n".join(lines)


def run(sentences: Iterable[dict[str, Any]], analyze: Any, max_compounds: Optional[int] = None) -> dict[str, Any]:
    total: dict[str, Any] = {}
    n = errors = 0
    for s in sentences:
        if max_compounds is not None and total.get("gold_compounds", 0) >= max_compounds:
            break
        n += 1
        try:
            reading = analyze(s["text"], verse_id=str(s["id"])).readings[0]
            total = add(total, score_compounds(er.our_view(reading), s))
        except BaseException as exc:  # a Rust panic in vidyut is a BaseException
            if isinstance(exc, (KeyboardInterrupt, SystemExit)):
                raise
            errors += 1
    return {"sentences": n, "exceptions": errors, "counts": total}


def agreement(a_sents: Sequence[dict], b_sents: Sequence[dict]) -> dict[str, Any]:
    b_by_id = {s["id"]: s for s in b_sents}
    total: dict[str, Any] = {}
    shared = 0
    for a in a_sents:
        b = b_by_id.get(a["id"])
        if b is not None:
            shared += 1
            total = add(total, score_compounds(er.agreement_view(a), b))
    return {"sentences": shared, "exceptions": 0, "counts": total}


def ud_sentences(names: Sequence[str]) -> Iterable[dict[str, Any]]:
    """UD sentences that contain a proxy-typed compound, each with its proxy compounds attached."""
    for name in names:
        for s in treebank.iter_source(name):
            comps = proxy_compounds(s)
            if any(c["type"] for c in comps):
                yield dict(s, compounds=comps)


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--source", choices=("ufal", "dcs", "vedic"), nargs="+", default=None)
    ap.add_argument("--claude", default=None)
    ap.add_argument("--gold", default=None)
    ap.add_argument("--agreement", nargs=2, metavar=("A", "B"), default=None)
    ap.add_argument("--max-compounds", type=int, default=500)
    ap.add_argument("--json", default=None)
    ap.add_argument("--gold-words", action="store_true", help="compound layer alone on the reference words")
    ap.add_argument("--verses", default=None, help="verse numbers of a --claude file, e.g. 21-40")
    ap.add_argument("--wrong-groups", action="store_true", help="most frequent kinds of wrong groups")
    args = ap.parse_args(argv)
    if args.gold_words:
        verses = wanted(json.loads(Path(args.claude).read_text(encoding="utf-8"))["verses"], args.verses)
        result = run_gold_words(verses)
        label = f"reference {Path(args.claude).name}, gold words ({result['counts'].get('morphs_from_feats', 0)}"\
                " Morphs built from feats)"
    elif args.agreement:
        a, b = (treebank.read_claude(p) for p in args.agreement)
        result, label = agreement(a, b), f"agreement {Path(args.agreement[0]).name} vs {Path(args.agreement[1]).name}"
    else:
        from mayur.pipeline import analyze_verse

        if args.claude:
            doc = json.loads(Path(args.claude).read_text(encoding="utf-8"))
            keep = {str(v.get("id", v.get("number", ""))) for v in wanted(doc["verses"], args.verses)}
            sents = [s for s in treebank.read_claude(args.claude) if s["id"] in keep]
            label = f"reference {Path(args.claude).name}"
        elif args.gold:
            sents, label = treebank.read_gold_roles(args.gold), f"human gold {Path(args.gold).name}"
        else:
            src = args.source or ["dcs", "ufal"]
            sents, label = ud_sentences(src), f"UD proxy ({'+'.join(src)}: only द्वन्द्व units are typed)"
        result = run(sents, analyze_verse, args.max_compounds)
    print(report(result["counts"], result["sentences"], result["exceptions"], label))
    if args.wrong_groups:
        print(wrong_group_table(result["counts"]))
    if args.json:
        Path(args.json).write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
