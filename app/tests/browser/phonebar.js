const { chromium, devices } = require('playwright');
(async () => { const b = await chromium.launch(); const c = await b.newContext({ ...devices['iPhone 13'] }); const p = await c.newPage();
 await p.goto('http://127.0.0.1:8099/index.html'); await p.fill('#nick', 'Bar test'); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
 const over = await p.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
 const bar = await p.evaluate(() => { const t = document.querySelector('.topbar-in'); return [t.scrollWidth, t.clientWidth]; });
 console.log('page scrolls sideways:', over, '| top bar content/visible width:', bar.join('/'));
 await p.screenshot({ path: __dirname + '/shots/61-phone-home.png' }); await b.close(); })();
