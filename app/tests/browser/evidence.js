// The teacher's "Learning evidence" page: reachable from Students, numbers only, sounds to hear; not for learners.
const { chromium } = require('playwright');
const BASE = 'http://127.0.0.1:8099';
(async () => {
  const b = await chromium.launch(); let ok = true; const errors = [];
  const check = (n, c) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n); };
  const ctx = await b.newContext({ viewport: { width: 1100, height: 900 } }); const page = await ctx.newPage();
  page.on('pageerror', e => errors.push(e.message));
  await page.goto(BASE + '/sso-demo.php?teacher=1&uid=1&name=Inga%20Teacher'); await page.waitForSelector('table');
  check('the Students page links to the evidence', (await page.locator('a:has-text("Learning evidence")').count()) === 1);
  check('the top bar has no new tab for it', (await page.locator('.nav a:has-text("Evidence")').count()) === 0);
  await page.click('a:has-text("Learning evidence")'); await page.waitForSelector('h1:has-text("Learning evidence")');
  check('it shows the three blocks', (await page.locator('h2:has-text("A missed question, asked again")').count()) === 1 && (await page.locator('h2:has-text("Mistakes")').count()) === 1 && (await page.locator('h2:has-text("The sounds")').count()) === 1);
  check('with no data it says there is too little so far', (await page.locator('text=Too few so far').count()) === 1);
  check('five sound buttons', (await page.locator('button:has-text("Locked in"), button:has-text("Tricky"), button:has-text("Fixed"), button:has-text("Wrong"), button:has-text("Right")').count()) === 5);
  await page.evaluate(() => { window.__played = []; });
  await page.click('button:has-text("Locked in")');   // must not throw even where audio is unavailable
  check('a sound button works without turning learners\' sound on', !(await page.evaluate(() => localStorage.getItem('ef_sound') === '1')));
  // a learner is sent home
  const lc = await b.newContext(); const lp = await lc.newPage();
  await lp.goto(BASE + '/sso-demo.php?uid=' + (Math.floor(Math.random() * 900000) + 3000) + '&name=Lena'); await lp.waitForSelector('#fn'); await lp.click('button[type=submit]'); await lp.waitForSelector('.hello h1');
  await lp.goto(BASE + '/#/evidence'); await lp.waitForTimeout(800);
  check('a learner cannot open it', (await lp.locator('h1:has-text("Learning evidence")').count()) === 0);
  check('no page errors', errors.length === 0 && true);
  console.log(ok ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
