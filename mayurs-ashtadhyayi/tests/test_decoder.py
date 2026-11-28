from __future__ import annotations

import time

from mayur import decoder
from mayur.segmenter import segment_line

LINE = "धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः"
BASE = {"enabled": True, "weights": {"base": 1.0}, "tag_bigram": {}}


def _forms(split):
    return tuple((w.form, w.in_compound) for w in split.words)


def test_base_weights_reproduce_segmenter_best():
    for line in (LINE, "तपःस्वाध्यायनिरतं तपस्वी वाग्विदां वरम्", "श्वेतो धावति"):
        assert _forms(decoder.decode(line, 3, BASE)[0]) == _forms(segment_line(line, 1).splits[0])


def test_disabled_model_falls_back_to_segmenter():
    out = decoder.decode(LINE, 5, {"enabled": False, "weights": {"base": 2.0}})
    assert list(map(_forms, out)) == list(map(_forms, segment_line(LINE, 5).splits))


def test_k_best_distinct_and_sorted():
    out = decoder.decode(LINE, 12, {**BASE, "weights": {"base": 1.0, "tag_bigram": 0.3}})
    assert 1 < len(out) <= 12
    assert len(set(map(_forms, out))) == len(out)
    assert out[0].score == max(s.score for s in out)


def test_both_readings_reachable():
    out = decoder.decode("श्वेतो धावति", 12, BASE)
    forms = {tuple(w.form for w in s.words) for s in out}
    assert ("श्वेतस्", "धावति") in forms
    assert ("श्वा", "इतस्", "धावति") in forms


def test_features_deterministic_and_generic():
    lat = decoder.lattice(LINE)
    g1, _ = decoder.build_graph(lat, {})
    g2, _ = decoder.build_graph(decoder.lattice(LINE), {})
    assert g1 == g2
    assert all(k.split(":")[0].isascii() for e in g1.edges for k, _ in e.feats)
    pf = decoder.pair_features(("रामस्य", False, "subanta:षष्ठी"), ("वनम्", False, "subanta:प्रथमा"))
    assert dict(pf)["pair_gen_nominal"] == 1.0


def test_long_line_is_fast_enough():
    line = "स हत्वा राक्षसान् सर्वान् यज्ञघ्नान् रघुनन्दनः ऋषिभिः पूजितस् तत्र यथेन्द्रो विजये पुरा"
    decoder.decode(line, 12, BASE)  # warm the caches
    t = time.time()
    assert decoder.decode(line, 12, BASE)
    assert time.time() - t < 3.0


def test_enabled_is_bool():
    assert isinstance(decoder.enabled(), bool)


def test_unknown_edges_are_gated_and_flagged():
    line = "नारदं परिपप्रच्छ वाल्मीकिर्मुनिपुंगवम्"
    g0, _ = decoder.build_graph(decoder.lattice(line), {})
    g1, _ = decoder.build_graph(decoder.lattice(line, unknown=True), {})
    assert not any(e.unknown for e in g0.edges)
    unk = [e for e in g1.edges if e.unknown]
    assert 0 < len(unk) <= 3 * 3  # capped per chunk-start state
    assert all(dict(e.feats).get("unknown") == 1.0 for e in unk)


def test_neural_features_mapping():
    from mayur.decoder_stats import neural_features

    lat = decoder.lattice(LINE)
    g, _ = decoder.build_graph(lat, {})
    lps = [{"N": -0.1, "P": -2.0, "C": -3.0, "FP": -4.0, "FC": -5.0} for _ in g.text]
    e = next(e for e in g.edges if e.kind == "cpd" and e.slen == 0)
    f = dict(neural_features(g, e, lps))
    assert f["nb_junc"] == -3.0
    assert abs(f["nb_inside"] - (-0.1) * (e.end - 1 - e.start)) < 1e-9


def test_member_indeclinable_flag():
    from mayur import decoder_words as dw

    assert dict(dw.word_features("तथा", True)).get("w_member_indeclinable") == 1.0
    assert "w_member_indeclinable" not in dict(dw.word_features("राम", True))


def test_prefix_features_use_counts_not_lists():
    from mayur import decoder_words as dw

    table = {"स": {"गुण": 7}}
    f = dict(dw.prefix_features("सगुणस्", False, table))
    if dw.lemma_of("सगुणस्", False) == "सगुण":
        assert "prefix_split_logratio" in f
    assert dw.prefix_features("सगुणस्", False, {}) == ()
    assert dw.prefix_pair_features("स", "गुणस्", {}) == ()


def test_neural_model_refused_without_neural(monkeypatch, tmp_path):
    import json

    main, fallback = tmp_path / "m.json", tmp_path / "b.json"
    main.write_text(json.dumps({"enabled": True, "neural": True, "weights": {"base": 1.0}, "score_scale": 9.0}))
    fallback.write_text(json.dumps({"enabled": True, "neural": False, "weights": {"base": 1.0}, "score_scale": 5.0}))
    monkeypatch.setattr(decoder, "MODEL_FILE", main)
    monkeypatch.setattr(decoder, "FALLBACK_FILE", fallback)
    monkeypatch.setattr(decoder, "neural_available", lambda: False)
    decoder._model.cache_clear()
    try:
        import pytest

        with pytest.warns(RuntimeWarning):
            assert decoder.score_scale() == 5.0
    finally:
        decoder._model.cache_clear()


MADE_UP = "ग्लोकस्य ब्लिम्फति ट्रम्पः"
RARE_REAL = ("तस्यार्णवस्य क्षुब्धस्य तस्मिन्नम्भसि मन्थिते", "औतथ्यो वेदमत्रैव षडङ्गं प्रत्यधीयत")


def test_guard_keeps_unknown_chunks_whole():
    from mayur import unknown_guard

    out = decoder.decode(MADE_UP, 5)
    assert [w.form for w in out[0].words] == ["ग्लोकस्य", "ब्लिम्फति", "ट्रम्पस्"]
    assert len(out[0].junctions) == 2
    assert unknown_guard.rewrite(MADE_UP, out[0]) is out[0]  # idempotent


def test_guard_leaves_rare_real_words_alone():
    from mayur import unknown_guard

    for line in RARE_REAL:
        best = decoder.decode(line, 3)[0]
        assert not unknown_guard.unknown_chunks(line, best)
    assert "मन्थिते" in [w.form for w in decoder.decode(RARE_REAL[0], 3)[0].words]
    assert "औतथ्यस्" in [w.form for w in decoder.decode(RARE_REAL[1], 3)[0].words]


def test_made_up_line_is_three_unverified_arsha_words():
    from mayur import pipeline

    analysis = pipeline.analyze_verse(MADE_UP)
    reading = analysis.readings[0]
    assert [w.form for w in reading.words] == ["ग्लोकस्य", "ब्लिम्फति", "ट्रम्पस्"]
    assert all(w.arsha for w in reading.words)
    assert analysis.status == "unverified"
