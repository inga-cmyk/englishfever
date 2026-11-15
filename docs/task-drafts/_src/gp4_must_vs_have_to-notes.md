# Batch 4, point `must_vs_have_to` (B1.1): notes from the writer

Topic: Modal verbs (`modal_verbs`), level B1.1. Grammar checked against Murphy, *English Grammar in Use*, unit 31 (*must and have to*),
with unit 32 for *mustn't / don't have to* (Murphy 31 also covers *don't have to* against *mustn't*).
Generator: `docs/task-drafts/_src/gp4_must_vs_have_to.py` (26 calls, no `save()`).

## The teacher's decision for this point (15 November), and how the tasks follow it
- Murphy's "*must* = the speaker's own view, *have to* = a rule or a situation" is a British tendency, not a rule. So no check / use
  task sets *must* against *have to* in present-time obligation, and in typed tasks both are accepted where both are correct English.
- The check / use tasks test only places where one form really is wrong: the past (*had to*, *didn't have to*, *Did … have to*), *will*
  + *have to* (not *will must*), *have to* after another verb (*might have to*, *'ll have to*, *going to have to*), questions and negatives
  with *do / does* (not *Do I must*, *Have I to*, *Has she to*, *hasn't to*), *has to* with *she*, and *mustn't* against *don't have to*
  where the situation makes one meaning certain.
- *Must I …?* is correct (formal; on the card) and is never a wrong option. *Has your brother to …?* and *Have I to …?* are used as wrong
  options as the teacher decided: they are old-fashioned British at most, and Murphy gives *Do I have to …?*.
- The meaning tendency appears only in two learning tasks: the meaning question (task 8, `learning_task()` after it) and the matching
  task (learning automatically). Both explanations say "very often both are possible".

## Mix
7 choice (check) + 1 extra learning choice (meaning), 5 word order (2 questions with *to make a question*), 4 word bank, 1 matching
(learning), 5 typed gaps, 3 whole sentences = 26 tasks: 24 check / use, 2 learning. The brief's mix plus the one meaning question the teacher allowed.

Checks run: `check_draft.php` 26 accepted, 0 refused (40 typed variants, 0 refused); `option_audit.py` 0 flagged (it first flagged
the *NOT correct* task because the wrong sentence was the longest; shortened). `draft_rules_test` on this file only: 0 problems.
`latvian_lint` on this file only: the only failures are the Latvian words below, which go into `LV_BY_FILE` (no other problem).
No model sentence repeats one in `app/content/items.json` or `docs/task-drafts/*.csv` (grep on every sentence).

## Latvian words the italics marking takes for English (for `LV_BY_FILE`)
`neliek nevar likt nesaka tabletes rada tulkojot Tulkojot burtiski britu Britu izsaka noteikumu vilciens nebija izpaliek`
(the lower-case forms are needed: *Tulkojot* and *Britu* at the start of a sentence stayed marked until *tulkojot* / *britu* were added).
The English *to* in "aiz *must* nav *to*" was not marked (Latvian *to*), so that sentence now says "vai *Must I to*" instead.

## Each task: what the learner must know, and why the wrong options compete
**Choice**
1. *My knee hurt so much last winter that I ___ stop running for two months.* had to: the past. *must*, *have to* (present) and *musted* (the typical made-up past) all miss *last winter*.
2. *The hotel is almost full, so we ___ find somewhere else to stay tonight.* might have to: after *might* only *have to*. *might must* and *must have to* (two modals), *might to* (the typical *to* after a modal).
3. *Which sentence is correct?* *Does your brother have to work late when the restaurant is busy?* against *Does … has to* (‑s after *does*), *Has your brother to* (question without *do*), *Do your brother* (agreement in the question).
4. *___ show my student card every time I use the library?* Do I have to, against *Do I must*, *Have I to*, *Must I to*. *Must I* (correct) is not offered.
5. *My manager ___ come to the office on Fridays, so she usually works from home.* doesn't have to, against *hasn't to*, *don't have to* (agreement), *doesn't must*. *mustn't* is not offered: "she isn't allowed to come in, so she works from home" would make sense too.
6. *These tablets can make you sleepy, so you ___ drive after taking them.* mustn't: the reason makes it "important not to". *don't have to* is grammatical but contradicts the reason (the Latvian *nav jā…* trap, explained in LV); *don't must*, *mustn't to* are the form mistakes. *shouldn't* (also correct) is not offered.
7. *Which sentence is NOT correct?* *From May, drivers will must pay to enter the city centre.* The other three are three different correct uses: a past (*had to*), a modal (*might have to*), a question (*Do you have to …?*).
8. **Learning.** *Which sentence is the speaker's own idea, not a rule?* *I must drink less coffee in the evenings.* against three clear rules with *have to* (staff badge, train tickets, essay deadline). Solved from the meaning: it shows the British tendency and is never evidence.

**Word order** (tiles are lower case as in the house style; *i'll* and *we're* are single tiles, so no question can be built from tasks 12 and 13)
9. *do we have to print our boarding passes before we get to the airport* (question; also with the *before* clause first).
10. *does the new manager have to speak latvian or is english enough* (question; also with *english* and *latvian* swapped, which is correct English).
11. *i had to cancel my dentist appointment because i was stuck at work*; also with the *because* clause first. *had* cannot start a question here (*Had I to* is not English), so no question order exists.
12. *i'll have to renew my passport before we fly to canada*; also with the *before* clause first.
13. *we're going to have to hire more staff if sales keep growing*; also with the *if* clause first.

**Word bank** (each wrong chip is a real form that misses the time or the meaning; no agreement-only chips)
14. *We ___ find a hotel near the station because the last train had already left.* had to · must · have to: the past decides.
15. *If nobody can fix the printer today, we ___ ___ buy a new one.* will · have to · must: *will have to*; *will must* and *must have to* are the mistakes the chips allow.
16. *___ she ___ take the whole exam again if she fails one part?* Does · have to · Has · must: every other combination (*Has she have to*, *Does she must*, *must she have to*, *Has she must*) is wrong.
17. *The gym membership includes all the classes, so you ___ pay extra for yoga.* don't have to · mustn't · don't must: the reason makes it "not necessary" (LV note on the *nav jā…* trap).

**Matching** (learning)
18. One verb in all four sentences so only the form decides: *I must book the tickets* = I feel it's necessary; *I had to …* = it was necessary in the past; *I don't have to …* = it isn't necessary; *Do I have to …?* = I'm asking if it's necessary. Swap test: no two right sides fit each other's sentence (a past, a negative and a question cannot be swapped with each other or with *must*). No present *have to* sentence is in it, because by the teacher's decision *I have to book …* = "I feel it's necessary" would also be right.

**Typed gap**
19. *I couldn't park near the office, so I ___ leave the car three streets away. (have to)* had to. *couldn't* fixes the past.
20. *We ___ queue for long at the concert because we had bought our tickets online. (have to / not)* didn't have to | did not have to.
21. *My sister works as a pilot, so she ___ have a medical check every year. (have to)* has to | must | has got to | 's got to. Present obligation: *must* is accepted (teacher's decision), *has got to* is correct British English.
22. *___ you ___ show your passport when you crossed the border last weekend? (have to)* Did / have to. The point is *Did … have*, not *had*. Nothing else fits both gaps (*Had you to* is not English; *Must* is impossible in the past).
23. *My flatmate ___ get up early on Mondays because her first class starts at eleven. (have to / not)* doesn't have to | does not have to | hasn't got to | has not got to.

**Whole sentence**
24. *Start with *Last month*: I have to work every Saturday to cover for a sick colleague.* Last month I had to work … (comma after *Last month* is handled by the checker).
25. *Make a yes/no question: Anna has to take the medicine twice a day while she is ill.* Accepted: *Does Anna have to …?*, *Must Anna take …?* (correct, formal), *Has Anna got to …?*, and the question without *while she is ill* (rule of 13 November).
26. *Say it another way with *might*: Perhaps we will have to sleep at the airport if the strike continues.* Accepted: *We might have to sleep …* in both clause orders, with or without *Perhaps*, and *might need to* (correct English with *might*).

## Card lines needed (the `modal_verbs` card)
1. A line for *have to* after another verb (the card says only *will have to*):
   - EN: "*must* cannot follow another verb: after *might, may, will* or *going to*, use *have to*: *We [[might have to]] wait. We're [[going to have to]] leave.*"
   - LV: "Aiz cita darbības vārda *must* neliek: aiz *might, may, will* vai *going to* lieto *have to*: *We [[might have to]] wait. We're [[going to have to]] leave.*"
2. The British tendency, for the two learning tasks (the card says only "Often both are possible"):
   - EN: "In British English *must* often shows the speaker's own feeling (*I [[must]] call my mum more often*), *have to* a rule or a situation (*I [[have to]] wear a badge at work*). Very often both are possible."
   - LV: "Britu angļu valodā *must* bieži izsaka paša runātāja sajūtu (*I [[must]] call my mum more often*), *have to* noteikumu vai situāciju (*I [[have to]] wear a badge at work*). Ļoti bieži der abi."
3. Optional, the past forms beyond *had to*: EN "Past negative and question: *I [[didn't have to]] pay. [[Did]] you [[have to]] wait?*" / LV "Noliegums un jautājums pagātnē: *I [[didn't have to]] pay. [[Did]] you [[have to]] wait?*" (tasks 20 and 22 use them; the card has *had to* and the *do / does* pattern, so this may be enough without the line).

## Doubts
- *Has your brother to …?* (task 3) and *Have I to …?* (task 4): old-fashioned British English, not wrong in the strict sense; used as wrong options as the teacher said. A blind reader may flag them; the explanation says *Do I have to …?*.
- *has got to* is accepted in tasks 21, 23 and 25 although it is not on the card: it is correct English and refusing it would be a refused correct answer. In task 22 *Has … got to* cannot be accepted per gap (the grader would then also accept *Does … got to*), so the task is past tense, where only *Did / have to* fits.
- Task 6 (*mustn't*): *shouldn't* would also be correct but is not offered; *don't have to* is the believable wrong option because of the Latvian *nav jā…*.
- Spotted in passing, not in this file: `twins-1.csv` has *She ___ call the bank tomorrow morning.* with *will have to* only. By the card ("*must* can also point to the future: *You must call me tomorrow*"), *must* would also be correct there; the options do not offer it, so the choice is fine, but a typed twin of it would need *must* accepted.
