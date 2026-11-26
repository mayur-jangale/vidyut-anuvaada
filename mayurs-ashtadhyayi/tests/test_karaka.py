"""Kāraka engine: the rule table, the forward rules (role → case), the lookup built from them,
and the sentence-level check on real readings."""

import pytest
from syntax_fixtures import avyaya, hand, nom, reading, verb

from mayur import karaka
from mayur.karaka_rules import RULES
from mayur.model import Morph

P1, P2, P3, P4, P5, P6, P7 = "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी"
ACTIVE = verb("धावति", "धाव्", "लट्")
PASSIVE = verb("हन्यते", "हन्", "लट्", "कर्मणि")
HATA = Morph(form="हतस्", lemma="हन्", kind="subanta", vibhakti=P1, vacana="एकवचन", linga="पुंलिङ्ग",
             krt="क्त", root="हन्")
GATA = Morph(form="गतस्", lemma="गम्", kind="subanta", vibhakti=P1, vacana="एकवचन", linga="पुंलिङ्ग",
             krt="क्त", root="गम्")
KARTR = Morph(form="कर्ता", lemma="कृ", kind="subanta", vibhakti=P1, vacana="एकवचन", linga="पुंलिङ्ग",
              krt="तृच्", root="कृ")


def _resolve(r):
    from mayur import compounds, shabdabodha
    return shabdabodha.resolve(compounds.annotate(r))


def _lex(items):
    try:
        return _resolve(reading(items))
    except Exception as e:  # lexicon data not installed
        pytest.skip(f"lexicon unavailable: {e}")


def _w(r, form):
    return next(w for w in r.words if w.form == form)


# The table

def test_table_matches_vidyut_sutrapatha():
    try:
        from mayur import lipi, resources
        texts = resources.sutra_texts()
    except Exception as e:
        pytest.skip(f"vidyut data unavailable: {e}")
    source = next(src for src, _ in texts if lipi.from_code(src) == "अष्टाध्यायी")
    for number, rule in RULES.items():
        assert lipi.from_code(texts[(source, number)]) == rule.text, number
    assert len(RULES) >= 45


def test_every_cited_rule_is_in_the_table():
    from mayur import karaka_rules
    cited = {s for _, rules in karaka_rules.UPAPADA_WORDS.values() for s in rules}
    for role in karaka.CASE_ROLES:
        for gov in (ACTIVE, PASSIVE, HATA, GATA, KARTR, nom("सह", "सह", P1), None):
            for lic in karaka.expected_cases(role, gov, nom("मासम्", "मास", P2)):
                cited |= set(lic.sutras)
    assert cited <= set(RULES), cited - set(RULES)


# Forward: role + governor → case

def _cases(role, gov):
    return {lic.vibhakti for lic in karaka.expected_cases(role, gov)}


def test_forward_active_verb():
    assert _cases("कर्ता", ACTIVE) == {P1}
    assert _cases("कर्म", ACTIVE) == {P2}
    agent = karaka.expected_cases("कर्ता", ACTIVE)[0]
    assert agent.sutras == ("1.4.54", "3.4.69", "2.3.46")


def test_forward_passive_verb():
    assert _cases("कर्म", PASSIVE) == {P1}
    assert _cases("कर्ता", PASSIVE) == {P3}
    assert karaka.expected_cases("कर्ता", PASSIVE)[0].sutras == ("1.4.54", "2.3.18")


def test_forward_kta():
    assert _cases("कर्म", HATA) == {P1}  # 3.4.70
    assert P3 in _cases("कर्ता", HATA) and P1 not in _cases("कर्ता", HATA)
    assert P1 in _cases("कर्ता", GATA)  # गत्यर्थ: 3.4.72
    assert any("3.4.72" in lic.sutras for lic in karaka.expected_cases("कर्ता", GATA))
    assert P6 not in _cases("कर्म", HATA)  # 2.3.69 blocks 2.3.65 for निष्ठा


def test_forward_krt_noun_genitive():
    assert P6 in _cases("कर्म", KARTR)
    assert any(lic.sutras[-1] == "2.3.65" for lic in karaka.expected_cases("कर्म", KARTR))


def test_forward_special_definitions():
    duh = verb("दोग्धि", "दुह्", "लट्")
    assert any(lic.sutras == ("1.4.51", "2.3.2") for lic in karaka.expected_cases("कर्म", duh))
    bhi = verb("बिभेति", "भी", "लट्")
    assert any(lic.sutras == ("1.4.25", "2.3.28") for lic in karaka.expected_cases("अपादान", bhi))
    ruc = verb("रोचते", "रुच्", "लट्")
    assert any(lic.sutras == ("1.4.33", "2.3.13") for lic in karaka.expected_cases("सम्प्रदान", ruc))


# Lookup: built from the forward rules

def _roles(dep, gov):
    return {lic.role for lic in karaka.licences(dep, gov)}


def test_licences_per_case():
    assert _roles(nom("रामस्", "राम", P1), ACTIVE) >= {"कर्ता"}
    assert "कर्म" in _roles(nom("वनम्", "वन", P2, "नपुंसकलिङ्ग"), ACTIVE)
    assert _roles(nom("बाणेन", "बाण", P3), ACTIVE) == {"करण"}  # the agent is already expressed
    assert _roles(nom("रामेण", "राम", P3), PASSIVE) == {"कर्ता", "करण"}  # a choice, noted
    assert "सम्प्रदान" in _roles(nom("रामाय", "राम", P4), ACTIVE)
    assert "अपादान" in _roles(nom("वृक्षात्", "वृक्ष", P5), ACTIVE)
    assert "सम्बन्ध" in _roles(nom("रामस्य", "राम", P6), nom("गृहम्", "गृह", P1, "नपुंसकलिङ्ग"))
    assert "अधिकरण" in _roles(nom("वने", "वन", P7, "नपुंसकलिङ्ग"), ACTIVE)
    assert "सम्बोधन" in _roles(nom("राम", "राम", "सम्बोधन"), ACTIVE)


def test_licence_person_and_number():
    lic = [x for x in karaka.licences(nom("रामस्", "राम", P1), ACTIVE) if x.role == "कर्ता"][0]
    assert lic.sutras[-2:] == ("1.4.108", "1.4.22")
    assert "कर्ता" not in _roles(nom("अहम्", "अस्मद्", P1), ACTIVE)  # 1.4.107 wants उत्तम
    assert "कर्ता" not in _roles(nom("रामास्", "राम", P1, vacana="बहुवचन"), ACTIVE)


def test_upapada_licences():
    assert [lic.sutras for lic in karaka.licences(nom("रामाय", "राम", P4), avyaya("नमस्"))] == [("2.3.16",)]
    assert ("2.3.19",) in [lic.sutras for lic in karaka.licences(nom("रामेण", "राम", P3), avyaya("सह"))]
    assert ("2.3.72",) in [lic.sutras for lic in karaka.licences(nom("रामेण", "राम", P3), nom("तुल्यस्", "तुल्य", P1))]


def test_kala_accusative():
    assert any(lic.sutras == ("2.3.5",) for lic in karaka.licences(nom("मासम्", "मास", P2), ACTIVE))


# Whole sentences

def test_shveta_dhavati():
    r = _lex([("श्वेतस्", False), ("धावति", False)])
    w = _w(r, "श्वेतस्")
    assert w.role == "कर्ता" and w.role_sutras[:3] == ("1.4.54", "3.4.69", "2.3.46")
    assert karaka.verify(r) == [] and r.scores["karaka_verified"] == 1.0


def test_passive_kta_sentence():
    r = _lex([("रामेण", False), ("रावणस्", False), ("हतस्", False)])
    assert _w(r, "हतस्").morph.krt == "क्त"
    assert (_w(r, "रावणस्").role, _w(r, "रावणस्").role_sutras[:2]) == ("कर्म", ("1.4.49", "3.4.70"))
    assert (_w(r, "रामेण").role, _w(r, "रामेण").role_sutras) == ("कर्ता", ("1.4.54", "2.3.18"))
    assert karaka.verify(r) == []


def test_double_object():
    r = _lex([("गाम्", False), ("दोग्धि", False), ("पयस्", False)])
    roles = {w.form: (w.role, w.role_sutras) for w in r.words}
    assert roles["गाम्"][0] == "कर्म" and roles["पयस्"][0] == "कर्म"
    assert ("1.4.51", "2.3.2") in (roles["गाम्"][1], roles["पयस्"][1])
    assert karaka.verify(r) == []


def test_upapada_sentences():
    r = _lex([("रामाय", False), ("नमस्", False)])
    assert (_w(r, "रामाय").role, _w(r, "रामाय").role_sutras) == ("सम्बन्ध", ("2.3.16",))
    # (सह before a noun is now joined to it as a compound prefix by compounds.annotate, so सह follows here)
    r = _lex([("सीता", False), ("रामेण", False), ("सह", False), ("गच्छति", False)])
    w = _w(r, "रामेण")
    assert (w.role, r.words[w.head].form, w.role_sutras) == ("सम्बन्ध", "सह", ("2.3.19",))
    assert any("उपपद" in n for n in r.notes)


def test_locative_absolute():
    r = _lex([("गते", False), ("रामे", False), ("सीता", False), ("रोदिति", False)])
    w = _w(r, "रामे")
    assert (w.role, w.morph.vibhakti, w.role_sutras) == ("भावलक्षण", P7, ("2.3.37",))
    assert r.words[w.head].form == "रोदिति"
    assert karaka.verify(r) == []


def test_verify_reports_violation():
    from dataclasses import replace
    r = hand([("रामम्", False, [nom("रामम्", "राम", P2)]), ("धावति", False, [ACTIVE])])
    bad = replace(r, words=[replace(r.words[0], role="कर्ता", head=1), replace(r.words[1], role="क्रिया")])
    assert karaka.verify(bad) and "प्रथमा" in karaka.verify(bad)[0]


# Rāmāyaṇa Bāla 1 through the whole pipeline

LINKED = set(karaka.CASE_ROLES)


def _verse(n):
    try:
        from mayur import gold, pipeline
        return pipeline.analyze_verse(gold.verse_text(n), f"1.1.{n}").readings[0]
    except Exception as e:  # data not installed
        pytest.skip(f"pipeline/gold unavailable: {e}")


@pytest.mark.parametrize("n", [1, 5, 6, 7, 19])
def test_ramayana_links_cite_rules(n):
    r = _verse(n)
    for w in r.words:
        if w.role in LINKED and w.head is not None and not w.in_compound:
            assert w.role_sutras, (n, w.form, w.role)
    assert "karaka_verified" in r.scores


@pytest.mark.parametrize("n", [1, 19])
def test_ramayana_verify_clean(n):
    r = _verse(n)
    assert karaka.verify(r) == [] and r.scores["karaka_verified"] == 1.0
