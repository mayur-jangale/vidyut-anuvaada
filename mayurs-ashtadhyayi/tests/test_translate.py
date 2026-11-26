from mayur import translate
from mayur.model import Compound, Morph, Reading, Word

SG = dict(vacana="एकवचन")


def W(form, lemma, kind, role="", head=None, gloss="", src="own", **kw):
    return Word(form, 0, 0, 0, role=role, head=head, gloss=gloss, gloss_source=src,
                analyses=[Morph(form, lemma, kind, **kw)], in_compound=kw.pop("_c", False))


def noun(form, lemma, role, head, gloss, vib="प्रथमा", vac="एकवचन", linga="पुंलिङ्ग", **kw):
    return W(form, lemma, "subanta", role, head, gloss, linga=linga, vibhakti=vib, vacana=vac, **kw)


def verb(form, lemma, gloss, lak="लट्", p="प्रथमपुरुष", vac="एकवचन", prayoga="कर्तरि", **kw):
    return W(form, lemma, "tinanta", "क्रिया", None, gloss, "dcs-sense", purusha=p, vacana=vac,
             lakara=lak, prayoga=prayoga, root=lemma, **kw)


def check(out):
    t = out.translation
    spans = sorted((a.start, a.end) for a in out.alignment)
    assert all(0 <= s < e <= len(t) for s, e in spans)
    assert all(spans[k][1] <= spans[k + 1][0] for k in range(len(spans) - 1))


def test_white_runs():
    r = Reading(words=[noun("श्वेतस्", "श्वेत", "कर्ता", 1, "white"), verb("धावति", "धाव्", "run")],
                anvaya=[0, 1])
    out = translate.render(r)
    assert out.translation == "white runs"
    assert [(a.word, a.start, a.end) for a in out.alignment] == [(0, 0, 5), (1, 6, 10)]
    assert r.translation == ""  # input untouched


def _verse1(with_mods):
    words = [
        noun("तपस्", "तपस्", "समासपूर्वपद", None, "austerity"),
        noun("स्वाध्याय", "स्वाध्याय", "समासपूर्वपद", None, "study"),
        noun("निरतम्", "निरत", "विशेषण", 4, "devoted", vib="द्वितीया"),
        noun("वरम्", "वर", "विशेषण", 4, "best", vib="द्वितीया"),
        noun("नारदम्", "नारद", "कर्म", 5, "Nārada", vib="द्वितीया"),
        verb("परिपप्रच्छ", "परिप्रच्छ्", "ask", lak="लिट्"),
        noun("वाल्मीकिस्", "वाल्मीकि", "कर्ता", 5, "Vālmīki"),
    ]
    words[0].in_compound = words[1].in_compound = True
    words[0].compound = words[1].compound = words[2].compound = 0
    comp = [Compound(0, [0, 1, 2])]
    if not with_mods:
        words = [words[4], words[5], words[6]]
        words[0].head = 1
        words[2].head = 1
        return Reading(words=words, anvaya=[2, 1, 0])
    return Reading(words=words, compounds=comp, anvaya=[6, 5, 2, 3, 4])


def test_verse_one_plain():
    out = translate.render(_verse1(False))
    assert out.translation == "Vālmīki asked Nārada"
    check(out)


def test_verse_one_compound_and_alignment():
    out = translate.render(_verse1(True))
    t = out.translation
    assert t == "Vālmīki asked austerity-study-devoted best Nārada"
    check(out)
    spans = {a.word: t[a.start:a.end] for a in out.alignment}
    assert spans[0] == "austerity" and spans[1] == "study" and spans[2] == "devoted"
    assert spans[6] == "Vālmīki" and spans[5] == "asked" and spans[4] == "Nārada"
    assert set(spans) == set(range(7))


def test_plural_instrument_locative_negation():
    r = Reading(words=[
        noun("मुनयस्", "मुनि", "कर्ता", 3, "sage", vac="बहुवचन"),
        noun("वनेषु", "वन", "अधिकरण", 3, "forest", vib="सप्तमी", vac="बहुवचन", linga="नपुंसकलिङ्ग"),
        W("न", "न", "avyaya", "अव्यय", 3, "not"),
        verb("गच्छन्ति", "गम्", "go", vac="बहुवचन"),
    ], anvaya=[0, 1, 2, 3])
    out = translate.render(r)
    assert out.translation == "sages do not go among forests"
    check(out)


def test_future_and_supplied_subject_and_vocative():
    r = Reading(words=[
        noun("राम", "राम", "सम्बोधन", 1, "Rāma", vib="सम्बोधन"),
        verb("वदिष्यामि", "वद्", "say", lak="लृट्", p="उत्तमपुरुष"),
    ], anvaya=[0, 1])
    out = translate.render(r)
    assert out.translation == "O Rāma, [I] will say"
    assert [a.word for a in out.alignment] == [0, 1]


def test_passive_and_verbless_and_arsha():
    r = Reading(words=[
        noun("रामेण", "राम", "कर्ता", 2, "Rāma", vib="तृतीया"),
        noun("रावणस्", "रावण", "कर्ता", 2, "Rāvaṇa"),
        verb("हन्यते", "हन्", "kill", prayoga="कर्मणि"),
    ], anvaya=[1, 2, 0])
    out = translate.render(r)
    assert out.translation == "Rāvaṇa is killed by Rāma"
    v = Reading(words=[noun("कस्", "क", "कर्ता", None, "who"),
                       noun("गुणवान्", "गुणवत्", "विधेय", None, "virtuous")], anvaya=[0, 1])
    o = translate.render(v)
    assert o.translation == "who [is] virtuous" and len(o.alignment) == 2
    a = Word("रामा", 0, 0, 0, role="कर्ता", arsha=True, analyses=[Morph("रामा", "राम", "subanta")])
    o = translate.render(Reading(words=[a]))
    assert o.translation.startswith("⟨") and len(o.alignment) == 1
