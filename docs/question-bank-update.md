# Question bank update

This update corrects 53 existing questions and adds 48 questions, bringing the active bank from 442 to 490. The existing 24 topics, language levels and six Bloom labels are preserved. This is a targeted correction and variety release, not completion of the planned A1–C2 curriculum.

## Student history

Changed questions receive new IDs ending in `-r2`. Their original versions remain in `content/retired.php` and resolve through `Content::item()`. New sessions draw only from the active bank. Existing pending questions and historical attempts still resolve to their original wording and answers. No database migration, historical regrading, XP reset or progress recalculation is performed.

The published ledger contains 543 immutable question versions: 490 active and 53 retired. Tests seed historical attempts, activity, skill statistics and a pending session in an isolated in-memory database and verify they remain unchanged.

## Variety and feedback

- 24 new word-order tasks, one for each topic.
- 12 new gap-fill tasks with word banks and decoys.
- 12 new matching tasks covering form, meaning and context.
- Total drag-and-drop items: 67, up from 19.
- New lower-level questions retain Latvian explanations.
- Order feedback displays capitalized, punctuated model sentences.
- Writing feedback now clearly describes the existing pattern checks; it does not claim to assess all grammar or meaning. AI feedback remains a separate future implementation.

## Validation

The package build passes five Python integrity tests, grading checks for all 490 active items, 2,222 word-ending changes, 748 accepted typo slips, and 1,604 history/correction/drag-and-drop integration checks. PHP tests ran with PHP 8.5 through PHP WASM. Local browser startup and the guest dashboard were verified; a full desktop/mobile interaction sweep and production-host verification remain to be done. No production student data was accessed or modified.

## Release and future edits

Deploy the complete app package so `src/Content.php` and `content/retired.php` travel together. The package excludes configuration files and student databases. The WordPress plugin does not need updating for this release. This branch is a review candidate and has not been deployed.

For future corrections, assign a new revision ID instead of modifying a published question. Preserve the ledger. Run `python3 app/authoring/build.py`, review the generated questions, then run `python3 app/authoring/build.py --record-release` to append the approved new IDs. `python3 tools/package_practice_app.py` runs all three validation suites before packaging. Update release-specific count assertions when adding another release.

## Corrected questions

Each row identifies the original version; the corrected active version has the same ID plus `-r2`.

| Original ID | Correction |
|---|---|
| ps-B11-1a | Distinguish continuous verb forms from gerunds such as knowing. |
| ps-B11-2a | Qualify the temperature and pressure in the general-truth example. |
| ps-B11-4a | Replace a context-dependent continuous use of like with a clear form error. |
| pc-A22-3a | Specify the target future form for an otherwise open completion. |
| pc-A22-5a | State the communicative criterion rather than declaring every other tense impossible. |
| pc-B11-4a | Use an unequivocal continuous-form error. |
| pa-A22-3b | Anchor the gap-fill sequence in the past. |
| pa-B11-2a | The present perfect option can also describe sequential actions; specify the target tense. |
| pac-A22-1a | A past-simple event can also occur at eight; specify an action already in progress. |
| pac-B11-1a | Make the background-action requirement explicit. |
| pac-B11-4a | Past continuous can describe repeated behaviour; replace the disputed error. |
| pac-B12-2a | A past intention does not by itself prove that the action never happened. |
| pp-B11-5a | Present perfect suggests current relevance rather than guaranteeing an unresolved problem. |
| pp-B12-3b | Specify the intended tense where past simple is also possible. |
| ppc-B11-1a | Specify duration continuing to now, not an ambiguous finished past event. |
| ppc-B11-3a | Specify the continuous target; present perfect simple can also express duration. |
| ppc-B12-4a | A bounded number of emails does not make continuous aspect universally impossible. |
| ppf-B12-3c | After does not itself require past perfect; make the exercise requirement explicit. |
| fu-A21-3a | Specify going to instead of rejecting other valid future forms. |
| fu-A22-5a | Both will and going to can predict rain; state the evidence-based criterion. |
| fu-B11-1a | Present continuous in an if-clause can be grammatical; use a clear distractor. |
| fu-B12-3a | Make the intended promise with will explicit. |
| fu-B12-3b | Specify going to in the open future gap. |
| ppp-B11-3a | Specify the intended passive tense. |
| ppp-B11-5a | Both past and present perfect can imply that an email is available; require the relevant reporting form. |
| fup-B11-3a | Specify the target future passive. |
| fup-B12-3a | Specify the target future passive. |
| cz-A22-1a | Will melt is grammatical in a future prediction; require the general-rule form. |
| cz-A22-2a | Qualify the boiling-point fact. |
| cz-B11-3a | The instruction requires when, not whenever. |
| cf-A22-1a | Remove a grammatical continuous alternative from the single-answer MCQ. |
| cf-B11-1a | Provide the meaning that makes unless the unique answer. |
| cf-B11-3b | Get at/reach at do not fit the fixed sentence. |
| cf-B12-4a | Assess the intended meaning rather than banning negatives after unless. |
| ct-B12-2a | A cheaper alternative does not establish that the actual price was expensive. |
| ct-B22-1a | Several offered combinations are valid conditional types; identify the required meaning. |
| ct-B22-4a | Distinguish formal standard usage from informal variants. |
| ca-C11-4a | Do not teach that unless can never take a negative clause. |
| rs-B11-1a | Backshift is not always compulsory; explicitly request it. |
| rs-B12-1a | Make backshift a task requirement. |
| rs-B12-4a | Unshifted will may be valid in context; test the requested reporting convention. |
| rs-B21-1a | Clarify the conventional backshift question. |
| rq-B12-3a | Require backshift instead of rejecting a contextually valid present tense. |
| rv-C12-4a | Replace the disputed recommend + object + infinitive example. |
| ia-C11-1a | The original what-clause was a fused relative, not an embedded question. |
| ps-A21-6a | Accept has and common adverbs in valid present-simple writing. |
| ps-B11-6a | Accept written times, noon and midnight, not just digits. |
| ppp-B11-6a | Accept contracted has/have been in passive writing. |
| ppp-B12-6a | Accept contracted has/have been in passive writing. |
| fup-B11-6a | Accept contracted will in future-passive writing. |
| fup-B12-6a | Accept contracted will in future-passive writing. |
| ct-B12-6a | Make the negative result in the model consistent with the instruction. |
| ct-B21-6a | Make the negative result in the model consistent with the instruction. |
