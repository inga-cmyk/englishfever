<?php
// php app/tests/error_model_test.php
// Error types in the background (docs/ERROR-TYPES.md): support levels, the state of each kind of mistake, and the rules that keep
// a learner from getting stuck. In-memory database only.
putenv('EF_DEV=1');
require __DIR__ . '/../src/Auth.php';
require __DIR__ . '/../src/Content.php';
require __DIR__ . '/../src/Grader.php';
require __DIR__ . '/../src/Db.php';
require __DIR__ . '/../src/Stats.php';
require __DIR__ . '/../src/Engine.php';
require __DIR__ . '/../src/Reports.php';
require __DIR__ . '/../src/Mistakes.php';
require __DIR__ . '/../src/ErrorModel.php';
Config::load();
Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']);
Db::migrate();

$n = 0; $bad = 0;
function check(bool $ok, string $why): void { global $n, $bad; $n++; if (!$ok) { $bad++; echo "FAIL $why\n"; } }

// 1. support levels (Content::scaffold) and error types (Content::errors)
$it = fn($id) => Content::item($id);
check(Content::scaffold($it('ps-A21-1a')) === 0, 'a choice task has support 0');
check(Content::scaffold($it('var-ps-a21-bank-01')) === 0, 'a word-bank gap has support 0');
check(Content::scaffold($it('pa-A21-3a')) === 1, 'a gap with the verb in brackets has support 1');
check(Content::scaffold($it('ip-B11-3a')) === 2, 'a typed gap without a clue has support 2');
check(Content::scaffold($it('ps-A21-6a-r3')) === 3, 'open writing has support 3');
check(Content::errors($it('ps-A21-1a')) === ['3S', 'DO', 'BASE'], 'a task without its own codes takes the codes of its topic');
check(!array_key_exists('err', Content::publicItem($it('ps-A21-1a'))), 'learners never receive the error types');
$meta = Content::meta();
foreach ($meta['skill_err'] as $skill => $codes) foreach ($codes as $c) check(isset($meta['errors'][$c]), "topic $skill names an unknown error type $c");

// 2. the state of a kind of mistake, from the answers
$uid = (int) Db::insert('users', ['provider' => 'guest', 'nickname' => 'Error Model', 'nickname_key' => 'error-model', 'created_at' => time()]);
$day = 86400; $t0 = time() - 20 * $day;
$add = function (string $item, bool $ok, int $t, ?string $err = '3S') use ($uid) {
    $i = Content::item($item);
    Db::insert('attempts', ['user_id' => $uid, 'psession_id' => 0, 'item_id' => $item, 'skill' => $i['skill'], 'level' => $i['level'], 'bloom' => $i['bloom'],
        'correct' => $ok ? 1 : 0, 'answer' => '', 'time_ms' => 1000, 'xp' => 0, 'created_at' => $t, 'err' => $err]);
};
$add('ps-A21-1a', false, $t0);
$s = ErrorModel::scan($uid, $t0 + 60);
check($s['3S']['state'] === 'learn', 'a wrong answer: learn');
check($s['3S']['due'] === $t0 + $day, 'a mistake is due again the next day');
$add('var-ps-a21-bank-01', true, $t0 + 120);
$s = ErrorModel::scan($uid, $t0 + 180);
check($s['3S']['state'] === 'practise', 'right again: practise');
$add('ps-A21-4a', true, $t0 + 240);
$add('pa-A21-3a', true, $t0 + 300, '3S');
$s = ErrorModel::scan($uid, $t0 + 400);
check($s['3S']['state'] === 'practise', '3 right on one day, all with support: not mastered yet');
$add('ip-B11-3a', true, $t0 + $day + 60, '3S');   // a typed task without a clue, on another day
$s = ErrorModel::scan($uid, $t0 + $day + 100);
check($s['3S']['state'] === 'mastered', '3 different tasks, 2 days, one without a clue: mastered');
check($s['3S']['due'] === $t0 + $day + 60 + 14 * $day, 'mastered: checked again after 14 days');
$add('ps-A22-1a', true, $t0 + 16 * $day, '3S');
$s = ErrorModel::scan($uid, $t0 + 16 * $day + 10);
check($s['3S']['state'] === 'kept', 'right at the check 14 days later: kept');
$add('ps-A22-4a', false, $t0 + 17 * $day, '3S');
$s = ErrorModel::scan($uid, $t0 + 17 * $day + 10);
check($s['3S']['state'] === 'practise', 'a mistake after that moves one step back, not to the start');
check(in_array('3S', ErrorModel::due($uid, $t0 + 19 * $day), true), 'it is due for review again');

// 3. the loop in a practice session: an easier task straight away, never stuck on one mistake
$uid2 = (int) Db::insert('users', ['provider' => 'guest', 'nickname' => 'Loop', 'nickname_key' => 'loop', 'created_at' => time()]);
$wrong = function (array $item) {
    switch ($item['kind']) {
        case 'mcq': return $item['wrong'][0];
        case 'gap': return array_fill(0, count($item['answers']), 'zzz');
        case 'order': return array_reverse(explode(' ', $item['sentence']));
        case 'match': return array_reverse(array_column($item['pairs'], 1));
        default: return 'zzz qqq';
    }
};
$easierNext = 0; $missesWithRoom = 0;
for ($round = 0; $round < 6; $round++) {
    $r = Engine::start($uid2, 'practice', ['present_simple', 'past_simple'], 'A2.2', 15);
    $sid = (int) $r['session']['id']; $cur = $r['item']; $served = [];
    while ($cur) {
        $item = Content::item($cur['id']);
        $served[] = $item;
        $res = Engine::answer($uid2, $sid, $item['id'], $wrong($item), 1000);   // a learner who gets everything wrong
        if ($res['done']) break;
        $next = Content::item($res['next']['id']);
        if (Content::scaffold($item) > 0) { $missesWithRoom++; if (Content::scaffold($next) < Content::scaffold($item)) $easierNext++; }
        $cur = $res['next'];
    }
    $st = json_decode(Db::val('SELECT state FROM psessions WHERE id = ?', [$sid]), true);
    $perCode = [];
    foreach ($st['probes'] ?? [] as $p) if (isset($p['code'])) $perCode[$p['code']] = ($perCode[$p['code']] ?? 0) + 1;
    check(!$perCode || max($perCode) <= 2, 'never more than 2 extra tasks for one kind of mistake in a session: ' . json_encode($perCode));
    check(count($st['probes'] ?? []) <= intdiv(15, 3), 'extra tasks take at most a third of the session');
    check(count(array_unique(array_column($served, 'id'))) === count($served), 'no task twice in a session');
}
check($missesWithRoom > 0 && $easierNext / $missesWithRoom >= 0.5, "after a miss the next task is usually easier (more support): $easierNext of $missesWithRoom");

// 4. a mistake is fixed by a different sentence; the same sentence right again counts only on a later day (memory is not the rule)
$uid3 = (int) Db::insert('users', ['provider' => 'guest', 'nickname' => 'Same Day', 'nickname_key' => 'same-day', 'created_at' => time()]);
$at = function (string $item, bool $ok, int $t) use ($uid3) {
    $i = Content::item($item);
    Db::insert('attempts', ['user_id' => $uid3, 'psession_id' => 0, 'item_id' => $item, 'skill' => $i['skill'], 'level' => $i['level'], 'bloom' => $i['bloom'],
        'correct' => $ok ? 1 : 0, 'answer' => '', 'time_ms' => 1000, 'xp' => 0, 'created_at' => $t]);
};
$d0 = strtotime('today 10:00') - 3 * 86400;
$at('ps-A21-1a', false, $d0);
$at('ps-A21-1a', true, $d0 + 60);
$m = Mistakes::scan($uid3);
check(isset($m['open']['ps-A21-1a']) && $m['fixed'] === 0, 'the same sentence right a minute later: still open');
$at('ps-A21-1a', true, $d0 + 86400);
$m = Mistakes::scan($uid3);
check(!isset($m['open']['ps-A21-1a']) && $m['fixed'] === 1, 'the same sentence right on a later day: fixed');

// 5. the check after a mistake is not harder: same level or lower whenever the topic has such a task
$lv = array_flip(array_keys(Content::BASE)); $higher = 0; $tried = 0;
foreach (array_slice(array_values(array_filter(Content::items(), fn($i) => $i['kind'] !== 'write')), 0, 400, true) as $k => $i) {
    if ($k % 8) continue;
    $t = Mistakes::twin($uid3, $i['id'], []);
    if (!$t) continue;
    $tried++; if ($lv[$t['level']] > $lv[$i['level']]) $higher++;
}
check($tried > 20 && $higher / $tried <= 0.1, "the similar task after a mistake is rarely at a higher level: $higher of $tried");

echo $bad ? "SOME FAILED ($bad of $n)\n" : "OK: $n error-type checks\n";
exit($bad ? 1 : 0);
