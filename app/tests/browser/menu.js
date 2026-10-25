const { chromium, devices } = require('playwright');
const fs = require('fs');
const ITEMS = Object.fromEntries(JSON.parse(fs.readFileSync('/home/user/englishfever/app/content/items.json')).map(i => [i.id, i]));
const BASE = 'http://127.0.0.1:8099';
const OUT = __dirname + '/shots/';
(async () => {
  const b = await chromium.launch(); let ok = true; const errs = [];
  const check = (n, c, x) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : ' -> ' + JSON.stringify(x))); };
  const post = (p, r, d) => p.evaluate(async ([r, d]) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json(), [r, d]);
  async function guest(opts, name) {
    const ctx = await b.newContext(opts); const p = await ctx.newPage();
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await p.goto(BASE + '/index.html'); await p.waitForSelector('#nick'); if (name) await p.fill('#nick', name); await p.waitForTimeout(1400); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
    return { ctx, p };
  }

  // ───── guest: home cards, no dashboard button ─────
  {
    const { ctx, p } = await guest({ viewport: { width: 1200, height: 900 } });
    await p.waitForTimeout(300);
    const txt = await p.locator('main').innerText();
    check('a new learner\'s Home is quiet: one main card (Find my level), two small links, no option cards or stat tiles', (await p.locator('.card.focus').count()) === 1 && (await p.locator('.card.focus .btn').count()) === 1 && /Find my level/.test(await p.locator('.card.focus').innerText()) && (await p.locator('.homelinks a').allInnerTexts()).join('|') === 'Choose topics|Rule cards' && !/option [123]/i.test(txt) && (await p.locator('.stat').count()) === 0, [await p.locator('.card.focus').innerText(), await p.locator('.homelinks a').allInnerTexts()]);
    check('the topics and progress are folded away by default', (await p.locator('details.card.fold[open]').count()) === 0 && (await p.locator('details.card.fold > summary .h3').allInnerTexts()).join('|') === 'Your topics', await p.locator('details.card.fold > summary .h3').allInnerTexts());
    await p.locator('details.card.fold > summary:has-text("Your topics")').click(); await p.waitForTimeout(150);
    check('a guest sees the website link, not "My dashboard"', (await p.locator('.sitelink').textContent()) === 'englishfever.com ↗' && (await p.locator('a:has-text("My dashboard")').count()) === 0);
    check('"Your topics" is grouped by area (fold-away sections)', (await p.locator('details.area-fold > summary .h3').allInnerTexts()).join('|').toLowerCase() === 'active tenses|passive tenses|conditionals|reported speech|questions inside sentences', await p.locator('details.area-fold > summary .h3').allInnerTexts());
    await p.screenshot({ path: OUT + '95-home-areas.png', fullPage: true });

    // picker
    await p.goto(BASE + '/index.html#/practice'); await p.waitForSelector('.picker-group');
    const M = await (await p.request.get(BASE + '/api.php?r=meta')).json();
    const has = (s, lvls) => lvls.some(l => ((M.skill_counts[s.id] || {})[l] || 0) > 0);
    const topicsAt = lvls => M.skills.filter(s => has(s, lvls)).length;
    check('the picker shows only the levels that have questions (A2 to C1); A1 and C2 are not shown', (await p.locator('.lvseg label').count()) === 4 && (await p.locator('.lvseg input:disabled').count()) === 0 && (await p.locator('.lvseg input[value=A1]').count()) === 0 && (await p.locator('.lvseg input[value=C2]').count()) === 0);
    check('only one level is chosen to start with, and it is A2 for a new learner', (await p.locator('.lvseg input:checked').count()) === 1 && (await p.locator('.lvseg input[value=A2]').isChecked()));
    check('all areas start closed', (await p.locator('details.picker-group[open]').count()) === 0);
    await p.evaluate(() => document.querySelectorAll('details.picker-group').forEach(d => { d.open = true; }));
    check('at A2 only the topics that have A2 questions are listed (' + topicsAt(['A2']) + ')', (await p.locator('.chipsel label').count()) === topicsAt(['A2']), await p.locator('.chipsel label').count());
    await p.locator('.lvseg label', { hasText: /^B1$/ }).click(); await p.waitForTimeout(100);
    await p.evaluate(() => document.querySelectorAll('details.picker-group').forEach(d => { d.open = true; }));
    check('pressing B1 adds the B1 topics (' + topicsAt(['A2', 'B1']) + ' in all)', (await p.locator('.chipsel label').count()) === topicsAt(['A2', 'B1']), await p.locator('.chipsel label').count());
    await p.locator('.lvseg label', { hasText: /^B1$/ }).click(); await p.waitForTimeout(100);
    check('Surprise me is on the Practice page too', (await p.locator('button:has-text("Surprise me")').count()) === 1);
    const cond = p.locator('details.picker-group', { hasText: 'Conditionals' });
    await cond.evaluate(e => { e.open = true; });
    await cond.locator('.chipsel label', { hasText: 'First conditional' }).click(); await p.waitForTimeout(100);
    check('ticking a topic shows the count', (await p.locator('.chipsel input:checked').count()) === 1 && /1 chosen/.test(await p.locator('summary:has-text("Conditionals")').innerText()));
    await p.locator('details.picker-group', { hasText: 'Active tenses' }).evaluate(e => { e.open = false; });
    await p.locator('details.picker-group summary:has-text("Active tenses")').click();
    check('an area can be opened', await p.locator('details.picker-group', { hasText: 'Active tenses' }).evaluate(e => e.open));
    await p.locator('details.picker-group summary:has-text("Active tenses")').click();
    check('and closed again', !(await p.locator('details.picker-group', { hasText: 'Active tenses' }).evaluate(e => e.open)));
    await p.screenshot({ path: OUT + '96-picker.png', fullPage: true });
    await p.click('button.btn:text-is("Start")'); await p.waitForSelector('.task');
    const label = await p.locator('.task .pill.dark').innerText();
    check('practice starts with a conditional topic', /conditional|Mixed|Advanced/i.test(label), label);

    // surprise me from the home card
    await p.goto(BASE + '/index.html#/home'); await p.waitForSelector('.hello h1'); await p.waitForTimeout(300);
    check('with a session left open, Home offers to continue it (and nothing else to start)', /Continue where you stopped/.test(await p.locator('.card.focus').innerText()) && (await p.locator('.card.focus button:has-text("Continue")').count()) === 1, await p.locator('.card.focus').innerText());
    const rs = await p.evaluate(async () => (await (await fetch('api.php?r=session%2Fresume')).json()).resume);
    const it0 = ITEMS[rs.item.id]; const a0 = it0.kind === 'mcq' ? it0.correct : (it0.kind === 'gap' ? it0.answers.map(a => a[0]) : (it0.answers ? it0.answers[0][0] : 'x'));
    await post(p, 'session/answer', { session_id: rs.session.id, item_id: rs.item.id, answer: a0, time_ms: 2000 });   // one answer: now Home offers "Practise now"
    await post(p, 'session/quit', { session_id: rs.session.id });
    await p.reload(); await p.waitForSelector('.hello h1'); await p.waitForTimeout(300);
    await p.click('.card.focus button:has-text("Practise now")'); await p.waitForSelector('.task');
    check('Surprise me starts a session without a quick check', /Practice · Question 1 of 12/.test(await p.locator('.sess-top').innerText()), await p.locator('.sess-top').innerText());

    // placement sizes
    await p.goto(BASE + '/index.html#/placement'); await p.waitForSelector('.sizes');
    check('the placement offers Quick, Medium and Full', (await p.locator('.size').count()) === 3 && /12 questions/.test(await p.locator('.sizes').innerText()) && /40 questions/.test(await p.locator('.sizes').innerText()));
    check('Medium (24) is chosen by default', await p.locator('input[name=sz][value="24"]').isChecked());
    await p.locator('.size', { hasText: 'Quick' }).click(); await p.screenshot({ path: OUT + '97-placement-sizes.png' });
    await p.click('#go'); await p.waitForSelector('.task');
    check('Quick starts a 12-question test', /Question 1 of 12/.test(await p.locator('.sess-top').innerText()));
    await ctx.close();
  }

  // ───── registered learner: dashboard link ─────
  {
    const ctx = await b.newContext({ viewport: { width: 1200, height: 900 } }); const p = await ctx.newPage();
    p.on('pageerror', e => errs.push(e.message));
    await p.goto(BASE + '/sso-demo.php?uid=' + (Math.floor(Math.random() * 900000) + 3000) + '&name=Dash%20Board'); await p.waitForSelector('#fn'); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1'); await p.waitForTimeout(300);
    check('a registered learner has "My dashboard" in the top bar', (await p.locator('.sitelink').innerText()) === 'My dashboard ↗' && /dashboard-demo/.test(await p.locator('.sitelink').getAttribute('href')));
    check('...and in the Home links (shown on phones only: on a computer the top bar has it)', (await p.locator('.homelinks a:has-text("My dashboard")').count()) === 1 && !(await p.locator('.homelinks a:has-text("My dashboard")').isVisible()) && (await p.locator('.sitelink').isVisible()));
    await p.screenshot({ path: OUT + '98-home-dashboard.png' });
    const m = await ctx.browser().newContext({ ...devices['iPhone 13'] }); const mp = await m.newPage();
    await mp.goto(BASE + '/sso-demo.php?uid=' + (Math.floor(Math.random() * 900000) + 3000) + '&name=Phone%20Dash'); await mp.waitForSelector('#fn'); await mp.click('button[type=submit]'); await mp.waitForSelector('.hello h1');
    check('on a phone the Home link is there (the top bar link is hidden)', (await mp.locator('.homelinks a:has-text("My dashboard")').isVisible()) && !(await mp.locator('.sitelink').isVisible()));
    const over = await mp.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
    check('phone: no sideways scrolling on Home', !over);
    await m.close(); await ctx.close();
  }

  // ───── Latvian explanations ─────
  {
    const { ctx, p } = await guest({ viewport: { width: 1200, height: 900 } });
    // a task up to B1.2 that we can answer wrongly: present simple A2.1 mcq
    let r = await post(p, 'session/start', { mode: 'practice', skills: ['present_simple'], level: 'A2.1', length: 10 });
    await p.goto(BASE + '/index.html#/session'); await p.reload(); await p.waitForSelector('.task');
    const it = ITEMS[r.item.id];
    if (it.kind === 'mcq') await p.locator('label.opt', { hasText: it.wrong[0] }).first().click();
    else if (it.kind === 'gap') { const ins = p.locator('.task .q input.blank'); for (let i = 0; i < await ins.count(); i++) await ins.nth(i).fill('zzz'); }
    else if (it.kind === 'text') await p.fill('.task input.type-in', 'zzz');
    else await p.fill('.task textarea.write', 'hello there');
    await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
    const fbEn = await p.locator('.feedback').innerText();
    check('the feedback shows a Latviski button up to B1.2', (await p.locator('.feedback button:has-text("Latviski")').count()) === 1 && /Why:/.test(fbEn), fbEn.slice(0, 80));
    await p.click('.feedback button:has-text("Latviski")');
    const fbLv = await p.locator('.feedback').innerText();
    check('pressing it shows the explanation in Latvian', /Kāpēc:/.test(fbLv) && !/Why:/.test(fbLv) && (await p.locator('.feedback button:has-text("English")').count()) === 1, fbLv.slice(0, 120));
    await p.locator('.feedback details.rule summary').click();
    check('the rule reminder is Latvian too', /Atgādinājums/.test(await p.locator('.feedback details.rule summary').innerText()) && /Kā to veido/.test(await p.locator('.feedback .rulecard').innerText()));
    await p.screenshot({ path: OUT + '99-latvian-feedback.png', fullPage: true });
    // remembered: the profile shows the choice, and the next feedback is Latvian at once
    await p.goto(BASE + '/index.html#/profile'); await p.waitForSelector('input[name=lang]');
    check('the choice is saved in the profile', await p.locator('input[name=lang][value=lv]').isChecked());
    await p.screenshot({ path: OUT + '99b-profile-language.png', fullPage: true });
    await p.locator('label:has(input[name=lang][value=en])').click(); await p.waitForTimeout(400);
    await p.reload(); await p.waitForSelector('input[name=lang]');
    check('and can be switched back to English', await p.locator('input[name=lang][value=en]').isChecked());
    await p.locator('label:has(input[name=lang][value=lv])').click(); await p.waitForTimeout(400);
    // rule cards page in Latvian, grouped by area
    await p.goto(BASE + '/index.html#/rules'); await p.waitForSelector('.rulecard');
    check('the rule cards page is Latvian and grouped by area', /Kā to veido/.test(await p.locator('main').innerText()) && (await p.locator('.area-block h2').count()) === 5);
    await p.screenshot({ path: OUT + '99c-rules-lv.png', fullPage: true });
    // above B1.2 there is no Latvian: a mixed conditional task
    r = await post(p, 'session/start', { mode: 'practice', skills: ['cond_mixed'], level: 'B2.1', length: 5 });
    await p.goto(BASE + '/index.html#/session'); await p.reload(); await p.waitForSelector('.task');
    const it2 = ITEMS[r.item.id];
    if (it2.kind === 'mcq') await p.locator('label.opt', { hasText: it2.wrong[0] }).first().click(); else await p.fill('.task textarea.write, .task input.type-in', 'hello there now');
    await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
    check('above B1.2 there is no Latviski button and the text stays English', (await p.locator('.feedback button:has-text("Latviski")').count()) === 0 && /Why:|Model answer/.test(await p.locator('.feedback').innerText()));
    await ctx.close();
  }

  check('no page errors', errs.length === 0, errs);
  console.log(ok ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
