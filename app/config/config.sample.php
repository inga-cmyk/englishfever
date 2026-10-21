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

    // Shown in the footer and the privacy note.
    'site_name'   => 'English Fever',
    'privacy_url' => 'https://www.englishfever.com/privacy-policy/',
    'contact_email' => '',

    // Set true while testing locally (no HTTPS).
    'debug' => false,
];
