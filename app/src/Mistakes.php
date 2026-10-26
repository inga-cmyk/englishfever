<?php
// "Comeback": a learner's open mistakes, worked out from their own answers (no extra table, so past results are never touched).
//
// A mistake is a task answered wrongly. It is fixed when the learner later answers a similar task (same topic, level within
// one step, thinking level within one step) correctly: a different sentence. The same task right again counts only on a later
// day (the same day it is memory, not yet the rule). A task answered wrongly again after it was fixed becomes a mistake again.
// Placement mistakes above the level the test found are PARKED: they are not offered for Second Chance until the learner
// practises that level (they mark the edge of the level, not a gap to fix first).
// A fixed mistake is LOCKED IN when the learner answers another, different task of the same kind correctly on a later day.
// A wrong answer on the same kind of task after that opens it again ("reopened").

final class Mistakes
{
    public const DAYS = 45;       // older mistakes are let go
    private const SCAN_LIMIT = 3000;

    /**
     * @param array<int,string> $plLevels level found by a placement session that has no saved report yet (session id => level)
     * @return array{open: array<string,array>, parked: array<string,array>, fixed: int, locked: int, reopened: int} open mistakes in the order they were made; parked ones; how many were fixed, locked in, or opened again
     */
    public static function scan(int $uid, array $plLevels = []): array
    {
        $rows = Db::all('SELECT item_id, skill, level, bloom, correct, created_at, for_item, psession_id FROM attempts WHERE user_id = ? AND created_at > ? ORDER BY id ASC LIMIT ' . self::SCAN_LIMIT, [$uid, time() - self::DAYS * 86400]);
        $open = [];
        $solid = [];      // fixed, not yet locked in: id => kind of task, the day it was fixed, the tasks that fixed it
        $fixed = $locked = $reopened = 0;
        foreach ($rows as $r) {
            $id = $r['item_id'];
            $day = date('Y-m-d', (int) $r['created_at']);
            if (!(int) $r['correct']) {
                if (!isset($open[$id])) $open[$id] = ['skill' => $r['skill'], 'level' => $r['level'], 'bloom' => (int) $r['bloom'], 'tries' => 0, 'day' => $day, 'ses' => (int) $r['psession_id']];
                $open[$id]['tries']++;
                $open[$id]['day'] = $day;
                foreach ($solid as $sid => $sv) {
                    if (self::similar($sv, $r)) { unset($solid[$sid]); $reopened++; }
                }
                continue;
            }
            if (isset($open[$id]) && $open[$id]['day'] === $day) {   // the same sentence right again on the same day: memory, not yet fixed
                $open[$id]['retried'] = true;
                continue;
            }
            if (isset($open[$id])) {
                $solid[$id] = ['skill' => $open[$id]['skill'], 'level' => $open[$id]['level'], 'bloom' => $open[$id]['bloom'], 'day' => $day, 'items' => [$id => 1]];
                unset($open[$id]); $fixed++;
                continue;
            }
            // Second Chance knows which mistake the task stood for: that one is fixed
            $for = $r['for_item'] ?? null;
            if ($for !== null && isset($open[$for])) {
                $m = $open[$for];
                $solid[$for] = ['skill' => $m['skill'], 'level' => $m['level'], 'bloom' => $m['bloom'], 'day' => $day, 'items' => [$id => 1]];
                unset($open[$for]); $fixed++;
                continue;
            }
            // a right answer fixes the open mistake it is closest to (same level and thinking level first; the oldest of equals)
            $best = null; $bestD = 99;
            foreach ($open as $mid => $m) {
                if (!self::similar($m, $r)) continue;
                $dist = abs(self::levelIdx($m['level']) - self::levelIdx($r['level'])) + abs((int) $m['bloom'] - (int) $r['bloom']);
                if ($dist < $bestD) { $bestD = $dist; $best = $mid; }
            }
            if ($best !== null) {
                $m = $open[$best];
                $solid[$best] = ['skill' => $m['skill'], 'level' => $m['level'], 'bloom' => $m['bloom'], 'day' => $day, 'items' => [$id => 1]];
                unset($open[$best]); $fixed++;
                continue;
            }
            foreach ($solid as $sid => $sv) {
                if ($sv['day'] !== $day && !isset($sv['items'][$id]) && self::similar($sv, $r)) { unset($solid[$sid]); $locked++; break; }
            }
        }
        // tasks the teacher has paused (reported as flawed) are not the learner's mistakes
        foreach (array_keys(Reports::pausedIds()) as $pid) unset($open[$pid]);
        $parked = [];
        if ($open) {
            $pl = $plLevels;   // placement sessions and the level each found
            foreach (Db::all("SELECT id, state FROM psessions WHERE user_id = ? AND mode = 'placement'", [$uid]) as $p) {
                if (isset($pl[(int) $p['id']])) continue;
                $lv = json_decode((string) $p['state'], true)['report']['overall_level'] ?? null;
                if ($lv) $pl[(int) $p['id']] = $lv;
            }
            if ($pl) {
                $fi = array_flip(Content::FULL_LEVELS);
                $practised = [];   // full levels the learner has practised outside a placement test
                foreach (Db::all("SELECT DISTINCT a.level FROM attempts a JOIN psessions s ON s.id = a.psession_id WHERE a.user_id = ? AND s.mode <> 'placement'", [$uid]) as $r) $practised[substr($r['level'], 0, 2)] = true;
                foreach ($open as $id => $m) {
                    if (!isset($pl[$m['ses']])) continue;
                    $f = substr($m['level'], 0, 2);
                    if (($fi[$f] ?? 0) > ($fi[substr($pl[$m['ses']], 0, 2)] ?? 99) && empty($practised[$f])) { $parked[$id] = $m; unset($open[$id]); }
                }
            }
        }
        return ['open' => $open, 'parked' => $parked, 'solid' => $solid, 'fixed' => $fixed, 'locked' => $locked, 'reopened' => $reopened];
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

    /**
     * Fixed mistakes due for a check: fixed 2 or more days ago and not yet locked in, the oldest first (spaced review; teacher's
     * decision 27 October: only 7% of fixed mistakes were ever locked in). @return string[] mistake ids
     */
    public static function reviewDue(int $uid, ?array $scan = null): array
    {
        $scan = $scan ?? self::scan($uid);
        $limit = date('Y-m-d', time() - 2 * 86400);
        $due = array_filter($scan['solid'], fn($v, $id) => $v['day'] <= $limit && Content::item((string) $id), ARRAY_FILTER_USE_BOTH);
        uasort($due, fn($a, $b) => strcmp($a['day'], $b['day']));
        return array_map('strval', array_keys($due));
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

    /**
     * A different task that trains the same thing as a mistake: same topic, close level and thinking level. Null when there is none.
     * $code: prefer tasks for this kind of mistake. $maxScaffold / $minScaffold: prefer tasks with at most / at least this much
     * independence (Content::scaffold), so an easier task follows a miss and the same support comes back later.
     */
    public static function twin(int $uid, string $mistakeId, array $exclude, bool $angle = false, ?array $levels = null, ?string $code = null, ?int $maxScaffold = null, ?int $minScaffold = null): ?array
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
            if ($levels && !in_array($it['level'], $levels, true)) continue;
            if ($it['kind'] === 'write' && $m['kind'] !== 'write') continue;   // open writing never stands in for a short task
            $cost = (isset($seen[$it['id']]) ? 0.8 * min(3, $seen[$it['id']]) : 0)
                + ($angle ? ($it['kind'] === $m['kind'] ? 0.3 : 0) : ($it['kind'] === $m['kind'] ? 0 : 0.3)) + abs($it['bloom'] - $m['bloom']) * 0.2 + random_int(0, 30) / 100;
            if ($code !== null && !in_array($code, $it['err'] ?? [], true)) $cost += 0.6;
            // the check after a mistake tests the same rule, not a harder or longer sentence with new words (Cowork test, 26 October)
            if (self::levelIdx($it['level']) > self::levelIdx($m['level'])) $cost += 0.8;
            if (mb_strlen(self::text($it)) > 1.3 * mb_strlen(self::text($m)) + 10) $cost += 0.5;
            $sc = Content::scaffold($it);
            if ($maxScaffold !== null && $sc > $maxScaffold) $cost += 1.0 * ($sc - $maxScaffold);
            if ($minScaffold !== null && $sc < $minScaffold) $cost += 1.0 * ($minScaffold - $sc);
            if ($cost < $bestCost) { $bestCost = $cost; $best = $it; }
        }
        return $best;
    }

    /** The words a learner has to read in a task (instruction and sentence), to compare how long two tasks are. */
    private static function text(array $it): string
    {
        return $it['q'] . ' ' . ($it['correct'] ?? '') . ' ' . ($it['sentence'] ?? '');
    }

    /** What the teacher can see of how the "slip or gap" probes and the mistake life-cycle work, in numbers only (no names). */
    public static function evidence(): array
    {
        $probe = ['first_probes' => 0, 'slips' => 0, 'gaps' => 0, 'angle_probes' => 0, 'angle_right' => 0];
        $topics = [];
        foreach (Db::all("SELECT state FROM psessions WHERE state LIKE '%probe_log%'") as $r) {
            $st = json_decode($r['state'], true);
            foreach ($st['probe_log'] ?? [] as $p) {
                if (($p['stage'] ?? 1) === 1) {
                    $probe['first_probes']++; if ($p['ok']) $probe['slips']++; else $probe['gaps']++;
                    $it = Content::item((string) ($p['for'] ?? ''));
                    if ($it) { $topics[$it['skill']]['probes'] = ($topics[$it['skill']]['probes'] ?? 0) + 1; if (!$p['ok']) $topics[$it['skill']]['gaps'] = ($topics[$it['skill']]['gaps'] ?? 0) + 1; }
                }
                else { $probe['angle_probes']++; if ($p['ok']) $probe['angle_right']++; }
            }
        }
        $life = ['learners' => 0, 'open' => 0, 'fixed' => 0, 'locked' => 0, 'reopened' => 0];
        foreach (Db::all("SELECT DISTINCT a.user_id AS id FROM attempts a JOIN users u ON u.id = a.user_id WHERE u.role = 'student' AND a.created_at > ?", [time() - self::DAYS * 86400]) as $u) {
            $m = self::scan((int) $u['id']);
            $life['learners']++;
            $life['open'] += count($m['open']);
            $life['fixed'] += $m['fixed']; $life['locked'] += $m['locked']; $life['reopened'] += $m['reopened'];
        }
        $list = [];
        foreach ($topics as $sid => $t) { $sk = Content::skill($sid); $list[] = ['id' => $sid, 'label' => $sk ? $sk['label'] : $sid, 'probes' => (int) $t['probes'], 'gaps' => (int) ($t['gaps'] ?? 0)]; }
        usort($list, fn($a, $b) => [$b['gaps'], $b['probes']] <=> [$a['gaps'], $a['probes']]);
        return ['probes' => $probe, 'mistakes' => $life, 'topics' => array_slice($list, 0, 8)];
    }
}
