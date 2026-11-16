<?php
// php tests/write_have_past_test.php: a writing task with have / has + a past simple form (I have never saw) is not "correct" (tester's report, 16 November)
chdir(__DIR__ . '/..'); putenv('EF_DEV=1');
require 'src/Auth.php'; require 'src/Grader.php'; Config::load();
$item = ['kind' => 'write', 'q' => 'Write about something you have never done.', 'model' => 'I have never seen the Northern Lights.', 'must' => [['\b(have|has|\'ve)\b', 'Use have / has.', 'Lieto have / has.']]];
$cases = ['I have never saw the Northern Lights.' => false, 'I have never seen the Northern Lights.' => true, "She's went to Paris twice." => false,
          'I have been to Rome but I saw only a little.' => true, 'We have just ate dinner.' => false, 'I have a car that I bought last year.' => true,
          "I've never ridden a horse." => true, "I've never rode a horse." => false];
$bad = 0;
foreach ($cases as $ans => $want) {
    $r = Grader::grade($item, $ans);
    if ((bool) $r['correct'] !== $want) { $bad++; echo "FAIL '$ans' wanted " . ($want ? 'right' : 'wrong') . ': ' . json_encode($r) . "\n"; }
}
echo $bad ? "SOME FAILED\n" : "ALL PASS: " . count($cases) . " have + past form checks\n";
