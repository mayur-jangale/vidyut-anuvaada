"""Forms of usage: analysed and labelled where the rules give another form; proved where two
forward steps give them (denominatives, passive present participles)."""

import pytest

from mayur import lexicon, pipeline, ud


def _find(form, **want):
    return [m for m in lexicon.padas(form) if all(getattr(m, k) == v for k, v in want.items())]


@pytest.mark.parametrize("form, lemma, rule_form", [
    ("अवनामितैस्", "अवनामय्", "अवनमितैः"),   # with an upasarga नम् is मित्: the rules give the short vowel
    ("प्रदत्तास्", "प्रदा", "प्रत्ताः"),         # 7.4.47 अच उपसर्गात्तः
])
def test_prefixed_participle_is_labelled_with_the_rule_form(form, lemma, rule_form):
    found = [m for m in _find(form, krt="क्त") if ud.lemma(m) == lemma]
    assert found, [(ud.lemma(m), m.krt) for m in lexicon.padas(form)]
    proof = lexicon.prove(found[0])
    assert not proof.derivable and rule_form in proof.note


def test_derivable_prefixed_participle_is_not_relabelled():
    found = [m for m in _find("विहितस्", krt="क्त") if ud.lemma(m) == "विधा"]
    assert found and lexicon.prove(found[0]).derivable


@pytest.mark.parametrize("form, lemma", [("छन्नस्", "छद्"), ("आच्छन्नम्", "आच्छद्"), ("चीर्णम्", "चर्")])
def test_listed_adjective_that_is_a_participle_names_its_root(form, lemma):
    found = [m for m in _find(form, krt="क्त") if ud.lemma(m) == lemma]
    assert found and not lexicon.prove(found[0]).derivable


def test_api_without_its_first_vowel():
    found = [m for m in _find("पिनद्धस्", krt="क्त") if m.prefixes[:1] == ("अपि",)]
    assert found and "भागुरि" in lexicon.prove(found[0]).note


def test_absolutive_in_tva_after_an_upasarga_is_arsha():
    found = _find("परिपालयित्वा", krt="क्त्वा")
    assert found and found[0].source == "arsha" and "7.1.37" in lexicon.prove(found[0]).note


@pytest.mark.parametrize("form, lakara", [("वधिष्यामि", "लृट्"), ("वध्यन्ते", "लट्")])
def test_root_of_usage_is_labelled(form, lakara):
    found = _find(form, lakara=lakara)
    assert found and found[0].root == "वध्"
    proof = lexicon.prove(found[0])
    assert not proof.derivable and "2.4.42" in proof.note


@pytest.mark.parametrize("form, lemma, base", [
    ("नमस्यति", "नमस्य्", "नमस् + क्यच्"), ("पुत्रीयति", "पुत्रीय्", "पुत्र + क्यच्"),
    ("श्येनायते", "श्येनाय्", "श्येन + क्यङ्"), ("उत्सुकयन्ति", "उत्सुकय्", "उत्सुक + णिच्"),
])
def test_denominative_is_derived_forward(form, lemma, base):
    found = [m for m in _find(form, kind="tinanta") if m.lemma == lemma and m.dhatu == base]
    assert found, [(m.lemma, m.dhatu) for m in lexicon.padas(form)]
    assert lexicon.prove(found[0]).derivable


def test_no_denominative_beside_a_listed_verb():
    assert not [m for m in lexicon.padas("कारयति") if m.gana == "नामधातु"]
    assert not [m for m in lexicon.padas("धर्माय") if m.kind == "tinanta"]


@pytest.mark.parametrize("form, stem", [("क्रियमाणानि", "क्रियमाण"), ("उच्यमानस्", "उच्यमान"), ("दृश्यमाना", "दृश्यमान")])
def test_passive_present_participle_is_proved_in_two_steps(form, stem):
    found = _find(form, krt="शानच्")
    assert found and found[0].stem == stem
    proof = lexicon.prove(found[0])
    assert proof.derivable and "two steps" in proof.method
    assert {"3.2.124", "7.2.82"} <= {step.code for step in proof.trace}


def test_active_participle_keeps_the_one_step_proof():
    proof = lexicon.prove(_find("कुर्वाणस्", krt="शानच्")[0])
    assert proof.derivable and proof.method == "vidyut-prakriya"


def test_passive_participle_stem_is_a_compound_member():
    assert [m for m in lexicon.stems("भिद्यमान") if m.krt == "शानच्" and m.root == "भिद्"]


@pytest.mark.parametrize("form, lemma, krt", [("अतिक्रामन्", "अतिक्रम्", "शतृ"), ("क्रामन्तम्", "क्रम्", "शतृ")])
def test_kram_participle_with_the_long_vowel(form, lemma, krt):
    found = [m for m in _find(form, krt=krt) if ud.lemma(m) == lemma]
    assert found and "7.3.76" in lexicon.prove(found[0]).note


def test_kram_without_the_long_vowel_is_arsha():
    found = _find("अतिक्रमेत्", lakara="विधिलिङ्")
    assert found and found[0].source == "arsha" and found[0].vacana == "एकवचन"


def test_voice_pair_needs_the_same_person_and_number():
    """क्रामेत् is the regular third singular; क्रामेत (second plural) is no sibling of it."""
    assert all(m.source != "arsha" for m in lexicon.padas("क्रामेत्"))


@pytest.mark.parametrize("form, root", [("गच्छस्व", "गम्"), ("पश्यस्व", "दृश्")])
def test_epic_imperative_in_sva(form, root):
    found = _find(form, lakara="लोट्")
    assert found and found[0].source == "arsha" and found[0].root == root


@pytest.mark.parametrize("form, lemma", [("परिरक्ष", "परिरक्ष्"), ("अन्विष्य", "अन्विष्")])
def test_prefixed_verb_beside_a_listed_noun(form, lemma):
    assert lemma in {ud.lemma(m) for m in lexicon.padas(form) if m.root}


@pytest.mark.parametrize("form, lemma, case", [("दस्युमते", "दस्युमत्", "चतुर्थी"), ("गन्धवाहिने", "गन्धवाहिन्", "चतुर्थी"),
                                               ("सुसंधेस्", "सुसंधि", "पञ्चमी")])
def test_dictionary_stem_with_a_consonant_or_nasal_spelling(form, lemma, case):
    found = [m for m in lexicon.padas(form) if m.lemma == lemma and m.vibhakti == case]
    assert found and found[0].source == "dictionary"


def test_listed_root_noun_is_a_word():
    found = [m for m in lexicon.padas("गीर्भिस्") if m.stem == "गिर्"]
    assert found and found[0].quality >= 2
    assert lexicon.padas("गीर्भिर्")  # as written before a voiced sound


def test_doubled_consonant_spelling():
    found = lexicon.padas("मित्त्रम्")
    assert found and found[0].lemma == "मित्र"
    assert "8.4.47" in lexicon.prove(found[0]).note


def test_sibling_pada_is_taken_and_the_other_named():
    reading = pipeline.analyze_verse("भीष्म उवाच").readings[0]
    assert [w.form for w in reading.words] == ["भीष्मस्", "उवाच"]
    assert any("भीष्मे" in note and "also allows" in note for note in reading.notes)


def test_sibling_swap_keeps_the_proof():
    verse = pipeline.analyze_verse("मूढा जना न जानन्ति")
    assert verse.status == "verified"
    assert verse.readings[0].words[0].morph.vacana == "बहुवचन"
