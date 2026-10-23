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

  // 1. the invitation: later, then yes
  let { ctx, page } = await newLearner(browser, 'Ada Study');
  const cardCount = () => page.locator('.card h2', { hasText: 'Help with a learning study?' }).count();
  if (!(await cardCount())) errors.push('invitation missing on Home');
  const dashLinks = await page.locator('a:has-text("My dashboard")').evaluateAll(a => a.map(x => [x.getAttribute('target'), x.getAttribute('rel')]));
  if (dashLinks.length !== 2 || dashLinks.some(d => d[0] !== '_blank' || !/noopener/.test(d[1] || ''))) errors.push('"My dashboard" links should open in a new tab: ' + JSON.stringify(dashLinks));
  await page.screenshot({ path: OUT + '30-invite.png', fullPage: true });
  await page.click('button:has-text("Ask me later")');
  if (await cardCount()) errors.push('"Ask me later" should hide the card');
  await page.reload(); await page.waitForSelector('.hello h1');
  if (await cardCount()) errors.push('"Ask me later" should keep it hidden after reload');
  await page.evaluate(() => localStorage.removeItem('ef_study_later')); await page.reload(); await page.waitForSelector('.hello h1');
  if (!(await cardCount())) errors.push('invitation should come back when the wait is cleared');
  await page.click('button:has-text("Yes, I take part")');
  await page.waitForFunction(() => !document.body.innerText.includes('Help with a learning study?'));
  let u = await me(page);
  if (u.research !== 1) errors.push('join did not stick: ' + JSON.stringify(u));
  await page.goto(BASE + '/#/profile'); await page.waitForSelector('h2:has-text("Learning study")');
  if (!(await page.locator('text=You are taking part in the learning study').count())) errors.push('profile should say taking part');
  await page.screenshot({ path: OUT + '31-profile-joined.png', fullPage: true });
  await page.click('button:has-text("Leave the study")');
  await page.waitForSelector('text=You are not taking part.');
  u = await me(page);
  if (u.research !== 2 || Object.keys(u.cond).length) errors.push('leave did not work: ' + JSON.stringify(u));
  if (!(await page.locator('button:has-text("Take part")').count())) errors.push('"Take part" button missing after leaving');
  await page.goto(BASE + '/#/home'); await page.waitForSelector('.hello h1');
  if (await cardCount()) errors.push('someone who said no/left must not be asked again on Home');
  await ctx.close();

  // 2. four learners join: the features follow the condition (blocks of four: two hidden for each factor)
  const seen = { streakOff: 0, boardOff: 0, streakOn: 0, boardOn: 0 };
  for (let i = 0; i < 4; i++) {
    const L = await newLearner(browser, 'Cond Learner ' + i); const p = L.page;
    await p.click('button:has-text("Yes, I take part")');
    await p.waitForFunction(() => !document.body.innerText.includes('Help with a learning study?'));
    const c = (await me(p)).cond;
    await p.goto(BASE + '/#/home'); await p.waitForSelector('.hello h1'); await p.waitForTimeout(250);
    const chip = await p.locator('.chip-top[title="Daily streak"]').count();
    const stats = await p.locator('.grid .stat, .grid > .card.stat').count();
    const homeText = await p.locator('main, #app').innerText();
    const flames = /streak/i.test(homeText);
    const tab = await p.locator('nav.nav a[href="#/leaderboard"]').count();
    if (c.streak === 'off') { seen.streakOff++; if (chip || flames) errors.push('streak off: counter still visible (' + c.streak + ')'); }
    else { seen.streakOn++; if (!chip) errors.push('streak on: counter missing'); }
    if (c.leaderboard === 'off') {
      seen.boardOff++;
      if (tab) errors.push('leaderboard off: tab still there');
      await p.goto(BASE + '/#/leaderboard'); await p.waitForTimeout(400);
      if (!/#\/home/.test(await p.evaluate(() => location.hash))) errors.push('leaderboard off: should land on Home, got ' + await p.evaluate(() => location.hash));
      await p.goto(BASE + '/#/profile'); await p.waitForSelector('h2:has-text("Profile")');
      if (await p.locator('text=Show me on the leaderboard').count()) errors.push('leaderboard off: profile still offers the leaderboard setting');
    } else {
      seen.boardOn++;
      if (!tab) errors.push('leaderboard on: tab missing');
      await p.goto(BASE + '/#/profile'); await p.waitForSelector('h2:has-text("Profile")');
      if (!(await p.locator('text=Show me on the leaderboard').count())) errors.push('leaderboard on: profile setting missing');
    }
    if (i === 0) await p.screenshot({ path: OUT + '32-cond-' + c.streak + '-' + c.leaderboard + '.png', fullPage: true });
    if (c.streak === 'off' && !L.shot) { L.shot = true; await p.goto(BASE + '/#/home'); await p.waitForSelector('.hello h1'); await p.waitForTimeout(250); await p.screenshot({ path: OUT + '33-streak-off-home.png', fullPage: true }); }
    // leaving puts everything back
    await p.goto(BASE + '/#/profile'); await p.waitForSelector('button:has-text("Leave the study")');
    await p.click('button:has-text("Leave the study")'); await p.waitForSelector('text=You are not taking part.');
    await p.waitForTimeout(250);
    if (!(await p.locator('.chip-top[title="Daily streak"]').count())) errors.push('after leaving the streak counter should be back');
    if (!(await p.locator('nav.nav a[href="#/leaderboard"]').count())) errors.push('after leaving the leaderboard tab should be back');
    await L.ctx.close();
  }
  // the first learner (who left again) used up one place in the sequence, so these four see both arms of each factor at least once
  if (!seen.streakOff || !seen.boardOff || !seen.streakOn || !seen.boardOn) errors.push('expected both arms of each factor, got ' + JSON.stringify(seen));

  // 3. Latvian wording, on a phone
  const lv = await newLearner(browser, 'Anna Latviete', { viewport: { width: 390, height: 800 } });
  await lv.page.evaluate(() => fetch('api.php?r=account/profile', { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify({ lang: 'lv' }) }));
  await lv.page.goto(BASE + '/#/profile'); await lv.page.reload(); await lv.page.goto(BASE + '/#/home'); await lv.page.waitForSelector('.hello h1');
  if (!(await lv.page.locator('h2', { hasText: 'Palīdziet pētījumā?' }).count())) errors.push('Latvian invitation missing');
  await lv.page.screenshot({ path: OUT + '34-invite-lv-phone.png', fullPage: true });
  const overflow = await lv.page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  if (overflow) errors.push('invitation overflows the phone width');
  await lv.page.click('button:has-text("Nē, paldies")');
  await lv.ctx.close();

  // 4. a guest is never asked
  const gc = await browser.newContext(); const gp = await gc.newPage();
  await gp.goto(BASE + '/'); await gp.waitForSelector('#nick'); await gp.waitForTimeout(1400); await gp.click('button:has-text("Continue as guest")'); await gp.waitForSelector('.hello h1');
  if (await gp.locator('text=learning study').count()) errors.push('guest should not see the study invitation');
  await gp.goto(BASE + '/#/profile'); await gp.waitForSelector('h2:has-text("Profile")');
  if (await gp.locator('h2:has-text("Learning study")').count()) errors.push('guest should not see the study card on Profile');
  await gc.close();

  // 5. the teacher's card
  const tc = await browser.newContext({ viewport: { width: 1100, height: 900 } }); const tp = await tc.newPage();
  tp.on('pageerror', e => errors.push('pageerror: ' + e.message));
  await tp.goto(BASE + '/sso-demo.php?teacher=1&uid=1&name=Inga%20Teacher'); await tp.waitForSelector('table');
  await tp.waitForSelector('.label:has-text("Learning study")');
  const links = await tp.locator('a[href*="teacher/research-export"]').evaluateAll(a => a.map(x => x.getAttribute('href')));
  if (links.length !== 4 || !links.some(l => /file=people/.test(l)) || !links.some(l => /file=readme/.test(l))) errors.push('teacher download links wrong: ' + links.join(', '));
  const cardText = await tp.locator('.card', { hasText: 'Learning study' }).first().innerText();
  if (!/take part/.test(cardText) || !/Daily streak counter: \d+ see it, \d+ do not/.test(cardText) || !/Leaderboard: \d+ see it, \d+ do not/.test(cardText)) errors.push('teacher card text: ' + cardText);
  await tp.screenshot({ path: OUT + '35-teacher-study.png', fullPage: true });
  // downloads work from the page
  const [dl] = await Promise.all([tp.waitForEvent('download'), tp.click('a:has-text("People (CSV)")')]);
  if (!/^research-people-\d{4}-\d{2}-\d{2}\.csv$/.test(dl.suggestedFilename())) errors.push('download name: ' + dl.suggestedFilename());
  await tc.close();

  await browser.close();
  if (errors.length) { console.log('FAILED:\n' + errors.join('\n')); process.exit(1); }
  console.log('STUDY UI OK');
})();
