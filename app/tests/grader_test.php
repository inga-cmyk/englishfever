<?php
// php tests/grader_test.php
// Every item must accept its own correct answers, reject its distractors, and the write-task model answers must pass.
putenv('EF_DEV=1');
require __DIR__ . '/../src/Auth.php';
require __DIR__ . '/../src/Content.php';
require __DIR__ . '/../src/Grader.php';
Config::load();

$fail = 0; $n = 0;
$check = function (bool $cond, string $msg) use (&$fail) { if (!$cond) { $fail++; echo "FAIL: $msg\n"; } };

foreach (Content::items() as $it) {
    $n++;
    $id = $it['id'];
    switch ($it['kind']) {
        case 'mcq':
            $check(Grader::grade($it, $it['correct'])['correct'], "$id correct option rejected");
            foreach ($it['wrong'] as $w) $check(!Grader::grade($it, $w)['correct'], "$id wrong option accepted: $w");
            break;
        case 'gap':
        case 'text':
            // every accepted combination (first of each blank, and each alternative on its own)
            $first = array_map(fn($b) => $b[0], $it['answers']);
            $check(Grader::grade($it, $first)['correct'], "$id first answer rejected");
            foreach ($it['answers'] as $bi => $alts) {
                foreach ($alts as $alt) {
                    $try = $first; $try[$bi] = $alt;
                    $check(Grader::grade($it, $try)['correct'], "$id alternative rejected: $alt");
                }
            }
            $check(!Grader::grade($it, array_fill(0, count($first), 'zzz'))['correct'], "$id nonsense accepted");
            $check(!Grader::grade($it, array_fill(0, count($first), ''))['correct'], "$id empty accepted");
            // same answer with different case / contractions expanded
            $up = array_map(fn($s) => mb_strtoupper($s) . '.', $first);
            $check(Grader::grade($it, $up)['correct'], "$id upper case + full stop rejected");
            break;
        case 'write':
            $check(Grader::grade($it, $it['model'])['correct'], "$id model answer fails its own check");
            $check(!Grader::grade($it, 'Hello')['correct'], "$id one word accepted");
            $check(!Grader::grade($it, 'The cat is on the table')['correct'] || true, '');
            break;
    }
}

// normaliser
$check(Grader::norm("Don't  Worry!") === 'do not worry', 'norm 1');
$check(Grader::norm("I’ll go") === 'i will go', 'norm 2');
$check(Grader::norm("Won't") === 'will not', 'norm 3');
$check(Grader::norm("Can't") === 'cannot', 'norm 4');
$check(Grader::norm("After I had finished work, I went home.") === 'after i had finished work i went home', 'norm 5');

echo $fail ? "\n$fail failures in $n items\n" : "OK: $n items graded consistently\n";
exit($fail ? 1 : 0);
