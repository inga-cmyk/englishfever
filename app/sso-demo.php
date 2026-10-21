<?php
// LOCAL TESTING ONLY. Pretends to be the WordPress plugin. Refuses to run anywhere except PHP's built-in server.
if (PHP_SAPI !== 'cli-server') { http_response_code(404); exit; }
require __DIR__ . '/src/bootstrap.php';
$teacher = !empty($_GET['teacher']);
$uid = (int) ($_GET['uid'] ?? 501);
$tok = Auth::signToken(['uid' => $uid, 'name' => $_GET['name'] ?? 'Demo Student', 'teacher' => $teacher, 'exp' => time() + 120, 'n' => bin2hex(random_bytes(8))], Config::get('sso_secret'));
header('Location: sso.php?token=' . $tok);
