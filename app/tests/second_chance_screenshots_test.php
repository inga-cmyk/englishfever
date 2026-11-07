<?php
putenv('EF_DEV=1');
foreach(['Auth','Content','Grader','Db','Stats','Path','Engine','Reports','Mistakes'] as $name)require __DIR__.'/../src/'.$name.'.php';
Config::load();Db::connect(['driver'=>'sqlite','sqlite'=>':memory:']);Db::migrate();
$now=time();$day=date('Y-m-d');
Db::insert('users',['id'=>1,'provider'=>'guest','nickname'=>'Repeat test','nickname_key'=>'repeat-test','created_at'=>$now]);
$sid=Db::insert('psessions',['user_id'=>1,'mode'=>'practice','skills'=>'["used_to"]','level'=>'B1.2','target_len'=>10,'state'=>'{}','started_at'=>$now]);
$a=['id'=>'sc-old','skill'=>'used_to','level'=>'B1.2','bloom'=>3,'kind'=>'gap','q'=>'I ___ at night.','answers'=>[['used to work']]];
$b=$a;$b['id']='sc-twin';$b['q']='We ___ in the garden.';$b['answers']=[['used to play']];
Content::items();$rp=new ReflectionProperty(Content::class,'items');$rp->setValue(null,array_merge($rp->getValue(),[$a,$b]));$rp=new ReflectionProperty(Content::class,'byId');$rp->setValue(null,$rp->getValue()+array_column([$a,$b],null,'id'));
function add($it,$right,$time,$for=null){global $sid;Db::insert('attempts',['user_id'=>1,'psession_id'=>$sid,'item_id'=>$it['id'],'skill'=>$it['skill'],'level'=>$it['level'],'bloom'=>3,'correct'=>$right,'answer'=>json_encode([$it['answers'][0][0]]),'xp'=>0,'created_at'=>$time,'for_item'=>$for]);}
function need($v,$m){if(!$v)throw new RuntimeException($m);}
add($a,0,$now-5*86400);add($b,1,$now-4*86400,$a['id']);need(in_array($a['id'],Mistakes::reviewDue(1)),'Old fixed mistake is due');
add($b,1,$now,$a['id']);$scan=Mistakes::scan(1);need($scan['locked']===0,'Repeating same sentence is not new transfer');need(!in_array($a['id'],Mistakes::reviewDue(1,$scan)),'No immediate repeat after successful check today');
add($a,1,$now+86400,$a['id']);need(Mistakes::scan(1)['locked']===1,'Different sentence on another day locks it');
echo "OK: 4 Second Chance repeat scheduling checks\n";
