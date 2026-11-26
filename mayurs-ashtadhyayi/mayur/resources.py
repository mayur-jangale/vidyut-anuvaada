"""Locations of external data and lazily loaded vidyut handles."""

from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any

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


def require(path: Path) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"{path} is missing; {FETCH_HINT}")
    return path


@lru_cache(maxsize=None)
def derived(name: str) -> Any:
    """A derived JSON table, or an empty dict when it has not been built."""
    try:
        return json.loads((derived_dir() / name).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


@lru_cache(maxsize=1)
def kosha():
    from vidyut.kosha import Kosha

    return Kosha(str(require(vidyut_dir() / "kosha")))


@lru_cache(maxsize=1)
def vyakarana():
    from vidyut.prakriya import Vyakarana

    return Vyakarana(log_steps=True, nlp_mode=True)


@lru_cache(maxsize=1)
def chandas():
    from vidyut.chandas import Chandas

    return Chandas(str(require(vidyut_dir() / "chandas" / "meters.tsv")))


@lru_cache(maxsize=1)
def sutra_texts() -> dict[tuple[str, str], str]:
    """(source, code) -> rule text, from vidyut's sutrapatha files."""
    from vidyut.prakriya import Data

    data = Data(str(require(vidyut_dir() / "prakriya")))
    return {(str(rule.source), rule.code): rule.text for rule in data.load_sutras()}
