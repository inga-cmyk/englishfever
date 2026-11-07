// Summary/alternative-answer scenarios from Inga's iPhone screenshots, using the real UI.
const {chromium}=require('playwright'),fs=require('fs'),path=require('path'),assert=require('assert');
const APP=path.resolve(__dirname,'../..');
(async()=>{
 const browser=await chromium.launch();let checks=0;
 for(const scenario of ['comeback','placement','alternative']){
  const context=await browser.newContext({viewport:{width:390,height:844},serviceWorkers:'block'}),page=await context.newPage();
  const item={id:'screen-fixture',kind:'gap',skill:'narrative_b2',skill_label:'Narrative tenses',level:'B2.1',bloom:3,q:'Tom was tired when he got home. He ___ hard all day. (work)',blanks:1};
  const session={id:901,mode:scenario==='placement'?'placement':'practice',length:1,n:0,correct:0,xp:0,level:'B2.1',skills:['narrative_b2'],comeback:scenario==='comeback'};
  const result={correct:true,show:'had been working',why:'An earlier activity.',specific:'Correct too: had worked focuses on the completed work.',alt:true,xp:14};
  const summary={session_id:901,mode:session.mode,n:scenario==='placement'?40:1,correct:scenario==='placement'?34:1,accuracy:scenario==='placement'?85:100,xp:14,by_skill:[],by_cat:{},comeback:scenario==='comeback',fixed:0,locked:1,open_after:0,review_due:1,next_topic:null,overall_level:'B2.1',gaps:[],parked:0};
  await page.route('**/*',async route=>{const u=new URL(route.request().url());if(u.pathname==='/api.php'){
   const r=u.searchParams.get('r');let json={};
   if(r==='config')json={privacy_url:'#',version:'local screenshot review'};
   if(r==='meta')json=JSON.parse(fs.readFileSync(path.join(APP,'content/meta.json')));
   if(r==='me')json={user:{id:1,role:'student',nickname:'Screenshot test',guest:false,lang:'en'}};
   if(r==='session/resume')json={resume:{session,item}};
   if(r==='session/answer')json={result,session:{...session,n:1},done:true,summary};
   if(r==='path')json={steps:[],current:null};return route.fulfill({json});
  }const file=path.join(APP,u.pathname==='/index.html'?'index.html':u.pathname);if(!file.startsWith(APP)||!fs.existsSync(file))return route.fulfill({status:404,body:''});return route.fulfill({body:fs.readFileSync(file),contentType:({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml'})[path.extname(file)]||'application/octet-stream'});});
  await page.goto('http://screenshot.invalid/index.html#/session');
  await page.getByRole('textbox',{name:'Answer 1',exact:true}).fill('had worked');await page.getByRole('button',{name:'Check',exact:true}).click();
  await page.waitForSelector('.submitted-answer');
  assert((await page.locator('.submitted-answer').innerText()).includes('had worked'));checks++;
  assert((await page.locator('.feedback').innerText()).includes('completed work'));checks++;
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));checks++;
  if(scenario!=='alternative'){
   await page.getByRole('button',{name:'See my results',exact:true}).click();await page.waitForSelector('.summary-cheer');
   const t=await page.locator('main').innerText();assert(!t.includes('Skills check'));checks++;
   if(scenario==='comeback'){assert(t.includes('Checked again and still right'));assert(t.includes('another earlier mistake is ready'));checks+=2;}
   if(scenario==='placement'){assert(!t.includes('No mistakes to fix'));assert(!t.includes('Nothing left to fix'));checks+=2;}
  }
  await page.waitForTimeout(500);
  const out=process.env.EF_REVIEW_SHOTS||'/tmp';fs.mkdirSync(out,{recursive:true});await page.screenshot({path:path.join(out,scenario+'.png'),fullPage:true});
  await context.close();
 }
 await browser.close();console.log('ALL PASS: '+checks+' screenshot summary and alternative-form checks');
})().catch(e=>{console.error(e);process.exit(1)});
