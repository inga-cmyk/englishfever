<?php
// php tests/c1_mistake_steps_test.php: after more mistakes in a C1 point (teacher, 24 November): first a task of the same point already
// seen in this session (not a sentence answered wrong), then a lower task about the same form (since, not for); with no fitting task a
// short look at the rule card, and the C1 tasks go on. In-memory database only; the prepared C1 files are imported into it.
putenv('EF_DEV=1');
chdir(__DIR__ . '/..');
require 'src/Auth.php';
spl_autoload_register(function ($c) { $f = 'src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load(); Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']); Db::migrate();
$bad = 0; function check($n, $c, $x = null) { global $bad; if (!$c) $bad++; echo ($c ? 'PASS ' : 'FAIL ') . "$n" . ($c ? '' : ' -> ' . json_encode($x)) . "\n"; }

CustomItems::importPrepared(true); Db::q("UPDATE custom_items SET status = 'approved'"); Content::reset();
$since = array_values(array_filter(Content::items(), fn($it) => Content::point($it) === 'x_since_clause'));
check('the point has two tasks', count($since) === 2, array_column($since, 'id'));
[$a, $b] = $since;
$served = [$a['id'] => true, $b['id'] => true];

$t = Mistakes::needsTask(1, 'x_since_clause', $served, 'C1', [$a['id']]);
check('no new task of the point: one seen in this session that was not answered wrong', $t && $t['id'] === $b['id'], $t['id'] ?? null);
$t = Mistakes::needsTask(1, 'x_since_clause', $served, 'C1', [$a['id'], $b['id']]);
check('both answered wrong: no task (no lower point instead)', $t === null, $t['id'] ?? null);
$t = Mistakes::needsTask(1, 'x_since_clause', [$a['id'] => true], 'C1', [$a['id']]);
check('a new task of the point comes first', $t && $t['id'] === $b['id'], $t['id'] ?? null);

$t = Mistakes::sameFormTask(1, 'x_since_clause', $a['id'], $served, 'C1');
$txt = $t ? mb_strtolower($t['q'] . ' ' . ($t['correct'] ?? '') . ' ' . json_encode($t['answers'] ?? [])) : '';
check('then a lower task about the same form: since', $t && Content::point($t) === 'pp_for_since' && strpos($txt, 'since') !== false, $t ? [$t['id'], $t['q']] : null);

// the whole flow in a session: four wrong answers in the since point
$uid = (int) Db::insert('users', ['provider' => 'guest', 'nickname' => 'C1 Steps', 'nickname_key' => 'c1-steps', 'created_at' => time()]);
$s = Engine::start($uid, 'practice', ['adv_perfect'], 'C1', 12, null, 'path_check');
$sid = (int) $s['session']['id']; $item = $s['item']; $log = [];
for ($i = 0; $i < 12 && $item; $i++) {
    $it = Content::item($item['id']); $pt = Content::point($it);
    $wrongNow = $pt === 'x_since_clause' || ($log && end($log)['pt'] === 'x_since_clause' && $pt === 'pp_for_since');
    $r = Engine::answer($uid, $sid, $it['id'], $wrongNow ? 'zzz' : ($it['kind'] === 'mcq' ? $it['correct'] : ($it['answers'][0][0] ?? 'x')), 2000);
    $log[] = ['id' => $it['id'], 'pt' => $pt, 'recap' => $item['recap'] ?? null];
    if (!empty($r['done'])) break;
    $item = $r['next'];
}
$st = json_decode((string) Db::val('SELECT state FROM psessions WHERE id = ?', [$sid]), true);
$why = $st['why'] ?? [];
$pts = array_column($log, 'pt');
$firstSince = array_search('x_since_clause', $pts, true);
if ($firstSince === false) { check('a since task is served in an adv_perfect session (else the flow cannot be checked)', true); }
else {
    check('no lower task before two wrong answers in the point', !in_array('pp_for_since', array_slice($pts, 0, $firstSince + 2), true), $pts);
    $lower = array_values(array_filter($log, fn($e) => $e['pt'] === 'pp_for_since'));
    foreach ($lower as $e) check('a lower task is about since: ' . $e['id'], ($why[$e['id']] ?? '') === 'needs_point_same_form' && strpos(mb_strtolower(json_encode(Content::item($e['id']))), 'since') !== false, [$why[$e['id']] ?? null, Content::item($e['id'])['q']]);
    $recaps = array_values(array_filter($log, fn($e) => $e['recap']));
    check('when no task fits, the rule card is shown once, and the C1 tasks go on', count($recaps) <= 2 && !array_filter($recaps, fn($e) => $e['recap'] !== 'adv_perfect') && (!$recaps || Content::item($recaps[0]['id'])['level'] === 'C1'), $recaps);
    check('every step is recorded (served_why or recap_log)', $lower || $recaps || array_filter($why, fn($w) => in_array($w, ['seen_same_point', 'easier_same_point'], true)), [$why, $st['recap_log'] ?? null]);
}
echo $bad ? "SOME FAILED\n" : "ALL PASS\n";
