const { chromium, devices } = require('playwright');
const fs = require('fs');
const ITEMS = Object.fromEntries(JSON.parse(fs.readFileSync('/home/user/englishfever/app/content/items.json')).map(i => [i.id, i]));
const META = JSON.parse(fs.readFileSync('/home/user/englishfever/app/content/meta.json'));
const BASE = 'http://127.0.0.1:8099', OUT = __dirname + '/shots/';
const LV = META.levels; const idx = l => LV.indexOf(l);
(async () => {
  const b = await chromium.launch(); let ok = true; const errs = [];
  const check = (n, c, x) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : ' -> ' + JSON.stringify(x))); };
  const ctx = await b.newContext({ viewport: { width: 1100, height: 1000 } });
  // a stand-in for the browser's sound: count the notes that would play
  await ctx.addInitScript(() => {
    window.__notes = 0;
    window.AudioContext = class { constructor() { this.state = 'running'; this.currentTime = 0; this.destination = {}; }
      createOscillator() { window.__notes++; return { type: '', frequency: { value: 0 }, connect() {}, start() {}, stop() {} }; }
      createGain() { return { gain: { setValueAtTime() {}, exponentialRampToValueAtTime() {} }, connect() {} }; } resume() {} };
  });
  const p = await ctx.newPage(); p.on('pageerror', e => errs.push(e.message));
  await p.goto(BASE + '/index.html'); await p.waitForSelector('#nick'); await p.waitForTimeout(1400); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
  const post = (r, d) => p.evaluate(async ([r, d]) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json(), [r, d]);

  // topics without any approved question are not shown to learners (Modal verbs and Comparison until their questions are approved)
  META.skills = (await (await p.request.get(BASE + '/api.php?r=meta')).json()).skills;
  // ── Home topics, new learner (level unknown: A2.1)
  const hiddenExpected = META.skills.filter(s => idx(s.levels[0]) > 0 + 2).length;
  await p.locator('details.card.fold > summary:has-text("Your topics")').click(); await p.waitForTimeout(150);   // Home keeps the topics folded
  const folds = () => p.locator('details.area-fold');
  check('areas are fold-away sections; only the first is open for a new learner', (await folds().count()) === 5 || (await folds().count()) >= 3, await folds().count());
  const openNames = await p.locator('details.area-fold[open] > summary .h3').allInnerTexts();
  check('first area open, the others folded', openNames.length === 1 && /Active/.test(openNames[0]), openNames);
  const sum0 = await p.locator('details.area-fold > summary').first().innerText();
  check('each area says how many topics are started', /0 of \d+ started/.test(sum0), sum0);
  const shown = await p.locator('.skill').count();
  check('topics far above A2 are not listed; the link says how many wait', (await p.locator('button:has-text("Show topics for higher levels")').innerText()).includes('(' + hiddenExpected + ')') && shown === META.skills.length - hiddenExpected, [hiddenExpected, shown]);
  await p.locator('button:has-text("Show topics for higher levels")').click(); await p.waitForTimeout(100);
  await p.evaluate(() => document.querySelectorAll('details.area-fold').forEach(d => { d.open = true; })); await p.waitForTimeout(100);
  check('after the link every topic is listed', (await p.locator('.skill').count()) === META.skills.length, await p.locator('.skill').count());
  check('the link now offers to hide them again', (await p.locator('button:has-text("Hide topics for higher levels")').count()) === 1);
  await p.reload(); await p.waitForSelector('.hello h1');
  check('the choices are remembered after a reload (all shown, areas stay open)', (await p.locator('.skill').count()) === META.skills.length, await p.locator('.skill').count());
  await p.locator('button:has-text("Hide topics for higher levels")').click();
  await p.screenshot({ path: OUT + '70-home-topics.png', fullPage: true });

  // ── card wording, one-tap Practise
  const card = p.locator('.skill', { hasText: 'Present simple' }).first();
  check('card of a new topic: "New", "Not started", Practise and Options', (await card.locator('.pill').innerText()) === 'New' && /Not started/.test(await card.innerText()) && (await card.locator('button:has-text("Practise")').count()) === 1 && (await card.locator('button:has-text("Options")').count()) === 1);
  // two answers in that topic through the API
  let cur = await post('session/start', { mode: 'practice', skills: ['present_simple'], level: 'A2.1', length: 10 });
  for (let i = 0; i < 2; i++) { const it = ITEMS[cur.item.id]; const ans = it.kind === 'mcq' ? it.correct : (it.kind === 'gap' ? it.answers.map(a => a[0]) : (it.kind === 'order' ? it.sentence.split(' ') : (it.kind === 'match' ? it.pairs.map(x => x[1]) : it.answers[0][0]))); cur = await post('session/answer', { session_id: cur.session.id, item_id: cur.item.id, answer: ans, time_ms: 2000 }); cur = { session: cur.session, item: cur.next }; }
  await post('session/quit', { session_id: cur.session.id });
  await p.goto(BASE + '/index.html#/home'); await p.reload(); await p.waitForSelector('.hello h1');
  const c2 = p.locator('.skill', { hasText: 'Present simple' }).first();
  check('after two answers: "Started" and "2 done · 100% correct"', (await c2.locator('.pill').innerText()) === 'Started' && /2 done · 100% correct/.test(await c2.innerText()), await c2.innerText());
  check('no card says "tasks" as if there were a limit', !(await p.locator('.skill').allInnerTexts()).some(t => /\btasks?\b/.test(t)));
  const openFirst = await p.locator('details.area-fold[open] > summary .h3').first().innerText();
  await p.locator('.skill', { hasText: 'Present simple' }).first().locator('button:has-text("Practise")').click();
  await p.waitForSelector('.sess .task .q'); await p.waitForTimeout(150);
  const lab = await p.locator('.sess-top > span').first().innerText();
  check('Practise starts the session at once, in that topic', /Question 1 of 10/.test(lab) && (await p.locator('.task .pill.dark').first().innerText()) === 'Present simple', lab);
  await post('session/quit', { session_id: (await p.evaluate(async () => (await (await fetch('api.php?r=session%2Fresume')).json()).resume.session.id)) });
  // Options → the picker with the topic chosen
  await p.goto(BASE + '/index.html#/home'); await p.waitForSelector('.hello h1');
  await p.locator('.skill', { hasText: 'Present simple' }).first().locator('button:has-text("Options")').click(); await p.waitForSelector('.picker-group');
  check('Options opens the picker with that topic chosen', (await p.locator('.chipsel input:checked').count()) === 1 && /Present simple/.test(await p.locator('.chipsel label:has(input:checked)').innerText()));
  check('the picker has no "higher levels" link: the level buttons do that job', (await p.locator('button:has-text("Show topics for higher levels")').count()) === 0 && (await p.locator('.lvseg input:checked').count()) === 1);

  // ── sound: off by default, on by choice
  await p.goto(BASE + '/index.html#/profile'); await p.waitForSelector('#snd');
  check('Profile has a Sounds card and it is OFF by default', (await p.locator('#snd').isChecked()) === false);
  await post('session/start', { mode: 'practice', skills: ['present_simple'], level: 'A2.1', length: 10 });
  await p.goto(BASE + '/index.html#/session'); await p.reload(); await p.waitForSelector('.task .q');
  check('speaker button in the session shows "off"', (await p.locator('.speaker').getAttribute('aria-pressed')) === 'false' && /off/i.test(await p.locator('.speaker').getAttribute('aria-label')));
  const answerFirst = async right => {
    await p.waitForSelector('.task .q'); const id = await p.evaluate(async () => (await (await fetch('api.php?r=session%2Fresume')).json()).resume.item.id); const it = ITEMS[id];
    if (it.kind === 'mcq') await p.locator('label.opt[data-opt="' + (right ? it.correct : it.wrong[0]).replace(/"/g, '\\"') + '"]').click();
    else if (it.kind === 'gap' && !it.bank) { const inp = p.locator('.task input.blank'); for (let i = 0; i < it.answers.length; i++) await inp.nth(i).fill(right ? it.answers[i][0] : 'zzz'); }
    else if (it.kind === 'text') await p.fill('.task input.type-in', right ? it.answers[0][0] : 'zzz');
    else if (it.kind === 'order') { const toks = it.sentence.split(' '); for (const t of (right ? toks : toks.slice().reverse())) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }).first().click(); }
    else if (it.kind === 'match') { const rs = it.pairs.map(x => x[1]); for (const t of (right ? rs : rs.slice().reverse())) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }).first().click(); }
    await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
  };
  const next = async () => { await p.click('.feedback .btn:has-text("Next")'); await p.waitForSelector('.task .q'); await p.waitForTimeout(60); };
  await answerFirst(true);
  check('with sound off, nothing is played', (await p.evaluate(() => window.__notes)) === 0);
  await next();
  await p.locator('.speaker').click();
  check('the speaker button turns sound on and plays a sample', (await p.locator('.speaker').getAttribute('aria-pressed')) === 'true' && (await p.evaluate(() => window.__notes)) === 2 && (await p.evaluate(() => localStorage.getItem('ef_sound'))) === '1', await p.evaluate(() => window.__notes));
  await p.evaluate(() => { window.__notes = 0; });
  await answerFirst(true);
  check('a right answer plays two notes', (await p.evaluate(() => window.__notes)) === 2, await p.evaluate(() => window.__notes));
  await next(); await p.evaluate(() => { window.__notes = 0; });
  await answerFirst(false);
  check('a wrong answer plays its own two notes', (await p.evaluate(() => window.__notes)) === 2, await p.evaluate(() => window.__notes));
  // looking back plays nothing
  await p.evaluate(() => { window.__notes = 0; });
  await p.click('.sess-top .linkbtn:has-text("Previous")'); await p.waitForSelector('.feedback'); await p.waitForTimeout(100);
  check('looking back at a task plays nothing', (await p.evaluate(() => window.__notes)) === 0);
  await p.goto(BASE + '/index.html#/profile'); await p.waitForSelector('#snd');
  check('Profile shows the same choice (on) and can switch it off', (await p.locator('#snd').isChecked()) === true);
  await p.locator('#snd').uncheck();
  check('switched off again and remembered', (await p.evaluate(() => localStorage.getItem('ef_sound'))) === '0');
  await p.reload(); await p.waitForSelector('#snd');
  check('after a reload it is still off', (await p.locator('#snd').isChecked()) === false);

  check('no page errors', errs.length === 0, errs);
  console.log(ok ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
