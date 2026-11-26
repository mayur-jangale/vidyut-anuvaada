import json
from pathlib import Path

import pytest

from mayur import cli
from tests.fixtures_ui import make_analysis

SCHEMA = json.loads((Path(__file__).parent.parent / "schema" / "verse.schema.json").read_text("utf-8"))


@pytest.fixture
def fake(monkeypatch):
    calls = []

    def fake_analyze(text, verse_id="", max_readings=5):
        calls.append((text, verse_id, max_readings))
        return make_analysis(verse_id or "x")

    monkeypatch.setattr(cli, "_analyze", fake_analyze)
    monkeypatch.setattr(cli, "_gold_text", lambda n: f"verse {n}")
    return calls


def test_analyze_prints_valid_json(fake, capsys):
    jsonschema = pytest.importorskip("jsonschema")
    assert cli.main(["analyze", "a | b ||", "--id", "7", "--max-readings", "3", "--compact"]) == 0
    out = capsys.readouterr().out
    assert "\n" not in out.strip()
    data = json.loads(out)
    jsonschema.validate(data, SCHEMA)
    assert data["id"] == "7"
    assert fake == [("a । b ॥", "7", 3)]
    assert "म" in out  # not ASCII-escaped


def test_analyze_pretty_default(fake, capsys):
    assert cli.main(["analyze", "x"]) == 0
    assert "\n  " in capsys.readouterr().out


def test_verse_command(fake, capsys):
    assert cli.main(["verse", "4"]) == 0
    assert json.loads(capsys.readouterr().out)["id"] == "1.4"


def test_html_writes_file(fake, tmp_path, capsys):
    out = tmp_path / "sub" / "index.html"
    assert cli.main(["html", "--verses", "1-3", "--out", str(out)]) == 0
    assert out.read_text("utf-8").count('class="card"') == 3
    assert [c[1] for c in fake] == ["1.1", "1.2", "1.3"]


def test_errors_exit_1(capsys, monkeypatch):
    assert cli.main(["analyze", "  "]) == 1
    assert cli.main(["html", "--verses", "5-2"]) == 1
    monkeypatch.setattr(cli, "_analyze", lambda *a, **k: (_ for _ in ()).throw(RuntimeError("boom")))
    assert cli.main(["analyze", "x"]) == 1
    err = capsys.readouterr().err
    assert "boom" in err and "Traceback" not in err


def test_parse_range():
    assert cli.parse_range("1-3,8") == [1, 2, 3, 8]
