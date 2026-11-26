import pytest

from mayur import lexicon as L

PADAS = ("वाल्मीकिस् नारदम् परिपप्रच्छ निरतम् तपस्वी विदाम् वरम् कस् नु अस्मिन् साम्प्रतम् सांप्रतम् लोके "
         "गुणवान् च वीर्यवान् कृतज्ञस् वाक्यस् व्रतस् अहम् मे त्वम् असि इच्छामि श्रोतुम् ज्ञातुम् हि बिभ्यति "
         "देवास् श्वा इतस् श्वेतस् धावति पुंगवम् पुङ्गवम् पर्यपृच्छत् प्रत्युवाच उपागमत्").split()
STEMS = "तपस् स्वाध्याय वाक् मुनि धर्म सत्य दृढ जित जात महा अ".split()


@pytest.mark.parametrize("form", PADAS)
def test_pada_analysed_and_proved(form):
    ms = L.padas(form)
    assert ms and ms[0].quality >= 2
    assert any(L.prove(m).derivable for m in ms[:3])


@pytest.mark.parametrize("form", STEMS)
def test_stem_analysed_and_proved(form):
    ms = L.stems(form)
    assert ms and all(m.kind == "stem" for m in ms)
    proof = L.prove(ms[0])
    assert proof.derivable and "2.4.71" in proof.note


def test_paripapraccha_prefixed():
    m = L.padas("परिपप्रच्छ")[0]
    assert m.kind == "tinanta" and m.lemma == "परिप्रच्छ्" and m.prefixes == ("परि",)
    assert m.lakara == "लिट्" and m.purusha == "प्रथमपुरुष" and m.vacana == "एकवचन"
    proof = L.prove(m)
    assert proof.derivable and proof.derived_form == "परिपप्रच्छ"
    assert all(step.code[0].isdigit() for step in proof.trace)


def test_niratam_krdanta():
    m = L.padas("निरतम्")[0]
    assert (m.lemma, m.stem, m.root, m.krt) == ("निरम्", "निरत", "रम्", "क्त")
    assert m.root_gloss


def test_junk_last_and_quality():
    ms = L.padas("तपस्")
    assert ms[-1].quality <= ms[0].quality
    assert L.padas("वाल्मीकिस्")[0].linga == "पुंलिङ्ग"


def test_devanagari_only():
    import re
    for form in ("निरतम्", "परिपप्रच्छ", "तपस्वी"):
        for m in L.padas(form):
            for v in (m.lemma, m.stem, m.linga, m.vibhakti, m.krt, m.dhatu, m.lakara):
                assert not v or not re.search(r"[A-Za-z]", v)
        for step in L.prove(L.padas(form)[0]).trace:
            assert not re.search(r"[A-Za-z]", step.source + step.result)


def test_nonwords():
    assert L.padas("क्ष्ज्ञ्") == ()
    assert not L.is_pada("क्ष्ज्ञ्") and L.is_pada("च") and L.is_stem("धर्म") and not L.is_stem("धर्मस्")


def test_generated():
    ms = L.generated("रामेण")
    assert ms and ms[0].source == "generated" and ms[0].vibhakti == "तृतीया"
    assert L.prove(ms[0]).derivable
