"""Proof of a passive present participle (क्रियमाण, उच्यमान) in two forward steps.

vidyut's Python API derives a kṛdanta stem in कर्तरि only, so for क्रियमाणः it gives कुर्वाणः and the
kosha's own entry cannot be re-derived in one call. The two halves can:

  1. क्रियते, the कर्मणि लट् form of the same root, derived by vidyut: its trace shows the aṅga क्रिय
     (यक्, 3.1.67) to which the ending is added;
  2. in place of that ending stands शानच् (3.2.124 लटः शतृशानचौ; आत्मनेपद by 1.4.100), with मुक् after
     the अ of the aṅga (7.2.82 आने मुक्): क्रिय + म् + आन = क्रियमाण (ण by 8.4.2);
  3. the stem क्रियमाण, inflected by vidyut.

Steps 1 and 3 are run by vidyut; step 2 is two rules stated here, and it is checked: the stem must
be exactly the passive form without ते, plus मान / माण. All strings Devanagari.
"""

from __future__ import annotations

from typing import Optional

from mayur import bridge
from mayur.model import Morph, SutraStep, WordProof

SOURCE = "अष्टाध्यायी"
METHOD = "vidyut-prakriya in two steps (कर्मणि लट्; शानच् by 3.2.124, 7.2.82; inflection)"


def _passive_present(stem: str, root: Optional[str]) -> Optional[bridge.Entry]:
    """The kosha's कर्मणि लट् third singular whose aṅga the participle stem is built on."""
    if not stem.endswith(("मान", "माण")):
        return None
    finite = stem[: -len("मान")] + "ते"
    return next((e for e in bridge.lookup(finite)
                 if e.entry == "tinanta" and e.morph.lakara == "लट्" and e.morph.prayoga in ("कर्मणि", "भावे")
                 and e.morph.purusha == "प्रथमपुरुष" and e.morph.vacana == "एकवचन" and e.morph.root == root), None)


def prove(m: Morph) -> Optional[WordProof]:
    """The two-step proof of ``m``, or None when ``m`` is not a passive participle this covers."""
    if m.krt != "शानच्" or m.kind != "subanta" or not m.stem or not m.linga:
        return None
    present = _passive_present(m.stem, m.root)
    if present is None:
        return None
    first = bridge.derive(present.morph.handle)
    first = [d for d in first if d.text == present.morph.form]
    nyap = m.linga == "स्त्रीलिङ्ग"
    cells = bridge.subanta_paradigm(m.stem + "ा" if nyap else m.stem, m.linga, nyap=nyap)
    for pada, template in cells:
        if (template.vibhakti, template.vacana) != (m.vibhakti, m.vacana):
            continue
        second = [d for d in bridge.derive(pada) if d.text == m.form]
        if first and second:
            anga = m.stem[: -len("मान")]
            middle = [SutraStep(SOURCE, "3.2.124", f"{anga} + शानच्"), SutraStep(SOURCE, "7.2.82", f"{anga} + म् + आन"),
                      SutraStep(SOURCE, "1.2.46", m.stem)]
            return WordProof(derivable=True, method=METHOD, derived_form=m.form,
                             trace=[*first[0].trace, *middle, *second[0].trace],
                             note=f"the aṅga is that of {present.morph.form} (derived by vidyut); the stem {m.stem} "
                                  f"is then inflected by vidyut")
    return None
