# Roadmap: from analysing words to interpreting Sanskrit

The Aṣṭādhyāyī is a generator: it goes from meaning (who does what to whom) to the
sentence. This project interprets by finding the meaning structures whose **forward**
derivation reproduces the text. Each layer below rests on a section of Pāṇini's rules;
sources outside the grammar (dictionary, corpus statistics, trained rankers) only choose
among readings the rules already allow.

**Production runs offline: no language model and no API key.** Claude is used only during
development, as a checker and as an annotator of reference sets (labelled as such, not human-verified).

| # | Milestone | Rules it rests on | Done when | State |
|---|---|---|---|---|
| 1 | Reliable analysis: split, lemma, grammar on any book | Sandhi 6.1, 8.2–8.4; word formation 3.1–7.4 (via vidyut) | ≥ 95% word-level on fresh sealed samples; no genre below 90% | Sealed run 1 (200 never-seen verses, 16 books): padas identified F1 0.961, words identified F1 0.951, lemma 99.2%, full analysis 95.8% — the 95% target is met. Not met: court poetry (Kirātārjunīya, Ṛtusaṃhāra: 5 verses drawn) is below 90%. The rules produce the corpus's split for 99.5% of lines and its analysis for 99.6% of words on an untouched sample |
| 2 | Sentence structure: roles, clauses, anvaya | Kāraka definitions 1.4.23–55; case assignment 2.3.1–73; 3.4.69; 1.4.105–108 | ≥ 90% of roles and ≥ 85% of heads correct on a reference set; each link cites its rules | Rule engine built (49 rules, every link cited and forward-checked). Plain prose: 45 of 46 sentences with every listed role and head right. Verse, on the Claude-annotated dev sets: roles 74–80% (79–81% if विशेषण and विधेय are not told apart), heads 57–70%; two annotation passes agree with each other on 89–98% |
| 3 | Meaning of words: derived sense by rule, sense in context, compounds by rule | Suffix-sense rules in 3.x, 4.x, 5.x; compounds 2.1–2.2 | ≥ 85% sense agreement with corpus sense tags; compound types scored on a reference set | Derived meaning from the trace: built (82 suffix-sense rules). Sense in context: 72.8% on ambiguous words. Compound type by rule: 85–98% when the split is given, about half through the whole pipeline (split errors); -त्व/-ता labelled as taddhita words |
| 4 | Choosing the intended reading | Outside the grammar: compatibility of meanings, reference of तद्/यद्, supplied words | Intended reading ranked first on a set of known ambiguous verses | Not started (needs 2 and 3) |
| 5 | Faithful, readable English | — (fixed rewriting rules over the literal rendering; no language model) | Code checks that words, number, tense, negation and alignment are unchanged; rating of a sample | Rule-based; plain sentences: 32 of 46 equal to hand-written English (articles ignored). Verse output is stiff and often wrong where the sentence structure is wrong |
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

## Reference sets for sentence structure

No open treebank with kāraka roles and compound types could be used (the Hyderabad set forbids
redistribution). So 139 verses were annotated by Claude on top of the corpus's word split
(`eval/review/claude/`, tool: `scripts/annotate_tool.py`): Rāmāyaṇa Bāla 1.1–79 and 60 verses
from 13 other books; 30 of them were annotated a second time for an agreement check (roles
agree on 98% and 89% of words; both annotators are the same model, so this overstates
independence). These files say "Claude (LLM), not human-verified" in their header.

## What needs a person

- A Sanskrit reader to correct the role and compound reference files, so milestones 2–4 are
  measured against human judgement and not only against Claude's.
- A decision on whether words that vidyut lists but cannot derive (enclitics such as मे, the
  in-compound form महा) may count as verified when our own sūtra-cited derivation is shown.
  Today they do not.
