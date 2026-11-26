"""Hand-made VerseAnalysis fixture for UI tests (no pipeline needed)."""

from __future__ import annotations

from mayur.model import (
    Alignment, Compound, Morph, Reading, SutraStep, VerseAnalysis, Word, WordProof,
)

XSS = "<script>alert('x')</script>"

_TRACE = [
    SutraStep("dhatupatha", "01.0001", "BU"),
    SutraStep("ashtadhyayi", "3.2.123", "BU + la~w"),
    SutraStep("ashtadhyayi", "1.4.99", "BU + la~w"),
    SutraStep("ashtadhyayi", "3.4.78", "BU + tip"),
    SutraStep("ashtadhyayi", "3.1.68", "BU + Sap + tip"),
    SutraStep("ashtadhyayi", "1.1.3", "BU + Sap + tip"),
    SutraStep("ashtadhyayi", "7.3.84", "Bo + a + ti"),
    SutraStep("ashtadhyayi", "6.1.78", "Bav + a + ti"),
    SutraStep("ashtadhyayi", "8.2.66", "Bavati"),
    SutraStep("ashtadhyayi", "8.3.15", "Bavati"),
]


def _morph(form: str, lemma: str, **kw) -> Morph:
    return Morph(form=form, lemma=lemma, kind=kw.pop("kind", "subanta"), **kw)


def _noun(form: str, lemma: str, vib: str = "praTamA", ling: str = "puM") -> Morph:
    return _morph(form, lemma, linga=ling, vibhakti=vib, vacana="eka")


def _word(form, line, start, end, morph, *, proof=True, **kw) -> Word:
    wp = WordProof(True, "vidyut-prakriya", form, list(_TRACE)) if proof else WordProof(
        False, "", "", [], "stem not derivable")
    return Word(form=form, line=line, start=start, end=end, analyses=[morph, _noun(form, lemma="putra")],
                chosen=0, proof=wp, **kw)


def _reading(rank: int) -> Reading:
    words = [
        _word("mahA", 0, 0, 4, _morph("mahA", "mahat", kind="stem"), in_compound=True, compound=0,
              role="samasa-purvapada", head=2, gloss="great"),
        _word("rAja", 0, 4, 8, _morph("rAja", "rAjan", kind="stem"), in_compound=True, compound=0,
              role="samasa-purvapada", head=2, gloss="king"),
        _word("putras", 0, 8, 14, _noun("putras", "putra"), compound=0, role="karta", head=4,
              gloss="son " + XSS, gloss_source="lexicon"),
        _word("vanam", 0, 15, 20, _noun("vanam", "vana", "dvitIyA", "napuM"), role="karma", head=4,
              gloss="forest"),
        _word("gacCati", 0, 21, 28,
              _morph("gacCati", "gam", kind="tinanta", lakara="la~w", purusha="praTama", vacana="eka",
                     prayoga="kartari", root="gam", dhatu="ga\\mx~", gana="BvAdi"),
              role="kriya", gloss="goes"),
        _word("sItAm", 1, 0, 5, _noun("sItAm", "sItA", "dvitIyA", "strI"), proof=False, role="karma",
              head=6, gloss="Sita"),
        _word("paSyati", 1, 6, 13,
              _morph("paSyati", "dfS", kind="tinanta", lakara="la~w", purusha="praTama", vacana="eka",
                     prayoga="kartari", root="dfS"),
              role="kriya", gloss="sees", arsha=True),
    ]
    comp = Compound(0, [0, 1, 2], "mahArAjaputra", "tatpuruza", "mahAn rAjA tasya putraH",
                    "heuristic: first member a stem, last member nominal")
    r = Reading(words=words, compounds=[comp],
                scores={"frequency": 0.5, "akanksha": 0.25, "yogyata": 0.5, "sannidhi": 0.5,
                        "total": 1.75 - 0.1 * rank},
                sandhi_ok=True, rejoined=["mahArAjaputro vanaM gacCati", "sItAM paSyati"],
                status="verified" if rank == 0 else "unverified",
                notes=["paSyati: arsha usage"] if rank == 0 else [],
                anvaya=[0, 1, 2, 3, 4, 5, 6], translation="The son goes to the forest and sees Sita.",
                alignment=[Alignment(2, 4, 7), Alignment(3, 24, 30)])
    return r


def make_analysis(verse_id: str = "1.1") -> VerseAnalysis:
    r0, r1 = _reading(0), _reading(1)
    r1.words = r1.words[:5] + r1.words[5:]
    r1.compounds, r1.alignment, r1.translation = [], [], ""
    return VerseAnalysis(
        id=verse_id, input="महाराजपुत्रो वनं गच्छति । सीतां पश्यति ॥",
        lines=["mahArAjaputro vanaM gacCati", "sItAM paSyati"],
        metre={"name": "anuzwuB", "ok": True}, split_counts=[3, 1], readings=[r0, r1],
        status="unverified", notes=["fixture"],
    )
