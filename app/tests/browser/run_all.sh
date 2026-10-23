#!/bin/bash
# Every test: python / php tests first, then the browser tests (Playwright). Start the dev server first:
#   php -S 127.0.0.1:8099 -t app        (from the repository root)
# The browser tests need Playwright (npm root -g) and use a fresh database each time. Output goes to the screen: pipe it to a file to keep it.
cd "$(dirname "$0")/../.."
APP=$(pwd)
export NODE_PATH=$(npm root -g)
php tests/grader_test.php 2>&1 | tail -1
for t in sso_test security_test research_test reports_test tasks_test comeback_test drafts_test placement_test; do rm -f var/ef.sqlite*; printf "== %-14s" $t; python3 tests/$t.py 2>&1 | grep -v "^PASS" | tail -2 | tr '\n' ' '; echo; done
cd tests/browser
for t in e2e e2e_teacher; do rm -f $APP/var/ef.sqlite*; printf "== %-14s" $t; timeout 250 node $t.js 2>&1 | tail -1; done
for t in instr_italics comeback_ui study_ui hover dnd dnd_stuck menu blank avatars pwa xss phonebar review review_dnd italics_ui topbar topics_sound; do rm -f $APP/var/ef.sqlite*; printf "== %-14s" $t; timeout 290 node $t.js 2>&1 | tail -1; done
echo FINISHED
