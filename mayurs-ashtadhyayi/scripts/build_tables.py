"""Build the derived tables in data/derived/ from the DCS Ramayana files.

    python scripts/build_tables.py [--data-dir DIR]

Every fetched text is counted except the held-out chapters (HELD_OUT_IDS).
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import dcs  # noqa: E402
from mayur.lipi import devanagari  # noqa: E402

# DCS chapter_ids that are never counted: Ramayana Balakanda 1, Kumarasambhava 1, Bhagavad Gita 1 and 2
# (= Mahabharata 6 BhaGi 1, 2).
HELD_OUT_IDS = frozenset({"1067", "7305", "7242", "7243"})
MIN_BIGRAM = 2
POOL_SEED, POOL_SHARE, POOL_MIN_CHAPTERS = 20261126, 0.06, 5
POOLS_FILE = Path(__file__).resolve().parent.parent / "mayur" / "gold" / "pools.json"
# (split, chapter_id, verse range): Ramayana Bala 1 and Kumarasambhava 1 are split 1-20 test / rest dev.
HELD_OUT_SPLITS = (("test", "1067", (1, 20)), ("dev", "1067", (21, 79)), ("test", "7305", (1, 20)),
                   ("dev", "7305", (21, 60)), ("test", "7242", None), ("test", "7243", None))
TAG_FEATS = ("Case", "Gender", "Number", "Person", "Tense", "Mood", "VerbForm")
CLASS_OF_UPOS = {"NOUN": "noun", "PROPN": "noun", "ADJ": "adjective", "NUM": "adjective", "PRON": "pronoun",
                 "DET": "pronoun", "VERB": "verb", "AUX": "verb"}


def tag_key(lemma: str, upos: str, feats: dict[str, str]) -> str:
    parts = [f"{k}={feats[k]}" for k in sorted(TAG_FEATS) if feats.get(k)]
    return "|".join([lemma, upos, *parts])


def count_sentences(sentences, held_out=HELD_OUT_IDS) -> dict:
    """Counts over an iterable of sentence dicts (``dcs.iter_sentences``)."""
    forms: Counter = Counter()
    bigrams: Counter = Counter()
    members: Counter = Counter()
    lemmas: Counter = Counter()
    tags: dict[str, Counter] = defaultdict(Counter)
    senses: dict[str, Counter] = defaultdict(Counter)
    upos: dict[str, Counter] = defaultdict(Counter)
    held, tokens = set(), 0
    for sent in sentences:
        if not sent["tokens"]:
            continue
        if sent["chapter_id"] in held_out:
            held.add(sent["chapter"])
            continue
        seq = [t["form"] for t in sent["tokens"]]
        bigrams.update(zip(seq, seq[1:]))
        for tok in sent["tokens"]:
            if tok["compound_member"]:
                members[tok["form"]] += 1
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
            "tokens": tokens, "held_out": sorted(held), "bigrams": bigrams, "members": members}


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
        "bigrams.json": {f"{a}\t{b}": n for (a, b), n in counted["bigrams"].items() if n >= MIN_BIGRAM},
        "member_counts.json": dict(counted["members"]),
        "form_tags.json": {f: dict(c) for f, c in counted["tags"].items()},
        "dcs_senses.json": {lm: labels.get(top(c), "") for lm, c in counted["senses"].items()},
        "dcs_dict.json": dictionary_rows,
        "lemma_class.json": {lm: CLASS_OF_UPOS.get(top(c), "indeclinable") for lm, c in counted["upos"].items()},
    }


def chapter_files(root: Path) -> list[Path]:
    return sorted((root / "files").glob("*/*.conllu"))  # not the *.conllu_parsed files


def chapter_id(path: Path) -> str:
    return path.stem.rsplit("-", 1)[-1]


def is_presplit(sentences: list[dict], threshold: float = 0.5) -> bool:
    """True when the ``# text`` lines are the plain space-join of the unsandhied forms (no real sandhi)."""
    usable = [s for s in sentences if len(s["tokens"]) >= 3]
    if not usable:
        return True
    same = sum(" ".join(t["unsandhied"] for t in s["tokens"]) == s["text"] for s in usable)
    return same / len(usable) > threshold


def draw_pools(by_text: dict[str, list[Path]], presplit: set[str], exclude: set[str]) -> dict[str, list[dict]]:
    """Seeded, stratified random chapter pools ("sealed_test", "dev_pool"), disjoint, about 6% of each
    text's chapters each (at least one for a text with 5 or more chapters)."""
    rng = random.Random(POOL_SEED)
    pools: dict[str, list[dict]] = {"sealed_test": [], "dev_pool": []}
    for text in sorted(by_text):
        files = by_text[text]
        if text in presplit or len(files) < POOL_MIN_CHAPTERS:
            continue
        k = max(1, round(POOL_SHARE * len(files)))
        candidates = sorted(chapter_id(f) for f in files if chapter_id(f) not in exclude)
        picked = rng.sample(candidates, min(2 * k, len(candidates)))
        for pool, ids in (("sealed_test", picked[:k]), ("dev_pool", picked[k:2 * k])):
            pools[pool] += [{"text": text, "chapter_id": cid} for cid in sorted(ids, key=int)]
    return pools


def splits(root: Path, files: list[Path], pools: dict[str, list[dict]] | None = None) -> dict[str, list[dict]]:
    """Train = every counted chapter; dev/test = parts of the held-out chapters (see HELD_OUT_SPLITS)."""
    rel = lambda f: str(f.relative_to(root))  # noqa: E731
    by_id = {chapter_id(f): f for f in files}
    pools = pools or {}
    pooled = {e["chapter_id"] for rows in pools.values() for e in rows}
    out: dict[str, list[dict]] = {"train": [{"file": rel(f), "verses": None}
                                            for cid, f in by_id.items() if cid not in HELD_OUT_IDS | pooled],
                                  "dev": [], "test": []}
    for pool, rows in pools.items():
        out[pool] = [{"file": rel(by_id[e["chapter_id"]]), "verses": None} for e in rows]
    for name, cid, span in HELD_OUT_SPLITS:
        if cid in by_id:
            out[name].append({"file": rel(by_id[cid]), "verses": list(span) if span else None})
    return out


def build(data_dir: Path) -> dict[str, int]:
    root = data_dir / "dcs" / "sanskrit" / "dcs" / "data" / "conllu"
    files = chapter_files(root)
    if not files:
        raise FileNotFoundError(f"no DCS files under {root}; run scripts/fetch_data.py")
    by_text: dict[str, list[Path]] = defaultdict(list)
    for f in files:
        by_text[f.parent.name].append(f)
    presplit = {t: is_presplit([x for f in fs[:3] for x in dcs.iter_sentences(f)]) for t, fs in by_text.items()}
    pools = draw_pools(by_text, {t for t, v in presplit.items() if v}, set(HELD_OUT_IDS))
    excluded = set(HELD_OUT_IDS) | {e["chapter_id"] for rows in pools.values() for e in rows}
    sentences = (s for f in files for s in dcs.iter_sentences(f))
    counted = count_sentences(sentences, held_out=excluded)
    out = tables(counted, sense_labels(root / "lookup" / "word-senses.csv"), dictionary(root / "lookup" / "dictionary.csv"))
    out["splits.json"] = splits(root, files, pools)
    POOLS_FILE.write_text(json.dumps({"seed": POOL_SEED, "presplit_texts_excluded": sorted(t for t, v in presplit.items() if v),
                                      **pools}, ensure_ascii=False, indent=1), encoding="utf-8")
    dest = data_dir / "derived"
    dest.mkdir(parents=True, exist_ok=True)
    for name, obj in out.items():
        (dest / name).write_text(json.dumps(obj, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    return {"files": len(files), "tokens": counted["tokens"], "presplit": sorted(t for t, v in presplit.items() if v),
            "pools": {k: len(v) for k, v in pools.items()}, **{n: len(o) for n, o in out.items()}}


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
