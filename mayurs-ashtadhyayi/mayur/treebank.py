"""Readers for gold sentence-structure data, and the mapping of its relation labels to our roles.

Every reader yields sentences in ONE format, all text in Devanagari:

    {"id": str, "source": str, "text": <Devanagari text as the pipeline expects it>,
     "words": [{"form", "lemma", "upos", "feats": {..}, "head_index": int | None  (None = root),
                "relation": <label of the dataset>, "role": <our role, "" if unmapped>,
                "compound_member": bool}],
     "compounds": [{"members": [int], "type": str, "vigraha": str}],     # only if the source has them
     "anvaya": [int]}                                                     # only if the source has it

Sources (see scripts/fetch_gold_external.py for licences):
  * "ufal"   UD_Sanskrit-UFAL, written in Devanagari.
  * "vedic"  UD_Sanskrit-Vedic, written in IAST (converted once on reading with ``mayur.lipi``).
  * "dcs"    the dependency-annotated chapters inside the DCS dump (IAST, converted on reading).
  * a "gold_roles.json" written by scripts/import_review.py, and Claude reference files
    (``read_claude``: {"annotator", "basis", "verses": [...]}).

Universal Dependencies treat a compound as several tokens (members flagged ``Compound=Yes`` or
``Case=Cpd``). We evaluate a compound as ONE unit attached by its final member: members get the role
समासपूर्वपद and point to the final member; the final member carries the attachment of the whole unit,
and every head that points into a unit is moved to its final member.

Mapping UD label -> role (``map_role``), first match wins; anything else is "" and is counted by
``unmapped_counts``, never forced:
  finite verb (any label)                       -> क्रिया
  VerbForm=Conv (क्त्वा/ल्यप्)                     -> पूर्वकालक्रिया
  VerbForm=Inf                                  -> तुमर्थ
  nsubj                                         -> कर्ता (कर्म under a passive / past-participle head)
  obj                                           -> कर्म
  iobj, obl:benef, obl + Case=Dat               -> सम्प्रदान
  obl:agent                                     -> कर्ता
  obl:instr, obl + Case=Ins                     -> करण (कर्ता under a passive head)
  obl:source, obl + Case=Abl                    -> अपादान
  obl:loc, obl:lmod, obl:temp/tmod + Loc, obl + Case=Loc -> अधिकरण
  (other obl subtypes, e.g. obl:goal, obl:soc, obl:manner: unmapped)
  nmod + Case=Gen (not nmod:appos)              -> सम्बन्ध
  amod, det, nummod, acl on an adjective/participle -> विशेषण
  vocative                                      -> सम्बोधन
  advmod, cc, mark, discourse, case on an indeclinable (ADV PART CCONJ SCONJ INTJ ADP) -> अव्यय
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Iterator, Optional, Sequence

from mayur import dcs, lipi

ROOT = Path(__file__).resolve().parent.parent
EXTERNAL = ROOT / "data" / "gold_external"
DCS_FILES = ROOT / "data" / "dcs" / "sanskrit" / "dcs" / "data" / "conllu" / "files"
DCS_INDEX = EXTERNAL / "dcs_dependency_files.json"
MEMBER = "समासपूर्वपद"
NON_FINITE = {"Part", "Conv", "Inf", "Gdv", "Ger"}
INDECLINABLE = {"ADV", "PART", "CCONJ", "SCONJ", "INTJ", "ADP", "CONJ"}
OBL_CASE = {"Dat": "सम्प्रदान", "Ins": "करण", "Abl": "अपादान", "Loc": "अधिकरण"}
OBL_SUB = {"agent": "कर्ता", "instr": "करण", "source": "अपादान", "loc": "अधिकरण", "lmod": "अधिकरण",
           "benef": "सम्प्रदान"}
SOURCES = {
    "ufal": {"dir": "ud_sanskrit_ufal", "scheme": "devanagari", "label": "UD_Sanskrit-UFAL"},
    "vedic": {"dir": "ud_sanskrit_vedic", "scheme": "iast", "label": "UD_Sanskrit-Vedic"},
}


def parse_feats(raw: str) -> dict[str, str]:
    if not raw or raw == "_":
        return {}
    return dict(p.split("=", 1) for p in raw.split("|") if "=" in p)


def is_member(feats: dict[str, str]) -> bool:
    return feats.get("Compound") == "Yes" or feats.get("Case") == "Cpd"


def is_passive(feats: dict[str, str]) -> bool:
    return feats.get("Voice") == "Pass" or (feats.get("VerbForm") == "Part" and feats.get("Tense") == "Past"
                                            and feats.get("Voice") != "Act")


def is_finite(upos: str, feats: dict[str, str]) -> bool:
    return (upos in ("VERB", "AUX") and feats.get("VerbForm") not in NON_FINITE
            and any(k in feats for k in ("Person", "Mood", "Tense")))


def map_role(relation: str, feats: dict[str, str], upos: str, head_feats: Optional[dict[str, str]] = None) -> str:
    """Our role for a UD relation, or "" if the label has no counterpart (see the module docstring)."""
    base, _, sub = relation.partition(":")
    case, head_feats = feats.get("Case", ""), head_feats or {}
    if is_finite(upos, feats):
        return "क्रिया"
    if feats.get("VerbForm") == "Conv":
        return "पूर्वकालक्रिया"
    if feats.get("VerbForm") == "Inf":
        return "तुमर्थ"
    passive = is_passive(head_feats)
    if base == "nsubj":
        return "कर्म" if passive else "कर्ता"
    if base == "obj":
        return "कर्म"
    if base == "iobj":
        return "सम्प्रदान"
    if base == "obl":
        if sub in OBL_SUB:
            role = OBL_SUB[sub]
        elif not sub or (sub in ("temp", "tmod") and case == "Loc"):
            role = OBL_CASE.get(case, "")
        else:
            role = ""
        return "कर्ता" if role == "करण" and passive else role
    if base == "nmod":
        return "सम्बन्ध" if case == "Gen" and sub != "appos" else ""
    if base in ("amod", "det", "nummod"):
        return "विशेषण"
    if base == "acl":
        return "विशेषण" if upos == "ADJ" or feats.get("VerbForm") == "Part" else ""
    if base == "vocative":
        return "सम्बोधन"
    if base in ("advmod", "cc", "mark", "discourse", "case") and upos in INDECLINABLE:
        return "अव्यय"
    return ""


def _units(rows: Sequence[dict[str, Any]]) -> list[int]:
    """For each row, the row index of the final member of its compound unit (itself if not a member)."""
    final = list(range(len(rows)))
    for i in range(len(rows) - 1, -1, -1):
        if rows[i]["member"]:
            final[i] = final[i + 1] if i + 1 < len(rows) else i
    return final


def build_words(rows: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
    """Words of one sentence from raw rows (id, form, lemma, upos, feats, head, rel); pure."""
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    final = _units(rows)
    attach: dict[int, int] = {}  # unit final -> row carrying the attachment of the whole unit
    for i, f in enumerate(final):
        inside = {j for j in range(len(rows)) if final[j] == f}
        out = [j for j in sorted(inside) if by_id.get(rows[j]["head"], -1) not in inside]
        attach.setdefault(f, f if f in out else (out[0] if out else f))
    words = []
    for i, r in enumerate(rows):
        f, w = final[i], {"form": r["form"], "lemma": r["lemma"], "upos": r["upos"], "feats": r["feats"],
                          "compound_member": r["member"]}
        if f != i:
            w.update(head_index=f, relation=r["rel"], role=MEMBER)
        else:
            a = rows[attach[i]]
            h = by_id.get(a["head"])
            head = None if h is None or a["head"] == 0 else final[h]
            hf = rows[head]["feats"] if head is not None else {}
            w.update(head_index=head, relation=a["rel"], role=map_role(a["rel"], r["feats"], r["upos"], hf))
        words.append(w)
    return words


def _row(cols: list[str], scheme: str) -> dict[str, Any]:
    feats = parse_feats(cols[5])
    if scheme == "devanagari":
        form, lemma = cols[1], cols[2]
    else:
        tok = dcs._parse_token(cols)  # form: padapatha form from the Unsandhied field; Devanagari
        form, lemma = tok["form"], tok["lemma"]
    return {"id": int(cols[0]), "form": form, "lemma": lemma, "upos": cols[3], "feats": feats,
            "member": is_member(feats), "head": int(cols[6]) if cols[6].isdigit() else 0, "rel": cols[7]}


def parse_conllu(lines: Iterable[str], scheme: str, source: str, annotated_only: bool = True) -> Iterator[dict]:
    """Sentences of CoNLL-U ``lines``; ``scheme`` is "devanagari" or "iast". Sentences without
    dependency annotation (HEAD "_") are skipped when ``annotated_only``."""
    sid, text, rows, n = "", "", [], 0
    for raw in list(lines) + [""]:
        line = raw.rstrip("\n")
        if line.startswith("# sent_id"):
            sid = line.split("=", 1)[1].strip()
        elif line.startswith("# text ="):
            text = line.split("=", 1)[1].strip()
        elif line and not line.startswith("#"):
            cols = line.split("\t")
            if len(cols) >= 8 and cols[0].isdigit() and cols[3] != "PUNCT":
                rows.append(_row(cols, scheme))
                n += cols[6].isdigit()
        elif not line:
            if rows and (n or not annotated_only):
                deva = text if scheme == "devanagari" else dcs.compact(lipi.devanagari(text, "iast"))
                yield {"id": sid or f"{source}.{len(rows)}", "source": source, "text": deva, "words": build_words(rows)}
            sid, text, rows, n = "", "", [], 0


def read_conllu(path: Path | str, scheme: str, source: str) -> Iterator[dict]:
    with open(path, encoding="utf-8") as fh:
        yield from parse_conllu(fh.readlines(), scheme, source)


def dcs_dependency_files(root: Path = DCS_FILES, index: Path = DCS_INDEX) -> list[Path]:
    """DCS chapter files that carry HEAD/DEPREL; from the index written by the fetch script if present."""
    if index.exists():
        return [root / p for p in json.loads(index.read_text(encoding="utf-8"))]
    pat = re.compile(r"^\d+\t[^\t]*\t[^\t]*\t[^\t]*\t[^\t]*\t[^\t]*\t\d+\t[a-z]", re.M)
    return [p for p in sorted(root.rglob("*.conllu")) if pat.search(p.read_text(encoding="utf-8"))]


def iter_source(name: str) -> Iterator[dict]:
    """Sentences of source ``ufal``, ``vedic`` or ``dcs``."""
    if name == "dcs":
        for p in dcs_dependency_files():
            yield from (dict(s, id=f"{p.stem}.{s['id']}") for s in read_conllu(p, "iast", "dcs"))
        return
    spec = SOURCES[name]
    for p in sorted((EXTERNAL / spec["dir"]).glob("*.conllu")):
        yield from read_conllu(p, spec["scheme"], name)


def unmapped_counts(sentences: Iterable[dict]) -> Counter:
    """How often each relation label of non-member words got no role."""
    c: Counter = Counter()
    for s in sentences:
        c.update(w["relation"] for w in s["words"] if not w["compound_member"] and not w["role"])
    return c


def mapping_coverage(sentences: Iterable[dict]) -> dict[str, int]:
    words = [w for s in sentences for w in s["words"] if not w["compound_member"]]
    return {"words": len(words), "mapped": sum(bool(w["role"]) for w in words)}


# Reference files written by annotators (Claude reviewers, or a human through scripts/import_review.py).

def verse_to_sentence(v: dict[str, Any], source: str) -> dict[str, Any]:
    words = [{"form": w["form"], "lemma": w.get("lemma", ""), "upos": "", "feats": {},
              "head_index": w.get("head"), "relation": w.get("role", ""), "role": w.get("role", ""),
              "compound_member": bool(w.get("compound_member")), "line": w.get("line", 0)}
             for w in sorted(v["words"], key=lambda x: x["index"])]
    return {"id": str(v.get("id", v.get("number", ""))), "source": source, "text": v["text"], "words": words,
            "compounds": v.get("compounds", []), "anvaya": v.get("anvaya", []), "english": v.get("english", "")}


def read_claude(path: Path | str) -> list[dict[str, Any]]:
    """Sentences of a reference file {"annotator", "basis", "verses": [...]} (indices are word positions)."""
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    label = doc.get("annotator", "annotator")
    return [verse_to_sentence(v, label) for v in doc["verses"]]


def read_gold_roles(path: Path | str) -> list[dict[str, Any]]:
    """Sentences of eval/review/gold_roles.json ({"sentences": [...]}, written by scripts/import_review.py)."""
    return list(json.loads(Path(path).read_text(encoding="utf-8"))["sentences"])
