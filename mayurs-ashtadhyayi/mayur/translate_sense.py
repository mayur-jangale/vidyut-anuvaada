"""Senses that depend on the sentence (a mixin of ``translate_core._Renderer``): a verb whose meaning follows its
argument, a noun that a verb of entering turns into "mouth", a participle used as a noun ("song", "Sanskrit"),
and the person a possessive refers to (स्व "own" -> "his own", a hand -> "his hand")."""

from __future__ import annotations

from typing import Optional

from . import english
from .translate_words import BODY_PARTS, KRT_NOUNS, NOUN_BY_VERB, POSSESSED, POSSESSIVES, VERB_SENSES


class SenseMixin:
    def verb_of(self, i: int) -> Optional[int]:
        """The finite verb or clause head that word ``i`` hangs on (through a compound), or None."""
        w = self.words[i]
        if w.head is None or not 0 <= w.head < len(self.words):
            return None
        h = self.resolve(w.head)
        return h if self.words[h].role == "क्रिया" else None

    def clause_verb(self, i: int) -> Optional[int]:
        """The verb of the clause word ``i`` belongs to: the first verb on its chain of heads, or None."""
        seen: set[int] = set()
        while i not in seen:
            seen.add(i)
            w = self.words[i]
            if w.role == "क्रिया":
                return i
            if w.head is None or not 0 <= w.head < len(self.words):
                return None
            i = self.resolve(w.head)
        return None

    def context_sense(self, i: int) -> str:
        """English that replaces the gloss of word ``i`` because of its arguments or its verb, else ''."""
        w = self.words[i]
        m = w.morph
        if m is None or w.arsha:
            return ""
        if m.root and not m.prefixes and m.kind == "tinanta":
            roles = {self.role(c) for c in self.children.get(i, [])}
            for (root, role), sense in VERB_SENSES.items():
                if m.root == root and role in roles:
                    return sense
        if w.gloss in NOUN_BY_VERB and m.kind == "subanta":
            v = self.verb_of(i)
            verbs, sense = NOUN_BY_VERB[w.gloss]
            if v is not None and (self.text(v).lower().split() or [""])[0] in verbs:
                return sense
        return ""

    def krt_noun(self, i: int) -> str:
        """A participle that stands as a noun in this clause (गीतम् "song"), else ''."""
        m = self.words[i].morph
        hit = KRT_NOUNS.get((m.lemma, m.krt)) if m is not None else None
        if hit is None or self.role(i) not in ("कर्म", "कर्ता"):
            return ""
        noun, verbs = hit
        v = self.verb_of(i)
        if verbs is None:
            return noun
        return noun if v is not None and (self.text(v).lower().split() or [""])[0] in verbs else ""

    def possessor(self, i: int) -> str:
        """The possessive pronoun of the subject of the clause that word ``i`` belongs to ("his"), else ''."""
        v = self.clause_verb(self.resolve(i))
        if v is None:
            return ""
        vm = self.words[v].morph
        passive = vm is not None and (vm.prayoga or "") in ("कर्मणि", "भावे")
        kids = [c for c in self.children.get(v, []) if not self.words[c].in_compound]
        subs = [c for c in kids if self.role(c) == "कर्ता" or (passive and self.role(c) == "कर्म"
                                                              and self.words[c].morph.vibhakti == "प्रथमा")]
        by_agent = [c for c in subs if self.words[c].morph and self.words[c].morph.vibhakti == "तृतीया"]
        pick = (by_agent or subs or [None])[0]
        sm = self.words[pick].morph if pick is not None else None
        if sm is None or sm.kind != "subanta":
            return ""
        if english.is_pronoun(sm.lemma):
            pron = english.pronoun(sm.lemma, sm.linga, sm.vacana, "षष्ठी")
            return pron if pron in POSSESSIVES else ""
        if sm.vacana in ("बहुवचन", "द्विवचन"):
            return "their"
        return {"पुंलिङ्ग": "his", "स्त्रीलिङ्ग": "her", "नपुंसकलिङ्ग": "its"}.get(sm.linga or "", "")

    def supplied_possessive(self, i: int) -> str:
        """'his' for a body part with no possessor of its own that serves as an instrument ('with [his] hand')."""
        w = self.words[i]
        m = w.morph
        if m is None or w.role not in ("करण", "अधिकरण") or w.gloss not in BODY_PARTS or m.kind != "subanta":
            return ""
        if any(self.role(c) in ("सम्बन्ध", "विशेषण") for c in self.children.get(i, [])) or self.members(i):
            return ""
        v = self.verb_of(i)
        vm = self.words[v].morph if v is not None else None
        if vm is None or vm.kind != "tinanta" or (vm.prayoga or "") in ("कर्मणि", "भावे"):
            return ""
        return self.possessor(i)

    def own_prefix(self, j: int) -> list:
        """['[his]'] before स्व "own" (it refers to the subject), or [] when the subject is not clear."""
        if self.words[j].gloss != "own":
            return []
        poss = self.possessor(j)
        return [(f"[{poss}]", None, " ")] if poss else []

    def when_participle(self, k: int, i: int) -> bool:
        """True for a past participle that qualifies the subject ``i`` from after the verb (धर्मो रक्षति रक्षितः):
        it says when the verb holds, so it reads "when protected" and not an attribute in front of the noun."""
        km = self.words[k].morph
        if km is None or km.krt != "क्त" or km.kind != "subanta" or self.role(i) not in ("कर्ता", "कर्म"):
            return False
        v = self.verb_of(i)
        vm = self.words[v].morph if v is not None else None
        bare = not self.children.get(k) and not self.words[k].gloss.startswith("be ")  # nothing attached to it
        return (vm is not None and vm.lakara == "लट्" and bare and k > v
                and self.words[k].morph.vibhakti == self.words[i].morph.vibhakti)

    def possessed_noun(self, i: int) -> str:
        """The noun an adjective of possession stands for when it is the head ('my' -> 'men'), else ''."""
        w = self.words[i]
        m = w.morph
        if m is None or w.gloss not in POSSESSIVES or w.role in ("विशेषण", "विधेय") or m.kind != "subanta":
            return ""
        noun = POSSESSED[{"पुंलिङ्ग": 0, "स्त्रीलिङ्ग": 1}.get(m.linga or "", 2)]
        return english.plural(noun) if m.vacana in ("बहुवचन", "द्विवचन") else noun
