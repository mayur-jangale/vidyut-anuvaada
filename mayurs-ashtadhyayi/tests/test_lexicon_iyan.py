"""Monosyllabic ई/ऊ feminines take इयङ्/उवङ् (6.4.77)."""

from mayur import lexicon
from mayur.lexicon_iyan import iyan_uvan


def test_shri_dhi_bhu_forms_are_analysed():
    cases = {"श्रियम्": ("श्री", "द्वितीया"), "धिया": ("धी", "तृतीया"), "भुवि": ("भू", "सप्तमी"),
             "श्रीणाम्": ("श्री", "षष्ठी"), "भूनाम्": ("भू", "षष्ठी"), "धीनाम्": ("धी", "षष्ठी")}
    for form, (lemma, case) in cases.items():
        found = {(m.lemma, m.vibhakti) for m in lexicon.padas(form)}
        assert (lemma, case) in found, form


def test_wrong_retroflex_and_plain_glide_forms_are_not_offered():
    assert not iyan_uvan("भूणाम्")
    assert not iyan_uvan("श्र्यौ")


def test_the_paradigm_is_not_claimed_as_derived():
    morph = next(m for m in lexicon.padas("श्रियम्") if m.source == "special")
    proof = lexicon.prove(morph)
    assert not proof.derivable and "6.4.77" in proof.note
