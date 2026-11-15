# Batch 5, point `plural_only` (A2.2): notes of the writer

Topic: Irregular plurals (`irregular_plurals`), level A2.2 (the topic of the six existing tasks). Murphy, *English Grammar in Use*, unit 79 (as on the map): *jeans, trousers, glasses, scissors* are plural nouns and take a plural verb; to count them, *a pair of*. The six existing tasks (4 check, 2 use) are all about *the police*; the four new ones use the two-part nouns that are on the card (*jeans, trousers, glasses, scissors*: use line *Always plural: things with two parts*), so the point is covered beyond *police*. No overlap with the `unc_nouns` writer (no *advice, news, furniture, information, luggage*).

## Mix (4) and why
1 choice (*Which sentence has a mistake?*), 1 word bank, 1 typed gap, 1 whole sentence: 2 check + 2 use, so the point ends at 6 check + 4 use. No word order: the point already has one, and with these nouns putting the words in order does not test the point (the cards show *are*; *a new pair of jeans / a pair of new jeans* would give two orders).

## What the learner must know, task by task
1. *Which sentence has a mistake?* → *My glasses is in the car.* The learner must know that *glasses* takes a plural verb. The three correct sentences are about three other things: *scissors* with *are* (kitchen; a correct always-plural noun, so the learner cannot pick the odd one out by spotting a two-part noun), *feet* + *hurt* (irregular plural), *people* + *are* (travel).
2. Word bank *Can I borrow ___ ___ for a minute?* [a pair of, a, scissors, scissor] → *a pair of / scissors*. *a scissors* and *a scissor* are the typical mistakes of the point (map: *a scissors*), *a pair of scissor* the half-learned form; no other chip pair gives a correct phrase.
3. *My jeans ___ too big for me now. (be)* → *are*. *now* rules out *were*; the learner must know that *jeans* takes *are* (mistake: *is*).
4. *Start with *These trousers*: This shirt is too expensive.* → *These trousers are too expensive.* The learner must change *is* to *are* because *trousers* is plural; the likely mistake is copying *is*.

Settings: travel / car, work (borrowing), lifestyle (clothes too big now), shopping.

## Card lines needed
Task 2 uses *a pair of*, which the `irregular_plurals` card does not show (the map's can-do has it). Line for the use *Always plural: things with two parts* (or `watch`):
- EN: To count them, use *a pair of*: *a pair of jeans, two pairs of scissors* (not *a jeans*, *a scissor*).
- LV: Lai tos saskaitītu, lieto *a pair of*: *a pair of jeans, two pairs of scissors* (nevis *a jeans*, *a scissor*).
Tasks 1, 3, 4 use only forms already on the card.

## Checks
`check_draft.php`: 4 accepted, 0 refused (3 typed variants). `option_audit.py`: 0 flagged. *jeans, trousers, scissors, glasses* appear in no task in `app/content/items.json` or `docs/task-drafts/*.csv`: no duplicates. The CSV was deleted.

## Doubts
- The italics helper marks *Tulkojot burtiski* (task 2, LV) as English, as in the `unc_nouns` draft: the packaging file needs *Tulkojot burtiski* in its `LV_BY_FILE` list (as for `gap-points-a2-1.csv`).
- Task 2's Latvian note (*vienas šķēres* → *a scissors*) is a real Latvian source of the mistake: Latvian counts these nouns with a plural numeral, English needs *a pair of*. For tasks 1, 3, 4 Latvian does not cause the mistake (*brilles, džinsi, bikses* are plural in Latvian too), so no note.
- Task 4 accepts only *These trousers are too expensive.*; a past tense would change the sentence, which a *Start with* task does not ask for.
