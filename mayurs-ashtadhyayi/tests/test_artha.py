"""Meaning of derived words read off their Paninian derivation (mayur.artha)."""

from __future__ import annotations

import dataclasses
import re

import pytest

from mayur import artha, lexicon, lipi
from mayur.model import Morph, Reading, SutraStep, Word, WordProof

_DEVANAGARI = re.compile(r"^[ऀ-ॿ\s,()ऽ]+$")
_KINDS = {"lakara", "prayoga", "krt", "taddhita", "sanadi", "samasanta", "stri", "vibhakti"}


@pytest.fixture(scope="module")
def vidyut_texts() -> dict[str, str]:
    from mayur import resources

    try:
        raw = resources.sutra_texts()
    except FileNotFoundError:
        pytest.skip("vidyut data not installed")
    return {code: lipi.from_code(text).replace("'", "ऽ") for (src, code), text in raw.items() if src == "azwADyAyI"}


def test_table_is_devanagari_and_well_formed() -> None:
    table = artha.table()
    assert len(table) >= 60
    for code, entry in table.items():
        assert re.fullmatch(r"\d\.\d\.\d+", code), code
        assert entry["kind"] in _KINDS, code
        for key in ("sutra", "pratyaya", "sense_sa"):
            assert _DEVANAGARI.match(entry[key]), (code, key, entry[key])
        assert entry["sense_en"] and entry["sense_en"].isascii()


def test_every_rule_number_and_text_agree_with_vidyut(vidyut_texts: dict[str, str]) -> None:
    for code, entry in artha.table().items():
        assert code in vidyut_texts, code
        assert entry["sutra"] == vidyut_texts[code], (code, entry["sutra"], vidyut_texts[code])


def _meaning(form: str, **want: str) -> artha.DerivedMeaning:
    for m in lexicon.padas(form):
        if all(getattr(m, k) == v for k, v in want.items()):
            return artha.derived_meaning(m, lexicon.prove(m))
    pytest.skip(f"{form} {want}: no such analysis in this lexicon")


def _codes(d: artha.DerivedMeaning) -> list[str]:
    return [p.sutra for p in d.parts]


@pytest.mark.parametrize("form, want, codes, sense_sa, english", [
    ("गुणवान्", {"lemma": "गुणवत्"}, ["5.2.94"], "तदस्यास्त्यस्मिन्", "possessing"),
    ("निरतम्", {"krt": "क्त"}, ["3.2.102"], "भूते", "[3.2.102]"),
    ("धावति", {"lakara": "लट्"}, ["3.2.123", "1.3.78"], "वर्तमाने", "runs"),
    ("परिपप्रच्छ", {"lakara": "लिट्"}, ["3.2.115", "1.3.78"], "परोक्षे भूते", "asked"),
    ("श्रोतुम्", {"krt": "तुमुन्"}, ["3.3.10"], "क्रियार्थायां क्रियायाम्", "to "),
    ("श्रुत्वा", {"krt": "क्त्वा"}, ["3.4.21"], "समानकर्तृकयोः पूर्वकाले", "having heard"),
    ("गच्छन्", {"krt": "शतृ"}, ["3.2.123", "1.3.78", "3.2.124"], "वर्तमाने", "going"),
    ("चिकीर्षति", {"lemma": "चिकीर्ष"}, ["3.1.7", "1.3.78", "3.2.123"], "इच्छायाम्", "wishes to"),
    ("गम्यते", {"lemma": "गम्", "prayoga": "कर्मणि"}, ["3.2.123", "1.3.13", "3.1.67"], "भावकर्मणोः", "is gone"),
    ("रक्षिता", {"lakara": "लुट्", "prayoga": "कर्तरि"}, ["3.3.15", "1.3.78"], "अनद्यतने भविष्यति", "will protect"),
    ("आगम्य", {"krt": "ल्यप्"}, ["3.4.21", "7.1.37"], "क्त्वार्थे", "having come"),
])
def test_derived_words(form: str, want: dict, codes: list[str], sense_sa: str, english: str) -> None:
    d = _meaning(form, **want)
    assert _codes(d) == codes
    assert sense_sa in [p.sense_sa for p in d.parts]
    assert english in d.english
    for code in codes:
        assert code in d.english  # every part is cited by its rule number
    assert not re.search(r"[A-Za-z]", d.sanskrit) and " — " in d.sanskrit


def test_causative_cites_hetumati() -> None:
    meanings = [artha.derived_meaning(m, lexicon.prove(m)) for m in lexicon.padas("कारयति") if m.lakara == "लट्"]
    assert meanings
    assert any("3.1.26" in _codes(d) and "हेतुमति" in d.sanskrit for d in meanings)
    assert any(d.english.startswith("causes to") for d in meanings)


def test_tric_agent_rule() -> None:
    # रक्षिता as a तृच् agent noun is not in the kosha; the rule is cited only when it is in a trace
    assert "3.1.133" in artha.table()
    step = lambda code, res: SutraStep("अष्टाध्यायी", code, res)
    m = Morph(form="रक्षिता", lemma="रक्ष्", kind="subanta", stem="रक्षितृ", root="रक्ष्", krt="तृच्")
    proof = WordProof(True, trace=[step("1.3.1", "रक्ष्"), step("3.1.133", "रक्ष् + तृच्")])
    d = artha.derived_meaning(m, proof)
    assert _codes(d) == ["3.1.133"] and d.parts[0].pratyaya == "तृच्" and d.parts[0].sense_sa == "कर्तरि"
    assert d.english == "protector [3.1.133]"


def test_patronymic_when_derived() -> None:
    d = _meaning("दाशरथिस्")
    if not d.parts:
        pytest.skip("दाशरथि is a kosha stem here: its trace has no तद्धित rule")
    assert "4.1.95" in _codes(d)


def test_no_proof_and_plain_words_give_nothing() -> None:
    plain = Morph(form="रामस्", lemma="राम", kind="subanta")
    assert artha.derived_meaning(plain, None) == artha.EMPTY
    assert artha.derived_meaning(None, None).english == ""
    assert _meaning("च").english == ""


def test_fields_without_trace_name_the_rule() -> None:
    m = Morph(form="गतम्", lemma="गम्", kind="subanta", stem="गत", root="गम्", krt="क्त")
    d = artha.derived_meaning(m, None)
    assert _codes(d) == ["3.2.102"] and "[3.2.102]" in d.english
    assert artha.derived_meaning(dataclasses.replace(m, krt=None), WordProof(False)) == artha.EMPTY


def test_annotate_fills_only_derived_meaning() -> None:
    m = lexicon.padas("गुणवान्")[0]
    words = [Word(form="गुणवान्", line=0, start=0, end=6, analyses=[m], proof=lexicon.prove(m), gloss="virtuous"),
             Word(form="च", line=0, start=6, end=7, gloss="and")]
    reading = Reading(words=words, translation="x")
    out = artha.annotate(reading)
    assert out is not reading and out.translation == "x"
    assert out.words[0].derived_meaning.startswith("possessing") and "[5.2.94]" in out.words[0].derived_meaning
    assert out.words[1].derived_meaning == ""
    for before, after in zip(reading.words, out.words):
        assert dataclasses.replace(after, derived_meaning="") == before
    assert reading.words[0].derived_meaning == ""  # the input is not mutated
