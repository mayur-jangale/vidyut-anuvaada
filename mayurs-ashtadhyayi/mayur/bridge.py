"""The single adapter to vidyut. Everything that leaves this module is Devanagari.

vidyut's kosha and prakriya engines speak a Roman sound code; this module converts at the
boundary with :func:`mayur.lipi.to_code` / :func:`mayur.lipi.from_code`. Vidyut objects are
passed outward only as opaque ``handle`` values that callers hand back to this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Optional

from mayur import lipi, resources
from mayur.model import Morph, SutraStep


@dataclass(frozen=True)
class Entry:
    """One kosha entry, converted. ``entry`` is "basic", "krdanta" or "tinanta"."""

    morph: Morph
    entry: str
    lingas: tuple[str, ...] = ()  # lexical genders of a basic stem
    pratipadika: str = ""  # basic stem text
    is_avyaya: bool = False


@dataclass(frozen=True)
class Derivation:
    text: str
    trace: tuple[SutraStep, ...]


_LINGA = {"puM": "पुंलिङ्ग", "strI": "स्त्रीलिङ्ग", "napuMsaka": "नपुंसकलिङ्ग"}
_VIBHAKTI = {"praTamA": "प्रथमा", "dvitIyA": "द्वितीया", "tftIyA": "तृतीया", "caturTI": "चतुर्थी",
             "paYcamI": "पञ्चमी", "zazWI": "षष्ठी", "saptamI": "सप्तमी", "samboDanam": "सम्बोधन",
             "samboDana": "सम्बोधन"}
_VACANA = {"eka": "एकवचन", "dvi": "द्विवचन", "bahu": "बहुवचन"}
_PURUSHA = {"praTama": "प्रथमपुरुष", "maDyama": "मध्यमपुरुष", "uttama": "उत्तमपुरुष"}
_LAKARA = {"la~w": "लट्", "li~w": "लिट्", "lu~w": "लुट्", "lf~w": "लृट्", "le~w": "लेट्", "lo~w": "लोट्",
           "la~N": "लङ्", "viDili~N": "विधिलिङ्", "ASIrli~N": "आशीर्लिङ्", "lu~N": "लुङ्", "lf~N": "लृङ्"}
_PRAYOGA = {"kartari": "कर्तरि", "karmaRi": "कर्मणि", "BAve": "भावे"}
_GANA = {"BvAdi": "भ्वादि", "adAdi": "अदादि", "juhotyAdi": "जुहोत्यादि", "divAdi": "दिवादि",
         "svAdi": "स्वादि", "tudAdi": "तुदादि", "ruDAdi": "रुधादि", "tanAdi": "तनादि",
         "kryAdi": "क्र्यादि", "curAdi": "चुरादि", "kaRqvAdi": "कण्ड्वादि"}

# Upasargas: Devanagari -> vidyut code.
UPASARGA_CODE = {"प्र": "pra", "परा": "parA", "अप": "apa", "सम्": "sam", "अनु": "anu", "अव": "ava",
                 "निस्": "nis", "निर्": "nis", "दुस्": "dus", "दुर्": "dus", "वि": "vi", "आ": "AN",
                 "नि": "ni", "अधि": "aDi", "अपि": "api", "अति": "ati", "सु": "su", "उद्": "ud",
                 "अभि": "aBi", "प्रति": "prati", "परि": "pari", "उप": "upa",
                 "पुरस्": "puras",  # पुरस् is a gati (1.4.67), prefixed like an upasarga
                 # gatis before कृ etc. (1.4.63 आदरानादरयोः सदसती, 1.4.64 भूषणेऽलम्, 1.4.65 अन्तरपरिग्रहे,
                 # 1.4.74 साक्षात्प्रभृतीनि च with नमस्); vidyut misplaces the augment after them, so only
                 # augment-free forms (क्त, ल्यप्, लट्) can match exactly
                 "सत्": "sat", "अलम्": "alam", "अन्तर्": "antar", "नमस्": "namas"}


_UPASARGA_OF_CODE = {"AN": "आ", "nis": "निस्", "dus": "दुस्"}


def _term(table: dict[str, str], value: Any) -> Optional[str]:
    if value is None:
        return None
    key = str(value)
    return table.get(key) or lipi.from_code(key.replace("~", ""))


def _krt(value: Any) -> Optional[str]:
    return None if value is None else lipi.from_code(str(value).replace("~", ""))


def _lyap(krt: Optional[str], prefixes: tuple[str, ...]) -> Optional[str]:
    """क्त्वा after an upasarga is replaced by ल्यप् (7.1.37); record what the form contains."""
    return "ल्यप्" if krt == "क्त्वा" and prefixes else krt


def _kind_of(obj: Any) -> str:
    return type(obj).__name__.rsplit("_", 1)[-1].lower()


def _dhatu_fields(dhatu_entry: Any) -> dict[str, Any]:
    dhatu = dhatu_entry.dhatu
    prefixes = tuple(_UPASARGA_OF_CODE.get(p, lipi.from_code(p)) for p in (getattr(dhatu, "prefixes", None) or []))
    plain = dhatu.with_prefixes([]) if prefixes else dhatu
    root_code = _root_code(plain)
    return {
        "lemma": lipi.from_code(dhatu_entry.clean_text),
        "root": lipi.from_code(root_code) if root_code else lipi.from_code(dhatu_entry.clean_text),
        "dhatu": lipi.from_code(dhatu.aupadeshika),
        "gana": _term(_GANA, getattr(dhatu, "gana", None)),
        "prefixes": prefixes,
        "root_gloss": getattr(dhatu_entry, "artha_en", None) or None,
    }


_ROOTS: dict[str, str] = {}


def _root_code(dhatu: Any) -> str:
    """Clean root text, from vidyut's own derivation of the bare dhatu (markers removed)."""
    key = repr(dhatu)
    if key not in _ROOTS:
        try:
            ps = resources.vyakarana().derive(dhatu)
            _ROOTS[key] = ps[0].text if ps else ""
        except Exception:  # noqa: BLE001 - vidyut raises plain exceptions for unsupported input
            _ROOTS[key] = ""
    return _ROOTS[key]


def _convert(code_form: str, form: str, e: Any) -> Optional[Entry]:
    kind = _kind_of(e)
    if kind == "tinanta":
        f = _dhatu_fields(e.dhatu_entry)
        m = Morph(form=form, lemma=f["lemma"], kind="tinanta", purusha=_term(_PURUSHA, e.purusha),
                  vacana=_term(_VACANA, e.vacana), lakara=_term(_LAKARA, e.lakara),
                  prayoga=_term(_PRAYOGA, e.prayoga), root=f["root"], dhatu=f["dhatu"], gana=f["gana"],
                  prefixes=f["prefixes"], root_gloss=f["root_gloss"], handle=e)
        return Entry(morph=m, entry="tinanta")
    pe = e.pratipadika_entry
    avyaya = bool(getattr(e, "is_avyaya", False))
    linga = _term(_LINGA, e.linga)
    vib = _term(_VIBHAKTI, e.vibhakti)
    vac = _term(_VACANA, e.vacana)
    if _kind_of(pe) == "krdanta":
        f = _dhatu_fields(pe.dhatu_entry)
        stem = _krdanta_stem(pe)
        m = Morph(form=form, lemma=f["lemma"], kind="avyaya" if avyaya else "subanta", stem=stem,
                  linga=None if avyaya else linga, vibhakti=None if avyaya else vib,
                  vacana=None if avyaya else vac, root=f["root"], dhatu=f["dhatu"], gana=f["gana"],
                  prefixes=f["prefixes"], krt=_lyap(_krt(pe.krt), f["prefixes"]), root_gloss=f["root_gloss"], handle=e)
        return Entry(morph=m, entry="krdanta", is_avyaya=avyaya)
    prati = pe.pratipadika
    text = lipi.from_code(prati.text)
    avyaya = avyaya or bool(getattr(prati, "is_avyaya", False))
    lingas = tuple(_term(_LINGA, x) or "" for x in (pe.lingas or []))
    m = Morph(form=form, lemma=text, kind="avyaya" if avyaya else "subanta",
              linga=None if avyaya else linga, vibhakti=None if avyaya else vib,
              vacana=None if avyaya else vac, handle=e)
    return Entry(morph=m, entry="basic", lingas=lingas, pratipadika=text, is_avyaya=avyaya)


_STEMS: dict[str, str] = {}


def _krdanta_stem(pe: Any) -> str:
    key = repr(pe)
    if key not in _STEMS:
        try:
            ps = resources.vyakarana().derive(pe)
            _STEMS[key] = lipi.from_code(ps[0].text) if ps else ""
        except Exception:  # noqa: BLE001
            _STEMS[key] = ""
    return _STEMS[key]


@lru_cache(maxsize=200_000)
def lookup(form: str) -> tuple[Entry, ...]:
    """All kosha entries keyed by the Devanagari pada ``form``."""
    if not form:
        return ()
    code = lipi.to_code(form)
    raw = resources.kosha().get(code)  # a missing kosha raises FileNotFoundError: never cached as "no entries"
    out = []
    for e in raw:
        conv = _convert(code, form, e)
        if conv is not None:
            out.append(conv)
    return tuple(out)


def _steps(prakriya: Any) -> tuple[SutraStep, ...]:
    return tuple(
        SutraStep(source=lipi.from_code(str(s.source)), code=str(s.code),
                  result=" + ".join(lipi.from_code(t) for t in s.result))
        for s in prakriya.history
    )


def derive(handle: Any) -> tuple[Derivation, ...]:
    """Forward vidyut-prakriya derivations of an opaque handle (kosha entry or Pada)."""
    if handle is None:
        return ()
    try:
        ps = resources.vyakarana().derive(handle)
    except Exception:  # noqa: BLE001
        return ()
    return tuple(Derivation(text=lipi.from_code(p.text), trace=_steps(p)) for p in ps)


def derived_texts(handle: Any) -> tuple[str, ...]:
    """Only the final texts of vidyut's forward derivations (cheap: no trace conversion)."""
    if handle is None:
        return ()
    try:
        ps = resources.vyakarana().derive(handle)
    except Exception:  # noqa: BLE001
        return ()
    return tuple(lipi.from_code(p.text) for p in ps)


def stem_handle(entry: Entry) -> Any:
    """Handle whose derivation yields the stem: the krdanta PratipadikaEntry, or the basic
    Pratipadika (1.2.45)."""
    e = entry.morph.handle
    if e is None or entry.entry == "tinanta":
        return None
    pe = e.pratipadika_entry
    return pe if entry.entry == "krdanta" else pe.pratipadika


def basic_pratipadika_handle(stem: str) -> Any:
    from vidyut.prakriya import Pratipadika

    return Pratipadika.basic(lipi.to_code(stem))


def prefixed_tinanta(entry: Entry, upasargas: tuple[str, ...]) -> Any:
    """A Pada.Tinanta for ``entry``'s verb with ``upasargas`` (Devanagari) prefixed."""
    from vidyut.prakriya import Pada

    e = entry.morph.handle
    dhatu = e.dhatu_entry.dhatu
    if getattr(dhatu, "prefixes", None):
        return None
    codes = [UPASARGA_CODE[u] for u in upasargas]
    return Pada.Tinanta(dhatu=dhatu.with_prefixes(codes), prayoga=e.prayoga, lakara=e.lakara,
                        purusha=e.purusha, vacana=e.vacana)


_LINGA_ENUM = ("Pum", "Stri", "Napumsaka")
_VIB_ENUM = ("Prathama", "Dvitiya", "Trtiya", "Caturthi", "Panchami", "Sasthi", "Saptami", "Sambodhana")
_VAC_ENUM = ("Eka", "Dvi", "Bahu")


def subanta_paradigm(stem: str, linga: str, nyap: bool = False, taddhita: str = "") -> tuple[tuple[Any, Morph], ...]:
    """Every (handle, Morph-template) of ``stem`` (Devanagari) in ``linga`` (Devanagari term);
    with ``nyap`` the stem is a feminine in ङी/आप् (सुमुखी, शिष्या: 4.1.4, 4.1.41ff.); with
    ``taddhita`` (its Devanagari name without markers, e.g. त्व) the stem is ``stem`` + that suffix."""
    from vidyut.prakriya import Linga, Pada, Pratipadika, Taddhita, Vacana, Vibhakti

    lmap = {"पुंलिङ्ग": Linga.Pum, "स्त्रीलिङ्ग": Linga.Stri, "नपुंसकलिङ्ग": Linga.Napumsaka}
    try:
        prati = (Pratipadika.nyap if nyap else Pratipadika.basic)(lipi.to_code(stem))
        if taddhita:
            prati = Pratipadika.taddhitanta(prati, getattr(Taddhita, lipi.to_code(taddhita)))
    except (ValueError, AttributeError):  # a sound vidyut's code cannot spell, an unknown suffix
        return ()
    out = []
    for vib in Vibhakti.choices():
        for vac in Vacana.choices():
            pada = Pada.Subanta(pratipadika=prati, linga=lmap[linga], vibhakti=vib, vacana=vac)
            m = Morph(form="", lemma=stem, kind="subanta", linga=linga, vibhakti=_term(_VIBHAKTI, vib),
                      vacana=_term(_VACANA, vac), source="generated", quality=1, handle=pada)
            out.append((pada, m))
    return tuple(out)


def matup_subanta(handle: Any) -> Any:
    """For a kosha subanta of a basic stem in -वत्/-मत्, the same pada with the stem built as a
    taddhitanta (base + मतुँप्), which vidyut needs to apply 7.1.70 and 6.4.14 (गुणवान्)."""
    from vidyut.prakriya import Pada, Pratipadika, Taddhita

    pe = getattr(handle, "pratipadika_entry", None)
    if pe is None or type(pe).__name__.rsplit("_", 1)[-1] != "Basic":
        return None
    text = pe.pratipadika.text
    if len(text) < 5 or text[-3:] not in ("vat", "mat"):
        return None
    base = Pratipadika.basic(text[:-3])
    stem = Pratipadika.taddhitanta(base, Taddhita.matup)
    return Pada.Subanta(pratipadika=stem, linga=handle.linga, vibhakti=handle.vibhakti, vacana=handle.vacana)


def prefixed_krdanta(entry: Entry, upasargas: tuple[str, ...], as_ktva: bool = False) -> Any:
    """A Pada.Subanta for ``entry``'s krdanta with ``upasargas`` (Devanagari) put before the
    prefixes its dhatu already has; vidyut then applies e.g. 7.1.37 (क्त्वा -> ल्यप्)."""
    from vidyut.prakriya import Krt, Pada, Pratipadika

    e = entry.morph.handle
    pe = e.pratipadika_entry
    prayoga = getattr(pe, "prayoga", None)
    if prayoga is not None and str(prayoga) != "kartari":
        return None  # the Python API cannot pass a krdanta's karmani/bhave prayoga
    dhatu = pe.dhatu_entry.dhatu
    codes = [UPASARGA_CODE[u] for u in upasargas] + list(getattr(dhatu, "prefixes", None) or [])
    try:
        stem = Pratipadika.krdanta(dhatu.with_prefixes(codes), Krt.ktvA if as_ktva else pe.krt)
        return Pada.Subanta(pratipadika=stem, linga=e.linga, vibhakti=e.vibhakti, vacana=e.vacana)
    except Exception:  # noqa: BLE001
        return None


def dhatu_of(entry: Entry) -> Any:
    """The vidyut Dhatu of a tinanta or kṛdanta kosha entry (opaque)."""
    e = entry.morph.handle
    de = getattr(e, "dhatu_entry", None) or getattr(getattr(e, "pratipadika_entry", None), "dhatu_entry", None)
    return de.dhatu if de is not None else None


def ktva_of_verb(entry: Entry, upasargas: tuple[str, ...]) -> Any:
    """A Pada for the क्त्वा/ल्यप् absolutive of a kosha entry's dhatu with ``upasargas``."""
    from vidyut.prakriya import Krt, Linga, Pada, Pratipadika, Vacana, Vibhakti

    dhatu = dhatu_of(entry)
    if dhatu is None:
        return None
    codes = [UPASARGA_CODE[u] for u in upasargas] + list(getattr(dhatu, "prefixes", None) or [])
    try:
        stem = Pratipadika.krdanta(dhatu.with_prefixes(codes), Krt.ktvA)
        return Pada.Subanta(pratipadika=stem, linga=Linga.Pum, vibhakti=Vibhakti.Prathama, vacana=Vacana.Eka)
    except Exception:  # noqa: BLE001
        return None


def kandvadi_paradigm(aupadeshika: str) -> tuple[tuple[str, Morph], ...]:
    """(text, Morph-with-Pada-handle) for every kartari tiṅanta of a kaṇḍvādi dhātu such as महीङ् (3.1.27)."""
    from vidyut.prakriya import Dhatu, Gana, Lakara, Pada, Prayoga, Purusha, Vacana

    try:
        dhatu = Dhatu.mula(lipi.to_code(aupadeshika), Gana.Kandvadi)
    except Exception:  # noqa: BLE001
        return ()
    root = lipi.from_code(_root_code(dhatu))
    out = []
    lakaras = (Lakara.Lat, Lakara.Lot, Lakara.Lan, Lakara.VidhiLin, Lakara.Lit, Lakara.Lrt, Lakara.Lut)
    cells = [(lak, pur, vac) for lak in lakaras + (Lakara.AshirLin,) for pur in Purusha.choices() for vac in Vacana.choices()]
    for lak, pur, vac in cells:
        pada = Pada.Tinanta(dhatu=dhatu, prayoga=Prayoga.Kartari, lakara=lak, purusha=pur, vacana=vac)
        m = Morph(form="", lemma=root, kind="tinanta", purusha=_term(_PURUSHA, pur), vacana=_term(_VACANA, vac),
                  lakara=_term(_LAKARA, lak), prayoga="कर्तरि", root=root, dhatu=aupadeshika, gana="कण्ड्वादि",
                  source="generated", quality=3, handle=pada)
        out.extend((t, m) for t in derived_texts(pada))
    return tuple(out)


def pratipadika_of(handle: Any) -> Any:
    """The pratipadika inside a Pada.Subanta handle (its own derivation gives the stem)."""
    return getattr(handle, "pratipadika", None)


def tasi_pada(stem: str) -> Any:
    """Pada of ``stem`` + तसि (5.4.44 प्रतियोगे पञ्चम्यास्तसिः): अनुराग -> अनुरागतस्."""
    from vidyut.prakriya import Linga, Pada, Pratipadika, Taddhita, Vacana, Vibhakti

    try:
        t = Pratipadika.taddhitanta(Pratipadika.basic(lipi.to_code(stem)), Taddhita.tasi)
        return Pada.Subanta(pratipadika=t, linga=Linga.Napumsaka, vibhakti=Vibhakti.Prathama, vacana=Vacana.Eka)
    except Exception:  # noqa: BLE001
        return None


@lru_cache(maxsize=1)
def kta_index() -> dict[str, tuple[Any, ...]]:
    """क्त stem -> kosha DhatuEntries (unprefixed, plain or ṇic) whose क्त derivation yields it (built once)."""
    from vidyut.prakriya import Krt, Pratipadika, Sanadi

    v = resources.vyakarana()
    table: dict[str, list[Any]] = {}
    for de in resources.kosha().dhatus():
        d = de.dhatu
        if d.prefixes or (d.sanadi and list(d.sanadi) != [Sanadi.Ric]):
            continue
        for t in {p.text for p in derive_quiet(v, Pratipadika.krdanta(d, Krt.kta))}:
            table.setdefault(lipi.from_code(t), []).append(de)
    return {k: tuple(x) for k, x in table.items()}


def derive_quiet(v: Any, handle: Any) -> list[Any]:
    try:
        return v.derive(handle)
    except Exception:  # noqa: BLE001
        return []


kta_fields = _dhatu_fields  # Devanagari lemma/root/dhatu/gana/root_gloss of an opaque dhātu entry


def kta_pratipadika(dhatu_entry: Any, upasargas: tuple[str, ...]) -> Any:
    """The क्त kṛdanta stem of ``dhatu_entry`` with ``upasargas`` (Devanagari), or None."""
    from vidyut.prakriya import Krt, Pratipadika

    try:
        codes = [UPASARGA_CODE[u] for u in upasargas]
        return Pratipadika.krdanta(dhatu_entry.dhatu.with_prefixes(codes), Krt.kta)
    except Exception:  # noqa: BLE001
        return None


def subanta_like(pratipadika: Any, entry: Entry) -> Any:
    """A Pada.Subanta of ``pratipadika`` in the linga/vibhakti/vacana of the kosha ``entry``."""
    from vidyut.prakriya import Pada

    e = entry.morph.handle
    return Pada.Subanta(pratipadika=pratipadika, linga=e.linga, vibhakti=e.vibhakti, vacana=e.vacana)
