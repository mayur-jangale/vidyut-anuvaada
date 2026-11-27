"""Which समास a compound is, decided by rule from what the sentence shows.

vidyut has no समास derivation, so the type is chosen here, in a fixed order of tests, each
naming the सूत्र it applies. The signals are read off the Morphs of the reading:
  * the member forms (स/सह, नञ्, प्रादि, indeclinables, numerals, सर्वादि pronouns);
  * the word class of the members: a कृत् participle (from the analysis), else the lexicon's
    genders (one or two genders: a noun; all three: an adjective), else the corpus tag class
    (``freq.lemma_class``, the most frequent DCS tag: "chosen by frequency");
  * agreement: another free word in the same case and number (and gender, when known);
  * gender shift: the compound is in a gender that the final member's stem does not have;
  * small tables keyed to the सूत्र that names the words (2.1.24, 2.1.31, 2.1.36, 2.1.37,
    2.1.40, 3.2.x upapada suffixes) and two lexical classes that are labelled as such
    (parts/qualities that a बहुव्रीहि typically possesses; relational nouns).
Every decision is a heuristic choice among the grammatically possible types and says so.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Optional, Sequence

from mayur.model import Morph, Reading, Word
from mayur.terms import PARTICIPLE_KRT
from mayur.samasa_tables import (AVYAYIBHAVA_FIRST, BV_HEADS, BV_HEADS_ALWAYS, INNER_DVANDVA_FINALS,  # noqa: F401
                                 NAN, NINI_FINALS, NUMERALS, PAIRED, PERSONAL, POSSESSED, PRADI, QUANTITY,
                                 RELATION, RELATIONAL, SAHA, SARVADI, UPAMANA_GUNA, UPAPADA_FINALS, UPAPADA_KRT)

TATPURUSHA = "तत्पुरुष"
KARMADHARAYA = "कर्मधारय"
DVANDVA = "द्वन्द्व"
BAHUVRIHI = "बहुव्रीहि"
NAN_TATPURUSHA = "नञ्-तत्पुरुष"
NAN_BAHUVRIHI = "नञ्-बहुव्रीहि"
UPAPADA = "उपपद-तत्पुरुष"
DVIGU = "द्विगु"
AVYAYIBHAVA = "अव्ययीभाव"
UNKNOWN = "अज्ञात"

M, F, N = "पुंलिङ्ग", "स्त्रीलिङ्ग", "नपुंसकलिङ्ग"
SG, DU, PL = "एकवचन", "द्विवचन", "बहुवचन"

@dataclass(frozen=True)
class Decision:
    samasa: str
    rule: str  # key into ``samasa.TYPE_RULE``
    relation: str = ""  # case of the first member in the vigraha (vibhakti-तत्पुरुष, upapada)
    note: str = ""  # why, citing the सूत्र
    inner: str = ""  # type of the non-final members when they form a compound of their own
    bracket: str = ""


def stem_of(word: Word) -> str:
    """The member's stem; a prefixed कृदन्त whose stem lacks its upasargas gets them back by
    running the sandhi forward (सम् + पन्न → सम्पन्न)."""
    m = word.morph
    if m is None:
        return word.form
    stem = m.stem or m.lemma
    if m.stem and m.prefixes and not stem.startswith(m.prefixes[0][:1]):
        return _prefixed(tuple(m.prefixes), stem)
    return stem


@lru_cache(maxsize=20_000)
def _prefixed(prefixes: tuple[str, ...], stem: str) -> str:
    from mayur import sandhi
    acc = stem
    for p in reversed(prefixes):
        outs = sandhi.outcomes(p, acc, samasa=True)
        acc = outs[0].text if outs else p + acc
    return acc


@lru_cache(maxsize=20_000)
def lexical_lingas(stem: str) -> frozenset[str]:
    """Genders the kosha lists for the basic stem (its nominative singulars looked up)."""
    from mayur import bridge
    out: set[str] = set()
    for g in (M, N, F):
        try:
            paradigm = bridge.subanta_paradigm(stem, g)
        except Exception:  # noqa: BLE001 - vidyut rejects the stem
            return frozenset()
        for h, m in paradigm:
            if (m.vibhakti, m.vacana) != ("प्रथमा", SG):
                continue
            for d in bridge.derive(h):
                for e in bridge.lookup(d.text):
                    if e.entry == "basic" and e.pratipadika == stem:
                        out |= set(e.lingas)
    return frozenset(out)


def _corpus_class(stem: str) -> str:
    try:
        from mayur import freq
        return freq.lemma_class(stem)
    except Exception:  # noqa: BLE001 - tables missing
        return ""


@lru_cache(maxsize=20_000)
def _stem_krts(stem: str) -> frozenset[str]:
    try:
        from mayur import lexicon
        return frozenset(m.krt for m in lexicon.stems(stem) if m.krt)
    except Exception:  # noqa: BLE001 - lexicon unavailable
        return frozenset()


@lru_cache(maxsize=50_000)
def dcs_grammar(stem: str) -> frozenset[str]:
    """Genders (पुंलिङ्ग ...) and "adj" that the DCS dictionary gives the stem's senses."""
    try:
        from mayur import resources
        senses = (resources.derived("dcs_dict.json") or {}).get(stem, [])
    except Exception:  # noqa: BLE001 - table missing
        return frozenset()
    out: set[str] = set()
    for sense in senses:
        g = str(sense.get("grammar", ""))
        if g.startswith("adj"):
            out.add("adj")
        elif set(g) <= set("mfn"):
            out |= {_LETTER[c] for c in g}
    return frozenset(out)


_LETTER = {"m": M, "f": F, "n": N}


def own_genders(stem: str) -> frozenset[str]:
    """Genders the stem has as a noun: the kosha's and the DCS dictionary's, together."""
    return lexical_lingas(stem) | (dcs_grammar(stem) - {"adj"})


def word_class(word: Word) -> tuple[str, str]:
    """(class, how it was found): numeral | sarvadi | personal | indeclinable | participle |
    adjective | noun | ""."""
    stem, m = stem_of(word), word.morph
    if stem in NUMERALS or word.form in ("एक", "द्वि", "त्रि", "चतुर्", "पञ्च", "षट्", "सप्त", "अष्ट", "नव", "दश"):
        return "numeral", "numeral stem"
    if stem in SARVADI:
        return "sarvadi", "सर्वादि (1.1.27)"
    if stem in PERSONAL:
        return "personal", "pronoun stem"
    if m is not None and m.kind == "avyaya":
        return "indeclinable", "analysis"
    corpus = _corpus_class(stem)
    krt = m.krt if m is not None and m.krt in PARTICIPLE_KRT else None
    if krt is None and word.in_compound and _stem_krts(stem) & {"क्त", "क्तवतु", "शतृ", "शानच्"}:
        krt = "क्त"
    if krt and not (word.in_compound and corpus == "noun"):
        return "participle", f"कृत् {krt}"
    if corpus in ("noun", "adjective"):
        return corpus, "corpus tag class (chosen by frequency)"
    dcs = dcs_grammar(stem)
    if dcs == {"adj"}:
        return "adjective", "DCS dictionary: adj"
    lingas = lexical_lingas(stem)
    if len(lingas) == 3:
        return "adjective", "kosha lists all three genders"
    if lingas or dcs:
        return "noun", "kosha/DCS genders"
    return "", "no class information"


def agreeing_word(reading: Reading, members: Sequence[int]) -> Optional[int]:
    """Index of a free word in the same case and number (and gender, when both have one)."""
    m = reading.words[members[-1]].morph
    if m is None or not m.vibhakti or not m.vacana:
        return None
    for j, other in enumerate(reading.words):
        om = other.morph
        if j in members or other.in_compound or om is None or om.kind != "subanta":
            continue
        if (om.vibhakti, om.vacana) == (m.vibhakti, m.vacana) and (not om.linga or not m.linga or om.linga == m.linga):
            return j
    return None


def _adjectival(stem: str) -> bool:
    """Used as an adjective: the corpus tags it so, or (unseen there) it has only adjective senses
    or all three genders in the kosha."""
    corpus = _corpus_class(stem)
    if corpus:
        return corpus == "adjective"
    return dcs_grammar(stem) == {"adj"} or len(lexical_lingas(stem)) == 3


def base_stem(stem: str) -> str:
    """The noun under a final member that took टाप् as a qualifier (लोचना → लोचन), else the stem."""
    if stem.endswith("ा") and own_genders(stem[:-1]) and F not in own_genders(stem[:-1]) \
            and F not in lexical_lingas(stem) and _corpus_class(stem) != "noun":
        return stem[:-1]
    return stem


def gender_shift(word: Word) -> str:
    """Why the final pada is in a gender its stem does not have ("" if it is not), with the rule
    that marks it: टाप् added to a non-feminine stem (4.1.4), ह्रस्व of a feminine (1.2.48)."""
    m = word.morph
    if m is None or not m.linga or m.krt:
        return ""
    stem = stem_of(word)
    base = base_stem(stem)
    if base != stem and m.linga == F and not _adjectival(base):
        return f"{base} ({'/'.join(sorted(own_genders(base)))}) takes टाप् (4.1.4) as a qualifier"
    own = own_genders(stem)
    if own and not _adjectival(stem):
        return "" if m.linga in own else f"the compound is {m.linga}, {stem} is {'/'.join(sorted(own))}"
    long = stem + "ा"
    if not own and own_genders(long) == {F} and m.linga != F:
        return f"{long} (स्त्रीलिङ्ग) shortened to {stem}: 1.2.48 गोस्त्रियोरुपसर्जनस्य"
    return ""


def _final_relation(stem: str) -> Optional[tuple[str, str]]:
    for key, rel in RELATION.items():
        if stem == key or (len(key) > 2 and stem.endswith(key)):
            return rel
    return None


def _upapada(final: Word, final_stem: str) -> Optional[tuple[str, str]]:
    """(the 3.2 rule, vigraha case) when the final is a bound कृत् agent."""
    if final_stem in UPAPADA_FINALS:
        return UPAPADA_FINALS[final_stem]
    if final_stem.endswith(NINI_FINALS):
        case = "सप्तमी" if final_stem.endswith(("वासिन्", "चारिन्", "शायिन्")) else "द्वितीया"
        return UPAPADA_KRT["णिनि"], case
    return None


def _d(samasa: str, rule: str, note: str, **kw: str) -> Decision:
    return Decision(samasa=samasa, rule=rule, note=note, **kw)


def _bv_signal(reading: Reading, members: Sequence[int]) -> str:
    """Why the whole is a qualifier of something else ("" if the sentence shows nothing)."""
    final = reading.words[members[-1]]
    m = final.morph
    shift = gender_shift(final)
    if shift:
        return f"gender shift: {shift}"
    j = agreeing_word(reading, members)
    if j is not None:
        return f"agrees with {reading.words[j].form}"
    if m is not None and m.vibhakti == "सम्बोधन":
        return "addresses a person (सम्बोधन)"
    return ""


def _prefix_decision(reading: Reading, members: Sequence[int], fcls: str, sig: str) -> Optional[Decision]:
    words = [reading.words[i] for i in members]
    first, final = words[0].form, words[-1]
    fm, fstem = final.morph, stem_of(final)
    if first in SAHA and fcls != "participle":
        return _d(BAHUVRIHI, "सह", "first member स/सह with a noun: 2.2.28 तेन सहेति तुल्ययोगे (सह → स 6.3.82)")
    if first in NAN:
        if fcls == "noun" and sig:
            return _d(NAN_BAHUVRIHI, "बहुव्रीहि", f"नञ् + noun used as a qualifier ({sig}): 2.2.24 with the "
                      "वार्त्तिक नञोऽस्त्यर्थानां बहुव्रीहिर्वा")
        return _d(NAN_TATPURUSHA, "नञ्", "नञ् first member: 2.2.6 नञ्")
    if first in AVYAYIBHAVA_FIRST and len(words) == 2 and fm.vacana == SG and fm.linga in (N, None)             and fm.vibhakti in ("प्रथमा", "द्वितीया") and agreeing_word(reading, members) is None:
        return _d(AVYAYIBHAVA, "अव्ययीभाव", f"indeclinable {first} + neuter singular used adverbially: "
                  f"{AVYAYIBHAVA_FIRST[first]}")
    if first in PRADI:
        if fcls == "noun" and (sig or fstem in POSSESSED):
            why = sig or f"{fstem} is a part/quality noun (lexical class)"
            return _d(BAHUVRIHI, "बहुव्रीहि", f"प्रादि + noun used as a qualifier ({why}): 2.2.24 अनेकमन्यपदार्थे")
        return _d(TATPURUSHA, "प्रादि", f"प्रादि {first} + {fcls or 'word'}: 2.2.18 कुगतिप्रादयः")
    return None


def decide(reading: Reading, members: Sequence[int]) -> Decision:
    """The samasa type of the compound ``members`` (indices into ``reading.words``)."""
    words = [reading.words[i] for i in members]
    final, prev = words[-1], words[-2] if len(words) > 1 else words[-1]
    fm, fstem, pstem = final.morph, stem_of(final), stem_of(prev)
    stems = [stem_of(w) for w in words]
    bracket = f"[{'-'.join(stems[:-1])}]-{fstem}" if len(words) > 2 else ""
    if fm is None or len(words) < 2:
        return _d(UNKNOWN, "", "final member has no analysis")
    (fcls, fsrc), (pcls, psrc) = word_class(final), word_class(prev)
    classes = f"classes: {pstem} {pcls or '?'} ({psrc}), {fstem} {fcls or '?'} ({fsrc})"
    sig = _bv_signal(reading, members)
    dec = _prefix_decision(reading, members, fcls, sig) or _main(reading, members, words, fcls, pcls, sig)
    return Decision(dec.samasa, dec.rule, dec.relation, f"{dec.note}; {classes}", dec.inner, bracket)


def _main(reading: Reading, members: Sequence[int], words: Sequence[Word], fcls: str, pcls: str,
          sig: str) -> Decision:
    final, prev = words[-1], words[-2]
    fm, fstem, pstem = final.morph, stem_of(final), stem_of(prev)
    noun = base_stem(fstem)
    up = _upapada(final, fstem)
    if up and pcls != "indeclinable":
        return _d(UPAPADA, "उपपद", f"{fstem} is a bound कृत् agent ({up[0]}): 2.2.19 उपपदमतिङ्", relation=up[1])
    if prev.form.endswith("तु") and fstem in ("काम", "मनस्"):
        return _d(BAHUVRIHI, "तुं-काम", "तुमुन् form + काम/मनस्: बहुव्रीहि, म् dropped (6.1.144 वार्त्तिक "
                  "तुं काममनसोरपि)")
    if fstem in BV_HEADS_ALWAYS or (fstem in BV_HEADS and (fm.vacana in (DU, PL) or sig)):
        return _d(BAHUVRIHI, "बहुव्रीहि", f"final {fstem} 'having X as first/chief' qualifies another word: "
                  "2.2.24 अनेकमन्यपदार्थे")
    shift = gender_shift(final)
    if shift and (fcls == "noun" or "4.1.4" in shift or "1.2.48" in shift):
        return _d(BAHUVRIHI, "बहुव्रीहि", f"gender shift ({shift}): the compound denotes another thing, "
                  "2.2.24 अनेकमन्यपदार्थे")
    if len(words) > 2 and word_class(words[0])[0] == "numeral" and fcls == "numeral":
        return _d(KARMADHARAYA, "संख्या", "numeral qualifying a numeral compound (दश + [X-सहस्र]): 2.1.57 "
                  "विशेषणं विशेष्येण बहुलम्")
    if pstem in QUANTITY and fcls == "noun" and sig:
        return _d(BAHUVRIHI, "बहुव्रीहि", f"quantity + noun qualifying another word ({sig}): 2.2.24 "
                  "अनेकमन्यपदार्थे")
    if pcls == "numeral" and len(words) == 2 and fcls == "noun":
        if sig and noun in POSSESSED:
            return _d(BAHUVRIHI, "बहुव्रीहि", f"numeral + part noun qualifying another word ({sig}): 2.2.24")
        return _d(DVIGU, "द्विगु", "numeral first member: 2.1.52 संख्यापूर्वो द्विगुः (2.1.51 तद्धितार्थोत्तरपद...)")
    if noun in POSSESSED and (fcls == "noun" or noun != fstem):
        if pcls in ("adjective", "participle", "numeral"):
            return _d(BAHUVRIHI, "बहुव्रीहि", f"qualifier + part/quality noun {noun} (lexical class): the "
                      f"possessor is meant, 2.2.24 अनेकमन्यपदार्थे{'; ' + sig if sig else ''}")
        if pcls == "noun" and sig:
            return _d(BAHUVRIHI, "उपमान-बहुव्रीहि", f"noun + part/quality noun qualifying another word ({sig}): "
                      "2.2.24 with the वार्त्तिक सप्तम्युपमानपूर्वपदस्य बहुव्रीहिरुत्तरपदलोपश्च")
    rel = _final_relation(fstem)
    if rel and pcls not in ("indeclinable", "numeral", "sarvadi"):
        nouns = all(word_class(w)[0] in ("noun", "") for w in words[:-1])
        inner = DVANDVA if len(words) > 2 and nouns and fstem in INNER_DVANDVA_FINALS else ""
        why = "; the members before it are coordinated (2.2.29 चार्थे द्वन्द्वः)" if inner else ""
        return _d(TATPURUSHA, rel[0], f"{fstem} takes the {rel[0]}: {rel[1]}{why}", relation=rel[0], inner=inner)
    if pcls == "participle" and prev.morph is not None and prev.morph.krt == "क्त" and fcls == "noun" and sig \
            and "agrees with" in sig:
        return _d(BAHUVRIHI, "बहुव्रीहि", f"क्त participle + noun {fstem}, the whole qualifying another word ({sig}): "
                  "2.2.24 अनेकमन्यपदार्थे, with the participle first by 2.2.36 निष्ठा")
    if pcls in ("adjective", "participle", "sarvadi"):
        rule = "2.1.49 पूर्वकालैकसर्वजरत्पुराणनवकेवलाः समानाधिकरणेन" if pcls == "sarvadi" else             "2.1.57 विशेषणं विशेष्येण बहुलम्"
        maha = "; महत् → महा 6.3.46 आन्महतः समानाधिकरणजातीययोः" if pstem == "महत्" else ""
        apposition = "; agreement alone does not make it a बहुव्रीहि: a कर्मधारय stands in apposition too"             if sig else ""
        return _d(KARMADHARAYA, "कर्मधारय", f"qualifier {pstem} + {fstem}, same referent: {rule}{maha}{apposition}")
    if pcls == "noun" and fstem in UPAMANA_GUNA:
        return _d(KARMADHARAYA, "उपमान", f"standard of comparison + common property: 2.1.55 उपमानानि सामान्यवचनैः")
    if pcls == "personal":
        return _d(TATPURUSHA, "षष्ठी", "pronoun stem + noun: 2.2.8 षष्ठी", relation="षष्ठी")
    if fcls == "participle" and fm.krt in ("क्त", "क्तवतु") and pcls in ("noun", ""):
        return _d(TATPURUSHA, "तृतीया", "noun + क्त participle (agent/instrument): 2.1.32 कर्तृकरणे कृता बहुलम्",
                  relation="तृतीया")
    if _is_dvandva(words):
        return _d(DVANDVA, "द्वन्द्व", f"coordinate nouns, {fm.vacana} for {len(words)} members: 2.2.29 चार्थे "
                  "द्वन्द्वः (2.2.34 for the order)")
    if pcls == "indeclinable":
        return _d(UNKNOWN, "", f"indeclinable first member {prev.form} is not one the rules here cover")
    why = "" if pcls and fcls else " (a member's class is unknown: षष्ठी by default)"
    return _d(TATPURUSHA, "षष्ठी", f"noun + {fcls or 'word'}: 2.2.8 षष्ठी{why}", relation="षष्ठी")


def _is_dvandva(words: Sequence[Word]) -> bool:
    """Coordinate nouns with a number that fits: dual for two, plural for more (2.2.29, 2.4.x)."""
    fm = words[-1].morph
    if fm is None or not all(word_class(w)[0] == "noun" for w in words):
        return False
    if stem_of(words[-1]) in PAIRED:  # रामपादौ: the dual is the pair of the final, not two members
        return False
    rel = [stem_of(w) in RELATIONAL for w in words]
    if rel[-1] and not all(rel):  # राजपुत्र, नृपात्मज: a relational final takes its correlate (षष्ठी)
        return False
    return (len(words) == 2 and fm.vacana == DU) or (len(words) > 2 and fm.vacana == PL)
