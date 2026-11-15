# Brief for a task writer: batch 4 (grammar points with a rule card and no task), 14 November 2026

Repository: /home/user/englishfever (do NOT commit, push or touch git; do NOT edit any file except the two you are told to create).
You write 25 tasks for ONE grammar point of an English grammar practice app for adult Latvian learners. The teacher
(Inga) expects you to be the expert in English and in language teaching: she must not have to correct your tasks by hand.
After you, two blind readers will solve every task without the key and a judge will compare; every second correct answer
you did not accept, every wrong option that is correct English, every superfluous situation will come back as a flag.

## Read first (all of it, really)
1. `docs/ITEM-WRITING-RULES.md` (every dated section; these are corrections she already made once and expects never again).
2. `docs/AGENT-HANDOVER.md` section 3 and the paragraph "The quality bar Inga set on 11 November".
3. `app/tests/bad_examples.json`: every entry, especially those with `reader` (mistakes no script catches).
4. `docs/BLIND-CHECK.md`, section "What every reader checks": your tasks must pass exactly these six checks.
5. `docs/NEXT-STEPS-BRIEF.md` Part A (situation before a choice: cover it; if only one option is still possible English, the situation is superfluous; if a wrong option is correct English in another situation, the situation is what makes the task: keep it short) and Part B (typed answers that are refused).
6. Your point in `docs/GRAMMAR-MAP.md` (search for the backticked id): can-do, typical errors, sources, contrasts.
7. Models of the API and style: `docs/task-drafts/_src/a2_rel_might.py`, `docs/task-drafts/_src/wish_rather_1.py` (see the `# blind check` comments: what readers found), `docs/task-drafts/_src/lib.py` (functions `mc`, `gp`, `tx`, `od`, `mt`, `learning_task`, `also`).
8. The rule card of your topic: `python3 -c "import json;m=json.load(open('app/content/meta.json'));s=[x for x in m['skills'] if x['id']=='TOPIC'][0];print(json.dumps(s['rule'],indent=1,ensure_ascii=False))"`. Every task of a topic uses only forms on its card; if your point needs a line on the card that is not there, say exactly what line (EN and LV) in your report: the lead agent adds it.
9. The existing tasks of your topic and level, to avoid duplicates and to match the house style: `docs/GRAMMAR-MAP-TASKS.csv` (filter by topic) and `grep -i` in `app/content/items.json` and `docs/task-drafts/*.csv` for every model sentence you write. The same sentence + the same task type anywhere = not allowed.

## What to write
25 tasks for your point, at the level given, in this mix (change it only with a reason in your report):
- 7 choice (`mc`): *Choose the correct option: …___…* (gap sentence) or *Which sentence is correct?* / *Which sentence is NOT correct?* (four whole sentences, in NOT correct the other three are correct and about three different things).
- 5 word order (`od`, instruction exactly *Put the words in order.*; a question: *Put the words in order to make a question.*). List every other natural order in `also=[…]` (time phrase first, swapped people). Only orders people really say.
- 4 word bank (`gp(..., bank=[…])`): the right word(s) plus 1-2 wrong chips that build REAL forms that do not fit this sentence (rule of 8 November); no chip that can be rejected without knowing the point.
- 1 matching (`mt`): exactly one sensible pairing (swap any two right sides: if both still make sense, rewrite). Matching is a learning task automatically.
- 5 typed gap (`gp` without bank): every correct word or form in the answer, separated by ` | ` (one gap) or ` / ` between gaps; an instruction or a bracket cue when needed (*(have got)*), never a grammar term.
- 3 whole sentence (`tx`): *Make it negative:*, *Make a yes/no question:*, *Make a question with *What*:*, *Say it another way with *X*:*, *Start with *X*:* … List EVERY correct answer (contractions that the checker cannot work out: *'d*, *'s*; *n't* = *not*, commas, the final full stop and curly apostrophes are handled automatically).

Hard rules (each was a real complaint):
- Exactly one answer fits the instruction and context, or every correct one is accepted. No open gap several words fit.
- Wrong options are ungrammatical in this sentence or a believable mistake of THIS point; never a second valid form; never a word of another kind; never forms nobody writes (*wills, is get*). A common learner mistake may be a wrong option.
- No situation in front of a choice that does not need it (cover test above). Keep instructions short.
- No grammar terms in instructions (not *article, gerund, modal, auxiliary, preposition, plural, negative form of…*). *Make it negative* is fine. Explanations (EN `why`) may use terms.
- Every word the learner must use is in italics in the instruction (`*no longer*`).
- No speaker tag after a quote. No *(to you)* notes. Don't give the answer away (the start never contains the answer).
- Sentences: natural, everyday, adult; settings varied (travel, work, hobbies, lifestyle, learning, relationships, technology), not the same setting twice in a row. A2: about 5-9 words, one clause, everyday words. B1: 10-16 words, two clauses.
- Explanation: short EN (`why`) and LV (`lvw`), Latvian terms from `docs/LATVIAN-TERMS.md`; in Latvian the learners are *izglītojamie*, never *skolēni*; English words in Latvian text in `*…*`; a Latvian typical-mistake note only where Latvian really causes it, starting *Tulkojot burtiski…*. No double dash anywhere. The feedback must fit the task (not a line about another part of the rule).
- Grammar decisions against Murphy, *English Grammar in Use* (name the unit in a comment). British English is the default; where American usage would give another correct answer (e.g. *Do you have* vs *Have you got*; *anymore* vs *any more*), accept it.

## Files you create (only these two)
1. `docs/task-drafts/_src/gp4_POINT.py`: top-level calls only, starting with
   ```python
   """Batch 4, point POINT (LEVEL): ... Murphy unit N."""
   from lib import gp, od, mc, tx, mt, learning_task
   T = "TOPIC SHORT NAME"   # e.g. "Articles"
   L = "LEVEL"
   ```
   then the 25 calls (`mc(T, L, 2, q, ok, [wrong…], why, lvw)`, `gp(T, L, 3, q, "ans | ans2", why, lvw, bank=None)`, `tx(T, L, 4, q, "a | b", why, lvw)`, `od(T, L, 3, "Put the words in order.", "lower case sentence without full stop", why, lvw, also=[...])`, `mt(T, L, 2, "Match each … with …", [(a, b), …], why, lvw)`). No `save()` in this file.
2. `docs/task-drafts/_src/gp4_POINT-notes.md`: in English: the mix, the Murphy unit, for each task one line on "what must the learner know to get this right, and why the wrong options compete"; the card line(s) needed (EN and LV), if any; anything you were unsure of.

## Check your file before you report (and fix what fails)
```bash
cd /home/user/englishfever/docs/task-drafts/_src && python3 -c "import lib, gp4_POINT; lib.save('pending/zz-POINT.csv')"
cd /home/user/englishfever && php tools/check_draft.php docs/task-drafts/pending/zz-POINT.csv   # 0 refused
python3 tools/option_audit.py docs/task-drafts/pending/zz-POINT.csv                         # read every flag
rm docs/task-drafts/pending/zz-POINT.csv
```
Then solve every task yourself as a hostile learner would: is there a second correct answer? a chip combination that gives another correct sentence? a wrong option that is correct English? Fix before reporting.

Report back (short): the file names, the mix, the card lines needed, doubts.
