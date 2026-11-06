const { chromium } = require('playwright');
const BASE = 'http://127.0.0.1:8099';
const OUT = __dirname + '/shots/';
const errors = [];
let uidSeq = 5000 + Math.floor(Math.random() * 90000);

async function newLearner(browser, name, opts) {
  const ctx = await browser.newContext({ viewport: (opts && opts.viewport) || { width: 1100, height: 900 } });
  const page = await ctx.newPage();
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/403|401/.test(m.text())) errors.push('console: ' + m.text()); });
  await page.goto(BASE + '/sso-demo.php?uid=' + (uidSeq++) + '&name=' + encodeURIComponent(name));
  await page.waitForSelector('#fn'); await page.click('button[type=submit]'); await page.waitForSelector('.hello h1');
  return { ctx, page };
}
const me = page => page.evaluate(() => fetch('api.php?r=me').then(r => r.json()).then(j => j.user));

(async () => {
  const browser = await chromium.launch();

  // 1. no invitation, no study card: everyone is in the study; Profile → Your data → Research explains it (teacher, 5 November)
  let { ctx, page } = await newLearner(browser, 'Ada Study');
  if (await page.locator('text=learning study').count()) errors.push('there should be no study invitation on Home');
  const dashLinks = await page.locator('a:has-text("My dashboard")').evaluateAll(a => a.map(x => [x.getAttribute('target'), x.getAttribute('rel')]));
  if (dashLinks.length < 1 || dashLinks.some(d => d[0] !== '_blank' || !/noopener/.test(d[1] || ''))) errors.push('"My dashboard" links should open in a new tab: ' + JSON.stringify(dashLinks));
  let u = await me(page);
  if (u.research !== 0 || Object.keys(u.cond).length) errors.push('a new learner should be in the study without conditions: ' + JSON.stringify(u));
  await page.goto(BASE + '/#/profile'); await page.waitForSelector('h2:has-text("Your data")');
  if (await page.locator('h2:has-text("Learning study")').count()) errors.push('the old study card should be gone');
  if (!(await page.locator('.study-link:has-text("Research")').count())) errors.push('Research link missing next to the privacy policy');
  await page.click('.study-link'); await page.waitForSelector('.modal h2:has-text("Research")');
  const txt = await page.locator('.modal').innerText();
  if (!/University of Latvia/.test(txt) || !/anonymous/.test(txt) || /18/.test(txt)) errors.push('Research text: ' + txt);
  await page.screenshot({ path: OUT + '31-research-en.png' });
  await page.click('.modal button:has-text("I do not agree to take part in the study")'); await page.waitForSelector('.toast');
  u = await me(page);
  if (u.research !== 2) errors.push('"I do not agree" did not stick: ' + JSON.stringify(u));
  await page.click('.study-link'); await page.waitForSelector('.modal button:has-text("Take part again")');
  await page.click('.modal button:has-text("Take part again")'); await page.waitForSelector('.toast');
  u = await me(page);
  if (u.research !== 1) errors.push('"Take part again" did not stick: ' + JSON.stringify(u));
  if (!(await page.locator('nav.nav a[href="#/leaderboard"]').count()) || !(await page.locator('.chip-top[title="Daily streak"]').count())) errors.push('everyone sees the streak and the leaderboard');
  await ctx.close();

  // 3. Latvian wording, on a phone
  const lv = await newLearner(browser, 'Anna Latviete', { viewport: { width: 390, height: 800 } });
  await lv.page.evaluate(() => fetch('api.php?r=account/profile', { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify({ lang: 'lv' }) }));
  await lv.page.goto(BASE + '/#/profile'); await lv.page.reload(); await lv.page.waitForSelector('.study-link');
  await lv.page.click('.study-link'); await lv.page.waitForSelector('.modal h2:has-text("Pētījums")');
  if (!(await lv.page.locator('.modal button:has-text("Nepiekrītu dalībai pētījumā")').count())) errors.push('Latvian button missing');
  await lv.page.screenshot({ path: OUT + '34-research-lv-phone.png' });
  const overflow = await lv.page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  if (overflow) errors.push('the Research window overflows the phone width');
  await lv.ctx.close();

  // 4. a guest has no Research link (a guest is not in the study)
  const gc = await browser.newContext(); const gp = await gc.newPage();
  await gp.goto(BASE + '/'); await gp.waitForSelector('#nick'); await gp.waitForTimeout(1400); await gp.click('button:has-text("Continue as guest")'); await gp.waitForSelector('.hello h1');
  await gp.goto(BASE + '/#/profile'); await gp.waitForSelector('h2:has-text("Profile")');
  if (await gp.locator('.study-link').count()) errors.push('guest should not see the Research link');
  await gc.close();

  // 5. the teacher's card
  const tc = await browser.newContext({ viewport: { width: 1100, height: 900 } }); const tp = await tc.newPage();
  tp.on('pageerror', e => errors.push('pageerror: ' + e.message));
  await tp.goto(BASE + '/sso-demo.php?teacher=1&uid=1&name=Inga%20Teacher'); await tp.waitForSelector('table');
  await tp.waitForSelector('.label:has-text("Learning study")');
  const links = await tp.locator('a[href*="teacher/research-export"]').evaluateAll(a => a.map(x => x.getAttribute('href')));
  if (links.length !== 4 || !links.some(l => /file=people/.test(l)) || !links.some(l => /file=readme/.test(l))) errors.push('teacher download links wrong: ' + links.join(', '));
  const cardText = await tp.locator('.card', { hasText: 'Learning study' }).first().innerText();
  if (!/registered learners in the study, \d+ said no/.test(cardText) || /see it/.test(cardText)) errors.push('teacher card text: ' + cardText);
  await tp.screenshot({ path: OUT + '35-teacher-study.png', fullPage: true });
  // downloads work from the page
  const [dl] = await Promise.all([tp.waitForEvent('download'), tp.click('a:has-text("People (CSV)")')]);
  if (!/^research-people-\d{4}-\d{2}-\d{2}\.csv$/.test(dl.suggestedFilename())) errors.push('download name: ' + dl.suggestedFilename());
  await tc.close();

  await browser.close();
  if (errors.length) { console.log('FAILED:\n' + errors.join('\n')); process.exit(1); }
  console.log('STUDY UI OK');
})();
