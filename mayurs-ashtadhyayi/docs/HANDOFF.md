# Handoff: Mayur's Ashtadhyayi

State of the project on 2026-11-28, for whoever picks it up next. The measured numbers and how
they were taken are in `README.md`; the milestones are in `docs/ROADMAP.md`. This note says what is
finished, what is not, and how to continue without breaking the measurements.

## What this is

A rule-based Sanskrit interpreter that runs offline, with no language model and no API key. For a
verse it gives the word split, compound breakdown, grammar of each word, prose order, a gloss per
word and two English lines, with every step traceable to a sūtra. A reading counts as `verified`
only if its words re-join to the input by sandhi and each word is re-derived by vidyut-prakriya.

Everything lives in `mayurs-ashtadhyayi/`. The `vidyut_anuvaada/` directory beside it is an earlier,
separate package; nothing here imports it.

## Set-up

```bash
cd mayurs-ashtadhyayi
pip install -e ".[dev]"          # add ".[neural]" for torch (trained rankers, optional translator)
python scripts/fetch_data.py     # vidyut data and the DCS corpus at pinned revisions; builds data/derived/
python -m pytest -q              # about 10 minutes on 4 cores; all tests pass at this commit
mayur analyze "श्वेतो धावति"
```

- `data/` is not in git. It is rebuilt by `fetch_data.py`. `MAYUR_DATA_DIR` points the package at a
  data directory elsewhere (needed when working in a second checkout or a git worktree).
- The processes are memory-hungry. On a shared machine run them under `ulimit -v 9000000` and not
  more than four at once.
- A plain `python script.py` picks up the editable install. In a second checkout use `PYTHONPATH=.`
  so that checkout's code is what runs.

## Where things are

| Layer | Files |
|---|---|
| Sandhi, split lattice, split ranker | `mayur/sandhi.py`, `segmenter.py`, `decoder.py` |
| Lexicon and labelled epic forms | `mayur/lexicon*.py` |
| Choice of analysis | `mayur/tagger*.py`, `siblings.py`, `particle_ma.py`, `one_verb.py` |
| Proof gate | `mayur/proof.py`, `proof_context.py`, `lexicon_passive.py` |
| Compounds | `mayur/compounds.py`, `samasa*.py` |
| Sentence structure | `mayur/vakya*.py`, `karaka*.py`, `anvaya.py`, `shabdabodha.py` |
| Meaning | `mayur/gloss.py`, `senses.py`, `artha.py`, `annotations/*.json` |
| English | `mayur/translate*.py`, `fluent*.py`, `english.py` |
| Optional trained translator | `mayur/translator*.py`, `models/translator*` |
| Orchestration, output | `mayur/pipeline.py`, `jsonout.py`, `render_html.py`, `cli.py`, `schema/verse.schema.json` |

## Where it stands

| Layer | Result | Target |
|---|---|---|
| Word analysis, two sealed runs of 200 unseen verses | full analysis 95.8% and 94.9% | 95%: met, without margin |
| Rules produce the corpus's split / analysis at all | 99.5% / 99.6% | 100%: not met |
| Roles / heads on verse, whole pipeline | 75–81% / 59–74% | 90% / 85%: not met |
| English on plain prose | 45 of 46 equal to hand-written (rules tuned on them) | — |
| English on verse | understandable on simple verses, stiff, wrong where roles are wrong | not met |
| Trained translator | worse than the rule-built line; off by default | not met |

## Rules for measuring (do not break these)

- **Sealed pool.** `mayur/dcs.py` refuses to read it. Only `scripts/sample_test.py` may draw from
  it, each draw is logged in `eval/sealed_ledger.json`, and no verse is tested twice. Two draws of
  200 are used. Do not re-run them after changing code: draw a fresh sample.
- **Held out, never tuned on:** Rāmāyaṇa Bāla 1.1–20 and the `*_B.json` reference files.
- **Validation only:** `eval/review/claude/dev_pool_061_100_V.json`. Use it to accept or reject a
  finished rule (aggregate numbers, ablation by switching a rule off). Do not read its items to
  write a rule.
- **Tuning sets:** `ramayana_bala1_041_079_A.json`, `dev_pool_001_060_A.json`, the development pool,
  `eval/samples/dev300b.json`.
- A rule that lowers the validation set is taken out again, however reasonable it looks. Two were
  removed this way (an apposition-list rule; two same-gender accusative nouns as two objects).
- Every number in the README comes from a script named beside it. Re-take all of them after any
  change to `mayur/`; the last full pass is described under "Re-measuring" below.

## Re-measuring

```bash
python -m pytest -q
python eval/eval_dcs.py --sample eval/samples/dev300b.json --json eval/results/dev300b_rN.json > eval/results/dev300b_rN.txt
for f in ramayana_bala1_041_079_A dev_pool_001_060_A dev_pool_061_100_V; do
  python eval/eval_roles.py --claude eval/review/claude/$f.json            # whole pipeline
  python eval/eval_roles.py --claude eval/review/claude/$f.json --gold-words
  python eval/eval_compounds.py --claude eval/review/claude/$f.json --gold-words
done
python eval/eval_roles.py --claude eval/review/claude/ramayana_bala1_001_040_A.json --verses 1-20   # held out: read the total only
python eval/eval_everyday.py; python eval/eval_simple.py; python eval/eval_wellknown.py
python eval/eval_english.py --file dev_pool_001_060_A.json --mode gold      # file name only, no directory
mayur html --verses 1-20 --out docs/index.html
```

Do not edit files under `mayur/` while such a pass is running: each script starts a new process and
would load the half-edited code.

## What remains, in the order I would take it

1. **Sentence structure on verse** (the main gap). `python eval/eval_roles.py --claude <A file>
   --matrix` prints the confusion matrix and the most frequent wrong links. The weakest role is
   विधेय (predicate); heads on the mixed-book sets are the weakest number. Everyday verse lines are
   at 11 of 35 with every role and head right.
2. **The held-out drop.** The clause rules of commit `c65fc0c` raised every tuning and validation
   set and lowered Rāmāyaṇa 1.1–20 from 84.7% / 73.5% to 83.8% / 71.3% (roles / heads). Which rule
   costs it was not examined, to keep those verses unseen. A fresh held-out set would let it be
   looked at properly.
3. **The translator.** Either train `scripts/train_translator.py` on the whole Itihāsa corpus (it
   saw 6,749 of about 75,000 verses; building the data takes about 5,000 verses an hour on CPU), or
   train the adapter variant on flan-t5-small (`scripts/train_translator_t5.py`, written, never
   run). Keep it off by default until it beats the rule-built line on both the plain sentences and
   verse. IndicTrans2 could not be fetched without a Hugging Face login.
4. **English of verse.** Compound shapes without a rule keep a hyphen form; clause joining is crude
   (Gītā 2.47 is garbled).
5. **Court poetry** at word level (long compounds, rare words): below 90% on the few verses drawn.
6. **A human check** of the reference sets for roles, compounds and English. They were written by
   Claude, so those scores are against Claude's own judgement.

## Known wrong outputs

- `स मा पातु` → "Let him not protect". Grammar alone does not tell it from `त्वं मा गच्छ`; the
  tagger's choice stands (`mayur/particle_ma.py` says where the rules stop).
- `मृत्योर्मामृतं गमय` written joined is split `माम् ऋतम्` first; `मा अमृतम्` is among the kept readings.
- `युयुत्सवः` (Gītā 1.1) is taken as a name, not "eager to fight".
- `त्यक्तराज्यः रामः` is typed कर्मधारय, so the English keeps "Abandon-kingdom Rāma".
- `उत्तिष्ठ जाग्रत` reads `जाग्रत` as a vocative noun.
- One development verse (Mahābhārata, "नातो विशिष्टं लोकेषु …") is now split `अतस् अविशिष्टम्`; it was
  right before the last day's rules. Which rule moved it was not found; on the half-verse alone the
  right split still wins.

## Things that are easy to get wrong

- All Sanskrit in code and data is Devanagari; romanisation only inside `lipi.py` and `bridge.py`.
- `mayur/annotations/gloss_draft.json` has one entry per line. Edit it as text; `json.dump` reformats
  the whole file.
- A causative's `Morph.root` is its stem (गामि), not the base root. Use `bridge.base_root(m)` and
  `bridge.is_causative(m)`.
- Labelled epic forms have `source == "arsha"` and quality 1, so the tagger passes over them when
  any ordinary analysis exists. `one_verb.py` shows the one case where a labelled verb is preferred.
- Monier-Williams is never committed and not used by the gloss lookup. No gloss or translation was
  copied from valmiki.iitk.ac.in or valmikiramayan.net.
- Never commit downloaded corpora. The translator weights (15 MB) are committed and are derived from
  the Itihāsa corpus (Apache-2.0); see `NOTICE`.
- Helper agents work in git worktrees under `.claude/worktrees/` (ignored). A new worktree starts
  from `master`; reset it to the working branch first.
