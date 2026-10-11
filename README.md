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

## Tutor LMS quiz settings
The `.json` files hold the questions and recommended settings. The `.csv` files are for copy/paste or a spreadsheet import.
**Grammar and vocabulary quiz:** Question order = *Random*; *Max questions allowed to answer* = **10** (the pool has 40). Passing grade 70%, time limit 15 minutes.
**Reading / listening quizzes:** question order = *Sorting*, all questions shown, passing grade 60%. Put the reading text in the quiz description (already in the `.json`).

## Rebuilding
Edit `tools/units/uNN.py`, then run `python3 tools/build.py` (or `python3 tools/build.py 3` for one unit).

## Not yet checked
- The H5P packages are generated from code and have not been uploaded to a live WordPress site. If an upload fails, install the content types first (H5P Hub) and tell us the error.
- The Tutor LMS file format is our own simple format; Tutor's own importer may need the questions entered by hand or pasted from the CSV.
- Audio is not included. Record `listening/scripts-to-record.md` (two voices) and upload the MP3s.
