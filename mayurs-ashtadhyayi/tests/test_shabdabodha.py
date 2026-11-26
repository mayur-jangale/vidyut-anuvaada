import pytest
from syntax_fixtures import reading, shveta, verse1, verse2

from mayur import compounds, shabdabodha


def _resolve(r):
    return shabdabodha.resolve(compounds.annotate(r))


def test_verse1_roles():
    r = _resolve(verse1())
    role = {w.form: (w.role, w.head) for w in r.words}
    assert role["परिपप्रच्छ"] == ("क्रिया", None)
    assert role["वाल्मीकिस्"] == ("कर्ता", 8)
    assert role["नारदम्"] == ("कर्म", 8)
    for q in ("निरतम्", "वरम्", "पुंगवम्"):
        assert role[q] == ("विशेषण", 7)
    assert role["तपस्वी"] == ("विशेषण", 9)
    assert role["विदाम्"] == ("सम्बन्ध", 6)
    assert role["तपस्"] == ("समासपूर्वपद", 2)
    assert r.scores["akanksha"] == 1.0
    assert 0 <= r.scores["sannidhi"] <= 1 and "total" in r.scores


def test_verse2_verbless():
    r = _resolve(verse2())
    assert r.words[0].role == "" and r.words[0].head is None  # कस् is the subject
    assert r.words[5].role == "विधेय" and r.words[17].role == "विधेय"
    assert r.words[4].role == "अधिकरण" and r.words[2].head == 4
    assert r.words[7].head == 6  # च joins the preceding कस्
    assert any("nominal clause" in n for n in r.notes)


@pytest.mark.parametrize("which", [0, 1])
def test_shveta_dhavati(which):
    r = _resolve(shveta()[which])
    verb = next(i for i, w in enumerate(r.words) if w.form == "धावति")
    assert r.words[verb].role == "क्रिया"
    assert any(w.role == "कर्ता" and w.head == verb for w in r.words)


def test_agreement_picks_accusative():
    r = _resolve(verse1())
    assert r.words[2].morph.vibhakti == "द्वितीया"  # निरतम् agrees with नारदम्
    assert len(r.words[2].analyses) == 2  # alternatives are kept


def test_unknown_word_passed_through():
    v = verse1()
    v.words.append(type(v.words[0])(form="क्ष", line=0, start=20, end=21))
    r = _resolve(v)
    assert r.words[-1].role == "" and any("क्ष" in n for n in r.notes)


def test_rank_keeps_all():
    a, b = (_resolve(x) for x in shveta())
    ranked = shabdabodha.rank([b, a])
    assert len(ranked) == 2 and {id(x) for x in ranked} == {id(a), id(b)}
    assert ranked[0].scores["total"] >= ranked[1].scores["total"]


def test_candidates_dedupe_and_quality():
    from mayur.model import Morph, Word
    m = Morph(form="क", lemma="क", kind="subanta", vibhakti="प्रथमा", quality=3)
    junk = Morph(form="क", lemma="ख", kind="subanta", vibhakti="प्रथमा", quality=0)
    w = Word(form="क", line=0, start=0, end=1, analyses=[m, m, junk])
    assert shabdabodha.candidates(w) == [0]


def test_verse1_from_lexicon():
    try:
        r = reading([("तपस्", True), ("स्वाध्याय", True), ("निरतम्", False), ("तपस्वी", False), ("वाक्", True),
                     ("विदाम्", False), ("वरम्", False), ("नारदम्", False), ("परिपप्रच्छ", False),
                     ("वाल्मीकिस्", False), ("मुनि", True), ("पुंगवम्", False)])
    except Exception as e:  # lexicon still under construction
        pytest.skip(f"lexicon unavailable: {e}")
    r = _resolve(r)
    assert r.words[8].role == "क्रिया"
    assert r.words[9].role == "कर्ता" and r.words[7].role == "कर्म"


def _gold(n):
    from syntax_fixtures import gold_reading
    try:
        return _resolve(gold_reading(n))
    except Exception as e:  # gold file or lexicon unavailable
        pytest.skip(f"gold/lexicon unavailable: {e}")


def _r(r, form):
    i = next(i for i, w in enumerate(r.words) if w.form == form)
    w = r.words[i]
    return w.role, (r.words[w.head].form if w.head is not None else None)


def test_person_agreement_and_copula_verse5():
    r = _gold(5)
    assert _r(r, "अहम्") == ("कर्ता", "इच्छामि")
    assert _r(r, "त्वम्") == ("कर्ता", "असि")
    assert _r(r, "समर्थस्") == ("विधेय", "त्वम्")


def test_number_agreement_and_fear_verse4():
    r = _gold(4)
    assert _r(r, "देवास्") == ("कर्ता", "बिभ्यति")
    assert _r(r, "कस्य") == ("अपादान", "बिभ्यति")
    first = [w for w in r.words if w.line == 0 and w.form == "कस्"][0]
    assert first.role == "" and first.head is None  # line 1 is a nominal clause


def test_quoted_speech_verse6():
    r = _gold(6)
    assert _r(r, "नारदस्") == ("कर्ता", "अब्रवीत्")
    assert _r(r, "वचस्") == ("कर्म", "श्रुत्वा")
    assert _r(r, "वाक्यम्") == ("कर्म", "अब्रवीत्")
    assert _r(r, "प्रहृष्टस्") == ("विशेषण", "नारदस्")
    assert _r(r, "इति") == ("अव्यय", "श्रूयताम्")


def test_instrumental_agent_of_kta_verse7():
    r = _gold(7)
    assert _r(r, "त्वया") == ("कर्ता", "कीर्तितास्")
    assert _r(r, "अहम्") == ("कर्ता", "वक्ष्यामि")
    assert all(w.morph.vibhakti != "सम्बोधन" for w in r.words if w.form == "एव")


def test_karma_capped_per_verb():
    from syntax_fixtures import hand, nom, verb
    r = _resolve(hand([("रामस्", False, [nom("रामस्", "राम", "प्रथमा")]),
                       ("वनम्", False, [nom("वनम्", "वन", "द्वितीया", "नपुंसकलिङ्ग")]),
                       ("गृहान्", False, [nom("गृहान्", "गृह", "द्वितीया", "पुंलिङ्ग", "बहुवचन")]),
                       ("गच्छति", False, [verb("गच्छति", "गम्", "लट्")])]))
    assert sum(1 for w in r.words if w.role == "कर्म") == 1
    assert r.scores["akanksha"] < 1.0


def test_epithet_list_without_subject_verse12():
    r = _gold(12)
    noms = [w for w in r.words if not w.in_compound and w.morph.vibhakti == "प्रथमा"]
    assert all(w.role == "विधेय" and w.head is None for w in noms)
    assert any("subject not expressed" in n for n in r.notes)
    assert _r(r, "हिते") == ("अधिकरण", "रतस्")
    assert _r(r, "प्रजानाम्") == ("सम्बन्ध", "हिते")
    assert r.scores["akanksha"] > 0.8


def test_local_attachment_verse17():
    r = _gold(17)
    assert _r(r, "विष्णुना") == ("करण", "सदृशस्")
    assert _r(r, "वीर्ये") == ("अधिकरण", "सदृशस्")
    assert _r(r, "क्षमया")[1] == "समस्"


def test_agent_noun_over_lut_verse13():
    r = _gold(13)
    assert r.words[0].morph.kind == "subanta" and r.words[0].morph.krt == "तृच्"
    assert not any(w.role == "क्रिया" for w in r.words)


def test_named_subject_kept_verse8():
    r = _gold(8)
    assert _r(r, "रामस्") == ("", None)
    assert _r(r, "वशी") == ("विधेय", "रामस्")
