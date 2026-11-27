"""Everyday check set (eval/samples/everyday_120.json): split, lemma, grammar and roles end to end.

    python eval/eval_everyday.py [--show] [--group a|b|c] [--ids a01,b07] [--json out.json]

120 lines in three groups: (a) plain prose of rising difficulty, (b) well-known verse lines and
sayings with full sandhi, (c) sandhi-heavy lines (long compounds, avagraha present and absent, the
same text with and without spaces). Per group and overall it reports: chosen split right; right
split among the kept readings; every lemma right; every grammar tag right; every listed role and
head right; status verified. Lemma, grammar and roles are read off the chosen reading and count as
wrong when its split is wrong. The set was written by an LLM and is not human-verified.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from mayur import lipi, sandhi  # noqa: E402
from mayur.model import Morph, Reading, VerseAnalysis  # noqa: E402

SAMPLE = ROOT / "eval" / "samples" / "everyday_120.json"
# स / एष before a consonant (6.1.132) stand without their ending; the pada is सः / एषः
_SU_LOPA = {"स": "सस्", "एष": "एषस्"}
NONFINITE = frozenset({"क्त्वा", "ल्यप्", "तुमुन्"})
ACTIVE = "कर्तरि"
GENDERS = frozenset({"पुंलिङ्ग", "स्त्रीलिङ्ग", "नपुंसकलिङ्ग"})
CHECKS = ("split", "kept", "lemma", "grammar", "roles", "verified")


# ---- the chosen reading as padas -------------------------------------------------------------

def groups(reading: Reading) -> list[list[int]]:
    """Word indices of each pada of the reading (a compound's members, then its final word)."""
    out: list[list[int]] = []
    group: list[int] = []
    for i, w in enumerate(reading.words):
        group.append(i)
        if not w.in_compound:
            out.append(group)
            group = []
    if group:
        out.append(group)
    return out


def _members(gold: str) -> list[str]:
    return gold.split("-")


def same_pada(forms: list[str], gold: str) -> bool:
    """Our pada (its members' forms) is the gold pada: equal as written, or re-joining to it by sandhi."""
    want = _members(gold)
    if len(forms) == 1 and len(want) == 1:
        ours = _SU_LOPA.get(forms[0], forms[0])
        return sandhi.canon(lipi.pausa(ours)) == sandhi.canon(lipi.pausa(want[0]))
    if [sandhi.canon(f) for f in forms[:-1]] == [sandhi.canon(m) for m in want[:-1]] \
            and sandhi.canon(lipi.pausa(forms[-1])) == sandhi.canon(lipi.pausa(want[-1])):
        return True
    flags_gold = [True] * (len(want) - 1)
    flags_ours = [True] * (len(forms) - 1)
    return any(sandhi.rejoin_matching(forms, flags_ours, surface) is not None
               for surface in sandhi.rejoin(want, flags_gold))


def split_right(reading: Reading, padas: list[str]) -> bool:
    gs = groups(reading)
    return len(gs) == len(padas) and all(
        same_pada([reading.words[i].form for i in g], p) for g, p in zip(gs, padas))


# ---- lemma and grammar -----------------------------------------------------------------------

def _norm(lemma: str) -> str:
    # त्त्र / त्र: optional doubling (8.4.47) in dictionary spellings such as छात्त्र
    return sandhi.canon(lemma).replace("त्त्र", "त्र")


def _lemma_one(cands: set[str], want: str, feminine: bool) -> bool:
    w = _norm(want)
    if w in cands:
        return True
    # a feminine adjective may be cited by its masculine stem or its feminine stem in -आ (4.1.4)
    return feminine and any(c == w + "ा" or w == c + "ा" for c in cands)


def _candidates(m: Morph | None) -> set[str]:
    if m is None:
        return set()
    return {_norm(x) for x in (m.lemma, m.stem) if x}


def _listed_compound(cands: set[str], want: list[str]) -> bool:
    """A compound the dictionary lists as one stem is right when the gold members re-join to it."""
    joined = sandhi.rejoin(want, [True] * (len(want) - 1))
    return bool(cands & {_norm(s) for s in joined})


def lemma_right(reading: Reading, group: list[int], gold: str, gold_grammar: str) -> bool:
    """Every member's lemma (or kṛdanta stem) equals one of the gold alternatives."""
    morphs = [reading.words[i].morph for i in group]
    feminine = "स्त्रीलिङ्ग" in gold_grammar
    for alt in (a.strip() for a in gold.split("|")):
        want = _members(alt)
        if len(morphs) == 1 and len(want) > 1 and _listed_compound(_candidates(morphs[0]), want):
            return True
        if len(want) == len(morphs) and all(
                _lemma_one(_candidates(m), w, feminine and k == len(want) - 1)
                for k, (m, w) in enumerate(zip(morphs, want))):
            return True
    return False


def morph_terms(m: Morph | None) -> frozenset[str]:
    """The grammar of one analysis as the set of terms the check set writes."""
    if m is None:
        return frozenset()
    if m.kind == "avyaya":
        return frozenset({m.krt}) if m.krt in NONFINITE else frozenset({"अव्यय"})
    if m.kind == "tinanta":
        terms = {m.lakara, m.purusha, m.vacana}
        if m.prayoga and m.prayoga != ACTIVE:
            terms.add(m.prayoga)
        return frozenset(t for t in terms if t)
    return frozenset(t for t in (m.linga, m.vibhakti, m.vacana) if t)


def grammar_right(m: Morph | None, gold: str) -> bool:
    """Our analysis carries exactly the gold terms (one of the alternatives); a gold tag without a
    gender (अस्मद्, युष्मद्, पञ्चन् ...) leaves our gender unscored."""
    ours = morph_terms(m)
    for alt in (a.strip() for a in gold.split("|")):
        want = frozenset(alt.split())
        have = ours if want & GENDERS else ours - GENDERS
        if have == want:
            return True
    return False


# ---- roles -----------------------------------------------------------------------------------

def pada_map(reading: Reading, padas: list[str], aligned: bool) -> dict[int, int]:
    """Gold pada index -> our pada index: by position when the split is right, else the same
    occurrence of the same written pada."""
    gs = groups(reading)
    if aligned:
        return {i: i for i in range(len(padas))}
    out: dict[int, int] = {}
    for i, p in enumerate(padas):
        occ = padas[:i].count(p)
        hits = [k for k, g in enumerate(gs) if same_pada([reading.words[j].form for j in g], p)]
        if len(hits) > occ:
            out[i] = hits[occ]
    return out


def role_problems(reading: Reading, item: dict, aligned: bool) -> list[str]:
    """The listed roles that the chosen reading gets wrong (empty when all are right)."""
    gs = groups(reading)
    pada_of = {j: k for k, g in enumerate(gs) for j in g}
    mapping = pada_map(reading, item["padas"], aligned)
    problems = []
    for r in item["roles"]:
        k = mapping.get(r["at"])
        if k is None:
            problems.append(f"{r['pada']}: not a pada of the chosen reading")
            continue
        w = reading.words[gs[k][-1]]
        head = None if w.head is None else pada_of.get(w.head)
        want = None if r["head_at"] is None else mapping.get(r["head_at"], -1)
        if w.role != r["role"] or head != want:
            got = "-" if head is None else "+".join(lipi.pausa(reading.words[j].form) for j in gs[head]) + f"@{head}"
            expected = f"{r['head']}@{r['head_at']}" if r["head"] else "-"
            problems.append(f"{r['pada']}@{r['at']}: expected {r['role']}>{expected}, got {w.role or '∅'}>{got}")
    return problems


# ---- one item --------------------------------------------------------------------------------

@dataclass
class Result:
    id: str
    group: str
    checks: dict[str, bool] = field(default_factory=dict)
    problems: list[str] = field(default_factory=list)
    ours: str = ""
    english: str = ""


def listed(reading: Reading, group: list[int], gold: dict) -> bool:
    """Some analysis the lexicon gave the pada's final word has the gold grammar and final lemma."""
    w = reading.words[group[-1]]
    finals = {_members(a.strip())[-1] for a in gold["lemma"].split("|")}
    feminine = "स्त्रीलिङ्ग" in gold["grammar"]
    return any(grammar_right(a, gold["grammar"]) and any(_lemma_one(_candidates(a), f, feminine) for f in finals)
               for a in w.analyses)


def word_problems(reading: Reading, item: dict) -> tuple[list[str], list[str]]:
    """(lemma problems, grammar problems) of an item whose split is right; each says whether the
    lexicon listed the right analysis (a choice) or not (a gap)."""
    lemmas, grams = [], []
    for g, gold in zip(groups(reading), item["words"]):
        m = reading.words[g[-1]].morph
        why = "listed, not chosen" if listed(reading, g, gold) else "not listed"
        if not lemma_right(reading, g, gold["lemma"], gold["grammar"]):
            got = "-".join((reading.words[i].morph.lemma if reading.words[i].morph else "∅") for i in g)
            lemmas.append(f"{gold['pada']}: lemma {got}, expected {gold['lemma']} ({why})")
        if not grammar_right(m, gold["grammar"]):
            grams.append(f"{gold['pada']}: grammar {' '.join(sorted(morph_terms(m))) or '∅'}, "
                         f"expected {gold['grammar']} ({why})")
    return lemmas, grams


def shown(reading: Reading) -> str:
    return " ".join("-".join(lipi.pausa(reading.words[i].form) if i == g[-1] else reading.words[i].form for i in g)
                    for g in groups(reading))


def score(analysis: VerseAnalysis, item: dict) -> Result:
    """All checks of one item against the pipeline's analysis of its text."""
    res = Result(id=item["id"], group=item["group"])
    if not analysis.readings:
        res.checks = {c: False for c in CHECKS}
        res.problems = ["no reading"]
        return res
    reading = analysis.readings[0]
    ok = split_right(reading, item["padas"])
    lemmas, grams = word_problems(reading, item) if ok else (["split wrong"], ["split wrong"])
    roles = role_problems(reading, item, ok)
    res.checks = {"split": ok, "kept": any(split_right(r, item["padas"]) for r in analysis.readings),
                  "lemma": ok and not lemmas, "grammar": ok and not grams,
                  "roles": ok and not roles, "verified": analysis.status == "verified"}
    res.problems = ([] if ok else ["split wrong"]) + (lemmas + grams if ok else []) + roles
    res.ours = shown(reading)
    res.english = reading.reworded or reading.translation
    return res


# ---- report ----------------------------------------------------------------------------------

def tally(results: list[Result]) -> dict[str, tuple[int, int]]:
    """check -> (passed, out of); the roles check counts only items that list roles."""
    out = {}
    for c in CHECKS:
        pool = [r for r in results if c != "roles" or r.checks.get("has_roles", True)]
        out[c] = (sum(r.checks[c] for r in pool), len(pool))
    return out


def report_line(name: str, results: list[Result]) -> str:
    t = tally(results)
    return f"{name:8} n={len(results):3}  " + "  ".join(f"{c} {p}/{n}" for c, (p, n) in t.items())


def show(item: dict, res: Result) -> None:
    print(f"✗ {item['id']} {item['text']}\n    ours: {res.ours}\n    want: {' '.join(item['padas'])}")
    for p in res.problems:
        print(f"    {p}")
    print(f"    en:   {res.english}\n    ref:  {item['english']}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--show", action="store_true", help="print every failing item, ours against expected")
    ap.add_argument("--group", choices=("a", "b", "c"), help="only this group")
    ap.add_argument("--ids", help="only these comma-separated item ids")
    ap.add_argument("--json", help="write per-item results to this file")
    args = ap.parse_args(argv)
    from mayur.pipeline import analyze_verse
    items = json.loads(SAMPLE.read_text(encoding="utf-8"))["items"]
    wanted = set(args.ids.split(",")) if args.ids else None
    items = [x for x in items if (not args.group or x["group"] == args.group) and (not wanted or x["id"] in wanted)]
    results = []
    for item in items:
        res = score(analyze_verse(item["text"]), item)
        res.checks["has_roles"] = bool(item["roles"])
        results.append(res)
        if args.show and not all(res.checks[c] for c in CHECKS if c != "roles" or item["roles"]):
            show(item, res)
    for g in "abc":
        part = [r for r in results if r.group == g]
        if part:
            print(report_line(f"group {g}", part))
    print(report_line("overall", results))
    if args.json:
        Path(args.json).write_text(json.dumps([r.__dict__ for r in results], ensure_ascii=False, indent=1),
                                   encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
