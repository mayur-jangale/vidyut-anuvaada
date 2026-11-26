import pytest

from mayur import lexicon as L

PADAS = ("वाल्मीकिस् नारदम् परिपप्रच्छ निरतम् तपस्वी विदाम् वरम् कस् नु अस्मिन् साम्प्रतम् सांप्रतम् लोके "
         "गुणवान् च वीर्यवान् कृतज्ञस् वाक्यस् व्रतस् अहम् मे त्वम् असि इच्छामि श्रोतुम् ज्ञातुम् हि बिभ्यति "
         "देवास् श्वा इतस् श्वेतस् धावति पुंगवम् पुङ्गवम् पर्यपृच्छत् प्रत्युवाच उपागमत्").split()
# महा (of महत्) is not claimed as derived: see test_proof_gate.py
STEMS = "तपस् स्वाध्याय वाक् मुनि धर्म सत्य दृढ जित जात अ".split()


@pytest.mark.parametrize("form", PADAS)
def test_pada_analysed_and_proved(form):
    ms = L.padas(form)
    assert ms and ms[0].quality >= 2
    assert any(L.prove(m).derivable for m in ms)


def test_enclitic_me_listed_not_forced():
    ms = L.padas("मे")
    assert ms[0].lemma == "अस्मद्" and ms[0].source == "kosha"
    proof = L.prove(ms[0])
    assert not proof.derivable and "8.1.2" in proof.note


def test_pronoun_and_verb_ranking():
    assert L.padas("अहम्")[0].lemma == "अस्मद्"
    assert L.padas("त्वम्")[0].lemma == "युष्मद्"
    assert L.padas("बिभ्यति")[0].kind == "tinanta"
    assert L.padas("असि")[0].kind == "tinanta"


def test_lyap_after_prefixes():
    m = L.padas("अनुप्राप्य")[0]
    assert m.krt == "ल्यप्" and m.prefixes == ("अनु", "प्र") and L.prove(m).derivable


def test_stem_cited_with_final_consonant():
    assert L.stems("वाच्")[0].lemma == "वाच्"
    assert L.padas("संनिभैस्")


@pytest.mark.parametrize("form", STEMS)
def test_stem_analysed_and_proved(form):
    ms = L.stems(form)
    assert ms and all(m.kind == "stem" for m in ms)
    proof = L.prove(ms[0])
    assert proof.derivable and "2.4.71" in proof.note


def test_paripapraccha_prefixed():
    m = L.padas("परिपप्रच्छ")[0]
    assert m.kind == "tinanta" and m.lemma == "परिप्रच्छ्" and m.prefixes == ("परि",)
    assert m.lakara == "लिट्" and m.purusha == "प्रथमपुरुष" and m.vacana == "एकवचन"
    proof = L.prove(m)
    assert proof.derivable and proof.derived_form == "परिपप्रच्छ"
    assert all(step.code[0].isdigit() for step in proof.trace)


def test_niratam_krdanta():
    m = L.padas("निरतम्")[0]
    assert (m.lemma, m.stem, m.root, m.krt) == ("निरम्", "निरत", "रम्", "क्त")
    assert m.root_gloss


def test_junk_last_and_quality():
    ms = L.padas("तपस्")
    assert ms[-1].quality <= ms[0].quality
    assert L.padas("वाल्मीकिस्")[0].linga == "पुंलिङ्ग"


def test_devanagari_only():
    import re
    for form in ("निरतम्", "परिपप्रच्छ", "तपस्वी"):
        for m in L.padas(form):
            for v in (m.lemma, m.stem, m.linga, m.vibhakti, m.krt, m.dhatu, m.lakara):
                assert not v or not re.search(r"[A-Za-z]", v)
        for step in L.prove(L.padas(form)[0]).trace:
            assert not re.search(r"[A-Za-z]", step.source + step.result)


def test_nonwords():
    assert L.padas("क्ष्ज्ञ्") == ()
    assert not L.is_pada("क्ष्ज्ञ्") and L.is_pada("च") and L.is_stem("धर्म") and not L.is_stem("धर्मस्")


def test_generated():
    ms = L.generated("रामेण")
    assert ms and ms[0].source == "generated" and ms[0].vibhakti == "तृतीया"
    proof = L.prove(ms[0])  # the ending is derived, but a stem fitted to the form proves nothing about the word
    assert not proof.derivable and proof.derived_form == "रामेण" and "not in the dictionary" in proof.note


def test_anvadesha_special():
    ms = L.padas("एनम्")
    assert {m.lemma for m in ms} >= {"इदम्", "एतद्"}
    assert (ms[0].linga, ms[0].vibhakti, ms[0].vacana) == ("पुंलिङ्ग", "द्वितीया", "एकवचन")
    proof = L.prove(ms[0])
    assert not proof.derivable and proof.trace == [] and "2.4.34" in proof.note


@pytest.mark.parametrize("form,lemma", [("कश्चित्", "कश्चित्"), ("केचिद्", "कश्चित्"), ("काचित्", "कश्चित्"),
                                        ("कस्यचित्", "कश्चित्"), ("क्वचित्", "क्वचिद्"), ("कश्चन", "कश्चन")])
def test_indefinites(form, lemma):
    m = L.padas(form)[0]
    assert m.lemma == lemma and m.source == "generated"
    proof = L.prove(m)
    assert proof.derivable and "अव्यय" in proof.note


def test_kosha_listed_method():
    proof = L.prove(L.padas("मे")[0])
    assert proof.method == "kosha-listed"
    assert proof.note == "listed in vidyut-kosha; enclitic by 8.1.20–23, which vidyut's Python API does not derive"


def test_more_stems_and_participles():
    assert L.stems("समिध्")[0].lemma == "समिध्"
    assert L.stems("वधू")[0].lemma == "वधू"
    m = L.padas("उद्वहन्त्यास्")[0]
    assert m.krt == "शतृ" and L.prove(m).derivable
    assert L.prove(L.padas("विवस्वान्")[0]).derivable


def test_upasarga_aa_written_as_aa():
    m = [m for m in L.padas("आनय") if m.kind == "tinanta"][0]
    assert "आ" in m.prefixes and "आङ्" not in m.prefixes


def test_maha_stem_lemma():
    m = L.stems("महा")[0]
    assert m.lemma == "महत्" and m.stem == ""


def test_sa_esha_special():
    m = [m for m in L.padas("एष") if m.source == "special"][0]
    assert (m.lemma, m.vibhakti, m.source) == ("एतद्", "प्रथमा", "special")
    proof = L.prove(m)
    assert not proof.derivable and "6.1.132" in proof.note
    assert L.padas("स")[0].lemma == "तद्"


def test_ena_dcs_lemma_present():
    assert "एनद्" in {m.lemma for m in L.padas("एनम्")}


@pytest.mark.parametrize("form,lemma", [("प्राप्तस्", "प्राप्"), ("प्रणम्य", "प्रणम्"), ("एत्य", "ए"),
                                        ("कारयेत्", "कारय्"), ("कथयति", "कथय्"), ("अचिन्तयत्", "चिन्तय्")])
def test_verbal_lemma_sandhi_joined(form, lemma):
    assert lemma in {L.verbal_lemma(m) for m in L.padas(form) if m.root}


def test_pronoun_stems_voiced():
    assert L.stems("मद्")[0].lemma == "अस्मद्" and L.stems("त्वद्")[0].lemma == "युष्मद्"


@pytest.mark.parametrize("form,lemma,krt", [("विचिन्त्य", "विचिन्तय्", "ल्यप्"), ("परित्यज्य", "परित्यज्", "ल्यप्"),
                                            ("पुरस्कृत्य", "पुरस्कृ", "ल्यप्"), ("निश्चित्य", "निश्चि", "ल्यप्"),
                                            ("सम्पन्नस्", "सम्पद्", "क्त")])
def test_prefixed_krdanta_always_offered(form, lemma, krt):
    from mayur import ud

    ms = [m for m in L.padas(form) if ud.lemma(m) == lemma and m.krt == krt]
    assert ms and L.prove(ms[0]).derivable


@pytest.mark.parametrize("form,lemma", [("पश्य", "पश्"), ("दध्यौ", "ध्या"), ("अगात्", "गा"), ("प्राह", "प्राह्")])
def test_corpus_citation_of_roots(form, lemma):
    from mayur import ud

    assert lemma in {ud.lemma(m) for m in L.padas(form)}


def test_participle_also_adjective():
    m = [m for m in L.padas("समन्वितस्") if m.lemma == "समन्वित" and not m.krt]
    assert m and L.prove(m[0]).derivable


@pytest.mark.parametrize("form,lemma", [("अनुष्ठितम्", "अनुष्ठा"), ("उत्थितस्", "उत्था"), ("उत्थाय", "उत्था"),
                                        ("अभ्यषिञ्चत्", "अभिषिच्"), ("न्यषेधत्", "निषिध्"), ("निषेदुस्", "निषद्")])
def test_retroflexed_prefixed_roots(form, lemma):
    from mayur import ud

    ms = [m for m in L.padas(form) if ud.lemma(m) == lemma]
    assert ms and L.prove(ms[0]).derivable


@pytest.mark.parametrize("form", ["किंतु", "किंच", "क्वापि", "कदापि", "किमु", "यथाशक्ति", "यथाक्रमम्"])
def test_avyaya_compounds(form):
    ms = [m for m in L.padas(form) if m.kind == "avyaya" and m.lemma == form]
    assert ms and ms[0].source == "generated"
    proof = L.prove(ms[0])
    assert not proof.derivable and proof.trace == [] and "not derived" in proof.note


@pytest.mark.parametrize("form,lemma", [("उन्नत", "उन्नम्"), ("प्रदीप्त", "प्रदीप्"), ("जनित", "जनय्")])
def test_participle_stems_in_compounds(form, lemma):
    from mayur import ud

    ms = [m for m in L.stems(form) if ud.lemma(m) == lemma]
    assert ms and L.prove(ms[0]).derivable


def test_prefix_joins():
    assert [L._join(a, b) for a, b in (("निस्", "क्रम्"), ("निर्", "चि"), ("निर्", "गम्"), ("उद्", "नम्"),
                                        ("अनु", "स्था"), ("पुरस्", "कृ"))] == \
        ["निष्क्रम्", "निश्चि", "निर्गम्", "उन्नम्", "अनुष्ठा", "पुरस्कृ"]


def test_tasi_ablative():
    ms = [m for m in L.padas("अनुरागतस्") if m.vibhakti == "पञ्चमी"]
    assert ms and ms[0].lemma == "अनुराग" and L.prove(ms[0]).derivable
    assert not [m for m in L.padas("इतस्") if m.lemma == "इ" and m.source == "generated"]


def test_nanj_stem():
    m = L.stems("अमित")[0]
    assert m.lemma == "अमित" and m.source == "generated"
    proof = L.prove(m)
    assert not proof.derivable and "नञ्" in proof.note and proof.trace


def test_n_numerals():
    from mayur import ud

    assert "पञ्चन्" in {ud.lemma(m) for m in L.padas("पञ्च")}
    m = [m for m in L.padas("पञ्चभिस्") if m.lemma == "पञ्चन्"][0]
    assert m.vibhakti == "तृतीया" and L.prove(m).derivable
    assert "पञ्चन्" in {m.lemma for m in L.stems("पञ्च")}


def test_lyap_of_vowel_roots_and_long_vowel_prefix():
    from mayur import ud

    assert "परिज्ञा" in {ud.lemma(m) for m in L.padas("परिज्ञाय")}
    assert "परीक्ष्" in {ud.lemma(m) for m in L.padas("परीक्षेत")}
