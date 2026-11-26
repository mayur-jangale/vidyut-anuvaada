# मयूरस्य अष्टाध्यायी — Mayur's Ashtadhyayi

A verifiable Sanskrit interpreter. It takes compact Sanskrit verse (sandhi-joined, compounded,
in verse order) and returns, for each verse:

1. **पदच्छेद** – the sandhi split, with the sūtra numbers that license every junction
2. **समास** – compound breakdown with a (heuristic) type and vigraha
3. **व्याकरण** – stem or root, case, number, gender, tense, person of every word
4. **अन्वय** – prose order
5. **पदार्थ** – word-by-word English gloss
6. a **literal English translation**, aligned word by word to the Sanskrit

Every word carries the full derivation (prakriyā) by Pāṇini's rules, produced by
[vidyut](https://github.com/ambuda-org/vidyut). First target: Vālmīki Rāmāyaṇa.

## How it works

| Step | What happens | Where |
|---|---|---|
| Script | Everything is Devanagari. Sounds are handled as varṇas (`क्`, `अ`, `स्`). Roman codes exist only in the two files that call vidyut. | `mayur/lipi.py`, `mayur/bridge.py` |
| Sandhi | Forward sandhi rules, each with its sūtra number. | `mayur/sandhi.py` |
| Split | A lattice of **all** valid splits; a split is valid only if its words re-join to the text by the forward rules. Ranked by corpus counts. | `mayur/segmenter.py` |
| Words | Lookup in vidyut-kosha, plus forward generation (upasarga verbs, unlisted nominals). Sūtras are never run backward. | `mayur/lexicon.py` |
| Proof gate | The chosen words must re-join to the input exactly and each word must be re-derived by vidyut-prakriya; otherwise the verse is marked `unverified`. | `mayur/proof.py` |
| Reading | Śābdabodha tests in code: ākāṅkṣā (connection, agreement), yogyatā, sannidhi, plus corpus frequency. Alternatives are kept with scores. | `mayur/shabdabodha.py` |
| Anvaya | By rule from the kāraka links: kartā group, others, karma group, verb. | `mayur/anvaya.py` |
| English | Dictionary gloss, then a template sentence. No language model is used. | `mayur/gloss.py`, `mayur/translate.py` |

The rules decide what is valid, so the same code runs on any Sanskrit text. The Rāmāyaṇa
corpus is used only to rank readings that are equally valid.

## Install and run

```bash
pip install -e ".[dev]"
python scripts/fetch_data.py            # vidyut data + DCS corpus files; builds data/derived/
mayur analyze "श्वेतो धावति"              # JSON for one verse (Devanagari or IAST input)
mayur verse 1                           # Rāmāyaṇa, Bālakāṇḍa 1.1 from the bundled text
mayur html --verses 1-20 --out docs/index.html
python -m pytest                        # test suite
python eval/eval_dcs.py --verses 1-20   # measured numbers against the DCS gold
```

Plain ASCII input is refused, because romanisation without diacritics is ambiguous.
The JSON format is described by `schema/verse.schema.json`. A rendered page for
Bālakāṇḍa 1.1–20 is in `docs/index.html`.

## Measured results

Measured with `eval/eval_dcs.py` against the Digital Corpus of Sanskrit (DCS) annotation, on verses
1–20 of each chapter. The input is the compact text; the evaluation chapter of the Rāmāyaṇa is held
out of every frequency table, and the Kumārasaṃbhava is not used for the tables at all (verses 21–60
of its first chapter were used to tune ranking weights). Full output: `eval/results/`.

| Measure | Rāmāyaṇa, Bāla 1.1–20 | Kumārasaṃbhava 1.1–20 (other book) |
|---|---|---|
| Half-verses split exactly as DCS | 28/41 (68.3%) | 15/40 (37.5%) |
| Half-verses with the same words (lemma match) | 30/41 (73.2%) | 17/40 (42.5%) |
| Verses split exactly | 10/20 | 4/20 |
| DCS split among the kept readings | 14/20 | 5/20 |
| Words: precision / recall / F1 | 95.1% / 91.5% / 0.933 | 83.9% / 86.8% / 0.853 |
| Lemma correct (aligned words) | 201/211 (95.3%) | 173/195 (88.7%) |
| All grammar features correct (aligned words) | 200/211 (94.8%) | 169/195 (86.7%) |
| Words proof-verified by vidyut-prakriya | 282/284 (99.3%) | 352/353 (99.7%) |
| Verses with status `verified` | 18/20 | 18/20 |

Most split differences are compounds that the dictionary lists as one word and DCS divides
(महोरस्कः / महा-उरस्कः), or forms DCS reconstructs differently from the text (मम for मे).
The test sentence `श्वेतो धावति` returns both `श्वेतः धावति` and `श्वा इतः धावति`, each proof-verified.

## Known limits

- Compound types and vigrahas are heuristics. vidyut's Python API has no samāsa derivation,
  so a compound is proved member by member, not as a whole.
- Yogyatā (semantic compatibility) is only a few structural checks.
- The English is a literal template rendering, not idiomatic prose.
- Words that vidyut lists but cannot derive (for example the enclitics मे, ते) leave a verse
  `unverified`; the reason is given per word.
- Only the Rāmāyaṇa feeds the frequency tables; ranking is weaker on other genres.

## Data and licences

- Code: Apache-2.0 (`LICENSE`). Own annotations in `mayur/annotations/`: CC BY-SA 4.0.
- vidyut (Ambuda): MIT; its data is downloaded by `scripts/fetch_data.py`.
- Digital Corpus of Sanskrit (Oliver Hellwig): CC BY 4.0. `mayur/gold/ramayana_bala_1.json`
  is an excerpt converted to Devanagari; all other DCS-derived tables are built locally.
- Monier-Williams (Cologne): licence unclear; optional (`fetch_data.py --with-mw`), local only,
  never committed. It is not used by the current gloss lookup.
- No gloss or translation was copied from valmiki.iitk.ac.in or valmikiramayan.net.

See `NOTICE` for full credits.
