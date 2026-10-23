# Item audit: layering and complexity (A2 and B1)

Method: every built-in item of the topics that already exist was read (A2: 118 items, B1 tenses and passives in detail) and
measured against the coursebook references (see `NOTES-picker-and-levels.md`). Nothing built-in was changed or retired,
so every learner's past results stay exactly as they are. New questions are added as drafts (CSV files in `docs/task-drafts/`).

## Standard used for the two layers
| | A2 (A2.1 / A2.2) | B1 (B1.1 / B1.2) |
|---|---|---|
| Sentence | one clause, about 5-9 words | two clauses or a longer clause, about 10-16 words |
| Vocabulary | everyday: home, shopping, routines | wider: work, news, plans, opinions |
| Forms | negatives, questions and short answers are already A2 | same forms, with the tense chosen by meaning, not by a clue word |
| Question types | choose, gap with the verb in brackets, put in order, match, correct the mistake | plus rewrite, join two sentences, which sentence is NOT correct, difference in meaning |
| Wrong options test | the form (*cans*, *to go*) | the meaning or the tense choice |

## Findings
1. **Layering by thinking level is good, layering by sentence is weak.** Every topic has the same template (form, meaning, gap, NOT correct, choose, write)
   at every level, so A2 and B1 differ in thinking level but the sentences are almost the same length (A2 about 9-10 words, B1 about 11-12).
2. **34 B1 items are A2-sized** (short, one clause, a clue word): `pc-B11-1a pc-B11-3b pa-B11-1a pa-B12-3a pp-B11-1a pp-B11-3a pp-B12-1a pp-B12-3a
   ppf-B12-1a ppf-B12-3a fu-B11-1a-r2 fu-B11-3a fu-B11-3b fu-B12-1a psp-B11-1a psp-B11-3a psp-B12-1a psp-B12-3a pasp-B11-1a pasp-B11-3a pasp-B11-3b
   pasp-B12-1a pcp-B12-1a pcp-B12-3a pcp-B12-3b ppp-B11-1a ppp-B12-1a ppp-B12-3a fup-B11-1a fup-B12-1a cf-B11-3a cs-B11-3b rs-B12-3a ip-B11-1a`.
   They are fine as a warm-up (the first three tasks of a session are the easiest ones), but they should not be the bulk of B1.
   Decision for Inga: keep them, or retire them once the new B1 questions are approved (retiring a built-in task is a code change, not a Tasks-tab action).
3. **Too few items per topic.** 7 to 17 items per topic and level means the same sentences return after two or three sessions.
4. **The first three tasks at the chosen level are always Bloom 1, 2, 3.** For B1 these are the A2-sized recognition items above.
5. **The instruction lines repeat** ("Which sentence is NOT correct?", "Choose the correct option", "Put the words in order") and made the duplicate checker
   reject a second task with the same text. New tasks therefore carry a context ("At work:", "In the factory:").
6. **Modal verbs card was wrong about must / have to** (corrected: both mean *necessary*; the real contrast is *mustn't* versus *don't have to*,
   and *had to / will have to*).
7. **Passive voice is placed at A2.2 in the bank**, as Inga decided from the Pre-Intermediate book; the A2+ book has no passive and the B1 book teaches it at B1.
   Left as is.

## What was added (drafts, not live)
| Topic | A2 now | A2 after | B1 now | B1 after |
|---|---|---|---|---|
| Present simple | 17 | 37 | 7 | 11 |
| Present continuous | 17 | 33 | 7 | 11 |
| Past simple | 17 | 34 | 14 | 19 |
| Past continuous | 9 | 18 | 15 | 19 |
| Present perfect | 9 | 19 | 15 | 19 |
| Present perfect continuous | 0 | 0 | 16 | 19 |
| Past perfect | 0 | 0 | 9 | 12 |
| Future: will, going to, present continuous | 17 | 30 | 16 | 20 |
| Present simple passive | 9 | 18 | 14 | 16 |
| Past simple passive | 9 | 18 | 15 | 17 |
| Present continuous passive | 0 | 0 | 9 | 11 |
| Present perfect passive | 0 | 0 | 15 | 17 |
| Future passive (will be done) | 0 | 0 | 15 | 17 |
| Modal verbs: can, should, must, have to | 0 | 36 | 0 | 25 |
| Comparison: -er, more, the most, as ... as | 0 | 26 | 0 | 21 |
| Zero conditional (if + present, present) | 7 | 14 | 6 | 8 |
| First conditional (if + present, will) | 10 | 18 | 16 | 19 |
| Second conditional (if + past, would) | 0 | 0 | 17 | 20 |
| Third conditional (if + had done, would have done) | 0 | 0 | 9 | 9 |
| Reported statements (tense changes) | 0 | 0 | 15 | 17 |
| Reported questions and requests | 0 | 0 | 10 | 12 |
| Indirect questions (Could you tell me where...) | 0 | 0 | 17 | 19 |

New topics: **Comparison** (A2 and B1) and **Modal verbs** (A2 and B1). Counts include approved drafts; A2 means A2.1 and A2.2 together.

B1 is still thin. The B1 reference also teaches these topics that the bank does not have: used to / would, be used to, articles, relative clauses,
time clauses, question tags, subject and object questions, the causative, -ing versus to, adjective and adverb order, so / such, more modals.
The next batches should add them, with about 30 to 40 questions per topic.
