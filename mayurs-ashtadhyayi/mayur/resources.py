"""Locations of external data and lazily loaded vidyut handles."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

DATA_ENV = "MAYUR_DATA_DIR"
FETCH_HINT = "run `python scripts/fetch_data.py` first"


def data_dir() -> Path:
    env = os.environ.get(DATA_ENV)
    if env:
        return Path(env)
    repo = Path(__file__).resolve().parent.parent / "data"
    return repo if repo.exists() else Path.home() / ".cache" / "mayur"


def vidyut_dir() -> Path:
    return data_dir() / "vidyut"


def derived_dir() -> Path:
    return data_dir() / "derived"


def _require(path: Path) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"{path} is missing; {FETCH_HINT}")
    return path


@lru_cache(maxsize=1)
def kosha():
    from vidyut.kosha import Kosha

    return Kosha(str(_require(vidyut_dir() / "kosha")))


@lru_cache(maxsize=1)
def vyakarana():
    from vidyut.prakriya import Vyakarana

    return Vyakarana(log_steps=True, nlp_mode=True)


@lru_cache(maxsize=1)
def sandhi_rules() -> tuple[tuple[str, str, str], ...]:
    """(first, second, result) triples from vidyut-sandhi's rule table."""
    import csv

    with open(_require(vidyut_dir() / "sandhi" / "rules.csv"), encoding="utf-8") as f:
        return tuple((r["first"], r["second"], r["result"]) for r in csv.DictReader(f))


@lru_cache(maxsize=1)
def chandas():
    from vidyut.chandas import Chandas

    return Chandas(str(_require(vidyut_dir() / "chandas" / "meters.tsv")))
