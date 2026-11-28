from mayur import lexicon, proof
from mayur.model import UNVERIFIED, VERIFIED, Reading, Word


def _word(form, line, start, end, in_compound=False):
    analyses = list(lexicon.stems(form) if in_compound else lexicon.padas(form))
    return Word(form=form, line=line, start=start, end=end, in_compound=in_compound, analyses=analyses)


def _reading(spec):
    return Reading(words=[_word(f, 0, 0, 0, c) for f, c in spec])


def test_verified_simple():
    r = proof.check(_reading([("रामस्", False), ("गच्छति", False)]), ["रामो गच्छति"])
    assert r.sandhi_ok
    assert all(w.proof is not None for w in r.words)
    if all(w.proof.derivable for w in r.words):
        assert r.status == VERIFIED


def test_wrong_sandhi_is_unverified():
    original = _reading([("रामस्", False), ("गच्छति", False)])
    r = proof.check(original, ["रामा गच्छति"])
    assert not r.sandhi_ok and r.status == UNVERIFIED
    assert any("re-join" in n for n in r.notes)
    assert original.status == UNVERIFIED and original.words[0].proof is None  # input untouched


def test_missing_analysis_noted():
    r = proof.check(Reading(words=[Word(form="क्ष्ट्र", line=0, start=0, end=0)]), ["क्ष्ट्र"])
    assert r.status == UNVERIFIED
    assert not r.words[0].proof.derivable
    assert any("क्ष्ट्र" in n for n in r.notes)


def test_compound_line():
    r = proof.check(_reading([("तपस्", True), ("स्वाध्याय", True), ("निरतम्", False)]), ["तपःस्वाध्यायनिरतं"])
    assert r.sandhi_ok
    assert r.rejoined and r.rejoined[0]
