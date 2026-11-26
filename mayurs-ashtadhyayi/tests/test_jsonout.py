from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from ui_fixture import make_analysis  # noqa: E402

from mayur import jsonout  # noqa: E402
from mayur.model import VerseAnalysis  # noqa: E402

RULES = {("अष्टाध्यायी", "8.3.23"): "मोऽनुस्वारः", ("अष्टाध्यायी", "6.1.87"): "आद्गुणः"}


@pytest.fixture(autouse=True)
def _rules(monkeypatch):
    monkeypatch.setattr(jsonout, "rule_texts", lambda: RULES)


def test_top_level_and_sanskrit_values():
    d = jsonout.to_json(make_analysis())
    assert d["status"] == "verified" and d["split_counts"] == [2, 3]
    assert d["lines"][0]["devanagari"].startswith("तपः")
    assert d["lines"][0]["iast"].startswith("tapaḥ")
    assert d["padaccheda"][0][0]["devanagari"] == "तपः-स्वाध्याय-निरतम्"


def test_word_grammar_and_description():
    d = jsonout.to_json(make_analysis())
    nrd = d["words"][6]
    assert nrd["form"]["devanagari"] == "नारदम्"
    assert nrd["grammar"]["case"] == {"devanagari": "द्वितीया", "english": "accusative"}
    assert nrd["description"] == "masculine accusative singular of नारद"
    assert nrd["verified"] is True
    verb = d["words"][7]
    assert verb["grammar"]["tense_mood"]["english"] == "perfect"
    assert verb["description"].startswith("3rd person singular perfect active")


def test_trace_and_junction_rule_texts():
    d = jsonout.to_json(make_analysis())
    step = d["words"][7]["sutra_trace"][0]
    assert set(step) == {"code", "number", "source", "sutra", "result"}
    assert step["number"]["arabic"].translate(str.maketrans("0123456789", "०१२३४५६७८९")) == step["code"]
    j = next(x for x in d["junctions"] if x["left"] == 4)
    assert j["sutras"][0]["text"]["devanagari"] == "मोऽनुस्वारः"
    assert j["surface"]["devanagari"] == "वाग्विदां"


def test_arsha_unverified_word():
    w = jsonout.to_json(make_analysis())["words"][3]
    assert w["arsha"] is True and w["verified"] is False and w["verified_reason"]


def test_other_analyses_limited_unless_full():
    a = make_analysis()
    extra = a.readings[0].words[0].analyses[0]
    a.readings[0].words[0].analyses = [extra] * 9
    assert len(jsonout.to_json(a)["words"][0]["other_analyses"]) == 5
    assert len(jsonout.to_json(a, full=True)["words"][0]["other_analyses"]) == 8


def test_alternatives_and_full():
    a = make_analysis()
    d = jsonout.to_json(a)
    assert len(d["alternatives"]) == 1 and "words" not in d["alternatives"][0]
    assert "words" in jsonout.to_json(a, full=True)["alternatives"][0]


def test_alignment_text_and_compound_type():
    d = jsonout.to_json(make_analysis())
    assert d["alignment"][0]["text"] == d["translation"][0:7]
    assert d["compounds"][0]["type"]["devanagari"] == "तत्पुरुष"


def test_empty_analysis():
    d = jsonout.to_json(VerseAnalysis(id="x", input="", lines=[]))
    assert d["words"] == [] and d["alternatives"] == [] and d["padaccheda"] == []


def test_json_serialisable_and_no_roman_sanskrit_terms():
    text = json.dumps(jsonout.to_json(make_analysis(), full=True), ensure_ascii=False)
    for roman in ("tatpurusha", "karmadharaya", "subanta", "tinanta"):
        assert roman not in text
    assert re.search(r"[ऀ-ॿ]", text)


def test_split_rule():
    assert jsonout.split_rule("6.1.87") == ("अष्टाध्यायी", "6.1.87")
    assert jsonout.split_rule("वार्त्तिक 6.1.87") == ("वार्त्तिक", "6.1.87")
