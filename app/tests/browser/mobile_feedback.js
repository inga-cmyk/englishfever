// Deterministic phone regression using the real frontend and mocked API replies.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const assert = require('assert');
const APP = path.resolve(__dirname, '../..');
(async () => {
  const browser = await chromium.launch();
  let checks = 0;
  for (const width of [320, 390]) for (const lang of ['en', 'lv']) {
    const context = await browser.newContext({ viewport: { width, height: 844 }, serviceWorkers: 'block' });
    const page = await context.newPage(); const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    const answer = 'If I had known about the cancellation before leaving the office, I would have called my colleague and arranged another meeting.';
    const item = { id: 'mobile-fixture', kind: 'text', skill: 'cond_third', skill_label: 'Narrative tenses with past perfect continuous', level: 'B2.1', bloom: 3, q: 'Rewrite the sentence without changing its meaning: I did not know about the cancellation, so I did not call my colleague.', practice_context: 'review' };
    const session = { id: 900, mode: 'practice', length: 10, n: 9, correct: 8, xp: 80, level: 'B2.1', skills: ['cond_third'] };
    const result = { correct: true, show: answer, why: 'The past situation is imagined differently.', why_lv: 'Iztēlojamies citādu pagātnes situāciju.', xp: 12, adapt: 'same', fixed: false };
    const summary = { session_id: 900, mode: 'practice', n: 10, correct: 9, accuracy: 90, xp: 92, by_skill: [], by_cat: { recognise: { n: 4, correct: 4 }, use: { n: 6, correct: 5 }, write: { n: 0, correct: 0 } } };
    await context.addInitScript(({item, result}) => sessionStorage.setItem('ef_hist_900', JSON.stringify(Array.from({length:9}, (_,n) => ({n,item,ans:'Earlier answer',result})))), {item,result});
    await page.route('**/*', async route => {
      const u = new URL(route.request().url());
      if (u.pathname === '/api.php') {
        const r = u.searchParams.get('r'); let json = {};
        if (r === 'config') json = { privacy_url: '#', version: 'review' };
        else if (r === 'meta') json = JSON.parse(fs.readFileSync(path.join(APP,'content/meta.json')));
        else if (r === 'me') json = {user:{id:1,role:'student',nickname:'Mobile test',guest:true,lang}};
        else if (r === 'session/resume') json = {resume:{session,item}};
        else if (r === 'session/answer') json = {result, session:{...session,n:10},done:true,summary};
        else if (r === 'path') json = {steps:[],current:null};
        return route.fulfill({json});
      }
      const target = path.join(APP, u.pathname === '/' ? 'index.html' : u.pathname);
      if (!target.startsWith(APP) || !fs.existsSync(target)) return route.fulfill({status:404,body:''});
      const mime = {'.html':'text/html','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.json':'application/json','.webmanifest':'application/manifest+json'}[path.extname(target)] || 'application/octet-stream';
      return route.fulfill({body:fs.readFileSync(target),contentType:mime});
    });
    await page.goto('http://ef-test.invalid/index.html#/session');
    await page.waitForSelector('textarea.type-in');
    assert((await page.locator('.sess-top').innerText()).includes('Review')); checks++;
    const stop = await page.getByRole('button',{name:'Quit',exact:true}).boundingBox();
    assert(stop && stop.x >= 0 && stop.x + stop.width <= width); checks++;
    await page.locator('textarea.type-in').fill(answer);
    assert(await page.locator('textarea.type-in').evaluate(el=>el.scrollHeight<=el.clientHeight+2)); checks++;
    await page.getByRole("button",{name:"Check",exact:true}).click();
    await page.waitForSelector('.submitted-answer');
    assert((await page.locator('.submitted-answer').innerText()).includes(answer)); checks++;
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth+1)); checks++;
    if (width === 390 && process.env.EF_REVIEW_SHOTS) {
      fs.mkdirSync(process.env.EF_REVIEW_SHOTS,{recursive:true});
      await page.waitForTimeout(400);
      await page.screenshot({path:path.join(process.env.EF_REVIEW_SHOTS,'feedback-'+lang+'.png'),fullPage:true});
    }
    await page.getByRole('button',{name:'Something is wrong',exact:true}).click();
    assert(!(await page.getByRole('button',{name:'See my results',exact:true}).isEnabled())); checks++;
    await page.getByRole('textbox',{name:'Comment',exact:true}).fill('Regression test comment');
    await page.getByRole('button',{name:'Cancel',exact:true}).click();
    assert(await page.getByRole('button',{name:'See my results',exact:true}).isEnabled()); checks++;
    await page.getByRole('button',{name:/Previous/}).click();
    await page.waitForSelector('textarea.type-in:disabled');
    assert((await page.locator('.sess-top').innerText()).includes('looking back')); checks++;
    // Return to current answered task through the question strip, then results.
    await page.locator('.dots .dot').last().click();
    await page.getByRole('button',{name:'See my results',exact:true}).click();
    await page.waitForSelector('.summary-cheer');
    assert(await page.locator('.cats').count() === 0); assert((await page.locator('.summary-cheer').innerText()).length > 0); checks++;
    await page.screenshot({path:path.join(process.env.EF_REVIEW_SHOTS || '/tmp','summary-'+width+'-'+lang+'.png'),fullPage:true});
    const stats = page.locator('.summary .grid.g3').first();
    assert((await stats.locator('.big').count())===3); checks++;
    assert(errors.length === 0, errors.join('\n')); checks++;
    await context.close();
  }
  await browser.close(); console.log('ALL PASS: '+checks+' phone feedback, review and summary checks');
})().catch(e=>{console.error(e);process.exit(1)});
