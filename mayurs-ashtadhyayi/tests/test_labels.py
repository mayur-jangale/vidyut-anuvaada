from __future__ import annotations

import pytest

from mayur import labels as LB
from mayur import lexicon as L


@pytest.mark.parametrize(
    "value, text",
    [("praTamA", "nominative"), ("puM", "masculine"), ("la~w", "present (laṭ)"), ("kartari", "active"),
     ("li~w", "perfect (liṭ)"), ("bahu", "plural"), ("uttama", "1st person"), ("samboDanam", "vocative")],
)
def test_english(value, text):
    assert LB.english(value) == text


def test_english_unknown_passthrough():
    assert LB.english("zzz") == "zzz"


def _m(form, **want):
    return next(m for m in L.analyses(form) if all(getattr(m, k) == v for k, v in want.items()))


def test_describe_nominal_and_verb():
    assert LB.describe(_m("nAradam", lemma="nArada", linga="puM")) == "masc. acc. sg. of nārada"
    d = LB.describe(_m("paripapracCa", kind="tinanta"))
    assert d.startswith("3rd sg. perfect (liṭ) active") and d.endswith("pari-pracch")


def test_ud_noun():
    m = _m("nAradam", lemma="nArada", linga="puM")
    assert LB.ud_feats(m) == {"Case": "Acc", "Gender": "Masc", "Number": "Sing"}
    assert LB.ud_lemma(m) == "nārada"


def test_ud_verb_matches_dcs():
    m = _m("paripapracCa", kind="tinanta")
    assert LB.ud_feats(m) == {"Tense": "Past", "Mood": "Ind", "Person": "3", "Number": "Sing"}
    assert LB.ud_lemma(m) == "paripracch"
    m = _m("abravIt", kind="tinanta")
    assert LB.ud_feats(m)["Tense"] == "Impf"


def test_ud_participle_lemma_under_verb():
    m = _m("niratam", krt="kta", linga="puM", vibhakti="dvitIyA")
    assert LB.ud_lemma(m) == "niram"
    assert LB.ud_feats(m) == {"Case": "Acc", "Gender": "Masc", "Number": "Sing", "VerbForm": "Part"}


def test_ud_conv_inf_cpd_pronoun():
    assert LB.ud_feats(_m("gatvA", kind="avyaya")) == {"VerbForm": "Conv"}
    assert LB.ud_feats(_m("Srotum", kind="avyaya")) == {"VerbForm": "Inf"}
    assert LB.ud_feats(L.stem_analyses("muni")[0]) == {"Case": "Cpd"}
    m = L.analyses("aham")[0]
    assert LB.ud_lemma(m) == "mad" and LB.ud_feats(m) == {"Case": "Nom", "Number": "Sing"}


def test_ud_periphrastic_perfect():
    m = _m("kaTayAmAsa", kind="tinanta")
    assert LB.ud_feats(m)["Formation"] == "peri"
    assert LB.ud_lemma(m) == "kathay"
