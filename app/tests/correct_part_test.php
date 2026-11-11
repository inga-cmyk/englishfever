<?php
// php tests/correct_part_test.php: 'Correct the mistake' accepts the corrected words alone or the whole sentence (teacher, 11 November); copying the wrong part or one neighbour of a removed word is still wrong.
chdir(__DIR__ . '/..'); putenv('EF_DEV=1');
require 'src/Auth.php'; require 'src/Grader.php'; Config::load();
$cases = [
 ['Correct the mistake: Can you help to me?', ['Can you help me?'], ['help me'=>1,'me'=>0,'Can you help me?'=>1,'help to me'=>0,'you help me'=>1]],
 ['Correct the mistake: My sister and her friend works in a café.', ['My sister and her friend work in a café.'], ['work'=>1,'friend work'=>1,'works'=>0,'her friend work in'=>1,'cafe'=>0]],
 ['Correct the mistake: I am waiting the bus.', ['I am waiting for the bus.', "I'm waiting for the bus."], ['waiting for'=>1,'for'=>1,"I'm waiting for the bus"=>1,'waiting'=>0,'the bus'=>0]],
 ['Correct the mistake: We use to visit them every summer.', ['We used to visit them every summer.'], ['used to'=>1,'used'=>1,'we used to visit'=>1,'use to'=>0]],
];
$bad = 0;
foreach ($cases as [$q, $acc, $tests]) foreach ($tests as $ans => $want) {
  $r = Grader::grade(['kind'=>'text','q'=>$q,'answers'=>[$acc]], $ans);
  if ((int)$r['correct'] !== $want) { $bad++; echo "FAIL $q | '$ans' => ".($r['correct']?'right':'wrong')."\n"; }
}
echo $bad ? "SOME FAILED\n" : "ALL PASS\n";
