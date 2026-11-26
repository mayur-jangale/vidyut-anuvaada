import json
from pathlib import Path

import pytest

jsonschema = pytest.importorskip("jsonschema")

from mayur.jsonout import to_json
from tests.fixtures_ui import make_analysis

SCHEMA = json.loads((Path(__file__).parent.parent / "schema" / "verse.schema.json").read_text("utf-8"))


@pytest.mark.parametrize("full", [False, True])
def test_fixture_validates(full):
    data = to_json(make_analysis(), full=full)
    jsonschema.Draft202012Validator(SCHEMA).validate(json.loads(json.dumps(data, ensure_ascii=False)))


def test_schema_is_valid_and_rejects_bad_status():
    jsonschema.Draft202012Validator.check_schema(SCHEMA)
    data = to_json(make_analysis())
    data["status"] = "maybe"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(data, SCHEMA)


def test_trim_and_full():
    a = make_analysis()
    trimmed = to_json(a)
    assert len(trimmed["words"][0]["other_analyses"]) <= 5
    assert "words" not in trimmed["alternatives"][0]
    assert "words" in to_json(a, full=True)["alternatives"][0]


def test_empty_readings_validates():
    a = make_analysis()
    a.readings = []
    jsonschema.validate(to_json(a), SCHEMA)


def test_padaccheda_compound_joined():
    assert "mahā-rāja-putras" in to_json(make_analysis())["padaccheda"][0]["iast"]
