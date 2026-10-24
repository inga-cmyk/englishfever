# Reported tasks — 24 October 2026

Reviewed all 20 rows in the teacher's report export against branch commit `30863a0`.
This patch is a review candidate, not a production deployment. Importing corrected
draft CSVs is a separate teacher action; a source commit alone does not update
the running site's database-backed custom tasks.

## Disposition

| Report ID | Resolution in source |
| --- | --- |
| c-0113 | Already replaced in the relabelled CSV: photo/take avoids the repeated film noun/verb. |
| c-0220 | Already corrected: will freeze is no longer a distractor; the remaining options are malformed in the sentence. |
| c-1304 | Already accepts now in either position. Regression checked through the real CSV importer and grader. |
| c-1307 | Already replaced with used to to match the topic's taught forms. Would itself is grammatical for this repeated past action. |
| c-1337 | Already replaced with an explicit used-to rewrite matching the topic. The reported would variant was correctly accepted by the old item. |
| c-1410 | Already accepts the alternative my boss order. Regression checked. |
| c-1414 | Already accepts both grammatical arrangements under the unrestricted order instruction. They change who called whom; neither should be described as an equivalent paraphrase. |
| c-1446 | Added a targeted missing-comma reminder while retaining the app's punctuation tolerance. Both driving-test tasks now explain what which refers to and why the comma is needed. |
| c-1449 | Added a concrete sentence/meaning replacement and explicit replacement metadata to retire the misleading old matching task on import. A comma before which does not prove whole-statement reference. |
| ca-C11-4a-r2 | Already replaced by a positive paraphrase task using Unless you hurry. |
| cm-B22-3a-r2 | Reported answer was accepted correctly; no key change. |
| ct-B22-2a | Already replaced the ill-fitting distractor; the learner's both-past answer remains wrong in the intended reading. |
| ct-B22-3a | Already accepts both hadn't driven and hadn't been driving, including expanded negatives. Regression checked. |
| ct-B22-4a-r2 | New revision ct-B22-4a-r4 states the formal written register explicitly and explains why Had I known is correct. |
| ia-B22-4a | Marking was correct: whether to accept is grammatical; the malformed whether accepting option is the answer to the negative-stem task. |
| ia-C11-3a-r2 | New revision ia-C11-3a-r4 explicitly preserves the source meaning; I wonder is grammatical but not equivalent to It's not clear. Existing unclear variants remain accepted. |
| ps-A22-5a-r2 | The instruction wrapper had already been removed from the answer options. |
| ps-B11-2a-r2 | New revision ps-B11-2a-r3 uses The Earth orbits the Sun, avoiding an unqualified boiling-temperature claim. |
| ps-B11-6a-r2 | Already accepts written and numeric times and checks for two sentences; feedback remains explicitly a pattern check, not complete grammar assessment. |
| var-ca-c11-order-01 | Already revised to Had I known about the delay, I would have called you, providing an explicit object/context. |

Also replaced generic feedback on the book which I bought it error with an
explanation of the repeated object pronoun.

## History and validation

- Existing ledger entries are unchanged. Retained all baseline active snapshots,
  including earlier source revisions that had not yet been recorded in the ledger.
- Three newly revised built-in questions retain their predecessors for past
  attempts. Active bank: 490 items; retained versions: 98.
- Fixed a build issue that assigned an unnecessary new revision when automatic
  answer expansion merely reproduced an already published item.
- No database migration, score reset, historical regrading or production data access.
- Python build, five bank-integrity tests, draft-rule checks, Latvian lint and
  order-alternative tests pass. Draft-rule checks cover 2,002 rows.
- PHP grading: all 490 built-ins consistent; 2,229 verb-ending changes checked,
  747 accepted inner-word typo cases.
- PHP history/in-memory integration: 1,980 checks pass.
- New `app/tests/reported_tasks_test.php`: 30 checks pass, including real import
  validation of all 2,002 draft rows, the reported variants, comma notes and
  meaning-preserving versus meaning-changing responses.
- PHP tests ran using the WordPress Playground PHP WASM CLI. Production-host
  deployment and a live teacher import have not been performed.

For release, rebuild/package the app and review/import the corrected
`docs/task-drafts/b1-new-2.csv`. The import preview should identify the old
misleading matching task as replaced; existing custom IDs depend on the site's
database and are not hard-coded in the source CSV.
