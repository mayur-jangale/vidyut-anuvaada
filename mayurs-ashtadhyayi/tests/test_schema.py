from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema
import pytest

sys.path.insert(0, str(Path(__file__).parent))
from ui_fixture import make_analysis  # noqa: E402

from mayur import jsonout  # noqa: E402
from mayur.model import VerseAnalysis  # noqa: E402

SCHEMA = json.loads((Path(__file__).parent.parent / "schema" / "verse.schema.json").read_text(encoding="utf-8"))


@pytest.fixture(autouse=True)
def _rules(monkeypatch):
    monkeypatch.setattr(jsonout, "rule_texts", lambda: {})


def test_schema_is_valid():
    jsonschema.Draft202012Validator.check_schema(SCHEMA)


@pytest.mark.parametrize("full", [False, True])
def test_fixture_validates(full):
    jsonschema.validate(jsonout.to_json(make_analysis(), full=full), SCHEMA, cls=jsonschema.Draft202012Validator)


def test_empty_validates():
    jsonschema.validate(jsonout.to_json(VerseAnalysis(id="", input="")), SCHEMA, cls=jsonschema.Draft202012Validator)


def test_bad_status_rejected():
    d = jsonout.to_json(make_analysis())
    d["status"] = "maybe"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(d, SCHEMA, cls=jsonschema.Draft202012Validator)
