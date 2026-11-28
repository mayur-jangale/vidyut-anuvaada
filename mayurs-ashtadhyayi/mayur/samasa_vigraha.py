"""Laukika-vigraha of a compound, following its type, from forms generated FORWARD by vidyut.

Every inflected word is produced by ``bridge.subanta_paradigm`` + ``bridge.derive`` (an
indeclinable is taken from the lexicon's own analysis of that form; the final member may be
the text's own pada when the compound stands in the nominative); nothing is glued from endings.
If a needed form cannot be generated the vigraha is "" and the caller falls back to the
hyphenated members. Words are shown in pausa (final स्/र् as visarga, 8.3.15).

    बहुव्रीहि      दृढं व्रतं यस्य सः · महान्तौ बाहू यस्य सः · गन्धर्वैः सह वर्तमानाः
    कर्मधारय      नीलं च तत् उत्पलं च · हेम इव पिङ्गलः · परमं प्रीतः
    तत्पुरुष       मुनिषु पुङ्गवः · तपसि स्वाध्याये च निरतः · न दीनः
    द्वन्द्व        रामः च लक्ष्मणः च
"""

from __future__ import annotations

from functools import lru_cache
from typing import Optional, Sequence

from mayur import lipi
from mayur import samasa_type as st
from mayur.model import Reading, Word
from mayur.samasa_tables import SAMASANTA, TADDHITA_FINALS

NOM, ACC, GEN, INS = "प्रथमा", "द्वितीया", "षष्ठी", "तृतीया"


@lru_cache(maxsize=50_000)
def form(stem: str, linga: Optional[str], vibhakti: str, vacana: str) -> str:
    """The pada of ``stem`` derived by vidyut ("" if none; a bare stem counts as none)."""
    from mayur import bridge
    if not linga or not stem:
        return ""
    bare = {stem, stem[:-2] + "द्" if stem.endswith("त्") else stem}
    try:
        paradigm = bridge.subanta_paradigm(stem, linga)
    except Exception:  # noqa: BLE001 - vidyut rejected the stem
        return ""
    for h, m in paradigm:
        if (m.vibhakti, m.vacana) == (vibhakti, vacana):
            texts = [d.text for d in bridge.derive(h) if d.text not in bare]
            return lipi.pausa(texts[0]) if texts else ""
    return ""


def gender(word: Word, fallback: Optional[str] = None) -> Optional[str]:
    """The stem's own gender (kosha and DCS dictionary), else ``fallback``, else by its ending."""
    stem = st.stem_of(word)
    own = st.own_genders(stem)
    if fallback and (not own or fallback in own or st._adjectival(stem)):
        return fallback
    if stem.endswith(("ा", "ी")) and (st.F in own or not own):
        return st.F
    for g in (st.M, st.N, st.F):
        if g in own:
            return g
    return fallback or st.M


def _all(parts: Sequence[str]) -> str:
    return " ".join(parts) if parts and all(parts) else ""


def _head(final: Word, g: Optional[str], n: str) -> str:
    """The final member in the nominative: generated; else the text's own pada if it is one."""
    stem = st.stem_of(final)
    stem = SAMASANTA.get(stem, (stem, ""))[0]
    out = form(stem, g, NOM, n)
    fm = final.morph
    if not out and fm is not None and (fm.vibhakti, fm.vacana, fm.linga) == (NOM, n, g):
        out = lipi.pausa(final.form)
    return out


def _bahuvrihi(d: st.Decision, words: Sequence[Word]) -> str:
    final, fm = words[-1], words[-1].morph
    g, n = fm.linga, fm.vacana or st.SG
    case = NOM if fm.vibhakti in (None, "सम्बोधन") else fm.vibhakti
    if d.rule == "सह":
        return _all([form(st.stem_of(final), gender(final), INS, n), "सह", form("वर्तमान", g, case, n)])
    rel = [form("यद्", g, GEN, n), form("तद्", g, case, n)]
    body = [w for w in words if w.form not in st.NAN] if d.samasa == st.NAN_BAHUVRIHI else list(words)
    noun = st.base_stem(st.stem_of(final))
    own = gender(final) if noun == st.stem_of(final) else st.M if st.M in st.own_genders(noun) else st.N
    num = st.DU if noun in st.PAIRED else st.SG
    head = form(noun, own, NOM, num)
    if d.rule == "तुं-काम":
        return _all([_infinitive(body[0].form), head] + rel)
    prev = body[-2] if len(body) > 1 else None
    if prev is None:
        return ""
    if d.rule == "उपमान-बहुव्रीहि":
        return _all([form(st.stem_of(prev), gender(prev), GEN, st.SG), head, "इव", head] + rel)
    if noun in st.BV_HEADS_ALWAYS | st.BV_HEADS and len(st.own_genders(noun)) != 1:
        own = gender(prev)  # पूर्व/प्रमुख agree with the noun before them
        head = form(noun, own, NOM, st.SG)
    first = form(st.stem_of(prev), own if st.word_class(prev)[0] != "noun" else gender(prev), NOM, num)
    earlier = [form(st.stem_of(w), gender(w), GEN, st.SG) for w in body[:-2]]
    neg = ["न"] if d.samasa == st.NAN_BAHUVRIHI else []
    return _all(neg + earlier + [first, head] + rel)


def _infinitive(member_form: str) -> str:
    """The तुमुन् form (the member drops its म्, 6.1.144 वार्त्तिक), as the lexicon analyses it."""
    from mayur import lexicon
    cand = member_form + "म्"
    return lipi.pausa(cand) if any(m.krt == "तुमुन्" for m in lexicon.padas(cand)) else ""


def _karmadharaya(d: st.Decision, words: Sequence[Word]) -> str:
    final, fm = words[-1], words[-1].morph
    n = fm.vacana or st.SG
    fcls = st.word_class(final)[0]
    g = gender(final, fm.linga) if fcls == "noun" else fm.linga
    prev = words[-2]
    b = _head(final, g, n)
    if d.rule == "उपमान":
        return _all([form(st.stem_of(prev), gender(prev), NOM, st.SG), "इव", b])
    if d.rule == "संख्या":
        return _all([form(st.stem_of(words[0]), g, NOM, n), form(st.stem_of(prev), gender(prev), GEN, st.PL), b])
    if d.samasa == st.DVIGU and fm.linga == st.N and n == st.SG:
        return _all([form(st.stem_of(prev), g, GEN, st.PL), form(st.stem_of(final), g, GEN, st.PL), "समाहारः"])
    pcls = st.word_class(prev)[0]
    if fcls in ("adjective", "participle") and pcls == "adjective":  # परमं प्रीतः: the first qualifies the quality
        return _all([form(st.stem_of(prev), st.N, ACC, st.SG), b])
    pron = form("तद्" if g == st.N else "अदस्", g, NOM, n)  # नीलं च तत् उत्पलं च, महान् च असौ मुनिः च
    return _all([form(st.stem_of(prev), g, NOM, n), "च", pron, b, "च"])


def _tatpurusha(d: st.Decision, words: Sequence[Word]) -> str:
    final, fm = words[-1], words[-1].morph
    n = fm.vacana or st.SG
    g = gender(final, fm.linga) if st.word_class(final)[0] == "noun" else fm.linga
    head = _head(final, g, n)
    if d.rule == "नञ्":
        return _all(["न", head])
    if d.rule == "प्रादि":
        return _pradi(words[0].form, head)
    case = d.relation or GEN
    number = st.PL if "निर्धारण" in d.note else st.SG
    if d.inner == st.DVANDVA:
        inner = [form(st.stem_of(w), gender(w), case, st.PL if len(words) > 2 else number) for w in words[:-1]]
        return _all(inner + ["च", head])
    earlier = [form(st.stem_of(w), gender(w), GEN, st.SG) for w in words[:-2]]
    prev = words[-2]
    return _all(earlier + [form(st.stem_of(prev), gender(prev), case, number), head])


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
    parts: list[str] = []
    for w in words:
        parts += [form(st.stem_of(w), gender(w, fm.linga if w is words[-1] else None), NOM, n), "च"]
    return _all(parts)


def vigraha(reading: Reading, members: Sequence[int], d: st.Decision) -> str:
    """Type-specific vigraha with generated forms; "" when a form is missing."""
    words = [reading.words[i] for i in members]
    final = words[-1]
    if len(words) < 2 or final.morph is None or not final.morph.vibhakti or st.stem_of(final) in TADDHITA_FINALS:
        return ""
    if any(w.morph is not None and w.morph.kind == "avyaya" and w.form not in st.PRADI | st.SAHA | st.NAN
           for w in words[:-1]):
        return ""  # an indeclinable member other than the prefixes: no generated vigraha
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
