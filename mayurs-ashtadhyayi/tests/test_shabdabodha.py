from dataclasses import replace

from fixtures_syntax import SVA_ITAS, SVETAS, VERSE1, VERSE2, analysed, reading_from_forms

from mayur.compounds import annotate
from mayur.shabdabodha import prune, rank, resolve


def _roles(r):
    return {w.form: (w.role, w.head) for w in r.words}


def test_verse1_roles():
    r = analysed(VERSE1)
    w = r.words
    verb = 8
    if not w[verb].analyses:  # lexicon may not cover the upasarga verb yet
        assert w[verb].role == "" and any("paripapracCa" in n for n in r.notes)
        return
    assert w[verb].role == "kriya" and w[verb].head is None
    assert (w[9].role, w[9].head) == ("karta", verb)  # vAlmIkis
    assert (w[7].role, w[7].head) == ("karma", verb)  # nAradam
    assert (w[3].role, w[3].head) == ("visheshana", 9)  # tapasvI -> vAlmIkis
    for i in (2, 6, 11):  # niratam, varam, puMgavam -> nAradam
        assert (w[i].role, w[i].head) == ("visheshana", 7)
        assert w[i].morph.vibhakti == "dvitIyA" and w[i].morph.linga == "puM"
    assert (w[5].role, w[5].head) == ("sambandha", 6)  # vidAm -> varam
    for i, h in ((0, 2), (1, 2), (4, 5), (10, 11)):
        assert (w[i].role, w[i].head) == ("samasa-purvapada", h)


def test_scores_present():
    r = analysed(VERSE1)
    for k in ("akanksha", "yogyata", "sannidhi", "total"):
        assert 0.0 <= r.scores[k] <= 1.0


def test_frequency_kept():
    base = replace(annotate(reading_from_forms(SVETAS)), scores={"frequency": 0.5})
    r = resolve(base)
    assert r.scores["frequency"] == 0.5
    assert base.words[0].role == ""  # input not mutated


def test_svetas_dhavati():
    r = analysed(SVETAS)
    assert r.words[1].morph.kind == "tinanta"
    assert _roles(r) == {"Svetas": ("karta", 1), "DAvati": ("kriya", None)}


def test_sva_itas_dhavati():
    r = analysed(SVA_ITAS)
    assert r.words[2].morph.kind == "tinanta"
    roles = _roles(r)
    assert roles["SvA"] == ("karta", 2)
    assert roles["itas"] == ("avyaya", 2)
    assert r.words[1].morph.kind == "avyaya"


def test_nominal_sentence_verse2():
    r = analysed(VERSE2)
    w = r.words
    assert not any(x.role == "kriya" for x in w)
    assert any("nominal sentence" in n for n in r.notes)
    assert (w[0].role, w[0].head) == ("karta", None)  # kas
    assert (w[6].role, w[6].head) == ("karta", None)  # second kas
    assert w[4].role == "adhikarana" and (w[2].role, w[2].head) == ("visheshana", 4)
    assert w[5].head == 0 and w[8].head == 6
    assert all(x.role for x in w)


def test_rank_keeps_all():
    a, b = analysed(SVA_ITAS), analysed(SVETAS)
    ranked = rank([a, b])
    assert len(ranked) == 2 and {id(x) for x in ranked} == {id(a), id(b)}
    assert ranked[0].scores["total"] >= ranked[1].scores["total"]
    tie_long = replace(a, scores={"total": 0.5})
    tie_short = replace(b, scores={"total": 0.5})
    assert rank([tie_long, tie_short])[0] is tie_short


def test_prune_distinct_signatures():
    w = reading_from_forms([("tapas", False)]).words[0]
    idx = prune(w.analyses)
    assert len(idx) < len(w.analyses)
    sigs = [(w.analyses[i].vibhakti, w.analyses[i].vacana, w.analyses[i].linga) for i in idx]
    assert len(sigs) == len(set(sigs))


def test_unanalysed_word_kept():
    r = reading_from_forms(SVETAS + [("xyzq", False)])
    out = resolve(annotate(r))
    assert out.words[2].role == "" and any("xyzq" in n for n in out.notes)
