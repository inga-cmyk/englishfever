<?php
// Isolated integration check: no server, production data, or persistent database.
// Run: php app/tests/twins_2_test.php
chdir(__DIR__ . '/..');
putenv('EF_DEV=1');
require 'src/Auth.php';
spl_autoload_register(function ($c) { $f = 'src/' . $c . '.php'; if (is_file($f)) require_once $f; });
Config::load(); Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']); Db::migrate();
foreach (glob('../docs/task-drafts/*.csv') as $f) {
    $r = CustomItems::import(file_get_contents($f), true);
    if ($r['bad']) throw new Exception('Existing CSV rejected: ' . basename($f));
}
$r = CustomItems::import(file_get_contents('../docs/task-drafts/pending/twins-1.csv'), true);
if ($r['bad']) throw new Exception('Batch 1 rejected');
function counts() {
    $items = array_merge(Content::items(), array_map(fn($r) => CustomItems::find($r['id']), CustomItems::listAll()['draft']));
    $counts = [];
    foreach ($items as $it) if (Content::role($it) !== 'learn') {
        $key = $it['skill'] . '|' . $it['level']; $counts[$key] = ($counts[$key] ?? 0) + 1;
    }
    return $counts;
}
$before = counts();

$r = CustomItems::import(file_get_contents('../docs/task-drafts/pending/twins-2.csv'), true);
if ($r['bad'] || $r['ok'] !== 50 || $r['updated'] || $r['same']) {
    echo json_encode($r, JSON_PRETTY_PRINT); exit(1);
}
$after = counts();
$checks = 0; $bad = 0; $roles = []; $groups = [];
function check_answer($it, $a, $want) {
    global $checks, $bad;
    $checks++;
    if ((bool)Grader::grade($it, $a)['correct'] !== $want) {
        $bad++; echo 'FAIL: ' . $it['q'] . ' ' . json_encode($a) . "\n";
    }
}
function product($groups) {
    $out = [[]];
    foreach ($groups as $g) { $next=[]; foreach($out as $prefix) foreach($g as $a) $next[]=array_merge($prefix,[$a]); $out=$next; }
    return $out;
}
foreach ($r['rows'] as $row) {
    if ($row['warnings']) { $bad++; echo 'WARNING: ' . implode('; ', $row['warnings']) . "\n"; }
    $it = CustomItems::find($row['id']);
    $key=$it['skill'].'|'.$it['level']; $groups[$key] = true;
    $role=Content::role($it); $roles[$role]=($roles[$role]??0)+1;
    if ($role==='learn') { $bad++; echo 'FAIL: non-evidence task ' . $it['q'] . "\n"; }
    if ($it['kind'] === 'mcq') {
        check_answer($it,$it['correct'],true);
        foreach($it['wrong'] as $w) check_answer($it,$w,false);
    } elseif ($it['kind'] === 'gap') {
        foreach(product($it['answers']) as $a) {
            check_answer($it,$a,true);
            check_answer($it,array_map(fn($s)=>str_replace("'","’",$s),$a),true);
        }
        for($i=0;$i<count($it['answers']);$i++) {
            $a=array_column($it['answers'],0); $a[$i]='zzz'; check_answer($it,$a,false);
        }
    } elseif ($it['kind'] === 'order') {
        foreach($it['answers'][0] as $a) check_answer($it,explode(' ',$a),true);
        check_answer($it,array_reverse(explode(' ',$it['sentence'])),false);
    } else {
        foreach($it['answers'][0] as $a) {
            check_answer($it,$a,true); check_answer($it,str_replace("'","’",rtrim($a,'.')),true);
        }
        check_answer($it,'zzz qqq',false);
    }
}
foreach(array_keys($groups) as $g) {
    echo $g . ': ' . ($before[$g]??0) . ' + ' . (($after[$g]??0)-($before[$g]??0)) . ' = ' . ($after[$g]??0) . "\n";
    if (($before[$g]??0) >= 10 || ($after[$g]??0) !== 10) $bad++;
}
if (isset(CustomItems::preparedFiles()['twins-2.csv'])) { $bad++; echo "FAIL: batch is packaged before review\n"; }
$again=CustomItems::import(file_get_contents('../docs/task-drafts/pending/twins-2.csv'),true);
if ($again['same']!==50 || $again['updated'] || $again['bad']) { $bad++; echo "FAIL: non-idempotent re-import\n"; }
echo 'Integrated import: 50 new, 0 duplicates, 0 replacements, 0 refused. Roles: ' . json_encode($roles) . "\n";
echo "$checks grading cases (all gap combinations, all order alternatives, MCQ distractors and invalid controls): $bad failures\n";
exit($bad?1:0);
