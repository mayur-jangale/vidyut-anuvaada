"""End-to-end tests of the verse pipeline (all Sanskrit in Devanagari)."""

import json

import pytest

from mayur import gold, jsonout, lipi, pipeline
from mayur.model import VERIFIED


def _splits(analysis):
    return [[w.form for w in r.words] for r in analysis.readings]


@pytest.fixture(scope="module")
def shveta():
    return pipeline.analyze_verse("श्वेतो धावति", verse_id="परीक्षा")


def test_to_lines_handles_dandas_numbers_and_iast():
    assert pipeline.to_lines("श्वेतो धावति ॥ १ ॥") == ["श्वेतो धावति"]
    assert pipeline.to_lines("śveto dhāvati") == ["श्वेतो धावति"]
    assert pipeline.to_lines("श्वेतो धावति । रामो गच्छति ॥") == ["श्वेतो धावति", "रामो गच्छति"]


def test_plain_ascii_input_is_refused():
    with pytest.raises(lipi.AmbiguousScript):
        pipeline.analyze_verse("shveto dhavati")


def test_shveto_dhavati_returns_both_readings(shveta):
    splits = _splits(shveta)
    assert ["श्वेतस्", "धावति"] in splits
    assert ["श्वा", "इतस्", "धावति"] in splits


def test_both_readings_pass_the_proof_gate(shveta):
    by_split = {tuple(w.form for w in r.words): r for r in shveta.readings}
    for split in (("श्वेतस्", "धावति"), ("श्वा", "इतस्", "धावति")):
        reading = by_split[split]
        assert reading.sandhi_ok
        assert all(w.proof and w.proof.derivable and w.proof.trace for w in reading.words)
        assert reading.status == VERIFIED


def test_chosen_reading_has_every_output(shveta):
    best = shveta.readings[0]
    assert best.words and all(w.morph for w in best.words)
    assert sorted(best.anvaya) == list(range(len(best.words)))
    assert best.translation
    assert all(0 <= a.start < a.end <= len(best.translation) for a in best.alignment)
    verb = next(w for w in best.words if w.form == "धावति")
    assert verb.morph.kind == "tinanta" and verb.role == "क्रिया"


def test_alternatives_are_kept_with_scores(shveta):
    assert len(shveta.readings) >= 2
    assert all("total" in r.scores for r in shveta.readings)


def test_unknown_word_is_labelled_not_forced():
    analysis = pipeline.analyze_verse("झ्रख्म्लुट्ट धावति")
    assert analysis.status != VERIFIED
    assert any(w.arsha for w in analysis.readings[0].words)


def test_ramayana_verse_one():
    analysis = pipeline.analyze_verse(gold.verse_text(1), verse_id="रामायण १.१.१")
    forms = [w.form for w in analysis.readings[0].words]
    assert {"नारदम्", "वाल्मीकिस्", "परिपप्रच्छ"} <= set(forms)
    assert analysis.metre["name"].startswith("अनुष्टुभ्")
    assert json.dumps(jsonout.to_json(analysis), ensure_ascii=False)
