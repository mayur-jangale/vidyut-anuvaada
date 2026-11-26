"""How the corpus cites verbal lemmas: upasargas joined to the root by sandhi, causatives as -अय्.

All strings Devanagari. Used by ``mayur.ud.lemma`` through ``mayur.lexicon.verbal_lemma``.
"""

from __future__ import annotations

from functools import lru_cache

from mayur import lipi
from mayur.model import Morph

_R_PREFIX = ("प्र", "परा", "परि", "निर्", "निस्", "दुर्")


def _join(left: str, right: str) -> str:
    from mayur import sandhi

    if left in ("पुरस्", "नमस्"):  # 8.3.40 नमस्पुरसोर्गत्योः
        return left + right
    if left[-1:] in ("ि", "ु") and right.startswith(_SHATVA_ROOTS):  # 8.3.65-8.3.70, 8.4.41
        right = "ष" + right[1:]
        right = right.replace("ष्था", "ष्ठा", 1).replace("ष्तु", "ष्टु", 1).replace("ष्तम्भ्", "ष्टम्भ्", 1)
        return left + right
    if left == "उद्" and right.startswith(("स्था", "स्तम्भ्")):  # 8.4.61 उदः स्थास्तम्भोः पूर्वस्य
        return "उत्" + right[2:]
    if left == "उद्" and right.startswith("श"):  # 8.4.40 + 8.4.63 शश्छोऽटि: उद् + श्रि -> उच्छ्रि
        return "उच्छ" + right[1:]
    if left == "उद्" and right[:1] in ("न", "म"):  # 8.4.45 यरोऽनुनासिकेऽनुनासिको वा (the usual spelling)
        return "उन्" + right
    if left in ("परा", "परि") and right.startswith("अय्"):  # 8.2.19 उपसर्गस्यायतौ
        left = left.replace("र", "ल", 1)
    if left.endswith("्") and left not in ("निस्", "दुस्", "निर्", "दुर्") and right[:1] in _VOWEL_INITIAL:
        return lipi.from_varnas(lipi.varnas(left) + lipi.varnas(right))  # सम् + आसद् -> समासद्
    if left in ("निर्", "दुर्"):  # the upasarga is निस् / दुस् (र् is its sandhi form)
        left = left[:-2] + "स्"
    if left in ("निस्", "दुस्") and right[:1] in _VOWEL_INITIAL:
        return lipi.from_varnas(lipi.varnas(left[:-2] + "र्") + lipi.varnas(right))
    outs = sandhi.outcomes(left, right)
    # within a word the samhita rules are obligatory (1.4.109 with 6.1.72): prefer an outcome that applied one
    applied = [o for o in outs if o.sutras and "पादान्त-विराम" not in o.sutras]
    text = (applied or list(outs))[0].text if outs else left + right
    if "ः" in text and right[:1] not in _VOWEL_INITIAL:  # निस्/दुस् before a voiced sound: निर्, दुर्
        if right[:1] in _VOICED:
            sub = "र्"
        elif right[:1] in "कखपफ" and left[-3:-2] in ("ि", "ु"):  # 8.3.41 इदुदुपधस्य चाप्रत्ययस्य
            sub = "ष्"
        elif right[:1] in "तथ":
            sub = "स्"
        elif right[:1] in "चछ":
            sub = "श्"
        else:
            sub = "ः"
        text = text.replace("ः", sub, 1)
    if left in _R_PREFIX and text[len(left):].startswith("न"):  # 8.4.14 उपसर्गादसमासेऽपि णोपदेशस्य
        text = text[: len(left)] + "ण" + text[len(left) + 1:]
    return text


_VOWEL_INITIAL = frozenset("अआइईउऊऋॠऌएऐओऔ")
_VOICED = frozenset("गघङजझञडढणदधनबभमयरलवह")
_SHATVA_ROOTS = ("स्था", "सद्", "सिच्", "सिध्", "सञ्ज्", "स्तु", "स्तम्भ्", "सेव्", "सो", "स्वप्", "सह्",
                 "सिव्", "सु", "सू", "स्यन्द्", "स्वञ्ज्", "स्वज्")


def _dcs_root(m: Morph) -> str:
    """A ṇic / curādi stem as the corpus cites it: कथि -> कथय्, कारि -> कारय् (vidyut ends it in इ)."""
    root = m.root or m.lemma
    taught = "".join(ch for ch in (m.dhatu or "") if ch not in "॒॑ँ")
    if taught[:1] in ("ष", "ण"):  # 6.1.64 धात्वादेः षः सः, 6.1.65 णो नः
        taught = {"ष": "स", "ण": "न"}[taught[0]] + taught[1:]
    if root.endswith("ि") and not taught.startswith(root):
        short = root.replace("ा", "", 1)
        if short != root and short[:-1] in m.form and root[:-1] not in m.form:  # 6.4.92 मितां ह्रस्वः
            root = short
        return root[:-1] + "य्"
    if root and "क" <= root[-1] <= "ह":  # a sanādi stem in -अ (जिगीष, विधित्स): cited with virāma
        return root + "्"
    return _CITED_ROOT.get(root, root.replace("ॄ", "ृ"))  # the corpus cites कॄ, स्तॄ as कृ, स्तृ


# How the corpus cites roots that vidyut names by their Dhatupatha form (ध्यै -> ध्या, 6.1.45)
_CITED_ROOT = {"स्वञ्ज्": "स्वज्", "ऋच्छ्": "ऋछ्", "तॄ": "तृ", "ध्यै": "ध्या", "गै": "गा", "ह्वे": "ह्वा", "म्लै": "म्ला", "ग्लै": "ग्ला", "त्रै": "त्रा",
               "दै": "दा", "वे": "वा", "व्ये": "व्या", "शो": "शा", "सो": "सा", "छो": "छा", "दो": "दा"}
# 3.1.31 आयादय आर्धधातुके वा: without आय the corpus cites the bare root (गुप्त -> गुप्)
_AYA_ROOT = {"गोपाय": "गुप्", "धूपाय": "धूप्", "पणाय": "पण्", "पनाय": "पन्", "विच्छाय": "विच्छ्"}
# Present-system suppletion (7.3.78 पाघ्राध्मास्थाम्नादाण्दृश्यर्तिसर्तिशदसदां पिबजिघ्र...): दृश् -> पश्य
_PRESENT = frozenset({"लट्", "लोट्", "लङ्", "विधिलिङ्"})


def _suppletive_root(m: Morph, root: str) -> str:
    if root == "दृश्" and "पश्य" in m.form and (m.lakara in _PRESENT or m.krt in ("शतृ", "शानच्")):
        return "पश्"
    if root == "ध्मा" and "धम" in m.form:  # 7.3.78 ... ध्मा -> धम in the present system: व्यधमत् -> विधम्
        return "धम्"
    if root == "हन्" and "वध" in m.form:  # 2.4.42 हनो वध लिङि, 2.4.43 लुङि च; the corpus cites वध्
        return "वध्"
    if root.endswith(("ाय", "ीय")):  # a sanādi stem in -आय/-ईय (3.1.28 आय, 3.1.27 यक्): गोपाय्, महीय्
        return root + "्" if root in m.form else _AYA_ROOT.get(root, root + "्")
    if root == "इ" and m.lakara == "लुङ्" and "गा" in m.form:  # 2.4.45 इणो गा लुङि
        return "गा"
    if root == "ब्रू" and any(x in m.form for x in ("आह", "ाह", "आत्थ", "ात्थ")):  # 3.4.84 ब्रुवः पञ्चानाम् ... आहः
        return "अह्"
    return root


@lru_cache(maxsize=100_000)
def _verbal_lemma(prefixes: tuple[str, ...], root: str) -> str:
    out = root
    for p in reversed(prefixes):
        out = _join(p, out)
    return out


def _labial_m(text: str) -> str:
    """The corpus writes म् before a labial (सम्पद्, सम्भू) and ं elsewhere (संगम्, संयम्)."""
    for lab in "पफबभम":
        text = text.replace("ं" + lab, "म्" + lab)
    return text


def verbal_lemma(m: Morph) -> str:
    """The upasargas joined to the root by sandhi, in the corpus' citation form: प्र+आप् -> प्राप्,
    प्र+नम् -> प्रणम्, आ+इ -> ए, आ+सादि -> आसादय्. For ``mayur.ud.lemma``."""
    return _labial_m(_verbal_lemma(tuple(m.prefixes), _suppletive_root(m, _dcs_root(m))))
