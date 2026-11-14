<?php
// Every task the app can serve (the built-in bank and all prepared files), as the importer reads them, with its role and source:
//   php tools/dump_items.php OUT.json
// Nothing is saved anywhere (an in-memory database). Used by app/tests/item_gates_test.py and for counting.
$out = $argv[1] ?? exit("Usage: php tools/dump_items.php OUT.json\n");
if ($out[0] !== '/') $out = getcwd() . '/' . $out;
chdir(__DIR__ . '/../app'); putenv('EF_DEV=1');
require 'src/Auth.php';
spl_autoload_register(function ($c) { $f = 'src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load(); Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']); Db::migrate();
$items = [];
foreach (Content::items() as $it) { $it['role'] = Content::role($it); $it['point'] = Content::point($it); $it['src'] = 'built-in'; $items[] = $it; }
$src = []; $bad = 0;
foreach (CustomItems::preparedFiles() as $name => $path) {
    $r = CustomItems::import((string) file_get_contents($path), true);
    $bad += $r['bad'];
    foreach ($r['rows'] as $x) if (!empty($x['id'])) $src[$x['id']] = $name . ':' . $x['line'];
}
foreach (Db::all('SELECT item_id FROM custom_items ORDER BY id') as $r) {
    $it = CustomItems::find($r['item_id']); $it['role'] = Content::role($it); $it['point'] = Content::point($it); $it['src'] = $src[$r['item_id']] ?? '?'; $items[] = $it;
}
// a typed sentence with "I had done" / "I would": is the same answer with 'd graded right? (the key must list it when the checker cannot work it out)
foreach ($items as &$it) {
    if ($it['kind'] !== 'text') continue;
    $a = $it['answers'][0][0];
    if (!preg_match('/\b(I|you|he|she|we|they) (would\b|had (\w+ed|been|known|seen|gone|done|taken|left|told|given|had)\b)/i', $a)) continue;
    $v = preg_replace('/\b(I|you|he|she|we|they) (would|had)\b/i', "$1'd", $a);
    $g = Grader::grade($it, $v);
    if (empty($g['correct'])) $it['d_refused'] = $v;
}
unset($it);
file_put_contents($out, json_encode($items, JSON_UNESCAPED_UNICODE));
echo count($items) . " tasks, $bad rows refused\n";
