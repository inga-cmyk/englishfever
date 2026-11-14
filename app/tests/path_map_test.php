<?php
// php app/tests/path_map_test.php
// My learning path follows the grammar map (14 November, C3): the teacher's level decisions of 13 November hold, a topic without
// tasks at a step's level is left out (never an empty step), and every topic of a step has tasks. In-memory database only.
putenv('EF_DEV=1');
require __DIR__ . '/../src/Auth.php';
spl_autoload_register(function ($c) { $f = __DIR__ . '/../src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load();
Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']);
Db::migrate();
foreach (CustomItems::preparedFiles() as $name => $path) CustomItems::import((string) file_get_contents($path), true);
Db::q("UPDATE custom_items SET status = 'approved'");
Content::reset();
$n = 0;
function check(bool $ok, string $why): void { global $n; $n++; if (!$ok) { fwrite(STDERR, "FAIL $why\n"); exit(1); } }
Db::insert('users', ['id' => 1, 'provider' => 'guest', 'nickname' => 'T', 'nickname_key' => 't', 'created_at' => time()]);
$p = Path::forUser(1);
$ids = array_column($p['steps'], 'id');
// decision 1: past perfect, second conditional and reported speech with the tense change are B1
foreach (['a2_pap', 'a2_c2', 'a2_rep'] as $gone) check(!in_array($gone, $ids, true), "no A2.2 step $gone (B1, decision 1)");
foreach (['b1_narr', 'b1_c2', 'b1_rep'] as $b1) check(in_array($b1, $ids, true), "the B1 step $b1 is there");
foreach ($p['steps'] as $s) if ($s['level'] === 'A2.2') foreach (['past_perfect', 'cond_second', 'rep_statements'] as $t) check(!in_array($t, $s['topics'], true), "no $t in the A2.2 step {$s['id']}");
// decision 2: relative clauses (who / which / that) and might / may are A2.2, with their own A2.2 tasks
$byHalf = Content::levelCounts()['by_half'];
foreach (['a2_rel' => 'relative_clauses', 'a2_might' => 'more_modals'] as $id => $t) {
    $s = $p['steps'][array_search($id, $ids, true)] ?? null;
    check($s !== null && $s['levels'] === ['A2.2'] && !$s['fallback'], "$id is an A2.2 step with A2.2 tasks");
    check(($byHalf[$t]['A2.2'] ?? 0) >= 25, "$t has at least 25 A2.2 tasks");
}
// no empty step: every topic of every step has tasks at the step's levels
foreach ($p['steps'] as $s) {
    check((bool) $s['topics'], "step {$s['id']} has topics");
    foreach ($s['topics'] as $t) { $c = 0; foreach ($s['levels'] as $l) $c += $byHalf[$t][$l] ?? 0; check($c > 0, "topic $t of step {$s['id']} has tasks at " . implode(',', $s['levels'])); }
}
echo "OK: $n path checks; " . count($p['steps']) . " steps\n";
