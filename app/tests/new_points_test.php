<?php
// php app/tests/new_points_test.php
// The New group (teacher, 15 November, option A): the grammar points of batch 4 are shown as their own tiles with their own
// card, and practising one serves only that point's tasks (state point, source new_point). In-memory database only.
putenv('EF_DEV=1');
require __DIR__ . '/../src/Auth.php';
spl_autoload_register(function ($c) { $f = __DIR__ . '/../src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load();
Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']);
Db::migrate();
$n = 0;
function check(bool $ok, string $why): void { global $n; $n++; if (!$ok) { fwrite(STDERR, "FAIL $why\n"); exit(1); } }

foreach (CustomItems::preparedFiles() as $name => $path) CustomItems::import((string) file_get_contents($path), true);
Db::q("UPDATE custom_items SET status = 'approved'");
Content::reset();

$pts = Content::liveMeta()['new_points'] ?? [];
$new = (time() - strtotime('2026-11-15')) < 21 * 86400;
check(!$new || count($pts) === 17, 'the 17 new points are sent while they are new (' . count($pts) . ')');
foreach ($pts as $p) {
    check(!empty($p['rule']['v2']['choice']) && !empty($p['rule_lv']['v2']['choice']) && !empty($p['rule']['v2']['mistakes']), "a card in EN and LV: {$p['id']}");
    check($p['n'] >= 20 && $p['levels'], "tasks and levels: {$p['id']}");
}
$u = 0;
foreach ($pts as $p) {
    $u++;
    Db::insert('users', ['id' => $u, 'provider' => 'guest', 'nickname' => "T$u", 'nickname_key' => "t-$u", 'created_at' => time()]);
    $s = Engine::start($u, 'practice', ['present_simple'], null, 10, null, 'practice_page', $p['id']);   // the point decides the topic
    $sid = (int) $s['session']['id'];
    $item = $s['item'];
    for ($k = 0; $k < 6 && $item; $k++) {
        $it = Content::item($item['id']);
        $needs = Content::mapPoint($p['id'])['needs'] ?? [];   // after two wrong answers one task may come from a point it stands on (C2)
        check(Content::point($it) === $p['id'] || in_array(Content::point($it), $needs, true), "only tasks of {$p['id']}, got " . Content::point($it) . ' ' . $it['id']);
        $r = Engine::answer($u, $sid, $it['id'], 'zzz qqq', 2000);   // also after a wrong answer
        $item = $r['next'] ?? null;
    }
    check(Db::val('SELECT source FROM psessions WHERE id = ?', [$sid]) === 'new_point', 'source new_point');
}
// an unknown point is refused
try { Engine::start(99, 'practice', [], null, 10, null, null, 'no_such_point'); check(false, 'unknown point refused'); } catch (ApiError $e) { check(true, ''); }
echo "ALL PASS: $n new-point checks\n";
