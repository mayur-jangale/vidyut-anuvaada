from syntax_fixtures import shveta, verse1, verse2

from mayur import anvaya, compounds, shabdabodha


def _full(r):
    return anvaya.order(shabdabodha.resolve(compounds.annotate(r)))


def _forms(r):
    return [r.words[i].form for i in r.anvaya]


def test_every_index_once():
    for v in (verse1(), verse2(), *shveta()):
        r = _full(v)
        assert sorted(r.anvaya) == list(range(len(r.words)))


def test_verse1_order():
    r = _full(verse1())
    assert _forms(r) == ["तपस्वी", "वाल्मीकिस्", "तपस्", "स्वाध्याय", "निरतम्", "वाक्", "विदाम्", "वरम्",
                         "मुनि", "पुंगवम्", "नारदम्", "परिपप्रच्छ"]


def test_compound_members_adjacent():
    r = _full(verse1())
    for c in r.compounds:
        pos = [r.anvaya.index(i) for i in c.members]
        assert pos == list(range(pos[0], pos[0] + len(pos)))


def test_verse2_subject_first_and_cha_after():
    r = _full(verse2())
    f = _forms(r)
    assert f.index("कस्") < f.index("गुणवान्")
    assert r.anvaya.index(7) == r.anvaya.index(6) + 1


def test_na_before_verb():
    from syntax_fixtures import avyaya, hand, nom, verb
    r = _full(hand([("न", False, [avyaya("न")]), ("रामस्", False, [nom("रामस्", "राम", "प्रथमा")]),
                    ("गच्छति", False, [verb("गच्छति", "गम्", "लट्")])]))
    assert _forms(r) == ["रामस्", "न", "गच्छति"]


def test_absolutive_with_own_object():
    from syntax_fixtures import avyaya, hand, nom, verb
    r = _full(hand([("गच्छति", False, [verb("गच्छति", "गम्", "लट्")]),
                    ("रामस्", False, [nom("रामस्", "राम", "प्रथमा")]),
                    ("वनम्", False, [nom("वनम्", "वन", "द्वितीया", "नपुंसकलिङ्ग")]),
                    ("दृष्ट्वा", False, [avyaya("दृष्ट्वा", krt="क्त्वा")])]))
    assert r.words[3].role == "पूर्वकालक्रिया" and r.words[2].head == 3
    assert _forms(r) == ["रामस्", "वनम्", "दृष्ट्वा", "गच्छति"]
