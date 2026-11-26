from syntax_fixtures import nom, verb

from mayur import tagger


def test_features_have_no_word_identities():
    m = nom("रामस्", "राम", "प्रथमा")
    keys = set(tagger.unary(m)) | set(tagger.pair(m, m)) | set(tagger.sentence([m]))
    assert not any("राम" in k for k in keys)


def test_decode_uses_agreement_weights():
    acc, nomv = nom("वनम्", "वन", "द्वितीया", "नपुंसकलिङ्ग"), nom("वनम्", "वन", "प्रथमा", "नपुंसकलिङ्ग")
    rama = nom("रामस्", "राम", "प्रथमा")
    gacchati = verb("गच्छति", "गम्", "लट्")
    w = {"acc_verb": 2.0, "karta": 1.0}
    path = tagger.decode([[rama], [nomv, acc], [gacchati]], w)
    assert path == [0, 1, 0]


def test_decode_viterbi_pairs():
    a = nom("क", "क", "षष्ठी")
    b1, b2 = nom("ख", "ख", "सप्तमी"), nom("ख", "ख", "षष्ठी")
    assert tagger.decode([[a], [b1, b2]], {"agree": 1.0}) == [0, 1]
    assert tagger.decode([[a], [b1, b2]], {"cp:षष्ठी>सप्तमी": 1.0}) == [0, 0]


def test_global_features_sum():
    ms = [nom("रामस्", "राम", "प्रथमा"), verb("गच्छति", "गम्", "लट्")]
    f = tagger.features([[m] for m in ms], [0, 0])
    assert f["bias"] == 2.0 and f["karta"] == 1.0


def test_model_file_is_optional(tmp_path):
    tagger.load.cache_clear()
    assert tagger.load(str(tmp_path / "missing.json")) is None
    tagger.load.cache_clear()
