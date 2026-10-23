const { chromium } = require('playwright');
const BASE = 'http://127.0.0.1:8099';
(async () => {
  const b = await chromium.launch(); const bad = [];
  for (const kind of ['guest', 'registered']) {
    for (const w of [820, 900, 960, 1024, 1100, 1180, 1280, 1440]) {
      const ctx = await b.newContext({ viewport: { width: w, height: 800 } }); const p = await ctx.newPage();
      if (kind === 'guest') { await p.goto(BASE + '/index.html'); await p.waitForSelector('#nick'); await p.waitForTimeout(1400); await p.click('button[type=submit]'); }
      else { await p.goto(BASE + '/sso-demo.php?uid=' + (3000 + w) + '&name=Top%20Bar%20' + w); await p.waitForSelector('#fn'); await p.click('button[type=submit]'); }
      await p.waitForSelector('.hello h1'); await p.waitForTimeout(200);
      const m = await p.evaluate(() => { const t = document.querySelector('.topbar-in'); return { sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth, tin: t.scrollWidth, tcw: t.clientWidth }; });
      const over = m.sw > m.cw || m.tin > m.tcw + 1;
      console.log((over ? 'OVERFLOW ' : 'ok       ') + kind.padEnd(10) + w + '  page ' + m.sw + '/' + m.cw + '  bar ' + m.tin + '/' + m.tcw);
      if (over) bad.push(kind + ' ' + w);
      await ctx.close();
    }
  }
  await b.close(); console.log(bad.length ? '\nFAILED: ' + bad.join(', ') : '\nALL OK'); process.exit(bad.length ? 1 : 0);
})();
