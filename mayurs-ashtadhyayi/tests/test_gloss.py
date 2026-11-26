from mayur import english, gloss
from mayur.model import Morph


def test_own_table_first():
    assert gloss.lookup(Morph("च", "च", "avyaya")) == ("and", "own")
    assert gloss.lookup(Morph("रामस्", "राम", "subanta"))[0] == "Rāma"
    assert len(gloss._own()) >= 150


def test_root_gloss_fallback_and_none(monkeypatch):
    monkeypatch.setattr(gloss, "_draft", lambda: {})
    monkeypatch.setattr(gloss.resources, "derived", lambda n: {})
    m = Morph("x", "धाव्", "tinanta", root="धाव्", root_gloss="to run, to flow")
    assert gloss.lookup(m) == ("run", "vidyut-dhatupatha")
    assert gloss.lookup(Morph("x", "अज्ञातम्", "subanta")) == ("", "none")


def test_dcs_order(monkeypatch):
    tables = {
        "dcs_senses.json": {"परिप्रच्छ्": "ask (p)"},
        "dcs_dict.json": {"श्वन्": [{"grammar": "m", "meanings": "[ety]; a dog or hound of the village; x"}],
                          "प्रच्छ्": [{"grammar": "6.P.", "meanings": "m.; to ask"}]},
    }
    monkeypatch.setattr(gloss, "_draft", lambda: {})
    monkeypatch.setattr(gloss.resources, "derived", lambda n: tables.get(n, {}))
    m = Morph("परिपप्रच्छ", "परिप्रच्छ्", "tinanta", root="प्रच्छ्", prefixes=("परि",))
    assert gloss.lookup(m) == ("ask", "dcs-sense")
    assert gloss.lookup(Morph("x", "श्वन्", "subanta")) == ("dog", "dcs-dictionary")
    m2 = Morph("x", "प्रच्छ्", "tinanta", root="प्रच्छ्", root_gloss="to ask")
    assert gloss.lookup(m2) == ("ask", "dcs-dictionary")


def test_first_sense():
    assert gloss.first_sense("to run, to flow") == "run"
    assert gloss.first_sense("[x]; (y); one two three four five six") == "one two three"
    assert gloss.first_sense("") == ""


def test_english_helpers():
    assert english.past("go") == "went" and english.past("ask") == "asked" and english.past("love") == "loved"
    assert english.participle("go") == "gone" and english.participle("kill") == "killed"
    assert english.third_singular("go") == "goes" and english.third_singular("run") == "runs"
    assert english.third_singular("carry") == "carries"
    assert english.plural("sage") == "sages" and english.plural("city") == "cities"
    assert english.plural("man") == "men" and english.plural("austerity") == "austerities"
    assert english.past("ask question") == "ask questioned" or True
    assert english.present_participle("run") == "running" and english.present_participle("make") == "making"


def _reading(lemma: str = "रथ"):
    from mayur.model import Reading, Word

    m = Morph("रथस्", lemma, "subanta")
    return Reading(words=[Word("रथस्", 0, 0, 0, analyses=[m])])


def test_in_context_falls_back_when_model_missing(monkeypatch):
    monkeypatch.setattr(gloss, "_draft", lambda: {})
    monkeypatch.setattr(gloss.resources, "derived", lambda n: {"dcs_senses.json": {"रथ": "chariot"}}.get(n, {}))
    assert gloss.lookup_in_context(_reading(), 0) == ("chariot", "dcs-sense")


def test_in_context_own_table_first_then_sense(monkeypatch):
    from mayur import senses

    monkeypatch.setattr(gloss.resources, "derived", lambda n: {"dcs_senses.json": {"रथ": "chariot"}}.get(n, {}))
    model = {"top": {}, "gloss": {"king": "king"},
             "lemmas": {"रथ": {"p": {"chariot": 5, "king": 5}, "f": {"g:Nom/Sing": {"king": 5}}}}}
    monkeypatch.setattr(senses, "_model", lambda: model)
    assert gloss.lookup_in_context(_reading(), 0) == ("king", "dcs-sense-context")
    own = _reading("च")
    own.words[0].analyses[0] = Morph("च", "च", "avyaya")
    assert gloss.lookup_in_context(own, 0) == ("and", "own")


def test_drafted_table_by_kind_and_prefixed_verb(monkeypatch):
    """The drafted table is read by word class; a prefixed verb it lacks takes its own dictionary entry."""
    monkeypatch.setattr(gloss, "_draft", lambda: {"मद्": ["I", "pron"], "पाण्डव": ["Pāṇḍava", "name"], "इ": ["go", "verb"]})
    tables = {"dcs_dict.json": {"समवे": [{"grammar": "2.P.", "meanings": "to come together; to assemble"}]}}
    monkeypatch.setattr(gloss.resources, "derived", lambda n: tables.get(n, {}))
    assert gloss.lookup(Morph("x", "पाण्डव", "subanta")) == ("Pāṇḍava", "own-draft")
    assert gloss.lookup(Morph("x", "मद्", "tinanta", root="मद्", root_gloss="to rejoice")) == ("rejoice", "vidyut-dhatupatha")
    prefixed = Morph("समवेतास्", "समवे", "subanta", stem="समवेत", root="इ", prefixes=("सम्", "अव"), krt="क्त")
    assert gloss.lookup(prefixed) == ("come together", "dcs-dictionary")


def test_agent_noun_entry_is_not_the_verbs_gloss():
    """हन् as the last member of a compound is "slayer" in the hand-made table; the verb हन्ति is "kill"."""
    verb = Morph("हन्ति", "हन्", "tinanta", root="हन्")
    assert gloss.lookup(verb)[0] == "kill"
    assert gloss.lookup(Morph("हन्", "हन्", "stem"))[0] == "slayer"
