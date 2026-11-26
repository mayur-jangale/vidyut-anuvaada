"""Gold data and count tables for scripts/train_decoder.py.

TRAIN = split_files("train") minus the named held-out chapters; DEV = split_files("dev") +
a dev_pool sample; TEST = split_files("test") (report only). sealed_test is never read.
"""

from __future__ import annotations

import hashlib
import math
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from mayur import dcs, freq  # noqa: E402
from mayur import decoder_words as dw  # noqa: E402

MAX_CHARS = 90  # longer (prose) lines are skipped in training
Line = tuple[str, list[dict]]


def held_out(path: Path) -> bool:
    n = path.name
    return ("Rāmāyaṇa-0000-" in n or n.startswith("Kumārasaṃbhava-0000-")
            or "BhaGī 1-" in n or "BhaGī 2-" in n)


def _text_of(entry: dict) -> str:
    return Path(entry["file"]).parent.name


INDECLINABLE_UPOS = frozenset({"ADV", "PART", "CONJ", "CCONJ", "SCONJ", "ADP", "INTJ"})


def _words(ws: list[dict]) -> list[dict]:
    """Gold words; ``either`` marks an indeclinable followed by another word, which the corpus tags
    as a free word even when it is a glued prefix (स-, सु-, अन्-): member or free both match it."""
    keep = ("form", "lemma", "compound_member", "upos")
    return [{**{k: w.get(k, "") for k in keep}, "either": w.get("upos") in INDECLINABLE_UPOS and n + 1 < len(ws)}
            for n, w in enumerate(ws)]


def gold_of(entries: list[dict], limit: int | None = None, seed: int = 0) -> list[Line]:
    return [(g["compact"], _words(g["words"])) for g in dcs.gold_lines(entries, limit=limit, seed=seed)
            if g["words"] and len(g["compact"]) <= MAX_CHARS]


def held_sets(per_pool_text: int = 20) -> dict[str, list[Line]]:
    """DEV per text (old DEV sets + dev_pool sample) and TEST per text. Never touches sealed_test."""
    out: dict[str, list] = {}
    for split, prefix, limit in (("dev", "dev", None), ("dev_pool", "dev", per_pool_text), ("test", "test", None)):
        by_text: dict[str, list[dict]] = {}
        for e in dcs.split_files(split):
            by_text.setdefault(_text_of(e), []).append(e)
        for text, es in sorted(by_text.items()):
            out.setdefault(f"{prefix}_{text}", []).extend(gold_of(es, limit))
    return out


def train_lines(n: int, seed: int = 0) -> list[Line]:
    """``n`` TRAIN half-verses stratified by text (equal share per text, sampled across its chapters)."""
    by_text: dict[str, list[dict]] = {}
    for e in dcs.split_files("train"):
        if not held_out(Path(e["file"])):
            by_text.setdefault(_text_of(e), []).append(e)
    rng = random.Random(seed)
    share = max(1, n // max(1, len(by_text)))
    pool: list = []
    for _, es in sorted(by_text.items()):
        rng.shuffle(es)
        pool.extend(gold_of(es[: max(3, share // 20)], limit=share, seed=seed))
    rng.shuffle(pool)
    return pool[:n]


def tag_table(lines: list[Line]) -> dict[str, float]:
    """log P(tag_i | tag_{i-1}) from TRAIN gold (add-one smoothed), tags via decoder_words.word_tag."""
    big, uni = Counter(), Counter()
    for _, gold in lines:
        seq = [dw.START_TAG, *(dw.word_tag(g["form"], g["compound_member"]) for g in gold), dw.END_TAG]
        for a, b in zip(seq, seq[1:]):
            big[(a, b)] += 1
            uni[a] += 1
    v = len({t for pair in big for t in pair})
    table = {f"{a}|{b}": math.log((c + 1) / (uni[a] + v)) for (a, b), c in big.items()}
    table["<unk>"] = math.log(1 / (max(uni.values()) + v))
    return table


def prefix_table(lines: list[Line], min_rests: int = 5) -> dict[str, dict[str, int]]:
    """How often the corpus writes a short indeclinable p as a free word before a word of lemma r
    although p+r is itself a corpus lemma (स गुणस् vs सगुणस्). Prefixes are found, not listed:
    a free short indeclinable qualifies when at least ``min_rests`` such r exist."""
    counts: dict[str, Counter] = defaultdict(Counter)
    for _, gold in lines:
        for a, b in zip(gold, gold[1:]):
            if a["compound_member"] or dw.syllables(a["form"]) > 2:
                continue
            if freq.lemma_class(a["lemma"]) != "indeclinable" and a["upos"] not in ("ADV", "PART", "ADP"):
                continue
            counts[a["form"]][b["lemma"]] += 1
    out = {}
    for p, rests in counts.items():
        ambiguous = {r: n for r, n in rests.items() if freq.lemma_count(p + r) > 0}
        if len(ambiguous) >= min_rests:
            out[p] = ambiguous
    return out


def digest(*objs: object) -> str:
    return hashlib.sha1(repr(objs).encode()).hexdigest()[:12]


def code_key() -> str:
    """Hash of everything a cached lattice shard depends on: the lattice and feature code and the
    corpus tables (content of the code, size+mtime of the tables)."""
    h = hashlib.sha1()
    mayur = ROOT / "mayur"
    for p in sorted([*mayur.glob("segmenter.py"), *mayur.glob("sandhi.py"), *mayur.glob("lexicon*.py"),
                     *mayur.glob("decoder*.py"), *mayur.glob("freq.py"), *mayur.glob("bridge.py"),
                     *mayur.glob("ud.py"), *mayur.glob("model.py"), *mayur.glob("lipi.py")]):
        h.update(p.name.encode() + p.read_bytes())
    for p in sorted((ROOT / "data" / "derived").glob("*.json")):
        st = p.stat()
        h.update(f"{p.name}:{st.st_size}:{st.st_mtime_ns}".encode())
    return h.hexdigest()[:12]
