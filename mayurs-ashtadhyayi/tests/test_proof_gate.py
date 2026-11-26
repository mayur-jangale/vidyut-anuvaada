"""The proof gate must never report a form as derived unless a derivation produced that form."""

import pytest

from mayur import lexicon

STEMS = ["महा", "मत्", "त्वत्", "अ", "प्राक्", "वाक्", "तपस्", "धर्म", "राज", "आत्म", "निरत", "मुनि",
         "तपस्वि", "सर्व", "तत्", "सत्य", "दृढ", "जित", "स्वाध्याय"]
PADAS = ["वाल्मीकिस्", "नारदम्", "परिपप्रच्छ", "निरतम्", "धावति", "श्वा", "इतस्", "मे", "एनम्", "श्रियम्",
         "कश्चित्", "गुणवान्", "रक्षिता", "श्रोतुम्"]


@pytest.mark.parametrize("form", STEMS)
def test_member_proof_derives_the_member_form_itself(form):
    for morph in lexicon.stems(form):
        proof = lexicon.prove(morph)
        if proof.derivable:
            assert form in lexicon.nasal_variants(proof.derived_form), (form, morph.lemma, proof.derived_form)


@pytest.mark.parametrize("form", PADAS)
def test_pada_proof_derives_the_pada_itself(form):
    for morph in lexicon.padas(form):
        proof = lexicon.prove(morph)
        if proof.derivable and proof.method.startswith("vidyut-prakriya") and "sandhi" not in proof.method:
            assert form in lexicon.nasal_variants(proof.derived_form), (form, morph.lemma, proof.derived_form)


def test_substitute_member_form_is_not_claimed_as_derived():
    mahat = [m for m in lexicon.stems("महा") if m.lemma == "महत्"]
    assert mahat, "महा should be recognised as the in-compound form of महत्"
    proof = lexicon.prove(mahat[0])
    assert not proof.derivable and "not" in proof.note


def test_words_vidyut_cannot_derive_stay_unproved():
    for form in ("मे", "एनम्", "श्रियम्"):
        special = [m for m in lexicon.padas(form) if m.lemma in ("अस्मद्", "इदम्", "एतद्", "श्री")]
        assert special and not any(lexicon.prove(m).derivable for m in special), form
