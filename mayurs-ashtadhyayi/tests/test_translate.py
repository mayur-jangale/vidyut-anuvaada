from fixtures_syntax import SVA_ITAS, SVETAS, VERSE1, VERSE2, rendered

from mayur.translate import verb_phrase
from mayur.model import Morph


def _check_alignment(r):
    assert r.translation
    covered = set()
    for a in r.alignment:
        assert 0 <= a.start < a.end <= len(r.translation)
        covered.add(a.word)
    for i, w in enumerate(r.words):
        if w.morph is None or w.morph.kind != "avyaya":
            assert i in covered, f"{w.form} not aligned in {r.translation!r}"


def test_alignment_all_verses():
    for v in (VERSE1, VERSE2, SVETAS, SVA_ITAS):
        _check_alignment(rendered(v))


def test_verse1_svo():
    r = rendered(VERSE1)
    if r.words[8].role != "kriya":
        return
    t = r.translation
    span = {r.words[a.word].form: t[a.start:a.end] for a in r.alignment}
    assert t.index(span["vAlmIkis"]) < t.index(span["paripapracCa"]) < t.index(span["nAradam"])
    assert span["paripapracCa"].endswith("ed")
    assert "-and-" in t  # tapas-svADyAya inner dvandva


def test_dhavati_present_third_singular():
    for v in (SVETAS, SVA_ITAS):
        r = rendered(v)
        verb = [a for a in r.alignment if r.words[a.word].form == "DAvati"][0]
        assert r.translation[verb.start:verb.end].endswith("s")


def test_nominal_sentence_copula():
    assert "[is]" in rendered(VERSE2).translation


def test_verb_templates():
    m = Morph(form="x", lemma="x", kind="tinanta", purusha="uttama", vacana="eka", lakara="la~w")
    assert verb_phrase("wish", m) == "wish"
    past = Morph(form="x", lemma="x", kind="tinanta", purusha="praTama", vacana="eka", lakara="li~w")
    assert verb_phrase("ask", past) == "asked" and verb_phrase("run", past) == "ran"
    fut = Morph(form="x", lemma="x", kind="tinanta", purusha="praTama", vacana="eka", lakara="lf~w")
    assert verb_phrase("go", fut) == "will go"
