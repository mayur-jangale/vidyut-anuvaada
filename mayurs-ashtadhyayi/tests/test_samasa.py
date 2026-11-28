"""Forward समास rule chains with real lexicon objects (Devanagari only)."""

import pytest

from mayur import compounds, lexicon, samasa


def _stem(form):
    found = lexicon.stems(form)
    if not found:
        pytest.skip(f"lexicon has no stem {form}")
    return found[0]


def _pada(form, lemma):
    found = [m for m in lexicon.padas(form) if m.kind == "subanta" and (m.stem or m.lemma) == lemma]
    if not found:
        pytest.skip(f"lexicon has no pada {form} of {lemma}")
    return found[0]


CASES = [
    # members, final pada, final stem, type, relation, surface, member written forms, type rule, derivable
    (["तपस्", "स्वाध्याय"], "निरतम्", "निरत", "तत्पुरुष", "सप्तमी", "तपस्स्वाध्यायनिरत", (), "2.1.40", True),
    (["वाच्"], "विदाम्", "विद्", "उपपद", "", "वाग्विद्", ("वाक्", "विदाम्"), "2.2.19", True),
    (["मुनि"], "पुंगवम्", "पुंगव", "तत्पुरुष", "षष्ठी", "मुनिपुंगव", (), "2.2.8", True),
    (["धर्म"], "ज्ञस्", "ज्ञ", "उपपद", "", "धर्मज्ञ", (), "2.2.19", True),
    (["दृढ"], "व्रतस्", "व्रत", "बहुव्रीहि", "", "दृढव्रत", (), "2.2.24", True),
    (["जित"], "क्रोधस्", "क्रोध", "बहुव्रीहि", "", "जितक्रोध", (), "2.2.24", True),
    (["महत्"], "बाहुस्", "बाहु", "बहुव्रीहि", "", "महाबाहु", (), "2.2.24", True),
    (["न", "दीन"], "आत्मा", "आत्मन्", "बहुव्रीहि", "", "अदीनात्मन्", (), "2.2.24", True),
    (["इक्ष्वाकु", "वंश"], "प्रभवस्", "प्रभव", "तत्पुरुष", "षष्ठी", "इक्ष्वाकुवंशप्रभव", (), "2.2.8", True),
    (["सर्व", "गुण"], "उपेतस्", "उपेत", "तत्पुरुष", "तृतीया", "सर्वगुणोपेत", (), "2.1.3", True),
    (["काल", "अग्नि"], "सदृशस्", "सदृश", "तत्पुरुष", "तृतीया", "कालाग्निसदृश", (), "2.1.3", True),
]


@pytest.mark.parametrize("mem,fin,lem,typ,rel,surf,forms,rule,ok", CASES, ids=[c[5] for c in CASES])
def test_forward_chain(mem, fin, lem, typ, rel, surf, forms, rule, ok):
    final = _pada(fin, lem)
    d = samasa.derive([_stem(m) for m in mem] + [final], final, typ, relation=rel, surface=surf, forms=forms)
    codes = [t.code for t in d.trace]
    assert d.stem == surf
    assert rule in codes and "1.2.46" in codes and "2.4.71" in codes
    assert any(samasa.HEUR in t.result for t in d.trace)
    assert d.derivable is ok
    assert all(t.source == "अष्टाध्यायी" for t in d.trace[:7])


def test_not_derivable_when_surface_differs():
    final = _pada("व्रतस्", "व्रत")
    d = samasa.derive([_stem("दृढ"), final], final, "बहुव्रीहि", surface="दृढवृत")
    assert not d.derivable and "sandhi gave" in d.note


def test_nan_member_rule():
    final = _pada("आत्मा", "आत्मन्")
    d = samasa.derive([_stem("न"), _stem("दीन"), final], final, "बहुव्रीहि", surface="अदीनात्मन्")
    assert "6.3.73" in [t.code for t in d.trace]


def test_relation_table():
    assert compounds.relation("निरत") == "सप्तमी"
    assert compounds.relation("उपेत") == "तृतीया"
    assert compounds.relation("प्राप्त") == "द्वितीया"
    assert compounds.relation("प्रभव") == "षष्ठी"
