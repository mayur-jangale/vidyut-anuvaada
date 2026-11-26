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
| Split | A lattice of **all** rule-valid splits of a line. Hard rules cut impossible paths (a merged vowel cannot be followed by a written space; particles, absolutives and finite verbs do not end a compound; a stem in -न् is not a member). | `mayur/segmenter.py` |
| Words | vidyut-kosha lookup plus forward generation: prefixed verbs and participles, feminines, closed paradigms, common spellings (पत्र for पत्त्र). | `mayur/lexicon*.py` |
| Choice of split | A trained ranker picks among the valid splits only. | `mayur/decoder.py` |
| Choice of analysis | A trained tagger picks among the lexicon's analyses only. | `mayur/tagger.py` |
| Proof gate | The chosen words must re-join to the input by sandhi, and each word must be re-derived by vidyut-prakriya; otherwise the verse is `unverified` and the reason is given per word. A word whose stem no dictionary lists is never verified. | `mayur/proof.py`, `mayur/lexicon.py` |
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

### Word level (development sample: 300 random verses from 13 books, `eval/samples/dev300b.json`)

`python eval/eval_dcs.py --sample eval/samples/dev300b.json` — full output in `eval/results/`.

| Measure | Result |
|---|---|
| Padas identified (a compound is one pada, compared as written) | F1 0.966 (P 97.0%, R 96.2%) |
| Words identified, compound members counted separately | F1 0.947 |
| Half-verses with every pada right | 559/683 = 81.8% |
| Lemma (aligned words) | 3740/3804 = 98.3% |
| All grammar features | 3548/3804 = 93.3% (case 95.3%, gender 95.4%, number 98.1%) |
| Full analysis: lemma and every feature | 3525/3804 = 92.7% |
| Words proof-verified by vidyut-prakriya | 4598/4717 = 97.5% |
| Verses with status `verified` | 206/300 = 68.7% |

**Sealed test:** not yet run for the current models. The target is 95% for padas identified and for full
analysis; the development numbers above say the first is met and the second is not yet.

The comparison conventions are documented and tested in `eval/eval_match.py` and `mayur/ud.py`
(for example: the corpus tags glued prefixes such as स-, सु-, अ- as free words, and reconstructs
some forms the text does not have). Compound members are scored separately because the corpus
itself is not consistent about splitting lexicalised compounds.

### Everyday Sanskrit (regression sets written by hand for this project)

| Set | Result | Command |
|---|---|---|
| 44 well-known lines (subhāṣitas, mottoes, simple prose): pada split | 41/44 chosen split right; 44/44 right split among the kept readings | `python eval/eval_wellknown.py` |
| 40 plain prose sentences: roles and heads of the listed words | 39/40 sentences, 104/106 words | `python eval/eval_simple.py` |
| The same 40 sentences: readable English equal to the hand-written one (articles ignored) | 26/40 | `python eval/eval_simple.py` |
| `श्वेतो धावति` | both `श्वेतः धावति` and `श्वा इतः धावति` are returned, each proof-verified | `mayur analyze "श्वेतो धावति"` |

### Sentence structure and compounds on verse (reference annotated by Claude, not human-verified)

139 verses (Rāmāyaṇa Bāla 1.1–79 and 60 verses from 13 other books) carry roles, heads, compound
types, prose order and English written by Claude on top of the corpus's word split
(`eval/review/claude/`). Verses 1–20 and a second annotation pass were kept out of tuning.

| Measure (development verses) | Rāmāyaṇa 1.41–79 | 60 verses, other books |
|---|---|---|
| Role right, whole pipeline from raw text | 76.4% | 72.5% |
| Head right, whole pipeline | 66.0% | 57.2% |
| Role right when the corpus's split and grammar are given | 78.7% | 74.3% |
| Compound type right when the split is given | 98.3% | 84.7% |
| Agreement of two annotation passes with each other (roles / heads) | 98% / 99% | 89% / 87% |

`python eval/eval_roles.py --claude <file> [--gold-words]`, `python eval/eval_compounds.py --claude <file> [--gold-words]`.

## Known limits

- **Sentence structure on verse is the weakest layer** (numbers above). Plain prose is handled
  well; long verse sentences with several clauses, relative clauses and ellipsis are not.
- **The English is rough.** It is built by rule from the analysis; it is right on plain
  sentences about half the time word for word, and stiff or wrong on complex verse.
- Compounds are not derived by vidyut's Python API; our own rule chain covers the type rule,
  the elision of case endings (2.4.71), sandhi and the final inflection.
- Words vidyut lists but cannot derive (the enclitics मे, ते; महा- in compounds) leave a verse
  `unverified`, with the reason; so does any word unknown to the dictionary.
- The reference sets for roles, compounds and English were annotated by Claude, not by a
  human Sanskritist; two annotation passes agree on 89–98% of roles.
- No Vedic rules, no accent.
- The trained rankers learn the conventions of one corpus (DCS). Where that corpus is
  inconsistent (whether a lexicalised compound is split), so is the score.

## Data and licences

- Code: Apache-2.0 (`LICENSE`). Own annotations in `mayur/annotations/` and
  `eval/review/claude/`, `eval/samples/wellknown.json`, `eval/samples/simple_sentences.json`:
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
