"""Word lookup (vidyut-kosha) and forward derivation (vidyut-prakriya).

Nothing here runs a sutra backward: a form is accepted only if it is listed in the
kosha or reproduced by a forward derivation.
"""

from __future__ import annotations

from functools import lru_cache

from mayur import resources
from mayur.model import Morph, SutraStep, WordProof

PARTICIPLE_KRTS = frozenset(
    {"kta", "ktavatu~", "Satf~", "SAnac", "tavya", "anIyar", "yat", "Ryat", "kyap", "kvasu~", "kAnac"}
)


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
    if type(entry).__name__.endswith("Tinanta"):
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
    is_krdanta = type(prati).__name__.endswith("Krdanta")
    extra = {"krt": _s(prati.krt), **_dhatu_fields(prati.dhatu_entry)} if is_krdanta else {}
    if entry.is_avyaya:
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
    """Prior plausibility of an analysis: 3 = ordinary, 0 = kosha over-generation."""
    if m.kind in ("tinanta", "avyaya"):
        return 3
    if m.krt is None:
        return 3 if m.lexical_linga_ok else 2
    if m.krt in PARTICIPLE_KRTS:
        return 3
    return 0 if m.krt == "kvi~p" else 1


@lru_cache(maxsize=200_000)
def analyses(form: str) -> tuple[Morph, ...]:
    """All analyses of ``form`` as a complete pada, best first. Empty if not a pada."""
    seen: dict[Morph, None] = {}
    for entry in resources.kosha().get(form):
        seen.setdefault(_to_morph(form, entry))
    return tuple(sorted(seen, key=quality, reverse=True))


@lru_cache(maxsize=200_000)
def stem_analyses(form: str) -> tuple[Morph, ...]:
    """Analyses of ``form`` as a non-final compound member (bare stem)."""
    out: dict[Morph, None] = {}
    for m in analyses(form):
        if m.kind == "avyaya" or (m.kind == "subanta" and m.krt is None and m.lemma == form):
            stem = Morph(form=form, lemma=m.lemma, kind="stem", source=m.source, handle=m.handle)
            out.setdefault(stem)
    return tuple(out)


def is_pada(form: str, min_quality: int = 0) -> bool:
    return any(quality(m) >= min_quality for m in analyses(form))


def is_stem(form: str) -> bool:
    return bool(stem_analyses(form))


def prove(m: Morph) -> WordProof:
    """Forward-derive ``m`` with vidyut-prakriya and check it yields ``m.form``."""
    if m.handle is None:
        return WordProof(derivable=False, note="no derivation arguments")
    if m.kind == "stem":
        return WordProof(derivable=True, method="kosha-pratipadika", derived_form=m.form,
                         note="listed pratipadika; compound-internal form not derived")
    try:
        prakriyas = resources.vyakarana().derive(m.handle)
    except Exception as exc:  # vidyut raises on unsupported argument combinations
        return WordProof(derivable=False, note=f"vidyut-prakriya error: {exc}")
    for p in prakriyas:
        if p.text == m.form:
            trace = [SutraStep(str(s.source), s.code, " + ".join(s.result)) for s in p.history]
            return WordProof(True, "vidyut-prakriya", p.text, trace)
    got = ", ".join(p.text for p in prakriyas) or "nothing"
    return WordProof(derivable=False, note=f"vidyut-prakriya derives {got}, not {m.form}")
