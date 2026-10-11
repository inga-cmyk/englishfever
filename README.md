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

## Quick import (about 15 minutes)
1. **H5P:** WordPress admin > H5P Content > Add New > Upload. Upload the 104 files from `dist/h5p/` (all zipped in `dist/all-h5p.zip`). Keep the titles unchanged.
2. **Pages:** Tools > Import > WordPress (install the importer if asked). Choose `dist/wordpress/english-fever-b1-pages.xml`. This creates 57 draft pages (course page, 8 unit pages, 48 lessons). The H5P activities are embedded with `[h5p slug="..."]`, which matches the H5P titles. Check that a lesson page shows its activities, then publish.
3. **Audio:** record `listening/scripts-to-record.md` and upload the MP3s to `wp-content/uploads/english-fever/` (names are in each script file).
4. **Quizzes:** create the Tutor LMS quizzes from `dist/tutor-lms-quizzes.zip` (settings below).
5. Regenerate everything with `python3 tools/build.py && python3 tools/make_wxr.py`.

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
