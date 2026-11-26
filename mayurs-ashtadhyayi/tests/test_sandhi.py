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
