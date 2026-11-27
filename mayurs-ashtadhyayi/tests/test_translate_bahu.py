"""बहुव्रीहि qualifiers, नञ्-adjectives and chains of absolutives in the English lines (translate_bahu, translate_clause).

Each rule reads the compound type (``Compound.samasa``) and the member classes of the analysis; every rule is
tested on sentences other than the two verses that motivated it, which are tested last."""

import re

import pytest

from mayur import pipeline
from mayur.fluent_checks import check_hyphens, check_supplied
from mayur.fluent_supplied import articles_in_hyphens, unbracketed_possessives


def read(text):
    return pipeline.analyze_verse(text).readings[0]


def types(reading):
    return {c.samasa for c in reading.compounds}


# (sentence, literal line, readable line)
NOUN_BODY_PART = [  # बहुव्रीहि, noun + part of the body
    ("शस्त्रपाणिः राजा वनं गच्छति", "King, with weapon in hand, goes to forest.", "The king, with weapon in hand, goes to the forest."),
    ("गदापाणिः भीमः आगच्छति", "Bhīma, with mace in hand, comes.", "Bhīma, with mace in hand, comes."),
    ("शस्त्रपाणयः पाण्डवाः रणं गच्छन्ति", "Pāṇḍavas, with weapon in hand, go to battle.", "The Pāṇḍavas, with weapon in hand, go to battle."),
    ("पद्मनेत्रः रामः आगच्छति", "Rāma, lotus-eyed, comes.", "Rāma, lotus-eyed, comes."),
]
PARTICIPLE = [  # बहुव्रीहि, क्त participle + noun, optionally a noun before the participle
    ("जितेन्द्रियं मुनिं राजा पश्यति", "King sees sage, [his] sense conquered.", "The king sees the sage, his sense conquered."),
    ("हृष्टमानसः बालकः आगच्छति", "Boy, [his] mind rejoiced, comes.", "The boy, his mind rejoiced, comes."),
    ("मुक्तबन्धनः नरः आगच्छति", "Man, [his] bond released, comes.", "The man, his bond released, comes."),
    ("शोकसंविग्नमानसः नरः आगच्छति", "Man, [his] mind agitated by grief, comes.", "The man, his mind agitated by grief, comes."),
    ("भयसंविग्नमानसः बालकः रोदिति", "Boy, [his] mind agitated by fear, weeps.", "The boy, his mind agitated by fear, weeps."),
]
WITH_SA = [  # बहुव्रीहि with स-
    ("सपुत्रः राजा वनं गच्छति", "King with son goes to forest.", "The king with son goes to the forest."),
    ("सलक्ष्मणः रामः वनं गच्छति", "Rāma with Lakṣmaṇa goes to forest.", "Rāma with Lakṣmaṇa goes to the forest."),
    ("सपुत्रं राजानं नरः पश्यति", "Man sees king with son.", "The man sees the king with son."),
]
ADJECTIVE_NOUN = [  # बहुव्रीहि, adjective + noun
    ("महाबाहुः रामः धनुः गृह्णाति", "Great-armed Rāma seizes bow.", "Great-armed Rāma seizes the bow."),
    ("महाबलः भीमः आगच्छति", "Bhīma of great strength comes.", "Bhīma of great strength comes."),
]
WITHOUT = [  # words glossed "without X"
    ("अशस्त्रः मुनिः वनं गच्छति", "Sage without weapon goes to forest.", "The sage without weapon goes to the forest."),
    ("राजा मामशस्त्रमप्रतीकारं हन्ति", "King kills me, without weapon and without resistance.",
     "The king kills me, without weapon and without resistance."),
]
ABSOLUTIVES = [  # two or more absolutives of one verb: one "having", joined by "and"
    ("रामः वनं गत्वा फलं खादित्वा तिष्ठति", "Having gone to forest and eaten fruit, Rāma stands.",
     "Having gone to the forest and eaten the fruit, Rāma stands."),
    ("बालकः गृहं गत्वा पुस्तकं पठित्वा भोजनं खादित्वा तिष्ठति", "Having gone to house, read book and eaten meal, boy stands.",
     "Having gone to the house, read the book and eaten the meal, the boy stands."),
]


@pytest.mark.parametrize("text,literal,readable", NOUN_BODY_PART + PARTICIPLE + WITH_SA + ADJECTIVE_NOUN + WITHOUT + ABSOLUTIVES)
def test_lines(text, literal, readable):
    r = read(text)
    assert r.translation == literal
    assert r.reworded == readable


@pytest.mark.parametrize("text", [t for t, _, _ in NOUN_BODY_PART + PARTICIPLE + WITH_SA + ADJECTIVE_NOUN])
def test_rule_reads_a_bahuvrihi(text):
    assert "बहुव्रीहि" in types(read(text))


def test_supplied_owner_is_bracketed_in_the_literal_line_only():
    for text, literal, readable in PARTICIPLE:
        r = read(text)
        assert "[his]" in r.translation and "[" not in r.reworded and " his " in r.reworded
        assert check_supplied(r) == []


def test_owner_follows_the_noun_qualified():
    r = read("जितेन्द्रियं मुनिं राजा पश्यति")  # the sage's sense, not the king's: the possessive is of the noun qualified
    assert r.translation.index("sage") < r.translation.index("[his]")


def test_qualifier_comes_after_its_noun():
    for text, _, _ in NOUN_BODY_PART[:2] + PARTICIPLE[:2]:
        t = read(text).translation
        assert t.index(",") > 0 and not t.startswith(("With", "Hand", "Weapon", "Conquer", "Rejoice"))


@pytest.mark.parametrize("text,keeps", [
    ("त्यक्तराज्यः रामः वनं गच्छति", "Abandon-kingdom Rāma"),   # typed कर्मधारय by the compound analysis: never guessed
])
def test_other_types_keep_the_hyphen_form(text, keeps):
    r = read(text)
    assert "बहुव्रीहि" not in types(r)
    assert r.translation.startswith(keeps)


@pytest.mark.parametrize("text,readable", [
    ("धर्मनिष्ठाः पाण्डवाः आगच्छन्ति", "The dharma-devotion Pāṇḍavas come."),  # the article goes before the whole compound
    ("सत्यवादिनः पाण्डवाः आगच्छन्ति", "The truth-speaking Pāṇḍavas come."),
    ("वीरपुत्राः पाण्डवाः आगच्छन्ति", "The hero-son Pāṇḍavas come."),
])
def test_no_article_inside_a_hyphenated_compound(text, readable):
    r = read(text)
    assert r.reworded == readable
    assert not re.search(r"-(the|a|an)\b|\b(the|a|an)-", r.reworded)


def test_hyphen_check_flags_an_article_in_a_compound():
    assert articles_in_hyphens("If weapon-the hand Dhārtarāṣṭras kill") != []
    assert articles_in_hyphens("If the weapon-hand Dhārtarāṣṭras kill") == []


def test_check_functions_report_failures():
    assert [f.code for f in check_hyphens("a-the b")] == ["hyphen"]
    r = read("हृष्टमानसः बालकः आगच्छति")
    assert unbracketed_possessives(r) == []
    bad = type(r)(**{**r.__dict__, "translation": r.translation.replace("[his]", "his")})
    assert [f.code for f in check_supplied(bad)] == ["supplied"]


# ---- the two verses that motivated the rules ------------------------------------------------------------

VERSE_1 = "यदि मामप्रतीकारमशस्त्रं शस्त्रपाणयः । धार्तराष्ट्रा रणे हन्युस्तन्मे क्षेमतरं भवेत्"
VERSE_2 = "एवमुक्त्वार्जुनः सङ्ख्ये रथोपस्थ उपाविशत् । विसृज्य सशरं चापं शोकसंविग्नमानसः"


def test_verse_one():
    r = read(VERSE_1)
    assert r.translation == ("If Dhārtarāṣṭras, with weapon in hand, should kill me, without resistance and without weapon, "
                             "in battle; it should be my greater safety.")
    assert "the Dhārtarāṣṭras, with weapon in hand," in r.reworded and "-the" not in r.reworded


def test_verse_two():
    r = read(VERSE_2)
    assert r.translation.startswith("Having said thus and released bow with arrow, Arjuna, [his] mind agitated by grief, sat")
    assert r.reworded.startswith("Having said thus and released the bow with arrow, Arjuna, his mind agitated by grief, sat")


import pytest as _pytest

from mayur import pipeline as _pipeline


@_pytest.mark.parametrize("text, english", [
    ("हतपुत्रः राजा रोदिति", "The king, his son killed, weeps."),
    ("गतप्राणः वीरः पतति", "The hero, his breath gone, falls."),
    ("भग्नमानसः नरः गच्छति", "The man, his mind broken, goes."),
])
def test_participle_first_compound_that_agrees_with_a_noun_is_a_bahuvrihi(text, english):
    """हत, गत, भग्न are tagged as nouns by the corpus; as first members before a noun, in a compound that
    agrees with another word, they are participles (2.2.24, 2.2.36 निष्ठा)."""
    reading = _pipeline.analyze_verse(text).readings[0]
    assert reading.compounds[0].samasa == "बहुव्रीहि" and reading.reworded == english
