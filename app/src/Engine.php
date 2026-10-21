<?php
// Adaptive practice engine: picks the next task, updates the learner's estimate, writes the log.

final class Engine
{
    public const PLACEMENT_LEN = 24;
    private const LEVELS = ['A2.1', 'A2.2', 'B1.1', 'B1.2', 'B2.1', 'B2.2', 'C1.1', 'C1.2'];
    public const PLACEMENT_SIZES = [12, 24, 40];

    // ───────── sessions ─────────

    public static function start(int $uid, string $mode, array $skills, ?string $level, int $len): array
    {
        $meta = Content::meta();
        $all = array_column($meta['skills'], 'id');
        $smart = false;
        if ($mode === 'placement') {
            $skills = $all;
            $level = 'A2.2';
            $len = in_array($len, self::PLACEMENT_SIZES, true) ? $len : self::PLACEMENT_LEN;
        } else {
            if ($mode === 'smart') {
                // "Surprise me": the app chooses topics from the learner's own mistakes and gaps
                [$skills, $level] = self::smartPick($uid, $all);
                $smart = true;
                $mode = 'practice';
            }
            $skills = array_values(array_intersect($skills, $all));
            if (!$skills) throw new ApiError('Choose at least one topic.', 400);
            if (!isset(Content::BASE[$level]) || !in_array($level, $meta['levels'], true)) throw new ApiError('Choose a level.', 400);
            $len = max(5, min(30, $len ?: 10));
        }
        // close old unfinished sessions of this user
        Db::q('UPDATE psessions SET ended_at = ? WHERE user_id = ? AND ended_at IS NULL', [time(), $uid]);

        $state = ['current' => null, 'seed' => random_int(1, 1 << 30), 'served' => [], 'theta' => [], 'g' => 2.0, 'last' => []];
        if ($smart) $state['smart'] = true;
        if ($mode === 'practice') {
            foreach ($skills as $s) {
                $row = Db::one('SELECT theta, n FROM skill_state WHERE user_id = ? AND skill = ?', [$uid, $s]);
                $init = Content::BASE[$level] + 0.3;
                if ($smart) $state['theta'][$s] = ($row && $row['n'] >= 3) ? (float) $row['theta'] : $init;
                else $state['theta'][$s] = ($row && $row['n'] >= 4) ? round(($row['theta'] + $init) / 2, 3) : $init;
            }
        }
        $sid = Db::insert('psessions', [
            'user_id' => $uid, 'mode' => $mode, 'skills' => json_encode($skills), 'level' => $level,
            'target_len' => $len, 'state' => json_encode($state), 'started_at' => time(),
        ]);
        $ses = self::load($uid, $sid);
        $item = self::pickNext($ses);
        if (!$item) throw new ApiError('No tasks found for this choice yet.', 404);
        $ses['state']['current'] = $item['id'];
        $ses['state']['served'][] = $item['id'];
        self::save($ses);
        return ['session' => self::pub($ses), 'item' => Content::publicItem($item, $ses['state']['seed'] + count($ses['state']['served']))];
    }

    public static function resume(int $uid): ?array
    {
        $row = Db::one('SELECT id FROM psessions WHERE user_id = ? AND ended_at IS NULL AND started_at > ? ORDER BY id DESC LIMIT 1', [$uid, time() - 6 * 3600]);
        if (!$row) return null;
        return self::current($uid, (int) $row['id']);
    }

    public static function current(int $uid, int $sid): array
    {
        $ses = self::load($uid, $sid);
        if ($ses['ended_at'] !== null || !$ses['state']['current']) throw new ApiError('This session is finished.', 409);
        $item = Content::item($ses['state']['current']);
        return ['session' => self::pub($ses), 'item' => Content::publicItem($item, $ses['state']['seed'] + count($ses['state']['served']))];
    }

    public static function answer(int $uid, int $sid, string $itemId, $answer, int $timeMs): array
    {
        $ses = self::load($uid, $sid);
        if ($ses['ended_at'] !== null) throw new ApiError('This session is finished.', 409);
        $st = &$ses['state'];
        if ($st['current'] !== $itemId) throw new ApiError('This task was already answered.', 409);
        $item = Content::item($itemId);
        $answer = self::cleanAnswer($answer);
        $g = Grader::grade($item, $answer);
        $ok = $g['correct'];
        $skill = $item['skill'];
        $d = $item['d'];

        // XP only once per day per item when correct, so repeating one easy task does not farm points
        $xp = 0;
        if ($ok) {
            $xp = 8 + 2 * $item['bloom'];
            $dup = Db::val('SELECT COUNT(1) FROM attempts WHERE user_id = ? AND item_id = ? AND correct = 1 AND created_at > ?', [$uid, $itemId, time() - 86400]);
            if ($dup) $xp = 0;
        } else {
            $xp = 2;
        }

        // learner estimate (Elo style)
        $theta = $st['theta'][$skill] ?? ($ses['mode'] === 'placement' ? $st['g'] : Content::BASE[$ses['level']] + 0.3);
        $seen = count(array_filter($st['last'], fn($h) => $h['skill'] === $skill));
        $k = $seen < 2 ? 0.5 : 0.3;
        $p = 1 / (1 + exp(-1.7 * ($theta - $d)));
        $theta = max(0.5, min(9.5, $theta + $k * (($ok ? 1 : 0) - $p)));
        $st['theta'][$skill] = round($theta, 3);
        $pg = 1 / (1 + exp(-1.7 * ($st['g'] - $d)));
        $st['g'] = round(max(0.5, min(9.5, $st['g'] + 0.4 * (($ok ? 1 : 0) - $pg))), 3);
        $st['last'][] = ['skill' => $skill, 'correct' => $ok ? 1 : 0, 'd' => $d, 'bloom' => $item['bloom']];

        $now = time();
        Db::insert('attempts', [
            'user_id' => $uid, 'psession_id' => $sid, 'item_id' => $itemId, 'skill' => $skill, 'level' => $item['level'],
            'bloom' => $item['bloom'], 'correct' => $ok ? 1 : 0, 'answer' => mb_substr(is_array($answer) ? implode($item['kind'] === 'order' ? ' ' : ' / ', array_map('strval', $answer)) : (string) $answer, 0, 500),
            'time_ms' => max(0, min(600000, $timeMs)), 'xp' => $xp, 'created_at' => $now,
        ]);
        $row = Db::one('SELECT n, n_correct FROM skill_state WHERE user_id = ? AND skill = ?', [$uid, $skill]);
        if ($row) {
            Db::update('skill_state', ['theta' => $theta, 'n' => $row['n'] + 1, 'n_correct' => $row['n_correct'] + ($ok ? 1 : 0), 'updated_at' => $now], 'user_id = ? AND skill = ?', [$uid, $skill]);
        } else {
            Db::insert('skill_state', ['user_id' => $uid, 'skill' => $skill, 'theta' => $theta, 'n' => 1, 'n_correct' => $ok ? 1 : 0, 'updated_at' => $now]);
        }
        Stats::addActivity($uid, 0, 1, $xp);

        $ses['n']++;
        $ses['n_correct'] += $ok ? 1 : 0;
        $ses['xp'] += $xp;
        $done = $ses['n'] >= $ses['target_len'];
        $next = null;
        $adapt = 'same';
        if (!$done) {
            $next = self::pickNext($ses);
            if (!$next) {
                $done = true;
            } else {
                $diff = $next['d'] - $d;
                $adapt = $diff > 0.15 ? 'harder' : ($diff < -0.15 ? 'easier' : 'same');
                $st['current'] = $next['id'];
                $st['served'][] = $next['id'];
            }
        }
        $summary = null;
        if ($done) {
            $st['current'] = null;
            $ses['ended_at'] = $now;
            $summary = self::buildSummary($ses);
            if ($ses['mode'] === 'placement') $st['report'] = $summary;
        }
        self::save($ses);

        $res = [
            'correct' => $ok,
            'show' => $g['show'],
            'specific' => $g['specific'],
            'notes' => $g['notes'] ?? [],
            'why' => $item['why'],
            'skill' => $skill,
            'kind' => $item['kind'],
            'xp' => $xp,
            'adapt' => $adapt,
        ];
        if (isset($g['marks'])) $res['marks'] = $g['marks'];
        if ($item['kind'] === 'match') $res['pairs'] = $item['pairs'];
        // Latvian explanations (up to B1.2): sent beside the English ones, the browser shows the learner's choice
        if (!empty($item['why_lv'])) {
            $res['why_lv'] = $item['why_lv'];
            $res['specific_lv'] = $g['specific_lv'] ?? null;
        }
        return [
            'result' => $res,
            'session' => self::pub($ses),
            'done' => $done,
            'next' => $next ? Content::publicItem($next, $st['seed'] + count($st['served'])) : null,
            'summary' => $summary,
        ];
    }

    public static function quit(int $uid, int $sid): array
    {
        $ses = self::load($uid, $sid);
        if ($ses['ended_at'] === null) {
            $ses['ended_at'] = time();
            $ses['state']['current'] = null;
            $summary = self::buildSummary($ses);
            if ($ses['mode'] === 'placement' && $ses['n'] >= 6) $ses['state']['report'] = $summary;
            self::save($ses);
        }
        return self::buildSummary($ses);
    }

    public static function summary(int $uid, int $sid): array
    {
        return self::buildSummary(self::load($uid, $sid));
    }

    // ───────── "Surprise me": topics chosen from the learner's own history ─────────

    /**
     * Up to four topics: the ones the learner gets wrong most (recent mistakes count), plus one they have not tried.
     * A new learner gets a few friendly starter topics. @return array{0: string[], 1: string} topics and the level to start from
     */
    private static function smartPick(int $uid, array $all): array
    {
        $rows = [];
        foreach (Db::all('SELECT skill, theta, n, n_correct FROM skill_state WHERE user_id = ?', [$uid]) as $r) {
            if (in_array($r['skill'], $all, true)) $rows[$r['skill']] = $r;
        }
        $wrong = [];
        foreach (Db::all('SELECT skill, COUNT(1) AS c FROM attempts WHERE user_id = ? AND correct = 0 AND created_at > ? GROUP BY skill', [$uid, time() - 14 * 86400]) as $r) {
            $wrong[$r['skill']] = (int) $r['c'];
        }
        $total = 0; $sum = 0.0;
        foreach ($rows as $r) { $total += (int) $r['n']; $sum += (float) $r['theta'] * (int) $r['n']; }
        if ($total < 5) {
            $starters = array_values(array_intersect(['present_simple', 'present_continuous', 'past_simple', 'present_perfect', 'future', 'cond_zero', 'cond_first'], $all));
            shuffle($starters);
            return [array_slice($starters, 0, 4), 'A2.2'];
        }
        $level = Content::levelFromTheta($sum / $total);
        $need = [];
        foreach ($rows as $s => $r) {
            if ((int) $r['n'] < 2) continue;
            $need[$s] = (1 - (int) $r['n_correct'] / (int) $r['n']) * 3 + min(5, $wrong[$s] ?? 0) * 0.25 + random_int(0, 30) / 100;
        }
        arsort($need);
        $pick = [];
        foreach ($need as $s => $v) {
            if ($v > 0.45 && count($pick) < 3) $pick[] = $s;
        }
        // one topic they have not tried yet, not far above their level
        $levelIdx = array_search($level, self::LEVELS);
        $fresh = [];
        foreach (Content::meta()['skills'] as $sk) {
            if (isset($rows[$sk['id']])) continue;
            if (array_search($sk['levels'][0], self::LEVELS) <= $levelIdx + 1) $fresh[] = $sk['id'];
        }
        shuffle($fresh);
        if ($fresh) $pick[] = $fresh[0];
        // not enough weak spots: add practised topics so the session has some variety
        $rest = array_diff(array_keys($rows), $pick);
        shuffle($rest);
        while (count($pick) < 3 && $rest) $pick[] = array_shift($rest);
        return [array_values(array_unique($pick)), $level];
    }

    // ───────── helpers ─────────

    /** Answers come from the browser: short text, or a short list of short text. Anything else counts as an empty answer. */
    private static function cleanAnswer($a)
    {
        if (is_array($a)) {
            $out = [];
            foreach (array_slice(array_values($a), 0, 24) as $x) $out[] = is_scalar($x) ? mb_substr((string) $x, 0, 300) : '';
            return $out;
        }
        return is_scalar($a) ? mb_substr((string) $a, 0, 2000) : '';
    }

    private static function load(int $uid, int $sid): array
    {
        $r = Db::one('SELECT * FROM psessions WHERE id = ? AND user_id = ?', [$sid, $uid]);
        if (!$r) throw new ApiError('Session not found.', 404);
        $r['skills'] = json_decode($r['skills'], true);
        $r['state'] = json_decode($r['state'], true);
        $r['ended_at'] = $r['ended_at'] === null ? null : (int) $r['ended_at'];
        foreach (['n', 'n_correct', 'xp', 'target_len'] as $c) $r[$c] = (int) $r[$c];
        return $r;
    }

    private static function save(array $ses): void
    {
        Db::update('psessions', [
            'n' => $ses['n'], 'n_correct' => $ses['n_correct'], 'xp' => $ses['xp'],
            'state' => json_encode($ses['state']), 'ended_at' => $ses['ended_at'],
        ], 'id = ?', [$ses['id']]);
    }

    private static function pub(array $ses): array
    {
        return [
            'id' => (int) $ses['id'], 'mode' => $ses['mode'], 'length' => $ses['target_len'], 'n' => $ses['n'],
            'correct' => $ses['n_correct'], 'xp' => $ses['xp'], 'level' => $ses['level'], 'skills' => $ses['skills'],
            'phase' => ($ses['mode'] === 'practice' && $ses['n'] < 3 && empty($ses['state']['smart'])) ? 'diagnostic' : 'adaptive',
            'smart' => !empty($ses['state']['smart']),
        ];
    }

    private static function pickNext(array $ses): ?array
    {
        $st = $ses['state'];
        $served = array_flip($st['served']);
        $placement = $ses['mode'] === 'placement';
        $skills = $ses['skills'];
        $levelIdx = array_search($ses['level'], self::LEVELS);
        $count = count($st['served']);

        $smart = !empty($st['smart']);
        // candidate items
        $bySkill = [];
        foreach (Content::items() as $it) {
            if (!in_array($it['skill'], $skills, true) || isset($served[$it['id']])) continue;
            if ($placement && ($it['kind'] === 'write' || $it['bloom'] > 4)) continue;
            $bySkill[$it['skill']][] = $it;
        }
        if (!$placement) {
            foreach ($bySkill as $s => $list) {
                // "Surprise me" centres each topic on the learner's own level in that topic
                $centre = $smart && isset($st['theta'][$s]) ? array_search(Content::levelFromTheta((float) $st['theta'][$s]), self::LEVELS) : $levelIdx;
                $win = array_values(array_filter($list, function ($it) use ($centre) {
                    $i = array_search($it['level'], self::LEVELS);
                    return $i >= $centre - 1 && $i <= $centre + 1;
                }));
                if ($win) $bySkill[$s] = $win;
            }
        }
        if (!$bySkill) return null;

        // how often each skill / bloom was used in this session
        $skillCount = array_fill_keys(array_keys($bySkill), 0);
        $bloomCount = array_fill_keys([1, 2, 3, 4, 5, 6], 0);
        foreach ($st['last'] as $h) {
            if (isset($skillCount[$h['skill']])) $skillCount[$h['skill']]++;
            $bloomCount[$h['bloom']]++;
        }

        // placement: a run of correct answers moves the target up faster, so strong learners are not stuck on easy tasks
        $boost = 0.0;
        if ($placement) {
            $streak = 0;
            foreach (array_reverse($st['last']) as $h) { if ($h['correct']) $streak++; else break; }
            $boost = min(1.2, max(0, $streak - 1) * 0.4);
        }
        // placement: skip skills that are far too hard for the current estimate
        if ($placement) {
            $g = $st['g'];
            foreach ($bySkill as $s => $list) {
                $min = min(array_column($list, 'd'));
                if ($min > $g + 1.2 + $boost) unset($bySkill[$s]);
            }
            if (!$bySkill) return null;
        }

        // choose the skill: least used so far; in placement, skills just answered wrongly are re-checked first
        $lastWrong = [];
        foreach ($st['last'] as $h) $lastWrong[$h['skill']] = !$h['correct'];
        $bestSkill = null;
        $bestScore = PHP_FLOAT_MAX;
        foreach ($bySkill as $s => $list) {
            $score = $skillCount[$s] * 10 + (random_int(0, 99) / 100);
            if ($placement && $skillCount[$s] > 0 && !empty($lastWrong[$s])) $score -= 4;
            if ($score < $bestScore) { $bestScore = $score; $bestSkill = $s; }
        }
        $pool = $bySkill[$bestSkill];

        // recent history penalty
        $recent = [];
        foreach (Db::all('SELECT item_id, MAX(correct) AS c FROM attempts WHERE user_id = ? AND created_at > ? GROUP BY item_id', [$ses['user_id'], time() - 7 * 86400]) as $r) {
            $recent[$r['item_id']] = (int) $r['c'];
        }

        // "Surprise me" brings back tasks the learner got wrong before (not in the last half hour)
        $missed = [];
        if ($smart) {
            foreach (Db::all('SELECT item_id FROM attempts WHERE user_id = ? AND created_at > ? AND created_at < ? GROUP BY item_id HAVING MAX(correct) = 0', [$ses['user_id'], time() - 30 * 86400, time() - 1800]) as $r) $missed[$r['item_id']] = true;
        }

        // target difficulty
        if (!$placement && !$smart && $count < 3) {
            $target = Content::BASE[$ses['level']] + 0.2 * $count; // diagnostic: Bloom 1, 2, 3 at the chosen level
        } else {
            $theta = $st['theta'][$bestSkill] ?? ($placement ? $st['g'] : Content::BASE[$ses['level']] + 0.3);
            $target = $theta + 0.1 + $boost;
        }

        $best = null;
        $bestCost = PHP_FLOAT_MAX;
        foreach ($pool as $it) {
            $cost = abs($it['d'] - $target) + 0.2 * $bloomCount[$it['bloom']] + random_int(0, 25) / 100;
            if (isset($recent[$it['id']])) $cost += $recent[$it['id']] ? 0.6 : 0.2;
            if (isset($missed[$it['id']])) $cost -= 0.7;
            if ($st['last'] && end($st['last'])['bloom'] === $it['bloom']) $cost += 0.3; // avoid the same thinking level twice in a row
            if (!$placement && !$smart && $count < 3 && $it['level'] !== $ses['level']) $cost += 0.5;
            if ($cost < $bestCost) { $bestCost = $cost; $best = $it; }
        }
        return $best;
    }

    /** Ability that best explains the answers (logistic model, weak prior), by Newton steps. @param array $pts list of [difficulty, 1|0] */
    private static function fitAbility(array $pts): float
    {
        $th = 3.0;
        for ($i = 0; $i < 30; $i++) {
            $g = 0.0; $h = 0.0;
            foreach ($pts as [$d, $ok]) {
                $p = 1 / (1 + exp(-1.7 * ($th - $d)));
                $g += 1.7 * ($ok - $p);
                $h += 2.89 * $p * (1 - $p);
            }
            $g -= ($th - 3.0) / 9; $h += 1 / 9;
            $step = max(-1.5, min(1.5, $g / $h));
            $th = max(0.0, min(10.0, $th + $step));
            if (abs($step) < 1e-4) break;
        }
        return $th;
    }

    private static function buildSummary(array $ses): array
    {
        $rows = Db::all('SELECT skill, level, bloom, correct FROM attempts WHERE psession_id = ?', [$ses['id']]);
        $bySkill = [];
        $byBloom = [];
        foreach ($rows as $r) {
            $bySkill[$r['skill']]['n'] = ($bySkill[$r['skill']]['n'] ?? 0) + 1;
            $bySkill[$r['skill']]['c'] = ($bySkill[$r['skill']]['c'] ?? 0) + (int) $r['correct'];
            $byBloom[$r['bloom']]['n'] = ($byBloom[$r['bloom']]['n'] ?? 0) + 1;
            $byBloom[$r['bloom']]['c'] = ($byBloom[$r['bloom']]['c'] ?? 0) + (int) $r['correct'];
        }
        $skills = [];
        foreach ($bySkill as $s => $v) {
            $meta = Content::skill($s);
            $theta = $ses['state']['theta'][$s] ?? $ses['state']['g'];
            $skills[] = [
                'id' => $s, 'label' => $meta['label'], 'area' => $meta['area'], 'n' => $v['n'], 'correct' => $v['c'],
                'theta' => round($theta, 2), 'level_est' => Content::levelFromTheta($theta, $meta['levels']),
            ];
        }
        usort($skills, fn($a, $b) => $a['theta'] <=> $b['theta']);

        $bloomOut = [];
        foreach ($byBloom as $b => $v) $bloomOut[(string) $b] = ['n' => $v['n'], 'correct' => $v['c']];
        ksort($bloomOut);

        $acc = $ses['n'] ? round(100 * $ses['n_correct'] / $ses['n']) : 0;
        $out = [
            'session_id' => (int) $ses['id'], 'mode' => $ses['mode'], 'n' => $ses['n'], 'correct' => $ses['n_correct'], 'accuracy' => $acc,
            'xp' => $ses['xp'], 'by_skill' => $skills, 'by_bloom' => $bloomOut, 'finished' => $ses['ended_at'] !== null,
        ];

        if ($ses['mode'] === 'placement') {
            $tested = array_column($skills, 'id');
            // The overall level is fitted to all the answers at once (not to the path the test took), so a strong learner
            // is not held back by the order in which tasks were served.
            $pts = [];
            foreach ($rows as $r) $pts[] = [Content::difficulty($r['level'], (int) $r['bloom']), (int) $r['correct']];
            $overall = $pts ? self::fitAbility($pts) : $ses['state']['g'];
            $out['overall_level'] = Content::levelFromAbility($overall);
            $out['overall_theta'] = round($overall, 2);
            $gaps = [];
            foreach (array_slice($skills, 0, 3) as $s) {
                $gaps[] = ['id' => $s['id'], 'label' => $s['label'], 'level' => $s['level_est'],
                    'why' => "{$s['correct']} of {$s['n']} correct at about {$s['level_est']} level"];
            }
            $out['gaps'] = $gaps;
            $untested = [];
            foreach (Content::meta()['skills'] as $s) {
                if (!in_array($s['id'], $tested, true)) $untested[] = ['id' => $s['id'], 'label' => $s['label']];
            }
            $out['untested'] = $untested;
        } else {
            $next = [];
            foreach ($skills as $s) {
                if ($s['n'] >= 2 && $s['correct'] / $s['n'] < 0.6) {
                    $next[] = ['type' => 'review', 'skill' => $s['id'], 'label' => $s['label'], 'text' => "Read the rule card for {$s['label']}, then try again."];
                }
            }
            if ($acc >= 80 && empty($ses['state']['smart'])) {
                $levels = Content::meta()['levels'];
                $idx = array_search($ses['level'], $levels);
                // only offer a level that exists for at least one of the topics practised
                $top = 0;
                foreach ($ses['skills'] as $sid) {
                    $sk = Content::skill($sid);
                    if ($sk) $top = max($top, (int) array_search(end($sk['levels']), $levels));
                }
                if ($idx !== false && isset($levels[$idx + 1]) && $idx + 1 <= $top) {
                    $next[] = ['type' => 'level_up', 'level' => $levels[$idx + 1], 'text' => "Great accuracy! Try the next level: {$levels[$idx + 1]}."];
                }
            }
            $out['next'] = array_slice($next, 0, 3);
            $out['level'] = $ses['level'];
        }
        return $out;
    }
}
