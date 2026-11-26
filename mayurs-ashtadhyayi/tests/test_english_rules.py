"""Rules of the English layer on made-up simple sentences (never Ramayana verses 1-20) and the eval proxy."""

from __future__ import annotations

import sys
from dataclasses import replace
from pathlib import Path

import pytest

from mayur import english, fluent, translate
from mayur.model import Compound, Morph, Reading, Word

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "eval"))
import eval_english  # noqa: E402

SG, PL = "एकवचन", "बहुवचन"


def w(form, kind, gloss, role, head, lemma=None, member=False, compound=None, **m):
    return Word(form=form, line=0, start=0, end=1, role=role, head=head, gloss=gloss, in_compound=member,
                compound=compound, analyses=[Morph(form=form, lemma=lemma or form, kind=kind, **m)])


def verb(gloss="go", lakara="लट्", form="गच्छति", head=None, **kw):
    return w(form, "tinanta", gloss, "क्रिया", head, lakara=lakara, prayoga="कर्तरि", purusha="प्रथमपुरुष", vacana=SG, **kw)


def noun(gloss, role, head, form="x", vac=SG, vib="प्रथमा", **kw):
    return w(form, "subanta", gloss, role, head, vacana=vac, vibhakti=vib, **kw)


def say(words, compounds=(), anvaya=None):
    r = Reading(words=words, compounds=list(compounds), anvaya=anvaya if anvaya is not None else list(range(len(words))))
    lit = translate.render(r)
    return lit.translation, fluent.rewrite(lit)[0].reworded


# ---------------------------------------------------------------- english.py

def test_phrasal_verbs_inflect_the_verb_not_the_particle():
    assert english.present_participle("dive into") == "diving into"
    assert english.past("come to") == "came to" and english.third_singular("look around") == "looks around"
    assert english.plural("sage of the gods").startswith("sages of")


def test_no_double_inflection_and_be_participles():
    assert english.participle("bewilder") == "bewildered" == english.participle("be bewildered")
    assert english.past("comforted") == "comforted"
    assert english.participle("arise") == "arisen" and english.past("slay") == "slew"


# ---------------------------------------------------------------- translate_core / fluent

def test_motion_verb_takes_to_before_its_destination():
    lit, flu = say([noun("Rāma", "कर्ता", 2), noun("forest", "कर्म", 2, vib="द्वितीया"), verb("go", "लङ्", head=None)])
    assert lit.startswith("Rāma went to forest") and flu == "Rāma went to the forest."


def test_with_is_the_preposition_not_by_with():
    ws = [noun("Rāma", "कर्ता", 3), noun("Sītā", "करण", 3, vib="तृतीया"),
          w("सह", "avyaya", "with", "अव्यय", 1), verb("go", "लङ्", head=None)]
    lit, flu = say(ws, anvaya=[0, 2, 1, 3])
    assert "with Sītā" in lit and " by " not in lit and flu == "Rāma went with Sītā."


def test_question_word_with_auxiliary():
    ws = [noun("man", "कर्ता", 2, vac=PL), w("किम्", "subanta", "who", "कर्म", 2, lemma="किम्", vacana=SG, vibhakti="द्वितीया"),
          verb("do", "लङ्", "अकुर्वत", None)]
    ws[2] = replace(ws[2], analyses=[replace(ws[2].morph, vacana=PL)])
    lit, flu = say(ws, anvaya=[1, 0, 2])
    assert lit.lower().startswith("what did men do") and lit.endswith("?")


def test_plural_names_and_coordinated_names():
    ws = [noun("man", "कर्ता", 3, vac=PL), noun("Pāṇḍava", "विशेषण", 0, vac=PL),
          w("च", "avyaya", "and", "अव्यय", 1), verb("see", "लङ्", head=None)]
    lit, flu = say(ws, anvaya=[0, 2, 1, 3])
    assert "Men and Pāṇḍavas" in lit and "Men and the Pāṇḍavas" in flu


def test_latin_binomial_is_replaced_by_the_sanskrit_name():
    ws = [noun("Bombax ceiba Linn", "कर्ता", 1, lemma="शाल्मली"), verb("grow", "लट्", head=None)]
    lit, _ = say(ws)
    assert "Linn" not in lit and "Śālmalī" in lit


def test_sentence_initial_capital_does_not_survive_an_article():
    _, flu = say([noun("king", "कर्ता", 1), verb("go", "लट्", head=None)])
    assert flu == "The king goes."


def test_determinative_compound_reads_y_of_x():
    ws = [w("गङ्गा", "stem", "Gaṅgā", "समासपूर्वपद", 1, member=True, compound=0),
          noun("bank", "अधिकरण", 2, vib="सप्तमी", compound=0), verb("stand", "लट्", "तिष्ठति")]
    lit, _ = say(ws, [Compound(id=0, members=[0, 1], samasa="तत्पुरुष")], anvaya=[2, 1, 0])
    assert "bank of Gaṅgā" in lit and "-" not in lit


def test_descriptive_compound_adjective_first_and_copulative_list():
    ws = [w("महा", "stem", "great", "समासपूर्वपद", 1, member=True, compound=0), noun("sage", "कर्ता", 2, compound=0),
          verb("go", "लट्", head=None)]
    assert say(ws, [Compound(id=0, members=[0, 1], samasa="कर्मधारय")])[0].startswith("Great sage goes")
    ws = [w("राम", "stem", "Rāma", "समासपूर्वपद", 2, member=True, compound=0),
          w("लक्ष्मण", "stem", "Lakṣmaṇa", "समासपूर्वपद", 2, member=True, compound=0),
          noun("Bharata", "कर्ता", 3, compound=0), verb("go", "लट्", head=None)]
    assert "Rāma, Lakṣmaṇa and Bharata" in say(ws, [Compound(id=0, members=[0, 1, 2], samasa="द्वन्द्व")])[0]


def test_together_with_bahuvrihi_is_a_preposition():
    ws = [noun("god", "कर्ता", 4, vac=PL), w("स", "avyaya", "with", "समासपूर्वपद", 2, lemma="स", member=True, compound=0),
          noun("Gandharva", "विशेषण", 0, vac=PL, compound=0), verb("go", "लट्", head=None)]
    ws[3] = replace(ws[3], head=None)
    lit, _ = say(ws, [Compound(id=0, members=[1, 2], samasa="बहुव्रीहि")], anvaya=[0, 1, 2, 3])
    assert "with Gandharvas" in lit and " of " not in lit


# ---------------------------------------------------------------- the eval proxy

def test_proxy_metrics():
    assert eval_english.chrf("Rāma went home.", "Rāma went home.") == pytest.approx(100.0)
    assert eval_english.chrf("zzz", "Rāma went home.") == 0.0
    assert eval_english.content_f1("The king went to the forest", "king went forest") == pytest.approx(100.0)
    assert 0 < eval_english.content_f1("king sleeps", "king went") < 100
    assert eval_english.parse_range("21-23,30") == {21, 22, 23, 30}


def test_passive_participle_is_not_a_tense_marker():
    from mayur import fluent_checks as fc
    assert fc.tense_classes("is conveyed", "convey") == {"present"}
    assert fc.tense_classes("was conveyed", "convey") == {"past"}
    assert fc.tense_classes("conveyed", "convey") == {"past"}


# ---------------------------------------------------------------- round 3: plain sentences

def test_passive_kta_with_agent_and_active_kta_motion():
    agent = noun("Rāma", "कर्ता", 2, vib="तृतीया")
    obj = noun("Rāvaṇa", "कर्म", 2)
    kta = w("हतः", "subanta", "kill", "क्रिया", None, krt="क्त", vacana=SG, vibhakti="प्रथमा")
    assert say([agent, obj, kta], anvaya=[0, 1, 2])[0] == "Rāvaṇa was killed by Rāma."
    go = w("गतः", "subanta", "go", "क्रिया", None, krt="क्त", vacana=SG, vibhakti="प्रथमा")
    assert say([noun("Rāma", "कर्ता", 1), go])[0] == "Rāma went."


def test_absolutive_clause_comes_first_and_motion_object_takes_to():
    ws = [noun("Rāma", "कर्ता", 3), noun("village", "कर्म", 2, vib="द्वितीया"),
          w("गत्वा", "avyaya", "go", "पूर्वकालक्रिया", 3, krt="क्त्वा"), verb("eat", "लट्", "खादति")]
    ws[2] = replace(ws[2], head=3)
    ws[1] = replace(ws[1], head=2)
    lit, flu = say(ws, anvaya=[0, 2, 1, 3])
    assert lit.startswith("Having gone to village, Rāma eats") and flu.startswith("Having gone to the village, Rāma eats")


def test_existential_and_time_and_adverb():
    ws = [verb("be", "लट्", "अस्ति"), noun("tree", "कर्ता", 0)]
    assert say(ws, anvaya=[0, 1])[0] == "There is tree."
    ws = [noun("sun", "कर्ता", 2), w("प्रातः", "avyaya", "morning", "अव्यय", 2, lemma="प्रातर्"), verb("rise", "लट्", "उदेति")]
    assert say(ws, anvaya=[0, 1, 2])[0] == "Sun rises in the morning."
    ws = [noun("horse", "कर्ता", 2), w("शीघ्रम्", "subanta", "quick", "अव्यय", 2, vibhakti="द्वितीया", vacana=SG),
          verb("run", "लट्", "धावति")]
    assert say(ws, anvaya=[0, 1, 2])[0] == "Horse runs quickly."


def test_with_dependent_instrument_and_to_for_say_and_bow():
    ws = [noun("Rāma", "कर्ता", 2), noun("Rāvaṇa", "कर्म", 2, vib="द्वितीया"),
          verb("kill", "लट्", "हन्ति"), noun("arrow", "करण", 2, vib="तृतीया")]
    ws[2] = replace(ws[2], head=None)
    lit, flu = say(ws, anvaya=[0, 3, 1, 2])
    assert flu.endswith("with the arrow.") or " with " in flu
    ws = [noun("pupil", "कर्ता", 2), noun("guru", "कर्म", 2, vib="द्वितीया"), verb("bow", "लट्", "नमति")]
    assert say(ws)[0] == "Pupil bows to guru."


def test_predicate_colour_gloss_and_ness_suffix_and_pluralless_fish():
    ws = [noun("crow", "कर्ता", None), noun("Krishna", "विधेय", 0)]
    assert say(ws)[1] == "The crow is black."
    ws = [w("वीर", "stem", "hero", "समासपूर्वपद", 1, member=True, compound=0), noun("ness", "कर्ता", 2, compound=0),
          verb("shine", "लट्", "भाति")]
    lit = say(ws, [Compound(id=0, members=[0, 1], samasa="तद्धित")], anvaya=[0, 1, 2])[0]
    assert "Heroness" in lit
    assert english.plural("fish") == "fish"
