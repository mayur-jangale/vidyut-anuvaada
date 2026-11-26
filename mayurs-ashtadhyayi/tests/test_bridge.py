import re

from mayur import bridge


def _no_roman(*values):
    return all(not v or not re.search(r"[A-Za-z]", v) for v in values)


def test_lookup_devanagari():
    entries = bridge.lookup("रामस्")
    assert entries
    for e in entries:
        m = e.morph
        assert _no_roman(m.form, m.lemma, m.stem, m.linga, m.vibhakti, m.vacana, m.krt, m.root, m.dhatu, m.gana)


def test_lookup_unknown():
    assert bridge.lookup("क्ष्ज्ञ्") == ()
    assert bridge.lookup("") == ()


def test_derive_trace():
    e = bridge.lookup("निरतम्")[0]
    ders = bridge.derive(e.morph.handle)
    assert any(d.text == "निरतम्" for d in ders)
    assert ders[0].trace[0].source == "अष्टाध्यायी"
    assert re.fullmatch(r"\d\.\d\.\d+", ders[0].trace[0].code)


def test_prefixed_tinanta():
    e = [x for x in bridge.lookup("पप्रच्छ") if x.entry == "tinanta"][0]
    pada = bridge.prefixed_tinanta(e, ("परि",))
    assert any(d.text == "परिपप्रच्छ" for d in bridge.derive(pada))


def test_matup():
    e = bridge.lookup("गुणवान्")[0]
    assert any(d.text == "गुणवान्" for d in bridge.derive(bridge.matup_subanta(e.morph.handle)))
