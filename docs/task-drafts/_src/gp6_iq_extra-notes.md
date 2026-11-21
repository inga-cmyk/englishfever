# Indirect questions: punctuation and *if* / *whether* (teacher, 21 November)

The teacher's summary listed three issues (scope only, no sentences copied): 1. no question mark when the whole sentence is not a
question; 2. *if* (a condition) vs *whether* (an indirect question, either way); 3. word order, which is already covered. The
ind_polite card already had the punctuation rule, but no task tested it, and typed answers ignore the final punctuation, so only a
choice can test it. Grammar: Murphy unit 50; Swan, *Practical English Usage*, "if and whether" (after a preposition, before
*to* + verb and directly before *or not* only *whether*; *if* can head a condition or an indirect question).

## Files

| File | What |
|---|---|
| `_src/gp6_iq_extra.py` | **new**: 10 tasks, top-level calls only, no `save()`. `POINT_OF` maps each row index in `lib.rows` to its point. The lead agent imports it in `iq_b1_6.py`. Note: `iq_b1_6.point_of()` gives `iq_yn` to any row with *if / whether* in the text, which would be wrong for all 10 rows, so use `gp6_iq_extra.POINT_OF` for these rows. |
| `app/authoring/cards2_h.py` | card `ind_advanced`: two new Watch out lines (EN and LV), so the card has three. `python3 app/authoring/build.py` was run (OK). |

The Latvian texts use only words the italics marking already knows as Latvian, so no `LV_BY_FILE` entry is needed. They never quote
*I have no idea*, because the Latvian *no* would break the italics.

Checks on a temporary `pending/zz-extra.csv`, deleted afterwards: `php tools/check_draft.php` 10 accepted, 0 refused. `option_audit.py`
gave 1 flag: *uneven* on B3 (*If / Whether / Whether or not*). I read it: the correct option is the shortest, so the lengths give
nothing away. `latvian_lint.py` and `draft_rules_test.py` (temporary copies pointed at the file) found 0 problems. The `mistake` gate
was checked by hand: no right sentence is a near-copy of the wrong one, and no OBVIOUS pattern matches.

## A. B1.2, "Indirect questions (Could you tell me where...)", point iq_wh: 4 x *Which sentence has a mistake?*

What the learner must know: *I'd like to know / I'm not sure / I have no idea / I wonder* + a question clause is a statement and
ends with a full stop. *Could you tell me / Do you know / Can you remember / Can you tell me* ask a question and keep *?*. In every
task, two right sentences correctly end in *?* and one right sentence correctly ends in a full stop after a statement frame. So a
learner who just looks for "?" fails: they must judge how each sentence starts. The word order of the wrong sentence is correct, so
the question mark is the only mistake. Each wrong sentence has a different frame, and every task has a different setting.

| # | Mistake (key) | Right sentences | Setting |
|---|---|---|---|
| A1 | I'd like to know why the meeting was moved? | Could you tell me when the last bus leaves? / I wonder what she bought for her brother. / Do you know if Tom has finished the report? | work |
| A2 | I'm not sure which gate our flight leaves from? | Can you remember where we parked the car? / I have no idea who sent me these flowers. / Do you know if the hotel serves breakfast? | travel |
| A3 | I have no idea why my phone keeps switching off? | Could you tell me how long the course lasts? / I'm not sure whether I locked the front door. / Do you know who won the match last night? | technology |
| A4 | I wonder how Anna's job interview went? | Could you tell me which room the exam is in? / I'm not sure how many people are coming. / Can you tell me how you made this soup? | relationships |

For A4 I chose a *wh*-clause after *I wonder*, not *I wonder if*. *I wonder if you could…* is a polite request, and some writers
put a question mark after it, so a reader could argue that one.

## B. B2.2, "Indirect questions, more uses (I don't know what to do)", point iq_whether: 6 tasks

The *if* that means a condition only ever appears as a fronted *if*-clause, or in a sentence that makes sense in only one case.
*Tell me if … / Let me know if …* at the end never appears as the condition, because it can also be an indirect question (both
readings).

| # | Kind | Task | Key | Wrong options / chips | What the learner must know; why the wrong ones compete |
|---|---|---|---|---|---|
| B1 | mcq (meaning, learn) | Which sentence means you give your manager an answer in either case? | Tell your manager whether you can work on Saturday. | If you can work on Saturday, tell your manager. / If you can't work on Saturday, tell your manager. / Tell your manager that you can work on Saturday. | *whether* = yes or no, answer either way. A fronted *if* is one case only; *that* gives one answer. All four are correct English with different meanings. |
| B2 | mcq (meaning, learn) | Which sentence means you call the airline only when there is a problem? | If your bag doesn't arrive, call the airline. | Call the airline to ask whether your bag has arrived. / Whether or not your bag arrives, call the airline. / Call the airline and ask if your bag has arrived. | Only the fronted *if* is a condition. *ask whether / ask if* report a question, so you call anyway; this also shows that *if* can report a question. *whether or not* = in both cases. The instruction shares no words with the key. |
| B3 | mcq (gap, check) | Choose the correct option: ___ the delivery driver rings while I'm in the shower, could you open the door? | If | Whether / Whether or not | Opening the door only makes sense if the driver rings, so it is a condition. *Whether* alone cannot start a condition; *Whether or not* is grammatical but illogical (open the door when nobody rings). |
| B4 | mcq (*Which sentence has a mistake?*, check) | Which sentence has a mistake? | Everything now depends on if the bank approves our loan. | We haven't decided whether to rent a car in Crete. / If the train is delayed, I'll take a taxi. / Could you check whether the hotel has a lift? | After a preposition, only *whether*. The three right sentences cover *whether* + *to*, a correct condition with *if*, and *whether* in a question. They are about three different things. |
| B5 | gap, word bank (check) | The hotel wants to know ___ to expect us before ten, and ___ we're late, they'll keep the room for us until midnight. | whether / if | bank: whether · if · unless | Before *to* + verb only *whether* is possible; the second gap is a condition. *unless we're late, they'll keep the room until midnight* is illogical, because keeping the room only matters when we are late. *if to expect* is the typical mistake. I replaced my first ending (*leave the key at the bar*): with *unless* it could make sense (the bar is closed late). |
| B6 | gap, typed (check) | Complete with one word: The caterer needs to know ___ or not you're coming to the wedding. | whether | none | Directly before *or not* only *whether*; *if or not* is the mistake. No other word fits. |

Mix: 2 meaning (learn), 4 check (2 choices, 1 bank, 1 typed). Settings: work, travel, home, money, travel (hotel, after B4), a
wedding. The two travel tasks are not next to each other.

## C. Card lines added (ind_advanced, Watch out; now three lines)

EN:
- *if* can be a condition (only in that case); *whether* means yes or no, in either case: *Call me [[if]] you need a lift.* = only if you need one; *Tell me [[whether]] you need a lift.* = tell me either way.
- A question mark only when the whole sentence asks: *I have no idea whether it's open[[.]]* but *Do you know whether it's open[[?]]*

LV:
- *if* var būt nosacījums ("ja", tikai tad); *whether* nozīmē "vai", atbildi gaida jebkurā gadījumā: *Call me [[if]] you need a lift.* = zvani tikai tad, ja vajag; *Tell me [[whether]] you need a lift.* = pasaki jebkurā gadījumā.
- Jautājuma zīme ir tikai tad, ja viss teikums jautā: *I have no idea whether it's open[[.]]*, bet *Do you know whether it's open[[?]]*

The card examples are not the answer of any task. The punctuation line was missing on ind_advanced (it is on ind_polite), so I added it.

## Open / for the lead agent
- All 10 tasks are new, so they need a blind round.
- Points: `POINT_OF` (A1 to A4 iq_wh, B1 to B6 iq_whether). Do not use `iq_b1_6.point_of()` for these rows.
- *depends on if* is common in informal native speech. The task follows the taught rule (Swan: after a preposition, *whether*), as the brief asks. A blind reader may flag it as "less natural, not wrong". Only the judge can decide that.
- The B rows go into `iq-b1-6.csv` next to the B1 rows, or into a file of their own: that is the lead agent's decision.
