# Practice app: what each package contains

The version in the app footer ("Version 2026-10-21 18:40") is the time the zip was made. Compare it with the entries below to see what is live. Upload when a batch is worth it; nothing here is urgent unless marked.

## Next package (not uploaded yet)
- Spelling policy: missing apostrophes, capital letters and safe one-letter typos accepted with a tip (`'spelling' => 'strict'` switches it off).
- A2.1 "evaluate" tasks reworded to "Is this sentence correct?".
- Version label in the footer, this changelog.
- Link back to englishfever.com (`site_url` in `config.php`) in the top bar and footer.
- Installable on iPhone and Android (home screen icon, full screen, offline message): manifest, icons, service worker, install hint on phones and in Profile. Guest chip and brand fit small phones.
- **Security hardening** (see SECURITY.md): answers in a `.php` file, bot trap and rate limits for guests and scripted answers, teacher access expires after 24 h without a website login, teacher can hide/rename names, HSTS, strict sessions, `object-src 'none'`.
- **Plugin 1.2.0** (upload it too): the guest-friendly `?ef_practice=open` link for menus and the homepage, `[ef_practice_banner]` homepage block (English and Latvian), button now uses the open link.

## Practice time and results on the website (plugin 1.1.0 + app)
- Practice time goes into "My activity" (needs `wp_sync_url` in `config.php` and plugin 1.1.0); `[ef_practice_results]` card; consent respected; teacher status line; `bin/sync-wp.php` for cron.

## Guests, names, registration
- Guests with an optional name; registered students continue with their website account and confirm how their name is shown; popup inviting guests to register, guest results move into the new account; guests purged after 60 days.

## First release
- 13 tenses A2.1–B1.2 (241 tasks, all six Bloom levels), placement test, adaptive practice, feedback with rule cards, time/streak/XP/leaderboard, teacher view, Tutor LMS login.
