# Batch 4, point `have_got` (A2.1): notes from the writer

Topic: Auxiliary verbs (`aux_verbs`), level A2.1. Grammar checked against Murphy, *English Grammar in Use*, unit 17 (*have and have got*).
Generator: `docs/task-drafts/_src/gp4_have_got.py` (25 calls, no `save()`).

## Mix (as in the brief, unchanged)
7 choice, 5 word order, 4 word bank, 1 matching (learning task), 5 typed gaps, 3 whole sentences.
Checks run: `check_draft.php` 25 accepted, 0 refused (32 typed variants, 0 refused); `option_audit.py` 0 flagged;
`latvian_lint` and `draft_rules_test` (run on this file only) 0 problems. No model sentence repeats one in `app/content/items.json` or `docs/task-drafts/*.csv`.

## Decisions on the form
- Murphy 17: in questions and negatives there are three forms: *Have you got …? / Do you have …? / Have you …? (less usual)*, and
  *I haven't got / I don't have / I haven't (less usual)*. So the forms without *got* or *do* (*I haven't a car*, *Has she a car?*)
  are **never wrong options**. In the typed negative and question tasks they are **accepted** (*My laptop hasn't a camera.*,
  *Has Tom a motorbike?*, *How many children has she?*, gap *haven't*). The lead listed *Has she a car?* as a typical error: if the
  lead wants it refused, remove the three keys named here; by Murphy it is correct (less usual), which is why I accepted it.
- Short answers drop *got*: *Yes, I have. No, she hasn't.* To *Do you have …?*: *Yes, I do.* (Murphy 17; the existing task
  *'Do you have a car?' → Yes, I do.* agrees).
- *have* for possession has no continuous form. *is having* is used as a wrong option only with nouns where it cannot mean an
  arrangement or an action (*blue eyes*, *a kitchen* in a question about an office, *a big garden*). I avoided *I'm having a car /
  a new kitchen / a cold / not having …*: BrE *We're having a new kitchen* (arrangement) and *I'm not having that* (= I won't allow) are correct.
- No *Do you got*: it is informal American; a reader could call it correct. *don't got / Does … got* appear only as wrong chips
  that build no correct sentence.
- No past (*had*).

## Each task: what the learner must know, and why the wrong options compete
**Choice**
1. *___ your neighbours got a dog?* Have: with *got* the question starts with *have/has*; plural subject → *Have*. *Has* (agreement), *Do* (do + got), *Are* (be for have) are the typical mixes.
2. *Which sentence is correct?* *Has your office got a kitchen?* against *Does … have got* (do + got), *Have your office got* (agreement), *Is … having* (continuous for possession).
3. *Which sentence is correct?* *She doesn't have a laptop at home.* against *doesn't has*, *doesn't have got*, *don't have*: after *doesn't* only *have*.
4. *Choose the correct short answer: 'Have you got a bike?'* Yes, I have. against *Yes, I have got.* (got kept), *Yes, I do.* (wrong auxiliary), *Yes, I've.* (contraction in a short answer).
5. *We ___ any milk.* haven't got, against *don't have got*, *hasn't got* (agreement), *not have got* (no auxiliary). The correct *don't have* is not offered.
6. *Which sentence is NOT correct?* *My sister is having blue eyes.* The other three are three different correct uses: a *have got* question, a *doesn't have* negative, *'s got*.
7. *What kind of car ___ got?* has she, against *she has* (statement order), *does she* (do + got), *have she* (agreement).

**Word order** (the generator makes every instruction *Put the words in order.*, so the statement is accepted where it is correct English)
8. *have you got a minute* (also *you have got a minute*, added automatically): *Have* + subject + *got*.
9. *my brother hasn't got a driving licence*: *hasn't got* stays together after the subject.
10. *does your flat have a balcony*; also *your flat does have a balcony* (stressed statement, correct English, added by hand).
11. *we don't have time for lunch today*; also *today we don't have time for lunch*.
12. *my gym has got a new sauna*: *has got* for *it*.

**Word bank**
13. *Does this bus ___ wifi?* have; chips *has* (does + has) and *have got* (does + have got): both the classic mistakes.
14. *My parents ___ ___ a big garden.* have / got; *are having* is a real form that does not fit a possession; *have having*, *are got* are not sentences.
15. *Sorry, I ___ ___ any change.* haven't / got; *don't got* is the learner mix. *don't have* cannot be built (no *have* chip), so only one answer.
16. *___ the room ___ a fridge?* Has / got; *Does … got* is the mix. *Does … have* cannot be built (no *have* chip).

**Matching** (learning task)
17. *Match each question with its short answer.* Two questions with *you*: only the first word decides between *Yes, I have.* and *No, I don't.*; *Mark* / *Anna* plus *has* / *does* decide the others. Swapping any two right sides gives a wrong short answer.

**Typed gap**
18. *My sister ___ three cats. (have got)* has got | 's got.
19. *We ___ a car, so we cycle to work. (not / have got)* haven't got (the cue names *got*, so *don't have* is not asked for).
20. *'Has the new library got a café?' 'Yes, it ___.'* has (no *got*, not *does*).
21. *___ you ___ an umbrella? (have got)* Have / got.
22. *My grandparents ___ a computer. (not / have)* don't have | haven't got | haven't | have no: every correct form is accepted.

**Whole sentence** (both the *got* form and the *do* form accepted)
23. *Make it negative: My laptop has got a camera.* hasn't got | doesn't have | has no | hasn't.
24. *Make a yes/no question: Tom has got a motorbike.* Has Tom got … | Does Tom have … | Has Tom a motorbike?
25. *Make a question with *How many*: She has got two children.* How many children has she got? | does she have? | has she?

## Card lines needed (`aux_verbs` card)
The card has only *Do you have…? / Have you got…?* (uses block). The tasks also use *has got*, the negatives, the short answers and
the two mistakes. Proposed (replace the third uses block, keep its examples, add one watch line):

- uses block, title
  - EN: *have* = own: *I've got / I have a car*, *She's got / She has a car*. Negative: *I haven't got / I don't have*. Question: *Have you got…? / Do you have…?* Short answer: *Yes, I have. / Yes, I do.* The meaning is the same; *have got* is more British.
  - LV: *have* = piederēt: *I've got / I have a car*, *She's got / She has a car*. Noliegums: *I haven't got / I don't have*. Jautājums: *Have you got…? / Do you have…?* Īsā atbilde: *Yes, I have. / Yes, I do.* Nozīme ir tā pati; *have got* biežāk lieto britu angļu valodā.
- watch line
  - EN: With *do / does* there is no *got*: *[[Do]] you have a car?*, not *Do you have got…?* *have* (own) has no *-ing*: *She [[has got]] blue eyes*, not *She is having blue eyes*.
  - LV: Ar *do / does* nav *got*: *[[Do]] you have a car?*, nevis *Do you have got…?* *have* (piederēt) nelieto ar *-ing*: *She [[has got]] blue eyes*, nevis *She is having blue eyes*.

## Doubts
- Whether to accept *Has Tom a motorbike?* / *How many children has she?* (see above; accepted by Murphy 17 as *less usual*).
- Task 10: *your flat does have a balcony* is accepted as a correct (stressed) statement because `plain()` removes *to make a question*
  from the instruction. The older task *does your brother play football* (learn-drag-4) does not accept its stressed statement; the lead may want one rule for both.
- Task 8 accepts *you have got a minute* (added by `od()`): correct English but an odd sentence on its own; harmless.
