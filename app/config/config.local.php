<?php
return [
    'driver' => 'sqlite',
    'mysql' => ['host' => 'localhost', 'name' => '', 'user' => '', 'pass' => ''],
    'sqlite' => __DIR__ . '/../var/ef.sqlite',
    'timezone' => 'Europe/Riga',
    'sso_secret' => 'local-dev-secret-local-dev-secret-local-dev-secret-0000',
    'wp_login_url' => '/sso-demo.php',
    'site_name' => 'English Fever',
    'privacy_url' => '#',
    'contact_email' => '', 'site_url' => 'http://127.0.0.1:8099/', 'dashboard_url' => 'http://127.0.0.1:8099/dashboard-demo/', 'register_url' => 'https://example.com/register/',
    'debug' => true,
    'research_enabled' => true, 'experiments' => ['streak', 'leaderboard'], // dev only: the research test needs them
];
