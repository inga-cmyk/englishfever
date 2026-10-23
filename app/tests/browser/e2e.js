const { chromium } = require('playwright');
const fs = require('fs');
const ITEMS = Object.fromEntries(JSON.parse(fs.readFileSync('/home/user/englishfever/app/content/items.json')).map(i => [i.id, i]));
const BASE = 'http://127.0.0.1:8099';
const OUT = __dirname + '/shots/';

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1100, height: 900 } });
  const page = await ctx.newPage();
  const errors = [];
  async function noJunk(p, label){ const t = await p.evaluate(() => document.body.innerText); if (/null|undefined|NaN|\[object/.test(t)) errors.push('junk text on ' + label + ': ' + (t.match(/.{0,30}(null|undefined|NaN|\[object).{0,30}/)||[''])[0]); }
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  let current = null;
  page.on('response', async r => {
    if (!r.url().includes('api.php')) return;
    if (r.status() >= 500) errors.push('HTTP ' + r.status() + ' ' + r.url());
    try { const j = await r.json(); if (j.item) current = j.item; if (j.next) current = j.next; if (j.done) current = null; } catch (e) {}
  });

  await page.goto(BASE + '/index.html');
  await page.waitForSelector('.hero');
  await noJunk(page,'01-welcome'); await page.screenshot({ path: OUT + '01-welcome.png', fullPage: true });

  const nick = 'Guest ' + Math.floor(Math.random() * 90000 + 10000);
  const wtxt = await page.evaluate(() => document.body.innerText);
  for (const needle of ['Registered at englishfever.com?', 'Continue with my account', 'Try it as a guest', 'Your name', '(optional)', 'Continue as guest', 'Create a free account']) if (!wtxt.includes(needle)) errors.push('welcome page misses: ' + needle);
  if (/Remember it|teacher can help|do not use your real name/i.test(wtxt)) errors.push('old long hint texts still on the welcome page');
  await page.fill('#nick', nick);
  await page.click('button[type=submit]');
  await page.waitForSelector('.hello h1');
  await page.waitForTimeout(400);
  await noJunk(page,'02-home-new'); await page.screenshot({ path: OUT + '02-home-new.png', fullPage: true });

  async function answerCurrent(correct, shot) {
    await page.waitForSelector('.task .q');
    await page.waitForTimeout(150);
    const it = ITEMS[current.id];
    if (shot) await page.screenshot({ path: OUT + shot + '-task.png', fullPage: true });
    if (it.kind === 'mcq') {
      const txt = correct ? it.correct : it.wrong[0];
      await page.locator('label.opt', { hasText: txt }).first().click();
    } else if (it.kind === 'gap' && it.bank) {
      for (let i = 0; i < it.answers.length; i++) {
        const t = correct ? it.answers[i][0] : it.bank.find(x => x !== it.answers[i][0]);
        await page.locator('.dnd-bank .chip', { hasText: new RegExp('^' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }).first().click();
      }
    } else if (it.kind === 'gap') {
      const inputs = page.locator('.task .q input.blank');
      const n = await inputs.count();
      for (let i = 0; i < n; i++) await inputs.nth(i).fill(correct ? it.answers[i][0] : 'zzz');
    } else if (it.kind === 'text') {
      await page.fill('.task input.type-in', correct ? it.answers[0][0] : 'zzz');
    } else if (it.kind === 'order') {
      const toks = it.sentence.split(' ');
      for (const t of (correct ? toks : [...toks].reverse())) await page.locator('.dnd-bank .chip', { hasText: new RegExp('^' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }).first().click();
    } else if (it.kind === 'match') {
      const rights = it.pairs.map(p => p[1]);
      for (const t of (correct ? rights : [...rights.slice(1), rights[0]])) await page.locator('.dnd-bank .chip', { hasText: new RegExp('^' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }).first().click();
    } else {
      await page.fill('.task textarea.write', correct ? it.model : 'hello there');
    }
    await page.click('.task .btn:has-text("Check answer")');
    await page.waitForSelector('.feedback');
    if (shot) await page.screenshot({ path: OUT + shot + '-feedback.png', fullPage: true });
    return it;
  }

  // placement: 24 tasks, mixed right/wrong
  await page.goto(BASE + '/index.html#/placement');
  await page.waitForSelector('#go');
  await page.screenshot({ path: OUT + '03-placement-intro.png' });
  await page.click('#go');
  for (let i = 0; i < 24; i++) {
    const ok = [true, true, false, true, false, true][i % 6];
    await answerCurrent(ok, i === 0 ? '04-placement1' : (i === 2 ? '05-placement-wrong' : null));
    await page.click('.feedback .btn');
  }
  await page.waitForSelector('.levelbadge');
  await page.waitForTimeout(300);
  await noJunk(page,'06-placement-result'); await page.screenshot({ path: OUT + '06-placement-result.png', fullPage: true });

  // practice picker + session of 10 with all kinds
  await page.goto(BASE + '/index.html#/practice');
  await page.waitForSelector('.lvseg');
  for (const l of ['A2', 'B1', 'B2', 'C1']) {   // B1 only
    const on = await page.locator('.lvseg input[value="' + l + '"]').isChecked();
    if (on !== (l === 'B1')) await page.locator('.lvseg label', { hasText: new RegExp('^' + l + '$') }).click();
  }
  await page.waitForSelector('details.picker-group'); await page.evaluate(() => document.querySelectorAll('details.picker-group').forEach(d => { d.open = true; }));   // the areas start closed
  await page.waitForSelector('.chipsel');
  await page.locator('.chipsel label', { hasText: 'Present perfect' }).first().click();
  await page.evaluate(() => document.querySelectorAll('details.picker-group').forEach(d => { d.open = true; }));
  await page.locator('.chipsel label', { hasText: 'Past simple passive' }).first().click();
  await page.screenshot({ path: OUT + '07-picker.png', fullPage: true });
  await page.click('button.btn:text-is("Start")');
  const kinds = [];
  for (let i = 0; i < 10; i++) {
    const it = await answerCurrent(i % 3 !== 1, i === 3 ? '08-practice' : (i === 4 ? '09-practice-b' : null));
    kinds.push(it.kind + ':B' + it.bloom);
    await page.click('.feedback .btn');
  }
  console.log('practice kinds served:', kinds.join(' '));
  await page.waitForSelector('.big');
  await page.waitForSelector('.modal', { timeout: 5000 });
  const mtxt = await page.locator('.modal').innerText();
  if (!/Save your results with a free account/.test(mtxt) || !/Create free account/.test(mtxt) || !/I already have an account/.test(mtxt)) errors.push('guest invitation popup incomplete: ' + mtxt.slice(0, 80));
  await page.screenshot({ path: OUT + '10b-guest-invite.png' });
  await page.click('#later');
  await noJunk(page,'10-summary'); await page.screenshot({ path: OUT + '10-summary.png', fullPage: true });

  await page.goto(BASE + '/index.html#/home'); await page.waitForSelector('.card.focus'); await page.waitForTimeout(300);
  if (!(await page.locator('text=Create a free account to keep your results').count())) errors.push('guest banner missing on home');
  await noJunk(page,'11-home-active'); await page.screenshot({ path: OUT + '11-home-active.png', fullPage: true });
  await page.goto(BASE + '/index.html#/leaderboard'); await page.waitForSelector('text=Guests are not ranked'); await noJunk(page,'12-leaderboard'); await page.screenshot({ path: OUT + '12-leaderboard.png', fullPage: true });
  await page.goto(BASE + '/index.html#/profile'); await page.waitForSelector('#pn'); await noJunk(page,'13-profile'); await page.screenshot({ path: OUT + '13-profile.png', fullPage: true });

  // mobile
  const m = await browser.newContext({ viewport: { width: 390, height: 800 }, isMobile: true });
  const mp = await m.newPage();
  mp.on('pageerror', e => errors.push('mobile pageerror: ' + e.message));
  await mp.goto(BASE + '/index.html'); await mp.waitForSelector('.hero'); await mp.screenshot({ path: OUT + '14-mobile-welcome.png', fullPage: true });
  await mp.click('button[type=submit]'); await mp.waitForSelector('.hello h1'); const gname = await mp.locator('.hello h1').innerText(); if (!/^Welcome, Guest \d{4}$/.test(gname)) errors.push('anonymous guest name wrong: ' + gname); await mp.waitForTimeout(400);
  await mp.screenshot({ path: OUT + '15-mobile-home.png', fullPage: true });

  console.log(errors.length ? 'ERRORS:\n' + errors.join('\n') : 'no console or server errors');
  await browser.close();
})().catch(e => { console.error('FAILED', e); process.exit(1); });
