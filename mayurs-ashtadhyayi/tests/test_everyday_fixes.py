"""Rules found with the everyday check set (eval/eval_everyday.py), each tested on inputs outside it."""

from mayur import lexicon, lipi, segmenter
from mayur.pipeline import analyze_verse


def _lemmas(form):
    return {m.lemma for m in lexicon.padas(form) if m.kind == "tinanta"}


def test_upasarga_joined_to_the_root_by_sandhi():
    # प्र + आप् = प्राप् (6.1.101), अव + आप् = अवाप् (6.1.101), अधि + आपि = अध्यापि (6.1.77)
    assert "प्राप्" in _lemmas("प्राप्नोति") and "प्रआप्" not in _lemmas("प्राप्नोति")
    assert "अवाप्" in _lemmas("अवाप्स्यसि")
    assert "अध्यापि" in _lemmas("अध्यापयति") and "अधिआपि" not in _lemmas("अध्यापयति")


def test_gati_kept_in_the_lemma():
    assert "अन्तर्धा" in {m.lemma for m in lexicon.padas("अन्तरधीयत")}


def test_mit_causative_is_shortened():
    # 6.4.92 मितां ह्रस्वः: गमयति, शमयति have गमि, शमि
    assert "गमि" in _lemmas("गमयति") and "गामि" not in _lemmas("गमयति")
    assert "शमि" in _lemmas("शमयति")


def test_unseen_stem_spelled_like_a_frequent_indeclinable_in_r():
    assert all(m.quality <= 1 for m in lexicon.padas("पुनस्"))
    assert any(m.kind == "avyaya" and m.quality == 3 for m in lexicon.padas("पुनर्"))


def test_frequent_free_word_is_no_compound_member():
    for form in ("ततस्", "मा", "स्वित्"):
        assert not segmenter._stem_ok(form, segmenter._analyses(form, True)), form
    for form in ("सु", "प्रति", "सह", "राज"):  # prefixes the compound rules name, and ordinary stems
        assert segmenter._stem_ok(form, segmenter._analyses(form, True)), form


def _padas(text):
    return [lipi.pausa(w.form) + ("-" if w.in_compound else "") for w in analyze_verse(text).readings[0].words]


def test_readings_with_the_fixes():
    assert _padas("पुनः पुनः") == ["पुनः", "पुनः"]
    assert _padas("ततोसौ वानरः कथयति")[:2] == ["ततः", "असौ"]
    assert "स्वित्" in _padas("मा गृधः कस्यस्विद्धनम्")
