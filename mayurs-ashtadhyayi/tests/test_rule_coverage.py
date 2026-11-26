"""Forms the kosha lacks, produced by lookup of a sibling form and forward generation
(scripts/coverage_rules.py measures how often the rules produce the corpus's reading)."""

import pytest

from mayur import lexicon as L, segmenter, ud


def _first(form, **want):
    for m in L.padas(form):
        if all(getattr(m, k) == v for k, v in want.items()):
            return m
    pytest.fail(f"{form}: no analysis with {want}")


def test_closed_forms():
    assert L.prove(_first("लक्ष्मीस्", vibhakti="प्रथमा", vacana="एकवचन")).derivable  # उणादि ई-stem keeps its सु
    imani = _first("इमानि", lemma="इदम्", vibhakti="प्रथमा")
    assert not L.prove(imani).derivable and "7.2.109" in L.prove(imani).note  # listed, vidyut gives इदानि


def test_augmentless_past_after_ma():
    m = _first("भूत्", kind="tinanta", lakara="लुङ्")
    assert L.prove(m).derivable and m.root == "भू"


def test_arsha_voice_is_labelled_not_proved():
    for form, root in (("त्यजामहे", "त्यज्"), ("क्षमेत्", "क्षम्"), ("शृणुध्वम्", "श्रु")):
        m = _first(form, kind="tinanta", source="arsha")
        assert m.root == root and not L.prove(m).derivable and "ārṣa" in L.prove(m).note
    assert not any(m.source == "arsha" for m in L.padas("गच्छति"))


def test_gati_and_cvi_composites():
    for form, lemma in (("प्रादुरासीत्", "प्रादुरस्"), ("नमश्चकार", "नमस्कृ"), ("आविर्भवति", "आविर्भू")):
        m = next(x for x in L.padas(form) if x.kind == "tinanta")
        assert ud.lemma(m) == lemma and L.prove(m).derivable and "गति" in L.prove(m).note
    assert any(ud.lemma(m) == "वशीकृ" for m in L.padas("वशीकृतम्"))  # च्वि: 5.4.50, 7.4.32


def test_dictionary_stems_and_kap():
    m = _first("हेहयस्", source="dictionary")
    assert m.lemma == "हेहय" and L.prove(m).derivable
    assert any(s.source == "dictionary" for s in L.stems("हेहय"))
    assert _first("लक्ष्मीकस्", lemma="लक्ष्मीक").quality == 2  # कप् after ई at the end of a बहुव्रीहि (5.4.153)
    assert not L.prove(L.generated("ग्लोकस्य")[0]).derivable  # a made-up stem is still not a word


def test_spelling_variants():
    assert _first("चिछेद", kind="tinanta").root == "छिद्"  # छ after a vowel is च्छ (6.1.73)
    assert L.padas("किन्तु") and L.padas("पत्रम्")


def test_stem_rules():
    assert segmenter.word_score("कुरु", True, 0) is not None and segmenter.word_score("आदि", True, 0) is not None
    assert segmenter.word_score("अस्ति", True, 0) is None and segmenter.word_score("राजन्", True, 0) is None
    assert segmenter.word_score("अन्", True, 0) is not None and L.stems("क्लिष्ट")
