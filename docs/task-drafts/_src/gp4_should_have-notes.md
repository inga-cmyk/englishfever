# Batch 4, point `should_have` (B1.2): notes from the writer

Topic: More modals (`more_modals`, label *More modals: might, could, be able to*), level B1.2. The teacher's decision of 15 November puts the
point here, not in the passive topic. Grammar checked against Murphy, *English Grammar in Use*, unit 27 (*could* and *could have*: a chance
that was missed, and *could have* as a reproach, "You could have told me") and unit 33 (*should*, section C: *should have done* = it was the
right thing, but it was not done; *shouldn't have done* = it was done, and it was wrong; *ought to have* as the alternative).
Generator: `docs/task-drafts/_src/gp4_should_have.py` (25 calls, no `save()`).

## How the tasks handle the risks
- Every check / use task fixes the modal (in the sentence or in the brackets) and tests the form: *should / could* + *have* + 3rd form.
  The wrong options are the typical mistakes: *should told*, *should have tell*, *should had told*, *should have took*, *should of*, *didn't should have*.
- *should have* and *could have* are never set against each other: *You could have called me* is a reproach too.
- *must have* (deduction, B2.1) is a wrong option in two tasks only, where the sentence says the action did not happen
  (*Why didn't you tell me …? You ___ me*; *I ___ ___ studied …, but I spent the whole weekend watching TV series*).
- *ought to have* (*oughtn't to have*, *ought not to have*, *Ought I to have …?*) is accepted in every typed task with *should*.
  *should've / could've* are listed in the keys.
- Typed gaps all end in a bracket cue: without one, `lib.gp` would add *Complete with a suitable modal verb:* for this topic (a grammar term).

## Mix (as in the brief)
7 choice, 5 word order (1 question), 4 word bank, 1 matching (learning), 5 typed gaps, 3 whole sentences = 25 (24 check / use, 1 learning).

Checks run: `check_draft.php` 25 accepted, 0 refused (47 typed variants, 0 refused). `option_audit.py`: 1 flag, `odd-theme:wrong` on choice 4
(*must have told* shares no content word with the others); a heuristic false alarm on a verb-form choice, kept. `draft_rules_test` with the
file copied into `docs/task-drafts/` for the run: 0 problems. No model sentence repeats one in `app/content/items.json` or `docs/task-drafts/*.csv`
(the bank has *should / could have* only in the passive, *should have been closed*, and inside conditionals).

## Card lines needed (More modals has nothing on this point)
`form`:
- EN: `*should have* + 3rd form = it was right, but it did not happen: *You should have told me.* *shouldn't have* + 3rd form = it happened, but it was wrong: *You shouldn't have shouted.*`
- LV: `*should have* + 3. forma = tā būtu bijis pareizi, bet tas netika izdarīts: *You should have told me.* *shouldn't have* + 3. forma = tas notika, bet tas bija nepareizi: *You shouldn't have shouted.*`
- EN: `*could have* + 3rd form = it was possible, but it did not happen: *We could have won.* It can also criticise: *You could have called me.*`
- LV: `*could have* + 3. forma = tas bija iespējams, bet nenotika: *We could have won.* Tas var arī pārmest: *You could have called me.*`
`mistakes` (v2), suggested: `You [[should told]] me.` → `You [[should have told]] me.` with the LV note `Tulkojot burtiski, "vajadzēja pateikt" šķiet *should told*, bet angliski pagātni rāda *have* + 3. forma.`
`watch`, suggested: EN `We say *should've*, but we write *should have*, never *should of*.` / LV `Runā saka *should've*, bet raksta *should have*, nekad *should of*.`

## Latvian words the italics marking takes for English (for `LV_BY_FILE`)
`Taksometrs Tev Tu tu Tulkojot tulkojot burtiski bijis pareizi nepareizi esmu kliegt kliedzi nepateici pateici nesaka to`
(*to* is the Latvian pronoun in "tu to izdarīji"; no English *to* appears in this file's Latvian texts, so adding it is safe here).

## Each task: what the learner must know, and why the wrong options compete
**Choice**
1. *We ___ a taxi to the airport, because the bus was so slow that we missed our flight.* should have taken: 3rd form after *have*. *should have took* (past for 3rd form), *should took* (no *have*), *should had taken* (*had* for *have*).
2. *You ___ at the waiter, because it wasn't his fault that the kitchen was slow.* shouldn't have shouted, against *shouldn't shouted*, *shouldn't have shout*, *didn't should have shouted* (negative with *did*).
3. *She ___ a great doctor, but she decided to study music instead.* could have been, against *could been*, *could have be*, *could had been*. *should have been* is not offered (it would be a correct opinion).
4. *Why didn't you tell me about the delay? You ___ me before I left home.* should have told: the first sentence says it did not happen, so *must have told* ("I'm sure you told me") contradicts it; *should have tell*, *should had told* are form mistakes. *could have told* (also a correct reproach) is not offered.
5. *Sorry, I should ___ called you last night, but my phone battery was dead.* have, against *of* (spelling from speech) and *had*.
6. *Which sentence is correct?* *You should have checked the figures before you sent the report.* against *should checked*, *should have check*, *should had checked*.
7. *Which sentence is NOT correct?* *You should of booked the tickets much earlier.* The other three are three different correct uses: a regret (*I shouldn't have eaten so much last night*), a missed chance (*We could have driven, but we took the train*), and *You should have seen the view* (you missed something good).

**Word order**
8. *you should have told me that the train was cancelled* (no other order).
9. *i shouldn't have bought these shoes without trying them on* (the fronted *without* phrase is not natural with this regret; not accepted).
10. *she could have got the job but she didn't apply in time* (the clauses cannot swap round *but*).
11. *you could have asked me for help instead of doing it alone*; also *instead of doing it alone you could have asked me for help* (natural).
12. Question: *what should i have said when my boss asked about the delay*; also with the *when* clause first. Written with *to make a question*; `plain()` turns it into *Put the words in order.*, and the lead keeps the question instruction. The library added no statement order here.

**Word bank** (the wrong chips are the mistakes of this point)
13. *You shouldn't ___ ___ the oven on when you went out this morning.* have · left · had · leave: *had left*, *have leave* are the mistakes.
14. *We could ___ ___ the earlier ferry, but we decided to stay another night.* have · taken · took · had: *have took*, *had taken*.
15. *Sorry, I should ___ you that the office was closed on Monday.* have told · told · had told.
16. *I ___ ___ studied for the exam, but I spent the whole weekend watching TV series.* should · have · must · had: *must have* contradicts *but I spent the weekend watching*, *should had* is not English; no other pair gives a sentence.

**Matching** (learning; each comment fits only its own situation: *one* = a coat, *laughed* = the haircut, *a taxi* = the last bus, *told someone* = the problem)
17. No coat → *You should have worn one*; laughed at the haircut → *You shouldn't have laughed*; missed the last bus → *We could have taken a taxi*; said nothing → *You should have told someone*.

**Typed gap** (the modal is in the brackets; a time word or *but* rules out the present form)
18. *You ___ me about the party. I would have loved to come! (should / tell)* should have told | should've told | ought to have told.
19. *I ___ so much at the wedding. I felt terrible the next morning. (should / not / drink)* shouldn't have drunk (and *should not*, *oughtn't to*, *ought not to*). *drank* is refused.
20. *We ___ the final, but we missed two penalties in the last ten minutes. (could / win)* could have won | could've won (the Latvian *varējām uzvarēt* → *could win* trap, in the LV note).
21. *We ___ the whole day at the beach yesterday, but we stayed in the hotel because of the clouds. (could / spend)* could have spent | could've spent; *yesterday* + *but we stayed* rule out *could spend*.
22. *You ___ me back last night. Your phone was with you all evening! (could / call)* could have called | could've called (reproach).

**Whole sentence**
23. *Make it negative: I should have told Anna what you said about her new boyfriend.* shouldn't / should not / oughtn't to / ought not to have told … (and *shouldn't've*).
24. *Start with You shouldn't: It was wrong of you to lend him your car for the whole weekend.* You shouldn't have lent him your car (for the whole weekend) / lent your car to him (…). The start does not contain *have lent*.
25. *Make a yes/no question: I should have told the manager about the mistake in the invoice.* Should I have told the manager about the mistake (in the invoice)? Also *Ought I to have told …?*

## Doubts
- Task 21 and 4: I kept short situations because the wrong option (*could spend*, *must have told*) is correct English in another context.
- *Ought I to have …?* is accepted though rare; it cannot be wrong.
- The *Tulkojot burtiski* note is in the *could have* explanation (all *could have* tasks) and in the explanation of task 15 only.
