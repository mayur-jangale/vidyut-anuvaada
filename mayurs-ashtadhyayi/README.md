# मयूरस्य अष्टाध्यायी — Mayur's Ashtadhyayi

A verifiable Sanskrit interpreter. It takes compact Sanskrit text (sandhi-joined, compounded,
verse or prose) and returns, for each verse:

1. **पदच्छेद** – the sandhi split, with the sūtra numbers that license every junction
2. **समास** – compound breakdown: type decided by rule, vigraha, forward rule chain
3. **व्याकरण** – stem or root, case, number, gender, tense, person of every word
4. **अन्वय** – prose order, from kāraka links that each cite their rules
5. **पदार्थ** – word-by-word English gloss, and the sense the derivation itself gives
6. a **literal English translation** aligned word by word, and a **readable English** line

Every word carries its full derivation (prakriyā) by Pāṇini's rules, produced by
[vidyut](https://github.com/ambuda-org/vidyut). It runs **offline: no language model, no API
key, no network**. Everything is Devanagari inside; roman sound codes exist only in the two
files that call vidyut.

## How it works

The Aṣṭādhyāyī generates sentences from meaning. The interpreter never runs a rule backward:
it proposes analyses by lookup and forward generation, and keeps those whose forward derivation
reproduces the text.

| Step | What happens | Where |
|---|---|---|
| Sandhi | Forward rules, each with its sūtra number; a reverse index is built from their outcomes. | `mayur/sandhi.py` |
| Split | A lattice of **all** rule-valid splits of a line. Hard rules cut impossible paths (a merged vowel cannot be followed by a written space; particles, absolutives and finite verbs do not end a compound; a stem in -न् is not a member). A compound printed with spaces (रत्न भाजः) is read as one after a stem the corpus knows almost only as a member. | `mayur/segmenter.py` |
| Words | vidyut-kosha lookup plus forward generation: prefixed verbs and participles, denominatives (नमस्यति, पुत्रीयति), feminines, closed paradigms, stems from the corpus dictionary, common spellings (पत्र for पत्त्र). | `mayur/lexicon*.py` |
| Epic and usage forms | Forms the rules do not give are analysed and **labelled**, never forced: epic voice endings (त्यजामहे, शृणुष्व), second-class roots conjugated as first-class (अहनत्), upasarga + participle where the rule form differs (प्रदत्त for प्रत्त), ready-made participles (छन्न, क्षुब्ध). Each names the rule form; the word stays unverified. | `mayur/lexicon_more.py`, `lexicon_usage.py`, `lexicon_thematic.py` |
| Choice of split | A trained ranker picks among the valid splits only. | `mayur/decoder.py` |
| Choice of analysis | A trained tagger picks among the lexicon's analyses only. Where one spelling stands for two or three padas by sandhi (भीष्म उवाच: भीष्मः, भीष्मे or the vocative), it weighs all of them; the pada not taken is named in the notes. | `mayur/tagger*.py`, `mayur/siblings.py` |
| Proof gate | The chosen words must re-join to the input by sandhi, and each word must be re-derived by vidyut-prakriya; otherwise the verse is `unverified` and the reason is given per word. A word whose stem no dictionary lists is never verified. Two word classes are proved in two vidyut steps where the Python API cannot do it in one: passive present participles (क्रियमाण: the passive present, then शानच् by 3.2.124, 7.2.82) and neuter plurals in -ईनि as accusative (through the identical nominative, 7.1.20). | `mayur/proof.py`, `mayur/lexicon.py`, `mayur/lexicon_passive.py` |
| Compounds | Type by rule (2.1–2.2) with the deciding sūtra, vigraha from real inflected forms, rule chain. | `mayur/compounds.py`, `mayur/samasa*.py` |
| Sentence | Kāraka roles and heads; a link is kept only if the forward rule (role + what the verb form expresses → case) gives the word's actual case (1.4.23–55, 2.3, 3.4.67–72). | `mayur/vakya.py`, `mayur/karaka*.py` |
| Meaning | Dictionary gloss; sense in context; meaning read off the derivation (which suffix rule gives which sense). | `mayur/gloss.py`, `mayur/senses.py`, `mayur/artha.py` |
| English | A literal aligned rendering, then fixed rewriting rules with checks that no word, number, tense or negation changed. | `mayur/translate*.py`, `mayur/fluent*.py` |

Statistics (corpus counts, the two trained rankers) only **choose among readings the rules
allow**. Alternatives are kept with their scores and never dropped silently.

## Install and run

```bash
pip install -e ".[dev]"                 # add ".[neural]" for the optional torch-based ranker features
python scripts/fetch_data.py            # vidyut data + DCS corpus at a pinned revision; builds data/derived/
mayur analyze "श्वेतो धावति"              # JSON for one verse (Devanagari or IAST input)
mayur verse 1                           # Rāmāyaṇa, Bālakāṇḍa 1.1 from the bundled text
mayur html --verses 1-20 --out docs/index.html
python -m pytest                        # test suite
```

Plain ASCII input is refused, because romanisation without diacritics is ambiguous. The JSON
format is described by `schema/verse.schema.json`.

## Measured results

All numbers are measured by the scripts named; nothing is estimated. Gold: the annotations of
the Digital Corpus of Sanskrit (DCS), 24 books. Chapters are divided into **train** (model
training and counts), **dev pool** (tuning and error analysis) and a **sealed pool** that no
training, tuning or audit code may read (`mayur/dcs.py` refuses it); a final test draws fresh
random verses from the sealed pool and logs them in `eval/sealed_ledger.json`, so no verse is
tested twice.

### The formula part: do the rules produce the right reading at all?

`python scripts/coverage_rules.py --seed N` — no ranking involved. Each run takes 1,500 random
development lines and keeps those whose corpus words re-join to the text by sandhi (about 86%;
in the rest the corpus has reconstructed a form the text does not have, e.g. ते for तव).

| Sample of 1,500 lines | The corpus's split is one of the splits the rules produce | The corpus's lemma and features are among the lexicon's analyses |
|---|---|---|
| Seed 73: measured once, never looked at before | 1280/1286 = 99.5% | 8987/9027 = 99.6% |
| Six earlier samples, re-measured after their gaps were fixed | 99.5% to 99.8% | 99.5% to 99.8% |

Each earlier sample was also measured once before anyone looked at it; as the rules were completed
those first measurements read 97.0% / 98.7%, 99.2% / 99.0%, 99.5% / 99.4%, 99.2% / 99.5%,
99.5% / 99.5% and 99.3% / 99.6% (split / analysis).

What the untouched sample still misses (6 lines, 40 words): epic forms no rule here covers yet
(ब्रवीहि for ब्रूहि, संक्रामयामास), words written with the sign ॐ, a few stems unknown to both
dictionaries, and words where the corpus's own lemma or tag is the odd one (हृदि as accusative
plural). This is the part that is "all formula", and its target is 100%. Which of several valid
readings is meant is not decided by the rules; that is the next table.

### Word level, first choice

`python eval/eval_dcs.py --sample <file>` — full output in `eval/results/`.

| Measure | Sealed run 1: 200 unseen verses | Sealed run 2: 200 more unseen verses | Development: 300 verses |
|---|---|---|---|
| Padas identified (a compound is one pada, compared as written) | F1 0.961 | F1 0.968 | F1 0.975 |
| Words identified, compound members counted separately | F1 0.951 | F1 0.957 | F1 0.959 |
| Lemma (aligned words) | 2422/2442 = 99.2% | 2486/2510 = 99.0% | 3878/3909 = 99.2% |
| All grammar features | 2344/2442 = 96.0% | 2389/2510 = 95.2% | 3717/3909 = 95.1% |
| Full analysis: lemma and every feature | 2340/2442 = 95.8% | 2381/2510 = 94.9% | 3706/3909 = 94.8% |
| End to end: the word found and fully analysed, of all corpus words | 2760/3066 = 90.0% | 2749/3042 = 90.4% | 4249/4735 = 89.7% |
| Words proof-verified | 2949/3046 = 96.8% | 3017/3036 = 99.4% | 4642/4681 = 99.2% |
| Verses with status `verified` | 123/200 = 61.5% | 182/200 = 91.0% | 267/300 = 89.0% |

Each sealed sample was drawn by `python scripts/sample_test.py --pool sealed_test --n 200 --label runN`
and evaluated once (`eval/results/sealed_run1.txt`, `sealed_run2.txt`); the verses are logged in
`eval/sealed_ledger.json` and are never drawn again. Run 1 followed the end of word-level tuning. Run 2
followed the contextual proofs (below) and the sentence rules; the word-level code was the same, so the
difference between the two runs in the first six rows is sampling. The target was 95% for padas
identified, words identified and full analysis. Padas and words meet it on both runs. Full analysis
is 95.8% and 94.9%, together 4721/4952 = 95.3%: at the target, with no margin. The end-to-end figure
multiplies the two steps: a word counts only if it was both found and fully analysed.

The jump in verified verses between the runs comes from proving three word forms that a rule gives
only in context, each with its condition checked on the reading: the enclitics मे, ते, नः … (8.1.20–23,
never first in the half-verse), स / एष without its ending (6.1.132 before a consonant), and महा- in a
कर्मधारय or बहुव्रीहि (6.3.46). Before, any verse with one of them was `unverified`.

By book on sealed run 1 (words identified F1): Bhāgavatapurāṇa, Buddhacarita, Manusmṛti and
Kathāsaritsāgara 0.95 to 0.96; Mahābhārata (97 verses) 0.94; Rāmāyaṇa 0.90; Liṅgapurāṇa and
Ṛtusaṃhāra 0.88; Kirātārjunīya (2 verses) 0.68. Court poetry is the weakest genre. With 1 to 18
verses per book outside the Mahābhārata, the per-book numbers are indications only.

What the word-level errors are (development sample, `python scripts/error_words.py`): of the words
with a wrong feature, the largest groups are gender where the masculine and neuter forms are the same
(the corpus itself tags the neuter इन्द्रिय as masculine 375 times and as neuter 359 times), nominative against accusative of neuters
(which only the sentence decides), and a participle against the adjective it has become (भूत).

The comparison conventions are documented and tested in `eval/eval_match.py` and `mayur/ud.py`
(for example: the corpus tags glued prefixes such as स-, सु-, अ- as free words, reconstructs
some forms the text does not have, cites causatives now under the root and now under the stem in
-अय्, and cites a participle now under its root and now under its own stem). Compound members are
scored separately because the corpus itself is not consistent about splitting lexicalised compounds.

### Everyday Sanskrit (regression sets written by hand for this project)

| Set | Result | Command |
|---|---|---|
| 44 well-known lines (subhāṣitas, mottoes, simple prose): pada split | 42/44 chosen split right; 44/44 right split among the kept readings | `python eval/eval_wellknown.py` |
| 46 plain prose sentences: roles and heads of the listed words | 45/46 sentences, 119/121 words | `python eval/eval_simple.py` |
| The same 46 sentences: readable English equal to the hand-written one (articles ignored). The English rules were tuned on these sentences, so this is not an independent score | 45/46 | `python eval/eval_simple.py` |
| 120 everyday lines the rules were not tuned on (40 prose sentences, 40 well-known verse lines, 40 sandhi-heavy lines; written by Claude, not human-verified): split right as first choice / right split among the kept readings | 110/120, 118/120 | `python eval/eval_everyday.py` |
| The same 120: every lemma right / every grammar tag right (per line) | 97/120, 92/120 | `python eval/eval_everyday.py` |
| The same: every listed role and head right (prose 26/40, verse lines 7/35, sandhi-heavy 17/34) | 50/109 | `python eval/eval_everyday.py` |
| The same: status `verified` | 116/120 | `python eval/eval_everyday.py` |
| `श्वेतो धावति` | both `श्वेतः धावति` and `श्वा इतः धावति` are returned, each proof-verified | `mayur analyze "श्वेतो धावति"` |

### Sentence structure and compounds on verse (reference annotated by Claude, not human-verified)

139 verses (Rāmāyaṇa Bāla 1.1–79 and 60 verses from 13 other books) carry roles, heads, compound
types, prose order and English written by Claude on top of the corpus's word split
(`eval/review/claude/`). Verses 1–20 and a second annotation pass were kept out of tuning.

| Measure (development verses) | Rāmāyaṇa 1.41–79 | 60 verses, other books |
|---|---|---|
| Role right, whole pipeline from raw text | 345/434 = 79.5% | 570/764 = 74.6% |
| Head right, whole pipeline | 305/434 = 70.3% | 447/764 = 58.5% |
| Role right when the corpus's split and grammar are given | 362/451 = 80.3% | 598/795 = 75.2% |
| Head right when the corpus's split and grammar are given | 332/451 = 73.6% | 509/795 = 64.0% |
| Compound type right when the split is given | 59/60 = 98.3% | 94/111 = 84.7% |
| Agreement of two annotation passes with each other (roles / heads) | 98% / 99% | 89% / 87% |

On Rāmāyaṇa 1.1–20, which no rule was tuned on: roles 182/215 = 84.7% and heads 158/215 = 73.5% for the
whole pipeline (`--verses 1-20` of `ramayana_bala1_001_040_A.json`).

`python eval/eval_roles.py --claude <file> [--gold-words]`, `python eval/eval_compounds.py --claude <file> [--gold-words]`.

## Known limits

- **Sentence structure on verse is the weakest layer** (numbers above). Plain prose is handled
  well; long verse sentences with several clauses, relative clauses and ellipsis are not.
- **The English is rough.** It is built by rule from the analysis; it is right on the plain sentences
  its rules were tuned on, and stiff or wrong on complex verse, where it inherits every wrong role.
- **Court poetry** (long compounds, rare words) is the weakest genre at word level.
- **Epic and usage forms** are analysed only where a rule here covers them (see the table above);
  others stay unknown words, e.g. ब्रवीहि for ब्रूहि.
- A compound printed with spaces is recognised only after a stem the corpus knows almost solely as
  a compound member; `वेद फलम्` stays two words.
- Compounds are not derived by vidyut's Python API; our own rule chain covers the type rule,
  the elision of case endings (2.4.71), sandhi and the final inflection.
- A verse is `unverified` when one word is: a word unknown to the dictionary, an epic form that is
  only labelled, an enclitic standing first in its half-verse, or a strong form of महत् (महान्), which
  vidyut lists but does not derive.
- The reference sets for roles, compounds and English were annotated by Claude, not by a
  human Sanskritist; two annotation passes agree on 89–98% of roles.
- No Vedic rules, no accent.
- The trained rankers learn the conventions of one corpus (DCS). Where that corpus is
  inconsistent (whether a lexicalised compound is split), so is the score.

## Data and licences

- Code: Apache-2.0 (`LICENSE`). Own annotations in `mayur/annotations/` and
  `eval/review/claude/`, `eval/samples/wellknown.json`, `eval/samples/simple_sentences.json`,
  `eval/samples/everyday_120.json`:
  CC BY-SA 4.0. The gloss draft table and the reference annotations were written by Claude
  (an LLM) and are labelled so; they are not human-verified.
- vidyut (Ambuda): MIT; its data is downloaded by `scripts/fetch_data.py`.
- Digital Corpus of Sanskrit (Oliver Hellwig): CC BY 4.0. Bundled excerpts and trained model
  files derived from it carry that attribution; all other tables are built locally.
- UD Sanskrit treebanks (UFAL, Vedic): CC BY-SA 4.0, fetched by script for evaluation only.
- Monier-Williams (Cologne): licence unclear; optional (`fetch_data.py --with-mw`), local only,
  never committed, not used by the gloss lookup.
- No gloss or translation was copied from valmiki.iitk.ac.in or valmikiramayan.net.

See `NOTICE` for full credits and `docs/ROADMAP.md` for the milestones.
