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
// relabelled built-in tasks: out of the active pool once their copy is approved, still readable for old answers
$active = array_column(Content::items(), null, 'id');
$have = array_flip(array_map(fn($it) => $it['skill'] . '|' . mb_strtolower($it['q']), array_filter(Content::items(), fn($it) => strpos($it['id'], 'c-') === 0 && strpos($it['level'], 'A2') === 0)));
foreach (array_keys(Content::relabelled()) as $rid) {
    $orig = Content::item($rid);
    if (!$orig) { $bad++; echo "relabelled task unreadable: $rid\n"; continue; }
    $copyExists = isset($have[$orig['skill'] . '|' . mb_strtolower($orig['q'])]);
    if ($copyExists && isset($active[$rid])) { $bad++; echo "relabelled task still active: $rid\n"; }
    if (!$copyExists) { $bad++; echo "no approved A2 copy for relabelled task: $rid\n"; }
}
echo "$n custom tasks graded, ", $bad ? "$bad mismatches" : "every answer graded as expected", "\n";
exit($bad ? 1 : 0);
