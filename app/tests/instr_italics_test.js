// node app/tests/instr_italics_test.js ITEMS.json
// Every word the learner is to use is in italics in the instruction (teacher, 14 November): runs the app's own UI.markForms
// (app/assets/ui.js) on the instruction of every task and lists those where a named word stays plain. Exit 1 when one is found.
const fs = require('fs'), path = require('path');
const src = fs.readFileSync(path.join(__dirname, '..', 'assets', 'ui.js'), 'utf8');
const body = src.slice(src.indexOf('function markForms('), src.indexOf('\n  }\n', src.indexOf('function markForms(')) + 4);
const markForms = new Function(body + '; return markForms;')();
const SPLIT = /^((?:Choose|Make|Use|Rewrite|Complete|Start|Imagine|Add|Ask|Give|Put|Change|Write|Turn|Report|Say|Correct|Fill|Match|Join|Finish|Answer|Decide|Find|Rephrase|Transform|Reorder|Order)[^:\n]{0,120}?):\s+([\s\S]*\p{L}[\s\S]*)$/u;
const items = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
// an instruction that names words to use: "with / without / using X", "Write X or Y", "(a, b or c)", "the past of X", "Use X for"
const NAMES = /\b(with|without|using)\s+(?!(?:a|an|the)\s)\S|^(Write|Choose|Use)\s+[A-Za-z']+(,\s+[A-Za-z']+)*\s+or\s+[A-Za-z']+\s*$|\([A-Za-z' ]+(,\s+[A-Za-z' ]+)*,?\s+or\s+[A-Za-z' ]+\)|\bthe (past|negative|question) of \w|^Use (?!(?:a|an|the|one|two|it|this|these)\s)\w[^:]* for\b|\bwith the elderly\b/i;
const bad = new Map();
for (const it of items) {
  const m = SPLIT.exec(it.q || ''); if (!m) continue;
  const instr = m[1], marked = markForms(instr);
  if (NAMES.test(instr) && marked.indexOf('*') < 0) bad.set(instr, (it.src || '') + ' ' + (it.id || ''));
}
for (const [i, w] of bad) console.log('PLAIN  ' + i + '   (' + w + ')');
console.log(bad.size ? `FAIL ${bad.size} instructions name a word to use without italics` : 'PASS every named word is in italics');
process.exit(bad.size ? 1 : 0);
