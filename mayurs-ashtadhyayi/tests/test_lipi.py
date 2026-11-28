"""Script handling: Devanagari in, Devanagari out, nothing lost on the way."""

import pytest

from mayur import lipi


def test_varnas_split_and_rejoin():
    assert lipi.varnas("रामस्") == ("र्", "आ", "म्", "अ", "स्")
    assert lipi.varnas("तपःस्वा")[:6] == ("त्", "अ", "प्", "अ", "ः", "स्")
    for text in ("वाल्मीकिर्मुनिपुंगवम्", "रामोऽत्र", "ताँल्लोकान्", "को न्वस्मिन्साम्प्रतं लोके"):
        assert lipi.from_varnas(lipi.varnas(text)) == text


def test_three_sibilants_stay_distinct():
    assert len({lipi.varnas(x) for x in ("श", "ष", "स")}) == 3
    assert [lipi.from_varnas(lipi.varnas(x)) for x in ("शम्", "षट्", "सत्")] == ["शम्", "षट्", "सत्"]


def test_pausa_form():
    assert lipi.pausa("रामस्") == "रामः"
    assert lipi.pausa("पुनर्") == "पुनः"
    assert lipi.pausa("निरतम्") == "निरतम्"


def test_input_scripts():
    assert lipi.devanagari("श्वेतो धावति") == "श्वेतो धावति"
    assert lipi.devanagari("śveto dhāvati") == "श्वेतो धावति"
    with pytest.raises(lipi.AmbiguousScript):
        lipi.devanagari("shveto dhavati")


def test_hiatus_and_om_survive_the_round_trip():
    assert lipi.from_varnas(("त्", "ए", "आ", "स्", "अ")) == "तेआस"
    for text in ("अइ", "प्रउग", "ॐकारस्", "निर्ॐकार"):
        assert lipi.from_varnas(lipi.varnas(text)) == text
