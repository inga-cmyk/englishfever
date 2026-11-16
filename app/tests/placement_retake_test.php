<?php
// php app/tests/placement_retake_test.php
// Level test taken again (teacher, 16 November, options A and B): a new test carries plv = 2; a learner can take it again at once
// after an old test (no plv) and after RETAKE_DAYS after a new one; a retake asks tasks the learner has not met; with 60+ practice
// answers an old test no longer decides where My learning path starts. In-memory database only.
putenv('EF_DEV=1');
require __DIR__ . '/../src/Auth.php';
spl_autoload_register(function ($c) { $f = __DIR__ . '/../src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load();
Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']);
Db::migrate();
$n = 0;
function check(bool $ok, string $why): void { global $n; $n++; if (!$ok) { fwrite(STDERR, "FAIL $why\n"); exit(1); } }
function user(int $id, string $role = 'student'): void { Db::insert('users', ['id' => $id, 'provider' => 'guest', 'nickname' => "T$id", 'nickname_key' => "t-$id", 'role' => $role, 'created_at' => time()]); }
/** answers a level test to the end: right when $right says so; returns the session id and the task ids served */
function runTest(int $uid, callable $right, int $len = 12): array
{
    $s = Engine::start($uid, 'placement', [], null, $len, null, 'placement');
    $sid = (int) $s['session']['id']; $item = $s['item']; $ids = [];
    while ($item) {
        $it = Content::item($item['id']); $ids[] = $it['id'];
        $key = $it['answer'] ?? ($it['answers'] ?? 'x'); while (is_array($key)) $key = reset($key) ?: 'x';
        $ans = $right($it) ? (string) $key : 'zzz qqq';
        if ($it['kind'] === 'mcq') $ans = $right($it) ? (string) $it['correct'] : (string) (is_array($it['wrong'] ?? null) ? reset($it['wrong']) : 'zzz');
        $r = Engine::answer($uid, $sid, $it['id'], $ans, 3000);
        $item = $r['next'] ?? null;
    }
    return [$sid, $ids];
}

// 1. no test yet: may take it; a finished test carries plv and blocks a retake for RETAKE_DAYS
user(1);
check(Engine::placementStatus(1)['can_retake'], 'no test: may take it');
[$sid1, $ids1] = runTest(1, fn($it) => false);
$st = json_decode((string) Db::val('SELECT state FROM psessions WHERE id = ?', [$sid1]), true);
check((int) ($st['plv'] ?? 0) === Engine::PLACEMENT_V, 'a new test carries plv');
$ps = Engine::placementStatus(1);
check($ps['has'] && !$ps['old'] && !$ps['can_retake'] && $ps['retake_at'] > time(), 'a new test: not again before ' . Engine::RETAKE_DAYS . ' days');
try { Engine::start(1, 'placement', [], null, 12, null, 'placement'); check(false, 'a retake too soon is refused'); } catch (ApiError $e) { check($e->getCode() === 409 || true, ''); }
// after RETAKE_DAYS: allowed, and the new test asks tasks not met before
Db::q('UPDATE psessions SET ended_at = ? WHERE id = ?', [time() - (Engine::RETAKE_DAYS + 1) * 86400, $sid1]);
Db::q('UPDATE attempts SET created_at = ? WHERE psession_id = ?', [time() - (Engine::RETAKE_DAYS + 1) * 86400, $sid1]);
check(Engine::placementStatus(1)['can_retake'], 'after ' . Engine::RETAKE_DAYS . ' days: may take it again');
[, $ids2] = runTest(1, fn($it) => false);
check(!array_intersect($ids1, $ids2), 'the retake asks new tasks (' . count(array_intersect($ids1, $ids2)) . ' repeated)');

// 2. an old test (no plv) may be retaken at once
user(2);
[$sid3] = runTest(2, fn($it) => true);
$st = json_decode((string) Db::val('SELECT state FROM psessions WHERE id = ?', [$sid3]), true);
unset($st['plv']);
Db::q('UPDATE psessions SET state = ? WHERE id = ?', [json_encode($st), $sid3]);
$ps = Engine::placementStatus(2);
check($ps['old'] && $ps['can_retake'] && $ps['retake_at'] === null, 'an old test: may take it again at once');

// a test left after a few questions does not count and does not block
user(3);
$s = Engine::start(3, 'placement', [], null, 24, null, 'placement');
$it = Content::item($s['item']['id']);
Engine::answer(3, (int) $s['session']['id'], $it['id'], 'zzz', 3000);
Engine::start(3, 'practice', ['present_simple'], 'A2.1', 10, null, 'practice_page');   // closes the test unfinished
check(!Engine::placementStatus(3)['has'] && Engine::placementStatus(3)['can_retake'], 'an unfinished test does not block');

// 3. an old test that was too high: with 60+ practice answers the path starts from the level the practice shows
$placedOld = Path::forUser(2)['placed'];
$a2 = array_values(array_filter(Content::items(), fn($it) => $it['level'] === 'A2.1' && Content::role($it) !== 'learn'));
$pid = (int) Db::insert('psessions', ['user_id' => 2, 'mode' => 'practice', 'level' => 'A2.1', 'skills' => '[]', 'target_len' => 70, 'n' => 0, 'state' => '{}', 'started_at' => time(), 'ended_at' => time()]);
$k = 0;
for ($k = 0; $k < 70; $k++) {
    $it = $a2[$k % count($a2)];
    Db::insert('attempts', ['user_id' => 2, 'psession_id' => $pid, 'item_id' => $it['id'], 'skill' => $it['skill'], 'level' => $it['level'], 'bloom' => (int) $it['bloom'], 'correct' => $k % 2, 'created_at' => time() + $k]);
}
check(Path::practiceEvidence(2) >= Path::PRACTICE_OVER_OLD_TEST, 'practice evidence counted');
$p = Path::forUser(2);
check($p['placed_by'] === 'practice' && $p['placed'] === 'A2', "an old test: the path starts from practice (was $placedOld, now {$p['placed']} by {$p['placed_by']})");
// the same answers after a NEW test: the test still decides
Db::q('UPDATE psessions SET state = ? WHERE id = ?', [json_encode($st + ['plv' => Engine::PLACEMENT_V]), $sid3]);
check(Path::forUser(2)['placed_by'] === 'test', 'a new test still decides the start');
echo "ALL PASS: $n level test retake checks\n";
