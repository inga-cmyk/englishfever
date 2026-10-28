<?php
/**
 * What learners open and press (teacher, 28 October; docs/USAGE.md): where each session was started, and a short log of
 * named actions (a page opened, a rule card opened, Skip, Quit ...). Only a fixed list of names and a short detail
 * (a topic id, a page name) is stored: never text the learner typed.
 */
final class Usage
{
    /** Where a session can be started. */
    public const SOURCES = ['placement', 'path', 'path_check', 'surprise', 'second_chance', 'home_topic', 'practice_page', 'rule_card'];

    /** Actions that may be logged, with a short meaning for the teacher page. */
    public const EVENTS = [
        'page' => 'Opened a page',
        'rule_card' => 'Opened a rule card',
        'lang' => 'Changed the explanation language',
        'skip' => 'Skipped a task',
        'quit' => 'Quit a session',
        'review' => 'Looked back at an earlier task',
        'report' => 'Reported a problem',
        'sound' => 'Turned sound on or off',
        'mood' => 'Chose a mood saying',
        'path_step' => 'Opened a step on My learning path',
        'bonus' => 'Took the Second Chance bonus',
    ];
    private const DAY_CAP = 2000;   // per learner per day: a page that loops cannot fill the table

    /** @param array $events [[ev, detail], ...] sent in one batch by the page */
    public static function record(int $uid, array $events): int
    {
        if (!$events) return 0;
        $today = (int) Db::val('SELECT COUNT(1) FROM events WHERE user_id = ? AND created_at > ?', [$uid, time() - 86400]);
        $n = 0;
        foreach (array_slice($events, 0, 50) as $e) {
            if ($today + $n >= self::DAY_CAP) break;
            $ev = is_array($e) ? (string) ($e[0] ?? '') : '';
            if (!isset(self::EVENTS[$ev])) continue;
            $detail = is_array($e) && isset($e[1]) ? preg_replace('/[^a-z0-9_\-]/', '', strtolower((string) $e[1])) : '';
            Db::insert('events', ['user_id' => $uid, 'ev' => $ev, 'detail' => $detail !== '' ? substr($detail, 0, 40) : null, 'created_at' => time()]);
            $n++;
        }
        return $n;
    }

    /** Teacher page: how sessions are started and what is used, over the last $days days (students only). */
    public static function summary(int $days): array
    {
        $since = time() - $days * 86400;
        $sources = [];
        foreach (Db::all("SELECT COALESCE(p.source, CASE WHEN p.mode = 'placement' THEN 'placement' WHEN p.state LIKE '%\"comeback\":true%' THEN 'second_chance' WHEN p.state LIKE '%\"smart\":true%' THEN 'surprise' ELSE 'unknown' END) AS src,
                                 COUNT(1) AS n, COUNT(DISTINCT p.user_id) AS people, SUM(p.n) AS answers
                          FROM psessions p JOIN users u ON u.id = p.user_id WHERE u.role = 'student' AND p.started_at >= ? GROUP BY src ORDER BY n DESC", [$since]) as $r) {
            $sources[] = ['source' => $r['src'], 'sessions' => (int) $r['n'], 'people' => (int) $r['people'], 'answers' => (int) $r['answers']];
        }
        $events = [];
        foreach (Db::all("SELECT e.ev, e.detail, COUNT(1) AS n, COUNT(DISTINCT e.user_id) AS people FROM events e JOIN users u ON u.id = e.user_id
                          WHERE u.role = 'student' AND e.created_at >= ? GROUP BY e.ev, e.detail ORDER BY n DESC LIMIT 200", [$since]) as $r) {
            $events[] = ['ev' => $r['ev'], 'label' => self::EVENTS[$r['ev']] ?? $r['ev'], 'detail' => $r['detail'], 'count' => (int) $r['n'], 'people' => (int) $r['people']];
        }
        $people = [];
        foreach (Db::all("SELECT u.id, u.nickname, COALESCE(p.source, CASE WHEN p.mode = 'placement' THEN 'placement' WHEN p.state LIKE '%\"comeback\":true%' THEN 'second_chance' WHEN p.state LIKE '%\"smart\":true%' THEN 'surprise' ELSE 'unknown' END) AS src, COUNT(1) AS n
                          FROM psessions p JOIN users u ON u.id = p.user_id WHERE u.role = 'student' AND p.started_at >= ? GROUP BY u.id, u.nickname, src", [$since]) as $r) {
            $id = (int) $r['id'];
            $people[$id] ??= ['id' => $id, 'nickname' => $r['nickname'], 'sources' => [], 'events' => 0];
            $people[$id]['sources'][$r['src']] = (int) $r['n'];
        }
        foreach (Db::all("SELECT e.user_id, COUNT(1) AS n FROM events e JOIN users u ON u.id = e.user_id WHERE u.role = 'student' AND e.created_at >= ? GROUP BY e.user_id", [$since]) as $r) {
            if (isset($people[(int) $r['user_id']])) $people[(int) $r['user_id']]['events'] = (int) $r['n'];
        }
        usort($people, fn($a, $b) => array_sum($b['sources']) <=> array_sum($a['sources']));
        return ['days' => $days, 'sources' => $sources, 'events' => $events, 'people' => array_values($people), 'source_names' => self::SOURCES];
    }

    /** Where a session was started; sessions from before 28 October: placement, Second Chance and Surprise me are known from the saved state. */
    public static function sourceOf(array $p): string
    {
        if (!empty($p['source'])) return $p['source'];
        if ($p['mode'] === 'placement') return 'placement';
        $st = (string) ($p['state'] ?? '');
        if (str_contains($st, '"comeback":true')) return 'second_chance';
        if (str_contains($st, '"smart":true')) return 'surprise';
        return 'unknown';
    }

    /** Every logged action of students, oldest first (for the teacher; the research export has its own pseudonymised file). */
    public static function export(): string
    {
        $fh = fopen('php://temp', 'w+');
        fputcsv($fh, ['time', 'nickname', 'event', 'detail'], ',', '"', '\\');
        foreach (Db::all("SELECT e.created_at, u.nickname, e.ev, e.detail FROM events e JOIN users u ON u.id = e.user_id WHERE u.role = 'student' ORDER BY e.id") as $r) {
            $t = (new DateTime('@' . $r['created_at']))->setTimezone(Stats::tz())->format('Y-m-d H:i:s');
            fputcsv($fh, [$t, Stats::csvCell((string) $r['nickname']), $r['ev'], $r['detail'] ?? ''], ',', '"', '\\');
        }
        fputcsv($fh, [], ',', '"', '\\');
        fputcsv($fh, ['session started', 'nickname', 'source', 'mode', 'answers'], ',', '"', '\\');
        foreach (Db::all("SELECT p.started_at, u.nickname, p.source, p.mode, p.state, p.n FROM psessions p JOIN users u ON u.id = p.user_id WHERE u.role = 'student' ORDER BY p.id") as $r) {
            $t = (new DateTime('@' . $r['started_at']))->setTimezone(Stats::tz())->format('Y-m-d H:i:s');
            fputcsv($fh, [$t, Stats::csvCell((string) $r['nickname']), self::sourceOf($r), $r['mode'], (int) $r['n']], ',', '"', '\\');
        }
        rewind($fh);
        return (string) stream_get_contents($fh);
    }
}
