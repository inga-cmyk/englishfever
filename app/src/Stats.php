<?php
// Activity, streaks, dashboard, leaderboard and the teacher's views.

final class Stats
{
    public static function tz(): DateTimeZone
    {
        return new DateTimeZone(Config::get('timezone', 'Europe/Riga'));
    }

    public static function today(): string
    {
        return (new DateTime('now', self::tz()))->format('Y-m-d');
    }

    public static function dayOffset(int $days): string
    {
        $d = new DateTime('now', self::tz());
        $d->modify(($days >= 0 ? '+' : '') . $days . ' day');
        return $d->format('Y-m-d');
    }

    public static function weekStart(): string
    {
        $d = new DateTime('now', self::tz());
        $d->modify('monday this week');
        return $d->format('Y-m-d');
    }

    public static function addActivity(int $uid, int $seconds, int $answers, int $xp): void
    {
        $day = self::today();
        $row = Db::one('SELECT seconds FROM activity WHERE user_id = ? AND day = ?', [$uid, $day]);
        if ($row) {
            Db::q('UPDATE activity SET seconds = seconds + ?, answers = answers + ?, xp = xp + ? WHERE user_id = ? AND day = ?', [$seconds, $answers, $xp, $uid, $day]);
        } else {
            try {
                Db::insert('activity', ['user_id' => $uid, 'day' => $day, 'seconds' => $seconds, 'answers' => $answers, 'xp' => $xp]);
            } catch (PDOException $e) { // two requests at once: the row now exists
                Db::q('UPDATE activity SET seconds = seconds + ?, answers = answers + ?, xp = xp + ? WHERE user_id = ? AND day = ?', [$seconds, $answers, $xp, $uid, $day]);
            }
        }
    }

    public static function streak(int $uid): array
    {
        $days = array_column(Db::all('SELECT day FROM activity WHERE user_id = ? AND answers > 0 ORDER BY day DESC', [$uid]), 'day');
        if (!$days) return ['current' => 0, 'best' => 0, 'today_done' => false];
        $set = array_flip($days);
        $today = self::today();
        $todayDone = isset($set[$today]);
        $cursor = $todayDone ? $today : self::dayOffset(-1);
        $cur = 0;
        while (isset($set[$cursor])) {
            $cur++;
            $d = new DateTime($cursor, self::tz());
            $d->modify('-1 day');
            $cursor = $d->format('Y-m-d');
        }
        $best = 0;
        $run = 0;
        $prev = null;
        foreach (array_reverse($days) as $day) {
            if ($prev !== null) {
                $p = new DateTime($prev, self::tz());
                $p->modify('+1 day');
                $run = ($p->format('Y-m-d') === $day) ? $run + 1 : 1;
            } else {
                $run = 1;
            }
            $best = max($best, $run);
            $prev = $day;
        }
        return ['current' => $cur, 'best' => max($best, $cur), 'today_done' => $todayDone];
    }

    private static function skillRows(int $uid): array
    {
        $have = [];
        foreach (Db::all('SELECT skill, theta, n, n_correct, updated_at FROM skill_state WHERE user_id = ?', [$uid]) as $r) $have[$r['skill']] = $r;
        $out = [];
        foreach (Content::liveMeta()['skills'] as $s) {
            $r = $have[$s['id']] ?? null;
            $n = $r ? (int) $r['n'] : 0;
            $out[] = [
                'id' => $s['id'], 'label' => $s['label'], 'area' => $s['area'], 'levels' => $s['levels'],
                'n' => $n, 'correct' => $r ? (int) $r['n_correct'] : 0, 'last' => $r ? (int) $r['updated_at'] : 0,
                'accuracy' => $n ? round(100 * $r['n_correct'] / $n) : null,
                'theta' => $r ? round((float) $r['theta'], 2) : null,
                'level_est' => ($r && $n >= 3) ? Content::levelFromTheta((float) $r['theta'], $s['levels']) : null,
            ];
        }
        return $out;
    }

    private static function bloomRows(int $uid): array
    {
        $out = [];
        foreach (Db::all('SELECT bloom, COUNT(1) AS n, SUM(correct) AS c FROM attempts WHERE user_id = ? GROUP BY bloom', [$uid]) as $r) {
            $out[(string) $r['bloom']] = ['n' => (int) $r['n'], 'correct' => (int) $r['c']];
        }
        ksort($out);
        return $out;
    }

    /**
     * How many learners are practising: "now" = answered a question in the last 10 minutes, "today" = answered one today (Riga calendar day).
     * Learners and guests, never teachers; only counts, kept for a minute.
     */
    public static function pulse(): array
    {
        $c = json_decode((string) Db::kvGet('pulse'), true);
        $today = self::today();
        if (is_array($c) && $c['day'] === $today && time() - (int) $c['at'] < 60) return ['now' => (int) $c['now'], 'today' => (int) $c['today']];
        $now = (int) Db::val("SELECT COUNT(DISTINCT a.user_id) FROM attempts a JOIN users u ON u.id = a.user_id WHERE u.role = 'student' AND a.created_at > ?", [time() - 600]);
        $day = (int) Db::val("SELECT COUNT(DISTINCT a.user_id) FROM activity a JOIN users u ON u.id = a.user_id WHERE u.role = 'student' AND a.day = ? AND a.answers > 0", [$today]);
        Db::kvSet('pulse', json_encode(['at' => time(), 'day' => $today, 'now' => $now, 'today' => $day]));
        return ['now' => $now, 'today' => $day];
    }

    public static function dashboard(int $uid): array
    {
        $today = self::today();
        $t = Db::one('SELECT seconds, answers, xp FROM activity WHERE user_id = ? AND day = ?', [$uid, $today]) ?: ['seconds' => 0, 'answers' => 0, 'xp' => 0];
        $tot = Db::one('SELECT COALESCE(SUM(seconds),0) AS s, COALESCE(SUM(answers),0) AS a, COALESCE(SUM(xp),0) AS x FROM activity WHERE user_id = ?', [$uid]);
        $acc = Db::one('SELECT COUNT(1) AS n, COALESCE(SUM(correct),0) AS c FROM attempts WHERE user_id = ?', [$uid]);
        $week = [];
        $rows = [];
        foreach (Db::all('SELECT day, seconds, answers, xp FROM activity WHERE user_id = ? AND day >= ?', [$uid, self::dayOffset(-6)]) as $r) $rows[$r['day']] = $r;
        for ($i = 6; $i >= 0; $i--) {
            $d = self::dayOffset(-$i);
            $week[] = ['day' => $d, 'seconds' => (int) ($rows[$d]['seconds'] ?? 0), 'answers' => (int) ($rows[$d]['answers'] ?? 0)];
        }
        $placement = null;
        $pr = Db::one("SELECT state, ended_at FROM psessions WHERE user_id = ? AND mode = 'placement' AND ended_at IS NOT NULL ORDER BY id DESC LIMIT 1", [$uid]);
        if ($pr) {
            $st = json_decode($pr['state'], true);
            if (!empty($st['report'])) $placement = ['at' => (int) $pr['ended_at'], 'report' => $st['report']];
        }
        return [
            'today' => ['seconds' => (int) $t['seconds'], 'answers' => (int) $t['answers'], 'xp' => (int) $t['xp']],
            'totals' => ['seconds' => (int) $tot['s'], 'answers' => (int) $tot['a'], 'xp' => (int) $tot['x'],
                'accuracy' => $acc['n'] ? round(100 * $acc['c'] / $acc['n']) : null],
            'streak' => self::streak($uid),
            'week' => $week,
            'skills' => self::skillRows($uid),
            'bloom' => self::bloomRows($uid),
            'placement' => $placement,
            'pulse' => self::pulse(),
            'comeback' => (function () use ($uid) { $m = Mistakes::scan($uid); return ['open' => count($m['open']), 'fixed' => $m['fixed'], 'review' => min(2, count(Mistakes::reviewDue($uid, $m)))]; })(),
        ];
    }

    /** The expected answer of a task, in one line (teacher's view of a wrong answer). */
    public static function answerKey(array $it): string
    {
        switch ($it['kind']) {
            case 'mcq': return (string) $it['correct'];
            case 'gap': return implode(' … ', array_map(fn($a) => (string) $a[0], $it['answers']));
            case 'text': return (string) ($it['answers'][0][0] ?? '');
            case 'order': return (string) $it['sentence'];
            case 'match': return implode(' | ', array_map(fn($p) => $p[0] . ' → ' . $p[1], $it['pairs']));
            case 'write': return (string) ($it['model'] ?? '');
        }
        return '';
    }

    public static function leaderboard(int $uid, string $period): array
    {
        $where = "u.show_on_board = 1 AND u.role = 'student' AND u.provider <> 'guest' AND u.board_hidden = 0" . Research::leaderboardClause();
        $p = [];
        if ($period === 'week') {
            $where .= ' AND a.day >= ?';
            $p[] = self::weekStart();
        }
        $rows = Db::all("SELECT u.id, u.nickname, u.avatar, u.mood, SUM(a.xp) AS pts, SUM(a.seconds) AS secs
                         FROM activity a JOIN users u ON u.id = a.user_id
                         WHERE $where GROUP BY u.id, u.nickname, u.avatar, u.mood HAVING SUM(a.xp) > 0
                         ORDER BY pts DESC, u.nickname ASC LIMIT 50", $p);
        $out = [];
        $me = null;
        foreach ($rows as $i => $r) {
            $row = ['rank' => $i + 1, 'nickname' => $r['nickname'], 'avatar' => Auth::effectiveAvatar($r['avatar'], (int) $r['id']), 'xp' => (int) $r['pts'], 'minutes' => (int) round($r['secs'] / 60), 'mood' => Auth::validMood($r['mood'] ?? null), 'me' => (int) $r['id'] === $uid];
            if ($row['me']) $me = $row;
            if ($i < 20) $out[] = $row;
        }
        $u = Db::one('SELECT show_on_board, role, provider FROM users WHERE id = ?', [$uid]);
        return [
            'period' => $period, 'rows' => $out, 'me' => $me,
            'hidden' => $u && (!(int) $u['show_on_board'] || $u['role'] !== 'student'),
            'guest' => $u && $u['provider'] === 'guest',
            'week_start' => self::weekStart(),
        ];
    }

    // ───────── teacher ─────────

    /** Which learners belong to this teacher: enrolled in their Tutor courses ('course') or added by hand ('added'). */
    private static function mineMap(int $teacherId): array
    {
        $t = $teacherId ? Db::one('SELECT provider, external_id FROM users WHERE id = ?', [$teacherId]) : null;
        $roster = ($t && $t['provider'] === 'wp') ? Wp::roster((int) $t['external_id']) : null;
        $manual = [];
        foreach (Db::all('SELECT student_id FROM teacher_mine WHERE teacher_id = ?', [$teacherId]) as $r) $manual[(int) $r['student_id']] = true;
        return [$roster === null ? null : array_flip($roster), $manual];
    }

    private static function mineState(array $map, array $u): ?string
    {
        if (isset($map[1][(int) $u['id']])) return 'added';
        if ($u['provider'] === 'wp' && $map[0] !== null && isset($map[0][(int) $u['external_id']])) return 'course';
        return null;
    }

    public static function teacherStudents(int $teacherId = 0): array
    {
        $users = Db::all("SELECT id, provider, external_id, nickname, avatar, full_name, created_at, last_seen FROM users WHERE role = 'student' ORDER BY nickname");
        $map = self::mineMap($teacherId);
        $act = [];
        $weekStart = self::weekStart();
        foreach (Db::all('SELECT user_id, SUM(seconds) AS s, SUM(answers) AS a, SUM(xp) AS x FROM activity GROUP BY user_id') as $r) $act[$r['user_id']] = $r;
        $wk = [];
        foreach (Db::all('SELECT user_id, SUM(seconds) AS s, SUM(answers) AS a FROM activity WHERE day >= ? GROUP BY user_id', [$weekStart]) as $r) $wk[$r['user_id']] = $r;
        $acc = [];
        foreach (Db::all('SELECT user_id, COUNT(1) AS n, SUM(correct) AS c FROM attempts GROUP BY user_id') as $r) $acc[$r['user_id']] = $r;
        $th = [];
        foreach (Db::all('SELECT user_id, SUM(theta * n) AS tn, SUM(n) AS n FROM skill_state GROUP BY user_id') as $r) $th[$r['user_id']] = $r;
        $pl = [];   // the latest placement result of each learner, with its date
        foreach (Db::all("SELECT user_id, state, ended_at FROM psessions WHERE mode = 'placement' AND ended_at IS NOT NULL ORDER BY id") as $r) {
            $lv = json_decode((string) $r['state'], true)['report']['overall_level'] ?? null;
            if ($lv) $pl[$r['user_id']] = ['level' => $lv, 'at' => (int) $r['ended_at']];
        }
        $out = [];
        foreach ($users as $u) {
            $id = $u['id'];
            $level = null;
            if (!empty($th[$id]) && $th[$id]['n'] >= 5) $level = Content::levelFromTheta($th[$id]['tn'] / $th[$id]['n']);
            $out[] = [
                'id' => (int) $id, 'nickname' => $u['nickname'], 'avatar' => Auth::effectiveAvatar($u['avatar'], (int) $u['id']), 'full_name' => $u['full_name'], 'provider' => $u['provider'],
                'joined' => (int) $u['created_at'], 'last_seen' => (int) $u['last_seen'],
                'week_minutes' => (int) round(($wk[$id]['s'] ?? 0) / 60), 'week_answers' => (int) ($wk[$id]['a'] ?? 0),
                'total_minutes' => (int) round(($act[$id]['s'] ?? 0) / 60), 'total_answers' => (int) ($act[$id]['a'] ?? 0),
                'xp' => (int) ($act[$id]['x'] ?? 0),
                'accuracy' => !empty($acc[$id]['n']) ? round(100 * $acc[$id]['c'] / $acc[$id]['n']) : null,
                'streak' => self::streak((int) $id)['current'],
                'level_est' => $level,
                'placement_level' => $pl[$id]['level'] ?? null, 'placement_at' => $pl[$id]['at'] ?? null,
                'mine' => self::mineState($map, $u),
            ];
        }
        return ['students' => $out, 'roster_ok' => $map[0] !== null];
    }

    public static function teacherStudent(int $id, int $teacherId = 0): array
    {
        $u = Db::one("SELECT id, provider, external_id, nickname, avatar, full_name, created_at, last_seen, show_on_board, board_hidden FROM users WHERE id = ? AND role = 'student'", [$id]);
        if (!$u) throw new ApiError('Student not found.', 404);
        $dash = self::dashboard($id);
        $days = [];
        $rows = [];
        foreach (Db::all('SELECT day, seconds, answers, xp FROM activity WHERE user_id = ? AND day >= ?', [$id, self::dayOffset(-29)]) as $r) $rows[$r['day']] = $r;
        for ($i = 29; $i >= 0; $i--) {
            $d = self::dayOffset(-$i);
            $days[] = ['day' => $d, 'minutes' => (int) round(($rows[$d]['seconds'] ?? 0) / 60), 'answers' => (int) ($rows[$d]['answers'] ?? 0)];
        }
        $recent = [];
        foreach (Db::all('SELECT item_id, skill, level, bloom, correct, answer, time_ms, created_at FROM attempts WHERE user_id = ? ORDER BY id DESC LIMIT 60', [$id]) as $r) {
            $it = Content::item($r['item_id']);
            $recent[] = [
                'at' => (int) $r['created_at'], 'skill' => $r['skill'], 'level' => $r['level'], 'bloom' => (int) $r['bloom'],
                'correct' => (bool) $r['correct'], 'answer' => $r['answer'], 'seconds' => (int) round($r['time_ms'] / 1000),
                'q' => $it['q'] ?? $r['item_id'], 'id' => $r['item_id'],
                'key' => !$r['correct'] && $it ? self::answerKey($it) : null,   // teachers only: what was expected
            ];
        }
        $sessions = [];
        foreach (Db::all('SELECT id, mode, level, n, n_correct, xp, started_at, ended_at FROM psessions WHERE user_id = ? AND n > 0 ORDER BY id DESC LIMIT 20', [$id]) as $r) {
            $sessions[] = ['mode' => $r['mode'], 'level' => $r['level'], 'n' => (int) $r['n'], 'correct' => (int) $r['n_correct'], 'xp' => (int) $r['xp'], 'at' => (int) $r['started_at']];
        }
        return [
            'user' => ['id' => (int) $u['id'], 'nickname' => $u['nickname'], 'avatar' => Auth::effectiveAvatar($u['avatar'], (int) $u['id']), 'full_name' => $u['full_name'], 'provider' => $u['provider'],
                'joined' => (int) $u['created_at'], 'last_seen' => (int) $u['last_seen'], 'board_hidden' => (bool) $u['board_hidden'],
                'mine' => self::mineState(self::mineMap($teacherId), $u)],
            'dashboard' => $dash, 'days' => $days, 'recent' => $recent, 'sessions' => $sessions,
        ];
    }

    /** @param string $view all | registered | mine (what the teacher has selected in the list) */
    public static function exportAttempts(string $view = 'all', int $teacherId = 0): string
    {
        $only = null;
        if ($view === 'registered' || $view === 'mine') {
            $only = [];
            foreach (self::teacherStudents($teacherId)['students'] as $s) {
                if ($view === 'mine' ? $s['mine'] !== null : $s['provider'] !== 'guest') $only[$s['id']] = true;
            }
        }
        $fh = fopen('php://temp', 'w+');
        fputcsv($fh, ['time', 'nickname', 'name', 'account', 'skill', 'level', 'bloom', 'correct', 'answer', 'seconds', 'item'], ',', '"', '\\');
        $users = [];
        foreach (Db::all('SELECT id, nickname, full_name, provider FROM users') as $u) $users[$u['id']] = $u;
        foreach (Db::all('SELECT * FROM attempts ORDER BY id') as $a) {
            if ($only !== null && !isset($only[(int) $a['user_id']])) continue;
            $u = $users[$a['user_id']] ?? ['nickname' => '?', 'full_name' => '', 'provider' => '?'];
            $cell = fn($v) => preg_match('/^[=+\-@]/', (string) $v) ? "'" . $v : $v; // stop spreadsheet formula injection
            fputcsv($fh, [
                (new DateTime('@' . $a['created_at']))->setTimezone(self::tz())->format('Y-m-d H:i:s'),
                $cell($u['nickname']), $cell($u['full_name']), $u['provider'] === 'guest' ? 'guest' : 'registered', $a['skill'], $a['level'], $a['bloom'], $a['correct'],
                $cell($a['answer']), round($a['time_ms'] / 1000), $a['item_id'],
            ], ',', '"', '\\');
        }
        rewind($fh);
        return stream_get_contents($fh);
    }
}
