# Batch 5, point `conj_parallel` (A2.2): notes of the writer

Topic: And, but, or, so, because (`conj_basic`), level A2.2. 7 new tasks in `gp5_conj_parallel.py`. Together with the 3 tasks already counted (2 check, 1 use), the point reaches 10.

## Mix (7)
2 choice, 2 word bank, 2 typed gap, 1 whole sentence, 0 word order.
- **No word order.** In a word order the words come with their forms already given (*cycling*, *went*), so putting them in order does not test whether the forms after *and / or* match. The point already has one order task (*she got up and left the room*). The brief says to use a kind only where it tests the point, so the 2 order tasks went to one more typed gap and one more bank.
- The point had only 1 *use* task, so 3 of the 7 are written answers (2 gaps, 1 sentence). The point now has 6 check and 4 use.

## Source
There is no Murphy unit. The map says "Not a Murphy EGiU unit". EGP: A1 clause + clause with the subject left out. The rule is on the card already, in the lines *Join the same kind of words* (*I like cooking and reading*, *Do you want to walk or to take the bus?*) and *No need to say the subject again* (*She got up and left*). Every task uses only these lines.

## The trap I avoided: a bare verb after *and* that is a second clause
*I enjoy hiking and camp in the mountains* is correct English when it means "I enjoy hiking, and I camp in the mountains". So is *My brother likes chess and watches old films*. For that reason no gap comes after *I / we / you* + present + *-ing and ___*. Each gap is in a place where only one form gives a sentence:
- after a third-person verb, where the bare form does not agree (*My sister loves swimming and cycle*);
- in a noun position after *are* or *for* (*are meeting people and ___*, *Thanks for coming and ___*), where no finite verb can stand;
- after a past or a habit verb with the subject left out, where the time decides (*visited … and ___*, *usually have … and ___*).

## Task by task: what the learner must know, and why the wrong options compete
1. *My sister loves swimming and ___.* (cycling / cycle / to cycle) After *and* the learner uses the same form as before it (*-ing*). *cycle* is the typical mistake from the card (*cooking and read*). It is also wrong here because the subject is *my sister* (it would need *cycles*, which is not offered). *to cycle* is the mixed-pattern mistake from the map (*to walk or taking*).
2. *Which sentence has a mistake?* *I usually have breakfast and reading the news.* The learner must see that the second verb has the same subject and the same form (*read*), the map's mistake *She got up and she leaving*. The other three are correct and test three different things: *so* with a comma, *because*, and *or* in a question.
3. *Would you like to stay in tonight or ___ out?* (go / going / went) After *or* the form follows *to stay*, so *(to) go*. *going* is the believable mistake (*to walk or taking*). *went* is a real form that a learner might copy from a story. *to go* is also correct but cannot be built from one chip, so no second answer exists.
4. *On Saturday we visited my parents and ___ in their garden.* (worked / working / work) Past + *and* + past with the subject left out. *working* is the map's mistake. *work* is the base form after *and*, also believable. Both chips agree with *we*, so the learner must know the point to reject them.
5. *Thanks for coming and ___ me with the move. (help)* → *helping*. After *for* and again after *and*: *-ing*. In this noun position *helped* and *help* give no sentence. The hint *help* is also a noun, but the noun reading gives no sentence here.
6. *The best parts of my job are meeting people and ___. (travel)* → *travelling* (US *traveling* is accepted). The learner must keep the *-ing* of *meeting*. *travel* as a noun gives no correct sentence after *meeting people and*, and *to travel* breaks the parallel form.
7. *Correct the mistake: She closed her laptop and go home.* → *She closed her laptop and went home.* (also with *she went*). The base form *go* after *and* is the mistake. I also accept *She closes her laptop and goes home* (with or without the second *she*): a learner may correct the first verb instead. It is correct English and keeps the forms equal, so it shows the point too. The explanation names both.

## Card lines needed
None. *Join the same kind of words* and *No need to say the subject again* are on the card.

## Checks
- `check_draft.php`: 7 accepted, 0 refused. Typed answers: 11 variants, 0 refused.
- `option_audit.py`: 0 flagged after I made the three correct sentences of task 2 about as long as the wrong one (*correct-longest*).
- `latvian_lint.py`: nothing for this file. The Latvian text was reworded so that no Latvian word (*otrajam, pirmajam, abiem, atkal*) is marked as English.
- The draft CSV was deleted. The other writers' `zz5-*.csv` files in `pending/` were left alone.
- No sentence from this file is in `app/content/items.json` or `docs/task-drafts/*.csv`.

## Doubts
- Task 1 has only two wrong options (*cycle*, *to cycle*). A third one (*cycled*, *cycles*) would be either correct English or not a believable mistake of this point.
- *to cycle* in task 1 (and *to travel* in task 6) treats *-ing and to + verb* as wrong. The card and the map count it as the mistake of this point. A very lenient reader might call *She loves swimming and to cycle* awkward rather than wrong. I kept it because the point is exactly this.
- Task 7: I did not accept *… and was going home*. It is grammatical, but with nothing after it, it is not a natural sentence on its own.
