<?php
declare(strict_types=1);

require __DIR__ . '/Db.php';
require __DIR__ . '/Auth.php';
require __DIR__ . '/Content.php';
require __DIR__ . '/Grader.php';
require __DIR__ . '/Engine.php';
require __DIR__ . '/Stats.php';

Config::load();
date_default_timezone_set(Config::get('timezone', 'Europe/Riga'));
Db::connect(Config::all());
Db::migrate();

$https = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') || (($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https');
$sessDir = __DIR__ . '/../var/sessions';
if (!is_dir($sessDir)) @mkdir($sessDir, 0770, true);
if (is_dir($sessDir) && is_writable($sessDir)) session_save_path($sessDir);
ini_set('session.gc_maxlifetime', (string) (60 * 60 * 24 * 30));
session_name('efp');
// Cookie only for the folder the app lives in (matters when it runs in a folder of the WordPress site, e.g. /practice/).
$cookiePath = rtrim(str_replace('\\', '/', dirname($_SERVER['SCRIPT_NAME'] ?? '/')), '/') . '/';
session_set_cookie_params([
    'lifetime' => 60 * 60 * 24 * 30, 'path' => $cookiePath, 'secure' => $https, 'httponly' => true, 'samesite' => 'Lax',
]);
session_start();
if (random_int(1, 200) === 1) Auth::purgeGuests(); // housekeeping: guests inactive for 60 days
