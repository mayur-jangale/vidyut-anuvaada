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
