# Review task for another agent: twins batch 3

Inga wants a second opinion on 33 new tasks before she approves them. **Review and suggest; do not change the task files.**

## Read first
- `docs/AGENT-HANDOVER.md` (rules, file map, how to hand work back)
- `docs/ITEM-WRITING-RULES.md`, especially the sections *Added 3 November* and *Added 4 November*: they list every mistake found in batches 1 and 2. Check each task against every one of them.
- `docs/LATVIAN-TERMS.md` (the Latvian terms; English tense names such as *Past Simple* are the correct Latvian terms)

## What to review
- `docs/task-drafts/pending/twins-3-review.md`: each task with its answer key, wrong options or words, the English and Latvian explanation, and the original it is a twin of.
- The data itself: `docs/task-drafts/pending/twins-3.csv`, made by `docs/task-drafts/_src/twins_3.py`.

For every task, ask:
1. Is the answer correct, and is it the **only** answer that fits the instruction and the situation? Would the app reject another correct answer (missing contraction, word order, synonym)?
2. Are the wrong options wrong for one clear reason, of about the same length, all on one theme or each on its own, with no near-identical pair?
3. Does the instruction avoid grammar terms and word counts that give the answer away?
4. Does the task test the skill at the stated level (B1.1, B2.1, B2.2, C1.1, C1.2), and is it really a twin of its original (same skill and type, a different sentence)?
5. Is the Latvian explanation correct, natural and in the terms of `LATVIAN-TERMS.md`?

## Checks to run (all must pass)
```
php tools/check_draft.php docs/task-drafts/pending/twins-3.csv
python3 tools/option_audit.py docs/task-drafts/pending/twins-3.csv     # two NOT-correct tasks are flagged because their four different sentences share "would" / "told": judge them yourself
```

## How to hand the review back
1. `git fetch origin claude/intelligent-albattani-2e9bfi && git checkout -b agent/review-twins-3 origin/claude/intelligent-albattani-2e9bfi`
2. Write `docs/AGENT-REPORT-review-twins-3.md` **in Latvian**: a table *Nr. · problēma · ieteiktais labojums* for every task that needs a change (quote the exact new task, key and options), then a short list of the tasks you would approve as they are. Say what you checked and with which sources.
3. Commit only that report, `git push -u origin agent/review-twins-3`. No pull request, no merge, no changes to the CSV or the generator.
