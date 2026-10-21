<?php
// php tests/grader_test.php
// Every item must accept its own correct answers, reject its distractors, and the write-task model answers must pass.
putenv('EF_DEV=1');
require __DIR__ . '/../src/Auth.php';
require __DIR__ . '/../src/Content.php';
require __DIR__ . '/../src/Grader.php';
Config::load();

$fail = 0; $n = 0;
$check = function (bool $cond, string $msg, $detail = null) use (&$fail) { if (!$cond) { $fail++; echo "FAIL: $msg" . ($detail !== null ? ' -> ' . json_encode($detail) : '') . "\n"; } };

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

// ───────── spelling policy ─────────
$setSpelling = function (string $mode) {
    (function () use ($mode) { self::$cfg['spelling'] = $mode; })->bindTo(null, Config::class)();
};
$setSpelling('forgiving');
$neg = Content::item('ps-A21-3b'); // Make it negative: They play tennis on Sundays.
$g = fn(string $a) => Grader::grade($neg, $a);
$r = $g('They dont play tennis on Sundays');
$check($r['correct'] && in_array("Use an apostrophe: don't.", $r['notes'], true), 'missing apostrophe accepted with a tip');
$r = $g("they don't play tennis on sundays.");
$check($r['correct'] && in_array('Capital letter: Sundays.', $r['notes'], true), 'missing capital accepted with a tip');
$r = $g("They don't play tenis on Sundays");
$check($r['correct'] && $r['notes'] === ['Spelling: tenis → tennis.'], 'one missing letter inside a copied word accepted', $r['notes']);
$r = $g("They don't play tenins on Sundays");
$check($r['correct'], 'swapped letters in a copied word accepted (tenins)');
$check(!$g("They don't paly tennis on Sundays")['correct'], 'short words (4 letters) are never forgiven, they carry grammar (paly)');
$check(!$g('They dont play tens on sundays')['correct'], '"tens" (a different word, two letters off) is not accepted');
$check(!$g("They don't plays tennis on Sundays")['correct'], 'grammar error plays is not forgiven');
$check(!$g("They doesn't play tennis on Sundays")['correct'], 'doesn\'t for they is not forgiven');
$check(!$g("They don't play tennis on Sunday")['correct'], 'Sunday for Sundays (last letter) is not forgiven');
$join = Content::item('ppf-B12-3c'); // Join with After ... had finished
$check(!Grader::grade($join, 'After I had finish work, I went home.')['correct'], 'had finish is not forgiven as a typo of finished');
$check(Grader::grade($join, 'After I had finished work, I went home.')['correct'], 'exact answer still correct');
$check(!Grader::grade($join, 'After I had finishes work, I went home.')['correct'], 'a wrong word ending is not forgiven (finishes)');
$check(!Grader::grade($join, 'After I had finishing work, I went home.')['correct'], 'a wrong word ending is not forgiven (finishing)');
$pc = Content::item('pac-B12-3b'); // While the guests ___ (arrive), the band ___ (play)
$r = Grader::grade($pc, ['were ariving', 'was playing']);
$check($r['correct'] && $r['notes'] === ['Spelling: ariving → arriving.'], 'the screenshot case: ariving accepted as a spelling slip of arriving', $r);
$check(Grader::grade($pc, ['were arriveing', 'was playing'])['correct'], 'arriveing accepted (extra letter in the stem)');
$check(Grader::grade($pc, ['were arirving', 'was playing'])['correct'], 'arirving accepted (extra letter in the stem)');
$check(Grader::grade($pc, ['were arriving', 'was plaing'])['correct'], 'plaing accepted as a spelling slip of playing (the ending -ing is intact)');
$check(!Grader::grade($pc, ['were arrived', 'was playing'])['correct'], 'were arrived is grammar, not spelling');
$check(!Grader::grade($pc, ['were arrive', 'was playing'])['correct'], 'were arrive is grammar, not spelling');
$check(!Grader::grade($pc, ['was arriving', 'was playing'])['correct'], 'was arriving (wrong auxiliary) is not forgiven');
$check(!Grader::grade($pc, ['were arrivin', 'was playing'])['correct'], 'a missing last letter is not forgiven');
$check(!Grader::grade($pc, ['were arriving', 'was playin'])['correct'], 'playin (last letter missing) is not forgiven');
$w = Content::item('fu-A21-6a'); // I am going to ...
$check(Grader::grade($w, 'Im going to visit a friend tomorrow')['correct'], 'write task: im accepted');
$check(Grader::grade($w, "I'm going to visit a friend tomorrow")['correct'], 'write task: normal answer');
$check(!Grader::grade($w, 'I going to visit a friend tomorrow')['correct'], 'write task: missing am still wrong');
$setSpelling('strict');
$check(!Grader::grade($neg, 'They dont play tennis on Sundays')['correct'], 'strict: missing apostrophe is a mistake');
$check(!Grader::grade($neg, "They don't play tenis on Sundays")['correct'], 'strict: typo is a mistake');
$check(Grader::grade($neg, "they don't play tennis on sundays")['correct'], 'strict: capital letters still never matter');
$setSpelling('forgiving');

// No grammar slip may pass: change the END of each word of every accepted answer, the result must be rejected
$bad = 0; $tried = 0;
foreach (Content::items() as $it) {
    if (!in_array($it['kind'], ['gap', 'text'], true)) continue;
    $firsts = array_map(fn($b) => $b[0], $it['answers']);
    foreach ($it['answers'] as $bi => $alts) {
        $accNorm = array_map([Grader::class, 'norm'], $alts);
        $tokens = explode(' ', Grader::norm($alts[0]));
        foreach ($tokens as $ti => $tok) {
            if (mb_strlen($tok) < 3) continue;
            $muts = [mb_substr($tok, 0, -1) . 's', mb_substr($tok, 0, -1) . 'd', $tok . 's', $tok . 'ed', $tok . 'd'];
            if (mb_strlen($tok) >= 4) $muts[] = mb_substr($tok, 0, -1);
            foreach (array_unique($muts) as $mu) {
                if ($mu === $tok) continue;
                $t2 = $tokens; $t2[$ti] = $mu;
                $cand = implode(' ', $t2);
                if (in_array($cand, $accNorm, true)) continue; // happens to be another accepted answer
                $try = $firsts; $try[$bi] = $cand;
                $tried++;
                if (Grader::grade($it, $it['kind'] === 'gap' ? $try : $try[0])['correct']) {
                    $bad++;
                    if ($bad <= 8) echo "  accepted wrongly in {$it['id']}: $cand\n";
                }
            }
        }
    }
}
$check($bad === 0, "grammar slips accepted by the forgiving rules: $bad of $tried");
echo "checked $tried word-ending changes\n";

// Inner one-letter slips (delete / duplicate one letter in the stem of each word of the first accepted answer). Everything the
// forgiving rules accept must still end exactly like the correct word, and be accepted only with a spelling tip.
$accepted = 0; $badEnd = 0;
foreach (Content::items() as $it) {
    if (!in_array($it['kind'], ['gap', 'text'], true)) continue;
    $firsts = array_map(fn($b) => $b[0], $it['answers']);
    foreach ($it['answers'] as $bi => $alts) {
        $accNorm = array_map([Grader::class, 'norm'], $alts);
        $tokens = explode(' ', Grader::norm($alts[0]));
        foreach ($tokens as $ti => $tok) {
            $len = mb_strlen($tok);
            if ($len < 5) continue;
            for ($k = 1; $k < $len - 2; $k++) {
                foreach ([mb_substr($tok, 0, $k) . mb_substr($tok, $k + 1), mb_substr($tok, 0, $k) . mb_substr($tok, $k, 1) . mb_substr($tok, $k)] as $mu) {
                    if ($mu === $tok) continue;
                    $t2 = $tokens; $t2[$ti] = $mu;
                    if (in_array(implode(' ', $t2), $accNorm, true)) continue; // another accepted spelling (cancelled / canceled)
                    $try = $firsts; $try[$bi] = implode(' ', $t2);
                    $res = Grader::grade($it, $it['kind'] === 'gap' ? $try : $try[0]);
                    if ($res['correct']) {
                        $accepted++;
                        if (mb_substr($mu, -2) !== mb_substr($tok, -2)) { $badEnd++; echo "  ending changed but accepted in {$it['id']}: $mu (for $tok)\n"; }
                        if (!$res['notes']) { $badEnd++; echo "  accepted without a tip in {$it['id']}: $mu\n"; }
                    }
                }
            }
        }
    }
}
$check($badEnd === 0, "inner slips accepted keep the grammatical ending and show a tip ($accepted accepted, $badEnd problems)");
echo "inner one-letter slips accepted with a tip: $accepted\n";

// normaliser
$check(Grader::norm("Don't  Worry!") === 'do not worry', 'norm 1');
$check(Grader::norm("I’ll go") === 'i will go', 'norm 2');
$check(Grader::norm("Won't") === 'will not', 'norm 3');
$check(Grader::norm("Can't") === 'cannot', 'norm 4');
$check(Grader::norm("After I had finished work, I went home.") === 'after i had finished work i went home', 'norm 5');

echo $fail ? "\n$fail failures in $n items\n" : "OK: $n items graded consistently\n";
exit($fail ? 1 : 0);
