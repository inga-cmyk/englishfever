<?php
// Sends practice time to the englishfever.com "My activity" tracker for every student who has something pending.
// The app already does this by itself while students practise. Run this from a cron job (for example every 15 minutes
// in hPanel > Advanced > Cron Jobs) so the last minutes of a session are never left waiting:
//     /usr/bin/php /home/USER/domains/englishfever.com/public_html/practice/bin/sync-wp.php
if (PHP_SAPI !== 'cli') { http_response_code(404); exit; }
chdir(__DIR__ . '/..');
require __DIR__ . '/../src/bootstrap.php';
if (!Wp::configured()) { fwrite(STDERR, "wp_sync_url is not set in config/config.php\n"); exit(1); }
$r = Wp::syncPending();
$st = Wp::status();
echo "students: {$r['users']}, sent: {$r['ok']}, errors: {$r['errors']}" . ($st['last_error'] ? "\nlast error: {$st['last_error']}" : '') . "\n";
exit($r['errors'] ? 2 : 0);
