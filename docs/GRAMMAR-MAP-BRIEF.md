# Brief: the grammar map (Inga, 13 November 2026)

For the agent who writes the map. Read `docs/AGENT-HANDOVER.md` (sections 2–4) and `docs/ITEM-WRITING-RULES.md` first. This task produces **documents only**: change nothing in `app/`, the task files or the tests, and do not package. Another session works on the same branch (stages 3–4 of the plan): pull before every push, touch only the files named here.

## Why
Inga wants a system in which all levels and topics are sequenced and linked, follows standard grammar and its usual order, adapts fully to the learner, and has a real C1. Today the order is a hand-written list of steps (`app/src/Path.php`), the 58 topics are not linked to each other, and the topics once labelled C1 are B2 by the reference list (they are being relabelled B2.2). There is no C1 content.

## What the map is
One table, one row per **grammar point**. A point is smaller than a topic: *Present perfect* is several points (form; *ever / never*; *just / already / yet*; *for / since*; contrast with the past simple). Expect about 150 points for the present 58 topics, plus the missing A2–B2 points and all of C1.

Columns:
- `id` (short, stable), `name`, `level` (A2.1 … C1.2)
- `can_do`: what the learner can say or do, one plain sentence
- `needs`: ids of the points that must be known first (prerequisites)
- `contrasts`: ids of the points it is confused with (where a choice task belongs)
- `typical_errors`: the mistakes Latvian adults make (from `docs/ERROR-TYPES.md`, the rule cards, the tasks)
- `sources`: the Murphy unit (*English Grammar in Use*), the line in `docs/LEVEL-LISTS-test-english.md`, and the English Grammar Profile level when it can be checked
- `topic`: the present topic id (`app/content/meta.json`) or *new*
- `content`: what exists now (rule card yes / no; number of check / use / learn tasks, from `tools/dump_items.php`)

## How levels are decided
Three sources that check each other: Inga's test-english.com lists (scope and order; the site blocks automated access, do not try to get round it), Murphy (the rules), the Cambridge English Grammar Profile (the CEFR level at which learners really use a form). Where they disagree, give both and a recommendation with the reason. Do not quote books from memory as if checked: say what was checked and what is from memory.

## C1
The reference list has ten strands: advanced present tenses; advanced past tenses; the perfect tenses; modals *will, would, should*; modals *can / be able to, may / might*; the subjunctive; advanced agreement; prepositions (position, advanced patterns); participle clauses; advanced word order. Each C1 point names the B2 points it stands on. Note for each strand which task forms it needs: C1 is mostly a choice between two correct forms by meaning or register (two correct sentences with different meanings, key-word transformations, finding mistakes in a paragraph, longer sentences and C1 vocabulary).

## What to deliver
1. `docs/GRAMMAR-MAP.md`: the table (may be split by level), with a short introduction in Latvian for Inga and the content in English.
2. `docs/GRAMMAR-MAP-GAPS.md` (Latvian): points in the reference lists A2–B2 that have no content; topics whose level in the app differs from the map; points with fewer than 10 check / use tasks; contrast pairs with no choice tasks.
3. A page Inga can open (Artifact) with the map in a readable form: by level, each point with what it needs and what it leads to.
4. A list of the questions only Inga can decide (levels where the sources disagree, the order inside a level), each with a recommendation.

## Quality bar
Inga is an English teacher and reads this as an expert. She must not have to correct it by hand: check every prerequisite (can a learner really not do B without A?), every level against the sources, every contrast pair. Have a second agent read the map before she sees it, with one job: find a wrong level, a missing or false prerequisite, a missing standard point. Answer her in Latvian; say *izglītojamie*, never *skolēni*.

## What comes after (not part of this task)
Tag the 3300 tasks to points; compute the path and *Learned* from the map; send a learner back to a prerequisite after an error; make the level test walk the map; write C1 strand by strand through the gates and the second reader. Also proposed and waiting: a short introduction before a new topic (situation and meaning → form and one typical mistake → one task done together), and a confidence rating.
