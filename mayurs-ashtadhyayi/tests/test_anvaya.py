from fixtures_syntax import SVA_ITAS, SVETAS, VERSE1, VERSE2, analysed, reading_from_forms

from mayur.anvaya import order


def _forms(r):
    return [r.words[i].form for i in r.anvaya]


def _check_permutation(r):
    assert sorted(r.anvaya) == list(range(len(r.words)))


def test_every_index_once():
    for v in (VERSE1, VERSE2, SVETAS, SVA_ITAS):
        _check_permutation(analysed(v))


def test_verse1_order():
    r = analysed(VERSE1)
    if r.words[8].role != "kriya":
        return
    assert _forms(r)[-1] == "paripapracCa"
    assert _forms(r)[:2] == ["tapasvI", "vAlmIkis"]
    assert _forms(r).index("nAradam") == len(r.words) - 2


def test_compound_members_contiguous():
    r = analysed(VERSE1)
    for c in r.compounds:
        pos = [r.anvaya.index(i) for i in c.members]
        assert pos == list(range(pos[0], pos[0] + len(pos)))


def test_simple_clauses():
    assert _forms(analysed(SVETAS)) == ["Svetas", "DAvati"]
    assert _forms(analysed(SVA_ITAS)) == ["SvA", "itas", "DAvati"]


def test_unresolved_reading_still_permutation():
    r = order(reading_from_forms(VERSE1))  # no roles at all
    _check_permutation(r)
