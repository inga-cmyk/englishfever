<?php
// Import the exact reported prompts, then the corrections, in an isolated DB.
putenv('EF_DEV=1');
require __DIR__ . '/../src/Auth.php';
spl_autoload_register(function ($c) { $f=__DIR__.'/../src/'.$c.'.php'; if(is_file($f)) require_once $f; });
Config::load(); Db::connect(['driver'=>'sqlite','sqlite'=>':memory:']); Db::migrate();
function csvText($rows) { $f=fopen('php://temp','r+'); foreach($rows as $r) fputcsv($f,$r,',','"','\\'); rewind($f); return stream_get_contents($f); }
function need($ok,$message) { if(!$ok) throw new RuntimeException($message); }
$new=[]; $old=[];
foreach(['compare-past-1.csv','unreal-time-1.csv'] as $file) {
    $f=fopen(__DIR__.'/../../docs/task-drafts/'.$file,'r'); $head=fgetcsv($f,0,',','"','\\'); $head[0]=ltrim($head[0],"\xEF\xBB\xBF");
    while(($r=fgetcsv($f,0,',','"','\\'))!==false) {
        if(!str_contains($r[3],'We ___ tennis for half an hour') && !str_contains($r[3],'At last the bus came.') && !str_contains($r[3],"It's high time we ___ home")) continue;
        $new[]=$r; $o=$r; $o[3]=$r[9]; $o[9]='';
        $o[5]=str_contains($r[3],"It's high time") ? 'bank: went | will go | going | to going' : '';
        $old[]=$o;
    }
    fclose($f);
}
need(count($new)===3,'Three reported draft corrections found');
$a=CustomItems::import(csvText(array_merge([$head],$old)),true);
need($a['bad']===0 && count($a['rows'])===3,'Original prompts import');
$b=CustomItems::import(csvText(array_merge([$head],$new)),true);
need($b['bad']===0 && count($b['rows'])===3,'Corrected prompts import');
foreach($a['rows'] as $r) need(Db::val('SELECT status FROM custom_items WHERE item_id=?',[$r['id']])==='retired','Old prompt retired');
foreach($b['rows'] as $r) {
    $it=CustomItems::find($r['id']);
    need(!empty($it['bank']),'Corrected task offers constrained choices');
    need(Grader::grade($it,[$it['answers'][0][0]])['correct'],'New answer accepted');
}
$c=CustomItems::import(csvText(array_merge([$head],$new)),true);
need($c['bad']===0 && $c['same']===3,'Reimport is idempotent');
echo "OK: three reported drafts retire old versions and reimport safely\n";
