# Upload steps (practice.englishfever.com)

Rules: the practice site is **not** connected to Git. Never push to `live`. One step at a time; check each result before the next.

## A. Before you start (once)
1. hPanel → Backups → make a **files** backup of the practice site (not englishfever.com).
2. Download from GitHub (branch `claude/intelligent-albattani-2e9bfi`): `dist/practice-app-update.zip` and the CSV files in `docs/task-drafts/`.

## B. The app update (code, picker, Second Chance, sounds)
1. hPanel → Files → File Manager → open the **practice site's** folder.
2. Upload `practice-app-update.zip` there (it has no `config/` or `var/`, so your settings and results stay).
3. Extract it in the same folder; answer "overwrite" if asked.
4. Check: no new folders named like `assets.1234` appeared. Delete the zip.
5. Open the practice site, press Ctrl+F5. The footer shows the version time. The new picker has the six level buttons.
6. Plugin: **not needed** this time (the website plugin did not change).

## C. The questions (Tasks tab → now called *Add questions*)
Import the files **one at a time, in this order**. For each: *Choose file* → *Check* (read the result; fix nothing if it says all rows are fine) → *Add as drafts* → look at a few drafts → *Approve all*.
1. `modal-verbs-1.csv` and `comparison-1.csv` (new topics; they appear to learners after approval).
2. `a2-relabelled-1.csv` (A2 copies of 20 B1 questions; the B1 originals leave the pool on their own).
3. `a2-extras-1.csv`, `a2-big-1.csv`.
4. `b1-upgrades-1.csv`, `b1-tenses-1.csv`, `b1-tenses-2.csv`, `b1-passives-1.csv`, `b1-cond-rep-1.csv`.
5. The eight new B1 topics: `b1-new-1.csv`, `b1-new-2.csv`, `b1-new-3.csv`. Read `b1-new-review.md` first. They need the app update (the topics, areas and rule cards are in the code); until then the importer says *Unknown topic*.
6. The nine more topics: `b1-new-4.csv`, `b1-new-5.csv`. Read `b1-new-review-2.md` first. Same rule: upload the app update first, then import.
**Corrected files (plain instructions):** if you already imported the earlier files, import the new ones the same way, one at a time. Tasks that are already there stay untouched; tasks whose wording changed (about 110) are *reworded in place* (same ID, same status, learners' answers stay with them); the check line says e.g. *12 new · 40 reworded · 90 already there*. Press *Add ... / Reword ...*. About 20 matching tasks were rewritten because two endings could fit two beginnings; their rows say *Replaces an older version* and the old version is retired automatically. Nothing needs to be retired by hand.
Latvian text: learners who choose Latvian see it. Approve the English now if you like; have a Latvian teacher read the Latvian columns soon (terms: `LATVIAN-TERMS.md`).

## D. Check as a learner
1. New browser window (or private window): sign in as a learner. Practice → A2 → Start. Questions are a mix of choose, drag and typed.
2. Answer two wrong, finish, open Home: **Second Chance** shows "2 mistakes to fix". Press Start; a right answer says *Mistake fixed!* (sound on: a chime).
3. Practice → press B1: more topics appear. A1 and C2 are greyed out.

## E. Later, not now
Rotate the database password and the SSO secret (config.php and wp-config.php together); research study stays off until the ethics wording is ready.
7. Corrections to questions you already imported: import the same files again (`a2-big-1`, `a2-extras-1`, `b1-cond-rep-1`, `b1-new-1` to `b1-new-3`, `b1-passives-1`, `b1-tenses-1`, `b1-tenses-2`, `comparison-1`, `modal-verbs-1`). The check page lists the changed questions as *updated* (they keep their number, status and results) and the rest as *already there*. One matching task is replaced by a new draft (the old one is retired); approve the new draft.
