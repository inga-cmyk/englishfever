# Batch 5, point `count_unc` (A2.1), topic Quantity: notes

**Murphy:** *English Grammar in Use*, unit 69 (countable and uncountable 1: *a / an* only with a singular countable noun, *money* is uncountable), unit 71 (*a / an* and *some*) and unit 85 (*some* in positive sentences, *any* in negatives and questions).

**Count:** the point had 5 check (3 choices, 2 word banks) and 3 use (3 whole sentences). N = 2, so 10 after this batch.

**Mix and why:** 1 typed gap (use) and 1 choice *Which sentence has a mistake?* (check). The point had no typed gap at all, and no task at all on *a / an* against *some* (all 8 existing tasks are *some / any*), so the typed gap fills both. No word order: here the choice is a single word (*some / any*, *a / an*), and the brief says to use gaps and choices for that, so a word order would not test the point. The choice keeps *some / any*, which the point is mostly about, and adds a choice with whole sentences (the existing choices are all gap sentences). Both stay away from *a few / a little* (another writer's point), from offers (*Would you like some …?*, the point `some_offers`) and from *advice / information / luggage* (the point `unc_nouns`, A2.2).

## Task by task: what the learner must know, and why the wrong options compete
1. Typed gap *Write a, an or some: I need ___ umbrella and ___ money.* → *an / some*. The learner must know that *umbrella* is one countable thing and starts with a vowel sound (*an*, not *a*), and that *money* is uncountable, so it takes *some* and never *a* (*a money* is one of the point's typical errors on the map). The instruction names the three words, so *any*, *much* or *a lot of* do not arise; neither gap takes a second word from the three (*some umbrella* and *a money* are wrong). 6 words, travel / everyday.
2. Choice *Which sentence has a mistake?* → *I don't have some free time this week.* (*some* in a negative: the map's typical error *There aren't some eggs*). The three correct sentences are about three different things: *a* + countable and *some* + uncountable in a positive sentence (*I'd like a sandwich and some water.*, food), *any* in a question (*Are there any shops near your hotel?*, travel), *some* + plural in a positive sentence (*Our office has some new computers.*, work). The wrong sentence is lifestyle. The learner who uses *some* everywhere (or *any* only in questions) does not see the mistake; the learner who thinks *a* cannot go with *some* in one sentence, or that a question needs *some*, picks a correct one. `option_audit.py` flags it `odd-theme:wrong`: on purpose, the brief asks for four sentences about different things.

## Checks
- `check_draft.php`: 2 accepted, 0 refused. `option_audit.py`: one flag, read (above). Temporary CSV deleted.
- Duplicates: no sentence of either task is in `app/content/items.json` or `docs/task-drafts/*.csv`. I avoided *Have you got any plans for Saturday?* (already in `gap-points-a2-1.csv`) and the card's *Do you have any brothers?*.
- Latvian: *lieta* and *apgalvojumos* were marked as English by `lv_fix`, so I reworded (*apgalvojumā, noliegumā un jautājumā*); the output has no Latvian word in italics.

## Card line needed (Quantity card, form section)
Task 1 uses *a / an* against *some*, which the Quantity card does not have (it starts with *some / any + plural or uncountable noun*). Proposed first form line:
- EN: *a / an* + one thing we can count: *an egg, a chair*. Not with uncountable nouns: *some bread*, not *a bread*.
- LV: *a / an* + viena lieta, ko var saskaitīt: *an egg, a chair*. Ar neskaitāmiem lietvārdiem nelieto: *some bread*, nevis *a bread*.
(Examples chosen so that the card does not repeat a task sentence. If the line is not added, task 1 uses a form the card does not teach; task 2 needs no new line.)

## Doubts
- *some* in questions is correct when we expect *yes* (Murphy 85), so I put *any* only in a question that is a plain request for information (*Are there any shops near your hotel?*) and used it as a correct sentence, never as the mistake.
- The topic has no A2.1 level in the app before 15 November; these sentences are 6-8 words, one clause, present simple only.
