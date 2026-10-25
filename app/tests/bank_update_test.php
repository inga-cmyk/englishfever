<?php
// php app/tests/bank_update_test.php
// Uses an in-memory database only. Never connects to the configured student DB.
putenv('EF_DEV=1');
require __DIR__ . '/../src/Auth.php';
require __DIR__ . '/../src/Content.php';
require __DIR__ . '/../src/Grader.php';
require __DIR__ . '/../src/Db.php';
require __DIR__ . '/../src/Stats.php';
require __DIR__ . '/../src/Engine.php';
require __DIR__ . '/../src/Reports.php';
require __DIR__ . '/../src/Mistakes.php';
Config::load();

$n = 0;
function check(bool $ok, string $why): void {
    global $n;
    $n++;
    if (!$ok) throw new RuntimeException($why);
}
$active = array_column(Content::items(), null, 'id');
$published = json_decode(file_get_contents(__DIR__ . '/../authoring/history/published_items.json'), true);
foreach ($published as $original) {
    $found = Content::item($original['id']);
    check($found !== null, 'Published question disappeared: ' . $original['id']);
    unset($found['d'], $found['scaffold'], $found['err']);   // worked out when the bank loads, not stored
    check($found === $original, 'Published question was rewritten: ' . $original['id']);
}
$retired = require __DIR__ . '/../content/retired.php';
foreach ($retired as $old) {
    check(!isset($active[$old['id']]), 'Retired question entered the active pool');
    $stem = preg_replace('/-r\d+$/', '', $old['id']); $rev = preg_match('/-r(\d+)$/', $old['id'], $m) ? (int) $m[1] : 1;
    $replacement = null;   // the active version of the same question with a higher revision number (numbers can skip when intermediate versions were recorded)
    foreach ($active as $aid => $a) if (preg_match('/^' . preg_quote($stem, '/') . '-r(\d+)$/', $aid, $mm) && (int) $mm[1] > $rev) $replacement = $a;
    check($replacement !== null, 'Missing corrected replacement');
    foreach (['skill', 'level', 'bloom', 'kind'] as $key) {
        check($old[$key] === $replacement[$key], "Correction changed $key");
    }
}
check(count($active) === 490, 'Unexpected active question count');
check(count($retired) === 137, 'Unexpected correction count');
check(Content::item('unknown-id') === null, 'Unknown ID should return null');

$grade = fn(string $id, $answer) => Grader::grade(Content::item($id), $answer);
check($grade('cf-B11-3b-r2', ['arrive'])['correct'], 'arrive must fit');
check(!$grade('cf-B11-3b-r2', ['get'])['correct'], 'get at must not pass');
check($grade('ca-C11-4a-r3', 'Unless you hurry, we will miss the flight.')['correct'], 'the same-meaning option is the key');
check(!$grade('ca-C11-4a-r3', 'If you hurry, we will miss the flight.')['correct'], 'the reversed option is wrong');
check($grade('ct-B21-3a-r2', "If I'd seen the sign, I wouldn't have parked there.")['correct'], "I'd seen = I had seen");
check($grade('ct-B21-3a-r2', "I'd not have parked there if I had seen the sign.")['correct'], "I'd not have = I would not have");
check(!$grade('ct-B21-3a-r2', "If I'd seen the sign, I'd have parked there.")['correct'], "a different meaning is still wrong");
check($grade('psp-B12-3b-r2', 'Every day the rooms are cleaned.')['correct'], 'time phrase first');
check($grade('ip-B12-3a-r2', 'Could you please tell me what time the museum closes?')['correct'], 'please is fine');
check($grade('rs-B12-3a-r2', 'Kate said she was leaving now.')['correct'], 'the time word may stay');
check($grade('rv-C12-3a-r2', 'my sister suggested seeing a doctor about that cough.')['correct'], 'suggested seeing is a correct report (learner report)');
check($grade('rv-C12-3a-r2', 'My sister said I should see a doctor about that cough.')['correct'], 'said I should see is a correct report');
check(!$grade('rv-C12-3a-r2', 'My sister suggested to see a doctor about that cough.')['correct'], 'suggested to see is not');
check(Content::item('var-ca-c11-order-01-r2')['sentence'] === 'had I known about the delay I would have called you', 'the inverted conditional has its object');
check(!in_array('Both are about the past.', Content::item('ct-B22-2a-r2')['wrong'], true), 'the illogical option is gone');
check(Content::item('pasp-B11-3a-r2')['q'] === 'Where ___ this photo ___? (take)', 'the film sentence is replaced');
check($grade('ct-B22-3a-r2', ["hadn't been driving", "wouldn't have lost"])['correct'], 'hadn\'t been driving is also correct');
check($grade('ct-B22-3a-r2', ["hadn't driven", "wouldn't have lost"])['correct'], 'hadn\'t driven stays correct');
check(!$grade('cf-B11-3b-r2', ['reach'])['correct'], 'reach at must not pass');
check($grade('pp-B12-3a', ['have', 'been studying'])['correct'], 'Per-blank alternatives regressed');
check($grade('ps-A21-6a-r2', 'She has breakfast every day.')['correct'], 'has rejected');
check($grade('ps-A21-6a-r2', 'He usually goes to work at eight.')['correct'], 'adverb rejected');
check(!$grade('ps-A21-6a-r2', 'She work every day.')['correct'], 'missing third-person ending accepted');
check($grade('ps-B11-6a-r2', 'My class starts at noon. It finishes at two.')['correct'], 'Written time rejected');
check($grade('ppp-B11-6a-r2', "The room's been cleaned this week.")['correct'], 'contracted has been rejected');
check($grade('fup-B11-6a-r2', "The library'll be opened next year.")['correct'], 'contracted will rejected');

$new = array_filter($active, fn($i) => strpos($i['id'], 'var-') === 0);
check(count($new) === 48, 'Expected 48 new variety tasks');
foreach ($new as $it) {
    check(in_array($it['kind'], ['order', 'match', 'gap'], true), 'Variety task is not drag and drop');
    if ($it['kind'] === 'gap') {
        check(!empty($it['bank']), 'Gap task missing its word bank');
        $answers = array_column($it['answers'], 0);
        foreach (array_diff($it['bank'], $answers) as $decoy) {
            foreach ($answers as $index => $answer) {
                $wrong = $answers;
                $wrong[$index] = $decoy;
                check(!Grader::grade($it, $wrong)['correct'], 'Bank distractor accepted');
            }
        }
    }
    if ($it['kind'] === 'order') {
        $result = Grader::grade($it, explode(' ', $it['sentence']));
        check($result['show'] === $it['display_answer'], 'Punctuated model lost');
        check((bool) preg_match('/[.!?]$/', $result['show']), 'Model lacks end punctuation');
    }
}
check($grade('var-cf-a22-order-01', explode(' ', 'if it rains we will stay indoors'))['show'] === 'If it rains, we will stay indoors.', 'Conditional comma missing');

// Existing attempts, XP, level estimates and activity must stay byte-for-byte
// unchanged when the new bank is loaded, a session resumes, or new items are picked.
Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']);
Db::migrate();
$now = time();
foreach ([1, 2] as $id) Db::insert('users', ['id' => $id, 'provider' => 'guest', 'nickname' => "Test $id", 'nickname_key' => "test-$id", 'created_at' => $now]);
$state = ['current' => 'ps-B11-4a', 'seed' => 1, 'served' => ['ps-B11-4a'], 'theta' => [], 'g' => 2.0, 'last' => []];
$sid = Db::insert('psessions', ['user_id' => 1, 'mode' => 'practice', 'skills' => '["present_simple"]', 'level' => 'B1.1', 'target_len' => 10,
    'state' => json_encode($state), 'n' => 1, 'n_correct' => 1, 'xp' => 16, 'started_at' => $now]);
Db::insert('attempts', ['user_id' => 1, 'psession_id' => $sid, 'item_id' => 'cf-B12-4a', 'skill' => 'cond_first', 'level' => 'B1.2',
    'bloom' => 4, 'correct' => 1, 'answer' => "Unless you don't hurry, you will be late.", 'xp' => 16, 'created_at' => $now]);
Db::insert('skill_state', ['user_id' => 1, 'skill' => 'cond_first', 'theta' => 4.1, 'n' => 8, 'n_correct' => 6, 'updated_at' => $now]);
Db::insert('activity', ['user_id' => 1, 'day' => Stats::today(), 'seconds' => 180, 'answers' => 8, 'xp' => 112]);
$snapshot = fn() => array_map(fn($table) => Db::all("SELECT * FROM $table WHERE user_id = 1 ORDER BY 1"), ['attempts', 'skill_state', 'activity', 'psessions']);
$before = $snapshot();
$dashboard = Stats::dashboard(1);
$resume = Engine::current(1, $sid);
check(in_array('I am liking this song.', $resume['item']['options'], true), 'Pending session silently switched question version');
check(Content::item('cf-B12-4a')['q'] === 'Which sentence is NOT correct?', 'Old answer history now shows a rewritten prompt');
check(Content::item('cf-B12-4a-r2')['q'] !== Content::item('cf-B12-4a')['q'], 'Correction was not applied to new version');
foreach (Content::liveMeta()["skills"] as $skill) {
    $session = Engine::start(2, 'practice', [$skill['id']], $skill['levels'][0], 5);
    check(isset($active[$session['item']['id']]), 'New session selected a retired question');
}
check($before === $snapshot(), 'Historical results or pending session changed');
check($dashboard === Stats::dashboard(1), 'Existing dashboard totals changed');
echo "OK: $n history, correction, drag-and-drop and in-memory integration checks\n";
