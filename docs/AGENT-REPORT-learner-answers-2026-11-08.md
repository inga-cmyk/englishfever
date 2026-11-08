# Learner-answer corrections — 8 November 2026

Addresses the 38 findings in issues #44–#81 (round summary #82). No learner
names, account identifiers, exports or scores are included in these changes.

## Pedagogical decisions

- **Present Perfect remains the target of c-3217.** The ambiguous morning
  question is replaced, in both draft copies, with “I ___ Anna since primary
  school, and we are still friends. (know)” → **have known**. Past simple and
  continuous alternatives are not added. The old question is named in
  `replaces` so the importer can retain its historical record and retire it.
- Unconstrained word-order tasks accept the reported grammatical alternatives.
  Their instructions explicitly acknowledge multiple answers, and their English
  and Latvian explanations describe the actual word-order or meaning difference.
- The conditional negative task now explicitly keeps “If she comes” and asks to
  negate only the result. Both-clause negation is not accepted for that revised
  instruction.
- Bare *homework*, the date *on 5th May*, *and then* for joining plans, and formal
  *used not to have* are accepted. *Persons* receives a register note instead of
  being described as ungrammatical.
- The mixed Past Simple / Past Continuous item accepts the temporary-background
  reading *was watching*. The indirect museum question accepts future opening
  readings; neither task specifically requires Present Perfect.
- Two built-in tasks receive new immutable revisions: the main-clause-first
  *unless* rewrite and the possession negative *hasn't got any money*.

## Files and persistence

39 draft rows across 17 CSV files cover the 36 custom task findings (some tasks
have copies in more than one file). The generator overlay
`docs/task-drafts/_src/learner_fixes_20261108.json` records each source match and
its changes, including the live task ID for traceability. It runs after the
earlier screenshot corrections. The remaining two findings concern built-ins.

The release ledger was missing 218 versions already present in the previous
active bank. Those existing versions are now recorded without rewriting their
content, so the two new revisions preserve their predecessors. Unchanged final
content reuses its recorded revision ID on rebuild, avoiding repeated new IDs.
There are still 483 active built-ins; retired versions increase from 329 to 331.

## Validation

- 125 checks against the real CSV importer and grader, in an in-memory database:
  reported alternatives, negative controls, register feedback, repeated imports,
  and retirement/preservation of the replaced diagnostic question.
- All 39 corrected draft rows survive regeneration from their source scripts.
- Full draft-rule validation: 2,830 questions, zero problems.
- Existing report/import tests: 46 checks, 2,829 validated draft rows.
- Bank history and integration: 3,793 checks; bank-integrity unit tests: five.
- Earlier screenshot/content checks: 20; Second Chance scheduling checks: four.
- Rebuilding the built-in bank again leaves its content and revision IDs unchanged.

## Deployment boundary

This is a GitHub source update, not a live deployment or CSV import. Existing
open issues are left open until the deployed application and imported task bank
can be verified. No learner records or historical scores are regraded.
