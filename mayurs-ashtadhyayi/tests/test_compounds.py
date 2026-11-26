from dataclasses import replace

from fixtures_syntax import VERSE1, VERSE2, reading_from_forms

from mayur.compounds import annotate, decline


def _cpds(pairs):
    return annotate(reading_from_forms(pairs))


def test_groups_runs_with_final_member():
    r = _cpds(VERSE1)
    assert [c.members for c in r.compounds] == [[0, 1, 2], [4, 5], [10, 11]]
    assert [c.stem for c in r.compounds] == ["tapassvADyAyaniratam", "vAcvidAm", "munipuMgavam"]
    for c in r.compounds:
        assert all(r.words[i].compound == c.id for i in c.members)
    assert r.words[3].compound is None


def test_does_not_mutate_input():
    base = reading_from_forms(VERSE1)
    annotate(base)
    assert base.compounds == [] and all(w.compound is None for w in base.words)


def test_kta_tatpurusha_with_inner_dvandva():
    c = _cpds(VERSE1).compounds[0]
    assert c.samasa == "tatpurusha"
    assert c.vigraha == "tapasi svADyAye ca niratam"
    assert c.basis.startswith("heuristic:") and "saptamI" in c.basis


def test_genitive_tatpurusha():
    cs = _cpds(VERSE1).compounds
    assert cs[2].samasa == "tatpurusha" and cs[2].vigraha == "munInAm puMgavam"
    assert cs[1].samasa == "tatpurusha" and cs[1].vigraha.startswith("vAcas")


def test_bahuvrihi():
    cs = {c.stem: c for c in _cpds(VERSE2).compounds}
    assert cs["dfQavratas"].samasa == "bahuvrihi"
    assert cs["dfQavratas"].vigraha == "dfQam vratam yasya sas"
    assert cs["satyavAkyas"].samasa == "bahuvrihi"
    assert all(c.basis.startswith("heuristic:") for c in cs.values())


def test_unanalysed_final_is_unknown():
    r = reading_from_forms([("muni", True), ("puMgavam", False)])
    r = replace(r, words=[r.words[0], replace(r.words[1], analyses=[])])
    c = annotate(r).compounds[0]
    assert c.samasa == "unknown" and c.vigraha == "muni-puMgavam"


def test_decline_generates_forms():
    assert decline("tapas", "saptamI", "eka") == "tapasi"
    assert decline("muni", "zazWI", "bahu", "puM") == "munInAm"
