<?php
// Every imported draft task must accept its own answers (run after tests/drafts_test.py has imported the drafts).
require __DIR__ . '/../src/bootstrap.php';
$rows = Db::all("SELECT * FROM custom_items");
$m = new ReflectionMethod('CustomItems', 'fromRow'); $m->setAccessible(true);
$bad = 0; $n = 0;
foreach ($rows as $r) {
  $it = $m->invoke(null, $r); $n++;
  $tries = [];
  if ($it['kind'] === 'mcq') $tries[] = $it['correct'];
  elseif ($it['kind'] === 'text') foreach ($it['answers'] as $a) $tries[] = is_array($a) ? $a[0] : $a;
  elseif ($it['kind'] === 'gap') { $one = []; foreach ($it['answers'] as $alts) $one[] = is_array($alts) ? $alts[0] : $alts; $tries[] = $one; }
  elseif ($it['kind'] === 'order') $tries[] = explode(' ', $it['sentence']);
  else continue;
  foreach ($tries as $t) {
    $g = Grader::grade($it, $t);
    if ($it["kind"] !== "mcq" && $it["kind"] !== "order") { $low = is_array($t) ? array_map("mb_strtolower", $t) : mb_strtolower($t); if (empty(Grader::grade($it, $low)["correct"])) { $bad++; echo "LOWER ", $it["id"], " ", json_encode($low), "\n"; } }
    if (empty($g["correct"])) { $bad++; echo $it['id'], ' | ', $it['kind'], ' | ', mb_substr($it['q'] ?? '', 0, 80), ' | answer: ', json_encode($t), "\n"; }
  }
}
echo "$n items, $bad accepted answers marked wrong\n";
exit($bad ? 1 : 0);
