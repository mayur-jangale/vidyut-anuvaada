"""Learned analysis choice: a lexicalised, candidate-restricted averaged-perceptron tagger.

Trained by ``scripts/train_tagger.py`` on DCS annotations (CC BY 4.0). A sequence is a whole
verse (half-verse boundaries kept as features). For each word the lexicon's analyses are the
only tags it may take; the model scores (word, candidate, context):

* observation features of the word (form, final/initial sounds, neighbouring forms, position),
* features of the candidate (lemma, lemma class, corpus counts, quality, source),
* agreement with the other words' candidate sets in the same half-verse (distance ≤ 4),
* history features from left-to-right beam search (two previous tags, concord with the chosen
  analyses of earlier words in the half-verse, verb–subject fit).

Every feature is conjoined with the candidate's full tag and with its case, gender and number
alone. Weights: ``{observation: {conjunct key: weight}}``.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Optional, Sequence

from mayur import tagger_siblings
from mayur.model import Morph
from mayur.tagger_features import Obs, Verse, _sounds, keys, tag  # noqa: F401  (re-exported)

MODEL_FILE = Path(__file__).resolve().parent / "models" / "tagger.json"
BEAM = 8
WINDOW = 4
Weights = dict[str, dict[str, float]]
_PARTICLES = frozenset({"च", "इव", "न", "तु", "हि", "वा", "एव", "अपि", "इति"})
_PERSON = {"अस्मद्": "उत्तमपुरुष", "युष्मद्": "मध्यमपुरुष"}


def score_obs(w: Weights, obs: Obs, ks: tuple[str, ...]) -> float:
    s = 0.0
    for o in obs:
        d = w.get(o)
        if d:
            for k in ks:
                s += d.get(k, 0.0)
    return s


def decode(v: Verse, w: Weights, gold: Optional[Sequence[tuple[int, ...]]] = None):
    """Beam search. Without ``gold``: best path. With ``gold`` (training): ``(pred, gold_path)``
    prefixes at the first point where no gold-consistent path survives (early update), else full paths."""
    n = len(v.cands)
    stat = [[score_obs(w, v.static[i][k], keys(m)) for k, m in enumerate(c)] for i, c in enumerate(v.cands)]
    # --- neural hook (mayur.neural): + λ · neural candidate score, set by choose_indices ---
    bonus = getattr(v, "neural_bonus", None)
    if bonus:
        stat = [[x + b for x, b in zip(row, brow)] for row, brow in zip(stat, bonus)]
    # --- end neural hook ---
    beam: list[tuple[float, tuple[int, ...]]] = [(0.0, ())]
    gpath: tuple[int, ...] = ()
    gscore = 0.0

    def ext(score: float, path: tuple[int, ...], i: int, k: int) -> float:
        return score + stat[i][k] + score_obs(w, v.history(i, k, path), keys(v.cands[i][k]))

    for i in range(n):
        if not v.cands[i]:
            beam = [(s, p + (-1,)) for s, p in beam]
            gpath += (-1,)
            continue
        cand = [(ext(s, p, i, k), p + (k,)) for s, p in beam for k in range(len(v.cands[i]))]
        cand.sort(key=lambda x: -x[0])
        beam = cand[:BEAM]
        if gold is None:
            continue
        allowed = gold[i] or tuple(range(len(v.cands[i])))
        opts = [(ext(gscore, gpath, i, k), gpath + (k,)) for k in allowed]
        gscore, gpath = max(opts, key=lambda x: x[0])
        consistent = [b for b in beam if all(not gold[j] or b[1][j] in gold[j] for j in range(i + 1))]
        if not consistent:
            return list(beam[0][1]), list(gpath)
        gscore, gpath = consistent[0]
    best = list(beam[0][1])
    return best if gold is None else (best, list(gpath))


@lru_cache(maxsize=1)
def load(path: Optional[str] = None) -> Optional[dict]:
    p = Path(path) if path else MODEL_FILE
    if not p.exists():
        return None
    data = json.loads(p.read_text(encoding="utf-8"))
    return data if data.get("enabled", True) and "weights" in data else None


def enabled() -> bool:
    return load() is not None


def choose_indices(cands: Sequence[Sequence[Morph]], lines: Sequence[int], compound_flags: Sequence[bool],
                   forms: Sequence[str], weights: Optional[Weights] = None,
                   weights2: Optional[Weights] = None, tables: Optional[dict] = None,
                   neural_bonus: Optional[Sequence[Sequence[float]]] = None,
                   obs_forms: Optional[Sequence[str]] = None,
                   variants: Optional[Sequence[Sequence[str]]] = None) -> list[int]:
    """Index of the chosen candidate per word (0 for a word without candidates). With second-pass
    weights the verse is decoded again, every word seeing the first-pass choices of the others.
    ``neural_bonus``: λ-weighted neural score per candidate; None = from ``mayur.neural`` when enabled
    (only when the saved model is used, i.e. ``weights`` is None)."""
    if weights is None:
        model = load() or {}
        weights, weights2, tables = model.get("weights", {}), model.get("weights2"), model.get("tables", {})
        if neural_bonus is None:  # --- neural hook ---
            neural_bonus = _neural_bonus(cands, lines, compound_flags, forms)
    if not cands:
        return []
    extra = {"obs_forms": obs_forms, "variants": variants, "tables": tables}
    v1 = Verse(cands, lines, compound_flags, forms, **extra)
    v1.neural_bonus = neural_bonus
    path = [max(k, 0) for k in decode(v1, weights)]
    if weights2:
        v2 = Verse(cands, lines, compound_flags, forms, prior=path, **extra)
        v2.neural_bonus = neural_bonus
        path = [max(k, 0) for k in decode(v2, weights2)]
    return path


def sibling_candidates(form: str) -> list[Morph]:
    """The pruned candidates (``shabdabodha.candidates``) of a sibling pada form."""
    from mayur import lexicon, shabdabodha
    from mayur.model import Word
    w = Word(form=form, line=0, start=0, end=1, in_compound=False, analyses=list(lexicon.padas(form)))
    return [w.analyses[i] for i in shabdabodha.candidates(w)] if w.analyses else []


def choose_with_siblings(cands: Sequence[Sequence[Morph]], lines: Sequence[int], compound_flags: Sequence[bool],
                         forms: Sequence[str], **kw) -> tuple[list[Morph | None], dict[int, str]]:
    """Chosen analysis per word among its own candidates and those of its sibling form
    (``mayur.tagger_siblings``), and ``{word index: sibling form}`` where a sibling's analysis won.
    Without a model trained with siblings, siblings are not considered."""
    use = kw.pop("siblings", None)
    if use is None:
        use = bool((load() or {}).get("siblings")) if kw.get("weights") is None else True
    find = kw.pop("sibling_candidates", sibling_candidates)
    if use:
        ext, own, obs, var = tagger_siblings.extend(cands, forms, compound_flags, find)
    else:
        ext, own, obs, var = [list(c) for c in cands], [len(c) for c in cands], None, None
    if kw.get("neural_bonus") is None and kw.get("weights") is None:
        kw["neural_bonus"] = _neural_bonus(ext, lines, compound_flags, forms)
    path = choose_indices(ext, lines, compound_flags, forms, obs_forms=obs, variants=var, **kw)
    chosen = [c[k] if c else None for c, k in zip(ext, path)]
    swaps = {i: m.form for i, (m, k) in enumerate(zip(chosen, path)) if m is not None and k >= own[i]}
    return chosen, swaps


def sibling_forms(words) -> dict[int, str]:
    """For ``shabdabodha``'s words: ``{index: form}`` where the tagger prefers the analysis of the word's
    sibling pada form (मूढा -> मूढास् before a voiced sound, भीष्मे -> भीष्मस् before a vowel)."""
    from mayur.shabdabodha import candidates
    if load() is None or not (load() or {}).get("siblings"):
        return {}
    cands = [[w.analyses[j] for j in candidates(w)] if w.analyses else [] for w in words]
    _, swaps = choose_with_siblings(cands, [w.line for w in words], [w.in_compound for w in words],
                                    [w.form for w in words])
    return swaps


def _neural_bonus(cands, lines, compound_flags, forms) -> list:
    """--- neural hook --- λ · Σ log P(feature value) per candidate, [] when the model is off."""
    try:
        from mayur import neural
        if not neural.enabled() or neural.weight() <= 0:
            return []
        lam = neural.weight()
        scores = neural.candidate_scores(cands, neural.feature_logprobs(forms, lines, compound_flags))
        return [[lam * x for x in row] for row in scores]
    except Exception:  # torch or model broken: fall back to the perceptron alone
        return []


def choose(words, candidates=None, compound_flags=None, forms=None):
    """Two call styles.

    * ``choose(cands, lines, compound_flags, forms) -> list[int]``: candidate index per word.
    * ``choose(words: list[Word], candidates: Callable[[Word], list[int]])`` (as ``shabdabodha``
      calls it): chosen index into ``word.analyses`` per word, or None when no model is enabled.
    """
    if not callable(candidates):
        return choose_indices(words, candidates or [0] * len(words), compound_flags or [False] * len(words),
                              forms or [""] * len(words))
    if load() is None:
        return None
    idx = [list(candidates(x)) for x in words]
    cands = [[x.analyses[j] for j in ix] for x, ix in zip(words, idx)]
    pick = choose_indices(cands, [x.line for x in words], [x.in_compound for x in words], [x.form for x in words])
    return [ix[k] if ix else x.chosen for x, ix, k in zip(words, idx, pick)]


def _agent_noun_governs(words, chosen: list[int], i: int) -> bool:
    """A feminine participle read where a तृच् agent noun is possible, next to a genitive it can govern
    (2.3.65 कर्तृकर्मणोः कृति) and with no feminine noun in its case in the half-verse to agree with."""
    m = words[i].analyses[chosen[i]]
    if not (m.krt and m.krt != "तृच्" and m.linga == "स्त्रीलिङ्ग" and m.vibhakti == "प्रथमा"):
        return False
    if not any(a.krt == "तृच्" and a.vibhakti == "प्रथमा" for a in words[i].analyses):
        return False
    near = [words[j].analyses[chosen[j]] for j in (i - 1, i + 1) if 0 <= j < len(words) and words[j].analyses]
    fem = any(w.analyses and k != i and w.line == words[i].line and w.analyses[chosen[k]].linga == "स्त्रीलिङ्ग"
              and w.analyses[chosen[k]].vibhakti == "प्रथमा" and not w.analyses[chosen[k]].krt
              for k, w in enumerate(words))
    return any(x.vibhakti == "षष्ठी" for x in near) and not fem


def enforce(words, chosen: list[int], force: bool = False) -> list[int]:
    """Hard constraints on a learned choice: a तृच् noun over an equally likely लुट् verb, and
    a finite verb without an agreeing nominative takes the nearest word that has one.
    The second is applied only when the saved model says it helps on DEV (or with ``force``)."""
    from mayur.shabdabodha import PRATHAMA, _agent_noun_preferred, candidates, is_case, is_finite, karta_agrees
    out = list(chosen)
    for i, w in enumerate(words):
        if w.analyses and _agent_noun_preferred(w, w.analyses[out[i]]):
            out[i] = next(j for j, a in enumerate(w.analyses) if a.krt == "तृच्" and is_case(a, PRATHAMA))
        elif w.analyses and _agent_noun_governs(words, out, i):
            out[i] = next(j for j, a in enumerate(w.analyses) if a.krt == "तृच्" and is_case(a, PRATHAMA))
    if not force and not (load() or {}).get("enforce", True):
        return out
    for v, wv in enumerate(words):
        vm = wv.analyses[out[v]] if wv.analyses else None
        if not is_finite(vm):
            continue
        line = [i for i, w in enumerate(words) if w.line == wv.line and w.analyses and not w.in_compound]
        if any(karta_agrees(words[i].analyses[out[i]], vm) for i in line):
            continue
        options = [(abs(i - v), i, j) for i in line if i != v for j in candidates(words[i])
                   if karta_agrees(words[i].analyses[j], vm) and not is_finite(words[i].analyses[out[i]])]
        if options:
            _, i, j = min(options)
            out[i] = j
    return out
