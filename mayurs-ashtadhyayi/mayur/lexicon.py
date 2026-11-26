"""Word lookup (vidyut-kosha) and forward derivation (vidyut-prakriya).

Nothing here runs a sutra backward: a form is accepted only if it is listed in the
kosha or reproduced by a forward derivation. Candidate generation (upasarga
stripping, out-of-kosha stems) only *proposes* vidyut arguments; a candidate is
kept only when the forward derivation yields exactly the form.
"""

from __future__ import annotations

from dataclasses import replace
from functools import lru_cache
from typing import Any, Iterable

from mayur import lexicon_gen as gen
from mayur import resources
from mayur.model import Morph, SutraStep, WordProof

PARTICIPLE_KRTS = frozenset(
    {"kta", "ktavatu~", "Satf~", "SAnac", "tavya", "anIyar", "yat", "Ryat", "kyap", "kvasu~", "kAnac",
     "ktvA", "lyap", "tumun"}
)
GOOD = 2  # quality threshold below which fallbacks are tried


def _s(value) -> str | None:
    return None if value is None else str(value)


def _dhatu_fields(dhatu_entry) -> dict:
    dhatu = dhatu_entry.dhatu
    return {
        "root": dhatu_entry.clean_text,
        "dhatu": dhatu.aupadeshika,
        "gana": _s(dhatu.gana),
        "prefixes": tuple(dhatu.prefixes or ()),
        "root_gloss": dhatu_entry.artha_en or None,
    }


def _to_morph(form: str, entry) -> Morph:
    if gen.is_tinanta_entry(entry):
        return Morph(
            form=form,
            lemma=entry.dhatu_entry.clean_text,
            kind="tinanta",
            purusha=_s(entry.purusha),
            lakara=_s(entry.lakara),
            prayoga=_s(entry.prayoga),
            vacana=_s(entry.vacana),
            handle=entry,
            **_dhatu_fields(entry.dhatu_entry),
        )
    prati = entry.pratipadika_entry
    is_krdanta = gen.is_krdanta_entry(entry)
    extra = {"krt": _s(prati.krt), **_dhatu_fields(prati.dhatu_entry)} if is_krdanta else {}
    if entry.is_avyaya or (is_krdanta and str(prati.krt) in gen.AVYAYA_KRTS):
        return Morph(form=form, lemma=entry.lemma, kind="avyaya", handle=entry, **extra)
    lingas = [] if is_krdanta else [str(x) for x in prati.lingas]
    linga = _s(entry.linga)
    return Morph(
        form=form,
        lemma=entry.lemma,
        kind="subanta",
        linga=linga,
        vibhakti=_s(entry.vibhakti),
        vacana=_s(entry.vacana),
        lexical_linga_ok=(not lingas) or linga in lingas,
        handle=entry,
        **extra,
    )


def quality(m: Morph) -> int:
    """Prior plausibility of an analysis: 3 = ordinary, 0 = kosha over-generation.

    Out-of-kosha nominals (``source="generated"``, no krt) get 1: derivable, but the
    stem itself is only a guess from the ending.
    """
    if m.kind == "unknown":
        return 0
    if m.kind in ("tinanta", "avyaya"):
        return 0 if m.krt == "kvi~p" else 3
    if m.kind == "stem":
        return 0 if m.krt == "kvi~p" else 3
    if m.krt is None:
        if m.source == "generated":
            return 1
        return 3 if m.lexical_linga_ok else 2
    if m.krt in PARTICIPLE_KRTS:
        return 3
    return 0 if m.krt == "kvi~p" else 1


def _lemma_count(lemma: str) -> int:
    try:
        from mayur import freq  # written by another agent; optional
    except ImportError:
        return 0
    try:
        return int(freq.lemma_count(lemma))
    except Exception:
        return 0


def _rank(m: Morph) -> tuple:
    return (quality(m), m.lexical_linga_ok, m.source == "kosha", _lemma_count(m.lemma))


def _ranked(morphs: Iterable[Morph]) -> tuple[Morph, ...]:
    unique = dict.fromkeys(morphs)
    return tuple(sorted(unique, key=_rank, reverse=True))


def _kosha_morphs(form: str, lookup: str | None = None) -> list[Morph]:
    return [_to_morph(form, e) for e in resources.kosha().get(lookup or form)]


# --------------------------------------------------------------------------- upasargas


def _generated_from(form: str, extra: tuple[str, ...], entry) -> list[Morph]:
    """Re-derive kosha ``entry`` with upasargas ``extra``; keep exact reproductions."""
    pada = gen.prefixed_pada(entry, extra)
    if pada is None or form not in gen.derive_texts(pada):
        return []
    base = _to_morph(form, entry)
    prefixes = tuple(extra) + base.prefixes
    return [replace(base, lemma=gen.join_prefixes(extra, base.lemma), prefixes=prefixes,
                    source="generated", handle=pada)]


def _lyap_from(form: str, extra: tuple[str, ...], entries: list) -> list[Morph]:
    """Prefixed absolutive (ktvA -> lyap, 7.1.37) of any dhatu found in the remainder."""
    if not form.endswith("ya"):
        return []
    out: list[Morph] = []
    seen: set[str] = set()
    for e in entries:
        dhatu_entry = e.dhatu_entry if gen.is_tinanta_entry(e) else (
            e.pratipadika_entry.dhatu_entry if gen.is_krdanta_entry(e) else None)
        if dhatu_entry is None or repr(dhatu_entry.dhatu) in seen:
            continue
        seen.add(repr(dhatu_entry.dhatu))
        pada = gen.lyap_pada(dhatu_entry.dhatu, extra)
        if form in gen.derive_texts(pada):
            fields = _dhatu_fields(dhatu_entry)
            fields["prefixes"] = tuple(extra) + fields["prefixes"]
            out.append(Morph(form=form, lemma=gen.join_prefixes(fields["prefixes"], dhatu_entry.clean_text),
                             kind="avyaya", krt="lyap", source="generated", handle=pada, **fields))
    return out


def _verbal_entries(lookup: str) -> list:
    return [e for e in resources.kosha().get(lookup)
            if gen.is_tinanta_entry(e) or (gen.is_krdanta_entry(e) and str(e.pratipadika_entry.krt) != "kvi~p")]


@lru_cache(maxsize=100_000)
def _upasarga_morphs(form: str, depth: int = 2) -> tuple[Morph, ...]:
    """Analyses of ``form`` as upasarga(s) + a kosha verb/krdanta, verified forward."""
    out: list[Morph] = []
    for u, rem in gen.upasarga_splits(form):
        entries = _verbal_entries(rem)
        for e in entries:
            out += _generated_from(form, (u,), e)
        out += _lyap_from(form, (u,), entries)
        if depth > 1 and not entries:
            for u2, rem2 in gen.upasarga_splits(rem):
                entries2 = _verbal_entries(rem2)
                for e in entries2:
                    out += _generated_from(form, (u, u2), e)
                out += _lyap_from(form, (u, u2), entries2)
    return tuple(dict.fromkeys(out))


# --------------------------------------------------------------------------- nominals


def _generated_nominals(form: str) -> list[Morph]:
    out = []
    for stem, linga, vib, vac, pada in gen.generated_subantas(form):
        out.append(Morph(form=form, lemma=stem, kind="subanta", linga=str(linga), vibhakti=str(vib),
                         vacana=str(vac), source="generated", handle=pada))
    return out


def _with_variants(form: str) -> list[Morph]:
    """Kosha analyses of spelling variants (final H/M, anusvara vs. class nasal)."""
    out: list[Morph] = []
    for v in gen.final_variants(form) + gen.nasal_variants(form):
        out += [replace(m, form=form) for m in _kosha_morphs(v)]
    return out


@lru_cache(maxsize=200_000)
def _core_analyses(form: str) -> tuple[Morph, ...]:
    """Kosha + spelling variants + upasarga generation (no nominal guessing)."""
    found = _kosha_morphs(form)
    if not any(quality(m) >= GOOD for m in found):
        found += _with_variants(form)
    if not any(quality(m) >= GOOD for m in found):
        found += list(_upasarga_morphs(form))
    return _ranked(found)


@lru_cache(maxsize=200_000)
def analyses(form: str) -> tuple[Morph, ...]:
    """All analyses of ``form`` as a complete pada, best first. Empty if not a pada."""
    found = list(_core_analyses(form))
    if not any(quality(m) >= GOOD for m in found):
        found += _generated_nominals(form)
    return _ranked(found)


# --------------------------------------------------------------------------- stems


def _stem_morph(form: str, m: Morph) -> Morph | None:
    """Stem analysis of ``form`` drawn from pada analysis ``m`` (of a probe form)."""
    entry = m.handle
    if m.kind not in ("subanta",) and not (m.kind == "avyaya" and m.krt is None):
        return None
    if m.krt is not None:
        if m.krt == "kvi~p" and len(form) < 3:
            return None
        prati = getattr(entry, "pratipadika", None) or getattr(entry, "pratipadika_entry", None)
        dhatu, krt = _krdanta_args(entry)
        if dhatu is None:
            return None
        stem = gen.krdanta_stem_text(dhatu, krt)
        if form not in gen.member_forms(stem):
            return None
        from vidyut.prakriya import Pratipadika

        del prati
        handle = gen.StemHandle("krdanta", stem, form, Pratipadika.krdanta(dhatu, krt))
        return Morph(form=form, lemma=stem, kind="stem", root=m.root, dhatu=m.dhatu, gana=m.gana,
                     prefixes=m.prefixes, krt=m.krt, root_gloss=m.root_gloss, source=m.source, handle=handle)
    stem = m.lemma
    if m.source != "kosha" or form not in gen.member_forms(stem):
        return None
    lingas = [str(x) for x in entry.pratipadika_entry.lingas] if hasattr(entry, "pratipadika_entry") else []
    handle = gen.StemHandle("kosha-pratipadika", stem, form)
    return Morph(form=form, lemma=stem, kind="stem", linga=lingas[0] if len(lingas) == 1 else None,
                 source="kosha", handle=handle)


def _krdanta_args(handle: Any) -> tuple[Any, Any]:
    """(dhatu, krt) of a kosha krdanta entry or a generated prefixed Pada."""
    prati_entry = getattr(handle, "pratipadika_entry", None)
    if prati_entry is not None and hasattr(prati_entry, "krt"):
        return prati_entry.dhatu_entry.dhatu, prati_entry.krt
    return None, None


def _special_stem(form: str) -> list[Morph]:
    if form not in gen.SPECIAL_STEMS:
        return []
    lemma, note = gen.SPECIAL_STEMS[form]
    return [Morph(form=form, lemma=lemma, kind="stem", source="kosha",
                  handle=gen.StemHandle("special", lemma, form, note=note))]


@lru_cache(maxsize=200_000)
def stem_analyses(form: str) -> tuple[Morph, ...]:
    """Analyses of ``form`` as a non-final compound member (bare stem), best first."""
    out: list[Morph] = _special_stem(form)
    for probe in gen.stem_probe_forms(form):
        for m in _kosha_morphs(probe):
            s = _stem_morph(form, m)
            if s is not None:
                out.append(s)
    if not any(quality(m) >= 3 for m in out):
        out += _prefixed_krdanta_stems(form)
    return _ranked(out)


def _prefixed_krdanta_stems(form: str) -> list[Morph]:
    """Stems like ``nirata``: upasarga + kosha krdanta, stem derived forward."""
    from vidyut.prakriya import Pratipadika

    out = []
    for m in _upasarga_morphs(form + "m") + _upasarga_morphs(form + "s"):
        if m.krt is None or m.kind != "subanta":
            continue
        prati = Pratipadika.krdanta(*_pada_krdanta_args(m.handle))
        texts = gen.derive_texts(prati)
        if texts and form in gen.member_forms(texts[0]):
            out.append(Morph(form=form, lemma=texts[0], kind="stem", root=m.root, dhatu=m.dhatu, gana=m.gana,
                             prefixes=m.prefixes, krt=m.krt, root_gloss=m.root_gloss, source="generated",
                             handle=gen.StemHandle("krdanta", texts[0], form, prati)))
    return out


def _pada_krdanta_args(pada: Any) -> tuple[Any, Any]:
    prati = pada.pratipadika
    return prati.dhatu, prati.krt


def is_pada(form: str, min_quality: int = 0) -> bool:
    return any(quality(m) >= min_quality for m in analyses(form))


def is_stem(form: str) -> bool:
    return bool(stem_analyses(form))


# --------------------------------------------------------------------------- proof


def _trace(p) -> list[SutraStep]:
    return [SutraStep(str(s.source), s.code, " + ".join(s.result)) for s in p.history]


def _derive_matching(arg: Any, target: str) -> WordProof:
    try:
        prakriyas = resources.vyakarana().derive(arg)
    except Exception as exc:  # vidyut raises on unsupported argument combinations
        return WordProof(derivable=False, note=f"vidyut-prakriya error: {exc}")
    norm = gen.nasal_norm(target)
    for p in prakriyas:
        if p.text == target or gen.nasal_norm(p.text) == norm:
            note = "" if p.text == target else f"derived {p.text}; {target} is a spelling variant (8.4.59)"
            return WordProof(True, "vidyut-prakriya", p.text, _trace(p), note)
    got = ", ".join(p.text for p in prakriyas) or "nothing"
    return WordProof(derivable=False, note=f"vidyut-prakriya derives {got}, not {target}")


def _prove_stem(m: Morph) -> WordProof:
    h = m.handle
    if not isinstance(h, gen.StemHandle):
        return WordProof(derivable=False, note="no stem handle")
    if h.method == "krdanta":
        proof = _derive_matching(h.pratipadika, h.stem)
        if proof.derivable and m.form != h.stem:
            proof.note = f"stem {h.stem}; compound-member form {m.form} by 1.4.17 + 8.2.7/8.2.30/8.2.39"
        return proof
    if h.method == "kosha-pratipadika":
        member = "" if m.form == h.stem else f"; member form {m.form} by 1.4.17 + 8.2.7/8.2.30/8.2.39"
        return WordProof(True, "kosha-pratipadika", m.form, [],
                         f"listed underived pratipadika {h.stem} (1.2.45 arthavad adhAtur apratyayaH "
                         f"prAtipadikam / 1.2.46 kfttaddhitasamAsAS ca); not derived by vidyut{member}")
    return WordProof(True, "special-stem", m.form, [], f"{h.stem}: {h.note}; not derived by vidyut")


def prove(m: Morph) -> WordProof:
    """Forward-derive ``m`` with vidyut-prakriya and check it yields ``m.form``."""
    if m.handle is None:
        return WordProof(derivable=False, note="no derivation arguments")
    if m.kind == "stem":
        return _prove_stem(m)
    proof = _derive_matching(m.handle, m.form)
    if not proof.derivable and m.source == "kosha":
        proof.note += "; attested in vidyut-kosha but not reproduced by vidyut-prakriya"
    return proof
