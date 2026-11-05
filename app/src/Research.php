<?php
// Research study: the anonymised export for the master's thesis (University of Latvia).
// Teacher's decision, 5 November 2026: every registered learner is in the study from registration, with all their data; a learner
// can say "I do not agree" (Profile → Your data → Research) and is then left out. No random conditions: everyone sees the same app.

final class Research
{
    /** What can be switched on or off for a learner. 'on' is the app as everyone else sees it (the control), 'off' hides the feature. */
    public const FACTORS = ['streak' => 'Daily streak counter', 'leaderboard' => 'Leaderboard'];
    public const JOINED = 1;
    public const DECLINED = 2;
    private const BLOCK = 4; // allocation in shuffled blocks of 4 (two of each arm), so the groups stay the same size

    public static function enabled(): bool
    {
        return true;   // always on (teacher, 5 November); 'research_enabled' in config.php is no longer read
    }

    /** The factors listed in config ('experiments' => ['streak', 'leaderboard']). Unknown names are ignored. */
    public static function activeFactors(): array
    {
        return [];   // no random conditions any more (teacher, 5 November): 'experiments' in config.php is ignored
    }

    /** Registered learners only: a guest is a cookie in one browser, so there is no person to ask or to follow over time. */
    public static function eligible(array $u): bool
    {
        return $u['provider'] !== 'guest' && $u['role'] === 'student';
    }

    /** Join (needs the study to be switched on) or leave (always possible). Leaving also puts the learner back on the normal app. */
    public static function join(array $u, bool $join): void
    {
        if (!self::eligible($u)) throw new ApiError('The study is for registered learners.', 403);
        // The app keeps time per day, so remember how much of today was already recorded: the export starts at the moment of consent.
        $base = (int) Db::val('SELECT seconds FROM activity WHERE user_id = ? AND day = ?', [$u['id'], Stats::today()]);
        Db::update('users', ['research' => $join ? self::JOINED : self::DECLINED, 'research_at' => time(), 'research_base' => $base], 'id = ?', [$u['id']]);
    }

    /** Condition of each active factor for this learner, assigned on first use. People outside the study always get the normal app. */
    public static function arms(array $u): array
    {
        $factors = self::activeFactors();
        if (!$factors || (int) ($u['research'] ?? 0) !== self::JOINED || !self::eligible($u)) return [];
        $have = [];
        foreach (Db::all('SELECT factor, arm FROM conditions WHERE user_id = ?', [$u['id']]) as $r) $have[$r['factor']] = $r['arm'];
        $out = [];
        foreach ($factors as $f) $out[$f] = $have[$f] ?? self::assign((int) $u['id'], $f);
        return $out;
    }

    private static function seed(): string
    {
        $s = Db::kvGet('research_seed');
        if ($s) return $s;
        try {
            Db::kvSet('research_seed', bin2hex(random_bytes(32)));
        } catch (PDOException $e) { // two first requests at once
        }
        return (string) Db::kvGet('research_seed');
    }

    /** Next arm in the sequence for this factor. The order inside each block comes from a keyed hash: reproducible by us, unpredictable for anyone else. */
    private static function assign(int $uid, string $factor): string
    {
        $seq = (int) Db::val('SELECT COALESCE(MAX(seq), 0) FROM conditions WHERE factor = ?', [$factor]) + 1;
        $pos = $seq - 1;
        $bytes = hash_hmac('sha256', $factor . ':' . intdiv($pos, self::BLOCK), self::seed(), true);
        $slots = ['on', 'on', 'off', 'off'];
        for ($i = self::BLOCK - 1; $i > 0; $i--) {
            $j = unpack('N', substr($bytes, $i * 4, 4))[1] % ($i + 1);
            [$slots[$i], $slots[$j]] = [$slots[$j], $slots[$i]];
        }
        $arm = $slots[$pos % self::BLOCK];
        try {
            Db::insert('conditions', ['user_id' => $uid, 'factor' => $factor, 'arm' => $arm, 'seq' => $seq, 'assigned_at' => time()]);
        } catch (PDOException $e) { // two requests at once: keep the first assignment
            $r = Db::one('SELECT arm FROM conditions WHERE user_id = ? AND factor = ?', [$uid, $factor]);
            if ($r) return $r['arm'];
            throw $e;
        }
        return $arm;
    }

    /** SQL for the leaderboard: learners whose condition hides the leaderboard are not listed on it either. */
    public static function leaderboardClause(): string
    {
        if (!in_array('leaderboard', self::activeFactors(), true)) return '';
        return " AND NOT (u.research = 1 AND EXISTS (SELECT 1 FROM conditions c WHERE c.user_id = u.id AND c.factor = 'leaderboard' AND c.arm = 'off'))";
    }

    /** For the teacher page: how many registered learners agreed, and how the conditions are split. */
    public static function summary(): array
    {
        $reg = "provider <> 'guest' AND role = 'student'";
        $out = [
            'enabled' => self::enabled(),
            'registered' => (int) Db::val("SELECT COUNT(1) FROM users WHERE $reg"),
            'joined' => (int) Db::val("SELECT COUNT(1) FROM users WHERE $reg AND is_test = 0 AND research <> ?", [self::DECLINED]),
            'declined' => (int) Db::val("SELECT COUNT(1) FROM users WHERE $reg AND research = ?", [self::DECLINED]),
            'factors' => [],
        ];
        foreach (self::activeFactors() as $f) {
            $c = ['on' => 0, 'off' => 0];
            foreach (Db::all('SELECT c.arm, COUNT(1) AS n FROM conditions c JOIN users u ON u.id = c.user_id WHERE c.factor = ? AND u.research = ? GROUP BY c.arm', [$f, self::JOINED]) as $r) $c[$r['arm']] = (int) $r['n'];
            $out['factors'][] = ['id' => $f, 'label' => self::FACTORS[$f], 'on' => $c['on'], 'off' => $c['off']];
        }
        return $out;
    }

    // ───────── export ─────────

    /** A code that stands for one learner in the files. The key is stored in the database, so the code stays the same in every export. */
    public static function pid(int $uid): string
    {
        return substr(hash_hmac('sha256', 'pid:' . $uid, self::seed()), 0, 12);
    }

    private static function participants(): array
    {
        // everyone except those who said no; all their data, from registration (the study day 0 is the day of registration)
        $out = [];
        foreach (Db::all("SELECT * FROM users WHERE research <> ? AND provider <> 'guest' AND role = 'student' AND is_test = 0 ORDER BY id", [self::DECLINED]) as $u) {
            $u['research_at'] = (int) $u['created_at']; $u['research_base'] = 0;
            $out[] = $u;
        }
        return $out;
    }

    private static function dayOf(int $ts): string
    {
        return (new DateTime('@' . $ts))->setTimezone(Stats::tz())->format('Y-m-d');
    }

    private static function weekOf(int $ts): string
    {
        return (new DateTime('@' . $ts))->setTimezone(Stats::tz())->format('o-\WW');
    }

    /** Whole days from $from to $to (both Y-m-d). Noon UTC keeps daylight saving out of it. */
    private static function between(string $from, string $to): int
    {
        return (int) round((strtotime($to . ' 12:00:00 UTC') - strtotime($from . ' 12:00:00 UTC')) / 86400);
    }

    private static function csv(array $header, iterable $rows): string
    {
        $fh = fopen('php://temp', 'w+');
        fputcsv($fh, $header, ',', '"', '\\');
        foreach ($rows as $r) fputcsv($fh, $r, ',', '"', '\\');
        rewind($fh);
        return (string) stream_get_contents($fh);
    }

    /**
     * Totals per day since registration (research_at is set to the registration time in participants()): day => [seconds, answers, xp]. Answers and points come from the time-stamped answers; seconds come
     * from the daily record, minus what it already held when the learner joined. Nothing from before the consent is counted.
     */
    private static function daily(array $u): array
    {
        $id = (int) $u['id'];
        $at = (int) $u['research_at'];
        $start = self::dayOf($at);
        $out = [];
        foreach (Db::all('SELECT created_at, xp FROM attempts WHERE user_id = ? AND created_at >= ?', [$id, $at]) as $a) {
            $d = self::dayOf((int) $a['created_at']);
            $out[$d] ??= [0, 0, 0];
            $out[$d][1]++;
            $out[$d][2] += (int) $a['xp'];
        }
        foreach (Db::all('SELECT day, seconds FROM activity WHERE user_id = ? AND day >= ?', [$id, $start]) as $a) {
            $s = (int) $a['seconds'] - ($a['day'] === $start ? (int) $u['research_base'] : 0);
            if ($s > 0) {
                $out[$a['day']] ??= [0, 0, 0];
                $out[$a['day']][0] = $s;
            }
        }
        ksort($out);
        return $out;
    }

    /** One row per learner. */
    public static function people(): string
    {
        $today = Stats::today();
        $factors = [];   // no conditions any more (teacher, 5 November)
        $rows = [];
        foreach (self::participants() as $u) {
            $id = (int) $u['id'];
            $start = self::dayOf((int) $u['research_at']);
            $cond = [];
            foreach (Db::all('SELECT factor, arm FROM conditions WHERE user_id = ?', [$id]) as $c) $cond[$c['factor']] = $c['arm'];
            $days = [];
            $secs = $xp = $ans = 0;
            foreach (self::daily($u) as $day => [$s, $a, $x]) {
                $secs += $s;
                $ans += $a;
                $xp += $x;
                if ($a > 0) $days[self::between($start, $day)] = true;
            }
            ksort($days);
            $idx = array_keys($days);
            $best = 0;
            $run = 0;
            $prev = null;
            foreach ($idx as $d) {
                $run = ($prev !== null && $d === $prev + 1) ? $run + 1 : 1;
                $best = max($best, $run);
                $prev = $d;
            }
            $weeks = [];
            foreach ($idx as $d) $weeks[intdiv($d, 7)] = true;
            $att = Db::one('SELECT COUNT(1) AS n, COALESCE(SUM(correct), 0) AS c FROM attempts WHERE user_id = ? AND created_at >= ?', [$id, (int) $u['research_at']]);
            $ses = Db::one("SELECT COUNT(1) AS n, COALESCE(SUM(CASE WHEN mode = 'smart' THEN 1 ELSE 0 END), 0) AS smart FROM psessions WHERE user_id = ? AND n > 0 AND started_at >= ?", [$id, (int) $u['research_at']]);
            $pl = Db::one("SELECT state, ended_at FROM psessions WHERE user_id = ? AND mode = 'placement' AND ended_at IS NOT NULL AND ended_at >= ? ORDER BY id DESC LIMIT 1", [$id, (int) $u['research_at']]);
            $plLevel = '';
            if ($pl) {
                $st = json_decode((string) $pl['state'], true);
                $plLevel = $st['report']['overall_level'] ?? '';
            }
            $row = [
                self::pid($id), self::weekOf((int) $u['created_at']), self::weekOf((int) $u['research_at']),
                ($u['lang'] ?? '') === 'lv' ? 1 : 0, !empty($u['avatar']) ? 1 : 0, (int) $u['show_on_board'] === 1 ? 1 : 0,
            ];
            foreach ($factors as $f) $row[] = $cond[$f] ?? '';
            array_push(
                $row,
                self::between($start, $today) + 1,
                count($days), $ans, $secs, $xp, $att['n'] ? round(100 * $att['c'] / $att['n'], 1) : '',
                (int) $ses['n'], (int) $ses['smart'], $plLevel,
                $idx ? $idx[0] : '', $idx ? end($idx) : '', $best, count($weeks),
                isset($days[1]) ? 1 : 0, isset($days[7]) ? 1 : 0, isset($days[30]) ? 1 : 0
            );
            $rows[] = $row;
        }
        return self::csv(array_merge(
            ['pid', 'join_week', 'consent_week', 'explanations_lv', 'avatar_chosen', 'board_opt_in'],
            array_map(fn($f) => 'cond_' . $f, $factors),
            ['observed_days', 'active_days', 'answers', 'seconds', 'xp', 'correct_pct', 'sessions', 'sessions_smart', 'placement_level',
                'first_active_day', 'last_active_day', 'longest_streak', 'weeks_active', 'active_day1', 'active_day7', 'active_day30']
        ), $rows);
    }

    /** One row per learner and day with any recorded activity. A day that is missing means no activity. */
    public static function days(): string
    {
        $rows = [];
        foreach (self::participants() as $u) {
            $start = self::dayOf((int) $u['research_at']);
            foreach (self::daily($u) as $day => [$s, $a, $x]) {
                $rows[] = [self::pid((int) $u['id']), self::between($start, $day), (int) date('N', strtotime($day . ' 12:00:00 UTC')), $s, $a, $x];
            }
        }
        return self::csv(['pid', 'study_day', 'weekday', 'seconds', 'answers', 'xp'], $rows);
    }

    /** One row per answered task. The learner's own text is left out. */
    public static function answers(): string
    {
        $area = [];
        foreach (Content::meta()['skills'] as $s) $area[$s['id']] = $s['area'];
        $rows = [];
        foreach (self::participants() as $u) {
            $start = self::dayOf((int) $u['research_at']);
            $pid = self::pid((int) $u['id']);
            $sql = 'SELECT a.item_id, a.skill, a.level, a.bloom, a.correct, a.time_ms, a.created_at, a.answer, a.exposure, a.served_why, a.app_ver, a.lang, a.fb_ms, a.card, p.mode, p.source FROM attempts a LEFT JOIN psessions p ON p.id = a.psession_id WHERE a.user_id = ? AND a.created_at >= ? ORDER BY a.id';
            foreach (Db::all($sql, [(int) $u['id'], (int) $u['research_at']]) as $a) {
                $t = (new DateTime('@' . $a['created_at']))->setTimezone(Stats::tz());
                $rows[] = [$pid, self::between($start, $t->format('Y-m-d')), (int) $t->format('N'), (int) $t->format('G'), $a['mode'] ?? '', $a['skill'], $area[$a['skill']] ?? '', $a['level'], (int) $a['bloom'], (int) $a['correct'], round($a['time_ms'] / 1000, 1), $a['item_id'],
                    $a['answer'] === '(skipped)' ? 1 : 0, $a['exposure'] ?? '', $a['served_why'] ?? '', $a['source'] ?? '', $a['lang'] ?? '', $a['fb_ms'] === null ? '' : round($a['fb_ms'] / 1000, 1), $a['app_ver'] ?? '', (int) ($a['card'] ?? 0), Content::role(Content::item((string) $a['item_id']))];
            }
        }
        return self::csv(['pid', 'study_day', 'weekday', 'hour', 'mode', 'skill', 'area', 'level', 'bloom', 'correct', 'seconds', 'item', 'skipped', 'exposure', 'served_why', 'source', 'lang', 'feedback_seconds', 'app_version', 'rule_card_before', 'task_role'], $rows);
    }

    /** What participants opened and pressed (Usage), and where each session was started; pseudonymised like the other files. */
    public static function events(): string
    {
        $rows = [];
        foreach (self::participants() as $u) {
            $start = self::dayOf((int) $u['research_at']);
            $pid = self::pid((int) $u['id']);
            foreach (Db::all('SELECT ev, detail, created_at FROM events WHERE user_id = ? AND created_at >= ? ORDER BY id', [(int) $u['id'], (int) $u['research_at']]) as $e) {
                $t = (new DateTime('@' . $e['created_at']))->setTimezone(Stats::tz());
                $rows[] = [$pid, self::between($start, $t->format('Y-m-d')), (int) $t->format('N'), (int) $t->format('G'), $t->format('i'), $e['ev'], $e['detail'] ?? ''];
            }
            foreach (Db::all('SELECT source, mode, state, n, started_at FROM psessions WHERE user_id = ? AND started_at >= ? ORDER BY id', [(int) $u['id'], (int) $u['research_at']]) as $p) {
                $t = (new DateTime('@' . $p['started_at']))->setTimezone(Stats::tz());
                $rows[] = [$pid, self::between($start, $t->format('Y-m-d')), (int) $t->format('N'), (int) $t->format('G'), $t->format('i'), 'session_start', Usage::sourceOf($p) . ':' . (int) $p['n']];
            }
        }
        usort($rows, fn($a, $b) => [$a[0], $a[1], $a[3], $a[4]] <=> [$b[0], $b[1], $b[3], $b[4]]);
        return self::csv(['pid', 'study_day', 'weekday', 'hour', 'minute', 'event', 'detail'], $rows);
    }

    /** Plain-text description of the files, for the methods section. */
    public static function codebook(): string
    {
        $now = (new DateTime('now', Stats::tz()))->format('Y-m-d H:i');
        $n = count(self::participants());
        return <<<TXT
English Fever practice app: research export
Created: {$now} ({$n} participants now in the study)

WHO IS IN THE FILES
All registered learners, with all their data from registration, except those who pressed "I do not agree to take part in the study"
(Profile → Your data → Research). Guests, teachers and test accounts are not included. Someone who says no disappears from the next export.
There are no random conditions: everyone sees the same app (decided 5 November 2026).
A learner who deletes their account disappears from the next export as well.

IDENTITY AND DATES
pid            12-character code for one learner, the same in every file and every export. It is a keyed hash made on the server; the key is
               stored in the app database, so the code cannot be turned back into a person without access to that database.
               The files contain no names, nicknames, e-mail addresses or the learners' own typed answers.
study_day      Whole days since registration (day 0 = the day of registration). Calendar dates are not included.
weekday        1 = Monday ... 7 = Sunday (Riga time).    hour   0-23 (Riga time).
join_week      ISO week of registration (coarse cohort marker); consent_week is the same week (kept for older scripts).

people.csv   (one row per learner)
explanations_lv       1 if the learner uses Latvian grammar explanations (current setting).
avatar_chosen         1 if the learner picked an avatar themselves.   board_opt_in   1 if the learner chose to appear on the leaderboard (current setting).
observed_days         Days from registration to the day of export, counting both. Use it to avoid counting a late joiner as a drop-out.
active_days           Number of days with at least one answered task.
answers, seconds, xp  Totals since registration. seconds = active time recorded by the app (0 if the learner turned time tracking off on the website);
correct_pct           Share of correct answers since registration.
sessions, sessions_smart   Practice sessions with at least one answer; how many of them were "Surprise me".
placement_level       Overall level from the latest placement test (any time since registration).
first_active_day, last_active_day   study_day of first and last day with an answer.
longest_streak        Longest run of consecutive active days.
weeks_active          Number of 7-day blocks since registration (days 0-6, 7-13, ...) with at least one active day.
active_day1/7/30      1 if the learner answered at least one task exactly on study day 1 / 7 / 30. Only meaningful when observed_days is above 1 / 7 / 30.

days.csv     (one row per learner and day with activity; a missing day means no activity)
seconds, answers, xp for that day.

answers.csv  (one row per answered task)
mode         practice, placement or smart ("Surprise me").   skill, area, level, bloom: the task's topic, area, CEFR sub-level and thinking level (1-6).
correct      1 or 0.   seconds   time to answer.   item   task id (for item analysis; -r2, -r3 = a corrected version).
skipped      1 = "I don't know" (counted as wrong in correct).
             The columns below are recorded from 1 November 2026; older rows have them empty.
exposure     1 = the first time this learner met this task, 2 = the second time ... (use exposure 1 for learning curves).
served_why   new | again_after_wrong (the task came back after a mistake) | again_after_right (no new task was left) |
             second_chance | bonus.
source       where the session was started (as in events.csv).   lang   explanation language set then (en / lv).
feedback_seconds  time from the feedback to Next on this task (reading the explanation); empty for the last task of a session.
app_version  the app version then; content and rules change between versions (docs/CHANGELOG-practice-app.md).
task_role    learn (can be solved from the meaning: not evidence of the form) | check (depends on the form) | use (the learner writes it).
rule_card_before  1 = the learner opened the rule card (the ? button) during this task, before answering; from 2 November 2026.

events.csv   (one row per logged action; from 28 October 2026)
event        page, rule_card, lang, skip, quit, review, report, sound, mood, path_step, bonus, or session_start.
detail       a page name or topic id; for session_start: where it was started (placement, path, path_check, surprise,
             second_chance, home_topic, practice_page, rule_card; older sessions: placement, second_chance and surprise are known, the rest is unknown) and the number of answers.

NOTES
Learners chose to join, so the sample is self-selected. Assignment to conditions is random only among those who joined.
The data are pseudonymised, not anonymous: the owner of the database can link a code to a person. Treat the files as personal data.
TXT;
    }
}
