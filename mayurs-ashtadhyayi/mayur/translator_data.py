"""The Itihāsa corpus and the prepared shards the translator is trained from (data side only).

Corpus files live in ``<data dir>/itihasa/`` (``scripts/fetch_data.py --with-itihasa``): one verse
or its English per line. Shards live in ``<data dir>/derived/translation/shards/`` as JSON lines
``{"i": line number in the corpus file, "r": dump_reading(...)}``.
"""

from __future__ import annotations

import json
import random
import re
import unicodedata
from pathlib import Path
from typing import Iterator, Optional

from mayur import resources

SHARD_SIZE = 250
SPLIT_SEED = {"train": 11, "dev": 12, "test": 13}
_NASAL_VIRAMA = re.compile("[ङञणनम]्")
_DROP = re.compile(r"[^ऀ-ॿ]|[ऽ।॥ॐ्]")


def itihasa_dir() -> Path:
    return resources.data_dir() / "itihasa"


def shard_dir() -> Path:
    return resources.derived_dir() / "translation" / "shards"


def read_lines(split: str, lang: str) -> list[str]:
    """Lines of ``<split>.<lang>.csv`` (``sn`` or ``en``); the corpus has no header and no quoting."""
    text = (itihasa_dir() / f"{split}.{lang}.csv").read_text(encoding="utf-8")
    lines = text.split("\n")
    return lines[:-1] if lines and lines[-1] == "" else lines


def compact_key(text: str) -> str:
    """Sanskrit text without spaces and punctuation; a nasal with virama is written as anusvara."""
    text = _NASAL_VIRAMA.sub("ं", unicodedata.normalize("NFC", text))
    return _DROP.sub("", text)


def _shingles(key: str) -> set[str]:
    return {key[i:i + 4] for i in range(len(key) - 3)}


def demo_line_ids(sanskrit: list[str], threshold: float = 0.8) -> set[int]:
    """Train lines of the project's demo verses (Rāmāyaṇa Bālakāṇḍa 1: ``mayur verse 1`` ... ``79``).

    The corpus's text differs from the project's in spelling (anusvara or nasal, split words), so a
    verse is matched on its compact key exactly or, failing that, by character similarity of at
    least ``threshold``. The corpus lists the sarga's verses in order, so every line between the
    first and the last match is dropped too (the corpus also splits and joins verses differently).
    """
    from difflib import SequenceMatcher

    from mayur import gold

    keys = [compact_key(s) for s in sanskrit]
    grams = [_shingles(k) for k in keys]
    found: set[int] = set()
    for n in range(1, 80):
        target = compact_key(gold.verse_text(n))
        near = _shingles(target)
        order = sorted(range(len(keys)), key=lambda i: -len(near & grams[i]))[:3]
        found.update(i for i in order if keys[i] == target
                     or SequenceMatcher(None, target, keys[i]).ratio() >= threshold)
    return set(range(min(found), max(found) + 1)) if found else set()


def corpus_ids(split: str, count: Optional[int] = None) -> list[int]:
    """Line numbers of ``split`` in a fixed random order (train: demo verses removed, empty lines dropped)."""
    sanskrit, english = read_lines(split, "sn"), read_lines(split, "en")
    demo = demo_line_ids(sanskrit) if split == "train" else set()
    ids = [i for i, (s, e) in enumerate(zip(sanskrit, english)) if s.strip() and e.strip() and i not in demo]
    random.Random(SPLIT_SEED[split]).shuffle(ids)
    return ids if count is None else ids[:count]


def shard_path(split: str, k: int) -> Path:
    return shard_dir() / f"{split}_{k:04d}.jsonl"


def read_shard(path: Path) -> Iterator[tuple[int, list]]:
    with open(path, encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            yield row["i"], row["r"]


def available_shards(split: str) -> list[Path]:
    return sorted(shard_dir().glob(f"{split}_*.jsonl"))


def load_verses(split: str, max_shards: Optional[int] = None) -> list[tuple[int, list]]:
    """(corpus line number, dumped reading) of the first ``max_shards`` complete shards of ``split``."""
    shards = available_shards(split)[:max_shards]
    return [row for path in shards for row in read_shard(path)]


def english_lines(split: str) -> list[str]:
    return read_lines(split, "en")
