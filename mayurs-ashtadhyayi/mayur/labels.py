"""English labels for Paninian categories and a mapping to DCS CoNLL-U conventions.

The lakara -> Tense/Mood table follows what the DCS Ramayana files actually use:
``uvāca`` (liṭ) and ``abhūt``/``agamat`` (luṅ) are ``Tense=Past|Mood=Ind``;
``abravīt``/``akarot`` (laṅ) ``Tense=Impf|Mood=Ind``; ``kariṣyati`` (lṛṭ) and
``gantā`` (luṭ) ``Tense=Fut|Mood=Ind``; ``bhajasva`` (loṭ) ``Tense=Pres|Mood=Imp``;
``syāt`` (vidhiliṅ) ``Tense=Pres|Mood=Opt``; ``bhūyāt`` (āśīrliṅ) ``Tense=Past|Mood=Prec``;
``gamiṣyāma`` (lṛṅ) ``Tense=Fut|Mood=Cond``. Active voice carries no ``Voice``
feature; passives carry ``Voice=Pass``. Participles (kta) are ``VerbForm=Part``
without Tense, present participles add ``Tense=Pres``, perfect ones ``Tense=Past``;
absolutives are ``VerbForm=Conv``, infinitives ``VerbForm=Inf``, gerundives
``VerbForm=Gdv``; compound members are ``Case=Cpd``.
"""

from __future__ import annotations

from mayur import lexicon_gen as gen
from mayur.model import Morph
from mayur.translit import to_iast

ENGLISH: dict[str, str] = {
    # vibhakti
    "praTamA": "nominative", "dvitIyA": "accusative", "tftIyA": "instrumental",
    "caturTI": "dative", "paYcamI": "ablative", "zazWI": "genitive", "saptamI": "locative",
    "samboDanam": "vocative",
    # linga
    "puM": "masculine", "strI": "feminine", "napuMsaka": "neuter",
    # vacana
    "eka": "singular", "dvi": "dual", "bahu": "plural",
    # purusha (Paninian prathama = 3rd person)
    "praTama": "3rd person", "maDyama": "2nd person", "uttama": "1st person",
    # lakara
    "la~w": "present (laṭ)", "li~w": "perfect (liṭ)", "lu~w": "periphrastic future (luṭ)",
    "lf~w": "future (lṛṭ)", "le~w": "subjunctive (leṭ)", "lo~w": "imperative (loṭ)",
    "la~N": "imperfect (laṅ)", "viDili~N": "optative (vidhiliṅ)",
    "ASIrli~N": "benedictive (āśīrliṅ)", "lu~N": "aorist (luṅ)", "lf~N": "conditional (lṛṅ)",
    # prayoga
    "kartari": "active", "karmaRi": "passive", "BAve": "impersonal",
    # kind
    "subanta": "nominal", "tinanta": "finite verb", "avyaya": "indeclinable",
    "stem": "compound member", "unknown": "unknown",
    # common krt
    "kta": "past passive participle (kta)", "ktavatu~": "past active participle (ktavatu)",
    "Satf~": "present active participle (śatṛ)", "SAnac": "present middle participle (śānac)",
    "kvasu~": "perfect active participle (kvasu)", "kAnac": "perfect middle participle (kānac)",
    "ktvA": "absolutive (ktvā)", "lyap": "absolutive (lyap)", "tumu~n": "infinitive (tumun)",
    "tavya": "gerundive (tavya)", "anIyar": "gerundive (anīyar)", "yat": "gerundive (yat)",
    "Ryat": "gerundive (ṇyat)", "kyap": "gerundive (kyap)",
}

_SHORT = {
    "praTamA": "nom.", "dvitIyA": "acc.", "tftIyA": "ins.", "caturTI": "dat.", "paYcamI": "abl.",
    "zazWI": "gen.", "saptamI": "loc.", "samboDanam": "voc.", "puM": "masc.", "strI": "fem.",
    "napuMsaka": "neut.", "eka": "sg.", "dvi": "du.", "bahu": "pl.",
    "praTama": "3rd", "maDyama": "2nd", "uttama": "1st",
}

UD_CASE = {"praTamA": "Nom", "dvitIyA": "Acc", "tftIyA": "Ins", "caturTI": "Dat", "paYcamI": "Abl",
           "zazWI": "Gen", "saptamI": "Loc", "samboDanam": "Voc"}
UD_GENDER = {"puM": "Masc", "strI": "Fem", "napuMsaka": "Neut"}
UD_NUMBER = {"eka": "Sing", "dvi": "Dual", "bahu": "Plur"}
UD_PERSON = {"praTama": "3", "maDyama": "2", "uttama": "1"}
UD_TENSE_MOOD: dict[str, tuple[str, str]] = {
    "la~w": ("Pres", "Ind"), "li~w": ("Past", "Ind"), "lu~N": ("Past", "Ind"),
    "la~N": ("Impf", "Ind"), "lf~w": ("Fut", "Ind"), "lu~w": ("Fut", "Ind"),
    "lo~w": ("Pres", "Imp"), "viDili~N": ("Pres", "Opt"), "ASIrli~N": ("Past", "Prec"),
    "lf~N": ("Fut", "Cond"), "le~w": ("Pres", "Sub"),
}
PART_TENSE = {"kta": None, "ktavatu~": None, "Satf~": "Pres", "SAnac": "Pres",
              "kvasu~": "Past", "kAnac": "Past"}
PERIPHRASTIC = ("AmAsa", "AmAsu", "AmAs", "AYcakAra", "AYcakre", "AYcakr", "AmbaBUv")
PRONOUN_LEMMAS = {"asmad": "mad", "yuzmad": "tvad"}  # DCS lemmatises personal pronouns so, without Gender
GERUNDIVE_KRTS = frozenset({"tavya", "anIyar", "yat", "Ryat", "kyap", "kelimar"})
CONV_KRTS = frozenset({"ktvA", "lyap", "Ramu~l"})


def english(value: str) -> str:
    """English name of a vidyut category value; the value itself if unknown."""
    return ENGLISH.get(value, value)


def _iast(slp1: str) -> str:
    try:
        return to_iast(slp1)
    except Exception:  # transliteration of odd strings must not break labelling
        return slp1


def _verb_lemma(m: Morph) -> str:
    prefixes = tuple(gen.upasarga_text(p) for p in m.prefixes)
    root = m.root or m.lemma
    return "-".join(prefixes + (root,)) if prefixes else root


def describe(m: Morph) -> str:
    """Short English description, e.g. ``masc. acc. sg. of nārada``."""
    if m.kind == "tinanta":
        voice = english(m.prayoga) if m.prayoga else ""
        parts = [_SHORT.get(m.purusha or "", ""), _SHORT.get(m.vacana or "", ""),
                 english(m.lakara or ""), voice]
        return f"{' '.join(p for p in parts if p)} of {_iast(_verb_lemma(m))}"
    if m.kind == "stem":
        what = f"{english(m.krt)} " if m.krt else ""
        return f"compound member: {what}stem {_iast(m.lemma)}"
    if m.kind == "avyaya":
        if m.krt:
            return f"{english(m.krt)} of {_iast(_verb_lemma(m))}"
        return f"indeclinable {_iast(m.lemma)}"
    if m.kind == "subanta":
        parts = [_SHORT.get(x or "", "") for x in (m.linga, m.vibhakti, m.vacana)]
        head = " ".join(p for p in parts if p)
        if m.krt in PART_TENSE or m.krt in GERUNDIVE_KRTS:
            return f"{head} {english(m.krt)} of {_iast(_verb_lemma(m))}"
        return f"{head} of {_iast(m.lemma)}"
    return f"unanalysed {_iast(m.form)}"


def _verbal_feats(m: Morph) -> dict[str, str]:
    if m.krt in CONV_KRTS:
        return {"VerbForm": "Conv"}
    if m.krt == "tumu~n":
        return {"VerbForm": "Inf"}
    if m.krt in GERUNDIVE_KRTS:
        return {"VerbForm": "Gdv"}
    if m.krt in PART_TENSE:
        tense = PART_TENSE[m.krt]
        return {"VerbForm": "Part", **({"Tense": tense} if tense else {})}
    return {}


def ud_feats(m: Morph) -> dict[str, str]:
    """UD/DCS morphological features of ``m`` (keys as in the DCS CoNLL-U FEATS column)."""
    if m.kind == "stem":
        return {"Case": "Cpd", **({"VerbForm": "Part"} if m.krt in PART_TENSE else {})}
    if m.kind == "tinanta":
        tense, mood = UD_TENSE_MOOD.get(m.lakara or "", ("", ""))
        out = {"Tense": tense, "Mood": mood, "Person": UD_PERSON.get(m.purusha or "", ""),
               "Number": UD_NUMBER.get(m.vacana or "", "")}
        if m.prayoga in ("karmaRi", "BAve"):
            out["Voice"] = "Pass"
        if m.lakara == "lu~w" or (m.lakara == "li~w" and any(x in m.form for x in PERIPHRASTIC)):
            out = {"Tense": out["Tense"], "Mood": out["Mood"], "Formation": "peri",
                   **{k: v for k, v in out.items() if k not in ("Tense", "Mood")}}
        return {k: v for k, v in out.items() if v}
    if m.kind == "avyaya":
        return _verbal_feats(m)
    if m.kind == "subanta":
        gender = "" if m.lemma in PRONOUN_LEMMAS else UD_GENDER.get(m.linga or "", "")
        out = {"Case": UD_CASE.get(m.vibhakti or "", ""), "Gender": gender,
               "Number": UD_NUMBER.get(m.vacana or "", ""), **_verbal_feats(m)}
        return {k: v for k, v in out.items() if v}
    return {}


def _is_verbal(m: Morph) -> bool:
    return m.kind == "tinanta" or m.krt in PART_TENSE or m.krt in GERUNDIVE_KRTS \
        or m.krt in CONV_KRTS or m.krt == "tumu~n"


def _causative(m: Morph) -> bool:
    handle = m.handle
    for attr in ("dhatu_entry", "pratipadika_entry"):
        obj = getattr(handle, attr, None)
        obj = getattr(obj, "dhatu_entry", obj)
        dhatu = getattr(obj, "dhatu", None)
        if dhatu is not None:
            return any(str(s) == "Ric" for s in (dhatu.sanadi or ()))
    return False


def _slp1_verb_lemma(m: Morph) -> str:
    """DCS lemmatises verbs and participles under the verb with its preverbs."""
    lemma = gen.fix_hiatus(m.root or m.lemma) if m.kind == "stem" else m.lemma
    if (m.gana == "curAdi" or _causative(m)) and lemma.endswith("i"):
        lemma = lemma[:-1] + "ay"  # DCS: cintay, AsAday
    return lemma


def ud_lemma(m: Morph) -> str:
    """Lemma in DCS conventions, IAST (``niratam`` -> ``niram``, ``paripapracCa`` -> ``paripracch``)."""
    if m.kind == "stem" and m.krt and m.krt in PART_TENSE:
        return _iast(_slp1_verb_lemma(m))
    if _is_verbal(m):
        return _iast(_slp1_verb_lemma(m))
    if m.krt and m.kind == "subanta" and m.handle is not None:
        stem = _krdanta_stem(m)
        if stem:
            return _iast(stem)
    return _iast(PRONOUN_LEMMAS.get(m.lemma, m.lemma))


def _krdanta_stem(m: Morph) -> str:
    prati = getattr(m.handle, "pratipadika_entry", None)
    if prati is None or not hasattr(prati, "krt"):
        return ""
    return gen.krdanta_stem_text(prati.dhatu_entry.dhatu, prati.krt)
