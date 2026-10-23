<?php
declare(strict_types=1);

require __DIR__ . '/Db.php';
require __DIR__ . '/Auth.php';
require __DIR__ . '/Content.php';
require __DIR__ . '/Grader.php';
require __DIR__ . '/Engine.php';
require __DIR__ . '/Stats.php';
require __DIR__ . '/Research.php';
require __DIR__ . '/Reports.php';
require __DIR__ . '/Mistakes.php';
require __DIR__ . '/CustomItems.php';
require __DIR__ . '/Wp.php';

Config::load();
date_default_timezone_set(Config::get('timezone', 'Europe/Riga'));
Db::connect(Config::all());
Db::migrate();
Auth::firstNameSweep();

$https = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') || (($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https');
$sessDir = __DIR__ . '/../var/sessions';
if (!is_dir($sessDir)) @mkdir($sessDir, 0770, true);
if (is_dir($sessDir) && is_writable($sessDir)) session_save_path($sessDir);
$keep = 60 * 60 * 24 * 90;                 // people stay signed in for 90 days after their last visit
ini_set('session.gc_maxlifetime', (string) $keep);
ini_set('session.use_strict_mode', '1');   // the server never accepts a session id it did not create
ini_set('session.use_only_cookies', '1');
session_name('efp');
// Cookie only for the folder the app lives in (matters when it runs in a folder of the WordPress site, e.g. /practice/).
$cookiePath = rtrim(str_replace('\\', '/', dirname($_SERVER['SCRIPT_NAME'] ?? '/')), '/') . '/';
session_set_cookie_params([
    'lifetime' => $keep, 'path' => $cookiePath, 'secure' => $https, 'httponly' => true, 'samesite' => 'Lax',
]);
session_start();
if (!empty($_SESSION['uid']) && time() - (int) ($_SESSION['_c'] ?? 0) > 86400) { // renew the cookie once a day: 90 days from the last visit
    $_SESSION['_c'] = time();
    setcookie(session_name(), session_id(), ['expires' => time() + $keep, 'path' => $cookiePath, 'secure' => $https, 'httponly' => true, 'samesite' => 'Lax']);
}
if (random_int(1, 200) === 1) Auth::purgeGuests(); // housekeeping: guests inactive for 60 days
