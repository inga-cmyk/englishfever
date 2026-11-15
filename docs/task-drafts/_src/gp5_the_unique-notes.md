# Batch 5, point `the_unique` (A2.2), topic Articles: notes

**Murphy:** *English Grammar in Use*, unit 73 (*the*: A *the same*, C *the* + superlative; also *the sun*, *play the piano*).

**What the point had:** 7 *check* tasks (3 word orders, 3 choices, 1 gap with *violin*), all on *the sun / the moon*, the superlative and an instrument, and 1 *use* task (a typed gap at B1.2). None at A2.2 is typed, there is no whole-sentence task, and *the same* is not tested at all.

**Mix (N = 2):** 1 typed gap, 1 whole sentence. With N ≤ 3 the brief says choose what the point lacks: the point has almost only *check* tasks and no *tx*, so both new tasks are written by the learner. No word order: *the* is a single-word choice (brief, point 3).

**Level A2.2:** 7 to 10 words, one clause, present simple only.

## Task by task
1. Typed gap *Complete with a, an or the: We always sit at ___ same table in this café.* → *the*. The learner must know that *same* always takes *the* (Murphy 73 A); the typical mistakes are no article (*at same table*, the map's error *We live in same street*) or *a same*. Naming the three words stops *this / our / that*. Setting: lifestyle (café).
2. Whole sentence *Correct the mistake: Maria is best driver in our family.* → *Maria is the best driver in our family.* (also *Maria's …*, listed because the checker cannot work out *'s*). The learner must add *the* before the superlative. There is only one mistake to find. Setting: family / relationships. Not a repeat of *best student in the class* / *best singer in our school* (different sentence and task type).

Duplicates: `grep` for *same table* and *best driver* in `app/content/items.json` and `docs/task-drafts/**/*.csv`: none.

## Card lines needed
The Articles card has the superlative (*the best*) but not *the same*. Proposed change to the third `use` line:
- EN: *the* is also used with superlatives, *same*, rivers, seas and some countries (*the best, the same, the Baltic Sea, the UK*).
- LV: *the* lieto arī ar vispārākās pakāpes formu, ar *same*, upēm, jūrām un dažām valstīm (*the best, the same, the Baltic Sea, the UK*).

## Checks run
`check_draft.php`: 2 accepted, 0 refused, 6 typed variants, 0 refused. `option_audit.py`: 0 flagged. `draft_rules_test.py`: 0 problems. CSV deleted. `lv_for_file(..., "gap-fill-a2-1.csv")` marks no Latvian word as English, so no `LV_BY_FILE` entry is needed.

## Doubts
- Task 1 depends on the card line above; without it, swap it for a superlative or *the sun* gap (the card already has both).
- *play piano* (no article, common in American English) was left out on purpose: a task on instruments could refuse a correct answer.
