"""Score the English layer against the reference sentences written by the Claude annotator.

    python eval/eval_english.py --file ramayana_bala1_001_040_A.json --verses 21-40 [--show] [--mode gold|pipeline|both]
    (files are in eval/review/claude/; never use Ramayana verses 1-20 or the *_B.json files)

Mode ``gold``: the Reading is built from the reference's own words, with the reference roles, heads,
compounds and prose order, so sentence structure is right by construction and only gloss -> artha ->
translate.render -> fluent.rewrite is measured. Mode ``pipeline``: the whole pipeline on the raw text.
Proxy metrics (local, no downloads): chrF (character 1-6-grams, beta 2) and content-word F1.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from dataclasses import replace
from pathlib import Path
from typing import Any, Iterable, Sequence

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "eval"))

REVIEW = ROOT / "eval" / "review" / "claude"
STOP = frozenset("""a an the of to in on at by with and or but for from as that which who whom whose is are was were be
been being am has have had does did do will shall it its he him his she her they them their we us our you your i me my
this these those then there so not no into upon after before when while until over under also o if than""".split())


def chrf(hyp: str, ref: str, n: int = 6, beta: float = 2.0) -> float:
    """Character n-gram F-score (chrF), 0..100, whitespace ignored."""
    h, r = "".join(hyp.lower().split()), "".join(ref.lower().split())
    ps, rs = [], []
    for k in range(1, n + 1):
        hg = Counter(h[i:i + k] for i in range(len(h) - k + 1))
        rg = Counter(r[i:i + k] for i in range(len(r) - k + 1))
        if not hg or not rg:
            continue
        hit = sum((hg & rg).values())
        ps.append(hit / sum(hg.values()))
        rs.append(hit / sum(rg.values()))
    if not ps:
        return 0.0
    p, rc = sum(ps) / len(ps), sum(rs) / len(rs)
    return 0.0 if p + rc == 0 else 100 * (1 + beta ** 2) * p * rc / (beta ** 2 * p + rc)


def _content(text: str) -> list[str]:
    from mayur.fluent_checks import stem, tokens
    return [stem(t) for t in tokens(text) if t not in STOP]


def content_f1(hyp: str, ref: str) -> float:
    """F1 of the bags of stemmed content words, 0..100."""
    h, r = Counter(_content(hyp)), Counter(_content(ref))
    hit = sum((h & r).values())
    if not hit:
        return 0.0
    p, rc = hit / sum(h.values()), hit / sum(r.values())
    return 100 * 2 * p * rc / (p + rc)


def parse_range(spec: str) -> set[int]:
    out: set[int] = set()
    for part in spec.split(","):
        lo, _, hi = part.partition("-")
        out |= set(range(int(lo), int(hi or lo) + 1))
    return out


def gold_reading(verse: dict[str, Any]):
    """Reading of the reference words with reference roles, heads, compounds and prose order, then the
    English layers: gloss -> artha -> translate.render -> fluent.rewrite. Returns (literal, fluent)."""
    import gold_words
    from mayur import anvaya as _anvaya, artha, fluent, gloss, translate
    from mayur.model import Compound

    reading, _ = gold_words.reading_of(verse)
    ws = sorted(verse["words"], key=lambda x: x["index"])
    words = [replace(w, role=g.get("role", ""), head=g.get("head")) for w, g in zip(reading.words, ws)]
    comps = []
    for k, c in enumerate(verse.get("compounds", [])):
        comps.append(Compound(id=k, members=list(c["members"]), samasa=c.get("type", ""), vigraha=c.get("vigraha", "")))
        for m in c["members"]:
            words[m] = replace(words[m], compound=k)
    reading = replace(reading, words=words, compounds=comps, anvaya=list(verse.get("anvaya", [])))
    glossed = []
    for i, w in enumerate(reading.words):
        text, source = gloss.lookup_in_context(reading, i)
        glossed.append(replace(reading.words[i], gloss=text, gloss_source=source))
    reading = artha.annotate(replace(reading, words=glossed))
    if not reading.anvaya:
        reading = _anvaya.order(reading)
    literal = translate.render(reading)
    return literal, fluent.rewrite(literal)[0]


def pipeline_reading(verse: dict[str, Any]):
    from mayur import pipeline
    r = pipeline.analyze_verse(verse["text"], max_readings=1).readings[0]
    return r, r


def score(verses: Sequence[dict[str, Any]], mode: str, show: bool) -> dict[str, float]:
    fn = gold_reading if mode == "gold" else pipeline_reading
    sums = {"chrF literal": 0.0, "chrF fluent": 0.0, "F1 literal": 0.0, "F1 fluent": 0.0}
    n = errors = 0
    for v in verses:
        try:
            lit, flu = fn(v)
        except Exception as exc:  # counted, never hidden
            errors += 1
            print(f"  ! {v['key']}: {type(exc).__name__}: {exc}", file=sys.stderr)
            continue
        ref, fluent_text = v.get("english", ""), flu.reworded or lit.translation
        n += 1
        sums["chrF literal"] += chrf(lit.translation, ref)
        sums["chrF fluent"] += chrf(fluent_text, ref)
        sums["F1 literal"] += content_f1(lit.translation, ref)
        sums["F1 fluent"] += content_f1(fluent_text, ref)
        if show:
            print(f"[{v['key']}] REF   {ref}\n      LIT   {lit.translation}\n      FLUENT {fluent_text}"
                  + ("" if flu.reworded else f"   ({flu.reworded_note})"))
    out = {k: round(s / max(n, 1), 1) for k, s in sums.items()}
    out["n"], out["errors"] = n, errors
    return out


def main(argv: Iterable[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--verses", default="")
    ap.add_argument("--mode", choices=["gold", "pipeline", "both"], default="both")
    ap.add_argument("--show", action="store_true")
    a = ap.parse_args(list(argv) if argv is not None else None)
    if a.file.endswith("_B.json"):
        ap.error("the *_B.json files are held out")
    data = json.loads((REVIEW / a.file).read_text(encoding="utf-8"))
    want = parse_range(a.verses) if a.verses else None
    if a.file.startswith("ramayana_bala1_001") and (want is None or min(want) < 21):
        ap.error("Ramayana verses 1-20 are held out: pass --verses 21-40")
    verses = [v for v in data["verses"] if want is None or v["key"] in want]
    for mode in (["gold", "pipeline"] if a.mode == "both" else [a.mode]):
        print(f"== {a.file} {a.verses or 'all'} mode={mode}")
        print(score(verses, mode, a.show))
    return 0


if __name__ == "__main__":
    sys.exit(main())
