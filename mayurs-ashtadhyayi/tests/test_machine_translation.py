"""The optional trained translator: off by default, and never able to break the analysis."""

import json
from pathlib import Path

import jsonschema

from mayur import jsonout, pipeline, render_html

SCHEMA = json.loads((Path(__file__).parents[1] / "schema" / "verse.schema.json").read_text(encoding="utf-8"))


def test_off_by_default():
    analysis = pipeline.analyze_verse("रामः वनं गच्छति")
    assert analysis.readings[0].machine_translation == ""
    data = jsonout.to_json(analysis)
    assert data["machine_translation"] == ""
    jsonschema.validate(data, SCHEMA)


def test_a_missing_or_failing_translator_gives_an_empty_line(monkeypatch):
    import sys
    import types

    broken = types.ModuleType("mayur.translator")
    broken.available = lambda: True
    broken.translate = lambda reading: 1 / 0
    monkeypatch.setitem(sys.modules, "mayur.translator", broken)
    monkeypatch.setattr("mayur.translator", broken, raising=False)
    analysis = pipeline.analyze_verse("रामः वनं गच्छति", translator=True)
    assert analysis.readings[0].machine_translation == "" and analysis.status == "verified"


def test_translator_line_is_in_the_json_and_the_page(monkeypatch):
    import sys
    import types

    fake = types.ModuleType("mayur.translator")
    fake.available = lambda: True
    fake.translate = lambda reading: "Rama goes to the forest."
    monkeypatch.setitem(sys.modules, "mayur.translator", fake)
    monkeypatch.setattr("mayur.translator", fake, raising=False)
    analysis = pipeline.analyze_verse("रामः वनं गच्छति", translator=True)
    data = jsonout.to_json(analysis)
    assert data["machine_translation"] == "Rama goes to the forest."
    jsonschema.validate(data, SCHEMA)
    assert "Machine translation" in render_html._translation(data)
