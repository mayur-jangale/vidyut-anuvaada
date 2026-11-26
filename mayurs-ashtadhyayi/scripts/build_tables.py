"""Build the derived tables in data/derived/ from the DCS Ramayana files.

    python scripts/build_tables.py [--data-dir DIR]

Chapter ``chapter_id`` 1067 (Bala 1) is held out for evaluation and never counted.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import dcs  # noqa: E402
from mayur.lipi import devanagari  # noqa: E402

HELD_OUT_IDS = ("1067",)  # DCS chapter_id of Ramayana, Balakanda, sarga 1
TAG_FEATS = ("Case", "Gender", "Number", "Person", "Tense", "Mood", "VerbForm")
CLASS_OF_UPOS = {"NOUN": "noun", "PROPN": "noun", "ADJ": "adjective", "NUM": "adjective", "PRON": "pronoun",
                 "DET": "pronoun", "VERB": "verb", "AUX": "verb"}
RAMAYANA_TEXT_ID = "143"  # DCS text_id of the Ramayana


def tag_key(lemma: str, upos: str, feats: dict[str, str]) -> str:
    parts = [f"{k}={feats[k]}" for k in sorted(TAG_FEATS) if feats.get(k)]
    return "|".join([lemma, upos, *parts])


def count_sentences(sentences, held_out=HELD_OUT_IDS) -> dict:
    """Counts over an iterable of sentence dicts (``dcs.iter_sentences``)."""
    forms: Counter = Counter()
    lemmas: Counter = Counter()
    tags: dict[str, Counter] = defaultdict(Counter)
    senses: dict[str, Counter] = defaultdict(Counter)
    upos: dict[str, Counter] = defaultdict(Counter)
    held, tokens = set(), 0
    for sent in sentences:
        if sent["text_id"] != RAMAYANA_TEXT_ID:
            continue
        if sent["chapter_id"] in held_out:
            held.add(sent["chapter"])
            continue
        for tok in sent["tokens"]:
            feats = dict(tok["feats"])
            if tok["compound_member"]:
                feats["Case"] = "Cpd"
            forms[tok["form"]] += 1
            lemmas[tok["lemma"]] += 1
            tokens += 1
            tags[tok["form"]][tag_key(tok["lemma"], tok["upos"], feats)] += 1
            upos[tok["lemma"]][tok["upos"]] += 1
            if tok["word_sem"]:
                senses[tok["lemma"]][tok["word_sem"]] += 1
    return {"forms": forms, "lemmas": lemmas, "tags": tags, "senses": senses, "upos": upos,
            "tokens": tokens, "held_out": sorted(held)}


def sense_labels(path: Path) -> dict[str, str]:
    with open(path, encoding="utf-8", newline="") as fh:
        rows = csv.reader(fh, delimiter="\t", quoting=csv.QUOTE_NONE)
        next(rows, None)
        return {r[0]: r[1] for r in rows if len(r) > 1}


def dictionary(path: Path) -> dict[str, list[dict[str, str]]]:
    out: dict[str, list[dict[str, str]]] = defaultdict(list)
    with open(path, encoding="utf-8", newline="") as fh:
        rows = csv.reader(fh, delimiter="\t", quoting=csv.QUOTE_NONE)
        next(rows, None)
        for r in rows:
            if len(r) < 5 or not r[1]:
                continue
            out[devanagari(r[1], "iast")].append(
                {"grammar": r[2], "preverbs": devanagari(r[3], "iast") if r[3] else "", "meanings": r[4]})
    return dict(out)


def tables(counted: dict, labels: dict[str, str], dictionary_rows: dict) -> dict[str, object]:
    top = lambda c: c.most_common(1)[0][0]  # noqa: E731
    return {
        "freq.json": {"forms": dict(counted["forms"]), "lemmas": dict(counted["lemmas"]),
                      "tokens": counted["tokens"], "held_out": counted["held_out"]},
        "form_tags.json": {f: dict(c) for f, c in counted["tags"].items()},
        "dcs_senses.json": {lm: labels.get(top(c), "") for lm, c in counted["senses"].items()},
        "dcs_dict.json": dictionary_rows,
        "lemma_class.json": {lm: CLASS_OF_UPOS.get(top(c), "indeclinable") for lm, c in counted["upos"].items()},
    }


def chapter_files(root: Path) -> list[Path]:
    return sorted((root / "files").glob("*/*.conllu"))


def build(data_dir: Path) -> dict[str, int]:
    root = data_dir / "dcs" / "sanskrit" / "dcs" / "data" / "conllu"
    files = chapter_files(root)
    if not files:
        raise FileNotFoundError(f"no DCS files under {root}; run scripts/fetch_data.py")
    sentences = (s for f in files for s in dcs.iter_sentences(f))
    counted = count_sentences(sentences)
    out = tables(counted, sense_labels(root / "lookup" / "word-senses.csv"), dictionary(root / "lookup" / "dictionary.csv"))
    dest = data_dir / "derived"
    dest.mkdir(parents=True, exist_ok=True)
    for name, obj in out.items():
        (dest / name).write_text(json.dumps(obj, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    return {"files": len(files), "tokens": counted["tokens"], **{n: len(o) for n, o in out.items()}}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=None)
    args = ap.parse_args(argv)
    if args.data_dir is None:
        from mayur.resources import data_dir
        args.data_dir = data_dir()
    print(build(args.data_dir))
    return 0


if __name__ == "__main__":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    raise SystemExit(main())
