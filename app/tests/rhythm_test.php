<?php
// php tests/rhythm_test.php: the learner's practice rhythm for the welcome-back line (teacher, 22 November; Stats::rhythm)
putenv('EF_DEV=1');
chdir(__DIR__ . '/..');
require 'src/Auth.php';
spl_autoload_register(function ($c) { $f = 'src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load(); Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']); Db::migrate();
$bad = 0; function check($n, $c, $x = null) { global $bad; if (!$c) $bad++; echo ($c ? 'PASS ' : 'FAIL ') . "$n" . ($c ? '' : ' -> ' . json_encode($x)) . "\n"; }
function days(int $uid, array $ago) { Db::q('DELETE FROM activity WHERE user_id = ?', [$uid]);
    foreach ($ago as $a) Db::insert('activity', ['user_id' => $uid, 'day' => Stats::dayOffset(-$a), 'seconds' => 300, 'answers' => 10, 'xp' => 10]); }
days(1, [1, 3, 9]); check('3 practice days: new', Stats::rhythm(1) === 'new', Stats::rhythm(1));
days(1, range(1, 20)); check('20 of the last 28 days: daily', Stats::rhythm(1) === 'daily', Stats::rhythm(1));
days(1, [1, 3, 5, 8, 10, 13, 15, 17, 22, 25]); check('2-3 days a week for four weeks: few', Stats::rhythm(1) === 'few', Stats::rhythm(1));
days(1, [2, 9, 16, 23]); check('once a week for four weeks: weekly', Stats::rhythm(1) === 'weekly', Stats::rhythm(1));
days(1, [20, 21, 22, 23, 24, 25]); check('a burst three weeks ago, nothing since: irregular', Stats::rhythm(1) === 'irregular', Stats::rhythm(1));
days(1, [0, 2, 9, 16, 23]); check('today does not count', Stats::rhythm(1) === 'weekly', Stats::rhythm(1));
echo $bad ? "SOME FAILED\n" : "ALL PASS\n";
