# Batch 4, point `no_longer` (A2.2): notes of the writer

Topic: Used to and be used to (`used_to`). Murphy, *English Grammar in Use*, unit 111 (*still, yet, already*; *not ... any more / any longer*, *no longer*): *no longer* goes in the middle (before the main verb, after *be*), *not ... any more / any longer* at the end; *no more* is not used this way (*We are no longer friends*, not *We are no more friends*). *anymore* (one word, American) is accepted wherever *any more* is typed.

## Mix (25, as in the brief)
7 choice, 5 typed gap, 3 whole sentence, 5 word order, 4 word bank, 1 matching (a learning task).

## What the learner must know, task by task
Choice
1. *I ___ eat meat.*: *no longer* before the verb. The wrong options are the position mistake (*any more*, *don't any more* in the middle) and the Latvian calque *no more*.
2. *She doesn't work here ___.*: after a negative verb, *any more* at the end. *no longer / no more* make a double negative; *more* is the word-for-word Latvian *vairs*.
3. *We are no longer friends.*: *no longer* after *be*. Against Murphy's own wrong example *no more friends* and two double negatives.
4. *He no longer plays the guitar.*: the position before the verb and a positive verb. Against the wrong position and two double negatives (*no longer doesn't*, *doesn't no longer*).
5. NOT correct: *I don't live there no more.* The other three are correct and on three topics (phone / boss / gym), one each with *no longer*, *any more*, *any longer*.
6. *The bank ___ open on Saturdays.*: *is no longer*. Against *is no more* (calque), *no longer* without *is*, *is any more* (any more needs a negative). *no longer is* was left out on purpose: it is rare but possible, so it cannot be a wrong option.
7. *Tom moved to Oslo. He ___ lives in Riga.*: the one task with a situation, and it is needed: without it *still* is correct English. The other two wrong options are position / calque mistakes.

Typed gap (every correct word accepted)
8. *... any ___.* → *more | longer* (both correct).
9. *I no ___ use this app.* → *longer* (not *more*).
10. *Write *no longer* or *any more*: The airline ___ flies to Riga.* → *no longer*: the verb is positive.
11. *... We don't go camping ___.* → *any more | anymore | any longer* (*any longer* is not in the instruction but is correct, so it is accepted).
12. *They're ___ longer married.* → *no* (not *not*).

Whole sentence
13. *I don't work there any more.* → *I no longer work there.* (also *I'm / I am no longer working there.*)
14. *The museum isn't free any more.* → *The museum is no longer free.* (also *The museum's*).
15. *Ben no longer studies Spanish.* → *Ben doesn't study Spanish any more / anymore* (also *isn't studying*, *Ben's not studying*). *any longer* is not accepted because the instruction asks for *any more*.

Word order
16-20. *i no longer drink coffee*, *we're no longer in the same team*, *my old printer no longer works*, *i don't drive to work any more*, *he's not my neighbour any longer*. Subjects are *I* or contractions so the cards cannot also make a yes/no question (*is this app no longer free* would have been a second correct order). *no longer* at the end (*I drink coffee no longer*) is literary and not accepted; *any more* moved into the middle (*don't drive any more to work*) is not natural and not accepted. No order with *any more* before a countable noun (it would make *any more coffee* = more coffee).

Word bank (wrong chips are mistakes of this point, never agreement or non-forms)
21. *She is ___ my teacher.* [no longer, no more, any more].
22. *We don't use cash ___ ___.* [any, no, more] → *any more*; *no more* is the double negative. (*longer* is not in the bank: *any longer* would be a second answer, and a bank gap takes one answer.)
23. *This bus ___ goes to the airport.* [no longer, any more, no more].
24. *These shoes ___ comfortable ___.* [aren't, are, any more]: *are ... any more* is wrong because *any more* needs a negative.

Matching (learning)
25. *He no longer / She is no longer / They don't live here / We aren't* + *plays football. / our manager. / any more. / neighbours any longer.* Every swap fails on grammar (no verb after *no longer* + noun, *any more* with nothing negative, double *no longer ... any longer*).

## Card lines needed (the card has only *any more in the negative*)
Replace the Watch out line *"*any more* in the negative: *I don't smoke [[any more]].*"* with:
- EN: *A situation has ended: *I [[no longer]] smoke.* (before the verb; after *be*: *She is [[no longer]] my boss.*) = *I don't smoke [[any more]] / [[any longer]].* (at the end, after a negative). Not *no more*.*
- LV: *Situācija ir beigusies: *I [[no longer]] smoke.* (pirms darbības vārda; aiz *be*: *She is [[no longer]] my boss.*) = *I don't smoke [[any more]] / [[any longer]].* (beigās, aiz nolieguma). Nevis *no more*.*
The tasks use *any longer*, so the card must name it. The signals line may add *no longer, any longer*.

## Needs the lead's attention (I could not fix it in my two files)
- **Italics in the Latvian text break *no longer*.** `italics.LV_ASCII` contains *no* (Latvian *no* = from), so `lv_mark` writes *no longer* as `no *longer*` and *I no longer eat meat* as `*I* no *longer eat meat*` in every Latvian explanation of this point. A fix in `lib.py` / `italics.py` is needed, e.g. hold *no longer* / *no more* as English before marking, or treat *no* as English when the next word is English.
- *Tulkojot burtiski* is marked as English (the same in about 44 existing rows: a known general problem). Other Latvian words were reworded so they are not marked.
- If the lead saves this under a new CSV name, no `LV_BY_FILE` entry is needed apart from the two points above.

## Unsure
- Literary *no longer* at the end (*I drink coffee no longer*) is not accepted in the word orders. A blind reader may call it "possible, less natural"; Murphy puts *no longer* in the middle.
- *I no longer smoke any more* (both together) is treated as wrong and was kept out of every bank, so no chip set can build it.
