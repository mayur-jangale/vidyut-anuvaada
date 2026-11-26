"""Mapping of Morph to DCS conventions."""

from mayur import ud
from mayur.model import Morph


def noun(form="रामस्", lemma="राम", **kw):
    base = dict(form=form, lemma=lemma, kind="subanta", linga="पुंलिङ्ग", vibhakti="प्रथमा", vacana="एकवचन")
    return Morph(**{**base, **kw})


def test_nominal_features():
    assert ud.feats(noun()) == {"Case": "Nom", "Gender": "Masc", "Number": "Sing"}
    assert ud.lemma(noun()) == "राम"


def test_finite_verb():
    m = Morph(form="परिपप्रच्छ", lemma="परिप्रच्छ्", kind="tinanta", root="प्रच्छ्", prefixes=("परि",),
              lakara="लिट्", purusha="प्रथमपुरुष", vacana="एकवचन", prayoga="कर्तरि")
    assert ud.lemma(m) == "परिप्रच्छ्"
    assert ud.feats(m) == {"Tense": "Past", "Mood": "Ind", "Person": "3", "Number": "Sing"}
    assert ud.upos(m) == "VERB"


def test_lakara_table():
    assert ud.LAKARA_TENSE_MOOD["लट्"] == ("Pres", "Ind")
    assert ud.LAKARA_TENSE_MOOD["लङ्"] == ("Impf", "Ind")
    assert ud.LAKARA_TENSE_MOOD["विधिलिङ्"] == ("Pres", "Opt")
    assert ud.LAKARA_TENSE_MOOD["लोट्"] == ("Pres", "Imp")


def test_participle_lemma_is_prefix_plus_root():
    m = noun("निरतम्", "निरत", vibhakti="द्वितीया", root="रम्", prefixes=("नि",), krt="क्त")
    assert ud.lemma(m) == "निरम्"
    assert ud.feats(m) == {"VerbForm": "Part", "Case": "Acc", "Gender": "Masc", "Number": "Sing"}


def test_nonfinite_and_compound_member():
    absolutive = Morph(form="कृत्वा", lemma="कृ", kind="avyaya", root="कृ", krt="क्त्वा")
    assert ud.feats(absolutive) == {"VerbForm": "Conv"}
    assert ud.feats(Morph(form="कर्तुम्", lemma="कृ", kind="avyaya", root="कृ", krt="तुमुन्")) == {"VerbForm": "Inf"}
    assert ud.feats(Morph(form="तपस्", lemma="तपस्", kind="stem")) == {"Case": "Cpd"}


def test_lemma_equivalence():
    assert ud.lemma(noun("कस्", "किम्")) == "क"
    assert ud.lemma(noun("अहम्", "अस्मद्")) == "मद्"


def test_tag_key_roundtrip():
    key = ud.tag_key("राम", "NOUN", {"Number": "Sing", "Case": "Nom", "Gender": "Masc"})
    assert key == "राम|NOUN|Case=Nom|Gender=Masc|Number=Sing"
    assert ud.parse_tag_key(key) == ("राम", "NOUN", {"Case": "Nom", "Gender": "Masc", "Number": "Sing"})


def test_feats_agree_ignores_unasserted():
    assert ud.feats_agree({"Case": "Nom"}, {"Case": "Nom", "Number": "Sing"})
    assert not ud.feats_agree({"Case": "Acc"}, {"Case": "Nom"})


def test_feats_agree_ignores_features_the_corpus_omits():
    ours = {"Case": "Nom", "Gender": "Masc", "Number": "Sing"}
    assert ud.feats_agree(ours, {"Case": "Nom", "Number": "Sing"})
    assert not ud.feats_agree(ours, {"Case": "Acc", "Number": "Sing"})


def test_citation_conventions():
    assert ud.canonical_lemma("हनुमन्त्") == "हनुमत्"
    adverb = Morph(form="भृशम्", lemma="भृश", kind="subanta", linga="नपुंसकलिङ्ग", vibhakti="द्वितीया", vacana="एकवचन")
    assert ud.same_lemma(adverb, "भृशम्", "ADV")
    assert not ud.same_lemma(adverb, "भृशम्", "NOUN")
    assert ud.same_feats(adverb, "ADV", {})
    assert not ud.same_feats(adverb, "NOUN", {"Case": "Nom", "Gender": "Neut", "Number": "Sing"})
    assert ud.compared_features("ADV", {"Case": "Voc"}) == ()


def test_features_the_gold_omits_are_not_scored():
    pronoun = Morph(form="अहम्", lemma="अस्मद्", kind="subanta", linga="पुंलिङ्ग", vibhakti="प्रथमा", vacana="एकवचन")
    assert ud.same_feats(pronoun, "PRON", {"Case": "Nom", "Number": "Sing"})
    assert not ud.same_feats(pronoun, "PRON", {"Case": "Acc", "Number": "Sing"})
