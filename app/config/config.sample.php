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

    // Shown in the footer and the privacy note.
    'site_name'   => 'English Fever',
    'privacy_url' => 'https://www.englishfever.com/privacy-policy/',
    'contact_email' => '',

    // Set true while testing locally (no HTTPS).
    'debug' => false,
];
