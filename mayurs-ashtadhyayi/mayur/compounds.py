"""Compound (samasa) grouping, heuristic classification and vigraha.

The Python vidyut API offers no samasa derivation, so every type decided here is a
heuristic over the members' morphology; ``Compound.basis`` always says so.
Case forms in a vigraha are generated forward with vidyut-prakriya when possible.
"""

from __future__ import annotations

from dataclasses import replace
from functools import lru_cache
from typing import Optional

from mayur import lexicon, resources
from mayur.model import Compound, Morph, Reading, Word

# Final members meaning "best/chief of" govern a genitive first member (zazWI tatpurusha).
EXCELLENCE_STEMS = frozenset({"puMgava", "vara", "SrezWa", "Rzaba", "uttama", "pravara", "sattama", "siMha"})
# Agent-like final members (upapada / krt) that govern their first member.
AGENT_STEMS = frozenset({"vid", "jYa", "kara", "kft", "ga", "da", "pa", "Bft", "Dara", "hara", "ja"})
AGENT_KRTS = frozenset({"kvi~p", "ka", "aR", "Rvul", "tfc", "ac", "wa", "kvi~n", "Kac"})
# kta of these roots takes a locative object ("devoted to/in"); others default to instrumental.
LOCATIVE_KTA_ROOTS = frozenset({"ram", "rat", "niram", "sakta", "saYj", "ras"})
PRONOUN_STEMS = frozenset({"kim", "idam", "tad", "etad", "yad", "adas", "asmad", "yuzmad", "sarva", "ka", "anya"})

ADJ_KRTS = lexicon.PARTICIPLE_KRTS


def stem_lingas(m: Optional[Morph]) -> list[str]:
    if m is None or m.handle is None:
        return []
    prati = getattr(m.handle, "pratipadika_entry", None)
    return [str(x) for x in getattr(prati, "lingas", []) or []]


def is_adjectival(m: Optional[Morph]) -> bool:
    """Heuristic: participle, pronoun, or stem listed in all three genders."""
    if m is None or m.kind not in ("subanta", "stem"):
        return False
    if m.krt in ADJ_KRTS or m.lemma in PRONOUN_STEMS or m.lemma in EXCELLENCE_STEMS:
        return True
    return len(stem_lingas(m)) == 3


@lru_cache(maxsize=20_000)
def decline(stem: str, vibhakti: str, vacana: str, linga: Optional[str] = None) -> Optional[str]:
    """Forward-generate a case form of ``stem`` with vidyut-prakriya; None if unsure."""
    import vidyut.prakriya as P

    if linga is None:
        lingas = [x for m in lexicon.stem_analyses(stem) for x in stem_lingas(m)]
        linga = lingas[0] if lingas else _guess_linga(stem)
    if linga is None:
        return None
    return _derive(stem, vibhakti, vacana, linga)


def _derive(stem: str, vibhakti: str, vacana: str, linga: str) -> Optional[str]:
    import vidyut.prakriya as P

    try:
        args = P.Pada.Subanta(P.Pratipadika.basic(stem), P.Linga.from_string(linga),
                              P.Vibhakti.from_string(vibhakti), P.Vacana.from_string(vacana))
        texts = [p.text for p in resources.vyakarana().derive(args)]
    except Exception:  # vidyut raises on unsupported combinations
        return None
    return texts[0] if texts else None


def _guess_linga(stem: str) -> Optional[str]:
    """Gender of a stem not listed as a bare form: accept a gender only if its derived
    nominative singular is in the kosha under the same lemma."""
    for linga in ("puM", "strI", "napuMsaka"):
        nom = _derive(stem, "praTamA", "eka", linga)
        if nom and any(m.lemma == stem and m.linga == linga for m in lexicon.analyses(nom)):
            return linga
    return None


def _runs(words: list[Word]) -> list[list[int]]:
    runs, cur = [], []
    for i, w in enumerate(words):
        cur.append(i)
        if not w.in_compound:
            if len(cur) > 1:
                runs.append(cur)
            cur = []
    if len(cur) > 1:  # dangling run without a final member
        runs.append(cur)
    return runs


def _first_is_kta(form: str) -> bool:
    return any(m.krt == "kta" for m in lexicon.analyses(form + "s"))


def _exocentric(final: Word) -> bool:
    """Final member's form is listed only via a stem whose lexical gender disagrees."""
    m = final.morph
    if m is None or m.kind != "subanta":
        return False
    same_stem = [a for a in final.analyses if a.kind == "subanta" and a.krt is None]
    return bool(same_stem) and all(not a.lexical_linga_ok for a in same_stem if a.linga == m.linga)


def _gen(stem: str, vib: str, vac: str = "eka", linga: Optional[str] = None) -> str:
    return decline(stem, vib, vac, linga) or stem


def classify(words: list[Word], members: list[int]) -> tuple[str, str, str]:
    """Return (samasa, vigraha, basis) for one compound."""
    firsts = [words[i] for i in members[:-1]]
    final = words[members[-1]]
    fm = final.morph
    hy = "-".join(w.form for w in firsts + [final])
    if fm is None:
        return "unknown", hy, "heuristic: final member unanalysed"
    fstem, ff = fm.lemma, final.form
    nouns = [w.form for w in firsts]
    if fm.krt == "kta" and not is_adjectival(firsts[-1].morph):
        vib = "saptamI" if (fm.root in LOCATIVE_KTA_ROOTS or fm.lemma in LOCATIVE_KTA_ROOTS) else "tftIyA"
        parts = [_gen(n, vib) for n in nouns]
        inner = " ".join(parts) + (" ca" if len(parts) > 1 else "")
        extra = " (inner dvandva of the first members)" if len(parts) > 1 else ""
        return ("tatpurusha", f"{inner} {ff}",
                f"heuristic: kta-participle final member governs noun first member in {vib}{extra}")
    if fstem in EXCELLENCE_STEMS or fstem in AGENT_STEMS or fm.krt in AGENT_KRTS:
        vac = "bahu" if fstem in EXCELLENCE_STEMS else "eka"
        g = _gen(nouns[-1], "zazWI", vac)
        why = "'best-of' final member" if fstem in EXCELLENCE_STEMS else "agent final member"
        return "tatpurusha", " ".join(nouns[:-1] + [g, ff]), f"heuristic: {why} governs first member in zazWI"
    first_adj = is_adjectival(firsts[-1].morph) or _first_is_kta(firsts[-1].form)
    if first_adj and (_exocentric(final) or _first_is_kta(firsts[-1].form)):
        vib, vac = "praTamA", fm.vacana or "eka"
        noun = _noun_analysis(final)
        noun_l = next(iter(stem_lingas(noun)), None)
        a = _gen(nouns[-1], vib, vac, noun_l)
        n = _gen(noun.lemma if noun else fstem, vib, vac, noun_l)
        yasya = _gen("yad", "zazWI", vac, fm.linga or "puM")
        sah = _gen("tad", "praTamA", vac, fm.linga or "puM")
        return ("bahuvrihi", f"{a} {n} {yasya} {sah}",
                "heuristic: adjective+noun whose gender/agreement points to an external head")
    if first_adj:
        return ("karmadharaya", " ".join(nouns + [ff]),
                "heuristic: adjectival first member qualifies noun final member")
    if fm.vacana in ("dvi", "bahu") and fm.kind == "subanta":
        parts = [_gen(n, "praTamA") for n in nouns] + [_gen(fstem, "praTamA", "eka", fm.linga)]
        return "dvandva", " ca ".join(parts) + " ca", "heuristic: noun+noun with dual/plural final member"
    return "unknown", hy, "heuristic: no pattern matched"


def _noun_analysis(final: Word) -> Optional[Morph]:
    """The final member read as a plain (non-krdanta) noun, if the kosha lists one."""
    m = final.morph
    plain = [a for a in final.analyses if a.kind == "subanta" and a.krt is None
             and (m is None or a.vibhakti == m.vibhakti)]
    return plain[0] if plain else m


def annotate(reading: Reading) -> Reading:
    words = list(reading.words)
    compounds: list[Compound] = []
    for cid, members in enumerate(_runs(words)):
        samasa, vigraha, basis = classify(words, members)
        stem = "".join(words[i].form for i in members)
        compounds.append(Compound(id=cid, members=members, stem=stem, samasa=samasa,
                                  vigraha=vigraha, basis=basis))
        for i in members:
            words[i] = replace(words[i], compound=cid)
    return replace(reading, words=words, compounds=compounds)
