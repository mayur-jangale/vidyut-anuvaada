from mayur import gloss
from mayur.model import Morph


def test_first_sense():
    assert gloss.first_sense("to go; to move; to approach") == "to go, to move"
    assert gloss.first_sense("[gramm.] foo; a (big) horse; lover") == "a horse, lover"
    assert gloss.first_sense("") == ""


def test_override():
    g, src = gloss.lookup(Morph(form="ca", lemma="ca", kind="avyaya"))
    assert (g, src) == ("and", "override")


def test_dcs_lookup():
    if not gloss._dcs_dict():
        return
    g, src = gloss.lookup(Morph(form="tapasvI", lemma="tapasvin", kind="subanta"))
    # override exists for tapasvin; use a word without override
    g, src = gloss.lookup(Morph(form="vIryavAn", lemma="vIryavat", kind="subanta"))
    assert src in ("override", "dcs") and g


def test_dcs_verb_with_preverb():
    if not gloss._dcs_dict():
        return
    m = Morph(form="paripapracCa", lemma="paricCa", kind="tinanta", root="pracC", prefixes=("pari",))
    g, src = gloss.lookup(m)
    assert src == "dcs" and "ask" in g or "interrogate" in g


def test_verb_fallback_to_root_gloss():
    m = Morph(form="zzz", lemma="qqqq", kind="tinanta", root="qqqq", root_gloss="to shine")
    assert gloss.lookup(m) == ("to shine", "vidyut-dhatupatha")


def test_participle_fallback():
    m = Morph(form="zzz", lemma="qqqqta", kind="subanta", root="qqqq", krt="kta", root_gloss="to shine")
    assert gloss.lookup(m) == ("to shine (past participle)", "vidyut-dhatupatha")


def test_unknown():
    assert gloss.lookup(Morph(form="zzz", lemma="qqqqzz", kind="subanta")) == ("", "none") or \
        gloss.lookup(Morph(form="zzz", lemma="qqqqzz", kind="subanta"))[1] == "none"
