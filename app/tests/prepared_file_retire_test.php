<?php
// php tests/prepared_file_retire_test.php: a prepared file's tasks remember the file; importing it again retires the ones it no
// longer has (rewritten or dropped), and nothing else (teacher, 24 November). In-memory database only.
putenv('EF_DEV=1');
chdir(__DIR__ . '/..');
require 'src/Auth.php';
spl_autoload_register(function ($c) { $f = 'src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load(); Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']); Db::migrate();
$bad = 0; function check($n, $c, $x = null) { global $bad; if (!$c) $bad++; echo ($c ? 'PASS ' : 'FAIL ') . "$n" . ($c ? '' : ' -> ' . json_encode($x)) . "\n"; }

$head = "topic,level,type,task,correct answer,wrong options / checks,explanation shown to learner,explanation in Latvian,thinking level\n";
$t = 'Subject and verb: advanced rules';
$row = fn($q, $a) => "\"$t\",C1,gap,\"$q\",$a,,\"Because.\",\"Tāpēc.\",3\n";
$a = $row('Politics ___ never interested me. (have)', 'has');
$b = $row('The criteria ___ changed. (have)', 'have');
$b2 = $row('The criteria for the award ___ changed this year. (have)', 'have');
$c = $row('Ten kilometres ___ a long way. (be)', 'is');
$status = fn($q) => Db::val("SELECT status FROM custom_items WHERE data LIKE ?", ['%' . $q . '%']);
$approve = function () { Db::q("UPDATE custom_items SET status = 'approved'"); };

$r = CustomItems::import($head . $a . $b . $c, true, 'c1-test-1.csv');
check('first import adds three', $r['ok'] === 3 && $r['retired'] === 0, $r);
CustomItems::import($head . $row('Each of the rooms ___ a bathroom. (have)', 'has'), true, 'c1-other.csv');
CustomItems::import($head . $row('Neither of the answers ___ correct. (be)', 'is'), true);   // a file the teacher uploaded: no file name
$approve();

// b rewritten as b2, c dropped
$p = CustomItems::import($head . $a . $b2, false, 'c1-test-1.csv');
check('the check says one new and two to retire', $p['ok'] === 1 && $p['retired'] === 2, $p);
check('a check changes nothing', $status('The criteria ___ changed') === 'approved' && $status('Ten kilometres') === 'approved');
$s = CustomItems::import($head . $a . $b2, true, 'c1-test-1.csv');
check('the import retires the rewritten and the dropped task', $status('The criteria ___ changed') === 'retired' && $status('Ten kilometres') === 'retired', $s);
check('the unchanged task stays', $status('Politics') === 'approved');
check('the new version is added', $status('for the award') === 'draft');
check('a task from another prepared file stays', $status('Each of the rooms') === 'approved');
check('a task from an uploaded file stays', $status('Neither of the answers') === 'approved');
$again = CustomItems::import($head . $a . $b2, false, 'c1-test-1.csv');
check('importing again retires nothing more', $again['retired'] === 0 && $again['ok'] === 0, $again);

// a file with a refused row retires nothing (the refused row may be a task that is meant to stay)
$broken = CustomItems::import($head . $a . "\"$t\",C1,gap,\"No gap here.\",x,,\"Because.\",\"Tāpēc.\",3\n", true, 'c1-test-1.csv');
check('a refused row: nothing retired', $broken['bad'] > 0 && $broken['retired'] === 0 && $status('for the award') === 'draft', $broken);

// tasks added before they remembered their file: matched by text on the next import, then they remember it
Db::q("UPDATE custom_items SET src_file = NULL");
CustomItems::import($head . $a . $b2, true, 'c1-test-1.csv');
check('an older task learns its file on the next import', Db::val("SELECT src_file FROM custom_items WHERE data LIKE '%Politics%'") === 'c1-test-1.csv');
$d = CustomItems::import($head . $a, true, 'c1-test-1.csv');
check('then a dropped one is retired', $d['retired'] === 1 && $status('for the award') === 'retired', $d);

echo $bad ? "SOME FAILED\n" : "ALL PASS\n";
