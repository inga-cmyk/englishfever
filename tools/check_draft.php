<?php
// Checks one prepared-questions CSV before anyone imports it (nothing is saved anywhere: an in-memory database):
//   php tools/check_draft.php docs/task-drafts/pending/twins-2.csv
// 1. the importer accepts every row (the same check as Questions → Add on the server);
// 2. every typed answer in the key is graded right, also with curly apostrophes, without the final full stop and with n't written as "not".
$csv = realpath($argv[1] ?? '') ?: exit("Usage: php tools/check_draft.php FILE.csv\n");
chdir(__DIR__ . '/../app'); putenv('EF_DEV=1');
require 'src/Auth.php';
spl_autoload_register(function ($c) { $f = 'src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load(); Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']); Db::migrate();
$r = CustomItems::import(file_get_contents($csv), true);
echo "import: {$r['ok']} accepted, {$r['bad']} refused\n";
foreach ($r['rows'] as $x) if (!$x['ok'] || $x['warnings']) echo "  line {$x['line']}: {$x['q']} :: " . implode('; ', array_merge($x['errors'], $x['warnings'])) . "\n";
$n = 0; $bad = 0;
foreach ($r['rows'] as $row) {
    $it = !empty($row['id']) ? CustomItems::find($row['id']) : null;
    if (!$it || !in_array($it['kind'], ['text', 'gap'], true) || !empty($it['bank']) || count($it['answers']) > 1) continue;
    foreach ($it['answers'][0] as $a) {
        foreach (array_unique([$a, str_replace("'", "\u{2019}", $a), rtrim($a, '.'), str_replace(["couldn't", "can't", "didn't", "don't", "wouldn't", "hadn't"], ["could not", "cannot", "did not", "do not", "would not", "had not"], $a)]) as $v) {
            $n++; $g = Grader::grade($it, $it['kind'] === 'gap' ? [$v] : $v);
            if (empty($g['correct'])) { $bad++; echo "  REFUSED: {$it['q']} :: $v\n"; }
        }
    }
}
echo "typed answers: $n variants, $bad refused\n";
