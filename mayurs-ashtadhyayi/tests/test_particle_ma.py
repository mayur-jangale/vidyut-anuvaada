"""मा as the prohibitive particle or the enclitic of माम्; the two objects of a causative; ablative or
genitive with a verb of moving; a root's English by its class; first-person imperatives without guṇa."""

import pytest

from mayur import bridge, lexicon, pipeline


def _reading(text):
    return pipeline.analyze_verse(text).readings[0]


def _roles(text):
    return [(w.form, w.morph.lemma, w.role, w.head) for w in _reading(text).words]


@pytest.mark.parametrize("text, lemma", [
    ("मा गच्छ", "मा"),            # first in the line: 8.1.18
    ("मा शुचः", "मा"),            # the augmentless aorist: 3.3.175
    ("त्वं मा गच्छ", "मा"),        # right before an imperative: the tagger's choice stands
    ("स मा पश्यति", "अस्मद्"),     # no prohibition with लट्
    ("तमसो मा ज्योतिर्गमय", "अस्मद्"),
])
def test_ma_particle_or_pronoun(text, lemma):
    word = next(w for w in _reading(text).words if w.form == "मा")
    assert word.morph.lemma == lemma


def test_two_ma_before_an_aorist():
    words = _reading("मा मा हिंसीः").words
    assert [w.morph.lemma for w in words[:2]] == ["मा", "अस्मद्"]
    assert (words[1].role, words[1].head) == ("कर्म", 2)


def test_pronoun_reading_is_noted_with_the_other():
    notes = _reading("तमसो मा ज्योतिर्गमय").notes
    assert any("8.1.23" in n and "prohibitive" in n for n in notes)


@pytest.mark.parametrize("text", ["तमसो मा ज्योतिर्गमय", "मृत्योर्मा अमृतं गमय"])
def test_causative_of_going_has_two_objects_and_a_source(text):
    words = _reading(text).words
    assert [(w.morph.vibhakti, w.role, w.head) for w in words[:3]] == [
        ("पञ्चमी", "अपादान", 3), ("द्वितीया", "कर्म", 3), ("द्वितीया", "कर्म", 3)]


def test_two_objects_of_a_causative_that_differ_in_gender():
    """ग्रामम् beside माम्: the other कर्म of the causative (1.4.52), not an apposition of the pronoun. Two nouns
    alike in gender and number (शिष्यम् धर्मम्) stay one phrase: a split lowered the validation set."""
    assert [(r, h) for _, _, r, h in _roles("रामः मां ग्रामं गमयति")][1:3] == [("कर्म", 3), ("कर्म", 3)]
    assert _roles("रामः वीरं रावणं हन्ति")[1][2:] == ("विशेषण", 2)


@pytest.mark.parametrize("text, case", [
    ("गुरोः आगच्छति शिष्यः", "पञ्चमी"),          # no noun next to it, a verb of moving
    ("गुरोः गृहं गच्छति शिष्यः", "षष्ठी"),        # a noun follows: it belongs to it
    ("पुत्रो रामस्य गच्छति", "षष्ठी"),            # no ablative reading of the form
])
def test_ablative_or_genitive_with_a_verb_of_moving(text, case):
    word = next(w for w in _reading(text).words if w.morph.lemma in ("गुरु", "राम"))
    assert word.morph.vibhakti == case


def test_base_root_of_a_causative():
    found = [m for m in lexicon.padas("गमयति") if m.kind == "tinanta"]
    assert "गम्" in {bridge.base_root(m) for m in found} and all(bridge.is_causative(m) for m in found)
    plain = next(m for m in lexicon.padas("चोरयति") if m.kind == "tinanta")
    assert not bridge.is_causative(plain)


@pytest.mark.parametrize("text, gloss", [
    ("शिवः लोकं पाति", "protect"), ("रामः जलं पिबति", "drink"), ("योगी सिद्धिम् अश्नुते", "attain"),
    ("बालः फलम् अश्नाति", "eat"), ("सः धनं विन्दति", "find"), ("नारी वस्त्रं वस्ते", "wear"),
    ("वीरः शरम् अस्यति", "throw"), ("वायुः वाति", "blow"), ("सः भूमिं मिमीते", "measure"),
    ("कृषकः बीजानि किरति", "scatter"), ("रामः जलं पास्यति", "drink"),  # पास्यति: the form does not decide the class
])
def test_root_is_glossed_by_its_class(text, gloss):
    assert _reading(text).words[-1].gloss == gloss


def test_first_person_imperative_without_guna_is_labelled():
    found = [m for m in lexicon.padas("विद्विषावहै") if m.kind == "tinanta"]
    assert found and found[0].source == "arsha" and found[0].purusha == "उत्तमपुरुष"
    proof = lexicon.prove(found[0])
    assert not proof.derivable and "3.4.92" in proof.note and "द्वेषावहै" in proof.note
    assert all(m.source != "arsha" for m in lexicon.padas("द्वेषावहै"))


def test_epic_imperative_of_bru_is_labelled_with_its_rule_form():
    found = [m for m in lexicon.padas("ब्रवीहि") if m.kind == "tinanta"]
    assert found and found[0].source == "arsha" and found[0].root == "ब्रू"
    assert "ब्रूहि" in lexicon.prove(found[0]).note
    assert [m for m in lexicon.padas("प्रब्रवीहि") if m.kind == "tinanta" and m.source == "arsha"]


@pytest.mark.parametrize("text, english", [
    ("रामः रावणम् अहनत्", "Rāma killed Rāvaṇa."),             # a labelled form, inflected by its analysis
    ("मा शुचः", "Do not grieve."),                           # मा with the aorist: a prohibition (3.3.175)
    ("मा मा हिंसीः", "Do not harm me."),
    ("न सः अगच्छत्", "He did not go."),                       # the plain past stays a statement
    ("तमसो मा ज्योतिर्गमय", "Send me to light from darkness."),  # the goal of a causative of going
    ("रामः मां ग्रामं गमयति", "Rāma sends me to village."),
])
def test_english_of_the_new_readings(text, english):
    assert _reading(text).translation == english


def test_two_locative_nouns_are_two_settings():
    """सङ्ख्ये रथोपस्थे (Gītā 1.47): "in battle, on the chariot seat", not one phrase; an adjective stays with its noun."""
    words = _reading("एवमुक्त्वार्जुनः सङ्ख्ये रथोपस्थ उपाविशत् । विसृज्य सशरं चापं शोकसंविग्नमानसः").words
    verb = next(i for i, w in enumerate(words) if w.form == "उपाविशत्")
    assert [(w.role, w.head) for w in words if w.form in ("सङ्ख्ये", "रथोपस्थे")] == [("अधिकरण", verb)] * 2
    assert _roles("रम्ये वने मृगः चरति")[0][2:] == ("विशेषण", 1)
