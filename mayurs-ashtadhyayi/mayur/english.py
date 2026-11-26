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
    "stay": ("stayed", "stayed"), "weep": ("wept", "wept"), "hide": ("hid", "hidden"),
}
_PLURALS = {"man": "men", "woman": "women", "child": "children", "foot": "feet", "tooth": "teeth",
            "mouse": "mice", "person": "people", "ox": "oxen", "wife": "wives", "life": "lives",
            "knife": "knives", "leaf": "leaves", "wolf": "wolves", "deer": "deer", "sheep": "sheep"}
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


def past(verb: str) -> str:
    pre, v = _head(verb)
    return pre + (_IRREGULAR[v][0] if v in _IRREGULAR else _ed(v))


def participle(verb: str) -> str:
    pre, v = _head(verb)
    return pre + (_IRREGULAR[v][1] if v in _IRREGULAR else _ed(v))


def third_singular(verb: str) -> str:
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
