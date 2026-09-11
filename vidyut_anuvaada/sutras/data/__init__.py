"""Root index — merges all root batches into a single lookup dict.

Usage:
 from vidyut_anuvaada.sutras.data.roots import ALL
 ALL[0] # (root, pos, gloss, decl_class)
 by_lemma["कृष्ण"] # (root, pos, gloss, decl_class)
"""
from __future__ import annotations
from typing import Dict, Tuple

from .roots_batch1 import ROOTS as _B1
from .roots_batch2 import ROOTS as _B2

RawEntry = Dict[str, str | None]
IndexEntry = Tuple[str, str, str, str | None]

ALL_RAW: list[RawEntry] = _B1 + _B2
ALL: list[IndexEntry] = []
_by_lemma: Dict[str, IndexEntry] = {}
_by_root: Dict[str, list[IndexEntry]] = {}

for e in ALL_RAW:
	root = e["r"]
	pos = e["p"]
	gloss = e["g"]
	decl = e.get("d")
	entry: IndexEntry = (root, pos, gloss, decl)
	ALL.append(entry)
	_by_lemma[root] = entry
	_by_root.setdefault(root, []).append(entry)

def by_lemma(lemma: str) -> IndexEntry | None:
	return _by_lemma.get(lemma)

def by_root(root: str) -> list[IndexEntry]:
	return _by_root.get(root, [])

def lookup(root: str) -> tuple | None:
	e = _by_lemma.get(root)
	if e:
		return (e[0], e[1], e[2])
	return None

def count() -> int:
	return len(ALL)
