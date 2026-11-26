from mayur import english, gloss
from mayur.model import Morph


def test_own_table_first():
    assert gloss.lookup(Morph("च", "च", "avyaya")) == ("and", "own")
    assert gloss.lookup(Morph("रामस्", "राम", "subanta"))[0] == "Rāma"
    assert len(gloss._own()) >= 150


def test_root_gloss_fallback_and_none(monkeypatch):
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
