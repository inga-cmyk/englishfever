<?php
// "Report a problem": learners tell the teacher that a task looks wrong; the teacher reads the reports on the Reports page.
// One report per learner and task (reporting again updates it). Reports hold the learner's own answer, so only teachers read them.

final class Reports
{
    public const REASONS = [
        'unclear' => 'The question is unclear or has a mistake',
        'ambiguous' => 'More than one answer could be right',
        'my_answer' => 'My answer was right but was marked wrong',
        'key_wrong' => 'The correct answer shown is wrong',
        'explanation' => 'The explanation is wrong or confusing',
        'other' => 'Something else',
    ];
    public const STATUSES = ['new', 'seen', 'fixed', 'dismissed'];

    public static function save(array $u, string $itemId, string $reason, string $comment): void
    {
        if (!isset(self::REASONS[$reason])) throw new ApiError('Please choose what is wrong.', 400);
        if (!Content::item($itemId)) throw new ApiError('Task not found.', 404);
        $comment = trim(mb_substr(preg_replace('/\s+/u', ' ', $comment), 0, 400));
        // what the learner answered in this task, if they did
        $last = Db::one('SELECT answer, correct FROM attempts WHERE user_id = ? AND item_id = ? ORDER BY id DESC LIMIT 1', [$u['id'], $itemId]);
        $now = time();
        $row = ['reason' => $reason, 'comment' => $comment, 'answer' => $last['answer'] ?? null, 'correct' => $last ? (int) $last['correct'] : null, 'status' => 'new', 'updated_at' => $now];
        $have = Db::one('SELECT id FROM reports WHERE user_id = ? AND item_id = ?', [$u['id'], $itemId]);
        if ($have) Db::update('reports', $row, 'id = ?', [$have['id']]);
        else Db::insert('reports', $row + ['user_id' => (int) $u['id'], 'item_id' => $itemId, 'created_at' => $now]);
    }

    public static function openCount(): int
    {
        return (int) Db::val("SELECT COUNT(DISTINCT item_id) FROM reports WHERE status = 'new'");
    }

    public static function setStatus(string $itemId, string $status): void
    {
        if (!in_array($status, self::STATUSES, true)) throw new ApiError('Unknown status.', 400);
        if (!Db::one('SELECT id FROM reports WHERE item_id = ?', [$itemId])) throw new ApiError('No reports for this task.', 404);
        Db::q('UPDATE reports SET status = ? WHERE item_id = ?', [$status, $itemId]);
    }

    /** The task as the teacher needs to judge it: the text, the key and the wrong options. */
    private static function describe(string $id): array
    {
        $it = Content::item($id);
        if (!$it) return ['id' => $id, 'q' => '(this task is no longer in the bank)', 'skill' => '', 'level' => '', 'kind' => '', 'key' => '', 'options' => null];
        $key = '';
        $options = null;
        switch ($it['kind']) {
            case 'mcq': $key = $it['correct']; $options = $it['wrong']; break;
            case 'gap':
            case 'text': $key = implode(' / ', array_map(fn($b) => implode('  |  ', $b), $it['answers'])); break;
            case 'order': $key = $it['sentence']; break;
            case 'match': $key = implode('; ', array_map(fn($p) => $p[0] . ' = ' . $p[1], $it['pairs'])); break;
            case 'write': $key = $it['model'] ?? ''; break;
        }
        $skill = Content::skill($it['skill']);
        return ['id' => $it['id'], 'q' => $it['q'], 'skill' => $skill['label'] ?? $it['skill'], 'level' => $it['level'], 'kind' => $it['kind'], 'key' => $key, 'options' => $options];
    }

    /** Reports grouped by task. $filter: open (new + seen), fixed, dismissed, all. Also: tasks most learners get wrong. */
    public static function forTeacher(string $filter): array
    {
        $where = ''; $p = [];
        if ($filter === 'open') $where = "WHERE r.status IN ('new', 'seen')";
        elseif (in_array($filter, ['fixed', 'dismissed'], true)) { $where = 'WHERE r.status = ?'; $p[] = $filter; }
        else $filter = 'all';
        $rows = Db::all("SELECT r.*, u.nickname, u.provider FROM reports r LEFT JOIN users u ON u.id = r.user_id $where ORDER BY r.updated_at DESC", $p);
        $groups = [];
        foreach ($rows as $r) {
            $g = &$groups[$r['item_id']];
            if (!isset($g)) $g = ['task' => self::describe($r['item_id']), 'count' => 0, 'reasons' => [], 'status' => $r['status'], 'last' => (int) $r['updated_at'], 'reports' => []];
            $g['count']++;
            $g['reasons'][$r['reason']] = ($g['reasons'][$r['reason']] ?? 0) + 1;
            if ($r['status'] === 'new') $g['status'] = 'new';
            $g['reports'][] = [
                'reason' => $r['reason'], 'comment' => (string) $r['comment'], 'answer' => $r['answer'], 'correct' => $r['correct'] === null ? null : (int) $r['correct'],
                'at' => (int) $r['updated_at'], 'who' => $r['provider'] === 'guest' ? 'guest' : 'registered', 'status' => $r['status'],
            ];
            unset($g);
        }
        return [
            'filter' => $filter, 'reasons' => self::REASONS, 'open' => self::openCount(),
            'groups' => array_values($groups),
            'hard' => self::hard(),
        ];
    }

    /** Tasks answered at least 8 times in the last 60 days with 70% or more wrong: often a faulty task, not a hard topic. */
    private static function hard(): array
    {
        $rows = Db::all('SELECT item_id, COUNT(1) AS n, SUM(1 - correct) AS wrong FROM attempts WHERE created_at > ? GROUP BY item_id HAVING COUNT(1) >= 8 AND SUM(1 - correct) * 10 >= COUNT(1) * 7 ORDER BY SUM(1 - correct) * 1.0 / COUNT(1) DESC, COUNT(1) DESC LIMIT 15', [time() - 60 * 86400]);
        return array_map(fn($r) => ['task' => self::describe($r['item_id']), 'n' => (int) $r['n'], 'wrong' => (int) $r['wrong'], 'pct' => (int) round(100 * $r['wrong'] / $r['n'])], $rows);
    }

    /** All reports as a spreadsheet file. No learner names: it can be shared to get the tasks fixed. */
    public static function exportCsv(): string
    {
        $fh = fopen('php://temp', 'w+');
        fputcsv($fh, ['reported', 'task id', 'topic', 'level', 'type', 'task', 'key (accepted answers)', 'learner answered', 'marked', 'reason', 'comment', 'status', 'learner'], ',', '"', '\\');
        $cell = fn($v) => preg_match('/^[=+\-@]/', (string) $v) ? "'" . $v : $v; // stop spreadsheet formula injection
        $tz = new DateTimeZone(Config::get('timezone', 'Europe/Riga'));
        foreach (Db::all('SELECT r.*, u.provider FROM reports r LEFT JOIN users u ON u.id = r.user_id ORDER BY r.item_id, r.updated_at') as $r) {
            $d = self::describe($r['item_id']);
            fputcsv($fh, [
                (new DateTime('@' . $r['updated_at']))->setTimezone($tz)->format('Y-m-d H:i'), $d['id'], $d['skill'], $d['level'], $d['kind'], $cell($d['q']), $cell($d['key']),
                $cell($r['answer'] ?? ''), $r['correct'] === null ? 'not answered' : ((int) $r['correct'] ? 'right' : 'wrong'),
                self::REASONS[$r['reason']] ?? $r['reason'], $cell($r['comment'] ?? ''), $r['status'], $r['provider'] === 'guest' ? 'guest' : 'registered',
            ], ',', '"', '\\');
        }
        rewind($fh);
        $csv = stream_get_contents($fh);
        fclose($fh);
        return $csv;
    }
}
