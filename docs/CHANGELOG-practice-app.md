# Practice app: what each package contains

The version in the app footer ("Version 2026-10-21 18:40") is the time the zip was made. Compare it with the entries below to see what is live. Upload when a batch is worth it; nothing here is urgent unless marked.

## Fixes and polish (not uploaded yet; goes on top of the packages below)
- **Quiet Home:** one main card with one button (*Find my level* for a new learner, *Practise now* afterwards, *Continue where you stopped* with an unfinished session), three small links, one muted line (XP and accuracy). The four stat tiles are gone (streak and time are in the top bar), the three option cards are links, and *Your topics* and *My progress* are folded until opened (remembered on the device). The home-screen card shows after the first answers; *My dashboard ↗* stays in the Home links on phones. Greeting: "Welcome, Anna" for a new learner, "Welcome back, Anna" afterwards.
- **One instruction for the Evaluate tasks:** 51 multiple-choice tasks that asked *What is the best advice?* / *Which sentence is best?* now say **Choose the correct option.** (the scenario stays: *Your colleague says: 'He go to the gym on Mondays.' Choose the correct option.*); 3 say *Choose the most formal / most polite option.* Questions that ask something specific (*Why do we say…?*, *Which one tells us…?*, true/false) are unchanged.
- **Plugin 1.6.0 (upload it; fixes people landing on the Tutor dashboard instead of the app):** after **registering or signing in from the app**, the next website page leads straight back into the app, even when the login form ignores `redirect_to`. New: *Sign in* leaves the same marker that *Create account* does, and a new account created from the app keeps a note on the account, so it works when the email confirmation opens in another browser, days later (bar after 24 hours, nothing after 3 days). Administrators, instructors and people who did not come from the app are never redirected. Tested in `tests/wp_integration_test.py` (cross-browser registration, sign-in, expiry).
- **Topic list:** fold-away areas (the one practised last is open), only topics in reach are listed with *Show topics for higher levels (N)* for the rest, *Practise* starts a session in that topic at once (*Options* opens the picker), cards say *New / Started / ≈ level* and "2 done · 100% correct" instead of "2 tasks". Same rule in the picker.
- **Sound, off by default:** soft tones for right / wrong / almost / finished, switch in Profile and a speaker button in the session; kept on the device; made in the browser.
- **Examples in italics** in all explanations, English and Latvian, in the feedback and on the rule cards (for example, in *Pēc does lieto pamatformu: start, nevis starts* the English words are italic): marked in the data and checked by the build; see PRACTICE-APP.md (Maintenance).
- **Look back at earlier tasks** (read-only): numbered dots under the progress bar (green = correct, pink dashed = not correct, gold ring = where you are) and a *‹ Previous* link. Clicking an answered task shows the question, the saved answer (also for drag-and-drop tasks) and the feedback; *Back to task N* returns. Answers cannot be changed afterwards: they are already recorded and decide the next task. The list survives a reload in the same tab.
- **Stuck drag copy fixed:** a floating word could stay on the screen (even over the next task). It is now removed in every case (release outside the card or window, Escape, window loses focus, a new press, a new page).
- **Writing tasks no longer ask for more than the instruction:** removed the time word (*He works hard.* was marked wrong), time phrase, *will*, *Start with If* and comma requirements that the task text never mentioned (7 tasks).
- **Sentence tasks:** a missing plural -s after a preposition (*on Sunday* for *on Sundays*) is accepted with a tip; a sentence that is right except for one word says *Almost – one word to check* and names the word.
- **Latvian terms:** *darāmā kārta / ciešamā kārta*, *teikuma priekšmets* (short *teik. priekšmets* in formulas), *jautājamais vārds*; see LATVIAN-TERMS.md for what was checked and what stays as teaching shorthand.
- **Top bar always fits** (it ran off the right edge for guests and on narrow computer windows); install hint says *phone* on phones and shows *Install the app on this computer* only where the browser offers it.
- Livelier cards and buttons (hover lift and glow, one gentle pulse on the main action).

## Research package (not uploaded yet; goes on top of the grammar batch)
- **Learning study, off by default** (`research_enabled` in `config.php`): registered learners are invited on Home and can join or leave in Profile. Only people who joined are randomised and exported.
- **Random conditions:** *streak counter* and *leaderboard* can each be hidden for half of the participants (`experiments` in `config.php`; shuffled blocks of four; same conditions if someone leaves and joins again).
- **Research export** on the teacher page: `people.csv`, `days.csv`, `answers.csv` and a codebook; no names or typed answers, no calendar dates, data from the moment of consent only.
- **Livelier cards and buttons:** cards lift and glow under the mouse (shadow, gold edge; in dark mode a gold glow), buttons rise and glow, arrows nudge forward; the main action on Home (practise now, or the placement test for a new learner) pulses twice gently. Touch screens get the pulse only; nothing moves for people who ask their device to reduce motion.
- Needs one new line of config only if you want it on; new database columns and table are created automatically. Docs: PRACTICE-APP.md (Learning study) and RESEARCH-DESIGN.md. Tests: `app/tests/research_test.py`.

## Grammar batch (not uploaded yet)
- **New topics:** conditionals (zero, first, second, third, mixed, advanced), reported speech (statements, questions and requests, reporting verbs) and indirect questions (polite and embedded). 11 topics, 201 new tasks, up to **C1.2**. Levels B2.1, B2.2, C1.1, C1.2 exist now.
- **New menu:** the practice picker groups topics into five areas (fold-away sections, *Select all*, counters) with eight levels. **Surprise me** (Home and Practice) picks topics from the learner's own mistakes and weak spots.
- **Placement:** Quick (12), Medium (24) and Full (40). The level is now fitted to all answers (more accurate, especially for strong learners); the old "below 35 percent means A2.1" rule is gone.
- **Drag-and-drop tasks:** word order, matching and word-bank gaps; mouse, touch and keyboard.
- **Latvian explanations up to B1.2** (334 tasks and 20 rule cards): button *Latviski* on the feedback, setting in Profile, rule cards page. Needs a Latvian teacher's review.
- **Link to the englishfever.com dashboard:** top bar (computers), Home and Profile-adjacent greeting; set `dashboard_url` in `config.php`.
- Answer boxes and the answer sanitiser: odd answers (lists, huge text, objects) count as wrong, never as an error.
- **Plugin 1.5.1:** the homepage banner text now says A2.1 – C1 (the banner can also be given its own text in the shortcode). Upload is optional.
- Placement review tests: `app/tests/sim.py` has learners from A2.1 to C1.

## Next package (not uploaded yet)
- Spelling policy: missing apostrophes, capital letters and safe one-letter typos accepted with a tip (`'spelling' => 'strict'` switches it off).
- A2.1 "evaluate" tasks reworded to "Is this sentence correct?".
- Version label in the footer, this changelog.
- Link back to englishfever.com (`site_url` in `config.php`) in the top bar and footer.
- Installable on iPhone and Android (home screen icon, full screen, offline message): manifest, icons, service worker, install hint on phones and in Profile. Guest chip and brand fit small phones.
- **Security hardening** (see SECURITY.md): answers in a `.php` file, bot trap and rate limits for guests and scripted answers, teacher access expires after 24 h without a website login, teacher can hide/rename names, HSTS, strict sessions, `object-src 'none'`.
- **Guest to registered, the return trip:** `register.php` marker + **plugin 1.3.0** sends new registrants straight back into the app; one-time welcome message with what moved over; sign-in lasts 90 days after the last visit.
- **Avatars** (no photos): ten stylish people (including a blonde lady), a superhero pair, a detective, a monocled gentleman, a bard, a guard, a professor, a fox and a flame with sunglasses, eight symbols or the initial, on six background colours; collapsible picker in Profile; anyone who has not chosen gets a fixed random symbol; shown in the top bar, home, leaderboard and teacher pages; guest avatars move with the guest.
- **Teacher filter:** My students / Registered / Everyone (tiles, list and CSV export follow it); My students = enrolled in your Tutor courses (plugin 1.5.0 asks the website) plus anyone you add by hand; guests show when they were first seen.
- **Spelling:** a slip in the stem of an inflected verb is a spelling tip, not a mistake (`ariving` for *arriving*, `stoped`, `writen`); endings must still be exact.
- **Registration with email confirmation:** the return marker lasts 3 days; straight back into the app within 30 minutes, a "Back to your practice" bar (with a close button) after that; the app shows "Account created? Confirm the email, then sign in" to guests who pressed Create account. Plugin version is now **1.5.0**.
- **Shorter screens:** helper sentences removed (leaderboard, profile, name, data, welcome, placement, practice); the privacy policy link stays.
- **Answer boxes grow** with what is typed (gap boxes widen, the writing box gets taller).
- **Plugin 1.5.0** (includes 1.4.0, 1.3.0 and 1.2.0; upload it too): the guest-friendly `?ef_practice=open` link for menus and the homepage, `[ef_practice_banner]` homepage block (English and Latvian), button now uses the open link.

## Practice time and results on the website (plugin 1.1.0 + app)
- Practice time goes into "My activity" (needs `wp_sync_url` in `config.php` and plugin 1.1.0); `[ef_practice_results]` card; consent respected; teacher status line; `bin/sync-wp.php` for cron.

## Guests, names, registration
- Guests with an optional name; registered students continue with their website account and confirm how their name is shown; popup inviting guests to register, guest results move into the new account; guests purged after 60 days.

## First release
- 13 tenses A2.1–B1.2 (241 tasks, all six Bloom levels), placement test, adaptive practice, feedback with rule cards, time/streak/XP/leaderboard, teacher view, Tutor LMS login.
