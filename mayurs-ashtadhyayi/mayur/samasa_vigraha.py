"""Laukika-vigraha of a compound, following its type, from forms generated FORWARD by vidyut.

Every inflected word is produced by ``bridge.subanta_paradigm`` + ``bridge.derive`` (or, for an
indeclinable, taken from the lexicon's own analysis of that form); nothing is glued from endings.
If a needed form cannot be generated the vigraha is "" and the caller falls back to the
hyphenated members. Words are shown in pausa (final स्/र् as visarga, 8.3.15).

    बहुव्रीहि      दृढं व्रतं यस्य सः · महान्तौ बाहू यस्य सः · गन्धर्वैः सह वर्तमानाः
    कर्मधारय      दृढः च असौ कपिः च · हेम इव पिङ्गलः
    तत्पुरुष       मुनिषु पुङ्गवः · तपसि स्वाध्याये च निरतः · न दीनः
    द्वन्द्व        रामः च लक्ष्मणः च
"""

from __future__ import annotations

from functools import lru_cache
from typing import Optional, Sequence

from mayur import lipi
from mayur import samasa_type as st
from mayur.model import Reading, Word

NOM, GEN, INS = "प्रथमा", "षष्ठी", "तृतीया"


@lru_cache(maxsize=50_000)
def form(stem: str, linga: Optional[str], vibhakti: str, vacana: str) -> str:
    """The pada of ``stem`` derived by vidyut ("" if none; a bare stem counts as none)."""
    from mayur import bridge
    if not linga:
        return ""
    try:
        paradigm = bridge.subanta_paradigm(stem, linga)
    except Exception:  # noqa: BLE001 - vidyut rejected the stem
        return ""
    for h, m in paradigm:
        if (m.vibhakti, m.vacana) == (vibhakti, vacana):
            texts = [d.text for d in bridge.derive(h) if d.text != stem]
            return lipi.pausa(texts[0]) if texts else ""
    return ""


def _own_gender(word: Word, fallback: Optional[str]) -> Optional[str]:
    """The stem's own gender: the lexicon's single one, else the compound's (``fallback``)."""
    lingas = st.lexical_lingas(st.stem_of(word))
    if fallback in lingas or not lingas:
        return fallback if fallback else (sorted(lingas)[0] if lingas else None)
    if len(lingas) == 3:
        return fallback
    if st.F in lingas and st.stem_of(word).endswith(("ा", "ी")):
        return st.F
    return sorted(lingas)[0]


def _all(parts: Sequence[str]) -> str:
    return " ".join(parts) if all(parts) else ""


def _chain(words: Sequence[Word], last_case: str, last_number: str = st.SG) -> list[str]:
    """Non-final members: earlier ones in the genitive (left bracketing), the last one in ``last_case``."""
    out = [form(st.stem_of(w), _own_gender(w, None), GEN, st.SG) for w in words[:-1]]
    w = words[-1]
    return out + [form(st.stem_of(w), _own_gender(w, None), last_case, last_number)]


def _bahuvrihi(d: st.Decision, words: Sequence[Word]) -> str:
    final, fm = words[-1], words[-1].morph
    g, n, case = fm.linga, fm.vacana or st.SG, fm.vibhakti or NOM
    if case == "सम्बोधन":
        case = NOM
    if d.rule == "सह":
        own = _own_gender(final, g)
        return _all([form(st.stem_of(final), own, INS, n), "सह", form("वर्तमान", g, case, n)])
    rel = _all([form("यद्", g, GEN, n), form("तद्", g, case, n)])
    body = [w for w in words if w.form not in st.NAN] if d.samasa == st.NAN_BAHUVRIHI else list(words)
    if not body or not rel:
        return ""
    fstem = st.stem_of(final)
    own = _own_gender(final, g)
    num = st.DU if fstem in st.PAIRED else st.SG
    if d.rule == "तुं-काम":
        inf = _infinitive(body[0].form)
        return _all([inf, form(fstem, own, NOM, st.SG), rel])
    if d.rule == "उपमान-बहुव्रीहि":
        prev = body[-2]
        head = form(fstem, own, NOM, num)
        return _all([form(st.stem_of(prev), _own_gender(prev, None), GEN, st.SG), head, "इव", head, rel])
    head_gender = own
    if fstem in st.BV_HEADS_ALWAYS | st.BV_HEADS and len(st.lexical_lingas(fstem)) != 1:
        head_gender = _own_gender(body[-2], own)  # पूर्व/प्रमुख agree with the noun before them
    parts = [form(st.stem_of(w), head_gender if w is not final else head_gender, NOM, num) for w in body]
    neg = ["न"] if d.samasa == st.NAN_BAHUVRIHI else []
    return _all(neg + parts + [rel])


def _infinitive(member_form: str) -> str:
    """The तुमुन् form (the member drops its म्, 6.1.144 वार्त्तिक), as the lexicon analyses it."""
    from mayur import lexicon
    cand = member_form + "म्"
    return cand if any(m.krt == "तुमुन्" for m in lexicon.padas(cand)) else ""


def _karmadharaya(d: st.Decision, words: Sequence[Word]) -> str:
    final, fm = words[-1], words[-1].morph
    g = _own_gender(final, fm.linga)
    n = fm.vacana or st.SG
    prev = words[-2]
    b = form(st.stem_of(final), g, NOM, n)
    if d.rule == "उपमान":
        return _all([form(st.stem_of(prev), _own_gender(prev, None), NOM, st.SG), "इव", b])
    if d.samasa == st.DVIGU and fm.linga == st.N and n == st.SG:
        return _all([form(st.stem_of(prev), g, GEN, st.PL), form(st.stem_of(final), g, GEN, st.PL), "समाहारः"])
    a = form(st.stem_of(prev), g, NOM, n)
    pron = form("अदस्", g, NOM, n)
    return _all([a, "च", pron, b, "च"])


def _tatpurusha(d: st.Decision, words: Sequence[Word]) -> str:
    final, fm = words[-1], words[-1].morph
    g = fm.linga if st.word_class(final)[0] != "noun" else _own_gender(final, fm.linga)
    n = fm.vacana or st.SG
    head = form(st.stem_of(final), g, NOM, n)
    if d.rule == "नञ्":
        return _all(["न", head])
    if d.rule == "प्रादि":
        return _pradi(words[0].form, head)
    case = d.relation or GEN
    number = st.PL if "निर्धारण" in d.note else st.SG
    if d.inner == st.DVANDVA:
        inner = [form(st.stem_of(w), _own_gender(w, None), case, number) for w in words[:-1]]
        return _all(inner + ["च", head])
    return _all(_chain(words[:-1], case, number) + [head])


def _pradi(prefix: str, head: str) -> str:
    from mayur import lexicon
    if prefix == "अति":
        return _all([form("अतिशय", st.M, INS, st.SG), head])
    if prefix == "सु" and any(m.kind == "avyaya" for m in lexicon.padas("सुष्ठु")):
        return _all(["सुष्ठु", head])
    return ""


def _dvandva(words: Sequence[Word]) -> str:
    fm = words[-1].morph
    n = st.PL if fm.vacana == st.PL else st.SG
    parts = []
    for w in words:
        parts += [form(st.stem_of(w), _own_gender(w, fm.linga if w is words[-1] else None), NOM, n), "च"]
    return _all(parts)


def vigraha(reading: Reading, members: Sequence[int], d: st.Decision) -> str:
    """Type-specific vigraha with generated forms; "" when a form is missing."""
    words = [reading.words[i] for i in members]
    if len(words) < 2 or words[-1].morph is None or not words[-1].morph.vibhakti:
        return ""
    try:
        if d.samasa in (st.BAHUVRIHI, st.NAN_BAHUVRIHI):
            return _bahuvrihi(d, words)
        if d.samasa in (st.KARMADHARAYA, st.DVIGU):
            return _karmadharaya(d, words)
        if d.samasa in (st.TATPURUSHA, st.NAN_TATPURUSHA, st.UPAPADA):
            return _tatpurusha(d, words)
        if d.samasa == st.DVANDVA:
            return _dvandva(words)
    except Exception:  # noqa: BLE001 - vidyut failure on an odd stem: no vigraha
        return ""
    return ""
