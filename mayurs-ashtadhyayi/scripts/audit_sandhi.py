"""Audit forward sandhi (and the segmenter lattice) against DCS gold half-verses.

    python scripts/audit_sandhi.py [--limit 5000] [--lattice 1000]

For every gold half-verse: canon(text) must be one of canon(sandhi.rejoin(forms, flags)).
Failures are grouped by the first junction that fails; lines whose gold words do not occur in
the text even ignoring sandhi are counted as DCS anomalies, not rule gaps.
"""

from __future__ import annotations

import argparse
import glob
import itertools
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import dcs, sandhi  # noqa: E402
from mayur.lipi import from_varnas, varnas  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RAMAYANA = ROOT / "data/dcs/sanskrit/dcs/data/conllu/files/Rāmāyaṇa"


def gold_lines(limit: int, seed: int = 1):
    if hasattr(dcs, "gold_lines"):
        try:
            lines = list(dcs.gold_lines())
            random.Random(seed).shuffle(lines)
            return lines[:limit]
        except Exception:  # noqa: BLE001 - fall back to the Ramayana files
            pass
    out = []
    for path in sorted(glob.glob(str(RAMAYANA / "*.conllu"))):
        for s in dcs.iter_sentences(path):
            words = [(t["form"], t["compound_member"]) for t in s["tokens"] if t["form"]]
            if words:
                out.append({"compact": dcs.compact(s["text"]), "words": words})
    random.Random(seed).shuffle(out)
    return out[:limit]


def _words(line) -> list[tuple[str, bool]]:
    ws = line["words"]
    return [(w["form"], w["compound_member"]) if isinstance(w, dict) else tuple(w) for w in ws]


def _ok(forms, flags, target: str) -> bool:
    return target in {sandhi.canon(x) for x in sandhi.rejoin(forms, flags)}


_NASALS = {"ं", "ङ्", "ञ्", "ण्", "न्", "म्", "ँ"}


def _flat(text: str) -> str:
    flat = ("N" if v in _NASALS else v for v in varnas(sandhi.canon(text)))
    return "".join("न्" if v == "ण्" else v for v in flat)


def _core(form: str) -> tuple:
    """The part of a pada no sandhi rule touches: edges that rules may change are dropped."""
    v = varnas(form)
    if v and sandhi.is_vowel(v[0]):
        v = v[1:]
    if len(v) >= 2 and v[-1] in ("स्", "र्") and v[-2] == "अ":
        return v[:-2]
    if v and (sandhi.is_vowel(v[-1]) or v[-1] in sandhi.CONSONANTS):
        return v[:-1]
    return v


def _anomalous(forms, target: str) -> bool:
    """A gold word whose untouchable core is not in the text: a DCS reconstruction (मम for मे)."""
    t = _flat(target)
    return any(len(c) >= 2 and _flat(from_varnas(c)) not in t for c in map(_core, forms))


def _dcs_variant_ok(forms, flags, target: str) -> bool:
    """DCS artefacts: न for internal ण (8.4.2 undone), र्/स् finals guessed from the lemma."""
    fixed = [f.replace("ण", "न") for f in forms]
    t = target.replace("ण", "न")
    swapped = [f[:-2] + "स्" if f.endswith("र्") else (f[:-2] + "र्" if f.endswith("स्") else f) for f in fixed]
    if _ok(fixed, flags, t):
        return True
    return any(_ok(fixed[:i] + [swapped[i]] + fixed[i + 1:], flags, t) for i in range(len(forms)) if swapped[i] != fixed[i])


def _first_bad(forms, flags, target: str) -> int:
    tv = varnas(target)
    for m in range(1, len(forms)):
        outs = sandhi.rejoin(forms[: m + 1], flags[: m + 1])
        good = False
        for x in outs:
            xv = varnas(sandhi.canon(x))
            cut = max(len(xv) - 3, 0)
            if tv[:cut] == xv[:cut]:
                good = True
                break
        if not good:
            return m - 1
    return len(forms) - 1


def audit(lines) -> None:
    ok = anomalies = 0
    groups: dict[tuple, list] = defaultdict(list)
    for line in lines:
        words = _words(line)
        forms, flags = [w[0] for w in words], [w[1] for w in words]
        target = sandhi.canon(line["compact"])
        if _ok(forms, flags, target):
            ok += 1
            continue
        if _anomalous(forms, target) or _dcs_variant_ok(forms, flags, target):
            anomalies += 1
            continue
        m = _first_bad(forms, flags, target)
        left = varnas(forms[m])[-2:]
        right = varnas(forms[m + 1])[:1] if m + 1 < len(forms) else ("<end>",)
        key = (from_varnas(left), from_varnas(right) if right != ("<end>",) else "<end>", flags[m])
        groups[key].append(f"{' '.join(forms)}  =>  {line['compact']}")
    n = len(lines)
    clean = n - anomalies
    print(f"re-join pass: {ok}/{n}; non-anomalous {ok}/{clean} = {ok / max(clean, 1):.2%}; anomalies {anomalies}")
    for key, ex in sorted(groups.items(), key=lambda kv: -len(kv[1]))[:40]:
        print(f"{len(ex):5d}  ...{key[0]} + {key[1]}  compound={key[2]}")
        for e in ex[:3]:
            print("         ", e)


def lattice(lines, out_misses: Path) -> None:
    from mayur import lexicon, segmenter

    ok = lex = other = 0
    misses: Counter = Counter()
    fails = []
    for line in lines:
        words = _words(line)
        forms, flags = [w[0] for w in words], [w[1] for w in words]
        missing = [f for f, c in words if not (lexicon.is_stem(f) if c else lexicon.is_pada(f))]
        if segmenter.contains(line["compact"], forms, flags):
            ok += 1
        elif missing:
            lex += 1
            misses.update(missing)
        else:
            other += 1
            fails.append(f"{' '.join(forms)}  =>  {line['compact']}")
    print(f"lattice coverage {ok}/{len(lines)}; lexicon misses {lex}; other {other}")
    for f in fails[:30]:
        print("   ", f)
    out_misses.parent.mkdir(parents=True, exist_ok=True)
    out_misses.write_text("".join(f"{f}\t{c}\n" for f, c in misses.most_common(50)), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=5000)
    ap.add_argument("--lattice", type=int, default=0, help="also test lattice coverage on this many lines")
    args = ap.parse_args()
    lines = gold_lines(args.limit)
    audit(lines)
    if args.lattice:
        lattice(list(itertools.islice(lines, args.lattice)), ROOT / "data/derived/audit_lexicon_misses.txt")


if __name__ == "__main__":
    main()
