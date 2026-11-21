# Fixes of 21 November: reported tasks (not indirect questions)

Source: the teacher's tester's report of 21 November and the learners' data (brief A). Indirect-question tasks (ind_polite, ip-*) were not touched. Nr. 23 (c-2367 *Whereas*) was not changed: it waits for the teacher.

Files changed:
- `app/authoring/content_review.py`: six `report_fix` calls (block "Tester's report of 21 November"), then `python3 app/authoring/build.py` (items.json, items.php, retired.json, retired.php regenerated).
- `app/tests/bank_update_test.php`: retired count 457 → 459 (only cs-B12-2a and psp-A22-5a had a ledger version that is now retired; the other four replace -r3 versions that are not yet in `history/published_items.json`).
- Generators in `docs/task-drafts/_src/`: `a2_big.py`, `b1_tenses2.py`, `compare_past.py`, `more_1.py`, `b1_new_4.py`, `comparison.py`, `gp4_wont_refuse.py`, `twins_2.py`; overlay `learner_fixes_20261121.json` (new, loaded in `learner_fixes.py`); `lib.py`: *Tulkojot tulkojot burtiski* added to `LV_BY_FILE["twins-2.csv"]`.
- Regenerated CSVs: `a2-big-1`, `b1-new-4`, `b1-tenses-1`, `b1-tenses-2`, `compare-past-1`, `comparison-1`, `conjunctions-1`, `gap-points-b12-1`, `more-1`. Only the rows below changed (diffed row by row against the files before).
- `twins-2.csv`: **not regenerated as a whole**. `twins_2.py` no longer runs (an assert on `rq-B21-3a-r2`, whose type changed, existed before this work), and `python3 -O twins_2.py` changes other rows (C1.1 → B2.2 levels, review text). The generator was edited, and only its two new rows were spliced into the CSV (the generator's own output for those two rows, made with `-O` and the `twins-2.csv` Latvian word list).
- `app/tests/bad_examples.json`: 13 `reader` entries (one per kind of corrected mistake).

Checks: `php tools/check_draft.php` on all ten CSVs: 0 refused each. `python3 tools/option_audit.py` on all ten: the only flags are old tasks (odd-theme on other rows), none on a changed row. `draft_rules_test.py`: 0 problems. `latvian_lint.py`: the 48 old findings, none new. `orders_test.py`: pass. `bank_update_test.php`: OK. `item_gates_test.py`: my changed tasks are flagged only by `blind` (expected: new round needed) and `point` (8 prepared tasks: map keys below). The gates `copy` and `mistake` (new, uncommitted, not mine) flag none of my tasks.

## Built-in tasks

**5. ia-C12-5a → ia-C12-5a-r4 (B2.2, Which sentence is correct?)**
Wrong: the option *How funds were the spent remains…* is an article scramble, not a mistake of the point.
Now wrong options: *How were the funds spent remains to be investigated.* (question word order) / *How the funds were spent it remains to be investigated.* (extra *it*) / *How the funds were spent remain to be investigated.* (plural verb after a clause subject: learners agree with *funds*). Correct option unchanged. Why: a question clause as subject keeps statement order, needs no *it* and takes a singular verb.

**6. ia-C11-6a → ia-C11-6a-r4 (B2.2, write)**
*The question is how to …* was already accepted (the old check was `how\b`). The feedback for *the questions is how to have balance* was only "Start with *The question is* + a question word". Now four checks, each with EN and LV messages:
1. *questions is* → "*Questions is* does not agree: one question, so *The question is*." (alone: the start check accepts *questions is*, so the learner gets only this message)
2. start → "Start with *The question is*."
3. a question word after it → "After *The question is* put *whether*, *how*, *why* or another question word."
4. question order after *how / why / whether / where / when* (*how can we*, *why is it*) → "After *how*, *why* or *whether* use statement word order: *how we can…*, not *how can we…*." (*who / what* left out: they can be the subject, *who has the keys*.)
Tested with Grader: *the questions is how to have balance* gets only message 1; *The question is how to have balance.* OK; *The question is who has the keys.* OK; *how can we pay* and *why is it so expensive* get message 4; *that we have no money* gets message 3.

**12. psp-A22-5a → psp-A22-5a-r3 (A2.2, Why do we say 'Tickets are sold here'?)**
Wrong: *The tickets are very old and cheap.* is not a misunderstanding anybody has.
Now: *Someone is selling tickets right now.* (reads *are sold* as an action going on now), next to the kept *We want to say who sells the tickets.* and *The sentence is about the past.* (*sold* read as the past). Correct unchanged.

**19. rv-C12-4a → rv-C12-4a-r4 (B2.2, Which sentence has a mistake?)**
Wrong: *He recommended to reading…* is too obvious, and the three right sentences were copies about the same report.
Not *He recommended me to read…* as suggested: *recommend* + person + *to* is accepted in British English (Oxford, Cambridge: formal), and an earlier fix of this task removed it as disputed. Now:
- mistake: *She suggested me to book the tickets early.* (Murphy unit 55: *suggest* never takes a person + *to*)
- correct: *He recommended trying the fish soup.* / *My doctor advised me to rest for a week.* / *They suggested that we meet at the station.*
Why (EN + LV): *suggest* + (*that*) I book / *booking*; *advise* can take a person + *to*.

**21. cs-B12-2a → cs-B12-2a-r2 (B1.2, matching)**
Wrong: *If you heat ice, it melts. = This is always true.* stood next to three car sentences; also *I don't have a car* fitted the first conditional too.
Now one context (getting to work; I have no car, I sometimes borrow my dad's):
- *If I had a car, I would drive to work.* = *I have no car.*
- *If I had had a car, I would have driven to work.* = *I had no car then.*
- *If I borrow my dad's car, I get to work in ten minutes.* = *This is what usually happens.*
- *If the trains are on strike tomorrow, I'll borrow my dad's car.* = *It is possible in the future.*
Swap test: *usually* fits only the present + present sentence (the strike is one day); *possible in the future* contradicts the two unreal sentences (no car) and does not fit a habit; *I have no car* / *I had no car then* differ by time and cannot go with the two sentences in which I drive. No shared word between a sentence and its label. Why EN + LV rewritten (every time / possible future / unreal now / unreal past).

**rs-B21-3a → rs-B21-3a-r4 (B2.1, gap, learners' data)**
'*You must finish by Friday.' → My boss told me ___.* Learner: *to finish by Friday*: correct English (*told me to* + verb reports an order). Added to the answers with a note: "Correct too: *told me to* + verb reports an order. With *that* the verb steps back: *told me that I had to finish*." (LV too). Only an accepted answer was added.

## Prepared tasks

**10. c-1904 (b1-tenses-1.csv:88) *I ___ the report on Monday, but I ___ it to my boss until Friday.***
No change. It is a word bank (finished · didn't send · have finished · haven't sent); the answer is shown as *finished / didn't send* in gap order. The reversed order gives *I didn't send the report on Monday, but I finished it to my boss until Friday*, which is not English, so marking it wrong is right. (If the teacher wants, the feedback could show the whole sentence instead of *a / b*: an app change, not a task change.)

**11. c-0182 (a2-big-1.csv:183) matching, *Match each famous thing with who made it.***
Wrong: literature knowledge; the two *was written by* endings swap. A passive matching with subjects and *by* + agent is always decided by meaning, so the task now matches questions with short answers; *was / were* and the subject give the pronoun:
*Match each question with its answer.* — *Was the bridge built in 1890? = Yes, it was.* ; *Were the photos taken in Rome? = No, they weren't.* ; *Was your sister born in Riga? = No, she wasn't.* ; *Were you invited to the wedding? = Yes, I was.*
Every answer has its own pronoun, so no two swap. `replaces(old pairs)`. Why EN/LV: a short answer repeats *was / were* with the subject's pronoun. Point changes from `pas_by` to `pas_past` (map key below). It stays a learning task (matching).

**14. c-1824 (b1-tenses-1.csv:8) order *my parents never watch the news but they read a newspaper every day***
Now also accepted (overlay): *my parents read a newspaper every day but they never watch the news* (clauses swapped, subject first: same cards, natural), *every day my parents read a newspaper but they never watch the news*, *my parents never watch the news but every day they read a newspaper*. Not accepted: *they read … but my parents never watch…* (*they* would be other people); moving *the / a* (*a news*) is not English.

**15. c-2089 (b1-tenses-2.csv:132) NOT correct *I will to meet you at the gate.***
Now *Which sentence has a mistake?*
- mistake: *Don't worry, I call you as soon as I land.* (present simple for a promise; map typical error of `will_now`: *I call you tomorrow* as a promise; Latvian says *es tev piezvanu*)
- correct: *I'm meeting my sister at the airport tomorrow.* (arrangement) / *I think the flight will be late.* (prediction) / *We're going to rent a car in Lisbon.* (plan)
The learner must know that a promise needs *will* while *as soon as* keeps the present. `replaces("I will to meet you at the gate.")`. Point: `will_now` (was `will_form`).

**16. c-2206 (compare-past-1.csv:59) *Correct the mistake: We had been knowing each other since school.***
The point card (`narrative_b2`) shows *We had been knowing each other for years → We had known…* (mistakes) and *We'd known each other for years* (watch). Three tasks of the point used *know each other*; none equals the card exactly, but each shows its answer. All three changed:
- c-2206 → *Correct the mistake: When she sold the café, she had been owning it since 2010.* Answers: *When she sold the café, she had owned it since 2010.* | *…she'd owned it since 2010.* (*since* rules out *owned*). `replaces(old text)`.
- compare-past-1.csv:57 (gap) *We ___ each other for years before we got married. (know)* → *By the time he retired, he ___ the same car for thirty years. (have)* Answers: *had had* | *'d had* (*by the time* rules out *had*; *have* = own is not continuous). `replaces(old text)`.
- twins-2.csv:49 *Correct the sentence. Keep had: We had been knowing each other for years before we married.* → *Correct the sentence. Keep *had*: The house had been belonging to my grandparents for decades before we bought it.* Answers: *The house had belonged to my grandparents for decades before we bought it.* | *Before we bought it, the house had belonged to my grandparents for decades.* `replaces(old text)`.
New EN/LV explanations name the verb of the task (*have* = own, *own*, *belong*), no card sentence. I checked the card's examples (form table, three mistakes, uses, watch lines) against every task of the point: no answer equals them now.

**17, 18. c-3182, c-3185 (more-1.csv:77, 80)**
- *We ___ to Spain last summer.* went / goed / gone / **were go** (the teacher's *was go*, agreeing with *we*: one mistake, not two)
- *She ___ her keys two days ago.* lost / losed / has lost / **was lost**
Each wrong in the sentence: *We goed / We gone / We were go*; *She losed / She has lost … two days ago / She was lost her keys*. Correct option unchanged (updated in place on import).

**20. c-3426 (twins-2.csv:9) NOT correct *If we had caught the flight, we would are in Rome now.***
*…we would have been in Rome now* was checked and not used: with *by now* it is correct, and with *now* many speakers say it, so blind readers would call it acceptable. Now the mistake is *would* in the *if*-part, the commonest mistake in these sentences (Latvian *ja mēs būtu* in both parts):
*If we would have caught the flight, we would be in Rome now.* The other three (receipt / course / job) were already three different sentences. Why EN/LV rewritten. `replaces(old correct option)`.

**22. c-2948 (gap-points-b12-1.csv:127)** → *Choose the correct option: I charged it all night, but my phone still ___.* (*won't switch on*; options unchanged). `replaces("won't switch on")` (the only B1.2 future choice with that answer).

**24. c-2361 (conjunctions-1.csv:103) *It was a difficult task, and ___ they finished it on time.***
*and nevertheless* is correct English (more formal; *and yet* is the usual pair; *nevertheless / nonetheless* = in spite of this). Accepted: *yet | still | nevertheless | nonetheless*, with an answer note for the two formal words (overlay). Only accepted answers were added.

**c-1822 (b1-tenses-1.csv:6)** *I usually don't drink coffee after lunch because it keeps me awake*: correct (*usually* may go before a negative auxiliary; *don't usually* is more common, Swan). Accepted with *because …* first, and *usually I don't …* (overlay).

**c-1393 (b1-new-4.csv:139)** *could you please pass me the salt*: correct, accepted. The generated order *please you could pass me the salt* is not English and was removed; *you could pass me the salt please* stays (the instruction does not say question, and the order gate wants the statement accepted).

**c-2233 (comparison-1.csv:26)** *that jacket is cheaper than this one*: correct, with no context to rule it out. Accepted (overlay).

**c-1282 / server c-1693 (b1-new-4.csv:28) NOT correct *You needn't to come early.***
The key is right (0 of 5 learners chose a correct sentence: *You needn't come early.* or *You don't need to come early.*). But the three correct sentences were copies of the wrong one (rule of 29 October), so learners compared near-identical pairs. Now: *We needn't book a table on a Monday.* / *You don't need to bring any food.* / *She doesn't need to work this Friday.* *needn't have come* removed (another point). Correct option unchanged (updated in place).

**c-2243 (comparison-1.csv:36)** *Rewrite with less ... than: This flat is more expensive than that flat.* → *Rewrite with *less*. Start with *That flat*: This flat is more expensive than that flat.* Answers: *That flat is less expensive than this flat / this one* (+ *That flat's …*, + *… this flat is / this one is*). The start fixes the direction without giving the form. `replaces(old text)`.

**c-3082 (modal-verbs-1.csv:38)** *Put the words in order to make a question.* 6 of 14 built *we should leave before it gets dark*. No task change: the instruction says question, and nothing else on the screen does (order tasks show no *?*; `Grader::nice` adds it only in the answer). Undecided, for the lead / teacher: showing a fixed *?* at the end of the answer line in tasks that say *to make a question* (an app change, display only) would make the task clear without a new instruction.

## Map keys to carry over (gate `point`; `docs/grammar-map-src/assign_keys.json` was not edited by me)

```json
"past_simple_passive | A2.2 | match | Match each question with its answer. | Was the bridge built in 1890? = Yes, it was. ; Were the photos taken in Rome? = No, they weren't. ; Was your sister born in Riga? = No, she wasn't. ; Were you invited to the wedding? = Yes, I was.": ["pas_past", "read"],
"future | B1.1 | mcq | Which sentence has a mistake? | Don't worry, I call you as soon as I land.": ["will_now", "read"],
"narrative_b2 | B2.2 | gap | By the time he retired, he ___ the same car for thirty years. (have) | ": ["pastpc_vs", "read"],
"narrative_b2 | B2.2 | text | Correct the mistake: When she sold the café, she had been owning it since 2010. | ": ["pastpc_vs", "read"],
"comparison | B1.1 | text | Rewrite with *less*. Start with *That flat*: This flat is more expensive than that flat. | ": ["cmp_less", "read"],
"future | B1.2 | mcq | Choose the correct option: I charged it all night, but my phone still ___. | won't switch on": ["wont_refuse", "read"],
"cond_mixed | B2.1 | mcq | Which sentence is NOT correct? | If we would have caught the flight, we would be in Rome now.": ["c_mixed", "read"],
"narrative_b2 | B2.2 | text | Correct the sentence. Keep *had*: The house had been belonging to my grandparents for decades before we bought it. | ": ["pastpc_vs", "read"]
```
(Copy the key text exactly as `item_gates_test.py` prints it; the old keys can stay or be removed.)

## Blind round needed (lead)
Answers only added, no new round: rs-B21-3a, c-1824, c-1822, c-2233, c-2361.
New round: c-1393 (a wrong generated order was removed, not only added), ia-C12-5a, ia-C11-6a (checks), psp-A22-5a, rv-C12-4a, cs-B12-2a, c-0182, c-2089, c-2206, compare-past-1.csv:57, twins-2.csv:49, c-3182, c-3185, c-3426, c-2948, c-1693 (b1-new-4.csv:28), c-2243.

## Undecided
- c-3082: a *?* on the answer line (app change), or nothing.
- c-1904: show the whole sentence after a two-gap word bank instead of *a / b* (app change), or nothing.
- Research data: added answers change grading of rs-B21-3a, c-1824, c-1822, c-1393, c-2233, c-2361 (a dated line in `RESEARCH-DATA-PLAN.md` is the lead's).
