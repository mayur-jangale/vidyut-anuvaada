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
    """A seeded sample of train-split gold lines across all texts (Ramayana files as fallback)."""
    files = dcs.split_files("train") if hasattr(dcs, "split_files") else []
    if not files:
        files = sorted(glob.glob(str(RAMAYANA / "*.conllu")))
    files = list(files)
    random.Random(seed).shuffle(files)
    out = []
    for entry in files:
        if len(out) >= 4 * limit:
            break
        path = entry["file"] if isinstance(entry, dict) else entry
        book = Path(path).parent.name
        for line in dcs.gold_lines([entry]):
            out.append({**line, "book": book})
    random.Random(seed).shuffle(out)
    return out[:limit]


def _words(line) -> list[tuple[str, bool]]:
    ws = line["words"]
    return [(w["form"], w["compound_member"]) if isinstance(w, dict) else tuple(w) for w in ws]


def _ok(forms, flags, target: str) -> bool:
    return sandhi.rejoin_matching(forms, flags, target) is not None


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


# DCS restores a different form of the same word than the text has (ते for तव, मम for मे ...).
_DCS_SUBST = (("ते", "तव"), ("मम", "मे"), ("मे", "मम"), ("नस्", "अस्माकम्"), ("वस्", "युष्माकम्"),
              ("त्वा", "त्वाम्"), ("मा", "माम्"), ("राज्ञ्", "राजन्"), ("तव", "ते"))


def _dcs_variant_ok(forms, flags, target: str) -> bool:
    """DCS artefacts: न for internal ण (8.4.2 undone), र्/स् finals guessed from the lemma."""
    fixed = [f.replace("ण", "न") for f in forms]
    t = target.replace("ण", "न")
    swapped = [f[:-2] + "स्" if f.endswith("र्") else (f[:-2] + "र्" if f.endswith("स्") else f) for f in fixed]
    if _ok(fixed, flags, t):
        return True
    for a, b in _DCS_SUBST:
        if a in fixed and _ok([b if f == a else (f[:-3] + "जन्" if f.endswith("ज्ञ्") else f) for f in fixed], flags, t):
            return True
    return any(_ok(fixed[:i] + [swapped[i]] + fixed[i + 1:], flags, t) for i in range(len(forms)) if swapped[i] != fixed[i])


def _first_bad(forms, flags, target: str) -> int:
    """Index of the left word of the first junction after which no re-join agrees with the text."""
    tv = sandhi.canon_varnas(target)
    states = {((), varnas(forms[0]), forms[0])}
    for i in range(1, len(forms)):
        nv = varnas(forms[i])
        keep = max(len(nv) - 1, 1)
        nxt = set()
        for done, cur, word in states:
            for seq, _ in sandhi._outcomes_v(cur, nv, word, bool(flags[i - 1])):
                nd = done + seq[:-keep]
                cv = sandhi.canon_varnas(sandhi.from_varnas(nd)) if nd else ()
                cut = max(len(cv) - 1, 0)
                if tv[:cut] == cv[:cut]:
                    nxt.add((nd, seq[-keep:], forms[i]))
        if not nxt:
            return i - 1
        states = nxt
    return len(forms) - 1


def audit(lines) -> None:
    ok = anomalies = 0
    groups: dict[tuple, list] = defaultdict(list)
    per_book: dict[str, list] = defaultdict(lambda: [0, 0])
    for line in lines:
        book = line.get("book", "")
        words = _words(line)
        forms, flags = [w[0] for w in words], [w[1] for w in words]
        target = sandhi.canon(line["compact"])
        if _ok(forms, flags, target):
            ok += 1
            line["rejoins"] = True
            per_book[book][0] += 1
            per_book[book][1] += 1
            continue
        if _anomalous(forms, target) or _dcs_variant_ok(forms, flags, target):
            anomalies += 1
            line["anomaly"] = True
            continue
        per_book[book][1] += 1
        m = _first_bad(forms, flags, target)
        left = varnas(forms[m])[-2:]
        right = varnas(forms[m + 1])[:1] if m + 1 < len(forms) else ("<end>",)
        key = (from_varnas(left), from_varnas(right) if right != ("<end>",) else "<end>", flags[m])
        groups[key].append(f"{' '.join(forms)}  =>  {line['compact']}")
    n = len(lines)
    clean = n - anomalies
    print(f"re-join pass: {ok}/{n}; non-anomalous {ok}/{clean} = {ok / max(clean, 1):.2%}; anomalies {anomalies}")
    for book, (good, tot) in sorted(per_book.items(), key=lambda kv: kv[1][0] / max(kv[1][1], 1)):
        print(f"   {book}: {good}/{tot}")
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
        lattice([ln for ln in lines if ln.get("rejoins")][: args.lattice], ROOT / "data/derived/audit_lexicon_misses.txt")


if __name__ == "__main__":
    main()
