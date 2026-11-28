import dataclasses
import sys
from pathlib import Path

import pytest
from syntax_fixtures import nom, verb

from mayur import dcs, tagger

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import train_tagger as tt  # noqa: E402


def _verse():
    rama = nom("रामस्", "राम", "प्रथमा")
    vanam_n, vanam_a = nom("वनम्", "वन", "प्रथमा", "नपुंसकलिङ्ग"), nom("वनम्", "वन", "द्वितीया", "नपुंसकलिङ्ग")
    gacchati = verb("गच्छति", "गम्", "लट्")
    return [[rama], [vanam_n, vanam_a], [gacchati]], [0, 0, 0], [False] * 3, ["रामस्", "वनम्", "गच्छति"]


def test_tag_and_keys_are_devanagari_values():
    m = nom("रामस्", "राम", "प्रथमा")
    assert tagger.tag(m).startswith("subanta|प्रथमा|एकवचन|पुंलिङ्ग")
    assert tagger.keys(m)[1:] == ("Cप्रथमा", "Gपुंलिङ्ग", "Nएकवचन")


def test_choose_new_api_uses_weights():
    cands, lines, cpd, forms = _verse()
    w = {"accV": {"Cद्वितीया": 1.0}}
    assert tagger.choose_indices(cands, lines, cpd, forms, weights=w, neural_bonus=[]) == [0, 1, 0]
    w = {"w=वनम्": {"Cप्रथमा": 1.0}}
    assert tagger.choose_indices(cands, lines, cpd, forms, weights=w, neural_bonus=[]) == [0, 0, 0]


def test_decode_is_deterministic_and_handles_empty_candidates():
    cands, lines, cpd, forms = _verse()
    cands = cands + [[]]
    args = (cands, lines + [0], cpd + [False], forms + ["क"])
    w = {"b": {"Cद्वितीया": 0.5}}
    first = tagger.choose_indices(*args, weights=w)
    assert first == tagger.choose_indices(*args, weights=w) and len(first) == 4


def test_perceptron_learns_a_toy_verse():
    cands, lines, cpd, forms = _verse()
    gold = [(0,), (1,), (0,)]
    w = tt.train([((cands, lines, cpd, forms, None), gold)], epochs=3)
    assert tagger.choose_indices(cands, lines, cpd, forms, weights=w, neural_bonus=[]) == [0, 1, 0]


def test_model_file_is_optional(tmp_path):
    tagger.load.cache_clear()
    assert tagger.load(str(tmp_path / "missing.json")) is None
    tagger.load.cache_clear()
    assert isinstance(tagger.enabled(), bool)


@pytest.mark.skipif(not dcs.split_files("train"), reason="DCS split manifest missing")
def test_tiny_training_beats_frequency_baseline():
    items = [it for _b, it in tt.load_train(4000)][:200]
    data = [(tt.verse_args(it, tt.minus_of(it)), it["gold"], tt.verse_kw(it)) for it in items]
    w = tt.train(data, epochs=2)

    def acc(choose) -> float:
        n = ok = 0
        for it in items:
            for t, c, p in zip(it["toks"], it["cands"], choose(it)):
                if c and not t["compound_member"]:
                    n, ok = n + 1, ok + tt.correct(c[p], t)
        return ok / n

    freq = lambda it: [tagger.Verse(*tt.verse_args(it), **tt.verse_kw(it)).top[i] if c else 0 for i, c in enumerate(it["cands"])]
    assert acc(lambda it: tt.learned_choice(it, w, False)) > acc(freq)


def test_structural_features_use_tables():
    phala = nom("फलम्", "फल", "द्वितीया", "नपुंसकलिङ्ग")
    phala_m = nom("फलम्", "फल", "द्वितीया", "पुंलिङ्ग")
    tables = {"g": {"फल": {"नपुंसकलिङ्ग": 0.9, "पुंलिङ्ग": 0.1}}, "acc": {}, "dat": {}}
    v = tagger.Verse([[phala, phala_m]], [0], [False], ["फलम्"], tables=tables)
    assert "gpTop=1" in v.static[0][0] and "gpTop=0" in v.static[0][1]


def test_agent_noun_with_adjacent_genitive_feature():
    agent = nom("रक्षिता", "रक्षितृ", "प्रथमा", krt="तृच्")
    gen = nom("धर्मस्य", "धर्म", "षष्ठी")
    v = tagger.Verse([[agent], [gen]], [0, 0], [False, False], ["रक्षिता", "धर्मस्य"], tables={})
    assert "trcGen" in v.static[0][0]


def test_sibling_forms_of_a_surface_spelling():
    from mayur.tagger_siblings import sibling_form, surface, variant
    assert sibling_form("मूढा", "ज्ञानिनस्") == "मूढास्"  # 8.3.17, 8.3.22: -आः loses its visarga before a voiced sound
    assert sibling_form("मूढास्", "ज्ञानिनस्") == "मूढा"
    assert sibling_form("मूढा", "तत्र") is None  # before a voiceless sound the visarga stays
    assert sibling_form("भीष्मे", "उवाच") == "भीष्मस्"  # 6.1.78 / 8.3.19: both end in -अ with hiatus
    assert sibling_form("भीष्मस्", "उवाच") == "भीष्मे"
    assert sibling_form("रामस्", "अत्र") is None  # before अ: रामोऽत्र
    from mayur.tagger_siblings import sibling_forms
    assert set(sibling_forms("भीष्म", "उवाच")) == {"भीष्मस्", "भीष्मे"}  # the vocative has the same spelling too
    assert "भीष्म" in sibling_forms("भीष्मस्", "उवाच") and "भीष्म" in sibling_forms("भीष्मे", "उवाच")
    assert variant("भीष्म") == "अ" and variant("भीष्मस्") == "अस्"
    assert surface("मूढा", "मूढास्") == surface("मूढास्", "मूढा") == "मूढा"
    assert (variant("मूढास्"), variant("मूढा"), variant("भीष्मे"), variant("भीष्मस्")) == ("आस्", "आ", "ए", "अस्")


def test_choose_with_siblings_returns_the_swap():
    fem = nom("मूढा", "मूढ", "प्रथमा", "स्त्रीलिङ्ग")
    pl = nom("मूढास्", "मूढ", "प्रथमा", vacana="बहुवचन")
    v = verb("पतन्ति", "पत्", "लट्")
    v = dataclasses.replace(v, vacana="बहुवचन")
    w = {"var=आस्": {"Nबहुवचन": 2.0}}
    chosen, swaps = tagger.choose_with_siblings([[fem], [v]], [0, 0], [False, False], ["मूढा", "नरास्"],
                                                weights=w, sibling_candidates=lambda f: [pl] if f == "मूढास्" else [])
    assert chosen[0] is pl and swaps == {0: "मूढास्"}
    chosen, swaps = tagger.choose_with_siblings([[fem], [v]], [0, 0], [False, False], ["मूढा", "नरास्"],
                                                weights={}, sibling_candidates=lambda f: [pl] if f == "मूढास्" else [])
    assert chosen[0] is fem and swaps == {}


def test_coordinated_nominatives_feature_marks_the_dual_verb():
    rama, laksmana = nom("रामस्", "राम", "प्रथमा"), nom("लक्ष्मणस्", "लक्ष्मण", "प्रथमा")
    ca = tagger.Morph(form="च", lemma="च", kind="avyaya")
    dual = dataclasses.replace(verb("गच्छतस्", "गम्", "लट्"), vacana="द्विवचन")
    gen = nom("गच्छतस्", "गम्", "षष्ठी", krt="शतृ")
    v = tagger.Verse([[rama], [laksmana], [ca], [dual, gen]], [0] * 4, [False] * 4,
                     ["रामस्", "लक्ष्मणस्", "च", "गच्छतस्"], tables={})
    assert "coord2=द्विवचनV" in v.static[3][0] and "coord2=द्विवचनV" not in v.static[3][1]


def test_coordinated_singular_nominatives_take_the_dual_verb():
    from mayur.model import Word
    rama, laksmana = nom("रामस्", "राम", "प्रथमा"), nom("लक्ष्मणस्", "लक्ष्मण", "प्रथमा")
    ca = tagger.Morph(form="च", lemma="च", kind="avyaya")
    vanam = nom("वनम्", "वन", "द्वितीया", "नपुंसकलिङ्ग")
    gen = nom("गच्छतस्", "गम्", "षष्ठी", krt="शतृ")
    dual = dataclasses.replace(verb("गच्छतस्", "गम्", "लट्"), vacana="द्विवचन")
    forms = [("रामस्", [rama]), ("लक्ष्मणस्", [laksmana]), ("च", [ca]), ("वनम्", [vanam]), ("गच्छतस्", [gen, dual])]
    words = [Word(form=f, line=0, start=k, end=k + 1, analyses=a) for k, (f, a) in enumerate(forms)]
    assert tagger._coordinated_agent_verb(words, [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 1]
    words[1] = Word(form="तस्य", line=0, start=1, end=2, analyses=[nom("तस्य", "तद्", "षष्ठी")])
    assert tagger._coordinated_agent_verb(words, [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]  # one nominative: no
