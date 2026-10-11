# English Fever – B1 course

Source and generated files for the B1 course on the English Fever WordPress site (H5P + Tutor LMS).
All instructions and explanations are in easy English.

## Each unit has
| Part | Files |
|---|---|
| 6 lesson pages: grammar, vocabulary, reading, listening, speaking, writing | `courses/b1/unit-NN/lesson-*.html` |
| H5P activities (every practice task has 8+ items; all interactive tasks are H5P) | `dist/h5p/uNN-*.h5p` |
| 3 Tutor LMS quizzes: grammar and vocabulary (pool of 40, 10 random), reading exam, listening exam | `courses/b1/unit-NN/tutor-lms/` |
| Listening scripts to record | `courses/b1/unit-NN/listening/scripts-to-record.md` |
| Speaking interview cards (H5P flashcards + printable) | `courses/b1/unit-NN/speaking/` |

See `courses/b1/course.md` for the unit list and `courses/b1/unit-NN/INDEX.md` for the upload order.

## Instructions for building and importing
- [docs/BUILD-RULES-FOR-NEXT-LEVELS.md](docs/BUILD-RULES-FOR-NEXT-LEVELS.md) – tested rules for layout, H5P, Tutor quizzes (CSV), assignments, QA and the prompt for the next levels (A2, B2, C1).
- [docs/IMPORT-WITH-CLAUDE-DESKTOP.md](docs/IMPORT-WITH-CLAUDE-DESKTOP.md) – importing with the Claude desktop built-in browser.

## Quick import
See [docs/BUILD-RULES-FOR-NEXT-LEVELS.md](docs/BUILD-RULES-FOR-NEXT-LEVELS.md) (sections 9–10) for the tested pipeline.
1. **H5P:** upload the files from `dist/h5p/` (zipped in `dist/all-h5p.zip`). Keep the titles unchanged.
2. **Lessons:** create the 6 lessons per unit from `courses/b1/unit-NN/lesson-*.html` (Tutor LMS lesson editor, HTML view). `dist/wordpress/english-fever-b1-pages.xml` is an alternative that creates ordinary pages.
3. **Assignments:** `courses/b1/unit-NN/assignment/` (`dist/tutor-lms-assignments.zip`).
4. **Quizzes:** import `courses/b1/unit-NN/tutor-lms/*.csv` with Tutor's quiz import (one first, open it, then the rest).
5. **Audio:** `python3 tools/make_audio.py` makes all 16 MP3 files with ElevenLabs (run on your own computer with `ELEVENLABS_API_KEY` set; start with `--dry-run`). See the top of the script.
6. Rebuild: `python3 tools/build.py && python3 tools/make_wxr.py` (`EF_LEVEL=A2 ...` for another level).

## Tutor LMS quiz settings (already inside the CSV)
The `.json` files hold the questions and recommended settings. The `.csv` files are for copy/paste or a spreadsheet import.
**Grammar and vocabulary quiz:** Question order = *Random*; *Max questions allowed to answer* = **10** (the pool has 40). Passing grade 70%, time limit 15 minutes.
**Reading / listening quizzes:** question order = *Sorting*, all questions shown, passing grade 60%. Put the reading text in the quiz description (already in the `.json`).

## Rebuilding
Edit `tools/units/uNN.py`, then run `python3 tools/build.py` (or `python3 tools/build.py 3` for one unit).

## Not yet checked
- The H5P packages are generated from code and have not been uploaded to a live WordPress site. If an upload fails, install the content types first (H5P Hub) and tell us the error.
- The Tutor LMS file format is our own simple format; Tutor's own importer may need the questions entered by hand or pasted from the CSV.
- Audio is not included. Record `listening/scripts-to-record.md` (two voices) and upload the MP3s.
