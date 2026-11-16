# Batch 5, point `a_few` (A2.1): notes of the writer

Topic: Quantity (`quantity`), level A2.1 (new for this topic; prepared tasks only, teacher's decision of 15 November). Murphy, *English Grammar in Use*, unit 87 (*few / a few, little / a little*): *a few* + plural noun, *a little* + uncountable noun, both = a small number / amount with a positive feeling. *few / little* without *a* (almost none) is the B1.1 point `few_little` and is not tested here. All forms are on the quantity card (form line 4, use line 2, the table row *a small amount*, the mistake *I have a few money*).

## Mix (6) and why
The point had 4 check tasks (2 choice, 2 word order, all A2.2 / B1.1) and no use task, so most new tasks are typed (brief 5, point 2):
1 choice (*Which sentence has a mistake?*), 1 word bank, 2 typed gaps, 2 whole sentences. No word order: the point already has two, and putting the words in order does not test the choice between *a few* and *a little* (the cards show the noun).

## What the learner must know, task by task
1. *Which sentence has a mistake?* → *I put a few salt in the soup.* The learner must know that *salt* is uncountable and takes *a little*. The other three are correct and about three different things: *a little* + language (*I speak a little German*), *a few* + plural (*a few museums in our town*), *How much* + uncountable (*water*). Two of them use the point correctly, so the learner cannot pick the odd one by spotting *a few / a little*.
2. Word bank *Can you wait ___ minutes, please?* [a few, a little, much] → *a few*: *minutes* is plural. *a little minutes* is the typical error of the point; *much minutes* is the countability mistake of the neighbouring point (real word, wrong with a plural). No *many* chip: *wait many minutes* would be grammatical.
3. *Write *a few* or *a little*: I go to the gym ___ times a week.* → *a few* (*times* plural). The two words are named because without them *some*, *three*, *many* etc. fit the gap.
4. *Write *a few* or *a little*: Can I have ___ milk in my tea?* → *a little* (*milk* uncountable). Named for the same reason (*some* fits).
5. *Say it another way with *a few* or *a little*: I speak some Spanish, but not much.* → *I speak a little Spanish.* The learner chooses the word for an uncountable noun and drops *but not much*. Also accepted: *can speak / know / only speak*, *a little bit of Spanish*, keeping *but not much*, and *a few words of Spanish* (correct, and it uses *a few* + plural).
6. *Say it another way with *a few* or *a little*: There are three or four cafés near my office.* → *There are a few cafés near my office.* (also *cafes*, and *Near my office there are a few cafés*). The learner chooses the word for a plural noun.

Settings: food, work (waiting), lifestyle (gym), food / drink, learning, work (office area); not the same twice in a row except the loose food link between 1 and 4, which are not next to each other.

## Card lines needed
None: every form is on the quantity card.

## Checks
`check_draft.php`: 6 accepted, 0 refused (32 typed variants). `option_audit.py`: 0 flagged. Every sentence grepped in `app/content/items.json` and `docs/task-drafts/*.csv`: no duplicates; no overlap with the `count_unc` draft of the same batch.

## Doubts
- The typed gaps name the two words (*Write *a few* or *a little*:*), as the `no_none` batch did with *no* / *any*: otherwise the gap is open. This makes 3 and 4 a typed choice between two; the whole sentences (5, 6) are the stronger use tasks.
- Latvian explanations do not gloss the meaning (*nedaudz*, *mazliet*): the italics helper marks those ASCII Latvian words as English, so the Latvian text says only which nouns each word goes with.

## Top-up, 16 November
The teacher decided that Quantity A2.1 needs at least 12 counted tasks, so 2 more tasks were appended here (and 2 in `gp5_count_unc.py`); the six above are unchanged. Murphy unit 87.
- **Kinds:** the point has fewest word orders and whole sentences (2 each). One whole sentence; instead of a word order a gap choice, because the cards of a word order show the noun, so ordering them does not test *a few* against *a little* (brief 5, point 3), and the point had no gap choice at A2.1.
7. *Choose the correct option: I need ___ help with my laptop.* [a little / a few / a little of] → *a little*. The learner must know that *help* is uncountable. *a few help* is the typical error of the point; *a little of help* is the Latvian genitive transfer (*palīdzības*) and competes with the right answer for a learner who knows *a little*. *some* is not offered, so the gap is closed. Technology.
8. *Correct the mistake. Change one word: There's a few snow on the roads today.* → *There's a little snow on the roads today.* (also *There is*). *Change one word* is needed: without it *some snow*, *a lot of snow* would also be corrections. With it *few* → *little* is the only fix (*There are a few snow*, *a few snows* are not English). Travel / weather.
- **Checks:** one `lib.save` of both modules (12 rows): `check_draft.php` 12 accepted, 0 refused; `option_audit.py` only the known odd-theme flag of count_unc task 2. Latvian lint: nothing for these rows; no Latvian word in italics. Sentences grepped in `items.json`, the draft CSVs and `_src`: no duplicates.
- **Doubt:** the auto-generated variant *Today There's a little snow on the roads.* has a capital *T* after *Today* (from `lib`, not from the key); harmless if the grader ignores case.
