<?php
// The 7 November screenshot fixes, tested against the real importer and grader.
putenv('EF_DEV=1');
require __DIR__.'/../src/Auth.php';
spl_autoload_register(function($c){$f=__DIR__.'/../src/'.$c.'.php';if(is_file($f)) require_once $f;});
Config::load(); Db::connect(['driver'=>'sqlite','sqlite'=>':memory:']); Db::migrate();
$n=0;
function need($v,$m){global $n;$n++;if(!$v)throw new RuntimeException($m);}
$items=[];
foreach(['a2-big-1.csv','b1-tenses-2.csv','compare-past-1.csv','comparison-1.csv'] as $f){
 $result=CustomItems::import(file_get_contents(__DIR__.'/../../docs/task-drafts/'.$f),true);
 need($result['bad']===0,"$f imports without errors");
 foreach($result['rows'] as $row){$it=CustomItems::find($row['id']);$items[]=$it;}
}
function task($fragment){global $items;foreach($items as $it)if(str_contains($it['q'],$fragment)||str_contains($it['sentence']??'',$fragment))return $it;throw new RuntimeException('Missing '.$fragment);}
need(Grader::grade(task('riga is smaller'),'london is smaller than riga')['correct'],'Grammar order is not a geography quiz');
$it=task('the parcel arrives');need(Grader::grade($it,'will you be at home when the parcel arrives')['correct'],'Question accepted');need(!Grader::grade($it,'you will be at home when the parcel arrives')['correct'],'Instruction explicitly requires a question');
$it=task('Tom was tired');$g=Grader::grade($it,['had worked']);need($g['correct']&&!empty($g['alt'])&&str_contains($g['specific'],'completed'),'Valid simple alternative has its own explanation');
need(!Mistakes::demonstratesTarget($it,json_encode(['had worked'])),'Simple alternative does not demonstrate continuous');
need(Mistakes::demonstratesTarget($it,json_encode(['had been working'])),'Continuous answer demonstrates continuous');
$it=task('the kitchen next month');$g=Grader::grade($it,['are painting']);need($g['correct']&&!empty($g['alt'])&&str_contains($g['specific'],'arrangement'),'Alternative future form has its own explanation');
$it=task('the team');need(empty($it['bank']),'Obvious incorrect cards removed');need(Grader::grade($it,['will win'])['correct'],'Typed prediction accepted');
$it=task('fits');need(!str_contains(json_encode($it),'gone'),'No I have gone it sentence');need(Grader::grade($it,array_map(fn($pair)=>$pair[1],$it['pairs']))['correct'],'All participles match');
$it=task("I've hurt my hand");need(str_contains($it['q'],"\nB:"),'Dialogue has separate turns');need(Grader::grade($it,['did','do'])['correct'],'New dialogue graded');
$it=task('what we know');need(count(array_unique(array_column($it['pairs'],1)))===4,'Four specific distinct meanings');
$it=task('finish the report. Then');need(!str_contains($it['why'],'Going to'),'When rewrite has relevant explanation');
$bundle=__DIR__.'/../../docs/review/labotie-10-uzdevumi-2026-11-07.csv';
if(is_file($bundle)){ $import=CustomItems::import(file_get_contents($bundle),true);need($import['bad']===0 && count($import['rows'])===10,'Delivery CSV imports all ten rows'); }
echo "OK: $n screenshot/content regressions\n";
