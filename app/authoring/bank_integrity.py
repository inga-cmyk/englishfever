"""Validate final learner-facing items and preserve published question versions."""
import json
import re
from collections import Counter


def validate(items, skills, levels):
    declared = {s[0]: s[3] for s in skills}
    ids = Counter(i['id'] for i in items)
    errors = [f'duplicate id: {k}' for k, n in ids.items() if n != 1]
    coverage = {}
    for it in items:
        def check(condition, message):
            if not condition:
                errors.append(f"{it['id']}: {message}")
        check(it['skill'] in declared and it['level'] in declared.get(it['skill'], []), 'undeclared skill/level')
        check(it['bloom'] in range(1, 7), 'invalid thinking level')
        check(bool(it.get('q', '').strip()) and bool(it.get('why', '').strip()), 'missing prompt/explanation')
        if it['level'] in levels[:levels.index('B1.2') + 1]:
            check(bool(it.get('why_lv', '').strip()), 'missing Latvian explanation')
        coverage.setdefault((it['skill'], it['level']), set()).add(it['bloom'])
        kind = it['kind']
        check(kind in {'mcq', 'gap', 'text', 'order', 'match', 'write'}, 'unsupported type')
        if kind == 'mcq':
            options = [it['correct']] + it['wrong']
            check(len(options) >= 3 and len(set(options)) == len(options), 'invalid/duplicate options')
            check(set(it.get('wrong_why', {})).issubset(it['wrong']), 'feedback for unknown option')
            if it.get('wrong_why_lv'):
                check(set(it['wrong_why_lv']) == set(it.get('wrong_why', {})), 'translation feedback mismatch')
        if kind in {'gap', 'text', 'order'}:
            check(bool(it['answers']) and all(b and all(isinstance(a, str) and a.strip() for a in b) for b in it['answers']), 'empty accepted answer')
        if kind == 'gap':
            check(it['q'].count('___') == len(it['answers']), 'blank count mismatch')
            if it.get('bank'):
                first = [b[0] for b in it['answers']]
                check(len(it['bank']) > len(first), 'word bank needs a decoy')
                check(len(set(it['bank'])) == len(it['bank']), 'duplicate bank cards')
                check(all(len(b) == 1 for b in it['answers']), 'bank gaps require one answer per slot')
                check(all(a in it['bank'] for a in first) and len(set(first)) == len(first), 'bank cannot fill every slot')
        if kind == 'order':
            tokens = sorted(it['sentence'].split())
            check(4 <= len(tokens) <= 16, 'order task must contain 4–16 tokens')
            check(all(sorted(a.split()) == tokens for a in it['answers'][0]), 'alternative changes the cards')
            if it.get('display_answer'):
                display = it['display_answer'].replace(',', '').rstrip('.?!').lower().split()
                check(display == it['sentence'].lower().split(), 'display model changes the answer words/order')
        if kind == 'match':
            check(3 <= len(it['pairs']) <= 6, 'matching needs 3–6 pairs')
            for side in (0, 1):
                check(len({p[side] for p in it['pairs']}) == len(it['pairs']), 'duplicate matching cards')
        for key in ('must', 'hints'):
            for rule in it.get(key, []):
                try:
                    rx = re.compile(rule[0], re.I)
                    if key == 'must':
                        check(bool(rx.search(it['model'])), 'model fails its own checklist')
                except re.error as exc:
                    check(False, f'invalid pattern: {exc}')
                if it.get('why_lv'):
                    check(len(rule) == 3 and bool(rule[2]), 'missing translated checklist/hint')
    for skill, allowed in declared.items():
        for level in allowed:
            if coverage.get((skill, level)) != set(range(1, 7)):
                errors.append(f'{skill} {level}: incomplete thinking-level coverage')
    if errors:
        raise ValueError('\n'.join(errors))


def history(items, path, record=False):
    with open(path, encoding='utf-8') as f:
        published = json.load(f)
    known = {i['id']: i for i in published}
    if len(known) != len(published):
        raise ValueError('Duplicate published ID')
    active = {i['id']: i for i in items}
    for it in items:
        if it['id'] in known and it != known[it['id']]:
            raise ValueError(f"{it['id']}: published content is immutable; give this correction a new revision ID")
    if record:
        published.extend(it for it in items if it['id'] not in known)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(published, f, ensure_ascii=False, indent=0)
    return [it for it in published if it['id'] not in active]
