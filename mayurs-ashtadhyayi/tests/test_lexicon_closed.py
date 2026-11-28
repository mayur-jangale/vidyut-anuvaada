"""Closed paradigms, क्त readings, feminine stems and citation conventions (all Devanagari)."""

from __future__ import annotations

import pytest

from mayur import lexicon as L
from mayur import ud


def _has(form: str, lemma: str, upos: str, feats: dict[str, str], stem: bool = False) -> list:
    ms = L.stems(form) if stem else L.padas(form)
    return [m for m in ms if ud.same_lemma(m, lemma, upos) and (stem or ud.same_feats(m, upos, feats))]


@pytest.mark.parametrize("form,feats", [
    ("पुमान्", {"Case": "Nom", "Gender": "Masc", "Number": "Sing"}),
    ("पुमांसम्", {"Case": "Acc", "Gender": "Masc", "Number": "Sing"}),
])
def test_pums_forward_derived(form, feats):
    good = _has(form, "पुंस्", "NOUN", feats)
    assert good and L.prove(good[0]).derivable


def test_tva_member_is_special_not_derivable():
    good = _has("त्वात्", "त्व", "NOUN", {"Case": "Abl", "Gender": "Neut", "Number": "Sing"})
    assert good and good[0].source == "special"
    proof = L.prove(good[0])
    assert not proof.derivable and "5.1.119" in proof.note
    assert L.padas("त्वम्")[0].lemma == "युष्मद्"  # the pronoun stays first


def test_kandvadi_mahiyate():
    good = _has("महीयते", "महीय्", "VERB", {"Mood": "Ind", "Tense": "Pres", "Person": "3", "Number": "Sing"})
    assert good and L.prove(good[0]).derivable


@pytest.mark.parametrize("form,lemma", [("वध्यस्", "वध्"), ("अवधीत्", "वध्"), ("गोपाय", "गोपाय्"),
                                        ("गुप्तम्", "गुप्"), ("जिगीषन्ति", "जिगीष्"), ("व्यधमत्", "विधम्"),
                                        ("ऋच्छति", "ऋछ्")])
def test_verbal_citation(form, lemma):
    assert lemma in {ud.lemma(m) for m in L.padas(form)}


def test_ahar_and_om_aliases():
    assert "अहर्" in {ud.lemma(m) for m in L.padas("अहनि")}
    assert "ॐ" in {ud.lemma(m) for m in L.padas("ओम्")}


@pytest.mark.parametrize("form,lemma", [("सत्कृत्य", "सत्कृ"), ("नमस्कृत्य", "नमस्कृ"), ("अलंकृतम्", "अलंकृ")])
def test_gati_prefixes(form, lemma):
    good = [m for m in L.padas(form) if ud.lemma(m) == lemma]
    assert good and L.prove(good[0]).derivable


@pytest.mark.parametrize("form,lemma", [("प्रहृष्ट", "प्रहृष्"), ("परिशुद्ध", "परिशुध्"), ("मूढ", "मुह्")])
def test_kta_stem_of_kosha_adjective(form, lemma):
    good = [m for m in L.stems(form) if m.krt == "क्त" and ud.lemma(m) == lemma]
    assert good and L.prove(good[0]).derivable


def test_kta_pada_of_kosha_adjective():
    good = [m for m in L.padas("विस्तीर्णस्") if m.krt == "क्त"]
    assert good and ud.lemma(good[0]) == "विस्तृ" and L.prove(good[0]).derivable


@pytest.mark.parametrize("form,lemma,feats", [
    ("सुन्दरास्", "सुन्दर", {"Case": "Nom", "Gender": "Fem", "Number": "Plur"}),
    ("मुखी", "मुख", {"Case": "Nom", "Gender": "Fem", "Number": "Sing"}),
    ("साध्वीम्", "साधु", {"Case": "Acc", "Gender": "Fem", "Number": "Sing"}),
    ("शिष्याम्", "शिष्या", {"Case": "Acc", "Gender": "Fem", "Number": "Sing"}),
])
def test_feminine_stems(form, lemma, feats):
    good = _has(form, lemma, "ADJ", feats)
    assert good and L.prove(good[0]).derivable


def test_feminine_stem_helper():
    assert L.feminine_stem("सुमुख", "सुमुख्या") == "सुमुखी"
    assert L.feminine_stem("शिष्य", "शिष्यया") == "शिष्या"
    assert L.feminine_stem("लता", "लताम्") == "लता"


@pytest.mark.parametrize("form,lemma", [("भुजङ्ग", "भुजंग"), ("प्राच्", "प्राञ्च्"), ("तिर्यञ्च्", "तिर्यञ्च्")])
def test_stems_spelling_and_anc(form, lemma):
    assert _has(form, lemma, "NOUN", {}, stem=True)


def test_miss_stays_cheap():
    import time

    L.padas("रामस्")
    L.padas("ख्घ्रट्लक")  # one unknown form first: the tables an unknown form needs are loaded once
    L.stems("ख्घ्रट्लक")
    forms = ["ग्घ्रप्ल" + c for c in "कखगघचजटडतदनपबमयरलवशसह"]
    start = time.perf_counter()
    for f in forms:
        L.padas(f)
        L.stems(f)
    assert (time.perf_counter() - start) / len(forms) < 0.002


def test_kta_after_restored_sha():
    good = [m for m in L.padas("विषण्णस्") if m.krt == "क्त"]
    assert good and ud.lemma(good[0]) == "विषद्" and L.prove(good[0]).derivable


def test_generated_fallback_names():
    assert any(m.lemma == "तुम्बरु" and m.vibhakti == "षष्ठी" for m in L.generated("तुम्बरोस्"))
    assert any(m.lemma == "शण्डामर्क" and m.vacana == "द्विवचन" for m in L.generated("शण्डामर्कौ"))
    assert L.generated("सर") == ()  # never for forms shorter than four sounds
