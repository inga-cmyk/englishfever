const { chromium } = require('playwright');
const BASE = 'http://127.0.0.1:8099';
let ok = true; const check = (n, c, x) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : '  -> ' + x)); };
(async () => {
  const b = await chromium.launch(); const p = await (await b.newContext()).newPage();
  await p.goto(BASE + '/index.html'); await p.waitForSelector('#nick');
  const f = s => p.evaluate(x => UI.markForms(x), s);
  const cases = [
    ["Make it negative with don't have to", "Make it negative with *don't have to*"],
    ["Complete with have to or has to", "Complete with *have to or has to*"],
    ["Make a question with How long", "Make a question with *How long*"],
    ["Make it negative and use 'any'", "Make it negative and use *any*"],
    ["Rewrite with as ... as", "Rewrite with *as ... as*"],
    ["Choose the correct form", "Choose the correct form"],
    ["Complete with the correct form", "Complete with the correct form"],
    ["Make the sentence negative", "Make the sentence negative"],
    ["Use the present simple for a timetable", "Use the present simple for a timetable"],
    ["Join with when", "Join with *when*"],
  ];
  for (const [a, e] of cases) check('"' + a + '"', (await f(a)) === e, await f(a));
  console.log(ok ? 'ALL PASS' : 'SOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
