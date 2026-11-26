"""End-to-end tests of the verse pipeline."""

import json

import pytest

from mayur import gold, jsonout, pipeline
from mayur.model import VERIFIED


def _splits(analysis):
    return [[w.form for w in r.words] for r in analysis.readings]


@pytest.fixture(scope="module")
def shveta():
    return pipeline.analyze_verse("श्वेतो धावति", verse_id="test")


def test_to_lines_handles_scripts_and_dandas():
    assert pipeline.to_lines("श्वेतो धावति ॥ १ ॥") == ["Sveto DAvati"]
    assert pipeline.to_lines("śveto dhāvati") == ["Sveto DAvati"]
    assert pipeline.to_lines("Sveto DAvati | rAmo gacCati") == ["Sveto DAvati", "rAmo gacCati"]


def test_shveto_dhavati_returns_both_readings(shveta):
    splits = _splits(shveta)
    assert ["Svetas", "DAvati"] in splits
    assert ["SvA", "itas", "DAvati"] in splits


def test_shveto_dhavati_readings_are_proof_verified(shveta):
    by_split = {tuple(w.form for w in r.words): r for r in shveta.readings}
    for split in (("Svetas", "DAvati"), ("SvA", "itas", "DAvati")):
        reading = by_split[split]
        assert reading.sandhi_ok
        assert all(w.proof and w.proof.derivable and w.proof.trace for w in reading.words)
        assert reading.status == VERIFIED


def test_chosen_reading_has_all_six_outputs(shveta):
    best = shveta.readings[0]
    assert best.words and all(w.morph for w in best.words)
    assert sorted(best.anvaya) == list(range(len(best.words)))
    assert best.translation
    assert all(0 <= a.start < a.end <= len(best.translation) for a in best.alignment)
    verb = next(w for w in best.words if w.form == "DAvati")
    assert verb.morph.kind == "tinanta" and verb.role == "kriya"


def test_alternatives_are_kept_with_scores(shveta):
    assert len(shveta.readings) >= 2
    assert all("total" in r.scores for r in shveta.readings)


def test_unknown_word_is_labelled_not_forced():
    analysis = pipeline.analyze_verse("xqzxqz DAvati")
    assert analysis.status != VERIFIED
    assert any(w.arsha for w in analysis.readings[0].words)


def test_ramayana_verse_one_is_verified_and_serialisable():
    analysis = pipeline.analyze_verse(gold.verse_text(1), verse_id="R.1.1.1")
    best = analysis.readings[0]
    forms = [w.form for w in best.words]
    assert "nAradam" in forms and "vAlmIkis" in forms and "paripapracCa" in forms
    assert analysis.metre["name"].startswith("anuzwuB")
    assert json.dumps(jsonout.to_json(analysis), ensure_ascii=False)
