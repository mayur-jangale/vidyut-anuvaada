"""Pytest configuration: make the project importable and check fetched data."""

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def pytest_sessionstart(session):
    from mayur.resources import vidyut_dir

    if not (vidyut_dir() / "kosha").exists():
        pytest.exit(
            "data missing: run `python scripts/fetch_data.py` first",
            returncode=2,
        )
