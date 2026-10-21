<?php
// "Create a free account" goes through here: it leaves a short-lived marker ("this person came from the practice app"),
// then sends them to the website's registration form. After they register, the website plugin sees the marker and
// sends them straight back into the app, where their guest results are moved to the new account.
require __DIR__ . '/src/Auth.php'; // defines Config
Config::load();
$to = (string) Config::get('register_url', '');
if ($to === '') { http_response_code(404); exit; }

$https = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') || (($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https');
$host = strtolower(preg_replace('/:\d+$/', '', $_SERVER['HTTP_HOST'] ?? ''));
$site = strtolower((string) parse_url((string) Config::get('site_url', ''), PHP_URL_HOST));
// shared with the website only when the app is on the same domain (practice.englishfever.com <-> englishfever.com)
$domain = ($site !== '' && !filter_var($site, FILTER_VALIDATE_IP) && $site !== 'localhost' && ($host === $site || substr($host, -strlen('.' . $site)) === '.' . $site)) ? $site : '';
setcookie('ef_return', (string) time(), [
    'expires' => time() + 1800, 'path' => '/', 'domain' => $domain, 'secure' => $https, 'httponly' => true, 'samesite' => 'Lax',
]);
header('Cache-Control: no-store');
header('Location: ' . $to);
exit;
