# Import the B1 course with the Claude desktop app's built-in browser

The built-in browser is the browser pane inside the Claude desktop app. It keeps your sign-ins, so Claude can work in your WordPress admin without you sharing a password.

> **Updated import method.** The B1 course was imported for real on englishfever.com. The tested pipeline (H5P upload, Tutor lessons via AJAX, quizzes via CSV, writing assignments) and all layout, quiz-CSV and QA rules are in [BUILD-RULES-FOR-NEXT-LEVELS.md](BUILD-RULES-FOR-NEXT-LEVELS.md). Where this guide and that document differ (for example the WXR page import and the "Next: do the quiz" lines), **follow BUILD-RULES-FOR-NEXT-LEVELS.md**.

## Before you start
1. **Back up or use a staging site.** Import into a staging copy first if you have one.
2. **Get the files on your computer.** Download the repository ZIP:
   https://github.com/inga-cmyk/englishfever/archive/refs/heads/claude/focused-archimedes-f14so6.zip
   Unzip it. You need these files:
   - `dist/all-h5p.zip` (unzip it: 104 `.h5p` files, or use `dist/h5p/`)
   - `dist/wordpress/english-fever-b1-pages.xml`
   - `dist/tutor-lms-quizzes.zip` (unzip it: 24 quizzes as `.json` and `.csv`)
3. **Check the plugins** in WordPress: *H5P* and *Tutor LMS* (with the WordPress Importer, installed when you first open Tools → Import).
4. Open the Claude desktop app, start a new session, and select the unzipped folder as the working folder.
5. In the built-in browser, open your WordPress admin (`https://YOUR-SITE/wp-admin`) and **log in yourself**. Do not type the password into the chat.

## Paste this prompt into Claude
> Use the built-in browser, which is already logged in to my WordPress admin at https://YOUR-SITE/wp-admin. Work in this order, and tell me what you did after each step. Stop and ask me if anything looks different from what you expect, or if you are about to delete something.
>
> 1. **H5P upload.** Go to H5P Content → Add New → Upload. Upload the files from `dist/h5p/` one at a time, starting with `u01-*.h5p`. Do not change the titles. After each upload, click Create/Save, and make sure the title is unchanged (it starts with "B1 Unit"). Report any file that fails and the error text. If a library is missing, install it from the H5P Hub and retry.
> 2. **Pages.** Go to Tools → Import → WordPress and import `dist/wordpress/english-fever-b1-pages.xml`. Choose "assign posts to an existing user" (me). When it finishes, open `B1 Unit 1 · Grammar` and check that the three H5P activities show. Then check one page from units 4 and 8.
> 3. **Audio.** I will record the audio later. Skip this step.
> 4. **Tutor LMS.** Create a course called "English Fever B1" (or use my existing one). For each unit, create one topic "Unit N". Add the 6 lessons from the imported pages (copy the page content into a Tutor lesson). Then create 3 quizzes per unit from `courses/b1/unit-NN/tutor-lms/`:
>    - "Unit N Grammar and Vocabulary": add all 40 single-choice questions from the CSV. Settings: question order Random; *Max questions allowed to answer* = 10; time limit 15 minutes; passing grade 70%; unlimited attempts; show correct answers.
>    - "Unit N Reading" and "Unit N Listening": add the 8 questions from the CSV. Put the quiz description from the `.json` file (reading text, or listening instructions) in the quiz description. Time limit 20 minutes; passing grade 60%; 3 attempts.
>    Do **unit 1 first**, then stop and show me so I can check before you do units 2–8.
> 5. Save everything as **draft**. Do not publish and do not delete anything.

## Tips
- The built-in browser can be slow on long forms. If Claude loses its place, tell it which unit and quiz it was on.
- The 40-question quizzes are the slowest. If it takes too long, check that Tutor LMS imports CSV quiz questions (in newer versions: *Quiz → Import*), and ask Claude to use that.
- If an H5P activity does not show on a page, the activity title was probably changed. Rename it back to the title in `courses/b1/unit-NN/INDEX.md` (the *Slug* column is the title in lower case).
- Record the listening audio from `courses/b1/unit-NN/listening/scripts-to-record.md` and upload it to the Media Library, then tell Claude to add the audio to the Listening pages.
