const { chromium } = require('playwright');
const BASE = 'http://127.0.0.1:8099', OUT = __dirname + '/shots/';
const errors = [];
(async () => {
  const browser = await chromium.launch();
  for (const scheme of ['light', 'dark']) {
    const ctx = await browser.newContext({ viewport: { width: 1200, height: 900 }, colorScheme: scheme });
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(scheme + ' pageerror: ' + e.message));
    await page.goto(BASE + '/sso-demo.php?uid=' + (7000 + Math.floor(Math.random() * 9000)) + '&name=Hover%20Tester');
    await page.waitForSelector('#fn'); await page.click('button[type=submit]'); await page.waitForSelector('.hello h1');
    // ask not about the study here
    const card = page.locator('.card.focus');
    const before = await card.evaluate(e => { const c = getComputedStyle(e); return [c.boxShadow, c.transform, c.borderColor]; });
    await card.hover(); await page.waitForTimeout(400);
    const after = await card.evaluate(e => { const c = getComputedStyle(e); return [c.boxShadow, c.transform, c.borderColor]; });
    if (before[0] === after[0] || after[1] === 'none') errors.push(scheme + ': option card does not react on hover ' + JSON.stringify([before, after]));
    await page.screenshot({ path: OUT + '40-hover-card-' + scheme + '.png', clip: { x: 0, y: 0, width: 1200, height: 520 } });
    const fold = page.locator('details.card.fold').first();
    const sb = await fold.evaluate(e => getComputedStyle(e).borderColor); await fold.hover(); await page.waitForTimeout(350);
    const sa = await fold.evaluate(e => getComputedStyle(e).borderColor);
    if (sb === sa) errors.push(scheme + ': folded card border does not change on hover');
    const btn = page.locator('.card.focus .btn:not(.ghost)').first();
    const bb = await btn.evaluate(e => getComputedStyle(e).boxShadow); await btn.hover(); await page.waitForTimeout(350);
    const ba = await btn.evaluate(e => { const c = getComputedStyle(e); return [c.boxShadow, c.transform]; });
    if (ba[0] === bb || ba[1] === 'none') errors.push(scheme + ': primary button does not react on hover ' + JSON.stringify([bb, ba]));
    await page.screenshot({ path: OUT + '41-hover-button-' + scheme + '.png', clip: { x: 0, y: 150, width: 1200, height: 420 } });
    const pulse = await page.locator('.btn.pulse').count();
    const anim = pulse ? await page.locator('.btn.pulse').first().evaluate(e => getComputedStyle(e).animationName + ' x' + getComputedStyle(e).animationIterationCount) : 'none';
    if (pulse !== 1 || !/nudge x2/.test(anim)) errors.push(scheme + ': exactly one button should pulse twice: ' + pulse + ' ' + anim);
    // no sideways scroll caused by the lift or glow
    if (await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth)) errors.push(scheme + ': sideways scroll');
    // skill card
    await page.locator('details.card.fold > summary:has-text("Your topics")').click(); await page.waitForTimeout(150);
    const sk = page.locator('.skill').first(); await sk.scrollIntoViewIfNeeded(); await sk.hover(); await page.waitForTimeout(350);
    const st = await sk.evaluate(e => getComputedStyle(e).transform); if (st === 'none') errors.push(scheme + ': skill card does not lift');
    await ctx.close();
  }
  // reduced motion: nothing animates or lifts
  const rctx = await browser.newContext({ viewport: { width: 1200, height: 900 }, reducedMotion: 'reduce' }); const rp = await rctx.newPage();
  await rp.goto(BASE + '/sso-demo.php?uid=' + (7000 + Math.floor(Math.random() * 9000)) + '&name=Calm%20Tester'); await rp.waitForSelector('#fn'); await rp.click('button[type=submit]'); await rp.waitForSelector('.hello h1');
  const ra = await rp.locator('.btn.pulse').first().evaluate(e => getComputedStyle(e).animationName);
  if (ra !== 'none') errors.push('reduced motion: the pulse still runs: ' + ra);
  await rctx.close();
  // phone (no hover): the pulse still runs
  const pctx = await browser.newContext({ viewport: { width: 390, height: 800 }, hasTouch: true, isMobile: true }); const pp = await pctx.newPage();
  await pp.goto(BASE + '/sso-demo.php?uid=' + (7000 + Math.floor(Math.random() * 9000)) + '&name=Phone%20Tester'); await pp.waitForSelector('#fn'); await pp.click('button[type=submit]'); await pp.waitForSelector('.hello h1');
  if ((await pp.locator('.btn.pulse').count()) !== 1) errors.push('phone: the pulse is missing');
  if (await pp.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth)) errors.push('phone: sideways scroll');
  await pctx.close();
  await browser.close();
  if (errors.length) { console.log('FAILED:\n' + errors.join('\n')); process.exit(1); }
  console.log('HOVER OK');
})();
