"""Citation and feature conventions of ``mayur.ud`` / ``mayur.lexicon_cite`` added from the dev error analysis."""

from mayur import ud
from mayur.lexicon_cite import _join, verbal_lemma
from mayur.model import Morph

F, M, N = "स्त्रीलिङ्ग", "पुंलिङ्ग", "नपुंसकलिङ्ग"


def _nom(form, lemma, linga=M, case="प्रथमा", vacana="एकवचन"):
    return Morph(form=form, lemma=lemma, kind="subanta", linga=linga, vibhakti=case, vacana=vacana)


def _verb(form, lemma, lakara="लट्", purusha="प्रथमपुरुष", vacana="एकवचन", prefixes=(), root=None):
    return Morph(form=form, lemma=lemma, kind="tinanta", lakara=lakara, purusha=purusha, vacana=vacana,
                 prefixes=prefixes, root=root or lemma, prayoga="कर्तरि")


def test_ubha_is_cited_with_viraama():
    assert ud.same_lemma(_nom("उभौ", "उभ", vacana="द्विवचन"), "उभ्", "PRON")


def test_feminine_pronoun_stem():
    assert ud.same_lemma(_nom("ताम्", "तद्", F, "द्वितीया"), "ता", "PRON")
    assert ud.same_lemma(_nom("ताम्", "ता", F, "द्वितीया"), "तद्", "PRON")
    assert not ud.same_lemma(_nom("तम्", "तद्", M, "द्वितीया"), "ता", "PRON")


def test_bahuvrihi_final_shortened_feminine_1_2_48():
    assert ud.same_lemma(_nom("प्रभम्", "प्रभ", N, "द्वितीया"), "प्रभा", "NOUN")
    assert ud.same_lemma(_nom("मर्यादस्", "मर्याद", M), "मर्यादा", "NOUN")
    assert not ud.same_lemma(_nom("प्रभा", "प्रभ", F), "प्रभा", "NOUN")  # a feminine keeps its -आ


def test_anusvara_and_class_nasal_are_one_spelling():
    assert ud.canonical_lemma("सांप्रतम्") == ud.canonical_lemma("साम्प्रतम्")
    assert ud.canonical_lemma("संज्ञा") == "सञ्ज्ञा"
    assert ud.canonical_lemma("संयम्") == "संयम्"  # before a non-stop the anusvara stays


def test_indeclinable_final_t_and_d():
    cet = Morph(form="चेत्", lemma="चेत्", kind="avyaya")
    assert ud.same_lemma(cet, "चेद्", "PART")


def test_pashya_counts_for_drsh():
    assert ud.same_lemma(_verb("पश्यन्ति", "पश्", vacana="बहुवचन", root="पश्"), "दृश्", "VERB")


def test_perfect_endings_of_vid_and_bru_3_4_83_84():
    past = {"Tense": "Past", "Mood": "Ind", "Person": "3", "Number": "Plur"}
    viduh = _verb("विदुस्", "विद्", vacana="बहुवचन")
    assert ud.perfect_ending_present(viduh) and ud.same_feats(viduh, "VERB", past)
    assert ud.same_feats(viduh, "VERB", {**past, "Tense": "Pres"})
    vetti = _verb("वेत्ति", "विद्")
    assert not ud.perfect_ending_present(vetti)
    assert not ud.same_feats(vetti, "VERB", {**past, "Number": "Sing"})


def test_nrt_is_not_natva_root():
    assert _join("प्र", "नृत्") == "प्रनृत्"
    assert _join("प्र", "नम्") == "प्रणम्"


def test_sut_after_pari_and_sam_6_1_137():
    m = Morph(form="परिष्कृतैस्", lemma="कृ", kind="subanta", root="कृ", prefixes=("परि",), krt="क्त",
              linga=M, vibhakti="तृतीया", vacana="बहुवचन")
    assert verbal_lemma(m) == "परिष्कृ"
    plain = Morph(form="परिकृतम्", lemma="कृ", kind="subanta", root="कृ", prefixes=("परि",), krt="क्त",
                  linga=N, vibhakti="प्रथमा", vacana="एकवचन")
    assert verbal_lemma(plain) != "परिष्कृ"
