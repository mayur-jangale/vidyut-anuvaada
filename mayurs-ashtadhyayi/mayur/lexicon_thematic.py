"""Epic forms of second-class roots conjugated in the first class: हनति, अहनत्, अशासत्, अन्वशासत्.

The Aṣṭādhyāyī gives the roots of the अदादि class no vikaraṇa (2.4.72 अदिप्रभृतिभ्यः शपः: शप् is elided),
so the rule forms are हन्ति, अहन्, शास्ति, अशात्. Epic Sanskrit often keeps the अ of शप्, as in the first
class. Such a form is found here by FORWARD generation: every root the Dhātupāṭha lists in the
second class is derived by vidyut as if it stood in the first (present, imperfect, imperative,
optative), and a text form that equals one of these and is not a rule form is LABELLED ārṣa with
its rule form. It is an analysis, not a proof: the word stays unverified.

The table (about 2,700 derivations) is built on first use and kept in data/derived/.
All strings Devanagari.
"""

from __future__ import annotations

import json
from dataclasses import replace
from functools import lru_cache
from typing import Optional

from mayur import bridge, lipi, resources
from mayur.model import Morph

ARSHA = "arsha"
NOTE = ("ārṣa: {root}, a root of the second class (2.4.72 elides शप्), conjugated here with the अ of the first class; "
        "the rule form is {regular}. Epic usage, labelled and not derived")
TABLE = "thematic_forms.json"
_VERB_FINALS = ("ि", "त्", "न्", "म्", "स्", "ु", "े", "थ", "त", "व", "म")


def _build() -> dict[str, list[list[str]]]:
    """form -> [[rule form of the same cell, lakāra, puruṣa, vacana, rule third singular present], ...]."""
    from vidyut.prakriya import Data, Dhatu, Gana, Lakara, Pada, Prayoga, Purusha, Vacana

    table: dict[str, list[list[str]]] = {}
    entries = Data(str(resources.vidyut_dir() / "prakriya")).load_dhatu_entries()
    for entry in entries:
        if entry.dhatu.gana != Gana.Adadi:
            continue
        try:
            first = Dhatu.mula(entry.dhatu.aupadeshika, Gana.Bhvadi)
        except Exception:  # noqa: BLE001 - vidyut rejects the re-classed root
            continue

        def cell(dhatu, lak, pur, vac):
            return bridge.derived_texts(Pada.Tinanta(dhatu=dhatu, prayoga=Prayoga.Kartari, lakara=lak, purusha=pur,
                                                     vacana=vac))

        present = cell(entry.dhatu, Lakara.Lat, Purusha.Prathama, Vacana.Eka)
        if not present:
            continue
        for lak in (Lakara.Lat, Lakara.Lan, Lakara.Lot, Lakara.VidhiLin):
            for pur in Purusha.choices():
                for vac in Vacana.choices():
                    rule = cell(entry.dhatu, lak, pur, vac)
                    for text in cell(first, lak, pur, vac):
                        if text not in rule:
                            table.setdefault(text, []).append([
                                rule[0] if rule else "", bridge._term(bridge._LAKARA, lak) or "",
                                bridge._term(bridge._PURUSHA, pur) or "", bridge._term(bridge._VACANA, vac) or "",
                                present[0]])
    return table


@lru_cache(maxsize=1)
def _table() -> dict[str, list[list[str]]]:
    path = resources.derived_dir() / TABLE
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        table = _build()
        try:
            path.write_text(json.dumps(table, ensure_ascii=False, sort_keys=True), encoding="utf-8")
        except OSError:  # a read-only data directory: build again next time
            pass
        return table


def _root(present: str) -> Optional[Morph]:
    return next((e.morph for e in bridge.lookup(present) if e.entry == "tinanta" and e.morph.gana == "अदादि"),
                next((e.morph for e in bridge.lookup(present) if e.entry == "tinanta"), None))


def thematic(form: str) -> tuple[Morph, ...]:
    """The first-class readings of ``form`` for a second-class root; () for a form no such root gives."""
    if not form.endswith(_VERB_FINALS) or len(form) < 3:
        return ()
    out: list[Morph] = []
    for regular, lakara, purusha, vacana, present in _table().get(form, ()):
        root = _root(present)
        if root is None:
            continue
        note = NOTE.format(root=root.root or root.lemma, regular=lipi.pausa(regular) if regular else "another form")
        out.append(replace(root, form=form, lakara=lakara, purusha=purusha, vacana=vacana, prayoga="कर्तरि",
                           source=ARSHA, quality=1, handle=("special", note)))
    return tuple(dict.fromkeys(out))
