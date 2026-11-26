"""Forward-generation helpers for :mod:`mayur.lexicon`.

Everything here proposes *candidates* by string inspection and then keeps only
those that vidyut-prakriya derives forward to exactly the observed form (or, for
compound-member stems, whose stem text a forward derivation / the kosha supplies).
No sutra is ever applied backward.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Iterable, Optional

from mayur import resources

# Upasargas as vidyut spells them ("AN" is the upadesha of A).
UPASARGAS: tuple[str, ...] = (
    "pra", "parA", "apa", "sam", "anu", "ava", "nis", "nir", "dus", "dur", "vi", "AN",
    "ni", "aDi", "api", "ati", "su", "ud", "aBi", "prati", "pari", "upa",
)
AVYAYA_KRTS = frozenset({"ktvA", "lyap", "tumun", "Ramul", "kamul"})
VOWELS = frozenset("aAiIuUfFxXeEoO")
_MERGED: dict[str, tuple[str, ...]] = {  # a-final upasarga + vowel -> merged vowel (6.1.87/88/101)
    "A": ("a", "A"), "e": ("i", "I"), "o": ("u", "U"), "E": ("e", "E"), "O": ("o", "O"),
    "Ar": ("f",), "ar": ("f",),
}
_CONSONANT_SURFACES: dict[str, tuple[str, ...]] = {
    "sam": ("sam", "saM", "saN", "saY", "saR", "san"),
    "ud": ("ud", "ut", "un", "uc", "uj", "uq", "ul"),
    "nis": ("nis", "niz", "niS", "niH"),
    "nir": ("nir", "nI"),
    "dus": ("dus", "duz", "duS", "duH"),
    "dur": ("dur", "dU"),
}
_NASAL_BY_CLASS = {
    **dict.fromkeys("kKgGN", "N"), **dict.fromkeys("cCjJY", "Y"), **dict.fromkeys("wWqQR", "R"),
    **dict.fromkeys("tTdDn", "n"), **dict.fromkeys("pPbBm", "m"),
}


def upasarga_text(u: str) -> str:
    """Surface spelling of an upasarga (``AN`` -> ``A``)."""
    return "A" if u == "AN" else u


def join_prefixes(prefixes: Iterable[str], base: str) -> str:
    """Join upasargas and a root/lemma with basic vowel sandhi (for lemma display)."""
    out = base
    for u in reversed(tuple(prefixes)):
        out = _join_vowels(upasarga_text(u), out)
    return out


def _join_vowels(left: str, right: str) -> str:
    if not left or not right or left[-1] not in VOWELS or right[0] not in VOWELS:
        return left + right
    a, b = left[-1], right[0]
    if a in "aA":
        merged = {"a": "A", "A": "A", "i": "e", "I": "e", "u": "o", "U": "o", "f": "ar",
                  "e": "E", "E": "E", "o": "O", "O": "O"}.get(b, b)
        return left[:-1] + merged + right[1:]
    if a in "iI":
        return left[:-1] + ("I" + right[1:] if b in "iI" else "y" + right)
    if a in "uU":
        return left[:-1] + ("U" + right[1:] if b in "uU" else "v" + right)
    return left + right


def _remainder_fixes(rem: str) -> tuple[str, ...]:
    """Undo prefix-triggered retroflexion in the remainder (8.4.14 Ratva, 8.3.65 zatva)."""
    out = [rem]
    if "R" in rem:
        out.append(rem.replace("R", "n", 1))
    if rem.startswith("zW"):
        out.append("sT" + rem[2:])
    elif rem.startswith("z"):
        out.append("s" + rem[1:])
    return tuple(out)


def _surfaces(u: str) -> list[tuple[str, str]]:
    """(surface, restored-initial) pairs for upasarga ``u`` before a following root."""
    text = upasarga_text(u)
    if u in _CONSONANT_SURFACES:
        return [(s, "") for s in _CONSONANT_SURFACES[u]]
    out = [(text, "")]
    last, head = text[-1], text[:-1]
    if last in "iI":
        out += [(head + "y", ""), (head + "I", "i")]
    elif last in "uU":
        out += [(head + "v", ""), (head + "U", "u")]
    elif last in "aA":
        out += [(head + m, r) for m, rs in _MERGED.items() for r in rs]
    return out


@lru_cache(maxsize=100_000)
def upasarga_splits(form: str) -> tuple[tuple[str, str], ...]:
    """Candidate (upasarga, remainder) pairs; remainders restored to pre-sandhi spelling."""
    out: dict[tuple[str, str], None] = {}
    for u in UPASARGAS:
        for surface, restore in _surfaces(u):
            if not form.startswith(surface):
                continue
            rem = restore + form[len(surface):]
            if len(rem) < 2:
                continue
            if restore and rem[len(restore):len(restore) + 1] in VOWELS:
                continue
            for r in _remainder_fixes(rem):
                out.setdefault((u, r))
    return tuple(out)


def nasal_variants(form: str) -> tuple[str, ...]:
    """Spelling variants anusvara <-> homorganic nasal before a stop (8.4.58/59)."""
    alt_n = "".join(
        _NASAL_BY_CLASS.get(form[i + 1], c) if c == "M" and i + 1 < len(form) else c
        for i, c in enumerate(form)
    )
    return tuple(v for v in dict.fromkeys((nasal_norm(form), alt_n)) if v != form)


def nasal_norm(form: str) -> str:
    """Canonical spelling with anusvara for every nasal+homorganic stop cluster."""
    chars = list(form)
    return "".join(
        "M" if c in "NYRnm" and i + 1 < len(chars) and _NASAL_BY_CLASS.get(chars[i + 1]) == c else c
        for i, c in enumerate(chars)
    )


def final_variants(form: str) -> tuple[str, ...]:
    """Pausal-spelling variants of a pada: final visarga -> s, final anusvara -> m."""
    if form.endswith("H"):
        return (form[:-1] + "s", form[:-1] + "r")
    if form.endswith("M"):
        return (form[:-1] + "m",)
    return ()


# --------------------------------------------------------------------------- derivation


def derive_texts(arg: Any) -> tuple[str, ...]:
    try:
        return tuple(p.text for p in resources.vyakarana().derive(arg))
    except Exception:  # vidyut raises on unsupported combinations
        return ()


def is_krdanta_entry(entry) -> bool:
    return type(entry).__name__.endswith("Subanta") and type(entry.pratipadika_entry).__name__.endswith("Krdanta")


def is_tinanta_entry(entry) -> bool:
    return type(entry).__name__.endswith("Tinanta")


def prefixed_pada(entry, extra: tuple[str, ...]) -> Optional[Any]:
    """The vidyut Pada for ``entry`` with upasargas ``extra`` prepended to its dhatu."""
    from vidyut.prakriya import Pada, Pratipadika

    if is_tinanta_entry(entry):
        dhatu = entry.dhatu_entry.dhatu
        new = dhatu.with_prefixes(list(extra) + list(dhatu.prefixes or ()))
        return Pada.Tinanta(dhatu=new, prayoga=entry.prayoga, lakara=entry.lakara,
                            purusha=entry.purusha, vacana=entry.vacana)
    if not is_krdanta_entry(entry):
        return None
    prati = entry.pratipadika_entry
    if str(prati.krt) == "kvi~p":
        return None
    dhatu = prati.dhatu_entry.dhatu
    new = dhatu.with_prefixes(list(extra) + list(dhatu.prefixes or ()))
    krt = prati.krt
    if str(krt) in AVYAYA_KRTS or entry.is_avyaya:
        return Pada.make_avyaya(Pratipadika.krdanta(new, krt))
    return Pada.Subanta(pratipadika=Pratipadika.krdanta(new, krt), linga=entry.linga,
                        vibhakti=entry.vibhakti, vacana=entry.vacana)


def lyap_pada(dhatu, extra: tuple[str, ...]) -> Any:
    from vidyut.prakriya import Krt, Pada, Pratipadika

    new = dhatu.with_prefixes(list(extra) + list(dhatu.prefixes or ()))
    return Pada.make_avyaya(Pratipadika.krdanta(new, Krt.ktvA))


# --------------------------------------------------------------------------- nominals

# (form ending, stem ending, lingas) for out-of-kosha nominal stems.
NOMINAL_ENDINGS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    ("asya", "a", ("Pum", "Napumsaka")), ("ena", "a", ("Pum", "Napumsaka")),
    ("Aya", "a", ("Pum", "Napumsaka")), ("At", "a", ("Pum", "Napumsaka")),
    ("as", "a", ("Pum",)), ("am", "a", ("Pum", "Napumsaka")), ("e", "a", ("Pum", "Napumsaka")),
    ("O", "a", ("Pum",)), ("An", "a", ("Pum",)), ("As", "a", ("Pum",)), ("Ani", "a", ("Napumsaka",)),
    ("EH", "a", ("Pum",)), ("Es", "a", ("Pum",)), ("Ayam", "A", ("Stri",)), ("Ayas", "A", ("Stri",)),
    ("A", "A", ("Stri",)), ("Am", "A", ("Stri",)), ("is", "i", ("Pum", "Stri")),
    ("im", "i", ("Pum", "Stri")), ("es", "i", ("Pum", "Stri")), ("inA", "i", ("Pum",)),
    ("us", "u", ("Pum", "Stri")), ("um", "u", ("Pum", "Stri")), ("os", "u", ("Pum", "Stri")),
    ("I", "I", ("Stri",)), ("Im", "I", ("Stri",)), ("yAs", "I", ("Stri",)), ("yAm", "I", ("Stri",)),
    ("U", "U", ("Stri", "Pum")), ("A", "f", ("Pum", "Stri")), ("aram", "f", ("Pum",)),
    ("Aram", "f", ("Pum",)), ("A", "an", ("Pum",)), ("Anam", "an", ("Pum",)),
    ("I", "in", ("Pum",)), ("inam", "in", ("Pum",)), ("An", "at", ("Pum",)),
    ("antam", "at", ("Pum",)), ("Antam", "at", ("Pum",)),
)
MAX_NOMINAL_CANDIDATES = 6


def nominal_candidates(form: str) -> list[tuple[str, str]]:
    """(stem, linga-name) pairs whose paradigm might contain ``form``; capped."""
    out: dict[tuple[str, str], None] = {}
    for ending, stem_end, lingas in NOMINAL_ENDINGS:
        if form.endswith(ending) and len(form) - len(ending) >= 2:
            stem = form[: len(form) - len(ending)] + stem_end
            for linga in lingas:
                out.setdefault((stem, linga))
    return list(out)[:MAX_NOMINAL_CANDIDATES]


@lru_cache(maxsize=20_000)
def generated_subantas(form: str) -> tuple[Any, ...]:
    """vidyut Pada.Subanta args (for stems absent from the kosha) deriving exactly ``form``."""
    from vidyut.prakriya import Linga, Pada, Pratipadika, Vacana, Vibhakti

    found = []
    for stem, linga_name in nominal_candidates(form):
        prati = Pratipadika.basic(stem)
        linga = getattr(Linga, linga_name)
        for vib in Vibhakti.choices():
            for vac in Vacana.choices():
                pada = Pada.Subanta(pratipadika=prati, linga=linga, vibhakti=vib, vacana=vac)
                if form in derive_texts(pada):
                    found.append((stem, linga, vib, vac, pada))
    return tuple(found)


# --------------------------------------------------------------------------- stems

# Indeclinable / special compound first members: stem -> (lemma, rule note).
SPECIAL_STEMS: dict[str, tuple[str, str]] = {
    "a": ("naY", "naY-tatpurusha, n-lopa 6.3.73"),
    "an": ("naY", "naY-tatpurusha before vowel, 6.3.74 (nuw)"),
    "su": ("su", "indeclinable first member (2.2.18 kugatiprAdayaH)"),
    "dus": ("dus", "indeclinable first member (2.2.18)"),
    "dur": ("dus", "indeclinable first member (2.2.18)"),
    "duH": ("dus", "indeclinable first member (2.2.18)"),
    "sa": ("saha", "saha -> sa in bahuvrihi, 6.3.82"),
    "mahA": ("mahat", "mahat -> mahA before uttarapada, 6.3.46"),
    "ku": ("ku", "indeclinable first member (2.2.18)"),
    "mad": ("asmad", "asmad -> mad before uttarapada, 7.2.98"),
    "mat": ("asmad", "asmad -> mad before uttarapada, 7.2.98"),
    "tvad": ("yuzmad", "yuzmad -> tvad before uttarapada, 7.2.98"),
    "tvat": ("yuzmad", "yuzmad -> tvad before uttarapada, 7.2.98"),
}


def stem_probe_forms(form: str) -> tuple[str, ...]:
    """Kosha padas that a stem spelled ``form`` (as a compound member) would produce."""
    probes = [form, form + "s", form + "m"]
    last = form[-1:]
    if last == "a":
        probes.append(form[:-1] + "A")  # rAja -> rAjA (an-stem), Atma -> AtmA
    elif last == "i":
        probes.append(form[:-1] + "I")  # tapasvi -> tapasvI (in-stem)
    elif last == "A":
        probes += [form + "n", form + "s"]  # mahA -> mahAn
    elif last == "f":
        probes.append(form[:-1] + "A")
    elif last in ("k", "g"):
        probes.append(form)  # vAk
    elif last in ("d", "t"):
        probes += [form[:-1] + "t", form[:-1] + "d"]
    return tuple(dict.fromkeys(probes))


def member_forms(stem: str) -> tuple[str, ...]:
    """Spellings of pratipadika ``stem`` as a non-final compound member.

    Pada-hood before the uttarapada (1.4.17 svAdizv asarvanAmasTAne) brings
    n-lopa (8.2.7: rAjan -> rAja, guRin -> guRi), kutva of c/j (8.2.30: vAc -> vAk)
    and jaztva (8.2.39: tad -> tat/tad).
    """
    out = [stem]
    if stem.endswith("an") or stem.endswith("in"):
        out.append(stem[:-1])
    elif stem.endswith("c") or stem.endswith("j"):
        out += [stem[:-1] + "k", stem[:-1] + "g"]
    elif stem.endswith("d"):
        out.append(stem[:-1] + "t")
    elif stem.endswith("t"):
        out.append(stem[:-1] + "d")
    return tuple(out)


@dataclass(frozen=True)
class StemHandle:
    """What ``prove`` needs to justify a compound-member stem."""

    method: str  # "krdanta" | "kosha-pratipadika" | "special"
    stem: str  # pratipadika text
    member_form: str  # spelling inside the compound
    pratipadika: Any = None  # vidyut Pratipadika for krdantas
    note: str = ""


_KRDANTA_STEMS: dict[str, str] = {}


def krdanta_stem_text(dhatu, krt) -> str:
    """Stem text of the krdanta dhatu+krt, by forward derivation (cached)."""
    from vidyut.prakriya import Pratipadika

    key = f"{dhatu!r}|{krt}"
    if key not in _KRDANTA_STEMS:
        texts = derive_texts(Pratipadika.krdanta(dhatu, krt))
        _KRDANTA_STEMS[key] = texts[0] if texts else ""
    return _KRDANTA_STEMS[key]
