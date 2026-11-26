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
