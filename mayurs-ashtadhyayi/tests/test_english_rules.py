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


# ---------------------------------------------------------------- round 4: verse-style phrases (made-up sentences)

def pron(form, lemma, gloss, role, head, vib="प्रथमा", linga="पुंलिङ्ग"):
    return w(form, "subanta", gloss, role, head, lemma=lemma, vacana=SG, vibhakti=vib, linga=linga)


def final(gloss, role, head, stem, krt=None, **kw):
    return w(stem, "subanta", gloss, role, head, lemma=stem, stem=stem, vacana=SG, vibhakti="प्रथमा", krt=krt, **kw)


def test_np_demonstrative_title_name_then_participial_phrase():
    ws = [pron("सः", "तद्", "that", "विशेषण", 2), noun("king", "विशेषण", 2), noun("Daśaratha", "कर्ता", 5),
          w("संयतः", "subanta", "bind", "विशेषण", 2, krt="क्त", vacana=SG, vibhakti="प्रथमा"),
          noun("noose", "करण", 3, vib="तृतीया"), verb("banish", "लिट्", "विवासयामास"),
          noun("Rāma", "कर्म", 5, vib="द्वितीया")]
    lit, flu = say(ws, anvaya=[0, 1, 2, 3, 4, 6, 5])
    assert lit == "That king Daśaratha, bound by noose, banished Rāma."
    assert flu == "That king Daśaratha, bound by the noose, banished Rāma."


def test_adjectives_before_the_noun_and_name_after_a_common_noun():
    ws = [noun("dear", "विशेषण", 1), noun("son", "कर्म", 3, vib="द्वितीया"), noun("Rāma", "विशेषण", 1),
          verb("see", "लिट्", "ददर्श")]
    ws[3] = replace(ws[3], head=None)
    assert say(ws, anvaya=[3, 0, 1, 2])[0] == "[He] saw dear son Rāma."


def test_genitive_of_a_person_is_possessive_and_otherwise_of():
    ws = [noun("Rāma", "सम्बन्ध", 1, vib="षष्ठी"), noun("wife", "कर्म", 2, vib="द्वितीया"), verb("seize", "लिट्", "जहार")]
    ws[2] = replace(ws[2], head=None)
    assert say(ws)[0] == "[He] seized Rāma's wife."
    ws = [noun("forest", "सम्बन्ध", 1, vib="षष्ठी"), noun("tree", "कर्म", 2, vib="द्वितीया"), verb("see", "लिट्", "ददर्श")]
    ws[2] = replace(ws[2], head=None)
    assert say(ws)[0] == "[He] saw tree of forest."


def test_compound_of_three_members_follows_the_bracketing():
    c = Compound(id=0, members=[0, 1, 2], samasa="तत्पुरुष", vigraha="", basis="x; bracketing [पुत्र-पौत्र]-समन्वित (inner द्वन्द्व)")
    ws = [noun("son", "समासपूर्वपद", 2, member=True, compound=0), noun("grandson", "समासपूर्वपद", 2, member=True, compound=0),
          final("accompanied", "विशेषण", 3, "समन्वित", compound=0), noun("king", "कर्ता", 4), verb("go", "लिट्", "जगाम")]
    ws[4] = replace(ws[4], head=None)
    lit, flu = say(ws, [c], anvaya=[3, 0, 1, 2, 4])
    assert lit == "King, accompanied by son and grandson, went."
    assert flu == "The king, accompanied by son and grandson, went."


def test_bahuvrihi_endings_like_and_the_rest_and_for_the_sake_of():
    c = Compound(id=0, members=[0, 1], samasa="बहुव्रीहि", vigraha="")
    ws = [noun("great", "समासपूर्वपद", 1, member=True, compound=0), final("arm", "विशेषण", 2, "बाहु", compound=0),
          noun("Rāma", "कर्ता", 3), verb("go", "लिट्", "जगाम")]
    ws[3] = replace(ws[3], head=None)
    assert say(ws, [c])[0] == "Great-armed Rāma went."
    c = Compound(id=0, members=[0, 1], samasa="तत्पुरुष", vigraha="")
    ws = [noun("sun", "समासपूर्वपद", 1, member=True, compound=0), final("like", "विशेषण", 2, "संनिभ", compound=0),
          noun("Rāma", "कर्ता", 3), verb("go", "लिट्", "जगाम")]
    ws[3] = replace(ws[3], head=None)
    assert say(ws, [c])[0] == "Rāma, like sun, went."
    ws = [noun("tree", "समासपूर्वपद", 1, member=True, compound=0), final("beginning", "कर्म", 3, "आदि", compound=0),
          noun("Rāma", "कर्ता", 3), verb("see", "लिट्", "ददर्श")]
    ws[3] = replace(ws[3], head=None)
    assert say(ws, [c], anvaya=[2, 3, 0, 1])[0] == "Rāma saw tree and the rest."


def test_taddhita_is_one_word_in_both_lines():
    c = Compound(id=0, members=[0, 1], samasa="तद्धित", vigraha="पात्रस्य भावः")
    ws = [noun("vessel", "समासपूर्वपद", 1, member=True, compound=0), noun("ness", "कर्ता", 2, compound=0),
          verb("go", "लट्", "गच्छति")]
    ws[2] = replace(ws[2], head=None)
    lit, flu = say(ws, [c])
    assert lit == "Vesselness goes." and flu == "Vesselness goes."


def test_epithet_list_has_one_copula_commas_and_and_before_the_last():
    ws = [noun("Rāma", "कर्ता", None), noun("brave", "विधेय", 0), noun("wise", "विधेय", 0), noun("kind", "विधेय", 0)]
    lit, flu = say(ws)
    assert flu == "Rāma is brave, wise and kind."


def test_relative_correlative_pair_reads_he_who():
    ws = [pron("यः", "यद्", "who", "कर्ता", 1), verb("read", "लट्", "पठति", head=None),
          pron("सः", "तद्", "he", "कर्ता", 3), verb("obtain", "लट्", "लभते", head=None),
          noun("happiness", "कर्म", 3, vib="द्वितीया")]
    lit, flu = say(ws, anvaya=[0, 1, 2, 4, 3])
    assert lit == "He who reads, obtains happiness." and flu == "He who reads, obtains happiness."


def test_when_then_and_as_so_pairs_join_with_a_comma():
    ws = [w("यदा", "avyaya", "when", "अव्यय", 2), noun("Rāma", "कर्ता", 2), verb("go", "लट्", "गच्छति", head=None),
          w("तदा", "avyaya", "then", "अव्यय", 5), noun("Sītā", "कर्ता", 5), verb("weep", "लट्", "रोदिति", head=None)]
    lit, flu = say(ws)
    assert lit == "When Rāma goes, then Sītā weeps."


def test_iti_quotes_the_clause_and_the_verb_of_saying_stays_outside():
    ws = [noun("Rāma", "कर्ता", 4), pron("अहम्", "अस्मद्", "I", "कर्ता", 2, linga=None),
          w("गच्छामि", "tinanta", "go", "क्रिया", 4, lakara="लट्", prayoga="कर्तरि", purusha="उत्तमपुरुष", vacana=SG),
          w("इति", "avyaya", "thus", "अव्यय", 2), verb("say", "लङ्", "अवदत्", head=None)]
    lit, flu = say(ws, anvaya=[0, 1, 2, 3, 4])
    assert lit == "Rāma said, “I go.”" and flu == "Rāma said, “I go.”"


def test_unrendered_particles_are_visible_and_only_those():
    from mayur import fluent_checks as fc
    assert {"एव", "हि", "वै", "तु", "ह", "खलु", "किल", "नु"} <= set(fc.UNRENDERED_PARTICLES)
    assert "च" not in fc.UNRENDERED_PARTICLES and "न" not in fc.UNRENDERED_PARTICLES
    ws = [noun("Rāma", "कर्ता", 2), w("हि", "avyaya", "indeed", "अव्यय", 2), verb("go", "लट्", "गच्छति", head=None)]
    lit, flu = say(ws)
    assert lit == "Rāma indeed goes." and flu == "Rāma goes."


def test_absolutive_present_participle_and_locative_absolute():
    ws = [noun("Rāma", "कर्ता", 3), w("गत्वा", "avyaya", "go", "पूर्वकालक्रिया", 3, krt="क्त्वा"),
          w("खादन्", "subanta", "eat", "विशेषण", 0, krt="शतृ", vacana=SG, vibhakti="प्रथमा"), verb("stand", "लट्", "तिष्ठति", head=None)]
    lit, flu = say(ws, anvaya=[1, 0, 2, 3])
    assert lit == "Having gone, Rāma, eating, stands."
    ws = [noun("Rāma", "भावलक्षण", 3, vib="सप्तमी"), w("गते", "subanta", "go", "विशेषण", 0, krt="क्त", vacana=SG, vibhakti="सप्तमी"),
          noun("Sītā", "कर्ता", 3), verb("weep", "लङ्", "अरोदीत्", head=None)]
    lit, flu = say(ws, anvaya=[0, 1, 2, 3])
    assert lit == "When Rāma had gone, Sītā wept."


def test_word_without_gloss_is_iast_in_literal_and_bare_name_in_fluent():
    ws = [noun("Rāma", "कर्ता", 2), Word(form="शुकम्", line=0, start=0, end=1, role="कर्म", head=2),
          verb("see", "लिट्", "ददर्श", head=None)]
    lit, flu = say(ws, anvaya=[0, 2, 1])
    assert lit == "Rāma saw ⟨śukam⟩." and flu == "Rāma saw Śukam."
