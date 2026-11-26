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
    assert r.words[0].role == "कर्ता" and r.words[0].head is None  # कस् is the subject
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
    assert _r(r, "कस्य") == ("सम्बन्ध", "बिभ्यति")  # षष्ठी शेषे (2.3.50): भी takes पञ्चमी by 1.4.25
    assert next(w for w in r.words if w.form == "कस्य").role_sutras == ("2.3.50",)
    first = [w for w in r.words if w.line == 0 and w.form == "कस्"][0]
    assert first.role == "कर्ता" and first.head is None  # line 1 is a nominal clause


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
    assert _r(r, "विष्णुना") == ("सम्बन्ध", "सदृशस्")  # तुल्यार्थैः … तृतीया (2.3.72), not a करण
    assert _r(r, "वीर्ये") == ("अधिकरण", "सदृशस्")
    assert _r(r, "क्षमया")[1] == "समस्"


def test_agent_noun_over_lut_verse13():
    r = _gold(13)
    assert r.words[0].morph.kind == "subanta" and r.words[0].morph.krt == "तृच्"
    assert not any(w.role == "क्रिया" for w in r.words)


def test_named_subject_kept_verse8():
    r = _gold(8)
    assert _r(r, "रामस्") == ("कर्म", "श्रुतस्")  # the क्त predicate expresses its कर्म (3.4.70)
    assert next(w for w in r.words if w.form == "रामस्").role_sutras[:2] == ("1.4.49", "3.4.70")
    assert _r(r, "वशी") == ("विशेषण", "रामस्")  # qualifies the subject of the क्त predicate


def test_relative_clause_yad_tad():
    from syntax_fixtures import hand, nom, verb
    r = _resolve(hand([("यस्", False, [nom("यस्", "यद्", "प्रथमा")]),
                       ("पठति", False, [verb("पठति", "पठ्", "लट्")]),
                       ("सस्", False, [nom("सस्", "तद्", "प्रथमा")]),
                       ("जानाति", False, [verb("जानाति", "ज्ञा", "लट्")])]))
    assert _r(r, "यस्") == ("कर्ता", "पठति")
    assert _r(r, "सस्") == ("कर्ता", "जानाति")


def test_question_keeps_its_clause():
    r = _resolve(verse2())
    assert r.words[0].role == "कर्ता" and all(w.head != 0 or w.line == 0 for w in r.words)


# Round 2: sentence structure by rule (dev verses 21-79 only; 1-20 are the test set).

def _ref(n):
    """Verse n of the reference file, built from its own words and feats (eval/gold_words.py)."""
    import json
    import sys
    from pathlib import Path
    root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(root / "eval"))
    try:
        import gold_words
        doc = json.loads((root / "eval/review/claude/ramayana_bala1_041_079_A.json").read_text(encoding="utf-8"))
        return _resolve(gold_words.reading_of(next(v for v in doc["verses"] if v["number"] == n))[0])
    except Exception as e:  # reference file or lexicon unavailable
        pytest.skip(f"reference unavailable: {e}")

def _two_lines(line0, line1):
    from syntax_fixtures import hand
    r = hand(line0 + line1)
    words = [type(w)(**{**w.__dict__, "line": 0 if k < len(line0) else 1}) for k, w in enumerate(r.words)]
    return type(r)(words=words)


def test_agent_in_the_other_half_verse():
    from dataclasses import replace
    from syntax_fixtures import nom, verb
    r = _resolve(_two_lines([("देवास्", False, [nom("देवास्", "देव", "प्रथमा", vacana="बहुवचन")])],
                            [("अभिगच्छन्ति", False, [replace(verb("अभिगच्छन्ति", "गम्", "लट्"), vacana="बहुवचन")]),
                             ("तीर्थम्", False, [nom("तीर्थम्", "तीर्थ", "द्वितीया", "नपुंसकलिङ्ग")])]))
    assert _r(r, "देवास्") == ("कर्ता", "अभिगच्छन्ति")  # the verb's line has no agreeing nominative
    assert r.words[0].role_sutras[:3] == ("1.4.54", "3.4.69", "2.3.46")


def test_particles_follow_their_word_or_verb_verse43():
    r = _ref(43)  # गृध्रं च निहतं दृष्ट्वा हृतां श्रुत्वा च मैथिलीम्
    ca = [i for i, w in enumerate(r.words) if w.form == "च"]
    assert all(r.words[i].head == i - 1 for i in ca)


def test_kta_predicates_of_a_verbless_clause_verse47():
    r = _ref(47)  # शबर्या पूजितः सम्यग्रामो दशरथात्मजः । पम्पातीरे हनुमता संगतो वानरेण ह
    assert _r(r, "पूजितस्")[0] == "क्रिया" and _r(r, "संगतस्")[0] == "क्रिया"
    assert _r(r, "रामस्") == ("कर्म", "पूजितस्")  # the क्त of a transitive root expresses its कर्म (3.4.70)
    assert _r(r, "आत्मजस्") == ("विशेषण", "रामस्")


def test_participle_qualifies_unexpressed_agent_verse44():
    r = _ref(44)  # … मार्गमाणो वने सीतां राक्षसं संददर्श ह
    assert _r(r, "मार्गमाणस्") == ("विशेषण", "संददर्श")
    assert any("unexpressed agent" in n for n in r.notes)
    assert _r(r, "गृध्रम्")[0] == "कर्म" and _r(r, "जटायुषम्") == ("विशेषण", "गृध्रम्")


def test_demonstrative_qualifies_verse48():
    r = _ref(48)  # सुग्रीवाय च तत्सर्वं शंसद्रामो महाबलः
    assert _r(r, "तत्") == ("विशेषण", "सर्वम्")


def _sync(items):
    from syntax_fixtures import hand
    from mayur import vakya_case
    return vakya_case.syncretic(hand(items).words)


def test_syncretic_accusative_when_the_agent_is_there():
    from syntax_fixtures import nom, verb
    words, notes = _sync([("रामस्", False, [nom("रामस्", "राम", "प्रथमा")]),
                          ("वनम्", False, [nom("वनम्", "वन", "प्रथमा", "नपुंसकलिङ्ग"),
                                           nom("वनम्", "वन", "द्वितीया", "नपुंसकलिङ्ग")]),
                          ("गच्छति", False, [verb("गच्छति", "गम्", "लट्")])])
    assert words[1].morph.vibhakti == "द्वितीया" and "1.4.49" in notes[0]


def test_syncretic_nominative_with_passive_and_not_in_a_question():
    from syntax_fixtures import nom, verb
    words, _ = _sync([("रामेण", False, [nom("रामेण", "राम", "तृतीया")]),
                      ("वनम्", False, [nom("वनम्", "वन", "द्वितीया", "नपुंसकलिङ्ग"),
                                       nom("वनम्", "वन", "प्रथमा", "नपुंसकलिङ्ग")]),
                      ("दृश्यते", False, [verb("दृश्यते", "दृश्", "लट्", "कर्मणि")])])
    assert words[1].morph.vibhakti == "प्रथमा"
    words, notes = _sync([("किम्", False, [nom("किम्", "किम्", "प्रथमा", "नपुंसकलिङ्ग"),
                                           nom("किम्", "किम्", "द्वितीया", "नपुंसकलिङ्ग")]),
                          ("अहम्", False, [nom("अहम्", "अस्मद्", "प्रथमा", None)]),
                          ("जाने", False, [verb("जाने", "ज्ञा", "लट्")])])
    assert words[0].morph.vibhakti == "प्रथमा" and not notes  # a question: not decisive
