#!/bin/bash
# Every test, the same set the developer runs before each package (about 15 minutes):
#   bash app/tests/browser/run_all.sh 2>&1 | tee /tmp/run_all.log
# Starts the dev server on 127.0.0.1:8099 if it is not running. Uses a fresh SQLite database (app/var/ef.sqlite) for each test,
# so never run two copies at once and do not use that database for anything else meanwhile.
# Needs php, python3, node and Playwright (require('playwright') from `npm root -g`). Each line ends with ALL PASS / OK / no errors.
cd "$(dirname "$0")/../.."
APP=$(pwd)
export NODE_PATH=$(npm root -g) EF_DEV=1
curl -s -o /dev/null --max-time 2 http://127.0.0.1:8099/index.html || { (nohup php -S 127.0.0.1:8099 -t "$APP" >/tmp/ef-php8099.log 2>&1 &); sleep 2; }
php tests/grader_test.php 2>&1 | tail -1; php tests/selfgrade_test.php 2>&1 | tail -1
rm -f var/ef.sqlite*; python3 tests/drafts_test.py >/dev/null 2>&1; php tests/selfgrade_drafts_test.php 2>&1 | tail -1
php tests/error_model_test.php 2>&1 | tail -1; php tests/bank_update_test.php 2>&1 | tail -1
for t in orders_test sso_test security_test research_test reports_test tasks_test comeback_test drafts_test placement_test pulse_test probe_test reword_test draft_rules_test; do
  rm -f var/ef.sqlite*; printf "== %-16s" $t; python3 tests/$t.py 2>&1 | grep -v "^PASS" | tail -2 | tr "\n" " "; echo
done
cd tests/browser
for t in e2e e2e_teacher comeback_ui study_ui hover dnd dnd_stuck menu blank avatars pwa xss phonebar review review_dnd italics_ui topbar topics_sound evidence usage; do
  rm -f "$APP"/var/ef.sqlite*; printf "== %-16s" $t; timeout 290 node $t.js 2>&1 | tail -1
done
rm -f "$APP"/var/ef.sqlite*
echo FINISHED
