# Notes: practice picker and levels (not built yet)

Status: agreed with Inga in chat, **nothing of this is built**. Build only when she says so.

## Picker layout (her suggestion)
1. **Level** first: A1, A2, B1, B2, C1, C2, all shown to every learner (multi-select, e.g. A2 + B1).
   - A1 and C2 are **greyed out** until they have questions.
   - Learners may pick any level; no locking by their estimated level.
2. **Topics**: only topics that have questions at the chosen level(s). A2 shows basic grammar, reported speech only from B1/B2, and so on.
3. **Number of questions**: rename "tasks" to **questions** everywhere learners see it (picker "10 tasks" etc.). Teacher tab "Tasks" could become "Add questions".
4. **Start.**
- **No topic ticked**: a random mix of topics, all suitable for the chosen level(s), as many questions as selected.
- Full levels only (A2, B1, B2, C1). Questions labelled A2.1/A2.2 stay in the bank but are grouped under A2, so one topic at A2 serves easier and harder cases (same for B1.1/B1.2 and so on). Learners never see the half-levels.
- Same topic, different depth by level: A2 = basic forms, B2/C1 = advanced rules for the same grammar. Needs a rule card per level.

## Writing tasks
- Change "Write two sentences." to **"Write one sentence."** (65 writing tasks; most already ask for one). Check each prompt still makes sense. The two-word minimum check stays.

## Technical sketch (for later)
- `session/start`: accept `levels` (full levels) and allow empty `skills` = mix. Engine keeps `state.levels` (the half-levels allowed) and `pickNext` filters items to them instead of the +/-1 window. Start ability = lowest allowed half-level BASE + 0.3, adapts within the allowed set.
- Keep the old path (single level, "Surprise me", placement) working.
- `Content::liveMeta()` should report which full levels each topic really has questions in.
- Update tests: menu, topics_sound, e2e, tasks, bank_update.

## Level reference material
- Inga pasted a general CEFR explainer (A1 to C2 can-do statements, from a commercial blog). Useful only for **general** level descriptions; it has **no grammar** per level.
- To label levels and write standard rule cards I need a grammar syllabus per level: course-book grammar contents pages (unit lists with level) or the Cambridge English Grammar Profile. Ask Inga for pages per topic, starting with the topics she wants standardised first (present/past tenses, modals).
- Plan once she sends them: audit every task's level against the source and list mismatches (change nothing without her word); write per-level rule cards; write a "can do" list per topic per level; draft new questions for her to approve.
- Current bank spread: A2 121, B1 257, B2 68, C1 44 (no A1, no C2). Levels were labelled by Claude, not from a reference.

## Reference book received: "Grammar reference, Pre-Intermediate" (22 pp, book pp. 166-187, units 1-16)
Format of every entry: **Use**, **Form**, example sentences with the key words in bold, **Did you know?**, **Common mistakes** (wrong sentence crossed out), then exercises (choose the option, find the incorrect sentences, complete with own ideas). The book does not print a CEFR label; "Pre-Intermediate" is roughly A2+/B1. Use it as the A2/B1 reference, and ask for the Intermediate and Upper-Intermediate books for B2/C1.

Topics in the book, with how they relate to the bank:
- Already in the bank: present simple and continuous (1A, state verbs list), zero conditional (1C), past simple (2A), past continuous with past simple (3B), present perfect (4A, also "present perfect or past simple", gone/been), future with going to, present continuous, will (5A, 7C), first conditional (8A), reported statements and questions (12C), present perfect continuous (13C, for/since), passives (11C), past perfect (11B), second conditional (15C), modals have to / don't have to / can / can't (7B), had to / didn't have to / could / couldn't (8C), should / ought to / why don't you (9A), must / mustn't (14B).
- **Not in the bank yet**: comparatives (2C) and superlatives (5B); quantifiers many / much / a few / a little / some / any (3C); too / not enough (4B); be thinking of / might for plans (5A); question formation with auxiliaries (6A); both / neither / all / none (6C); imperatives and if + imperative (9C); used to (10B, Inga wants it as its own topic); time clauses when / as soon as / until (10C); yet / already / just / still (12A); be supposed to (13A); defining relative clauses (14A); time phrases with tenses (15A); articles (16B); verb patterns -ing vs to (16C).

Findings to act on when we build:
1. **Must vs have to.** The book says they "have a similar meaning and can often be used for the same situation"; the real contrast is **mustn't (not allowed) vs don't have to (not necessary)**, and the past/future (**had to**, must has none). It also adds **be allowed to** and informal **have got to**. This is different from the card I wrote ("must = speaker's feeling, have to = from outside"). Revise the Modal verbs card and the two new tasks I added to match the book, and drop the "personal feeling" wording.
2. **Rule-card style**: copy the book's habit of a short "Common mistakes" line (e.g. "You should eat, NOT You should to eat"; "enough goes after an adjective, before a noun") and "Did you know?" notes. The app's rule cards could get an optional mistakes line.
3. **Task types to add**: "which sentences are incorrect, correct them" (our check can do one-sentence answers), "match the first and second halves" (match type exists), rewrite with a given word.
4. Level labelling: place book units into our full levels only after Inga confirms; suggested start: units 1-9 A2, 10-16 B1, to be checked.

## Decisions and plan (Inga, latest)
- Labels stay: the Pre-Intermediate book maps to **A2.1 = units 1-9, A2.2 = units 10-16**. Learners see only A2 (and B1 ...). Open point: unit 11 has past perfect and passives, which the bank places at B1; decide per topic.
- Layer names to show next to the CEFR code: A1 Elementary, A2 Pre-intermediate, B1 Intermediate, B2 Upper-intermediate, C1 Advanced, C2 Proficient. Beginners (level 0) are skipped.
- **Priority: build B1 as completely as possible** (most common level; many topics are reused at A2 and B2).
- How layers differ for one topic: (1) form complexity, (2) task type / thinking level, (3) context, (4) rule card depth, (5) what the wrong options test.
- More reference material wanted: Intermediate (B1) book first; then Upper-Intermediate (B2), Elementary (A1), Advanced (C1). Use books as a syllabus and rule guide; write our own sentences, never copy their text or exercises.
- Proposed library: one spec sheet per topic (`docs/grammar-library/<topic>.md`) with can-do per layer, forms, uses, common mistakes, task types per layer; cards and questions are written from it.

## Correction (Inga): what really separates A2 from B1
- Negatives, questions and short answers belong to **A2 as well**; they are learned before B1, so they are not a B1 marker. Remove that from the layer differences above.
- The difference is mainly **sentence length** (short single clauses at A2, longer and combined sentences at B1) and **vocabulary choice** (everyday words at A2, wider and more abstract words at B1). The other differences (task type, context, rule card depth, what the wrong options test) stay open for discussion.
- Inga will send reference pages from the **Elementary** and **Intermediate** books; decisions on layers are to be checked against them before anything is built.

## Reference book received: "A2 Grammar" (Elementary-style, 32 pp, units 1-8, each unit = 3 grammar pages + one "How to ..." speaking page)
Layout per page: REFERENCE (tables with subject / auxiliary / infinitive / object columns, short answers, NOT wrong examples) and PRACTICE (put words in order, correct the mistake (some sentences are correct), complete the conversation with words from a box, choose the correct word, use prompts to write sentences or questions, match with pictures).
Contents: 1A present simple I/you/we/they, 1B he/she/it (spelling -s/-es/-ies, does/doesn't, short answers), 1C suggestions, 1D possessive 's, 2A countable/uncountable a/an/some/any, 2B frequency adverbs, 2C ordering in a restaurant, 2D like/hate/love + -ing, 3A this/that/these/those, 3B have got, 3C invitations and offers, 3D there is/are, 4A was/were, 4B how much/many/how + adjective, 4C shops, 4D should/shouldn't and imperatives, 5A past simple regular (spelling, did/didn't, yes/no), 5B irregular past + wh-questions + time phrases, 5C apologising, 5D adjectives and modifiers (really/very/too/quite/a bit), 6A present continuous (state verbs), 6B comparatives, 6C directions, 6D prepositions of movement, 7A articles, 7B present simple vs continuous, 7C phoning, 7D verbs + to infinitive, 8A superlatives, 8B be going to, 8C hotel requests and offers (I'll), 8D adverbs of manner.

### What the two books show about layers (same topic, two depths)
| Topic | This book (A1/A2 base) | Pre-Intermediate book (A2/B1) |
|---|---|---|
| Present simple | I/you/we/they and he/she/it taught separately; negative, question, short answers; spelling; frequency adverbs | contrast with present continuous, state verbs, habit vs permanent |
| Past simple | was/were; regular -ed spelling; about 20 common irregulars; did/didn't; wh-questions; time phrases | past continuous + past simple with when/while; longer sentences; be vs did; present perfect contrast |
| Present continuous | now; state verbs not used; questions | also for fixed arrangements (future) |
| Comparatives / superlatives | -er/more, than, irregular; -est/most, "in the world" | much / a bit / less; least, "I've ever ...", the second biggest |
| Future | be going to for plans; I'll for offers | will for decisions and predictions, might, be thinking of, present continuous for arrangements |
| should | should/shouldn't + imperatives | ought to, why don't you, maybe / I think you should |
| Quantity | countable/uncountable, a/an/some/any, how much/many, there is/are | many/much, a few/a little, a bit of, plenty of, no |
| Articles | full a / the / zero table | a then the in texts |
Pattern: the higher layer **adds uses and contrasts** and uses **longer sentences with more than one clause** and less basic vocabulary. The same forms (negatives, questions, short answers) appear in both. This supports Inga's correction: A2 and B1 differ by sentence length, vocabulary and added uses, not by negatives/questions.

### Other findings
- Practice sentences in the base book are short and concrete (about 5-8 words: "I love talking to people."); the Pre-Intermediate ones are longer ("I was reading the last few pages of my book when I suddenly heard the last call for my flight.").
- The base book teaches **everyday functions** in "How to ..." pages: suggestions, ordering food, invitations and offers, shopping, apologising and excuses, directions, phoning, hotel requests. The bank has no such area yet; it could be an "Everyday English" area with order-the-conversation, choose-the-phrase and match tasks.
- Task types seen: mostly ones the app already has (choose, gap with word box, put in order, match, correct the mistake). Picture-based and free "use the prompts to write" tasks are not possible or not auto-gradable.
- Topics here that the bank lacks: present simple basics (he/she/it), was/were, have got, there is/are, possessive 's, this/that, frequency adverbs, adjectives and modifiers, adverbs of manner, prepositions of movement, directions, verbs + to infinitive, like + -ing (see also the earlier "not in the bank yet" list).
- Open question for Inga: which level label does this book get? Its content is A1 to low A2 (the file name says A2). Suggest: treat units 1-4 as A1 (Elementary, shown greyed until built), units 5-8 as A2.1, Pre-Intermediate units 1-9 as A2.2... to be decided before any labelling.
