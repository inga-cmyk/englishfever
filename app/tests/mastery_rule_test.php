<?php
// php tests/mastery_rule_test.php: Learned counts different sentences (U4 A) and at most 3 word orders in a topic about a form (U1 B) (teacher, 12 November)
putenv('EF_DEV=1');
chdir(__DIR__ . '/..');
require 'src/Auth.php';
spl_autoload_register(function ($c) { $f = 'src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load(); Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']); Db::migrate();
$bad = 0; function check($n, $c) { global $bad; if (!$c) $bad++; echo ($c ? 'PASS ' : 'FAIL ') . "$n\n"; }
$all = array_values(array_filter(Content::items(), fn($i) => Content::role($i) !== 'learn'));
// a task with a fake sentence of its own, so the test does not depend on how many word orders the bank has
$orders = [];
$base = array_values(array_filter($all, fn($i) => $i['kind'] === 'order' && !in_array($i['skill'], Path::ORDER_SKILLS, true)))[0];
for ($k = 0; $k < 5; $k++) { $o = $base; $o['id'] = 'test-order-' . $k; $o['sentence'] = "sentence number $k"; $orders[] = $o; }
Content::addTest($orders);
$skill = $base['skill']; $lv = [$base['level']];
$ev = array_values(array_filter(Content::items(), fn($i) => $i['skill'] === $skill && Content::role($i) !== 'learn'));
$t = time() - 5 * 86400;
$add = function (array $it, int $at) { Db::insert('attempts', ['user_id' => 1, 'psession_id' => 1, 'item_id' => $it['id'], 'skill' => $it['skill'], 'level' => $it['level'], 'bloom' => (int) $it['bloom'], 'correct' => 1, 'answer' => '', 'created_at' => $at]); };
foreach ($orders as $k => $o) $add($o, $t + $k);
$m = Path::mastery(1, $skill, $lv);
check('only 3 of 5 right word orders count in a form topic', $m['distinct'] === 3);
// two tasks with the same sentence count once: a typed gap and a choice made from it
$g = array_values(array_filter($all, fn($i) => $i['kind'] === 'gap' && empty($i['bank']) && count($i['answers']) === 1))[0];
$c = $g; $c['id'] = 'test-choice'; $c['kind'] = 'mcq'; $c['correct'] = $g['answers'][0][0]; $c['wrong'] = ['x', 'y', 'z']; unset($c['answers']);
Content::addTest([$c]);
check('a gap and a choice with the same sentence have the same key', Content::sentenceKey($g) === Content::sentenceKey(Content::item('test-choice')));
Db::q('DELETE FROM attempts');
$add($g, $t); $add(Content::item('test-choice'), $t + 1);
check('the same sentence in two tasks counts once', Path::mastery(1, $g['skill'], null)['distinct'] === 1);
echo $bad ? "SOME FAILED\n" : "ALL PASS\n";
