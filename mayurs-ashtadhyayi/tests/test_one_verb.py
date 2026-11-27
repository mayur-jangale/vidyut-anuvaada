"""One finite verb to a sentence: a second one that is also a vocative; a labelled verb in a verbless line."""

import pytest

from mayur import pipeline


def _reading(text):
    return pipeline.analyze_verse(text).readings[0]


def test_sanjaya_is_addressed_not_a_second_verb():
    reading = _reading("धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः । मामकाः पाण्डवाश्चैव किमकुर्वत सञ्जय")
    last = reading.words[-1]
    assert last.morph.vibhakti == "सम्बोधन" and last.morph.lemma == "संजय"
    assert any("read as a vocative" in n and "सञ्जि" in n for n in reading.notes)
    assert "O Sañjaya" in reading.translation


@pytest.mark.parametrize("text", ["एहि पश्य", "पठ लिख वद", "रामः गच्छति पश्यति च", "त्वं गच्छ जय शत्रून्", "जय जय राम"])
def test_real_second_verbs_stay(text):
    assert not any("read as a vocative" in n for n in _reading(text).notes)


def test_satyam_eva_jayate():
    reading = _reading("सत्यमेव जयते")
    verb = reading.words[-1]
    assert verb.morph.kind == "tinanta" and verb.morph.root == "जि" and verb.morph.source == "arsha"
    assert "conquers" in reading.translation and reading.reworded == "Truth conquers."
    assert pipeline.analyze_verse("सत्यमेव जयते").status == "unverified"  # the middle voice of जि is labelled, not derived


def test_dative_participle_with_its_governor_stays():
    words = _reading("गच्छते नमः").words
    assert words[0].morph.kind == "subanta" and words[0].morph.vibhakti == "चतुर्थी"
