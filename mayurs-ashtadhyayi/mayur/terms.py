"""Grammatical terms used across the package, in Devanagari, with English names.

These exact strings are the values stored in ``model.Morph`` and ``model.Word.role``.
"""

from __future__ import annotations

LINGA = {"पुंलिङ्ग": "masculine", "स्त्रीलिङ्ग": "feminine", "नपुंसकलिङ्ग": "neuter"}
VIBHAKTI = {
    "प्रथमा": "nominative", "द्वितीया": "accusative", "तृतीया": "instrumental", "चतुर्थी": "dative",
    "पञ्चमी": "ablative", "षष्ठी": "genitive", "सप्तमी": "locative", "सम्बोधन": "vocative",
}
VACANA = {"एकवचन": "singular", "द्विवचन": "dual", "बहुवचन": "plural"}
PURUSHA = {"प्रथमपुरुष": "3rd person", "मध्यमपुरुष": "2nd person", "उत्तमपुरुष": "1st person"}
LAKARA = {
    "लट्": "present", "लिट्": "perfect", "लुट्": "periphrastic future", "लृट्": "future",
    "लेट्": "subjunctive", "लोट्": "imperative", "लङ्": "imperfect", "विधिलिङ्": "optative",
    "आशीर्लिङ्": "benedictive", "लुङ्": "aorist", "लृङ्": "conditional",
}
PRAYOGA = {"कर्तरि": "active", "कर्मणि": "passive", "भावे": "impersonal"}
KIND = {"subanta": "सुबन्त", "tinanta": "तिङन्त", "avyaya": "अव्यय", "stem": "प्रातिपदिक", "unknown": "अज्ञात"}

# krt suffixes are stored without their nasal marker: क्त, क्तवतु, शतृ, शानच्, क्त्वा, ल्यप्, तुमुन् ...
PARTICIPLE_KRT = {
    "क्त": "past passive participle", "क्तवतु": "past active participle", "शतृ": "present active participle",
    "शानच्": "present middle participle", "तव्य": "gerundive", "अनीयर्": "gerundive", "यत्": "gerundive",
    "ण्यत्": "gerundive", "क्यप्": "gerundive", "क्वसु": "perfect active participle", "कानच्": "perfect middle participle",
}
NONFINITE_KRT = {"क्त्वा": "absolutive", "ल्यप्": "absolutive", "तुमुन्": "infinitive"}

ROLES = {
    "कर्ता": "agent", "कर्म": "object", "करण": "instrument", "सम्प्रदान": "recipient", "अपादान": "source",
    "अधिकरण": "locus", "सम्बन्ध": "possessor", "क्रिया": "verb", "विशेषण": "qualifier", "विधेय": "predicate",
    "सम्बोधन": "address", "अव्यय": "particle", "पूर्वकालक्रिया": "prior action", "तुमर्थ": "purpose",
    "समासपूर्वपद": "compound member", "": "",
}

# Universal Dependencies values used by the Digital Corpus of Sanskrit, for evaluation.
UD_CASE = {"प्रथमा": "Nom", "द्वितीया": "Acc", "तृतीया": "Ins", "चतुर्थी": "Dat", "पञ्चमी": "Abl",
           "षष्ठी": "Gen", "सप्तमी": "Loc", "सम्बोधन": "Voc"}
UD_GENDER = {"पुंलिङ्ग": "Masc", "स्त्रीलिङ्ग": "Fem", "नपुंसकलिङ्ग": "Neut"}
UD_NUMBER = {"एकवचन": "Sing", "द्विवचन": "Dual", "बहुवचन": "Plur"}
UD_PERSON = {"प्रथमपुरुष": "3", "मध्यमपुरुष": "2", "उत्तमपुरुष": "1"}

ALL = {**LINGA, **VIBHAKTI, **VACANA, **PURUSHA, **LAKARA, **PRAYOGA, **PARTICIPLE_KRT, **NONFINITE_KRT, **ROLES}


def english(term: str | None) -> str:
    """English name of a Devanagari grammatical term ("" if none)."""
    return ALL.get(term or "", term or "")
