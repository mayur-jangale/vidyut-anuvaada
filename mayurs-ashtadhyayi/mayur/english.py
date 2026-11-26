"""Small English morphology helpers (verbs and nouns), written for this package."""

from __future__ import annotations

_IRREGULAR: dict[str, tuple[str, str]] = {
    "go": ("went", "gone"), "say": ("said", "said"), "be": ("was", "been"), "see": ("saw", "seen"),
    "know": ("knew", "known"), "do": ("did", "done"), "give": ("gave", "given"),
    "come": ("came", "come"), "speak": ("spoke", "spoken"), "tell": ("told", "told"),
    "hear": ("heard", "heard"), "become": ("became", "become"), "run": ("ran", "run"),
    "stand": ("stood", "stood"), "think": ("thought", "thought"), "take": ("took", "taken"),
    "make": ("made", "made"), "win": ("won", "won"), "hold": ("held", "held"),
    "bear": ("bore", "borne"), "sit": ("sat", "sat"), "eat": ("ate", "eaten"),
    "drink": ("drank", "drunk"), "bring": ("brought", "brought"), "fight": ("fought", "fought"),
    "leave": ("left", "left"), "fall": ("fell", "fallen"), "rise": ("rose", "risen"),
    "kill": ("killed", "killed"), "wish": ("wished", "wished"), "find": ("found", "found"),
    "get": ("got", "got"), "send": ("sent", "sent"), "write": ("wrote", "written"),
    "lie": ("lay", "lain"), "sleep": ("slept", "slept"), "lead": ("led", "led"),
    "grow": ("grew", "grown"), "throw": ("threw", "thrown"), "cut": ("cut", "cut"),
    "put": ("put", "put"), "set": ("set", "set"), "burn": ("burned", "burned"),
    "ask": ("asked", "asked"), "choose": ("chose", "chosen"), "break": ("broke", "broken"),
    "wear": ("wore", "worn"), "keep": ("kept", "kept"), "meet": ("met", "met"),
    "swim": ("swam", "swum"), "fly": ("flew", "flown"), "beat": ("beat", "beaten"),
    "bind": ("bound", "bound"), "buy": ("bought", "bought"), "pay": ("paid", "paid"),
    "stay": ("stayed", "stayed"), "weep": ("wept", "wept"), "hide": ("hid", "hidden"), "beg": ("begged", "begged"), "extol": ("extolled", "extolled"),
    "control": ("controlled", "controlled"), "compel": ("compelled", "compelled"),
}
_PLURALS = {"man": "men", "woman": "women", "child": "children", "foot": "feet", "tooth": "teeth",
            "mouse": "mice", "person": "people", "ox": "oxen", "wife": "wives", "life": "lives",
            "knife": "knives", "leaf": "leaves", "wolf": "wolves", "deer": "deer", "sheep": "sheep", "people": "people",
            "folk": "folk", "cattle": "cattle", "police": "police"}
_VOWELS = "aeiou"


def _head(phrase: str) -> tuple[str, str]:
    """(everything before the last word, last word) of a multi-word phrase."""
    head, _, last = phrase.rpartition(" ")
    return (head + " " if head else ""), last


def _doubles(v: str) -> bool:
    return (len(v) >= 3 and v[-1] not in _VOWELS + "wxyh" and v[-2] in _VOWELS
            and v[-3] not in _VOWELS and len(v) <= 4 and v not in ("visit", "enter"))


def _ed(v: str) -> str:
    if v.endswith("e"):
        return v + "d"
    if v.endswith("y") and len(v) > 1 and v[-2] not in _VOWELS:
        return v[:-1] + "ied"
    if _doubles(v):
        return v + v[-1] + "ed"
    return v + "ed"


_ING_KEEP = {"bring", "sing", "ring", "swing", "cling", "fling", "string", "spring", "hang", "king"}


def base(verb: str) -> str:
    """Bare verb from a gloss that is already an -ing form ("seeing" -> "see")."""
    pre, v = _head(verb)
    if not v.endswith("ing") or len(v) < 5 or v in _ING_KEEP or v in _IRREGULAR:
        return verb
    stem = v[:-3]
    if len(stem) > 2 and stem[-1] == stem[-2] and stem[-1] not in "lsfz" + _VOWELS:
        stem = stem[:-1]
    elif stem[-1] in "vcz" or (stem[-1] == "s" and not stem.endswith("ss")) or \
            (stem.endswith("ng") and stem not in _IRREGULAR):
        stem += "e"
    return pre + stem


def past(verb: str) -> str:
    verb = base(verb)
    pre, v = _head(verb)
    return pre + (_IRREGULAR[v][0] if v in _IRREGULAR else _ed(v))


def participle(verb: str) -> str:
    verb = base(verb)
    pre, v = _head(verb)
    return pre + (_IRREGULAR[v][1] if v in _IRREGULAR else _ed(v))


def third_singular(verb: str) -> str:
    verb = base(verb)
    pre, v = _head(verb)
    irregular = {"be": "is", "have": "has", "do": "does", "go": "goes"}
    if v in irregular:
        return pre + irregular[v]
    if v.endswith(("s", "x", "z", "ch", "sh", "o")):
        return pre + v + "es"
    if v.endswith("y") and len(v) > 1 and v[-2] not in _VOWELS:
        return pre + v[:-1] + "ies"
    return pre + v + "s"


def plural(noun: str) -> str:
    pre, n = _head(noun)
    if n in _PLURALS:
        return pre + _PLURALS[n]
    if n.endswith(("s", "x", "z", "ch", "sh")):
        return pre + n + "es"
    if n.endswith("y") and len(n) > 1 and n[-2] not in _VOWELS:
        return pre + n[:-1] + "ies"
    return pre + n + "s"


def present_participle(verb: str) -> str:
    verb = base(verb)
    pre, v = _head(verb)
    if v.endswith("ie"):
        return pre + v[:-2] + "ying"
    if v.endswith("e") and not v.endswith(("ee", "ye")):
        return pre + v[:-1] + "ing"
    return pre + (v + v[-1] if _doubles(v) else v) + "ing"


# pronouns: lemma -> (singular forms, plural forms), each (nominative, accusative, genitive)
_PRON = {
    "अस्मद्": (("I", "me", "my"), ("we", "us", "our")),
    "युष्मद्": (("you", "you", "your"), ("you", "you", "your")),
    "किम्": (("who", "whom", "whose"), ("who", "whom", "whose")),
    "क": (("who", "whom", "whose"), ("who", "whom", "whose")),
    "यद्": (("who", "whom", "whose"), ("who", "whom", "whose")),
}
_THIRD = {
    "पुंलिङ्ग": ("he", "him", "his"), "स्त्रीलिङ्ग": ("she", "her", "her"),
    "नपुंसकलिङ्ग": ("it", "it", "its"),
}
_DEMONSTRATIVE = {"तद्": ("that", "those"), "एतद्": ("this", "these"), "इदम्": ("this", "these"),
                  "अदस्": ("that", "those"), "किम्": ("which", "which"), "क": ("which", "which"),
                  "यद्": ("which", "which")}
_CASES = {"प्रथमा": 0, "सम्बोधन": 0, "षष्ठी": 2}


_ALIAS = {"अहम्": "अस्मद्", "मद्": "अस्मद्", "मा": "अस्मद्", "अस्मत्": "अस्मद्", "वयम्": "अस्मद्",
          "त्वम्": "युष्मद्", "त्वद्": "युष्मद्", "त्वा": "युष्मद्", "यूयम्": "युष्मद्", "भवत्": "युष्मद्",
          "सः": "तद्", "तत्": "तद्", "एषः": "एतद्", "कः": "किम्", "यः": "यद्", "अयम्": "इदम्"}


def is_pronoun(lemma: str) -> bool:
    lemma = _ALIAS.get(lemma, lemma)
    return lemma in _PRON or lemma in _THIRD_LEMMAS or lemma in _DEMONSTRATIVE


_THIRD_LEMMAS = {"तद्", "एतद्", "इदम्", "अदस्"}


def pronoun(lemma: str, linga: str | None, vacana: str | None, vibhakti: str | None,
            demonstrative: bool = False, force_acc: bool = False) -> str | None:
    """English pronoun for a Sanskrit pronoun form, or None when the lemma is not a pronoun."""
    lemma = _ALIAS.get(lemma, lemma)
    plural_ = vacana == "बहुवचन"
    dual = vacana == "द्विवचन"
    if demonstrative and lemma in _DEMONSTRATIVE:
        return _DEMONSTRATIVE[lemma][1 if plural_ else 0]
    idx = 1 if force_acc else _CASES.get(vibhakti or "", 1)
    if lemma in _PRON and not (lemma in ("किम्", "क", "यद्") and linga == "नपुंसकलिङ्ग" and idx == 0):
        forms = _PRON[lemma][1 if (plural_ or dual) else 0]
        text = forms[idx]
        return text + " two" if dual and idx != 2 else text
    if lemma in ("किम्", "क", "यद्"):
        return "what" if lemma != "यद्" else "which"
    if lemma in ("तद्",):
        if plural_ or dual:
            return ("they", "them", "their")[idx]
        return _THIRD.get(linga or "", _THIRD["पुंलिङ्ग"])[idx]
    if lemma in ("एतद्", "इदम्", "अदस्"):
        return _DEMONSTRATIVE[lemma][1 if plural_ else 0]
    return None


def supplied_subject(purusha: str | None, vacana: str | None, accusative: bool = False) -> str:
    """Bracketed subject pronoun for a verb with no expressed agent."""
    plural_ = vacana in ("बहुवचन", "द्विवचन")
    if purusha == "उत्तमपुरुष":
        w = ("us" if accusative else "we") if plural_ else ("me" if accusative else "I")
    elif purusha == "मध्यमपुरुष":
        w = "you"
    else:
        w = ("them" if accusative else "they") if plural_ else ("him" if accusative else "he")
    return f"[{w}]"


_AGENT = {"protect": "protector", "act": "actor", "create": "creator", "govern": "governor",
          "direct": "director", "instruct": "instructor", "conduct": "conductor", "rule": "ruler"}


def agent(verb: str) -> str:
    """Agent noun of a verb gloss ("protect" -> "protector", "teach" -> "teacher")."""
    pre, v = _head(base(verb))
    if v in _AGENT:
        return pre + _AGENT[v]
    if v.endswith("e"):
        return pre + v + "r"
    if v.endswith("y") and len(v) > 1 and v[-2] not in _VOWELS:
        return pre + v[:-1] + "ier"
    return pre + (v + v[-1] if _doubles(v) else v) + "er"


_PARTICIPLE_TABLE = {"listen": "heard", "hear": "heard", "see": "seen", "tell": "told", "know": "known",
                     "say": "said", "speak": "spoken", "tell of": "told"}


def krt_form(krt: str | None, g: str) -> str:
    """English for a krdanta suffix applied to a verb gloss."""
    if krt == "क्त":
        return _PARTICIPLE_TABLE.get(base(g), participle(g))
    if krt == "क्तवतु":
        return past(g)
    if krt in ("शतृ", "शानच्"):
        return present_participle(g)
    if krt in ("तृच्", "तृन्", "तृ"):
        return agent(g)
    if krt in ("तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्"):
        return "to be " + participle(g)
    if krt in ("क्वसु", "कानच्"):
        return "having " + participle(g)
    return g
