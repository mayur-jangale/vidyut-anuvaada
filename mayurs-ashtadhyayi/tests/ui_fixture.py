"""A hand-made, realistic VerseAnalysis (Valmiki Ramayana 1.1.1) for UI and JSON tests."""

from __future__ import annotations

from mayur import lipi
from mayur.model import (
    UNVERIFIED, VERIFIED, Alignment, Compound, Junction, Morph, Reading, SutraStep, VerseAnalysis,
    Word, WordProof,
)

LINE1 = "तपःस्वाध्यायनिरतं तपस्वी वाग्विदां वरम्"
LINE2 = "नारदं परिपप्रच्छ वाल्मीकिर्मुनिपुङ्गवम्"
TEXT = LINE1 + " । " + LINE2

TRANSLATION = "Valmiki asked Narada, the best of sages, who is the best of the eloquent, an ascetic, devoted to austerity and study."


def _trace(n: int = 8) -> list[SutraStep]:
    base = [
        SutraStep("धातुपाठ", "1.1", "प्रच्छ्"),
        SutraStep("अष्टाध्यायी", "3.1.68", "प्रच्छ् + शप्"),
        SutraStep("अष्टाध्यायी", "3.2.115", "प्रच्छ् + लिट्"),
        SutraStep("अष्टाध्यायी", "6.1.8", "प्रच्छ्-प्रच्छ् + ल"),
        SutraStep("अष्टाध्यायी", "7.4.59", "प-प्रच्छ् + ल"),
        SutraStep("अष्टाध्यायी", "6.1.87", "परि + प-प्रच्छ् + अ"),
        SutraStep("अष्टाध्यायी", "8.2.36", "परि + पप्रच्छ्+ अ"),
        SutraStep("अष्टाध्यायी", "8.4.1", "परिपप्रच्छ"),
    ]
    return base[:n]


def _word(form, line, start, end, kind="subanta", lemma=None, **kw) -> Word:
    morph_kw = {k: kw.pop(k) for k in list(kw) if k in Morph.__dataclass_fields__}
    other = [
        Morph(form=form, lemma=lemma or form, kind="subanta", linga="नपुंसकलिङ्ग",
              vibhakti="प्रथमा", vacana="एकवचन", quality=1)
    ]
    return Word(
        form=form, line=line, start=start, end=end,
        analyses=[Morph(form=form, lemma=lemma or form, kind=kind, **morph_kw)] + other, **kw,
    )


def make_reading(rank: int = 0) -> Reading:
    s = lambda p: len(lipi.varnas(p))  # noqa: E731
    words = [
        _word("तपस्", 0, 0, s("तपस्"), lemma="तपस्", linga="नपुंसकलिङ्ग", in_compound=True, compound=0,
              role="समासपूर्वपद", gloss="austerity", gloss_source="mw", proof=WordProof(True, "lexicon", "तपस्")),
        _word("स्वाध्याय", 0, 4, 4 + s("स्वाध्याय"), lemma="स्वाध्याय", linga="पुंलिङ्ग", in_compound=True,
              compound=0, role="समासपूर्वपद", gloss="study of the scriptures", gloss_source="mw",
              proof=WordProof(True, "lexicon", "स्वाध्याय")),
        _word("निरतम्", 0, 11, 11 + s("निरतम्"), lemma="निरत", stem="निरत", linga="पुंलिङ्ग", vibhakti="द्वितीया",
              vacana="एकवचन", krt="क्त", root="रम्", prefixes=("नि",), compound=0, role="विशेषण", head=3,
              gloss="devoted to", gloss_source="mw",
              proof=WordProof(True, "derived by rules", "निरतम्", _trace(8))),
        _word("तपस्वी", 0, 18, 18 + s("तपस्वी"), lemma="तपस्विन्", linga="पुंलिङ्ग", vibhakti="द्वितीया",
              vacana="एकवचन", role="कर्म", gloss="ascetic", gloss_source="mw", arsha=True,
              proof=WordProof(False, "none", "", [], "द्वितीया रूप तपस्वी (तपस्विनम् के स्थान पर) आर्ष; not derivable by the rules")),
        _word("वाग्विदाम्", 0, 24, 24 + s("वाग्विदाम्"), lemma="वाग्विद्", linga="पुंलिङ्ग", vibhakti="षष्ठी",
              vacana="बहुवचन", role="सम्बन्ध", head=5, gloss="knowers of speech", gloss_source="mw",
              proof=WordProof(True, "lexicon", "वाग्विदाम्", _trace(5))),
        _word("वरम्", 0, 34, 34 + s("वरम्"), lemma="वर", linga="पुंलिङ्ग", vibhakti="द्वितीया",
              vacana="एकवचन", role="कर्म", gloss="best", gloss_source="mw",
              proof=WordProof(True, "lexicon", "वरम्", _trace(4))),
        _word("नारदम्", 1, 0, s("नारदम्"), lemma="नारद", linga="पुंलिङ्ग", vibhakti="द्वितीया",
              vacana="एकवचन", role="कर्म", head=7, gloss="Narada", gloss_source="mw",
              proof=WordProof(True, "lexicon", "नारदम्", _trace(6))),
        _word("परिपप्रच्छ", 1, 6, 6 + s("परिपप्रच्छ"), kind="tinanta", lemma="परिप्रच्छ्", root="प्रच्छ्",
              prefixes=("परि",), purusha="प्रथमपुरुष", vacana="एकवचन", lakara="लिट्", prayoga="कर्तरि",
              dhatu="प्रछ", gana="तुदादि", role="क्रिया", gloss="asked", gloss_source="mw",
              proof=WordProof(True, "derived by rules", "परिपप्रच्छ", _trace(8))),
        _word("वाल्मीकिस्", 1, 16, 16 + s("वाल्मीकिस्"), lemma="वाल्मीकि", linga="पुंलिङ्ग", vibhakti="प्रथमा",
              vacana="एकवचन", role="कर्ता", head=7, gloss="Valmiki", gloss_source="mw",
              proof=WordProof(True, "lexicon", "वाल्मीकिस्", _trace(3))),
        _word("मुनिपुङ्गवम्", 1, 26, 26 + s("मुनिपुङ्गवम्"), lemma="मुनिपुङ्गव", linga="पुंलिङ्ग",
              vibhakti="द्वितीया", vacana="एकवचन", role="विशेषण", head=6, gloss="best of sages",
              gloss_source="mw", proof=WordProof(True, "lexicon", "मुनिपुङ्गवम्", _trace(2))),
    ]
    junctions = [
        Junction(0, ("6.1.87",), True, "तपः"),
        Junction(1, ("6.1.77", "8.3.34"), True, "स्वाध्याय"),
        Junction(2, ("8.3.23", "8.4.58"), False, "निरतं"),
        Junction(3, (), False, "तपस्वी"),
        Junction(4, ("8.3.23",), False, "वाग्विदां"),
        Junction(5, (), False, "वरम्"),
        Junction(6, ("8.3.23",), False, "नारदं"),
        Junction(7, (), False, "परिपप्रच्छ"),
        Junction(8, ("6.1.87", "8.3.15"), False, "वाल्मीकिर्मुनि"),
    ]
    compounds = [
        Compound(0, [0, 1, 2], "तपःस्वाध्यायनिरत", "तत्पुरुष",
                 "तपसि स्वाध्याये च निरतः", "heuristic: locative-governing participle, treated as तत्पुरुष"),
    ]
    return Reading(
        words=words, junctions=junctions, compounds=compounds,
        scores={"splits": 0.9, "grammar": 0.8, "metre": 1.0, "total": 0.87 - 0.1 * rank},
        sandhi_ok=True, rejoined=[LINE1, LINE2], status=VERIFIED if rank == 0 else UNVERIFIED,
        notes=["तपस्वी is labelled आर्ष: the accusative तपस्वी is not derivable"] if rank == 0 else [],
        anvaya=[8, 6, 9, 5, 4, 3, 0, 1, 2, 7],
        translation=TRANSLATION if rank == 0 else "Valmiki asked sage Narada, an ascetic.",
        alignment=[Alignment(8, 0, 7), Alignment(7, 8, 13), Alignment(6, 14, 20), Alignment(9, 22, 37)]
        if rank == 0 else [],
    )


def make_analysis(verse_id: str = "1.1") -> VerseAnalysis:
    r0 = make_reading(0)
    r1 = make_reading(1)
    r1.words = r1.words[:8] + r1.words[8:]
    return VerseAnalysis(
        id=verse_id, input=TEXT, lines=[LINE1, LINE2],
        metre={"name": "अनुष्टुप्", "english": "epic eight-syllable metre", "pattern": "ग्-ग्-ल्-ग्"},
        split_counts=[2, 3], readings=[r0, r1], status=VERIFIED,
        notes=["Reading 2 splits वाग्विदाम् differently."],
    )
