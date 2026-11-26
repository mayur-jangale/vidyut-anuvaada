import itertools
import time

from mayur import segmenter


def _rank(seg, words, limit=5000):
    for n, sp in enumerate(itertools.islice(seg.iter_splits(), limit)):
        if [(w.form, w.in_compound) for w in sp.words] == words:
            return n + 1
    return None


def test_shveto_dhavati_both_readings():
    seg = segmenter.segment_line("श्वेतो धावति")
    forms = [[w.form for w in sp.words] for sp in seg.iter_splits()]
    assert ["श्वेतस्", "धावति"] in forms
    assert ["श्वा", "इतस्", "धावति"] in forms
    assert seg.count >= 2 and seg.tier == 0


def test_gold_tapas():
    seg = segmenter.segment_line("तपःस्वाध्यायनिरतं तपस्वी वाग्विदां वरम्")
    gold = [("तपस्", True), ("स्वाध्याय", True), ("निरतम्", False), ("तपस्वी", False),
            ("वाक्", True), ("विदाम्", False), ("वरम्", False)]
    assert _rank(seg, gold) is not None


def test_gold_ko_nu():
    seg = segmenter.segment_line("को न्वस्मिन्साम्प्रतं लोके गुणवान्कश्च वीर्यवान्")
    gold = [("कस्", False), ("नु", False), ("अस्मिन्", False), ("साम्प्रतम्", False), ("लोके", False),
            ("गुणवान्", False), ("कस्", False), ("च", False), ("वीर्यवान्", False)]
    assert _rank(seg, gold) is not None


def test_gold_dharmajna():
    seg = segmenter.segment_line("धर्मज्ञश्च कृतज्ञश्च सत्यवाक्यो दृढव्रतः")
    forms = [[w.form for w in sp.words] for sp in itertools.islice(seg.iter_splits(), 5000)]
    assert any(f[:4] == ["धर्मज्ञस्", "च", "कृतज्ञस्", "च"] for f in forms)


def test_junctions_and_spans():
    seg = segmenter.segment_line("श्वेतो धावति")
    best = seg.splits[0]
    assert len(best.junctions) == len(best.words) - 1
    assert best.words[0].start == 0 and best.words[-1].end == 9 or best.words[-1].end > 0


def test_speed_32_syllables():
    line = "तपःस्वाध्यायनिरतं तपस्वी वाग्विदां वरम्"
    segmenter.segment_line(line)
    t = time.time()
    segmenter.segment_line("नारदं परिपप्रच्छ वाल्मीकिर्मुनिपुंगवम्")
    assert time.time() - t < 1.0


def test_fallback_never_fails():
    seg = segmenter.segment_line("क्ष्ट्रप्")
    assert seg.splits and seg.tier >= 1
