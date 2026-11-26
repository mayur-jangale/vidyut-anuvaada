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
    assert tagger.choose_indices(cands, lines, cpd, forms, weights=w) == [0, 1, 0]
    w = {"w=वनम्": {"Cप्रथमा": 1.0}}
    assert tagger.choose_indices(cands, lines, cpd, forms, weights=w) == [0, 0, 0]


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
    assert tagger.choose_indices(cands, lines, cpd, forms, weights=w) == [0, 1, 0]


def test_model_file_is_optional(tmp_path):
    tagger.load.cache_clear()
    assert tagger.load(str(tmp_path / "missing.json")) is None
    tagger.load.cache_clear()
    assert isinstance(tagger.enabled(), bool)


@pytest.mark.skipif(not dcs.split_files("train"), reason="DCS split manifest missing")
def test_tiny_training_beats_frequency_baseline():
    items = [it for _b, it in tt.load_train(4000)][:200]
    data = [(tt.verse_args(it, tt.minus_of(it)), it["gold"]) for it in items]
    w = tt.train(data, epochs=2)

    def acc(choose) -> float:
        n = ok = 0
        for it in items:
            for t, c, p in zip(it["toks"], it["cands"], choose(it)):
                if c and not t["compound_member"]:
                    n, ok = n + 1, ok + tt.correct(c[p], t)
        return ok / n

    freq = lambda it: [tagger.Verse(*tt.verse_args(it)).top[i] if c else 0 for i, c in enumerate(it["cands"])]
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
