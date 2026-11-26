from __future__ import annotations

from mayur import ranker
from mayur.segmenter import segment_line

LINE = "धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः"


def _splits(line: str = LINE, k: int = 10):
    return list(segment_line(line, k).splits)


def test_features_deterministic_and_generic():
    s = _splits()[0]
    a, b = ranker.features(LINE, s, {}), ranker.features(LINE, s, {})
    assert a == b
    assert a["n_words"] == len(s.words)
    assert all(k.isascii() for k in a)  # English identifiers, no word identities


def test_rerank_is_permutation():
    splits = _splits()
    out = ranker.rerank(LINE, splits)
    key = lambda s: tuple((w.form, w.in_compound) for w in s.words)  # noqa: E731
    assert sorted(map(key, out)) == sorted(map(key, splits))
    assert len(out) == len(splits)


def test_no_model_keeps_order():
    splits = _splits()
    assert ranker.rerank(LINE, splits, model={}) == splits
    assert ranker.rerank(LINE, splits, model={"enabled": False, "weights": {"n_words": 1.0}}) == splits


def test_model_reorders_and_replaces_score():
    splits = _splits()
    model = {"enabled": True, "weights": {"n_words": -1.0}, "mean": {}, "std": {}}
    out = ranker.rerank(LINE, splits, model=model)
    assert [len(s.words) for s in out] == sorted(len(s.words) for s in splits)
    assert out[0].score == -len(out[0].words)


def test_both_readings_survive():
    line = "श्वेतो धावति"
    out = ranker.rerank(line, _splits(line, 20))
    forms = {tuple(w.form for w in s.words) for s in out}
    assert ("श्वेतस्", "धावति") in forms
    assert ("श्वा", "इतस्", "धावति") in forms


def test_syllables():
    assert ranker.syllables("राम") == 2
    assert ranker.syllables("क्षेत्रे") == 2
