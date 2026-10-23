<?php
// "Comeback": a learner's open mistakes, worked out from their own answers (no extra table, so past results are never touched).
//
// A mistake is a task answered wrongly. It is fixed when the learner later answers the same task correctly, or a similar
// task (same topic, level within one step, thinking level within one step) correctly. A task answered wrongly again after
// it was fixed becomes a mistake again.

final class Mistakes
{
    public const DAYS = 45;       // older mistakes are let go
    private const SCAN_LIMIT = 3000;

    /** @return array{open: array<string,array>, fixed: int} open mistakes in the order they were made, and how many were fixed */
    public static function scan(int $uid): array
    {
        $rows = Db::all('SELECT item_id, skill, level, bloom, correct FROM attempts WHERE user_id = ? AND created_at > ? ORDER BY id ASC LIMIT ' . self::SCAN_LIMIT, [$uid, time() - self::DAYS * 86400]);
        $open = [];
        $fixed = 0;
        foreach ($rows as $r) {
            $id = $r['item_id'];
            if (!(int) $r['correct']) {
                if (!isset($open[$id])) $open[$id] = ['skill' => $r['skill'], 'level' => $r['level'], 'bloom' => (int) $r['bloom']];
                continue;
            }
            if (isset($open[$id])) { unset($open[$id]); $fixed++; continue; }
            foreach ($open as $mid => $m) {
                if (self::similar($m, $r)) { unset($open[$mid]); $fixed++; break; }
            }
        }
        // tasks the teacher has paused (reported as flawed) are not the learner's mistakes
        foreach (array_keys(Reports::pausedIds()) as $pid) unset($open[$pid]);
        return ['open' => $open, 'fixed' => $fixed];
    }

    private static function levelIdx(string $level): int
    {
        $i = array_search($level, array_keys(Content::BASE), true);
        return $i === false ? 0 : (int) $i;
    }

    private static function similar(array $m, array $r): bool
    {
        return $m['skill'] === $r['skill']
            && abs(self::levelIdx($m['level']) - self::levelIdx($r['level'])) <= 1
            && abs((int) $m['bloom'] - (int) $r['bloom']) <= 1;
    }

    /** Open mistakes in a good teaching order: oldest first, but different topics take turns. @return string[] item ids */
    public static function queue(int $uid, int $max = 10): array
    {
        $by = [];
        foreach (self::scan($uid)['open'] as $id => $m) {
            if (Content::item($id)) $by[$m['skill']][] = $id;
        }
        $out = [];
        while ($by && count($out) < $max) {
            foreach ($by as $s => &$list) {
                $out[] = array_shift($list);
                if (!$list) unset($by[$s]);
                if (count($out) >= $max) break;
            }
            unset($list);
        }
        return $out;
    }

    /** A different task that trains the same thing as a mistake: same topic, close level and thinking level. Null when there is none. */
    public static function twin(int $uid, string $mistakeId, array $exclude): ?array
    {
        $m = Content::item($mistakeId);
        if (!$m) return null;
        $paused = Reports::pausedIds();
        $seen = [];
        foreach (Db::all('SELECT item_id, COUNT(1) AS c FROM attempts WHERE user_id = ? GROUP BY item_id', [$uid]) as $r) $seen[$r['item_id']] = (int) $r['c'];
        $best = null;
        $bestCost = PHP_FLOAT_MAX;
        foreach (Content::items() as $it) {
            if ($it['skill'] !== $m['skill'] || $it['id'] === $mistakeId || isset($exclude[$it['id']]) || isset($paused[$it['id']])) continue;
            if (abs(self::levelIdx($it['level']) - self::levelIdx($m['level'])) > 1 || abs($it['bloom'] - $m['bloom']) > 1) continue;
            $cost = (isset($seen[$it['id']]) ? 0.8 * min(3, $seen[$it['id']]) : 0)
                + ($it['kind'] === $m['kind'] ? 0 : 0.3) + abs($it['bloom'] - $m['bloom']) * 0.2 + random_int(0, 30) / 100;
            if ($cost < $bestCost) { $bestCost = $cost; $best = $it; }
        }
        return $best;
    }
}
