from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema
import pytest

sys.path.insert(0, str(Path(__file__).parent))
from ui_fixture import make_analysis  # noqa: E402

from mayur import cli, jsonout, lipi  # noqa: E402

SCHEMA = json.loads((Path(__file__).parent.parent / "schema" / "verse.schema.json").read_text(encoding="utf-8"))


@pytest.fixture(autouse=True)
def _patched(monkeypatch):
    calls = []

    def fake(text, verse_id="", script=None, max_readings=5):
        calls.append((text, verse_id, script, max_readings))
        if text.isascii():
            raise lipi.AmbiguousScript("plain ASCII input is ambiguous")
        return make_analysis(verse_id or "x")

    monkeypatch.setattr(cli, "run_pipeline", fake)
    monkeypatch.setattr(cli, "gold_text", lambda n: "श्वेतो धावति")
    monkeypatch.setattr(jsonout, "rule_texts", lambda: {})
    return calls


def test_analyze_prints_valid_json(capsys, _patched):
    assert cli.main(["analyze", "श्वेतो धावति", "--id", "t1", "--max-readings", "3"]) == 0
    out = capsys.readouterr().out
    data = json.loads(out)
    jsonschema.validate(data, SCHEMA, cls=jsonschema.Draft202012Validator)
    assert "तपः" in out and "\\u" not in out and out.count("\n") > 5
    assert _patched[0] == ("श्वेतो धावति", "t1", None, 3)


def test_compact_is_single_line(capsys):
    assert cli.main(["analyze", "श्वेतो धावति", "--compact", "--full"]) == 0
    assert len(capsys.readouterr().out.strip().splitlines()) == 1


def test_ascii_refused(capsys):
    assert cli.main(["analyze", "rama"]) == 1
    cap = capsys.readouterr()
    assert cap.out == "" and "ambiguous" in cap.err


def test_verse_command(capsys, _patched):
    assert cli.main(["verse", "4"]) == 0
    assert json.loads(capsys.readouterr().out)["id"] == "1.4"
    assert _patched[0][1] == "1.4"


def test_html_writes_file(tmp_path, capsys):
    out = tmp_path / "sub" / "index.html"
    assert cli.main(["html", "--verses", "1-3", "--out", str(out)]) == 0
    page = out.read_text(encoding="utf-8")
    assert page.count('class="card"') == 3


def test_bad_range_exit_1(capsys):
    assert cli.main(["html", "--verses", "x"]) == 1
    assert "error" in capsys.readouterr().err


def test_parse_range():
    assert cli.parse_range("1-3,7") == [1, 2, 3, 7]
