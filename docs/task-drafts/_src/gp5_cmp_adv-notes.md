# Batch 5, point `cmp_adv` (A2.2): notes of the writer

Topic: Comparison: -er, more, the most, as ... as (`comparison`), level A2.2. 8 new tasks in `gp5_cmp_adv.py`; with the 2 existing check tasks (`comparison-1.csv:30, 31`, *works harder*, *the most fluently*, both B1.1) the point reaches 10.

## Mix and why
2 choice, 1 word order, 1 word bank, 3 typed gap, 1 whole sentence (brief: 2-3 / 2 / 2 / 2 / 1). The point had **no use task**, so the brief asks for mostly typed tasks: one word order and one word bank moved to typed (4 of 8 are *use*: 3 gaps, 1 sentence). Only one word order, because adverb comparison seldom decides a word order; the one written tests the place of the adverb after the object (*speaks English more fluently*, Latvian *runā brīvāk angliski*).

## Murphy
Unit 105 (comparative adverbs: *more slowly, more carefully*; *harder, faster, earlier, later*; *better, worse, further*; *slower / quicker / louder* also used informally). Unit 108 (superlatives; with an adverb, *the* is often left out: *who works hardest*). *than me / than I do* as on the card (unit 107).

## Decisions
- No adverb whose *-er* form is used informally as an adverb (*slow, quick, loud, clear, cheap*) in a typed gap or as a wrong option. Task 1 keys *more slowly* and does not offer *slower*; the explanation names *slower* as everyday speech.
- *slowlier, more slowlier, more well, more fast* are used as wrong forms: they are the point's listed typical errors (*more fast, more quicklier, more well*), i.e. common learner mistakes (rule of 11 November).
- Superlative gap accepts with and without *the*, and *further / farther*.
- Typed comparative gaps accept *much / a lot / far / a bit* + comparative; the cue word in brackets rules out *less* and other adverbs.

## Task by task: what must the learner know, and why the wrong options compete
1. *Please drive ___. The road is icy.* (more slowly / slowlier / more slowlier / the most slowly) An *-ly* adverb takes *more*. *slowlier* is the -er transfer from adjectives; *more slowlier* is the double form; *the most slowly* is the superlative, wrong with no group.
2. *Which sentence has a mistake?* *Tom drives more fast than his father.* *fast* has no *-ly*, so *faster*. The other three are correct and about three different things: *later than* (adverb -er), *much faster* (degree), *the best* (irregular superlative).
3. *my sister speaks english more fluently than me* The adverb follows the object; the tempting order is *speaks more fluently English*. People cannot swap (*me* cannot be the subject); no other natural order.
4. *She plays the guitar ___ than her brother.* (better / more well / best) *well* → *better*. *more well* is the typical error; *best* is the wrong degree before *than*.
5. *Marta has never had an accident. She drives ___ than her brother. (careful)* The learner must make the adverb and its comparative: *more carefully*. *more careful* (adjective) is the believable mistake. The first sentence rules out *less carefully*.
6. *Today I started work ___ than usual. (early)* *early → earlier*, not *more early*. *than usual* forces the comparative (without it, *early* would be correct).
7. *Of all my colleagues, Anna lives ___ from the office. (far)* *Of all* needs the superlative; *far* is irregular. Accepted: *the furthest, the farthest, furthest, farthest*.
8. *Start with *My brother*: I cook worse than my brother.* The learner must turn *worse* into its opposite *better* (irregular, adverb after *cooks*) and add *than me / than I do*. Accepted also *much / a lot better* and *My brother is a better cook than me / than I am / than I* (correct English with the same meaning).

## Card lines needed
The topic card is about adjectives only; nothing on adverbs. Add (EN and LV) one `form` line:
- EN: "Adverbs: *-ly* adverbs take *more / the most* (*more slowly, the most carefully*). *fast, hard, early, late* take *-er / -est* (*faster, harder, earlier*). Irregular: *well - better - the best*; *badly - worse - the worst*; *far - further - the furthest*."
- LV: "Apstākļa vārdi: apstākļa vārdi ar *-ly* lieto *more / the most* (*more slowly, the most carefully*). *fast, hard, early, late* lieto *-er / -est* (*faster, harder, earlier*). Nekārtnie: *well - better - the best*; *badly - worse - the worst*; *far - further - the furthest*."
Optionally a mistake row: *He speaks English [[more well]].* → *He speaks English [[better]].* The point has no card of its own (map: "card: no"), and it is not in `app/authoring/new_points.py`.

## Doubts
- Latvian words that `lib.save()` marked as English in the explanations (no Latvian letters): *visu, grupu, pareizi, dzird, galotnes, Tulkojot, burtiski, otrs*. Add them to the `LV_BY_FILE` entry of the batch-5 CSV.
- Map level: the map lists the point at A2.2 but the app's two existing tasks are B1.1; the new ones are written at A2.2 (short, one clause) as the brief says.
- *fluently* (task 3) is the same adverb as existing task 31 (*the most fluently*), but a different sentence and task type.
