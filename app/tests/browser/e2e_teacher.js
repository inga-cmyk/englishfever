const { chromium } = require('playwright');
const BASE = 'http://127.0.0.1:8099';
const OUT = __dirname + '/shots/';
(async () => {
  const browser = await chromium.launch();
  const errors = [];
  const ctx = await browser.newContext({ viewport: { width: 1100, height: 900 } });
  const page = await ctx.newPage();
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  // two registered learners and one guest exist before the teacher looks
  for (const nm of ['Rita Reg', 'Sam Student']) {
    const lc = await browser.newContext(); const lp = await lc.newPage();
    await lp.goto(BASE + '/sso-demo.php?uid=' + (Math.floor(Math.random() * 900000) + 2000) + '&name=' + encodeURIComponent(nm));
    await lp.waitForSelector('#fn'); await lp.click('button[type=submit]'); await lp.waitForSelector('.hello h1'); await lc.close();
  }
  await page.goto(BASE + '/sso-demo.php?teacher=1&uid=1&name=Inga%20Teacher');
  await page.waitForSelector('table');
  // default view: nobody is "mine" yet, so the list starts on Registered
  await page.waitForSelector('[role=tab][aria-selected=true]');
  const selected = await page.locator('[role=tab][aria-selected=true]').innerText();
  if (!/^Registered/.test(selected)) errors.push('default view should be Registered, got: ' + selected);
  if (await page.locator('.pill', { hasText: 'guest' }).count()) errors.push('guests should not show under Registered');
  const tabsText = await page.locator('[role=tablist]').innerText();
  if (!/My students \(0\)/.test(tabsText) || !/Everyone \(\d+\)/.test(tabsText)) errors.push('tab counts missing: ' + tabsText);
  await page.click('[role=tab]:has-text("Everyone")');
  if (!(await page.locator('.pill', { hasText: 'guest' }).count())) errors.push('guest pill missing under Everyone');
  if (!(await page.locator('td.name .small', { hasText: 'first seen' }).count())) errors.push('"first seen" missing for guests');
  await page.click('[role=tab]:has-text("My students")');
  if (!/No students here yet/.test(await page.locator('td.empty').innerText())) errors.push('empty message for My students missing');
  await page.click('[role=tab]:has-text("Registered")');
  const href = await page.locator('a:has-text("Export answers")').getAttribute('href');
  if (!/view=registered/.test(href)) errors.push('export link does not follow the view: ' + href);
  await page.waitForTimeout(300);
  await page.screenshot({ path: OUT + '20-teacher-list.png', fullPage: true });
  // add the first registered learner to my students from their page
  await page.locator('td.name a').first().click();
  await page.waitForSelector('.hello h1');
  await page.click('button:has-text("Add to my students")');
  await page.waitForSelector('button:has-text("Remove from my students")');
  await page.click('a:has-text("All students")');
  await page.waitForSelector('table');
  if (!/^Registered/.test(await page.locator('[role=tab][aria-selected=true]').innerText())) errors.push('the last chosen view (Registered) should be remembered');
  await page.click('[role=tab]:has-text("My students")');
  if (!(await page.locator('[role=tab]:has-text("My students (1)")').count())) errors.push('My students should now count 1');
  if ((await page.locator('tbody tr').count()) !== 1) errors.push('My students should list exactly one learner');
  await page.reload(); await page.waitForSelector('table');
  if (!/^My students \(1\)/.test(await page.locator('[role=tab][aria-selected=true]').innerText())) errors.push('choice not remembered after reload');
  await page.screenshot({ path: OUT + '20b-teacher-mine.png', fullPage: true });
  await page.locator('td.name a').first().click();
  await page.waitForSelector('.hello h1'); await page.waitForTimeout(400);
  await page.screenshot({ path: OUT + '21-teacher-student.png', fullPage: true });
  // dark mode + mobile
  const dctx = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, colorScheme: 'dark' });
  const dp = await dctx.newPage();
  dp.on('pageerror', e => errors.push('dark pageerror: ' + e.message));
  await dp.goto(BASE + '/sso-demo.php?uid=' + (Math.floor(Math.random()*900000)+1000) + '&name=Dark%20Tester');
  await dp.waitForSelector('#fn'); const pre = await dp.inputValue('#fn'); if (pre !== 'Dark') errors.push('name not prefilled with the first name: ' + pre); const heading = await dp.locator('h1').innerText(); if (!/How should we show your name/.test(heading)) errors.push('nickname screen heading wrong: ' + heading); await dp.screenshot({ path: OUT + '24-dark-name-screen.png' }); await dp.click('button[type=submit]');
  await dp.waitForSelector('.hello h1'); await dp.waitForTimeout(400);
  await dp.screenshot({ path: OUT + '22-dark-mobile-home.png', fullPage: false });
  await dp.goto(BASE + '/index.html#/practice'); await dp.waitForSelector('details.picker-group'); await dp.locator('details.picker-group summary').first().click(); await dp.waitForSelector('.chipsel'); await dp.screenshot({ path: OUT + '23-dark-mobile-picker.png', fullPage: false });
  console.log(errors.length ? 'ERRORS:\n' + errors.join('\n') : 'no errors');
  await browser.close();
})().catch(e => { console.error('FAILED', e); process.exit(1); });
