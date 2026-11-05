<?php
// Isolated regression: one construction must not repair another in the same topic.
putenv('EF_DEV=1');
foreach (['Auth','Content','Grader','Db','Stats','Path','Engine','Reports','Mistakes'] as $name) require __DIR__ . '/../src/' . $name . '.php';
Config::load();
Db::connect(['driver'=>'sqlite', 'sqlite'=>':memory:']); Db::migrate();
$n=0;
function expect($condition, $message) { global $n; $n++; if (!$condition) throw new RuntimeException($message); }
function fixture($id, $q, $answer, $learn=false) {
    return ['id'=>$id,'skill'=>'used_to','level'=>'B1.2','bloom'=>3,'kind'=>'gap','q'=>$q,'answers'=>[[$answer]],'bank'=>[$answer,'wrong'],'practice_only'=>$learn];
}
$a=fixture('test-habit','We ___ to the lake every summer.','used to go');
$b=fixture('test-accustomed',"She ___ alone.","isn't used to living");
$c=fixture('test-habit-twin','I ___ at night.','used to work');
$d=fixture('test-learn','He ___ every day.','used to swim',true);
$e=fixture('test-accustomed-twin','We ___ early.','are used to getting up');
Content::items();
$rp=new ReflectionProperty(Content::class,'items'); $rp->setValue(null,array_merge($rp->getValue(),[$a,$b,$c,$d,$e]));
$bp=new ReflectionProperty(Content::class,'byId'); $bp->setValue(null,$bp->getValue()+array_column([$a,$b,$c,$d,$e],null,'id'));
expect(!Mistakes::sameConstruction($a,$b),'Habit and accustomed state must be separate');
expect(Mistakes::sameConstruction($a,$c),'Different past habits match');
expect(Mistakes::sameConstruction($b,$e),'Negative and positive accustomed states match');
expect(!Mistakes::sameConstruction(null,$a),'Missing historical task cannot establish transfer');
expect(!Mistakes::sameConstruction($a,fixture('mixed','We used to work late but now we ___ early.','are used to leaving')),'Mixed task is not specific evidence');
expect(Content::role(['kind'=>'mcq','q'=>"'I used to swim.' What does it say?"])==='learn','Meaning-only task is learning');
$now=time();
Db::insert('users',['id'=>1,'provider'=>'guest','nickname'=>'Regression','nickname_key'=>'regression','created_at'=>$now]);
$sid=Db::insert('psessions',['user_id'=>1,'mode'=>'practice','skills'=>'["used_to"]','level'=>'B1.2','target_len'=>10,'state'=>'{}','started_at'=>$now]);
function attempt($it,$right,$for=null,$days=0) { global $sid,$now; Db::insert('attempts',['user_id'=>1,'psession_id'=>$sid,'item_id'=>$it['id'],'skill'=>$it['skill'],'level'=>$it['level'],'bloom'=>$it['bloom'],'correct'=>$right,'answer'=>'test','xp'=>0,'created_at'=>$now+$days*86400,'for_item'=>$for]); }
attempt($a,0); attempt($b,1,$a['id']);
expect(isset(Mistakes::scan(1)['open'][$a['id']]),'Second Chance cannot bypass construction matching');
attempt($d,1,$a['id']);
expect(isset(Mistakes::scan(1)['open'][$a['id']]),'Learning task cannot fix evidence');
$t=Mistakes::twin(1,$a['id'],[]);
expect($t && $t['id']===$c['id'],'Twin uses the same construction and excludes learning tasks');
attempt($c,1,$a['id']);
expect(Mistakes::scan(1)['fixed']===1,'Another habit fixes the original habit');
attempt($b,0);
expect(Mistakes::scan(1)['reopened']===0,'Other construction cannot reopen a fixed habit');
attempt($e,1,null,1);
expect(Mistakes::scan(1)['locked']===0,'Other construction cannot lock a fixed habit');
attempt($a,1,null,1);
expect(Mistakes::scan(1)['locked']===1,'Same construction checked next day locks it');
echo "OK: $n construction and mistake lifecycle checks\n";
