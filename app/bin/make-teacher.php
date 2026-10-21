<?php
// Usage: php bin/make-teacher.php <nickname> [password]
// Creates a teacher account (or promotes an existing nickname account). Run it once on the server over SSH,
// or use the hPanel terminal. Teachers who sign in through englishfever.com are made teachers automatically
// (WordPress administrators and Tutor LMS instructors), so this is only needed for a nickname-based teacher.
if (PHP_SAPI !== 'cli') { http_response_code(404); exit; }
chdir(__DIR__ . '/..');
putenv('EF_DEV=1');
require __DIR__ . '/../src/bootstrap.php';
$nick = $argv[1] ?? null;
if (!$nick) { fwrite(STDERR, "Usage: php bin/make-teacher.php <nickname> [password]\n"); exit(1); }
$key = mb_strtolower($nick);
$u = Db::one('SELECT * FROM users WHERE nickname_key = ?', [$key]);
if ($u) {
    Db::update('users', ['role' => 'teacher'], 'id = ?', [$u['id']]);
    echo "Promoted existing user '{$u['nickname']}' to teacher.\n";
} else {
    $pass = $argv[2] ?? null;
    if (!$pass) { fwrite(STDERR, "User does not exist. Give a password: php bin/make-teacher.php $nick <password>\n"); exit(1); }
    $nick = Auth::validNickname($nick);
    Db::insert('users', ['provider' => 'local', 'nickname' => $nick, 'nickname_key' => $key, 'pass_hash' => password_hash($pass, PASSWORD_DEFAULT), 'role' => 'teacher', 'created_at' => time(), 'last_seen' => time()]);
    echo "Created teacher '$nick'.\n";
}
