# Build rules for the next course levels (lessons learned from the B1 import)

Status: written 2026-10-11 after the B1 course ("English Fever B1 – Intermediate English", course ID 9037) was built on englishfever.com.
Purpose: change the generator (`tools/build.py`, `tools/make_wxr.py`, unit files) and the instructions, so the A2, B2, C1 (and other) courses come out right the first time.

All rules below were found by really importing the B1 package into WordPress (Tutor LMS Pro 4.1, H5P, LiteSpeed). Nothing is theoretical.

---

## 1. What went wrong or was missing in the first B1 package, and what fixes it

| # | Problem found | Cause | Fix (put it in the generator) |
|---|---|---|---|
| 1 | Reading and Listening lessons ended with *"Next: do the graded quiz "Unit 1 Reading" in Tutor LMS."* | Text written for the old pipeline. Learners are already in Tutor. "Next" in Tutor means the next lesson, not the quiz. | Delete the sentence. Learners use Tutor's own Previous / Next. Quizzes are at the end of the unit. |
| 2 | Exam tip about True / False / Not given was shown in every Reading lesson | One generic tip text for all units | Build the tip from the **real task type** of that page (see section 4). Describe the task the learner sees: a/b/c multiple choice gets multiple-choice tips. Write a True / False / Not given tip only when **every** question on the page has that format. |
| 3 | Listening tip said "Write an answer for every question" and "You hear the recording twice" | Wrong for multiple choice. Audio is not recorded yet. | Use the multiple-choice tip set. Say *"Listen twice, if you need to."* |
| 4 | Lesson title was missing at the top of the lesson | Generator removed the `<h1>`; Tutor does not show the title in the content area | Put the title back as `<h2>` with an icon at the top of every lesson. |
| 5 | Pages were long and plain: all text in one flow | No template classes used | Use the site's lesson templates (`ef-box` family). See section 3. |
| 6 | H5P looked wrong inside a pink box | H5P is an iframe with a white background. A coloured box leaves a coloured frame around it. | Use a **white box with a coloured left bar** for anything that contains H5P (`ef-box--praksa`). |
| 7 | Flashcards: text top-left, small, dull; the title appeared twice | Default Dialogcards CSS; title and description were the same text | Inject CSS into the H5P iframe (same origin): centre text, 30 px bold, coloured card, hide the description. See section 7. |
| 8 | No speaking practice after Grammar and Vocabulary | Not in the package | Add a "Speaking practice" box with 10 questions to the end of every Grammar and Vocabulary lesson (section 5). |
| 9 | No place to hand in writing | Writing lesson said "Write both emails" with nothing to submit | Add a Tutor **Assignment** after every Writing lesson, with a choice of one task and a rubric (section 6). Change the Writing text to "Choose one email". |
| 10 | Quiz CSV imported with literal `<br>` in gap-fill sentences (seen in another quiz) | HTML was put in an **answer** field. Tutor prints tags in answers as text. | No HTML in answer rows at all (section 8). |
| 11 | Same instruction in title, description and answer ("Complete the sentence" ... "Complete the sentence using ...") | Generator filled all three fields with the instruction | One instruction, one place (section 8). |
| 12 | A CSV exported from one course and imported into another produced broken questions (wrong question type, cut-off text, 0 points) | Tutor's own export escapes apostrophes with backslashes and puts `\"` inside HTML. The importer reads with `\` as the escape character, so fields split at commas. | Never move quizzes between courses by CSV. Generate a clean CSV (section 8) or copy the quiz in the database / use Tutor's JSON export. |

---

## 2. Course structure that works

```
Course (draft until checked)
  Topic: 🔒 Lesson bank (hidden from students)      <- exists in every course, empty at start
  Topic: Unit N – <title>
     1 Grammar        (lesson)
     2 Vocabulary     (lesson)
     3 Reading        (lesson)
     4 Listening      (lesson)
     5 Speaking       (lesson)
     6 Writing        (lesson)
     7 Writing assignment: Unit N   (Tutor assignment)
     8 Unit N Grammar and Vocabulary (quiz, 40 pool, 10 shown)
     9 Unit N Reading   (quiz, 8)
    10 Unit N Listening (quiz, 8)
```

* Order matters: Tutor puts a new assignment or quiz at the **end** of the topic. After creating items, set `menu_order` in the order above (a one-off snippet did it for B1).
* Lesson titles inside a topic: `Grammar – <topic>`, `Vocabulary – <topic>`, `Reading – exam practice`, `Listening – exam practice`, `Speaking – exam practice`, `Writing – informal and formal emails`.

---

## 3. Lesson page templates and colours (use the existing `ef-box` family)

The site snippet "EF: Lesson layout + templates" defines the classes. One extra variant was added for H5P ("praksa", see section 7).

| Colour | Class | Use for | Heading icon |
|---|---|---|---|
| Yellow | `ef-box ef-box--tip` | Goal, exam tips, tips, notices, time words, quick test | 🎯 💡 ⏰ 🧪 |
| Grey / neutral | `ef-box ef-box--vocab` | Rules, word lists, texts, examples, scripts, emails | 📘 🔤 📄 ✉️ 📜 |
| White + pink bar | `ef-box ef-box--praksa` | Anything with H5P: practice, questions, flashcards, "Your turn" | ✏️ 🃏 ✍️ |
| Pink | `ef-box ef-box--rozs` | Warnings: Common mistake, Watch out!, Be careful | ⚠️ |
| Blue | `ef-box ef-box--speaking` | Speaking tasks, Speaking practice | 🗣️ |
| Green | `ef-box ef-box--listening` | Listening input (audio player + "Listen twice, if you need to.") | 🎧 |
| Two columns | `ef-rinda` > `ef-kolonna` | Informal vs formal example email; assignment Option A / Option B | – |
| Tables | `<table class="ef-tabula">` | All tables | – |

Page skeleton by lesson type:

* **Grammar:** `<h2>🧩 Unit N · Grammar: …</h2>` → 🎯 Goal (tip) → one neutral box per numbered section → separate ⚠️ and 💡 boxes for callouts → ✏️ Practice (praksa, 3 H5P) → 🗣️ Speaking practice (10 questions).
* **Vocabulary:** `<h2>🔤 …` → 🎯 Goal → 🔤 Word list (table) → 🃏 Flashcards (praksa) → ✏️ Practice (praksa, 3 H5P) → 🗣️ Speaking practice.
* **Reading:** `<h2>📖 …` → 💡 Exam tips (multiple choice) → 📄 text (neutral) → ✏️ Questions (praksa).
* **Listening:** `<h2>🎧 …` → 💡 Exam tips → 🎧 audio (green) → ✏️ Questions (praksa) → 📜 Script (neutral, `<details>`).
* **Speaking:** `<h2>🗣️ …` → "How the speaking exam works" (neutral) → Part 1 interview cards (praksa) → Part 2 and Part 3 (blue).
* **Writing:** `<h2>📝 …` → 🎯 Goal → numbered neutral sections → examples in two columns (✉️ Informal | ✉️ Formal) → 💡 Notice → ✏️ Practice (praksa) → ✍️ Your turn (praksa, "Choose one email … hand it in in the Assignment").

**Checked against the site snippet `ef-lesson-layout.php`:** it defines `ef-box` (+ `--tip`, `--speaking`, `--listening`, `--vocab`, `--rozs`), `ef-tabula`, `ef-rinda`/`ef-kolonna`, `ef-teksts`. It does **not** define `ef-box--praksa`: that comes from the separate H5P snippet (section 7), so it must be active. `.ef-tabula` is only coloured and striped inside `<thead>` / `<tbody>`, so the generator writes every table with both. The snippet does not touch `[h5p slug="…"]` shortcodes (its placeholder filter only acts on `[h5p id="000"]`).

Heading rules: `<h2>` page title only; `<h3>` box title; `<h4>` task titles inside a praksa box.

---

## 4. Exam tips: write them from the task type

Never use one tip text for all units. Check what the page really asks the learner to do.

* **Reading, multiple choice (3 options):**
  1. Read the title and look at the text quickly.
  2. Read each question. Then find the part of the text that answers it.
  3. Check all the options (a, b, c). Wrong options often use words from the text, but they say something different.
* **Listening, multiple choice (3 options):**
  1. Read the questions and the three options before you listen.
  2. Listen for the main idea, not for every word.
  3. Wrong options may use a word from the recording, but they say something different.
  4. Choose one answer for every question, even if you are not sure.
* A page where **every** question is True / False / Not given gets its own tips: read each statement; *True* = the text says the same, *False* = the opposite, *Not given* = the text does not say it. Do not mix this line into multiple-choice tips.
* Different task types (gap fill, matching, open answer) need their own tips. Write them when you add such tasks.
* Listening wording: *"Listen twice, if you need to."* Do not promise "you hear it twice" unless the real exam does.

---

## 5. Speaking practice (Grammar and Vocabulary lessons)

* A blue box titled `🗣️ Speaking practice` at the end of the lesson, a numbered list of **10 questions**, nothing else (no extra instruction text).
* Grammar lesson: questions force the unit grammar in the learner's own context (past experiences, plans, opinions, advice).
* Vocabulary lesson: questions use the unit words and phrases in the learner's own life.
* Questions are short, open, and answerable by a B1 learner in 2–4 sentences.
* Example (Unit 3 grammar: future forms): *What are you doing this weekend? Give details.* / *What do you think the world will be like in twenty years?*

---

## 6. Writing assignment and rubric (after every Writing lesson)

Tutor assignment, title `Writing assignment: Unit N`.

* Learner **chooses ONE** of two tasks (Option A informal email, Option B formal email), 100–120 words. May write in the text box or upload a file. May write the second one for extra practice and send it as a second file.
* Settings used: total 15, pass 9, up to 2 files, 5 MB each, no time limit, retry allowed. *(Tutor showed "Total attempts 3" although 2 was sent. Check this in the builder.)*
* Text layout: 🎯 What to do (tip) → ✍️ Choose your task (two columns) → 📋 How your work is assessed (neutral, rubric table) → 💡 Check before you hand in (tip, checklist).
* Spacing: a plain heading placed directly before an `ef-rinda` row sits too close to the boxes. Give that heading `style="margin:32px 0 18px"` (top 32 px, bottom 18 px). Use the same spacing wherever a loose `<h3>` is followed by a row of boxes (for example "📘 4. Unit N examples" in the Writing lesson).

**Rubric (3 criteria × 5 points = 15):**

| Criteria | 5 points | 3 points | 1 point |
|---|---|---|---|
| **Grammar** (the unit grammar, named) | Used correctly in most sentences. Only small mistakes. | Used, but several mistakes. Sometimes the meaning is not clear. | Missing or mostly incorrect. |
| **Vocabulary** (words from the unit word list) | 6 or more words or phrases used correctly and naturally. | 3–5 used. Some are incorrect. | 0–2 used. |
| **Writing phrases and structure** (from the Writing lesson) | Correct greeting and ending for the register, clear reason for writing, paragraphs, 3 or more linking words. | Most are present, but register or linking words are not always correct. | Few are present. Structure unclear or wrong register. |

For A1/A2 reduce the word count (60–80) and the vocabulary threshold (4 words); for B2/C1 raise it (150–180, 8 words) and add a "register and tone" criterion if wanted.

---

## 7. H5P rules and the two small CSS/JS additions

### Upload and titles
* Package file name pattern: `uNN-<type>.h5p`; H5P **title must stay unchanged** (it starts with `B1 Unit N – …`). Lessons embed with `[h5p slug="…"]` and the slug is the title in lower case with dashes. If a title is changed, the activity disappears from the page.
* 13 activities per unit: grammar (blanks, choice, drag), vocabulary (flashcards, blanks, choice, drag), reading, listening, speaking cards, writing (register, mark, drag).
* Uploading through the admin form works from script: POST multipart to `admin.php?page=h5p_new` with fields `h5p_file`, `action=upload`, `library=0`, `parameters={"params":{},"metadata":{}}`, `yes_sir_will_do=<nonce from the page>`, `_wp_http_referer`. The file can be fetched from raw.githubusercontent.com (public repo) inside the browser, so nothing needs to be pasted.
* A page reload while a long upload runs stops the script. Check which H5P IDs already exist before re-running (never re-run the whole batch).

### Box variant for H5P (add as a snippet, front end)
```css
.ef-box.ef-box--praksa { background:#fff; border-color:#f4c6d4; border-left:5px solid #d83060; }
.ef-box.ef-box--praksa > h2:first-child, .ef-box.ef-box--praksa > h3:first-child { color:#d83060; }
.ef-box--praksa iframe { background:#fff; }
```

### Flashcards (Dialogcards) style
H5P iframes are same-origin, so a small script in `wp_footer` can add a `<style>` inside each `iframe.h5p-iframe` (on load and for 20 seconds after page load, because iframes appear late):
```css
.h5p-dialogcards-description{display:none!important}
.h5p-dialogcards-title-inner,.h5p-dialogcards-title-inner p{text-align:center!important;color:#0b3f56;font-weight:700}
.h5p-dialogcards-card-content{background:linear-gradient(135deg,#eaf4fa,#fff 70%)!important;border:2px solid #cfe3ef!important;border-top:8px solid #0b3f56!important;border-radius:18px!important;text-align:center!important}
.h5p-dialogcards-card-text-wrapper{display:flex!important;flex-direction:column;align-items:center;justify-content:center}
.h5p-dialogcards-card-text-inner-content,.h5p-dialogcards-card-text-inner-content p{font-size:30px!important;font-weight:700!important;color:#0b3f56!important;text-align:center!important}
.h5p-theme-flip{background:#0b3f56!important;border-radius:999px!important;padding:10px 28px!important}
.h5p-navigation{justify-content:center!important;gap:12px}
```
The script tag needs `data-no-optimize="1" data-no-defer="1" data-cfasync="false"`, otherwise LiteSpeed turns inline JS into a deferred data-URL and the page flashes.

---

## 8. Tutor quizzes: CSV that imports correctly

Source of truth: Tutor Pro `QuizImportExport::quiz_import_data` (AJAX action `quiz_import_data`, fields `topic_id`, `_tutor_nonce`, file `csv_file`). Read with `fgetcsv(',', '"', '\\')`.

### File rules
* UTF-8, comma separated, **no header row**, no empty lines. **Every field in double quotes**; a double quote inside text is written `""` (better: avoid).
* **No backslash anywhere.** No HTML attributes (`style=`, `class=`). No line breaks inside a field.
* Apostrophes are fine. Do not add a backslash before them.
* HTML only in the **question text** (column 3) and the **explanation** (column 10), as `<p>…</p>`. **Never in an answer row.**
* Do not open or save the CSV in Excel.

### Row types
* `settings` – **21 columns**: `settings`, title, description (plain text), time value, time unit (`minutes`), hide timer `0`, attempts allowed (`0` = unlimited), passing grade, max questions shown, auto start `0`, layout (`single_question`), order (`rand` or `sorting`), hide numbers `0`, short answer limit `200`, open answer limit `500`, feedback mode (`default`/`reveal`/`retry`), limit attempts flag `0`, partial marking `0`, negative marking `0`, negative type `percent`, negative value `0`.
* `question` – **11 columns**: `question`, short title, question text (`<p>…</p>`), type, points (`1.00`), order number (1…N across the file), answer required (`""`), randomize (`""`), show points `1`, explanation (`<p>…</p>`), `""`.
* `answer` – **7 columns**: `answer`, answer text (plain), `text`, correct (`1`/`0`), `0`, gap/match value, answer order.

### Answers by type
* `single_choice`, `multiple_choice`: one row per option; correct `1`/`0`; gap/match `""`.
* `true_false`: two rows `True`, `False`.
* `fill_in_the_blank`: **one** row; answer text = only the sentence with `{dash}`; gap/match = the correct word (plain text). One gap per question, one accepted answer, no apostrophes in the answer.
* `matching`: one row per pair; answer text = left item, gap/match = right item.
* `ordering`: rows in the correct order.

### Text rules (avoids duplicated instructions)
* **Title** = short task label ("Choose the correct answer", "Complete the sentence").
* **Question text** = only what the title does not say (the sentence, the tense to use, "Write exactly one word."). Never repeat the title's words. Empty is allowed.
* **Answer rows** = answer content only.

### Settings per quiz type used in B1
* Grammar and Vocabulary: 40 questions, shown 10, order `rand`, 15 min, pass 70 %, attempts unlimited, feedback `reveal` (shows the correct answer).
* Reading and Listening: 8 questions, all shown, order `sorting`, 20 min, pass 60 %, 3 attempts. Reading text or listening instructions go in the quiz description (this is the quiz `post_content`; HTML allowed there).

### Self-check before import
* first row is `settings`, only one; column counts 21 / 11 / 7;
* single_choice and true_false: exactly one correct answer;
* no `<`, `>` or `\` in answer rows; no repeated instruction between title, question text and answers;
* number of questions and total points match the plan.
Import ONE quiz first and open it before importing the rest.

---

## 9. Build and import pipeline (what worked in B1)

Everything below ran from the browser (logged in as admin), fetching source files from GitHub raw, so no file had to be pasted:

1. **H5P:** upload each `.h5p` (section 7).
2. **Lessons:** AJAX `tutor_save_lesson` with `topic_id`, `title`, `description` (HTML). Generate the HTML from the unit source files with the template rules above. (Pages import via WXR is no longer needed.)
3. **Quizzes:** build the CSV in memory and send it to `quiz_import_data` (one request per quiz).
4. **Assignments:** AJAX `tutor_assignment_save` with `topic_id`, `assignment_id` (`0` = create, ID = update), `title`, `summary` (HTML) and `assignment_option[...]` (`total_mark`, `pass_mark`, `upload_files_limit`, `upload_file_size_limit`, `attempts_allowed`, `is_retry_allowed`, `time_duration[value|time]`). **Update re-sends all options, otherwise they are wiped.**
5. **Order:** set `menu_order` in the topic (lessons, assignment, quizzes).
6. **Verify with data, not only by eye:** for every lesson compare the number of `[h5p` shortcodes with the source; for every quiz check question count, exactly one correct answer, no tags in answers, settings; for the course check item counts per topic.

Pitfalls:
* The Tutor nonce and any variables in the page are lost on navigation. Re-read the nonce (`_tutor_nonce` from the course builder page) at the start of each run.
* The H5P admin list is loaded by JS, so you cannot search it by fetching HTML. Check IDs with `admin.php?page=h5p&task=show&id=N` instead.
* Keep requests few and sequential on the live site (a CDN bot protection exists).
* Keep the course in **draft** until a teacher has checked at least one lesson per unit and one quiz run-through.

---

## 10. QA checklist per unit (do before publishing)

- [ ] 6 lessons, 1 assignment, 3 quizzes, in the right order.
- [ ] Lesson title at the top of every lesson; no "Next: … in Tutor LMS".
- [ ] H5P count equals the source; each activity loads and gives feedback.
- [ ] Reading and Listening tips fit the task type.
- [ ] Grammar and Vocabulary lessons end with 10 speaking questions.
- [ ] Writing lesson says "Choose one"; the assignment shows 15 points, pass 9, rubric and both options.
- [ ] Quizzes: 40 / 8 / 8 questions, one correct answer each, settings correct, no tags in answers.
- [ ] Flashcards centred; no duplicated title.
- [ ] Mobile view: tables scroll, boxes fit, two columns stack.
- [ ] Audio recorded and attached (open item for B1).

---

## 11. Open items for B1 (carry over to the next levels)

* **Audio:** 8 listening recordings are not made. Listening quiz descriptions mention `b1-unit-NN-listening-quiz.mp3`.
* **Images:** only emoji icons so far. Plan: one real photo per unit (licensed, with alt text and credit), flashcard images later.
* **Unit 1 Grammar** was hand-styled earlier (inline styles). Only the Speaking box was added. Decide whether to move it to templates.
* **Unused H5P:** three Unit 1 grammar activities (IDs 530–532) are not placed because the hand-built lesson uses other H5P.
* **Assignment attempts:** the builder showed 3 although 2 was sent.

---

## 12. Prompt skeleton for generating the next level (give to the AI generator)

> Build a Tutor LMS course for CEFR level **X** with 8 units, using the rules in `docs/BUILD-RULES-FOR-NEXT-LEVELS.md`. For each unit produce: 6 lesson HTML files with the `ef-box` templates (section 3), 13 H5P packages, 3 quiz files in the CSV format of section 8 (40 / 8 / 8 questions), 10 speaking questions each for Grammar and Vocabulary, 2 writing tasks (informal, formal) and the rubric of section 6. Write exam tips from the real task type (section 4). Do not put HTML in answers. Do not repeat instructions between title, question text and answers. Run the self-check of section 8 and the QA list of section 10 and report the result before importing.

---

## 13. What changed in the generator (tools/build.py, make_wxr.py, units/extras.py)

* **Lessons** use the `ef-box` templates, with the lesson title as `<h2>` at the top (sections 3). Callout paragraphs in the unit text (`Watch out!`, `Common mistake`, `Be careful`) become pink boxes; `Tip`, `Quick test`, `Time words` become yellow boxes. H5P goes in white `praksa` boxes.
* **Tips** come from the practice questions on the same page (section 4), not from the quiz. The True / False / Not given tip is written only when every question on the page has that format; otherwise the multiple-choice tips are used.
* **No "Next: … in Tutor LMS"**. Listening says "Listen twice, if you need to."
* **Speaking practice**: 10 questions at the end of every Grammar and Vocabulary lesson, from `tools/units/extras.py`. The build stops if a unit does not have exactly 10 + 10.
* **Writing**: "Choose one" and a Writing assignment (`courses/<level>/unit-NN/assignment/*.html` + `.json`, settings 15 / 9 / 2 files / 5 MB), rubric from `GRAMMAR_LABEL`. `make_wxr.py` also builds `tutor-lms-assignments.zip`.
* **Quiz CSV** in the Tutor importer format (settings 21 / question 11 / answer 7 columns, all fields quoted, no HTML in answers, one correct answer). The build runs the self-check from section 8 and **stops on any error**. Reading and listening quiz descriptions are written as `*.description.html`; the CSV `settings` description is plain text.
* **Flashcards**: no description (the title was repeated).
* **Level**: `EF_LEVEL=A2 python3 tools/build.py` writes `courses/a2/` and `dist/a2/`; H5P titles start with the level; the audio file names use the level.

### Still to do before building another level
1. The unit text (`tools/units/uNN.py`) and `extras.py` are B1 content. A2/B2/C1 need their own versions.
2. Strings that are still B1-specific: the speaking-exam text (`SPEAKING_FORMAT`), the writing core (`WRITING_SECTIONS`), and the tips for task types other than multiple choice.
3. `WRITING_SIZE` in `build.py` sets the word count and the vocabulary threshold per level (A1/A2: 60–80 words, 4 words; B1: 100–120, 6; B2/C1: 150–180, 8). Check these numbers with the teacher.
4. The new CSV has been tested by the self-check only. Import ONE quiz into a test course first and open it.
