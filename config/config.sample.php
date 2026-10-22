<?php
// Copy this file to config/config.php and fill it in. config.php is never committed.
return [
    // 'sqlite' for local testing, 'mysql' on Hostinger.
    'driver'   => 'mysql',
    'mysql'    => [
        'host' => 'localhost',
        'name' => 'u123456789_practice',
        'user' => 'u123456789_practice',
        'pass' => 'CHANGE-ME',
    ],
    'sqlite'   => __DIR__ . '/../var/ef.sqlite',

    'timezone' => 'Europe/Riga',

    // Shared secret with the WordPress plugin (ef-practice-sso). Use 64 random hex characters.
    // Generate one with: php -r "echo bin2hex(random_bytes(32)), PHP_EOL;"
    'sso_secret' => 'CHANGE-ME',

    // Where "Sign in with englishfever.com" sends people (the page that has the [ef_practice_button] shortcode).
    'wp_login_url' => 'https://www.englishfever.com/practice-login/',

    // Optional: send practice time to the "My activity" tracker on englishfever.com (needs plugin ef-practice-sso 1.1 or newer).
    // Leave empty to switch the link off.
    'wp_sync_url' => 'https://englishfever.com/wp-json/ef-practice/v1/activity',

    // Optional: where people without an englishfever.com account can register (shown under the sign-in button).
    'register_url' => 'https://englishfever.com/en/register/',

    // 'forgiving' (default): missing apostrophes, capital letters and one-letter typos in words copied from the task are
    // accepted, with a spelling tip. 'strict': only exact answers (capital letters still never matter).
    'spelling' => 'forgiving',

    // Link back to the website (footer and top bar of the app).
    'site_url' => 'https://englishfever.com/',
    'dashboard_url' => 'https://englishfever.com/en/dashboard/', // the student dashboard: the app links to it (top bar, Home)

    // Learning study (research). Off by default. When on, registered learners are invited to take part; only people who agree
    // are randomised to the conditions listed under 'experiments' and appear in the research export (teacher page, Students).
    // Switch it on only when your ethics review and information sheet are ready, and replace the default wording with the approved text.
    // The "test version" notice for everyone (top bar, Home, welcome page). Set to false when the tasks are checked.
    'beta_notice' => true,

    'research_enabled' => false,
    'experiments' => [],            // any of: 'streak' (daily streak counter), 'leaderboard'. Half of the participants get the feature hidden.
    'research_info_url' => '',      // page with the information sheet (shown as a link in the invitation)
    // 'research_text' => "Paragraph one.\n\nParagraph two.",      // optional: your own wording (English)
    // 'research_text_lv' => "Pirmā rindkopa.\n\nOtrā rindkopa.",  // optional: your own wording (Latvian)

    // Shown in the footer and the privacy note.
    'site_name'   => 'English Fever',
    'privacy_url' => 'https://www.englishfever.com/privacy-policy/',
    'contact_email' => '',

    // Set true while testing locally (no HTTPS).
    'debug' => false,
];
