import pytest

from mayur import sandhi


def texts(left, right, samasa=False):
    return {o.text: o.sutras for o in sandhi.outcomes(left, right, samasa)}


@pytest.mark.parametrize(
    "left,right,samasa,expected,sutra",
    [
        ("श्वा", "इतस्", False, "श्वेतस्", "६.१.८७"),
        ("राम", "आलयम्", False, "रामालयम्", "६.१.१०१"),
        ("तव", "एव", False, "तवैव", "६.१.८८"),
        ("इति", "अत्र", False, "इत्यत्र", "६.१.७७"),
        ("वने", "अस्मिन्", False, "वनेऽस्मिन्", "६.१.१०९"),
        ("रामस्", "अत्र", False, "रामोऽत्र", "६.१.११३"),
        ("श्वेतस्", "धावति", False, "श्वेतोधावति", "६.१.११४"),
        ("हरिस्", "गच्छति", False, "हरिर्गच्छति", "८.२.६६"),
        ("हरिस्", "रमते", False, "हरीरमते", "८.३.१४"),
        ("रामस्", "च", False, "रामश्च", "८.३.३४"),
        ("रामस्", "कथम्", False, "रामःकथम्", "८.३.१५"),
        ("सस्", "गच्छति", False, "सगच्छति", "६.१.१३२"),
        ("वनम्", "गच्छति", False, "वनंगच्छति", "८.३.२३"),
        ("तान्", "च", False, "तांश्च", "८.३.७"),
        ("अस्मिन्", "अपि", False, "अस्मिन्नपि", "८.३.३२"),
        ("तत्", "च", False, "तच्च", "८.४.४०"),
        ("तत्", "शिवम्", False, "तच्छिवम्", "८.४.६३"),
        ("वाक्", "विदाम्", True, "वाग्विदाम्", "८.२.३९"),
        ("तपस्", "स्वाध्याय", True, "तपःस्वाध्याय", "८.३.३६"),
        ("तत्", "हि", False, "तद्धि", "८.४.६२"),
        ("वाक्", "मयम्", False, "वाङ्मयम्", "८.४.४५"),
    ],
)
def test_outcomes(left, right, samasa, expected, sutra):
    found = texts(left, right, samasa)
    assert expected in found
    assert sutra in found[expected]


def test_avagraha_both_spellings():
    found = texts("रामस्", "अत्र")
    assert "रामोऽत्र" in found and "रामोत्र" in found


def test_punar_keeps_r():
    assert "पुनरागतस्" in texts("पुनर्", "आगतस्")
    assert "पुनर्गच्छति" in texts("पुनर्", "गच्छति")


def test_samasa_cites_pada_status():
    assert "१.४.१४" in texts("मुनि", "पुंगव", True)["मुनिपुंगव"]


def test_rejoin_compound_line():
    got = {sandhi.canon(x) for x in sandhi.rejoin(["तपस्", "स्वाध्याय", "निरतम्"], [True, True, False])}
    assert sandhi.canon("तपःस्वाध्यायनिरतं") in got


def test_rejoin_chain():
    got = {sandhi.canon(x) for x in sandhi.rejoin(["कस्", "नु", "अस्मिन्", "साम्प्रतम्"], [False] * 4)}
    assert sandhi.canon("को न्वस्मिन्साम्प्रतं") in got


def test_pausa_forms():
    assert sandhi.pausa_forms("रामस्") == ("रामः",)
    assert set(sandhi.pausa_forms("वरम्")) == {"वरम्", "वरं"}


def test_canon():
    assert sandhi.canon("मुनिपुंगव") == sandhi.canon("मुनिपुङ्गव")
    assert sandhi.canon("निरतं तपस्वी") == "निरतन्तपस्वी"
    assert sandhi.canon("वरं") == sandhi.canon("वरम्")


def test_palatal_final_becomes_velar():  # 8.2.30
    found = texts("प्राच्", "मुखास्", True)
    assert "प्राङ्मुखास्" in found and "८.२.३०" in found["प्राङ्मुखास्"]
    assert "वाक्" in sandhi.pausa_forms("वाच्")


def test_sh_final_becomes_retroflex():  # 8.2.36
    assert "प्रावृट्काले" in texts("प्रावृष्", "काले", True) or "प्रावृट्काले" in texts("प्रावृश्", "काले", True)


def test_n_before_l_with_anusvara():  # 8.4.60, 8.3.4
    assert "तांल्लोकान्" in texts("तान्", "लोकान्")


def test_pragrhya_stays_unjoined():  # 1.1.11, 6.1.125
    assert "१.१.११" in texts("ते", "आसने").get("तेआसने", ())


def test_pada_hiatus_only_marked():
    assert sandhi.PADA_HIATUS in texts("एव", "आर्जवम्")["एवआर्जवम्"]


def test_pada_hiatus_needs_space():
    from mayur import segmenter
    assert segmenter.contains("चैव आर्जवम्", ["च", "एव", "आर्जवम्"], [False] * 3)
    assert not segmenter.contains("चैवआर्जवम्", ["च", "एव", "आर्जवम्"], [False] * 3)


def test_nan_before_vowel_in_compound():  # 6.3.74
    assert "अनसूयुस्" in texts("अन्", "असूयुस्", True)


def test_canon_unassimilated_m():
    assert sandhi.canon("युक्तम्गुणैः") == sandhi.canon("युक्तं गुणैः")


def test_raj_final_j_to_d():  # 8.2.36, 8.2.39
    assert "शैलराडिव" in texts("शैलराज्", "इव")


def test_optional_samhita_keeps_visarga():  # 1.4.109 kārikā
    assert sandhi.rejoin_matching(["युधिष्ठिरस्", "उवाच"], [False, False], "युधिष्ठिरः उवाच") is not None
