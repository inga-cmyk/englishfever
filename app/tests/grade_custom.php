<?php
// Grades every approved custom task with its own listed answers: each right answer must be accepted, each wrong option refused.
// Used by tests/drafts_test.py (dev database only).
require __DIR__ . '/../src/bootstrap.php';
$bad = 0; $n = 0;
foreach (Content::items() as $it) {
    if (strpos($it['id'], 'c-') !== 0) continue;
    $n++;
    $answers = [];
    switch ($it['kind']) {
        case 'mcq': $answers[] = [$it['correct'], true]; foreach ($it['wrong'] as $w) $answers[] = [$w, false]; break;
        case 'gap':
            $answers[] = [array_map(fn($b) => $b[0], $it['answers']), true];
            if (count($it['answers']) === 1) foreach ($it['answers'][0] as $alt) $answers[] = [[$alt], true];
            $answers[] = [array_fill(0, count($it['answers']), 'zzz'), false];
            break;
        case 'text': foreach ($it['answers'][0] as $a) $answers[] = [$a, true]; $answers[] = ['zzz qqq', false]; break;
        case 'order': $answers[] = [explode(' ', $it['sentence']), true]; $answers[] = [array_reverse(explode(' ', $it['sentence'])), false]; break;
        case 'match': $answers[] = [array_column($it['pairs'], 1), true]; $answers[] = [array_reverse(array_column($it['pairs'], 1)), false]; break;
    }
    foreach ($answers as [$a, $want]) {
        $r = Grader::grade($it, $a);
        if ((bool) $r['correct'] !== $want) { $bad++; echo "MISMATCH {$it['id']} ({$it['q']}) ", json_encode($a), " wanted ", $want ? 'right' : 'wrong', "\n"; }
    }
}
echo "$n custom tasks graded, ", $bad ? "$bad mismatches" : "every answer graded as expected", "\n";
exit($bad ? 1 : 0);
