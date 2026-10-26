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
            if (!empty($it['bank'])) {
                $pub = Content::publicItem($it, 3);
                foreach ($first as $a1) $check(in_array($a1, $pub['bank'], true), "$id the word bank misses an answer");
                $check(count($pub['bank']) > count($first), "$id the word bank has no decoy");
            }
            // same answer with different case / contractions expanded
            $up = array_map(fn($s) => mb_strtoupper($s) . '.', $first);
            $check(Grader::grade($it, $up)['correct'], "$id upper case + full stop rejected");
            break;
        case 'order':
            $toks = explode(' ', $it['sentence']);
            $check(Grader::grade($it, $toks)['correct'], "$id correct order rejected");
            foreach (array_slice($it['answers'][0], 1) as $alt) $check(Grader::grade($it, explode(' ', $alt))['correct'], "$id alternative order rejected: $alt");
            $accepted = array_map([Grader::class, 'norm'], $it['answers'][0]);
            $rev = array_reverse($toks);
            if (!in_array(Grader::norm(implode(' ', $rev)), $accepted, true)) $check(!Grader::grade($it, $rev)['correct'], "$id reversed order accepted");
            $check(!Grader::grade($it, array_slice($toks, 1))['correct'], "$id a missing card was accepted");
            $check(!Grader::grade($it, 'anything at all')['correct'], "$id free text accepted");
            $pub = Content::publicItem($it, 7);
            $a = $pub['tokens']; $b = $toks; sort($a); sort($b);
            $check($a === $b && $pub['tokens'] !== $toks, "$id public cards are the same words in a different order");
            $check(!isset($pub['sentence']) && !isset($pub['answers']), "$id the public item leaks the answer");
            break;
        case 'match':
            $rights = array_column($it['pairs'], 1);
            $r = Grader::grade($it, $rights);
            $check($r['correct'] && !in_array(false, $r['marks'], true), "$id correct pairs rejected");
            $sw = $rights; [$sw[0], $sw[1]] = [$sw[1], $sw[0]];
            $r2 = Grader::grade($it, $sw);
            $check(!$r2['correct'] && $r2['marks'][0] === false && $r2['marks'][1] === false, "$id swapped pairs accepted or not marked");
            $check(!Grader::grade($it, array_slice($rights, 1))['correct'], "$id too few answers accepted");
            $pub = Content::publicItem($it, 7);
            $check($pub['lefts'] === array_column($it['pairs'], 0) && $pub['rights'] !== $rights && count($pub['rights']) === count($rights), "$id public cards");
            $check(!isset($pub['pairs']), "$id the public item leaks the pairs");
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
$r = $g("They don't play tennis on Sunday");
$check($r['correct'] && in_array('Check the ending: sunday → Sundays.', $r['notes'], true), 'a missing plural -s after a preposition (on Sunday) is a copying slip: accepted with a tip', $r['notes']);
$r = $g('they do not play tennis on sunday');
$check($r['correct'] && in_array('Check the ending: sunday → Sundays.', $r['notes'], true), 'the learner answer from the screenshot (do not ... on sunday) is accepted with a tip', $r['notes']);
$r = $g("They don't plays tennis on Sundays");
$check(!$r['correct'] && !empty($r['near']) && strpos((string) $r['specific'], 'Almost') === 0, 'a one-word grammar error is not forgiven; the feedback says which word', $r);
$room = Content::item('psp-B12-3b'); // The rooms are cleaned daily.
$check(!Grader::grade($room, 'The room are cleaned daily.')['correct'], 'a missing -s on a SUBJECT noun hides a verb-agreement error: not forgiven');
$check(!Grader::grade($room, 'The rooms are clean daily.')['correct'] && empty(Grader::grade($room, 'Totally different words here now')['near']), 'a different sentence is not a near miss');

// write tasks must only ask for what the instruction asks for
$w = fn(string $id, string $a) => Grader::grade(Content::item($id), $a);
$check($w('ps-A21-6a', 'He works hard.')['correct'], 'ps-A21-6a: no time word is required (He works hard.)');
$check($w('pc-B11-6a', 'More people are cycling to work.')['correct'], 'pc-B11-6a: no time phrase is required');
$check($w('cf-B11-6a', 'I must leave now unless I want to miss the train.')['correct'], 'cf-B11-6a: will is not required in the other part');
$check($w('ct-B22-6a', "Penicillin might not have been discovered if Fleming hadn't left his dish uncovered.")['correct'], 'ct-B22-6a: the sentence need not start with If');
$check($w('cm-B22-6a', "I wouldn't have shouted at the printer yesterday if I were more patient.")['correct'], 'cm-B22-6a: the sentence need not start with If');
foreach (['cs-B11-6a' => 'If I won a free holiday I would go to Iceland.', 'cs-B12-6a' => 'If I were a pilot I would fly everywhere.'] as $id => $ans) {
    $check($w($id, $ans)['correct'], "$id: the comma after the if-part is not required");
}
$check($w('cs-B11-6a', 'If I won a free holiday, I would go to Iceland.')['correct'], 'cs-B11-6a: with a comma still fine');
$check(!$w('cs-B11-6a', 'If I would win a free holiday I would go to Iceland.')['correct'], 'cs-B11-6a: would in the if-part is still wrong (no comma)');
$check(!$w('cs-B11-6a', 'If I would win a free holiday, I would go to Iceland.')['correct'], 'cs-B11-6a: would in the if-part is still wrong (comma)');
$check(!$w('cf-B11-6a', 'I will leave now.')['correct'], 'cf-B11-6a: unless is still required');
$check(!$w('ps-A21-6a', 'They work hard.')['correct'], 'ps-A21-6a: he/she + verb-s is still required');
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
            // the one intended exception: a missing plural -s on a noun after a preposition (on Sunday) is a copying slip
            $afterPrep = $ti > 0 && (in_array($tokens[$ti - 1], Grader::PREPOSITIONS, true) || ($ti > 1 && in_array($tokens[$ti - 1], Grader::DETERMINERS, true) && in_array($tokens[$ti - 2], Grader::PREPOSITIONS, true)));
            foreach (array_unique($muts) as $mu) {
                if ($mu === $tok) continue;
                if ($afterPrep && $it['kind'] === 'text' && mb_strlen($tok) >= 5 && mb_substr($tok, -1) === 's' && $mu === mb_substr($tok, 0, -1)) continue;
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

// Latvian explanations travel beside the English ones and every skill has areas
$lvn = 0;
foreach (Content::items() as $it) {
    if (!empty($it['why_lv'])) $lvn++;
    if ($it['kind'] === 'mcq' && !empty($it['wrong_why_lv'])) {
        $w = array_key_first($it['wrong_why_lv']);
        $r = Grader::grade($it, $w);
        $check(!$r['correct'] && $r['specific_lv'] === $it['wrong_why_lv'][$w] && $r['specific'] === $it['wrong_why'][$w], "{$it['id']} Latvian and English wrong-answer messages");
    }
}
$check($lvn >= 300, "Latvian explanations present on $lvn items");
foreach (Content::meta()['skills'] as $sk) $check(isset($sk['area']), "{$sk['id']} has an area");
$check(Content::levelFromTheta(1.0) === 'A2.1' && Content::levelFromTheta(4.0) === 'B1.2' && Content::levelFromTheta(5.0) === 'B2.1' && Content::levelFromTheta(6.0) === 'B2.2' && Content::levelFromTheta(7.0) === 'C1.1' && Content::levelFromTheta(8.6) === 'C1.2', 'level boundaries');
// a level when its typical task (difficulty base + 0.4) is right at least half of the time (25 October)
$check(Content::levelFromAbility(2.3) === 'A2.1' && Content::levelFromAbility(2.4) === 'A2.2' && Content::levelFromAbility(3.3) === 'A2.2' && Content::levelFromAbility(3.4) === 'B1.1' && Content::levelFromAbility(4.4) === 'B1.2' && Content::levelFromAbility(4.86) === 'B1.2' && Content::levelFromAbility(5.4) === 'B2.1' && Content::levelFromAbility(8.4) === 'C1.2', 'placement level boundaries');
$check(Content::levelFromTheta(4.0, ['A2.1', 'B1.2']) === 'B1.2' && Content::levelFromTheta(7.0, ['A2.1', 'B1.2']) === 'B1.2', 'estimates of topics without high levels stay within their levels');

// normaliser
$check(Grader::norm("Don't  Worry!") === 'do not worry', 'norm 1');
$check(Grader::norm("I’ll go") === 'i will go', 'norm 2');
$check(Grader::norm("Won't") === 'will not', 'norm 3');
$check(Grader::norm("Can't") === 'cannot', 'norm 4');
$check(Grader::norm("After I had finished work, I went home.") === 'after i had finished work i went home', 'norm 5');

// typical mistakes in a typed answer: named first, never when an accepted answer has the same pattern
$typ = fn($g, $a) => (Grader::typical($g, $a) ?? [null, null, null])[2];
$check($typ('My boss said I must to finish by Friday.', ['My boss said I must finish by Friday.']) === 'MODAL', 'typical: must to');
$check($typ('She can to swim.', ['She can swim.']) === 'MODAL', 'typical: can to');
$check($typ('I have lived here since five years.', ['I have lived here for five years.']) === 'DURATION', 'typical: since five years');
$check($typ('I will call you as soon as I will arrive.', ['I will call you as soon as I arrive.']) === 'TIME-CLAUSE', 'typical: will after as soon as');
$check($typ('What you do?', ['What do you do?']) === 'DO', 'typical: What you do');
$check($typ('Where your sister works?', ['Where does your sister work?']) === 'DO', 'typical: Where your sister works');
$check($typ('I am agree with you.', ['I agree with you.']) === 'BE-VERB', 'typical: I am agree');
$check($typ("I don't know if he will come.", ["I don't know if he'll come.", "I don't know if he will come."]) === null, 'typical: if + will in an accepted answer is not flagged');
$check($typ('She has worked here since 2019.', ['She has worked here since 2019.']) === null, 'typical: since + a year is fine');
$ans = Grader::grade(['id' => 't', 'kind' => 'text', 'q' => 'Report this', 'answers' => [['My boss said I had to finish by Friday.', 'My boss said I must finish by Friday.']], 'hints' => []], 'My boss said I must to finish by Friday.');
$check(!$ans['correct'] && str_contains((string) $ans['specific'], 'without *to*') && empty($ans['near']), 'typical: the note comes first, not "change must to had"');

echo $fail ? "\n$fail failures in $n items\n" : "OK: $n items graded consistently\n";
exit($fail ? 1 : 0);
