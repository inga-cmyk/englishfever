<?php
// Dry run of the AI writing check on answers already given (teacher, 3 November): nothing is stored, no learner sees it.
// php tools/ai_dryrun.php attempts-export.csv [max]   (needs ANTHROPIC_API_KEY in the environment)
// Prints, for every open-writing answer: the pattern check's verdict, the AI verdict, and the AI feedback line.
putenv('EF_DEV=1');
require __DIR__ . '/../app/src/bootstrap.php';
[$file, $max] = [$argv[1] ?? '', (int) ($argv[2] ?? 200)];
if (!is_file($file)) { fwrite(STDERR, "usage: php tools/ai_dryrun.php attempts.csv [max]\n"); exit(1); }
if (!AiGrader::enabled()) { fwrite(STDERR, "No ANTHROPIC_API_KEY (or the SDK is missing: composer install -d app).\n"); exit(1); }
$fh = fopen($file, 'r'); $head = fgetcsv($fh, 0, ',', '"', '\\'); $head[0] = preg_replace('/^\xEF\xBB\xBF/', '', $head[0]);
$col = array_flip($head); $n = 0; $agree = 0; $stricter = 0; $looser = 0; $seen = [];
echo "| task | answer | pattern | AI | AI feedback |\n|---|---|---|---|---|\n";
while (($r = fgetcsv($fh, 0, ',', '"', '\\')) !== false && $n < $max) {
    $item = Content::item((string) ($r[$col['item']] ?? ''));
    if (!$item || $item['kind'] !== 'write') continue;
    $ans = (string) $r[$col['answer']];
    if ($ans === '' || $ans === '(skipped)' || isset($seen[$item['id'] . '|' . $ans])) continue;
    $seen[$item['id'] . '|' . $ans] = true;
    $g = Grader::grade($item, $ans);
    $v = AiGrader::check($item, $ans);
    if (!$v) { echo "| {$item['id']} | " . str_replace('|', '/', $ans) . " | " . ($g['correct'] ? 'right' : 'wrong') . " | (no answer) | |\n"; continue; }
    $n++;
    if ($v['correct'] === $g['correct']) $agree++; elseif ($g['correct']) $stricter++; else $looser++;
    echo "| {$item['id']} | " . str_replace('|', '/', $ans) . " | " . ($g['correct'] ? 'right' : 'wrong') . " | " . ($v['correct'] ? 'right' : 'wrong') . " | " . str_replace('|', '/', AiGrader::line($v)) . " |\n";
}
echo "\n$n answers: agree $agree; AI stricter (pattern right, AI wrong) $stricter; AI looser (pattern wrong, AI right) $looser\n";
