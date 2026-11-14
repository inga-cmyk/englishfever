<?php
// php tools/grade_items.php IN.json OUT.json
// Grades answers with the app's own grader (tools/blind_check.py compare): IN = [{"item": {...}, "answer": ...}], OUT = [true|false, ...].
chdir(__DIR__ . '/../app'); putenv('EF_DEV=1');
require 'src/Auth.php';
spl_autoload_register(function ($c) { $f = 'src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load();
$in = json_decode(file_get_contents($argv[1]), true); $out = [];
foreach ($in as $x) {
    $it = $x['item']; $a = $x['answer'];
    if ($it['kind'] === 'order' && is_string($a)) $a = preg_split('/\s+/', trim(preg_replace('/[.?!]$/', '', $a)));
    if ($it['kind'] === 'gap' && is_string($a)) $a = array_map('trim', explode('/', $a));
    if ($it['kind'] === 'text' && is_array($a)) $a = (string) ($a[0] ?? '');
    try { $g = Grader::grade($it, $a); $out[] = (bool) ($g['correct'] ?? false); } catch (Throwable $e) { $out[] = false; }
}
file_put_contents($argv[2], json_encode($out));
