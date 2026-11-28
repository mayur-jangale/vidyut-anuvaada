"""Matching conventions of the evaluation: when one of our words, padas or analyses counts as the
corpus's (spelling normalisation, lemma conventions, the corpus's member flags, padas compared as
written, morphology counts). Pure functions, unit-tested; see eval/eval_dcs.py for the conventions."""

from __future__ import annotations

from typing import Any, Callable, Sequence

from mayur import freq, lipi, sandhi, ud

FEATURES = ("Case", "Number", "Gender", "Tense", "Mood", "Person", "VerbForm")
_VARGA = {"ङ्": "कखगघ", "ञ्": "चछजझ", "ण्": "टठडढ", "न्": "तथदधन", "म्": "पफबभम"}


_FINAL_STOP = {"द्": "त्", "ग्": "क्", "ड्": "ट्", "ब्": "प्"}


def normalize(form: str) -> str:
    """Spelling differences that are not analysis differences, removed before comparing forms.

    * anusvara for a nasal + virama followed by a consonant of its own varga (साम्प्रतम् = सांप्रतम्);
    * a pada-final voiced stop as its unvoiced partner (the corpus writes both काचिद् and काचित्);
    * ण as न: the corpus often undoes retroflexion in its reconstructed forms (ब्रह्मना for ब्रह्मणा).
    """
    for voiced, plain in _FINAL_STOP.items():
        if form.endswith(voiced):
            form = form[: -len(voiced)] + plain
    form = form.replace("ण", "न")
    out, i = [], 0
    while i < len(form):
        pair = form[i:i + 2]
        if pair in _VARGA and i + 2 < len(form) and form[i + 2] in _VARGA[pair]:
            out.append("ं")
            i += 2
        else:
            out.append(form[i])
            i += 1
    return "".join(out)


def word_matches(form: str, gold_form: str, gold_lemma: str = "", compound_member: bool = False,
                 lemma: str = "", lenient: bool = False) -> bool:
    f = normalize(form)
    if f == normalize(gold_form):
        return True
    same_lemma = same_lexeme(lemma, gold_lemma)
    if compound_member and gold_lemma and (f == normalize(gold_lemma) or same_lemma):
        return True
    return lenient and same_lemma


def _lexeme(lemma: str) -> str:
    return normalize(ud.canonical_lemma(lemma))


def same_lexeme(ours: str, gold_lemma: str) -> bool:
    """Same lemma under the citation conventions of ``mayur.ud`` (strong stems, feminine stems)."""
    if not ours or not gold_lemma:
        return False
    a, b = _lexeme(ours), _lexeme(gold_lemma)
    return a == b or ud._feminine_of(a, b)


def scored_member(w: Any) -> bool:
    """Whether our word counts as a compound member when compared with the corpus, which tags
    indeclinable members and glued prefixes as free words (see the module docstring)."""
    if not w.in_compound:
        return False
    lemma = ud.lemma(w.morph) if w.morph is not None else w.form
    return freq.lemma_class(lemma) != "indeclinable"


def _parts(ours_word: Sequence[Any]) -> tuple[str, str]:
    """(form, lemma) of one of our words given as (form, in_compound[, lemma])."""
    return ours_word[0], (ours_word[2] if len(ours_word) > 2 else "")


def our_word(w: Any) -> tuple[str, bool, str]:
    return w.form, scored_member(w), (ud.lemma(w.morph) if w.morph is not None else "")


def lcs_pairs(a: Sequence[Any], b: Sequence[Any], eq: Callable[[Any, Any], bool]) -> list[tuple[int, int]]:
    """Index pairs (i, j) of one longest common subsequence of ``a`` and ``b`` under ``eq``."""
    n, m = len(a), len(b)
    table = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            table[i][j] = table[i + 1][j + 1] + 1 if eq(a[i], b[j]) else max(table[i + 1][j], table[i][j + 1])
    pairs, i, j = [], 0, 0
    while i < n and j < m:
        if eq(a[i], b[j]):
            pairs.append((i, j))
            i, j = i + 1, j + 1
        elif table[i + 1][j] >= table[i][j + 1]:
            i += 1
        else:
            j += 1
    return pairs


def prf(matched: int, n_ours: int, n_gold: int) -> dict[str, float]:
    p = matched / n_ours if n_ours else 0.0
    r = matched / n_gold if n_gold else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return {"precision": p, "recall": r, "f1": f}


def split_equal(ours: Sequence[Sequence[Any]], gold_words: Sequence[dict], lenient: bool = False) -> bool:
    """Our (form, in_compound[, lemma]) sequence equals the gold word sequence (after normalisation)."""
    return len(ours) == len(gold_words) and all(
        word_matches(_parts(o)[0], g["form"], g["lemma"], g["compound_member"], _parts(o)[1], lenient)
        for o, g in zip(ours, gold_words))


def align_words(ours: Sequence[Sequence[Any]], gold_words: Sequence[dict],
                lenient: bool = False) -> list[tuple[int, int]]:
    """LCS alignment; ``lenient`` also pairs words with the same lemma but a differently
    reconstructed form (the corpus has मम where the text has मे)."""
    return lcs_pairs(ours, gold_words, lambda o, g: word_matches(
        _parts(o)[0], g["form"], g["lemma"], g["compound_member"], _parts(o)[1], lenient))


def morphology_counts(pairs: Sequence[tuple[Any, dict]]) -> dict[str, int]:
    """Counts over (Morph | None, gold word) pairs of non-compound words."""
    c = {"words": 0, "lemma": 0, "all_features": 0, "analysis": 0, **{f"feat_{k}_total": 0 for k in FEATURES},
         **{f"feat_{k}": 0 for k in FEATURES}}
    for morph, g in pairs:
        c["words"] += 1
        ours = ud.feats(morph) if morph is not None else {}
        upos = g.get("upos", "")
        lemma_ok = morph is not None and ud.same_lemma(morph, g["lemma"], upos)
        c["lemma"] += int(lemma_ok)
        c["analysis"] += int(lemma_ok and ud.same_feats(morph, upos, g["feats"]))  # lemma AND every feature
        for k in ud.compared_features(upos, g["feats"]):
            if k in FEATURES:
                c[f"feat_{k}_total"] += 1
                c[f"feat_{k}"] += int(ours.get(k) == g["feats"][k])
        c["all_features"] += int(morph is not None and ud.same_feats(morph, upos, g["feats"]))
    return c


def add_counts(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    return {k: a.get(k, 0) + b.get(k, 0) for k in {*a, *b}}


def pada_units(words: Sequence[Sequence[Any]]) -> list[tuple[str, str, tuple[str, ...]]]:
    """Group (form, in_compound[, lemma]) words into padas: a run of compound members plus its final
    word is ONE unit ``(glued forms, lemma of the final word, member forms)``."""
    units, run = [], []
    for w in words:
        run.append(w[0])
        if not w[1]:
            units.append(("".join(run), w[2] if len(w) > 2 else "", tuple(run)))
            run = []
    if run:
        units.append(("".join(run), "", tuple(run)))
    return units


def gold_pada_units(gold_words: Sequence[dict]) -> list[tuple[str, str, tuple[str, ...]]]:
    return pada_units([(w["form"], w["compound_member"], w["lemma"]) for w in gold_words])


def written(members: Sequence[str]) -> frozenset[str]:
    """The ways a pada made of ``members`` is written: joined by compound sandhi, cited in isolation."""
    if len(members) == 1:
        return frozenset({normalize(lipi.pausa(members[0]))})
    try:
        return frozenset(normalize(x) for x in sandhi.rejoin(list(members), [True] * (len(members) - 1)))
    except Exception:  # noqa: BLE001 - a corpus form the sandhi rules cannot read
        return frozenset()


def pada_match(ours: Sequence[Any], gold_unit: Sequence[Any]) -> bool:
    """Same pada: the same glued forms, the same written word after sandhi, or failing that the
    same lemma of the final member."""
    if normalize(ours[0]) == normalize(gold_unit[0]) or same_lexeme(ours[1], gold_unit[1]):
        return True
    return len(ours) > 2 and len(gold_unit) > 2 and bool(written(ours[2]) & written(gold_unit[2]))


def pada_line_equal(ours: Sequence[Sequence[Any]], gold_words: Sequence[dict]) -> bool:
    a, b = pada_units(ours), gold_pada_units(gold_words)
    return len(a) == len(b) and all(pada_match(x, y) for x, y in zip(a, b))
