# Brief for the AI agent that works in the WordPress admin of englishfever.com

Copy everything below the line into the agent. Do the hosting steps (wp-config.php, the app's config.php, the app zip) yourself in Hostinger; they are not in this brief.

---

You are helping the owner of englishfever.com (WordPress + Tutor LMS, Latvian by default, English pages under /en/, a language plugin) make a new grammar practice app easy to find. You work in the WordPress admin, logged in as an administrator. The app lives at https://practice.englishfever.com and a plugin called "EF Practice" connects it to the website.

## Rules
- Do only the tasks below, in this order. Change nothing else: no users, no passwords, no payment or Tutor LMS settings, no theme or plugin files, no other plugins or updates, no deletions.
- Never read out, copy or type any secret, key or password. You will not need any.
- Before each task, say what you are about to do. After each task, take a screenshot as proof.
- Anything public (homepage, menus, footer): make the change in a **draft or preview first**, show the owner a screenshot, and **publish only after the owner says yes**.
- If a screen looks different from what is described, or something would fail, **stop and ask**. Do not improvise.
- Keep the owner's wording style: short, friendly, simple English.

The practice link (call it LINK) is exactly:
`https://englishfever.com/practice-login/?ef_practice=open`
Use it unchanged. It must open in the same tab. It takes logged-in students straight into the app and visitors to the app's welcome page.

## Tasks

**1. Plugin (only if you can upload a file from the owner's computer; otherwise skip and tell the owner)**
Plugins → Add New Plugin → Upload Plugin → choose `ef-practice-sso.zip` (the owner provides it) → Install Now → "Replace current with uploaded" → keep it **active**. Check that the plugin list shows "EF Practice – sign in with englishfever.com" at **version 1.4.0 or newer**. Report the version.

**2. The "Practice login" page**
Pages: a page with slug `practice-login` should exist and be published, with one Shortcode block containing `[ef_practice_button label="Start practising"]`. If it exists, leave it; just report. If an SEO plugin is installed, set this page to noindex. Do **not** add this page to any menu.

**3. Main menu, every language**
Appearance → Menus (or Site Editor → Navigation). In each language's main menu add one **Custom Link**:
- Latvian menu: label `Gramatikas prakse`, URL = LINK
- English menu: label `Grammar practice`, URL = LINK
Place it right after the course link ("Atrast kursu" / its English equivalent). Check that it also appears in the mobile menu. Show the owner a screenshot of the menu before saving the final order.

**4. Footer**
In the footer column "MĀCIES" (English: the same column), add a link with the same URL = LINK: `Gramatikas prakse` / `Grammar practice`. Use the theme's normal way to edit the footer (Customizer, widget, Site Editor, or footer menu). If the footer can only be changed by editing theme code, do not do that: report it instead.

**5. Homepage banner (Latvian homepage and English homepage)**
Edit each homepage. Below the top (hero) section, add one **Shortcode** block (or the page builder's shortcode widget):
- Latvian homepage: `[ef_practice_banner lang="lv"]`
- English homepage: `[ef_practice_banner lang="en"]`
Preview it on desktop and phone width and show the owner screenshots. The block is a black panel with a gold heading and a raspberry button. Do not restyle it. **Publish only after the owner approves the position.**

**6. Caching**
If the LiteSpeed Cache plugin is active: LiteSpeed Cache → Cache → Excludes → "Do Not Cache Query Strings" → add `ef_practice`, save, then purge all caches. If a different caching plugin is active, do not change it; report its name.

**7. Student dashboard card (Code Snippets) — only with the owner's explicit yes**
Snippets → open the active snippet "EF: My activity on student Home". First copy its full text into your report as a backup. Find the line `echo $report;` (inside `add_action( 'wp_footer', function () {`). Directly after it add exactly this one line, nothing else:
`if ( shortcode_exists( 'ef_practice_results' ) ) { echo do_shortcode( '[ef_practice_results plain="1"]' ); }`
Save. Then open the student dashboard Home (https://englishfever.com/en/dashboard/) and check that the page still loads and "My activity" is still shown. If anything breaks, restore the backup text immediately and tell the owner.

**8b. Registration with email confirmation (check only, change nothing)**
Register a test student on https://englishfever.com/en/register/ (use an address the owner provides). Report: (a) which plugin or setting sends the confirmation email, (b) what the new user sees after the form, (c) whether clicking the email link logs the user in, and (d) which page they land on. Do not change any settings; the owner decides.

**8c. Social login (optional, only after the owner's yes)**
If Tutor LMS Pro is active: Tutor LMS Pro → Add-ons → enable "Social Login", then Tutor LMS Pro → Settings → Authentication → turn on **Google only** (the owner supplies the Google Client ID). Otherwise install the free plugin "Nextend Social Login" and enable Google only. Set the default role for new users to the same role normal registrations get, make sure the login returns to the page the person came from (`redirect_to`), and test with a Google account: the user must be created as a normal website user and the practice link LINK must then sign them in. Report what you see.

**8. "My activity" page (optional)**
On the page https://englishfever.com/my-activity/, below the existing `[ef_my_activity]` shortcode, add a Shortcode block `[ef_practice_results]`. Preview first; publish after the owner's yes.

## Do NOT touch
The snippet "Optional activity consent and withdrawal" (its wording is legal text and stays with the owner), `wp-config.php`, Hostinger settings, any other snippet.

## Final check (as the logged-in administrator)
Open the menu link LINK. You should land in the practice app signed in as a teacher, with **Students** in the app's top bar. Report what you see. (The owner will test the visitor view in a private window.)

## Report back
For every task: done / skipped / problem, a screenshot, and anything that looked different from this brief.
