# Roadmap: from analysing words to interpreting Sanskrit

The Aṣṭādhyāyī is a generator: it goes from meaning (who does what to whom) to the
sentence. This project interprets by finding the meaning structures whose **forward**
derivation reproduces the text. Each layer below rests on a section of Pāṇini's rules;
sources outside the grammar (dictionary, corpus statistics, trained rankers) only choose
among readings the rules already allow.

| # | Milestone | Rules it rests on | Done when | State |
|---|---|---|---|---|
| 1 | Reliable analysis: split, lemma, grammar on any book | Sandhi 6.1, 8.2–8.4; word formation 3.1–7.4 (via vidyut) | ≥ 95% word-level on fresh sealed samples; no genre below 90% | In progress |
| 2 | Sentence structure: roles, clauses, anvaya | Kāraka definitions 1.4.23–55; case assignment 2.3.1–73; 3.4.69; 1.4.105–108 | ≥ 90% of role links correct on a checked set; each link cites its rules | Rule engine in progress; gold data being located |
| 3 | Meaning of words: derived sense by rule, sense in context, compounds by rule | Suffix-sense rules in 3.x, 4.x, 5.x; compounds 2.1–2.2 | ≥ 85% sense agreement with corpus sense tags; compound types scored on a checked set | In progress |
| 4 | Choosing the intended reading | Outside the grammar: compatibility of meanings, reference of तद्/यद्, supplied words | Intended reading ranked first on a set of known ambiguous verses | Not started (needs 2 and 3) |
| 5 | Faithful, readable English | — (constrained rewording of the verified analysis) | Code checks that grammar and alignment are unchanged; human rating of a sample | Rewording step in progress; needs an API key to run |
| 6 | Hard genres: court poetry, technical prose | Same rules; long compounds, deliberate double meanings shown as two readings | Per-genre scores at milestone-1 level | Not started |
| 7 | Vedic | Vedic rules (छन्दसि), accent | Split agrees with the traditional padapāṭha on a held-out sample | Not started |

## How accuracy is measured

- Gold: Digital Corpus of Sanskrit annotations (24 books fetched).
- Three disjoint sets of chapters: **train** (counts and model training), **dev pool**
  (tuning and error analysis), **sealed test** (never read by any training, tuning or
  audit code; each final test draws fresh random verses and logs them in
  `eval/sealed_ledger.json` so no verse is tested twice).
- Headline numbers are word-level: words identified (same boundaries and lexeme),
  lemma, and all grammar features. Comparison conventions are documented and tested in
  `mayur/ud.py` and `eval/eval_dcs.py`.

## What needs a person

- A Sanskrit reader to correct role and compound sheets (`scripts/export_review.py`)
  so milestones 2–4 can be measured against human judgement.
- A decision on whether words that vidyut lists but cannot derive (enclitics such as मे)
  may count as verified when our own sūtra-cited derivation is shown.
- An API key for the optional rewording step.
