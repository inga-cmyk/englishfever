# Batch 5, point `indef_form` (A2.2): notes of the writer

Topic: Someone, anything, nobody (`indefinite_pronouns`), level A2.2. N = 7 new tasks (the point has 2 check + 1 use: the order *nobody knows the answer*, the choice *___ called you. He didn't leave his name.* → *Someone*, the typed gap *I'm sure I've seen her ___.* → *somewhere*; plus 2 matching tasks that are learning tasks). With these 7 it reaches 10.

Murphy, *English Grammar in Use*: unit 85 (*some* and *any*: *some-* in positive sentences, *any-* in negatives and most questions; *something / anything*, *somebody / anybody*, *somewhere / anywhere*) and unit 86 (*no / none / any*: *nobody, nothing, nowhere* with a positive verb = *not … anybody / anything / anywhere*). *every-* = all: Murphy 86 and 90 (*everybody / everything*, singular verb).

What this point tests (and what it leaves to its neighbours): choosing the first part (*some- / any- / no- / every-*) by the sentence (positive, negative, question, all) and the second part (*-one / -body* people, *-thing* things, *-where* places) by the meaning. The double negative (*I didn't see nobody*) belongs to `indef_neg` (25 tasks already) and the verb after *everybody* to `indef_sing`, so no task here is built on those mistakes.

## Mix (7) and why
2 choice, 2 word bank, 2 typed gap, 1 whole sentence, **no word order**.
- No word order: the cards would hand the learner the word, so putting the words in order does not test which word goes there (batch 5 brief, point 3: for a single-word choice use gaps and choices). The word order the mix asked for (2) went to one more typed gap and one more choice / bank.
- The point had only 1 *use* task, so 3 of the 7 are typed (2 gaps, 1 whole sentence).

## What the learner must know, task by task
1. Choice: *The party was great. ___ had a good time.* → *Everybody*. Must know *every-* = all the people. *Anybody* competes as the *any = all / jebkurš* confusion and is wrong in a positive statement; *Nobody* is correct English in itself, so the short first sentence is what rules it out (cover test: without it, *Everybody* and *Nobody* both fit, so the situation is needed and kept to four words).
2. Choice, *Which sentence has a mistake?*: *I heard anybody in the garden last night.* (*any-* in a positive statement; the right form is *somebody*). The three correct ones are about three different things: *any-* in a question (*Did anyone call me this morning?*), *every-* for all (*Everybody in my office drives to work.*), *no-* with a positive verb (*Nobody in my family can cook.*). The learner has to check the first part of the word against each sentence type.
3. Word bank: *My glasses are ___ in this room. Can you help me look?* → *somewhere*. Must know both parts: a place (*-where*, not *something*) and a positive statement (*some-*, not *anywhere*). Each wrong chip gets one part right, so neither can be rejected without the point. No other chip makes a correct sentence.
4. Word bank: *There's ___ in my wallet. It's empty.* → *nothing*. Must know that with a positive verb (*There's*) the word itself carries the no (*no-*), and that *anything* needs a negative verb (*There isn't anything*). *something* is grammatical but contradicts *It's empty*; *anything* is the believable mistake (Latvian *nav nekā* pushes towards a negative word).
5. Typed gap (lib adds *Complete with a word like someone, anything, nowhere:*): *___ works here on Sundays. The office is closed.* → *Nobody | No one*. Must know that *no-* + a positive verb makes the sentence negative and pick *-body / -one* for people. *Everybody* is ruled out by *closed*. The instruction's example words are not the answer.
6. Typed gap (same instruction): *There are trees ___: in the streets, in the parks, by the river.* → *everywhere*. Must know *every-* = all and *-where* = places; the list after the colon says "all the places". The instruction's example *nowhere* shows the family, not the answer.
7. Whole sentence: *Make it negative: I bought something for Anna.* → *I didn't buy anything for Anna.* | *I didn't buy Anna anything.* | *I bought nothing for Anna.* (*did not* is handled by the checker). Must know that *something* becomes *anything* in a negative (Murphy 85), or *nothing* with a positive verb (Murphy 86). The typical mistake *I didn't buy something* is refused.

Settings, in order: a party (social life), mixed, home, money, work, a town (travel), shopping / relationships. No two neighbours share a setting. Sentences 5-12 words, present and past simple only, everyday words.

Duplicates checked (`grep -i` in `app/content/items.json` and `docs/task-drafts/*.csv`): none of the seven sentences exists anywhere; none repeats the card example (*Everybody was there, but nobody said anything.*). Scenes of the topic's existing tasks avoided (keys, phone, fridge, door, umbrella).

## Checks
- `check_draft.php`: 7 accepted, 0 refused; typed answers 13 variants, 0 refused.
- `option_audit.py`: 0 flagged.
- `draft_rules_test.py` and `latvian_lint.py` (temporary copies pointed at `pending/zz5-*.csv`): 0 problems.
- The temporary CSV was deleted.

## Card lines needed
None: every form used (*some- / any- / no- / every-* with *-one / -body / -thing / -where*, *no-* with a positive verb) is on the card's form table and "When" row.

## Latvian words the italics marking takes for English (for `LV_BY_FILE` under the final CSV name)
*visi, neviens, labi, pareizi, apgalvojuma, lieta, izsaka, pats, neder, makam, visur, kola, koki*. I could not add them (only these two files may be edited). I took *No one* out of the Latvian of task 5: the marker treats *No* as the Latvian word *no* and printed *No \*one\**.

## Doubts
- Task 7: *I didn't buy something for Anna* is possible English in a narrow sense (one particular thing I didn't buy), but for this point it is the taught mistake (Murphy 85), so it is not accepted.
- Task 6: a reader might try *here* (*There are trees here: in the streets…*). The instruction asks for a word like *someone, anything, nowhere*, and the list of places points to *everywhere*, so I accept only *everywhere*. If the blind readers find *here*, the fix is to add it with an answer note or change the sentence, not just widen the key.
- Task 1: *Somebody had a good time* would be grammatical but odd, so it is not an option. The wrong options are only *Anybody* and *Nobody* (three options in all).
