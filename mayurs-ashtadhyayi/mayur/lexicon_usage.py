"""Forms that usage has and the rules, as vidyut applies them, do not give: analysed and LABELLED.

Each analysis here names the root, the upasargas and the suffix, and says in its note what the
rules give instead. None of them is a proof: the word stays unverified, with the reason.

* upasarga + past participle where vidyut derives another form with that upasarga:
  प्रदत्त (rule form प्रत्त, 7.4.47 अच उपसर्गात्तः), अवनामित (rule form अवनमित), निषूदित (rule form निसूदित);
* participles the kosha lists only as adjectives: छन्न, स्पष्ट (7.2.27), क्षुब्ध (7.2.18), चीर्ण, गुह्य;
* अपि without its अ before नह्, धा (पिनद्ध, पिधाय, पिहित): Bhāguri's rule, not in the Aṣṭādhyāyī;
* क्त्वा kept after an upasarga, where 7.1.37 gives ल्यप्: परिपालयित्वा (epic).

All strings Devanagari.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Callable, Iterator, Sequence

from mayur import bridge, lipi
from mayur.model import Morph

Lookup = Callable[[str], Sequence[Morph]]

ARSHA = "arsha"
KTA = ("क्त", "क्तवतु")
PREFIX_NOTE = ("{prefix} + {participle} ({root} + {krt}); with this upasarga vidyut derives {derived}, so the form "
               "is labelled as usage, not proved")
KTVA_NOTE = ("ārṣa: {prefix} + {absolutive} with क्त्वा kept after an upasarga, where 7.1.37 समासेऽनञ्पूर्वे क्त्वो ल्यप् "
             "gives ल्यप्; epic usage, labelled and not derived")
BHAGURI_NOTE = ("अपि without its अ (वष्टि भागुरिरल्लोपमवाप्योरुपसर्गयोः, a rule of Bhāguri, not of the Aṣṭādhyāyī); the "
                "form with अपि is {full}; labelled, not derived")
# stem the kosha lists as an adjective -> (presents of its root, to take the root from the kosha; kṛt; why)
IRREGULAR_KRT = {
    "छन्न": (("छादयति",), "क्त", "छन्न is taught ready-made by 7.2.27 वा दान्तशान्तपूर्णदस्तस्पष्टच्छन्नज्ञप्ताः (छद् + णिच् + क्त)"),
    "स्पष्ट": (("स्पाशयति", "स्पशते"), "क्त", "स्पष्ट is taught ready-made by 7.2.27 (स्पश् + णिच् + क्त)"),
    "ज्ञप्त": (("ज्ञपयति",), "क्त", "ज्ञप्त is taught ready-made by 7.2.27 (ज्ञप् + णिच् + क्त)"),
    "क्षुब्ध": (("क्षुभ्यति", "क्षोभते"), "क्त", "क्षुब्ध is taught ready-made by 7.2.18 क्षुब्धस्वान्तध्वान्तलग्नम्लिष्टविरिब्धफाण्टबाढानि"),
    "चीर्ण": (("चरति",), "क्त", "चीर्ण stands in usage beside the rule form चरित (चर् + क्त)"),
    "गुह्य": (("गूहति",), "क्यप्", "गुह्य by the vārttika शंसिदुहिगुहिभ्यो वा on 3.1.109 (गुह् + क्यप्); the sūtra form is गोह्य"),
}
IRREGULAR_NOTE = "{why}; vidyut does not derive this stem, so the form is labelled, not proved"


def prefix_splits(form: str, gati: bool = False) -> Iterator[tuple[tuple[str, ...], str]]:
    """(upasargas, remainder) for one or two real upasargas before ``form``'s remainder; with
    ``gati`` also one of सत्, अलम्, नमस् (which join कृ only: the caller checks the root)."""
    from mayur.lexicon_gen import _GATI_WITH_KR, _splits

    for u1, rest in _splits(form):
        if u1 in _GATI_WITH_KR:
            if gati:
                yield (u1,), rest
            continue
        yield (u1,), rest
        for u2, rest2 in _splits(rest):
            if u2 not in _GATI_WITH_KR:
                yield (u1, u2), rest2


_PLAIN = str.maketrans("षटठण", "सतथन")


def _joins(prefixes: Sequence[str], rest: str, form: str) -> bool:
    """The upasargas and ``rest`` give ``form`` by plain sandhi, or with the ष / ण an upasarga in
    इ, उ causes (8.3.65 ff., 8.4.14): नि + सूदित = निषूदित. निस् + सूदित does not."""
    from mayur import sandhi

    joined = {t for flags in [[True] * len(prefixes)] for t in sandhi.rejoin([*prefixes, rest], flags)}
    wanted = {form, lipi.pausa(form)}
    if joined & wanted:
        return True
    return prefixes[-1][-1:] in ("ि", "ु") and bool({t.translate(_PLAIN) for t in joined} & {w.translate(_PLAIN) for w in wanted})


def prefixed_participle(form: str, found: Sequence[Morph]) -> tuple[Morph, ...]:
    """अवनामितैस्: अव + नामितैस्, a participle of नम् + णिच् that the kosha lists."""
    if any(m.root and m.krt in KTA for m in found):
        return ()
    out: list[Morph] = []
    for prefixes, rest in prefix_splits(form):
        if not _joins(prefixes, rest, form):
            continue
        for entry in bridge.lookup(rest):
            m = entry.morph
            if entry.entry != "krdanta" or m.krt not in KTA:
                continue
            pada = bridge.prefixed_krdanta(entry, prefixes)
            derived = bridge.derived_texts(pada) if pada is not None else ()
            if form in derived:
                continue  # derivable: the forward generator has it
            note = PREFIX_NOTE.format(prefix=" + ".join(prefixes), participle=lipi.pausa(rest), root=m.root or m.lemma,
                                      krt=m.krt, derived=", ".join(lipi.pausa(t) for t in derived) or "nothing")
            every = prefixes + tuple(m.prefixes)
            out.append(replace(m, form=form, lemma="".join(every) + (m.root or m.lemma), prefixes=every,
                               source="generated", quality=2, handle=("special", note)))
    return tuple(dict.fromkeys(out))


def _root_of(present: str) -> Morph | None:
    return next((e.morph for e in bridge.lookup(present) if e.entry == "tinanta"), None)


def irregular_participle(form: str, found: Sequence[Morph]) -> tuple[Morph, ...]:
    """छन्नस्, आच्छन्नम्, चीर्णम्: a listed adjective that is the participle of a known root."""
    out: list[Morph] = []
    for m in found:
        stem = m.stem or m.lemma
        if m.kind != "subanta" or m.krt or m.source != "kosha":
            continue
        options = [((), stem), *prefix_splits(stem)]
        for prefixes, rest in options:
            if rest not in IRREGULAR_KRT:
                continue
            presents, krt, why = IRREGULAR_KRT[rest]
            root = next((r for r in map(_root_of, presents) if r is not None), None)
            if root is None:
                continue
            out.append(replace(m, lemma="".join(prefixes) + (root.root or root.lemma), stem=stem, root=root.root,
                               dhatu=root.dhatu, gana=root.gana, prefixes=prefixes, krt=krt,
                               root_gloss=root.root_gloss, source="generated", quality=2,
                               handle=("special", IRREGULAR_NOTE.format(why=why))))
    return tuple(dict.fromkeys(out))


def bhaguri(form: str, padas: Lookup) -> tuple[Morph, ...]:
    """पिनद्धस्, पिधाय: the same word with अपि is in the lexicon."""
    if not form.startswith("पि") or len(form) < 5:
        return ()
    full = "अ" + form
    note = BHAGURI_NOTE.format(full=lipi.pausa(full))
    return tuple(dict.fromkeys(
        replace(m, form=form, source="generated", quality=2, handle=("special", note))
        for m in padas(full) if m.root and m.prefixes[:1] == ("अपि",)))


def prefixed_ktva(form: str) -> tuple[Morph, ...]:
    """परिपालयित्वा: an upasarga before a क्त्वा absolutive the kosha lists."""
    if not form.endswith("त्वा"):
        return ()
    out: list[Morph] = []
    from mayur.lexicon_gen import _GATI_WITH_KR

    for prefixes, rest in prefix_splits(form, gati=True):
        for entry in bridge.lookup(rest):
            m = entry.morph
            if prefixes[0] in _GATI_WITH_KR and m.root != "कृ":  # नमस्कृत्वा, never नमस् + गत्वा
                continue
            if entry.entry == "krdanta" and m.krt == "क्त्वा":
                note = KTVA_NOTE.format(prefix=" + ".join(prefixes), absolutive=rest)
                every = prefixes + tuple(m.prefixes)
                out.append(replace(m, form=form, lemma="".join(every) + (m.root or m.lemma), prefixes=every,
                                   source=ARSHA, quality=1, handle=("special", note)))
    return tuple(dict.fromkeys(out))


def _distinct(morphs: Sequence[Morph]) -> tuple[Morph, ...]:
    """One analysis per lemma and grammatical value (the kosha lists a participle under several entries)."""
    seen: dict[tuple, Morph] = {}
    for m in morphs:
        seen.setdefault((m.lemma, m.krt, m.linga, m.vibhakti, m.vacana, m.lakara, m.purusha), m)
    return tuple(seen.values())


def usage_forms(form: str, found: Sequence[Morph], padas: Lookup) -> tuple[Morph, ...]:
    """Every labelled usage analysis of ``form`` given what the lexicon already ``found``."""
    out = [*irregular_participle(form, found)]
    if not any(m.root for m in found):
        out += usage_root_forms(form)
    if not any(m.root and m.krt in KTA for m in [*found, *out]):
        out += prefixed_participle(form, found)
    if not any(m.root for m in found):
        out += bhaguri(form, padas)
    if not any(m.kind == "avyaya" and m.krt in ("ल्यप्", "क्त्वा") for m in found):
        out += prefixed_ktva(form)
    return _distinct(out)


# Roots of usage that the Dhātupāṭha does not teach: name -> (vidyut code of the root as if taught, why)
USAGE_ROOTS = {
    "वध्": ("vaDa~", "the root वध् is not in the Dhātupāṭha: 2.4.42 हनो वध लिङि and 2.4.43 लुङि च teach वध only as a "
                    "substitute of हन्; usage has वध्यते, वधिष्यति. Derived by vidyut as if वध were a root of the "
                    "first class; labelled, not proved"),
}


def _usage_root_table() -> dict[str, tuple[Morph, ...]]:
    """form -> analyses for the finite forms and the passive participle of each usage root."""
    global _TABLE
    if _TABLE is not None:
        return _TABLE
    from vidyut.prakriya import Dhatu, Gana, Lakara, Pada, Prayoga, Purusha, Vacana

    table: dict[str, list[Morph]] = {}
    lakaras = (Lakara.Lat, Lakara.Lot, Lakara.Lan, Lakara.VidhiLin, Lakara.Lrt, Lakara.Lun, Lakara.Lit)
    for root, (code, why) in USAGE_ROOTS.items():
        try:
            dhatu = Dhatu.mula(code, Gana.Bhvadi)
        except Exception:  # noqa: BLE001 - vidyut rejects the code
            continue
        for prayoga, name in ((Prayoga.Kartari, "कर्तरि"), (Prayoga.Karmani, "कर्मणि")):
            for lak in lakaras:
                for pur in Purusha.choices():
                    for vac in Vacana.choices():
                        pada = Pada.Tinanta(dhatu=dhatu, prayoga=prayoga, lakara=lak, purusha=pur, vacana=vac)
                        m = Morph(form="", lemma=root, kind="tinanta", purusha=bridge._term(bridge._PURUSHA, pur),
                                  vacana=bridge._term(bridge._VACANA, vac), lakara=bridge._term(bridge._LAKARA, lak),
                                  prayoga=name, root=root, dhatu=root, gana="—", source=ARSHA, quality=1,
                                  handle=("special", why))
                        for text in bridge.derived_texts(pada):
                            table.setdefault(text, []).append(replace(m, form=text))
        passive = root[:-1] + "्यमान"  # वध्यमान: the passive aṅga + शानच् (3.2.124, 7.2.82)
        for linga in ("पुंलिङ्ग", "नपुंसकलिङ्ग", "स्त्रीलिङ्ग"):
            nyap = linga == "स्त्रीलिङ्ग"
            for pada, template in bridge.subanta_paradigm(passive + "ा" if nyap else passive, linga, nyap=nyap):
                for text in bridge.derived_texts(pada):
                    table.setdefault(text, []).append(replace(
                        template, form=text, lemma=root, stem=passive, root=root, dhatu=root, krt="शानच्",
                        source=ARSHA, quality=1, handle=("special", why)))
    _TABLE = {k: tuple(dict.fromkeys(v)) for k, v in table.items()}
    return _TABLE


_TABLE: dict[str, tuple[Morph, ...]] | None = None


def usage_root_forms(form: str) -> tuple[Morph, ...]:
    """वध्यते, वधिष्यामि, वध्यमानस्: forms of a root of usage (see USAGE_ROOTS)."""
    if not any(form.startswith(root[:-1]) or form.startswith("अ" + root[:-1]) for root in USAGE_ROOTS):
        return ()
    return _usage_root_table().get(form, ())
