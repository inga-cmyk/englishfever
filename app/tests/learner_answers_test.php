<?php
// Historical learner variants, actual CSV importer/grader, isolated in-memory DB.
putenv('EF_DEV=1');
require __DIR__.'/../src/Auth.php';
spl_autoload_register(function($c){$p=__DIR__.'/../src/'.$c.'.php';if(is_file($p))require_once $p;});
Config::load(); Db::connect(['driver'=>'sqlite','sqlite'=>':memory:']);Db::migrate();
$n=0;
function demand($ok,$why){global $n;$n++;if(!$ok)throw new RuntimeException($why);}
$root=__DIR__.'/../../docs/task-drafts/';
$fixes=json_decode(file_get_contents($root.'_src/learner_fixes_20261108.json'),true);
$items=[];
foreach(array_keys($fixes) as $file){
 $r=CustomItems::import(file_get_contents($root.$file),true);
 demand($r['bad']===0,$file.' must import: '.json_encode(array_filter($r['rows'],fn($x)=>!$x['ok'])));
 foreach($r['rows'] as $row)if(isset($row['id']))$items[$row['id']]=CustomItems::find($row['id']);
}
function pick($q,$sentence=null){global $items;foreach($items as $i)if($i['q']===$q&&($sentence===null||($i['sentence']??null)===$sentence))return $i;throw new RuntimeException('Missing task: '.$q.' / '.$sentence);}
foreach($fixes as $file=>$rows)foreach($rows as $fix){
 $set=$fix['set'];$q=$set[3]??$fix['match'][1];$sentence=$fix['match'][0]==='order'?$fix['match'][2]:null;
 $it=pick($q,$sentence);
 if($it['kind']==='order'){
  $alts=explode('|',preg_replace('/^also accepted:\s*/i','',$set[5]));
  foreach($alts as $a)demand(Grader::grade($it,trim($a))['correct'],$fix['id'].' rejects '.trim($a));
  demand(!Grader::grade($it,$it['sentence'].' extra')['correct'],'Extra word cannot pass');
 }
}
$since=pick('I ___ Anna since primary school, and we are still friends. (know)');
demand(Grader::grade($since,['have known'])['correct'],'Continuing state uses present perfect');
foreach(['knew','know','have been knowing','did see','have seen'] as $a)demand(!Grader::grade($since,[$a])['correct'],'Present-perfect task rejects '.$a);
$negative=pick("Make only the result negative. Keep 'If she comes': If she comes, I will stay.");
demand(Grader::grade($negative,"If she comes, I won't stay.")['correct'],'Main-clause negative accepted');
demand(!Grader::grade($negative,"If she doesn't come, I won't stay.")['correct'],'Explicit condition must stay unchanged');
$used=pick('When I was a teenager, I ___ any money, so I walked everywhere. (not / have)');
$g=Grader::grade($used,['used not to have']);demand($g['correct']&&str_contains($g['specific'],'formal'),'Formal negative explained');
demand(!Grader::grade($used,["didn't used to have"])['correct'],'Malformed used to still rejected');
$hw=pick('Say you did not do it yet: I / not / finish / homework / yet.');
demand(Grader::grade($hw,'I have not finished homework yet.')['correct'],'No invented possessive required');
demand(!Grader::grade($hw,'I have not finish homework yet.')['correct'],'Missing participle rejected');
$date=pick('Correct the mistake: My birthday is in 5 May.');
demand(Grader::grade($date,'My birthday is on 5th May.')['correct'],'Ordinal date accepted');
demand(!Grader::grade($date,'My birthday is in 5th May.')['correct'],'Wrong preposition rejected');
$persons=pick('Many ___ came to the party. (person)');$g=Grader::grade($persons,['persons']);
demand($g['correct']&&str_contains($g['specific'],'formal'),'Formal plural accepted with note');
demand(!Grader::grade($persons,['person'])['correct'],'Singular not accepted');
$live=array_column(Content::items(),null,'id');
foreach($live as $it){
 if(str_starts_with($it['id'],'cf-B12-3a'))demand(Grader::grade($it,"You won't improve unless you practice.")['correct'],'Built-in unless alternative accepted');
 if(str_starts_with($it['id'],'ps-B11-3b')){
  demand(Grader::grade($it,"She hasn't got any money.")['correct'],'Built-in possession alternative accepted');
  demand(!Grader::grade($it,'She has got any money.')['correct'],'Positive not accepted for negative instruction');
 }
}
// A re-import is repeatable and does not create another copy of an existing item.
$count=(int)Db::val('SELECT COUNT(*) FROM custom_items');
foreach(array_keys($fixes) as $file){$r=CustomItems::import(file_get_contents($root.$file),true);demand($r['bad']===0,'Re-import '.$file);}
demand((int)Db::val('SELECT COUNT(*) FROM custom_items')===$count,'Re-import must not add duplicates');
// A changed diagnostic example retires only its own earlier question.
$fh=fopen($root.'compare-past-1.csv','r');$head=fgetcsv($fh,0,',','"','\\');$newRow=null;
while(($r=fgetcsv($fh,0,',','"','\\'))!==false)if(($r[3]??'')===$since['q']){$newRow=$r;break;}fclose($fh);
demand($newRow!==null,'Revised diagnostic row exists');
$oldRow=$newRow;$oldRow[3]=$newRow[9];$oldRow[4]='Have / seen';$oldRow[5]='';$oldRow[9]='';$oldRow[13]='';
function singleCsv($head,$row){$f=fopen('php://temp','r+');fputcsv($f,$head,',','"','');fputcsv($f,$row,',','"','');rewind($f);return stream_get_contents($f);}
Db::connect(['driver'=>'sqlite','sqlite'=>':memory:']);Db::migrate();
$old=CustomItems::import(singleCsv($head,$oldRow),true);demand($old['bad']===0,'Original diagnostic imports');
$oldId=$old['rows'][0]['id'];Db::update('custom_items',['status'=>'approved'],'item_id = ?',[$oldId]);
$replacement=CustomItems::import(singleCsv($head,$newRow),true);demand($replacement['bad']===0,'Replacement imports');
demand(Db::val('SELECT status FROM custom_items WHERE item_id = ?',[$oldId])==='retired','Old diagnostic retired, not overwritten');
demand(CustomItems::find($oldId)['q']===$oldRow[3],'Historical prompt still readable');
echo "OK: $n learner-answer/import regressions\n";
