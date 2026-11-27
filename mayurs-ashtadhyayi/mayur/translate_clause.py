"""Clause rendering (verbs, their arguments, adjuncts) for the template renderer: a mixin of
``translate_core._Renderer``, which supplies the noun-phrase methods and the word tables."""

from __future__ import annotations

from typing import Optional

from . import english
from .translate_words import SUBORDINATORS, TIME_PHRASES, TO_OBJECT, WITH_LEMMAS, adverb, is_motion, is_question_lemma

Piece = tuple[str, Optional[int], str]
_CONNECTIVES = {"and", "but", "or", "then", "now", "thus", "if", "when", "so", "as"}
_NEGATIONS = {"not", "no"}
_MODAL = {"लृट्": "will", "लुट्": "will", "विधिलिङ्": "should", "आशीर्लिङ्": "may", "लृङ्": "would",
          "लेट्": "shall"}
_PAST = {"लिट्", "लङ्", "लुङ्"}
_PASSIVE = {"कर्मणि", "भावे"}


def _p(text: str, idx: Optional[int] = None, sep: str = " ") -> Piece:
    return (text, idx, sep)


class ClauseMixin:
    def nonfinite(self, i: int, mode: str) -> list[Piece]:
        self.used.add(i)
        w = self.words[i]
        g = self.text(i)
        if w.morph is None or w.arsha:
            word = g
        elif mode == "to":
            word = "to " + g
        else:
            word = "having " + english.participle(g)
        return [_p(word, i)] + self.tail(i)

    def tail(self, v: int) -> list[Piece]:
        out: list[Piece] = []
        kids = self.children.get(v, [])
        for k in [c for c in kids if self.role(c) in ("कर्म", "विधेय")] + [c for c in kids if self.role(c) not in ("कर्म", "विधेय")]:
            r = self.role(k)  # the object comes first: "having killed Vālin in battle"
            if r == "अव्यय":
                out = self.np(k) + out
            elif r == "कर्म" or r == "विधेय":
                out += self._object(v, k, is_motion(self.text(v)))
            elif r == "तुमर्थ":
                out += self.nonfinite(k, "to")
            elif r == "पूर्वकालक्रिया":
                out = self.nonfinite(k, "having") + out
            else:
                out += self.case_phrase(k)
        return out

    # ---- verbs ---------------------------------------------------------------------
    def verb(self, v: int, neg: Optional[int]) -> tuple[list[Piece], bool]:
        """Pieces for the verb; True when it is a 'let' clause (subject goes after 'let')."""
        w = self.words[v]
        m = w.morph
        g = self.text(v)
        if m is None or w.arsha or m.kind != "tinanta":
            txt = g if (m is None or w.arsha or not m.krt) else english.krt_form(m.krt, g)
            return ([_p(txt, v)] + ([_p("not", neg)] if neg is not None else [])), False
        p = {"उत्तमपुरुष": 1, "मध्यमपुरुष": 2}.get(m.purusha or "", 3)
        sg = m.vacana not in ("बहुवचन", "द्विवचन")
        sg3 = p == 3 and sg
        is_be = "am" if p == 1 and sg else "is" if sg3 else "are"
        was = "was" if sg and p != 2 else "were"
        passive = (m.prayoga or "") in _PASSIVE
        parts = g.split()
        if len(parts) == 2 and parts[0] == "be" and parts[1].endswith(("ed", "en")):
            g, passive = parts[1], True  # "be bewildered": already a passive participle
        isbe = g in ("be", "is", "are", "am")
        g = "be" if isbe else g
        aux, main, plain, let = "", g, "", False
        lak = m.lakara or "लट्"
        if lak in _MODAL:
            aux = _MODAL[lak] + (" be" if passive and not isbe else "")
            main = english.participle(g) if passive and not isbe else g
            plain = f"{aux} {main}"
        elif lak == "लोट्" and p != 2:
            let, aux, plain = True, "", g
        elif lak in ("लोट्",):
            aux, plain = "do", g
        elif lak in _PAST:
            aux = "did" if not passive else was
            main = english.participle(g) if passive else g
            plain = f"{was} {main}" if passive and not isbe else (was if isbe else english.past(g))
        else:
            aux = ("does" if sg3 else "do") if not passive else is_be
            main = english.participle(g) if passive else g
            plain = f"{is_be} {main}" if passive and not isbe else (is_be if isbe else
                                                                  english.third_singular(g) if sg3 else g)
        if isbe and not passive and lak not in _MODAL:
            piece = _p(plain.split()[0] if plain else is_be, v)
            if lak == "लोट्":
                return ([_p("not", neg)] if neg is not None else []) + [_p("be", v)], let
            return [piece] + ([_p("not", neg)] if neg is not None else []), False
        if neg is None:
            return [_p(plain, v)], let
        out = [_p(aux)] if aux and not let else []
        out.append(_p("not", neg))
        out.append(_p(main, v))
        return out, let

    def _object(self, v: int, k: int, motion: bool) -> list[Piece]:
        """An object with the preposition its verb needs: went *to* the forest, bows *to* the guru."""
        km = self.words[k].morph
        verb = self.text(v).lower().split()
        if verb and verb[-1] in ("to", "into", "towards", "toward"):
            return self.np(k)  # the verb's own gloss already ends in the preposition ("come to")
        to = self.role(k) == "कर्म" and (
            (motion and not (km and english.is_pronoun(km.lemma)))
            or (bool(verb) and verb[0] in TO_OBJECT and (verb[0] == "bow" or (km and english.is_pronoun(km.lemma))
                                                         or self.words[k].gloss[:1].isupper())))
        return ([_p("to")] if to else []) + self.np(k)

    def clause_core(self, v: int, keep_conn: bool = True) -> list[Piece]:
        self.used.add(v)
        m = self.words[v].morph
        passive = m is not None and (m.prayoga or "") in _PASSIVE
        kta = m is not None and m.kind == "subanta" and m.krt == "क्त"
        voc, conn, adv, after_verb, tail_adv = [], [], [], [], []
        subj: list[int] = []
        agent: list[int] = []
        objs: list[int] = []
        rest: list[int] = []
        neg: Optional[int] = None
        motion = is_motion(self.text(v)) and m is not None
        if kta:  # a past participle as the verb: passive with an agent, active when it only moves
            passive = any(self.role(k) == "कर्ता" and (self.words[k].morph or m).vibhakti == "तृतीया"
                          for k in self.children.get(v, [])) or not motion
        for k in self.children.get(v, []):
            r = self.role(k)
            km = self.words[k].morph
            if r == "सम्बोधन":
                voc += [_p("O")] + self.np(k) + [_p(",", None, "")]
            elif r == "अव्यय":
                g = self.text(k)
                if g in _NEGATIONS and neg is None:
                    neg = k
                    self.used.add(k)
                elif g in _CONNECTIVES:
                    self.used.add(k)
                    if keep_conn or g in SUBORDINATORS:  # a clause-initial 'and' of the first clause would dangle
                        conn.append(_p(g, k))
                elif g in TIME_PHRASES:
                    self.used.add(k)
                    tail_adv.append(_p(TIME_PHRASES[g], k))
                elif km is not None and km.lemma in WITH_LEMMAS:
                    tail_adv += self.np(k)  # सह / विना with its dependent: "with Sītā"
                elif km is not None and km.kind == "subanta" and not km.vibhakti == "सम्बोधन":
                    self.used.add(k)
                    after_verb.append(_p(adverb(g), k))  # an adverbial adjective: quick -> quickly
                else:
                    self.used.add(k)
                    adv.append(_p(g, k))
            elif r == "कर्ता":
                (agent if passive and km and km.vibhakti == "तृतीया" else subj).append(k)
            elif r in ("कर्म", "विधेय"):
                objs.append(k)
            else:
                rest.append(k)
        if passive and not subj:
            subj, objs = objs, []
        vpieces, let = self.verb(v, neg)
        if kta and passive and vpieces:
            plural = bool(subj) and (self.words[subj[0]].morph or m).vacana in ("बहुवचन", "द्विवचन")
            txt = ("were " if plural else "was ") + english.participle(self.text(v))
            vpieces = ([_p(txt, v)] if neg is None else [_p("was" if not plural else "were", v), _p("not", neg),
                                                          _p(english.participle(self.text(v)))])
        elif kta and not passive and vpieces:
            vpieces = [_p(english.past(self.text(v)), v)]
        self.used.add(neg) if neg is not None else None
        spieces: list[Piece] = []
        if let:
            for k in subj:
                self.acc.add(k)
        for k in subj:
            preds = [c for c in self.children.get(k, []) if self.role(c) == "विधेय" and c not in self.used]
            spieces += self.np(k, [c for c in self.children.get(k, []) if c not in preds])
            for c in preds:
                objs.append(c)
        if not subj and m is not None and not (m.lakara == "लोट्" and m.purusha == "मध्यमपुरुष"):
            if m.kind == "tinanta":
                spieces = [_p(english.supplied_subject(m.purusha, m.vacana, accusative=let))]
        prior = [k for k in rest if self.role(k) == "पूर्वकालक्रिया"]
        pre: list[Piece] = []
        for k in prior:
            pre += self.nonfinite(k, "having")
        post: list[Piece] = []
        wh = next((k for k in objs if self.words[k].morph and is_question_lemma(self.words[k].morph.lemma)), None)
        ask = (wh is not None and m is not None and m.kind == "tinanta" and neg is None and not let and not passive
               and (m.lakara or "लट्") in ("लट्", "लङ्", "लिट्", "लुङ्") and self.text(v) not in ("be", "is"))
        if ask:
            objs = [k for k in objs if k != wh]
        for k in objs:
            post += self._object(v, k, motion)
        for k in agent:
            post += [_p("by")] + self.np(k)
        for k in rest:
            if k in prior:
                continue
            if self.role(k) == "अधिकरण" and self.text(v).lower().split()[:1] == ["enter"]:
                post += self.np(k)  # enters the mouth, not "enters in the mouth"
                continue
            post += self.nonfinite(k, "to") if self.role(k) == "तुमर्थ" else self.case_phrase(k)
        post = after_verb + post + tail_adv
        if ask:  # "what did they do?": question word, auxiliary, subject, bare verb
            sg3 = m.vacana not in ("बहुवचन", "द्विवचन") and m.purusha not in ("उत्तमपुरुष", "मध्यमपुरुष")
            aux = "did" if m.lakara in _PAST else "does" if sg3 else "do"
            base = english.base(self.text(v))
            base = "do" if base == "make" and self.text(wh) == "what" else base
            return voc + conn + self.np(wh) + [_p(aux)] + spieces + adv + pre + [_p(base, v)] + post
        existential = (subj and self.text(v) in ("be", "is", "are") and min(subj) > v and not let and not passive
                       and not any(self.role(k) == "विधेय" for k in objs))
        if existential:  # a sentence-initial अस्ति: "There is a tree on the bank"
            return voc + conn + [_p("there")] + vpieces + spieces + adv + pre + post
        if pre and not let:  # an absolutive clause comes first: "Having gone to the village, he eats"
            return voc + conn + pre + [_p(",", None, "")] + spieces + adv + vpieces + post
        head = [_p("let")] + spieces + adv + pre + vpieces if let else spieces + adv + pre + vpieces
        return voc + conn + head + post
