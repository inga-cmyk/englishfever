# Security of the practice app

## Can the app harm a phone or computer?
No more than any website. The app is a web page that runs inside the browser's sandbox. It cannot read the phone's files, contacts or other apps, cannot install anything, and cannot run when it is closed. It asks for no permissions (camera, microphone and location are switched off in the headers). It offers no downloads. It loads no code from other companies, so there is no third-party script that could go bad. On the phone it stores only a login cookie, a small cache of its own screens, and a few settings (such as "install hint hidden"); removing the home-screen icon or clearing site data erases them.

**The real risk is not the learners' device but your server.** If someone broke into the hosting or the WordPress site, they could change the app's files and show learners a fake login or a phishing page. That is why most of the checklist below is about WordPress and your accounts, which are the usual weak point.

## What the app already does
- **Answers never reach the browser** before the learner answers. The answer file is a `.php` file (prints nothing if requested) and a `.htaccess` blocks the folders as well.
- **No passwords** are stored. Registered students sign in with a signed, single-use link from englishfever.com that expires after 2 minutes. Guests have no password.
- **No script injection:** the app never builds pages from learners' text with `innerHTML`; names and answers are always shown as plain text. A strict Content-Security-Policy forbids inline scripts, outside scripts and framing. A hostile name like `<img onerror=…>` is refused for guests and cleaned for website users, and it showed as harmless text in the teacher pages in a test.
- **No SQL injection:** all database queries use bound parameters (checked, and attacked in tests).
- **Forged requests are refused:** every request that changes data needs a custom header; cookies are `HttpOnly`, `SameSite=Lax` and `Secure` on HTTPS; the server only accepts session IDs it created.
- **Bots and abuse:** guests need an unfilled hidden field and a form that took longer than 1.2 s; 100 new guests per hour per connection; 3,000 per day in total; 150 new practice sessions per hour per connection; more than 45 answers in a minute is refused (scripts); a guest's daily limit (600 answers) points to registering.
- **Teachers:** the teacher role only comes from the website's signed link and expires after 24 hours without a new website login, so a teacher whose role you remove loses access within a day. Teachers can hide a name from the leaderboard or replace it with "Learner ####".
- **No way for users to reach each other:** there is no chat, comments or public profile. The only visible names are on the leaderboard (registered learners only, opt-out in Profile). Guests are never shown to other learners.
- **Avatars are a fixed list** (symbol and colour); there are no photo uploads, so no image files to attack or moderate.
- **Data kept small:** guest data is deleted after 60 days without a visit; learners can download or delete their results; the CSV export neutralises spreadsheet formulas.
- **Tested:** `app/tests/security_test.py` (injection, bots, sessions, teacher expiry, moderation), the browser check for script injection, the website-login tests, and the grader tests.

## What it does not do (be aware)
- The bot filters are speed bumps. A determined attacker with many IP addresses can still create guests or flood requests. If that happens, put the site behind Cloudflare (free plan) or turn on Hostinger's protection, and add a CAPTCHA such as Cloudflare Turnstile to the guest form. I can add that.
- The leaderboard can still be gamed by someone who solves tasks slowly with a script. The teacher can hide such a name.
- Names cannot be checked for rudeness automatically. The teacher hides or renames after a report.
- These tests are not an independent security audit. Before you advertise the app widely, have a professional review the setup.
- When AI sentence-checking is added later, learners' sentences go to an AI provider. That needs a data-processing agreement and a line in the privacy policy.

## Launch checklist (you)
1. **Change the two secrets that appeared in our chat and screenshots:** the database password (hPanel → Databases → change password, then the same in `config/config.php`) and the website-login secret (a new 64-character hex value in both `config/config.php` as `sso_secret` and `wp-config.php` as `EF_PRACTICE_SECRET`). I can generate the new value.
2. **Check that the private files are closed.** These must show 403 or "not found": `/config/config.php`, `/src/Engine.php`, `/content/items.php` (it may show a blank page, which is fine), `/var/`.
3. `config.php`: `'debug' => false`.
4. **Two-step login (2FA) on:** WordPress admin accounts, Hostinger, GitHub, and the e-mail address used for them. Strong, unique passwords.
5. **WordPress hygiene:** update WordPress, Tutor LMS and all plugins; delete plugins and themes you do not use; only install plugins you trust.
6. **Hostinger:** HTTPS forced for the site (hPanel → Security → SSL), automatic backups on, and the malware scanner on if your plan has it. Download one manual backup of the database before launch.
7. **Update the privacy policy** (the draft text is in `PRACTICE-APP.md`) and the consent snippet.
8. **Closed test first:** invite 10–20 learners. Watch the teacher page, the "Website activity tracker" line and Hostinger's resource usage for a week.
9. **Know how to switch it off quickly:** in File Manager rename the `practice` folder to `practice-off`. The app is offline at once. Rename it back to restore.
10. **If something looks wrong** (unknown teachers, strange names, a spike of guests, files changed): switch the app off as above, change both secrets and your WordPress admin passwords, check the plugin list and File Manager for files you do not recognise, and restore the latest backup.
