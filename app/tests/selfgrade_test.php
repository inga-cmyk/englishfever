<?php
// Every built-in task must accept its own answers, also typed in small letters (teacher, 28 October: correct answers were marked wrong).
require __DIR__ . '/../src/bootstrap.php';
$items = json_decode(file_get_contents(__DIR__ . '/../content/items.json'), true);
$bad = 0;
foreach ($items as $it) {
  $tries = [];
  if ($it['kind'] === 'mcq') $tries[] = $it['correct'];
  elseif ($it['kind'] === 'text') foreach ($it['answers'] as $a) $tries[] = is_array($a) ? $a[0] : $a;
  elseif ($it['kind'] === 'gap') { $one = []; foreach ($it['answers'] as $alts) $one[] = is_array($alts) ? $alts[0] : $alts; $tries[] = $one; }
  elseif ($it['kind'] === 'order') $tries[] = explode(' ', $it['sentence']);
  else continue;
  foreach ($tries as $t) {
    if (empty(Grader::grade($it, $t)['correct'])) { $bad++; echo $it['id'], ' ', json_encode($t), "\n"; }
    if ($it['kind'] === 'text' || $it['kind'] === 'gap') { $low = is_array($t) ? array_map('mb_strtolower', $t) : mb_strtolower($t); if (empty(Grader::grade($it, $low)['correct'])) { $bad++; echo 'LOWER ', $it['id'], ' ', json_encode($low), "\n"; } }
  }
}
echo count($items), " built-in items, $bad problems\n";
exit($bad ? 1 : 0);
