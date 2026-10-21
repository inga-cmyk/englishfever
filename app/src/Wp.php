<?php
// Link to the englishfever.com "My activity" tracker (plugin ef-practice-sso).
//
// App -> website: daily practice totals for registered students, signed with a key derived from sso_secret.
//   The website decides whether the student agreed to tracking and writes the row into wp_ef_aktivitate.
// Website -> app: a signed request for one student's practice summary (shown by [ef_practice_results]).

final class Wp
{
    private const KEEP_DAYS = 14;        // only recent days are ever sent
    private const MAX_DAY_SECONDS = 14400; // 4 hours, like the tracker's own cap
    private const MIN_GAP = 60;          // seconds between syncs of one student

    public static function configured(): bool
    {
        $s = (string) Config::get('sso_secret', '');
        return Config::get('wp_sync_url', '') !== '' && strlen($s) >= 32 && $s !== 'CHANGE-ME';
    }

    private static function key(): string
    {
        return hash_hmac('sha256', 'ef-tracker-v1', (string) Config::get('sso_secret', ''));
    }

    public static function sign(string $time, string $body): string
    {
        return hash_hmac('sha256', $time . '.' . $body, self::key());
    }

    public static function verify(string $time, string $body, string $sig): bool
    {
        if (!ctype_digit($time) || abs(time() - (int) $time) > 120) return false;
        return hash_equals(self::sign($time, $body), $sig);
    }

    /** Days (recent) whose totals differ from what the website last received. */
    public static function pending(int $uid): array
    {
        return Db::all(
            'SELECT a.day, a.seconds, a.answers, COALESCE(s.base_seconds, 0) AS base FROM activity a
             LEFT JOIN sync_wp s ON s.user_id = a.user_id AND s.day = a.day
             WHERE a.user_id = ? AND a.day >= ? AND (a.seconds > 0 OR a.answers > 0)
               AND (s.day IS NULL OR s.seconds <> a.seconds OR s.answers <> a.answers)
             ORDER BY a.day',
            [$uid, Stats::dayOffset(-self::KEEP_DAYS)]
        );
    }

    /** Send the pending days of one student. Returns a short status string. */
    public static function syncUser(int $uid, bool $force = false): string
    {
        if (!self::configured()) return 'not configured';
        $u = Db::one('SELECT id, provider, role, external_id, track_time FROM users WHERE id = ?', [$uid]);
        if (!$u || $u['provider'] !== 'wp' || $u['role'] !== 'student' || !(int) $u['track_time']) return 'skipped';
        $last = (int) (Db::kvGet('sync_last:' . $uid) ?? 0);
        if (!$force && time() - $last < self::MIN_GAP) return 'throttled';
        $days = self::pending($uid);
        if (!$days) return 'nothing to send';
        Db::kvSet('sync_last:' . $uid, (string) time());

        $send = [];
        foreach ($days as $d) {
            // time recorded before the student opted out (base) is never sent, even if they opt in again the same day
            $secs = max(0, (int) $d['seconds'] - (int) $d['base']);
            if ((int) $d['answers'] > 0 && $secs < 30) $secs = 30; // a day with practice counts as an active day
            $send[] = ['day' => $d['day'], 'seconds' => min(self::MAX_DAY_SECONDS, $secs), 'answers' => (int) $d['answers']];
        }
        $body = json_encode(['user' => (int) $u['external_id'], 'days' => $send]);
        [$code, $resp, $err] = self::post((string) Config::get('wp_sync_url'), $body);
        if ($code !== 200) {
            $msg = $err ?: ('website answered ' . $code . ' ' . mb_substr(trim(strip_tags((string) $resp)), 0, 160));
            Db::kvSet('wp_sync_last_error', date('Y-m-d H:i:s') . ' – ' . $msg);
            return 'error: ' . $msg;
        }
        $res = json_decode((string) $resp, true);
        if (!is_array($res) || !isset($res['results']) || !is_array($res['results'])) {
            Db::kvSet('wp_sync_last_error', date('Y-m-d H:i:s') . ' – unexpected answer from the website');
            return 'error: unexpected answer';
        }
        foreach ($days as $d) {
            $status = $res['results'][$d['day']] ?? null;
            if (!in_array($status, ['recorded', 'no_consent', 'skipped'], true)) continue;
            // remember what was handled. For no_consent the whole day so far becomes the base that is never sent,
            // so a later "yes" does not back-fill time from before the student opted out.
            $base = $status === 'no_consent' ? (int) $d['seconds'] : (int) $d['base'];
            if (Db::val('SELECT COUNT(1) FROM sync_wp WHERE user_id = ? AND day = ?', [$uid, $d['day']])) {
                Db::q('UPDATE sync_wp SET seconds = ?, answers = ?, base_seconds = ?, synced_at = ? WHERE user_id = ? AND day = ?', [$d['seconds'], $d['answers'], $base, time(), $uid, $d['day']]);
            } else {
                Db::insert('sync_wp', ['user_id' => $uid, 'day' => $d['day'], 'seconds' => (int) $d['seconds'], 'answers' => (int) $d['answers'], 'base_seconds' => $base, 'synced_at' => time()]);
            }
            if ($status === 'no_consent') Db::q('UPDATE users SET track_time = 0 WHERE id = ?', [$uid]);
        }
        Db::kvSet('wp_sync_last_ok', (string) time());
        Db::kvSet('wp_sync_last_error', null);
        return 'ok';
    }

    /** All students with something to send (used by bin/sync-wp.php, for a cron job). */
    public static function syncPending(int $maxSeconds = 25): array
    {
        $out = ['users' => 0, 'ok' => 0, 'errors' => 0];
        $start = time();
        $ids = Db::all("SELECT DISTINCT u.id FROM users u JOIN activity a ON a.user_id = u.id
                        WHERE u.provider = 'wp' AND u.role = 'student' AND u.track_time = 1 AND a.day >= ? AND (a.seconds > 0 OR a.answers > 0)", [Stats::dayOffset(-self::KEEP_DAYS)]);
        foreach ($ids as $r) {
            if (time() - $start > $maxSeconds) break;
            if (!self::pending((int) $r['id'])) continue;
            $out['users']++;
            $res = self::syncUser((int) $r['id'], true);
            if ($res === 'ok') $out['ok']++; elseif (strpos($res, 'error') === 0) $out['errors']++;
        }
        return $out;
    }

    /** Run the sync after the answer has been sent to the browser, so learners never wait for the website. */
    public static function afterResponse(int $uid, bool $force): void
    {
        if (!self::configured()) return;
        register_shutdown_function(function () use ($uid, $force) {
            if (function_exists('fastcgi_finish_request')) fastcgi_finish_request();
            elseif (function_exists('litespeed_finish_request')) litespeed_finish_request();
            try {
                self::syncUser($uid, $force);
            } catch (Throwable $e) {
                error_log('[practice] website sync failed: ' . $e->getMessage());
            }
        });
    }

    private static function post(string $url, string $body): array
    {
        $time = (string) time();
        $headers = ['Content-Type: application/json', 'X-EF-Time: ' . $time, 'X-EF-Sign: ' . self::sign($time, $body), 'User-Agent: EF-Practice/1'];
        if (function_exists('curl_init')) {
            $ch = curl_init($url);
            curl_setopt_array($ch, [CURLOPT_POST => true, CURLOPT_POSTFIELDS => $body, CURLOPT_HTTPHEADER => $headers,
                CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 6, CURLOPT_CONNECTTIMEOUT => 3, CURLOPT_FOLLOWLOCATION => false]);
            $resp = curl_exec($ch);
            $code = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
            $err = $resp === false ? curl_error($ch) : '';
            curl_close($ch);
            return [$code, $resp === false ? '' : $resp, $err];
        }
        $ctx = stream_context_create(['http' => ['method' => 'POST', 'header' => implode("\r\n", $headers), 'content' => $body, 'timeout' => 6, 'ignore_errors' => true]]);
        $resp = @file_get_contents($url, false, $ctx);
        $code = 0;
        if (isset($http_response_header[0]) && preg_match('~\s(\d{3})\s~', $http_response_header[0], $m)) $code = (int) $m[1];
        return [$code, $resp === false ? '' : $resp, $resp === false ? 'no connection to the website' : ''];
    }

    /**
     * WordPress ids of the students enrolled in this teacher's Tutor LMS courses (courses they wrote or teach).
     * Asked from the website, cached for 10 minutes, and the last known list is kept if the website cannot be reached.
     * Null when nothing is known (the sync address is not set, or the website never answered).
     */
    public static function roster(int $wpTeacherId): ?array
    {
        if (!self::configured() || $wpTeacherId < 1) return null;
        $k = 'roster:' . $wpTeacherId;
        $c = json_decode((string) Db::kvGet($k), true);
        if (is_array($c) && time() - (int) $c['at'] < 600) return $c['ids'];
        $url = (string) preg_replace('~/activity/?$~', '/roster', (string) Config::get('wp_sync_url', ''));
        if (substr($url, -7) === '/roster') {
            [$code, $resp] = self::post($url, json_encode(['teacher' => $wpTeacherId]));
            $j = json_decode((string) $resp, true);
            if ($code === 200 && is_array($j) && isset($j['students']) && is_array($j['students'])) {
                $ids = array_values(array_unique(array_map('intval', $j['students'])));
                Db::kvSet($k, json_encode(['at' => time(), 'ids' => $ids]));
                return $ids;
            }
        }
        return is_array($c) ? $c['ids'] : null;
    }

    // ───────── what the website shows ─────────

    public static function summary(int $wpUserId): array
    {
        $u = Db::one("SELECT id, track_time FROM users WHERE provider = 'wp' AND external_id = ? AND role = 'student'", [(string) $wpUserId]);
        if (!$u) return ['practice' => false];
        $uid = (int) $u['id'];
        $d = Stats::dashboard($uid);
        if ($d['totals']['answers'] < 1) return ['practice' => false];
        $skills = array_values(array_filter($d['skills'], fn($s) => $s['n'] >= 3 && $s['theta'] !== null));
        usort($skills, fn($a, $b) => $a['theta'] <=> $b['theta']);
        $weak = array_map(fn($s) => ['label' => $s['label'], 'level' => $s['level_est'], 'accuracy' => $s['accuracy']], array_slice($skills, 0, 3));
        $overall = null;
        $row = Db::one('SELECT SUM(theta * n) AS tn, SUM(n) AS n FROM skill_state WHERE user_id = ?', [$uid]);
        if ($row && (int) $row['n'] >= 5) $overall = Content::levelFromTheta((float) $row['tn'] / (float) $row['n']);
        $weekAnswers = 0;
        $weekSeconds = 0;
        foreach ($d['week'] as $w) { $weekAnswers += $w['answers']; $weekSeconds += $w['seconds']; }
        $track = (int) $u['track_time'] === 1;
        return [
            'practice' => true,
            'level' => $overall,
            'answers' => $d['totals']['answers'],
            'accuracy' => $d['totals']['accuracy'],
            'minutes' => $track ? (int) round($d['totals']['seconds'] / 60) : null,
            'week_minutes' => $track ? (int) round($weekSeconds / 60) : null,
            'week_answers' => $weekAnswers,
            'streak' => $d['streak']['current'],
            'weak' => $weak,
        ];
    }

    public static function status(): array
    {
        $pending = 0;
        if (self::configured()) {
            foreach (Db::all("SELECT id FROM users WHERE provider = 'wp' AND role = 'student' AND track_time = 1") as $r) {
                if (self::pending((int) $r['id'])) $pending++;
            }
        }
        return [
            'configured' => self::configured(),
            'last_ok' => (int) (Db::kvGet('wp_sync_last_ok') ?? 0),
            'last_error' => Db::kvGet('wp_sync_last_error'),
            'students_waiting' => $pending,
        ];
    }
}
