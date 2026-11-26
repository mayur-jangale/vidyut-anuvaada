from syntax_fixtures import verse1, verse2

from mayur import compounds


def test_verse1_compounds_grouped():
    r = compounds.annotate(verse1())
    assert [c.members for c in r.compounds] == [[0, 1, 2], [4, 5], [10, 11]]
    assert r.words[2].compound == 0 and r.words[3].compound is None
    assert r.compounds[0].samasa == compounds.TATPURUSHA  # क्त final member
    assert r.compounds[0].stem == "तपस्स्वाध्यायनिरत"


def test_basis_is_always_heuristic():
    for v in (verse1(), verse2()):
        for c in compounds.annotate(v).compounds:
            assert c.basis.startswith("heuristic:")
            assert c.vigraha


def test_dridhavrata_is_bahuvrihi():
    r = compounds.annotate(verse2())
    dridha = next(c for c in r.compounds if c.members[0] == 16)
    assert dridha.samasa == compounds.BAHUVRIHI
    dharmajna = next(c for c in r.compounds if c.members[0] == 9)
    assert dharmajna.samasa == compounds.TATPURUSHA


def test_annotate_returns_new_object():
    v = verse1()
    r = compounds.annotate(v)
    assert r is not v and v.compounds == [] and v.words[0].compound is None
