const { chromium } = require('playwright');
const fs = require('fs');
const BASE = 'http://127.0.0.1:8099', OUT = __dirname + '/shots/';
fs.mkdirSync(OUT, { recursive: true });
const raw = JSON.parse(fs.readFileSync(require('path').resolve(__dirname, '../../content/items.json'), 'utf8'));
const ITEMS = {}; (Array.isArray(raw) ? raw : raw.items).forEach(i => { ITEMS[i.id] = i; });
let ok = true; const errors = [];
function check(n, c, x) { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : '  -> ' + x)); }
const esc = t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 420, height: 900 } }); await ctx.addInitScript(() => {
    try { localStorage.setItem('ef_sound', '1'); } catch (e) {}
    window.__notes = 0;
    window.AudioContext = class { constructor() { this.state = 'running'; this.currentTime = 0; this.destination = {}; }
      createOscillator() { window.__notes++; return { type: '', frequency: { value: 0 }, connect() {}, start() {}, stop() {} }; }
      createGain() { return { gain: { setValueAtTime() {}, exponentialRampToValueAtTime() {} }, connect() {} }; } resume() {} };
  });
  const page = await ctx.newPage();
  page.on('pageerror', e => errors.push(e.message));
  await page.goto(BASE + '/sso-demo.php?uid=' + (8000 + Math.floor(Math.random() * 900)) + '&name=Comeback%20UI');
  await page.waitForSelector('#fn'); await page.click('button[type=submit]'); await page.waitForSelector('.hello h1');
  const post = (r, d) => page.evaluate(async ([r, d]) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json(), [r, d]);
  let s = await post('session/start', { mode: 'practice', source: 'path_check', skills: ['past_simple'], level: 'A2.2', length: 5 }), item = s.item;
  for (let i = 0; i < 5 && item; i++) { const a = await post('session/answer', { session_id: s.session.id, item_id: item.id, answer: 'zzz', time_ms: 2000 }); item = a.next; }
  await page.goto(BASE + '/index.html#/home'); await page.reload(); await page.waitForSelector('.card.focus');
  const card = page.locator('.card.fn-chance');
  check('Home shows the Second Chance card with the number of mistakes', await card.count() === 1 && /5 mistakes to fix/.test(await card.innerText()), await card.count() ? await card.innerText() : 'no card');
  await page.screenshot({ path: OUT + 'comeback-home.png', fullPage: true });
  await card.locator('button').click(); await page.waitForSelector('.task .q');
  check('the session is labelled Second Chance', /Second Chance/.test(await page.locator('.sess-top').innerText()));
  let fixedLines = 0, n = 0, lastAnswer = null;
  page.on('response', async r => { if (/api\.php\?r=session(?:%2F|\/)answer/.test(r.url())) { try { lastAnswer = await r.json(); } catch(e) {} } });
  for (let k = 0; k < 5; k++) {
    await page.waitForSelector('.task .q'); await page.waitForTimeout(150);
    const cur = await page.evaluate(async () => (await (await fetch('api.php?r=session/resume')).json()).resume);
    const it = ITEMS[cur.item.id];
    if (it.kind === 'mcq') await page.locator('label.opt', { hasText: it.correct }).first().click();
    else if (it.kind === 'gap' && it.bank) { for (let i = 0; i < it.answers.length; i++) await page.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(it.answers[i][0]) + '$') }).first().click(); }
    else if (it.kind === 'gap') { const inputs = page.locator('.task .q input.blank'); for (let i = 0; i < await inputs.count(); i++) await inputs.nth(i).fill(it.answers[i][0]); }
    else if (it.kind === 'text') await page.fill('.task textarea.type-in', it.answers[0][0]);
    else if (it.kind === 'order') { for (const t of it.sentence.split(' ')) await page.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(t) + '$') }).first().click(); }
    else if (it.kind === 'match') { for (const t of it.pairs.map(p => p[1])) await page.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(t) + '$') }).first().click(); }
    else await page.fill('.task textarea.write', it.model);
    const notesBefore = await page.evaluate(() => window.__notes);
    await page.click('.task .btn:has-text("Check answer")'); await page.waitForSelector('.feedback');
    if (await page.locator('.fixed-line').count()) fixedLines++;
    if (k === 0) { await page.screenshot({ path: OUT + 'comeback-feedback.png', fullPage: true }); check('the chime matches whether a mistake was fixed', (await page.evaluate(() => window.__notes)) - notesBefore === (lastAnswer.result.fixed ? 4 : 2), lastAnswer.result); }
    n++; await page.click('.feedback .nextrow .btn'); await page.waitForTimeout(300);
    if (await page.locator('.wins, h1:has-text("Great job")').count()) break;
  }
  await page.waitForSelector('h1');
  const h1 = await page.locator('h1').first().innerText();
  check('feedback counts exactly the fixes in the summary', fixedLines === lastAnswer.summary.fixed, fixedLines);
  check('the summary praises with the number of fixed mistakes', h1.includes('Great job! ' + fixedLines + (fixedLines === 1 ? ' mistake fixed.' : ' mistakes fixed.')), h1);
  const body = await page.locator('body').innerText();
  check('the summary ends with one line: today and next time', body.includes('Today: ' + fixedLines + (fixedLines === 1 ? ' mistake fixed' : ' mistakes fixed')), body.slice(0, 300));
  check('5 mistakes: 2 optional bonus questions are offered', /Bonus: 2 questions/.test(body) && (await page.locator('button:has-text("Enough for today")').count()) === 1, body.slice(0, 400));
  await page.screenshot({ path: OUT + 'comeback-summary.png', fullPage: true });
  await page.click('button:has-text("Try it")'); await page.waitForSelector('.task .q');
  check('the bonus is labelled with double XP', /Bonus · double XP/.test(await page.locator('.sess-top').innerText()), await page.locator('.sess-top').innerText());
  await page.screenshot({ path: OUT + 'comeback-bonus.png', fullPage: true });
  await page.goto(BASE + '/index.html#/home'); await page.reload(); await page.waitForSelector('.card.focus');
  const dashboard = await page.evaluate(async () => (await fetch('api.php?r=dashboard')).json());
  check('Home card matches the remaining mistake queue', (await page.locator('.card.fn-chance').count() > 0) === (dashboard.comeback.open > 0 || dashboard.comeback.review > 0));
  check('no page errors', errors.length === 0, errors);
  console.log(ok ? 'ALL PASS' : 'SOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
