<?php
// php app/tests/map_followup_test.php
// The grammar map in practice (14 November, C2): after a wrong answer the next task comes from the same grammar point (another
// sentence); after a second wrong answer in that point, one task from a point in its "needs" at the learner's level or below.
// The engine draws with random_int (not seedable), so every check is repeated over 40 sessions with different draws.
// In-memory database only.
putenv('EF_DEV=1');
require __DIR__ . '/../src/Auth.php';
spl_autoload_register(function ($c) { $f = __DIR__ . '/../src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load();
Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']);
Db::migrate();
$n = 0;
function check(bool $ok, string $why): void { global $n; $n++; if (!$ok) { fwrite(STDERR, "FAIL $why\n"); exit(1); } }

// the prepared tasks as on the server after Add all → Approve all (they live in the database there)
foreach (CustomItems::preparedFiles() as $name => $path) CustomItems::import((string) file_get_contents($path), true);
Db::q("UPDATE custom_items SET status = 'approved'");
Content::reset();

// every task of the bank has a point (C1), and the points it names exist
foreach (Content::items() as $it) {
    $p = Content::point($it);
    check($p !== null && Content::mapPoint($p) !== null, 'task without a known grammar point: ' . $it['id']);
}

$plans = [['present_perfect', 'B1.1'], ['past_simple', 'A2.2'], ['present_simple', 'A2.1'], ['cond_first', 'B1.1'], ['rep_questions', 'B1.2'],
          ['past_continuous', 'A2.2'], ['modal_verbs', 'A2.2'], ['present_perfect_continuous', 'B1.2']];
$runs = 0; $same = 0; $needs = 0; $samePossible = 0; $needsPossible = 0;
for ($u = 1; $u <= 40; $u++) {
    [$skill, $level] = $plans[$u % count($plans)];
    Db::insert('users', ['id' => $u, 'provider' => 'guest', 'nickname' => "T$u", 'nickname_key' => "t-$u", 'created_at' => time()]);
    $s = Engine::start($u, 'practice', [$skill], $level, 10);
    $sid = (int) $s['session']['id'];
    $first = Content::item($s['item']['id']);
    $point = Content::point($first);
    // 1. wrong: the next task should be of the same point
    $r = Engine::answer($u, $sid, $first['id'], 'zzz qqq', 2000);
    $second = $r['next'] ? Content::item($r['next']['id']) : null;
    check($second !== null && $second['id'] !== $first['id'], 'a next task that is not the missed one');
    $others = array_filter(Content::items(), fn($it) => $it['id'] !== $first['id'] && Content::point($it) === $point && Content::role($it) !== 'learn'
        && $it['skill'] === $first['skill'] && $it['kind'] !== 'write' && abs(array_search($it['level'], Engine::levels()) - array_search($first['level'], Engine::levels())) <= 1 && abs($it['bloom'] - $first['bloom']) <= 1);
    if ($others) { $samePossible++; check(Content::point($second) === $point, "after a miss in $point the next task is from $point, not " . Content::point($second)); $same++; }
    // 2. wrong again: one task from a point the missed point needs
    $r = Engine::answer($u, $sid, $second['id'], 'zzz qqq', 2000);
    $third = $r['next'] ? Content::item($r['next']['id']) : null;
    $mp = Content::mapPoint($point);
    if ($others && $mp['needs'] && $third && Content::point($second) === $point) {
        $cands = array_filter(Content::items(), fn($it) => in_array(Content::point($it), $mp['needs'], true) && Content::role($it) !== 'learn' && $it['kind'] !== 'write'
            && empty($it['practice_only']) && array_search($it['level'], Engine::levels()) <= array_search($level, Engine::levels()));
        if ($cands) {
            $needsPossible++;
            check(in_array(Content::point($third), $mp['needs'], true), "after a second miss in $point the next task is from its needs (" . implode(', ', $mp['needs']) . '), not ' . Content::point($third));
            check(array_search($third['level'], Engine::levels()) <= array_search($level, Engine::levels()), 'the prerequisite task is at the learner\'s level or below');
            $needs++;
            $why = Db::val('SELECT served_why FROM attempts WHERE user_id = ? AND item_id = ?', [$u, $second['id']]);
            check($why === 'same_point', 'served_why of the same-point task is same_point, not ' . var_export($why, true));
            Engine::answer($u, $sid, $third['id'], 'zzz qqq', 2000);
            $why = Db::val('SELECT served_why FROM attempts WHERE user_id = ? AND item_id = ?', [$u, $third['id']]);
            check($why === 'needs_point', 'served_why of the prerequisite task is needs_point, not ' . var_export($why, true));
        }
    }
    $runs++;
}
check($samePossible >= 20, "the same-point rule was tried in enough sessions ($samePossible)");
check($needsPossible >= 10, "the needs rule was tried in enough sessions ($needsPossible)");
echo "OK: $n checks; $runs sessions, same point $same of $samePossible, prerequisite $needs of $needsPossible\n";
