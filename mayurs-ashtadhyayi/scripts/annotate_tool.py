"""Reference annotation of roles, compounds, anvaya and English on top of the gold word split.

    python scripts/annotate_tool.py skeleton --source ramayana --verses 1-40 --out eval/review/claude/x.json
    python scripts/annotate_tool.py skeleton --source eval/samples/dev300b.json --verses 1-60 --out ...
    python scripts/annotate_tool.py show --file eval/review/claude/x.json --verse 1
    python scripts/annotate_tool.py apply --file eval/review/claude/x.json --notes notes.txt

Notes format, one block per verse (indices are positions in the verse's word list):

    # verse 1
    roles: 0=समासपूर्वपद>2 1=समासपूर्वपद>2 2=विशेषण>7 7=कर्म>8 8=क्रिया>- ...
    compounds: 0,1,2=तत्पुरुष|तपसि स्वाध्याये च निरतः ; 10,11=तत्पुरुष|मुनीनां पुङ्गवः
    anvaya: 9 3 0 1 2 4 5 6 10 11 7 8
    english: Vālmīki the ascetic asked Nārada ...
    issues: (optional: errors noticed in the gold annotation)

``apply`` validates every block (known role names, heads in range and not self, anvaya a
permutation of all indices, compound members contiguous) and reports problems per verse.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import gold, terms  # noqa: E402

ANNOTATOR = "Claude (LLM), not human-verified"
COMPOUND_TYPES = ("तत्पुरुष", "कर्मधारय", "द्वन्द्व", "बहुव्रीहि", "अव्ययीभाव", "नञ्-तत्पुरुष", "नञ्-बहुव्रीहि",
                  "उपपद-तत्पुरुष", "द्विगु", "अज्ञात")


def _range(spec: str) -> list[int]:
    lo, _, hi = spec.partition("-")
    return list(range(int(lo), int(hi or lo) + 1))


def _verses(source: str, positions: list[int]) -> list[dict]:
    if source == "ramayana":
        by_number = {v["number"]: v for v in gold.load()["verses"]}
        return [by_number[n] for n in positions if n in by_number]
    doc = json.loads(Path(source).read_text(encoding="utf-8"))["verses"]
    return [doc[p - 1] for p in positions if 0 < p <= len(doc)]


def skeleton(source: str, positions: list[int]) -> dict:
    verses = []
    for key, v in zip(positions, _verses(source, positions)):
        words = [{"index": 0, "line": li, "form": w["form"], "lemma": w["lemma"], "upos": w.get("upos", ""),
                  "feats": w.get("feats", {}), "compound_member": w["compound_member"],
                  "role": "", "head": None, "note": ""}
                 for li, line in enumerate(v["lines"]) for w in line["words"]]
        for i, w in enumerate(words):
            w["index"] = i
        verses.append({"key": key, "id": v["id"], "number": v["number"], "book": v.get("book", "रामायण"),
                       "text": gold.text_of(v), "words": words, "compounds": [], "anvaya": [],
                       "english": "", "gold_issues": ""})
    return {"annotator": ANNOTATOR, "basis": "DCS gold split", "source": source, "verses": verses}


def show(doc: dict, key: int) -> str:
    v = next(x for x in doc["verses"] if x["key"] == key)
    rows = [f"verse {key}  [{v['id']}]  {v['text']}"]
    for w in v["words"]:
        feats = " ".join(f"{k}={val}" for k, val in w["feats"].items())
        member = " (compound member)" if w["compound_member"] else ""
        rows.append(f"  {w['index']:>2}  line {w['line']}  {w['form']}  lemma {w['lemma']}  {w['upos']} {feats}{member}")
    return "\n".join(rows)


def parse_notes(text: str) -> dict[int, dict[str, str]]:
    blocks: dict[int, dict[str, str]] = {}
    key = None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("# verse"):
            key = int(line.split()[2])
            blocks[key] = {}
        elif key is not None and ":" in line:
            field, _, value = line.partition(":")
            blocks[key][field.strip()] = value.strip()
    return blocks


def apply_block(verse: dict, block: dict[str, str]) -> tuple[dict, list[str]]:
    """A new verse dict with the block's annotation merged in, and the problems found."""
    n, problems = len(verse["words"]), []
    words = [dict(w) for w in verse["words"]]
    for item in block.get("roles", "").split():
        try:
            index, rest = item.split("=", 1)
            role, _, head = rest.partition(">")
            i = int(index)
            h = None if head in ("-", "") else int(head)
        except ValueError:
            problems.append(f"cannot read role item {item!r}")
            continue
        if role not in terms.ROLES or not role:
            problems.append(f"unknown role {role!r} at {i}")
        if not 0 <= i < n or (h is not None and (not 0 <= h < n or h == i)):
            problems.append(f"index out of range or self-head in {item!r}")
            continue
        words[i] = {**words[i], "role": role, "head": h}
    problems += [f"word {w['index']} ({w['form']}) has no role" for w in words if not w["role"]]
    compounds = []
    for part in filter(None, (p.strip() for p in block.get("compounds", "").split(";"))):
        try:
            members_text, rest = part.split("=", 1)
            kind, _, vigraha = rest.partition("|")
            members = [int(x) for x in members_text.split(",")]
        except ValueError:
            problems.append(f"cannot read compound {part!r}")
            continue
        if kind.strip() not in COMPOUND_TYPES:
            problems.append(f"unknown compound type {kind!r}")
        if members != list(range(members[0], members[0] + len(members))) or members[-1] >= n:
            problems.append(f"compound members not contiguous or out of range: {members}")
        compounds.append({"members": members, "type": kind.strip(), "vigraha": vigraha.strip()})
    try:
        anvaya = [int(x) for x in block.get("anvaya", "").split()]
    except ValueError:
        anvaya = []
    if sorted(anvaya) != list(range(n)):
        problems.append("anvaya is not a permutation of all word indices")
    if not block.get("english"):
        problems.append("english missing")
    merged = {**verse, "words": words, "compounds": compounds, "anvaya": anvaya,
              "english": block.get("english", ""), "gold_issues": block.get("issues", "")}
    return merged, problems


def apply(doc: dict, notes: str) -> tuple[dict, dict[int, list[str]]]:
    blocks, report, verses = parse_notes(notes), {}, []
    for v in doc["verses"]:
        if v["key"] in blocks:
            v, problems = apply_block(v, blocks[v["key"]])
            if problems:
                report[v["key"]] = problems
        verses.append(v)
    return {**doc, "verses": verses}, report


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sk = sub.add_parser("skeleton")
    sk.add_argument("--source", required=True)
    sk.add_argument("--verses", required=True)
    sk.add_argument("--out", required=True)
    sh = sub.add_parser("show")
    sh.add_argument("--file", required=True)
    sh.add_argument("--verse", required=True)
    aply = sub.add_parser("apply")
    aply.add_argument("--file", required=True)
    aply.add_argument("--notes", required=True)
    args = ap.parse_args(argv)
    if args.cmd == "skeleton":
        doc = skeleton(args.source, _range(args.verses))
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"wrote {args.out}: {len(doc['verses'])} verses")
        return 0
    doc = json.loads(Path(args.file).read_text(encoding="utf-8"))
    if args.cmd == "show":
        for key in _range(args.verse):
            print(show(doc, key))
        return 0
    merged, report = apply(doc, Path(args.notes).read_text(encoding="utf-8"))
    Path(args.file).write_text(json.dumps(merged, ensure_ascii=False, indent=1), encoding="utf-8")
    done = sum(1 for v in merged["verses"] if v["anvaya"])
    print(f"{done}/{len(merged['verses'])} verses annotated; {len(report)} with problems")
    for key, problems in report.items():
        print(f"  verse {key}: " + "; ".join(problems))
    return 1 if report else 0


if __name__ == "__main__":
    raise SystemExit(main())
