"""Corpus-structure features of the analysis tagger: lemma gender priors and noun concord, verb valency
and clause type, verse-wide verb–subject fit. ``v`` is a :class:`mayur.tagger_features.Verse`; the
tables (``v.tab``) are built from TRAIN gold by ``scripts/train_tagger.py`` and saved in the model.
"""

from __future__ import annotations

from typing import Optional

from mayur.model import Morph

WINDOW = 4
Obs = list[str]


def _f():
    from mayur import tagger_features
    return tagger_features


def gender_prior(v, m: Morph) -> Optional[dict]:
    key = _f()._lkey(m)
    return v.tab.get("g", {}).get(key) or v.tab.get("gs", {}).get("".join(_f()._sounds(key)[-2:]))

def structural(v, i: int, m: Morph) -> Obs:
    """Corpus-learned structure: lemma gender priors, noun concord, verb valency, clause type."""
    if m.kind != "subanta":
        return []
    o: Obs = []
    gp = gender_prior(v, m)
    if gp and m.linga:
        o += ["gp=%d" % int(4 * gp.get(m.linga, 0.0)), "gpTop=%d" % (max(gp, key=gp.get) == m.linga)]
    n, line = len(v.forms), v.lines[i]
    refs = {j: v.cands[j][v.ref[j]] for j in range(n) if j != i and not v.cpd[j] and v.cands[j]}
    if _f()._lemma_class(m.lemma) != "noun":
        for side, rng in (("L", range(i - 1, max(-1, i - WINDOW - 1), -1)), ("R", range(i + 1, min(n, i + WINDOW + 1)))):
            for j in rng:
                if v.lines[j] != line or j not in refs:
                    continue
                nouns = [x for x in v.cands[j] if _f()._lemma_class(x.lemma) == "noun" and x.kind == "subanta"
                         and (x.vibhakti, x.vacana) == (m.vibhakti, m.vacana)]
                pr = gender_prior(v, nouns[0]) if nouns else None
                if pr:
                    o.append("nG%s=%d" % (side, max(pr, key=pr.get) == m.linga))
                    break
    verbs = [x for x in refs.values() if x.kind == "tinanta"]
    nonfin = [x for x in refs.values() if _f()._verbal(x) in ("abs", "inf")]
    acc, dat = v.tab.get("acc", {}), v.tab.get("dat", {})
    if m.vibhakti in ("प्रथमा", "द्वितीया"):
        ps = [acc[_f()._lkey(x)] for x in verbs + nonfin if _f()._lkey(x) in acc]
        o.append("vacc=%s" % (int(4 * max(ps)) if ps else "-"))
        if not verbs and not nonfin:
            o.append("noVerb")
        for j, x in refs.items():
            if x.krt in ("क्त", "क्तवतु") or _f()._verbal(x) == "part" and x.krt in ("तव्य", "अनीयर्", "यत्", "ण्यत्"):
                if _f()._agree(m, x):
                    o.append("ktaAg")
            if abs(j - i) == 1 and (_f()._verbal(x) in ("abs", "inf") or x.krt in ("शतृ", "शानच्")):
                o.append("gov%+d" % (j - i))
        if verbs and m.lemma not in ("अस्मद्", "युष्मद्") and all(x.purusha not in (None, "प्रथमपुरुष") for x in verbs):
            o.append("onlyV12")  # जानामि अहम् सर्वम्: a 1st/2nd-person verb has no 3rd-person subject
        kartas = [x for x in refs.values() if any(_f()._fits(x, y) for y in verbs)]
        if kartas:
            o.append("otherKarta=%d" % any(_f()._agree(m, x) for x in kartas))
        prv = refs.get(i - 1)
        if prv is not None and prv.kind == "tinanta":
            o.append("postV=" + (prv.prayoga or ""))
        nxt = refs.get(i + 1)
        if nxt is not None and nxt.kind == "tinanta" and any(_f()._fits(x, nxt) for j, x in refs.items() if j < i):
            o.append("preVnom")
    if m.vibhakti in ("चतुर्थी", "षष्ठी", "पञ्चमी"):
        ps = [dat[_f()._lkey(x)] for x in verbs if _f()._lkey(x) in dat]
        o.append("vdat=%s" % (int(4 * max(ps)) if ps else "-"))
    if m.vibhakti in ("सम्बोधन", "प्रथमा"):
        o.append("v2p=%d" % any(x.purusha == "मध्यमपुरुष" for x in verbs))
        o.append("voc2=%d" % any(x.vibhakti == "सम्बोधन" for x in refs.values()))
    if m.krt == "तृच्" and any(refs.get(j) is not None and refs[j].vibhakti == "षष्ठी" for j in (i - 1, i + 1)):
        o.append("trcGen")
    if m.krt and m.linga == "स्त्रीलिङ्ग":
        fem = any(x.linga == "स्त्रीलिङ्ग" and x.vibhakti == m.vibhakti and not x.krt and v.lines[j] == line
                  for j, x in refs.items())
        o.append("femPN=%d" % fem)
    return o


def verse_level(v, i: int, m: Morph) -> Obs:
    """Verb–subject and object features across the whole verse (half-verse boundaries are arbitrary)."""
    if m.kind not in ("subanta", "tinanta"):
        return []
    refs = [(j, v.cands[j][v.ref[j]]) for j in range(len(v.forms))
            if j != i and not v.cpd[j] and v.cands[j]]
    verbs = [x for _, x in refs if x.kind == "tinanta"]
    o = ["Vverbs=%d" % min(len(verbs), 2)]
    if m.vibhakti == "प्रथमा":
        o.append("Vfit" if any(_f()._fits(m, v) for v in verbs) else "Vnofit")
        o += ["Vpr=" + (v.prayoga or "") for v in verbs[:2]]
        if any(_f()._agree(m, x) for _, x in refs):
            o.append("VagNom")
    if m.kind == "subanta" and m.vibhakti in ("प्रथमा", "द्वितीया"):
        o += ["Vlm=" + v.lemma for v in verbs[:2]]
        other_nom = [x for j, x in refs if all(c.vibhakti == "प्रथमा" for c in v.cands[j])
                     and any(_f()._fits(x, v) for v in verbs)]
        if other_nom:
            o.append("VsureNom")
    if m.kind == "tinanta":
        o.append("Vkarta" if any(_f()._fits(x, m) for _, x in refs) else "Vnokarta")
    # रामो लक्ष्मणश्च वनं गच्छतः: two singular nominatives joined by च agree with a dual (1.2.64, 2.2.29)
    sg_noms = sum(1 for _, x in refs if x.vibhakti == "प्रथमा" and x.vacana == "एकवचन")
    if sg_noms >= 2 and "च" in v.forms:
        o.append("coord2=" + (m.vacana or "") + ("V" if m.kind == "tinanta" else ""))
    if v.p2 and m.kind == "subanta":
        o += ["Pag%+d" % max(-6, min(6, j - i)) for j, x in refs if _f()._agree(m, x)]
    return o
