<?php
// Adaptive practice engine: picks the next task, updates the learner's estimate, writes the log.

final class Engine
{
    public const PLACEMENT_LEN = 24;
    private const LEVELS = ['A2.1', 'A2.2', 'B1.1', 'B1.2', 'B2.1', 'B2.2', 'C1.1', 'C1.2'];
    public const PLACEMENT_SIZES = [12, 24, 40];
    /** Share of each question type in a practice session, per 10: 3 choose, 4 drag (order, word bank, matching), 2 type a word or words, 1 type the whole sentence. Open writing is rare on purpose. */
    public const MIX = ['choose' => 0.3, 'drag' => 0.4, 'word' => 0.2, 'sentence' => 0.1, 'write' => 0.0];

    /** @return string choose | drag | word | sentence | write */
    public static function typeGroup(array $it): string
    {
        switch ($it['kind']) {
            case 'mcq': return 'choose';
            case 'order': case 'match': return 'drag';
            case 'gap': return !empty($it['bank']) ? 'drag' : 'word';
            case 'text': return 'sentence';
        }
        return 'write';
    }

    // ───────── sessions ─────────

    public static function start(int $uid, string $mode, array $skills, ?string $level, int $len, ?array $fullLevels = null): array
    {
        $meta = Content::liveMeta();
        $all = array_column($meta['skills'], 'id');
        $smart = false;
        $comeback = false;
        if ($mode === 'comeback') {
            // "Comeback": the learner's open mistakes, each met again as a similar task
            $queue = Mistakes::queue($uid, 10);
            $review = array_slice(Mistakes::reviewDue($uid), 0, 2);   // 1-2 mistakes fixed a few days ago, checked again in a new sentence
            if (!$queue && !$review) throw new ApiError('No mistakes are waiting right now. Nice work!', 404);
            $queue = array_merge(array_slice($queue, 0, 10 - count($review)), $review);
            $comeback = true;
            $mode = 'practice';
            $skills = array_values(array_unique(array_map(fn($id) => Content::item($id)['skill'], $queue)));
            $level = Content::item($queue[0])['level'];
            $len = count($queue);
        } elseif ($mode === 'placement') {
            $skills = $all;
            $level = 'A2.2';
            $len = in_array($len, self::PLACEMENT_SIZES, true) ? $len : self::PLACEMENT_LEN;
        } else {
            if ($mode === 'smart') {
                // "Surprise me": the app chooses topics from the learner's own mistakes and gaps
                [$skills, $level, $firstTime] = self::smartPick($uid, $all) + [2 => false];
                if ($firstTime) $len = 8;   // a new learner: a short taste of the most common mistakes (teacher, 27 October)
                $smart = true;
                $mode = 'practice';
            }
            if ($fullLevels !== null) {
                // levels first: whole levels (A2, B1 ...), with or without topics; no topic = a mix of the topics that have questions there
                $fullLevels = array_values(array_intersect(Content::FULL_LEVELS, array_map('strval', $fullLevels)));
                $allowed = array_values(array_filter($meta['levels'], fn($l) => in_array(substr($l, 0, 2), $fullLevels, true)));
                if (!$fullLevels) throw new ApiError('Choose a level.', 400);
                if (!$allowed) throw new ApiError('No questions at this level yet.', 404);
                $counts = Content::levelCounts()['by_skill'];
                $have = fn($sid) => array_sum(array_map(fn($f) => $counts[$sid][$f] ?? 0, $fullLevels));
                $skills = array_values(array_filter(array_intersect($skills, $all), fn($sid) => $have($sid) > 0));
                if (!$skills) $skills = array_values(array_filter($all, fn($sid) => $have($sid) >= 8));   // a mix
                if (!$skills) throw new ApiError('No questions at this level yet.', 404);
                $level = $allowed[0];
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
        if ($comeback) { $state['comeback'] = true; $state['queue'] = $queue; $state['review'] = array_fill_keys($review, true); }
        if (!empty($allowed)) $state['levels'] = $allowed;
        if ($mode === 'placement') {
            // placement: climb level by level (A2, B1, B2 ...) in blocks of 3 questions, then fine-tune around the ability found
            $ladder = array_values(array_unique(array_map(fn($l) => substr($l, 0, 2), $meta['levels'])));
            $state['pl'] = ['ladder' => $ladder, 'lv' => $ladder[0], 'n' => 0, 'c' => 0, 'nn' => 0, 'cc' => 0, 'bn' => 0, 'done' => false, 'passed' => [], 'long' => $len >= 40, 'strict' => $len <= 12];   // the full test asks two blocks at the first level, so A2 and B1 can be told apart
        }
        $state['fixed'] = 0;
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
        if (!$item) throw new ApiError('No questions found for this choice yet.', 404);
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

    public static function answer(int $uid, int $sid, string $itemId, $answer, int $timeMs, bool $skip = false): array
    {
        $ses = self::load($uid, $sid);
        if ($ses['ended_at'] !== null) throw new ApiError('This session is finished.', 409);
        $st = &$ses['state'];
        if ($st['current'] !== $itemId) throw new ApiError('This task was already answered.', 409);
        $item = Content::item($itemId);
        $answer = $skip ? '' : self::cleanAnswer($answer);   // Skip = "I don't know": counted as not known, no guessing, no XP (teacher, 27 October)
        $g = Grader::grade($item, $skip ? (in_array($item['kind'], ['gap', 'order', 'match'], true) ? [] : '') : $answer);
        $ok = $skip ? false : $g['correct'];
        if ($skip) { $g['specific'] = $g['specific_lv'] = $g['err'] = null; $g['notes'] = []; $g['near'] = false; }
        $skill = $item['skill'];
        $d = $item['d'];

        // XP only once per day per item when correct, so repeating one easy task does not farm points
        $xp = 0;
        if ($ok) {
            $xp = 8 + 2 * $item['bloom'];
            $dup = Db::val('SELECT COUNT(1) FROM attempts WHERE user_id = ? AND item_id = ? AND correct = 1 AND created_at > ?', [$uid, $itemId, time() - 86400]);
            if ($dup) $xp = 0;
        } else {
            $xp = $skip ? 0 : 2;
        }
        if ($ok && isset($st['bonus_from']) && count($st['served']) > $st['bonus_from']) $xp *= 2;   // a bonus question after Second Chance: double XP

        // learner estimate (Elo style)
        $theta = $st['theta'][$skill] ?? ($ses['mode'] === 'placement' ? $st['g'] : Content::BASE[$ses['level']] + 0.3);
        $seen = count(array_filter($st['last'], fn($h) => $h['skill'] === $skill));
        $k = $seen < 2 ? 0.5 : 0.3;
        $p = 1 / (1 + exp(-1.7 * ($theta - $d)));
        $theta = max(0.5, min(9.5, $theta + $k * (($ok ? 1 : 0) - $p)));
        $st['theta'][$skill] = round($theta, 3);
        $pg = 1 / (1 + exp(-1.7 * ($st['g'] - $d)));
        $st['g'] = round(max(0.5, min(9.5, $st['g'] + 0.4 * (($ok ? 1 : 0) - $pg))), 3);
        $st['last'][] = ['skill' => $skill, 'correct' => $ok ? 1 : 0, 'd' => $d, 'bloom' => $item['bloom'], 'level' => substr($item['level'], 0, 2), 'sc' => Content::scaffold($item)];
        if ($ses['mode'] === 'placement') self::plAdvance($st, substr($item['level'], 0, 2), $ok);

        // the kinds of mistake this answer is evidence for (background only): a wrong option or hint that names one, else the task's own list
        $errCodes = (!$ok && !empty($g['err'])) ? [$g['err']] : Content::errors($item);
        $before = $ses['mode'] === 'placement' ? null : Mistakes::scan($uid);
        $now = time();
        Db::insert('attempts', [
            'user_id' => $uid, 'psession_id' => $sid, 'item_id' => $itemId, 'skill' => $skill, 'level' => $item['level'],
            'bloom' => $item['bloom'], 'correct' => $ok ? 1 : 0, 'answer' => $skip ? '(skipped)' : mb_substr(is_array($answer) ? implode($item['kind'] === 'order' ? ' ' : ' / ', array_map('strval', $answer)) : (string) $answer, 0, 500),
            'time_ms' => max(0, min(600000, $timeMs)), 'xp' => $xp, 'created_at' => $now,
            'for_item' => !empty($st['comeback']) ? (function () use ($st) { $q = $st['queue'][count($st['served']) - 1] ?? null; return $q === null ? null : ($st['queue_extra'][$q] ?? $q); })() : null,
            'err' => $errCodes ? implode(',', $errCodes) : null,
        ]);
        $row = Db::one('SELECT n, n_correct FROM skill_state WHERE user_id = ? AND skill = ?', [$uid, $skill]);
        if ($row) {
            Db::update('skill_state', ['theta' => $theta, 'n' => $row['n'] + 1, 'n_correct' => $row['n_correct'] + ($ok ? 1 : 0), 'updated_at' => $now], 'user_id = ? AND skill = ?', [$uid, $skill]);
        } else {
            Db::insert('skill_state', ['user_id' => $uid, 'skill' => $skill, 'theta' => $theta, 'n' => 1, 'n_correct' => $ok ? 1 : 0, 'updated_at' => $now]);
        }
        Stats::addActivity($uid, 0, 1, $xp);
        $fixedNow = $lockedNow = false;
        if ($before !== null && $ok) {
            $after = Mistakes::scan($uid);
            $fixedNow = $after['fixed'] > $before['fixed'];
            $lockedNow = $after['locked'] > $before['locked'];   // a mistake the learner has now got right again, on another day: kept quiet, only the sound tells
        }
        if ($fixedNow) $st['fixed'] = ($st['fixed'] ?? 0) + 1;
        if ($lockedNow) $st['locked'] = ($st['locked'] ?? 0) + 1;
        $gapNow = self::probeAnswered($st, $itemId, $ok, $ses);
        if (!empty($st['comeback'])) $gapNow = self::comebackGap($st, $ses, $itemId, $ok) || $gapNow;

        if (!$ok && $ses['mode'] === 'practice' && empty($st['comeback'])) self::probeSchedule($st, $item, $errCodes, count($st['served']), (int) $ses['target_len']);
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
                // after a wrong answer the next task is never announced as harder, after a right one never as easier (guest test report)
                $adapt = ($ok && $diff > 0.15) ? 'harder' : ((!$ok && $diff < -0.15) ? 'easier' : 'same');
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
            'near' => !empty($g['near']),
            'why' => $item['why'],
            'skill' => $skill,
            'kind' => $item['kind'],
            'xp' => $xp,
            'adapt' => $adapt,
            'fixed' => $fixedNow,
            'locked' => $lockedNow,
            'gap' => $gapNow,
            'skipped' => $skip,
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
            // first time: the mistakes Latvian adults make most (he work, no article, I have seen yesterday, What you want?, in Monday, listen music, will after when)
            $starters = array_values(array_intersect(['present_simple', 'agreement', 'articles', 'present_perfect', 'past_simple', 'prep_time_place', 'dep_prepositions', 'subject_object_q', 'time_clauses'], $all));
            shuffle($starters);
            return [array_slice($starters, 0, 5), 'A2.2', true];
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
            'n' => $ses['n'], 'n_correct' => $ses['n_correct'], 'xp' => $ses['xp'], 'target_len' => $ses['target_len'],
            'state' => json_encode($ses['state']), 'ended_at' => $ses['ended_at'],
        ], 'id = ?', [$ses['id']]);
    }

    private static function pub(array $ses): array
    {
        return [
            'id' => (int) $ses['id'], 'mode' => $ses['mode'], 'length' => $ses['target_len'], 'n' => $ses['n'],
            'correct' => $ses['n_correct'], 'xp' => $ses['xp'], 'level' => $ses['level'], 'skills' => $ses['skills'],
            'phase' => ($ses['mode'] === 'practice' && $ses['n'] < 3 && empty($ses['state']['smart']) && empty($ses['state']['comeback'])) ? 'diagnostic' : 'adaptive',
            'smart' => !empty($ses['state']['smart']),
            'comeback' => !empty($ses['state']['comeback']),
            'bonus' => isset($ses['state']['bonus_from']),
        ];
    }

    private static function pickNext(array &$ses): ?array
    {
        $st = $ses['state'];
        $served = array_flip($st['served']);
        $placement = $ses['mode'] === 'placement';
        $skills = $ses['skills'];
        $levelIdx = array_search($ses['level'], self::LEVELS);
        $count = count($st['served']);

        $smart = !empty($st['smart']);
        $comeback = !empty($st['comeback']);
        if ($comeback) {
            // each task answers one open mistake: a similar task if there is one, else the task itself
            $mid = $st['queue'][$count] ?? null;
            if ($mid === null) return null;
            if (!empty($st['queue_extra'][$mid])) return Content::item($mid);   // a task added after a gap: already a similar task
            // never another open mistake as the "similar task": it would fix itself and leave the one it stood for
            $open = array_fill_keys(array_keys(Mistakes::scan((int) $ses['user_id'])['open']), true);
            return Mistakes::twin((int) $ses['user_id'], $mid, $served + $open) ?? Content::item($mid);
        }
        // slip or gap: a task like the one just missed comes back soon, in a different sentence (and from other angles when it is missed again)
        if (!$placement && !empty($st['probes'])) {
            foreach ($st['probes'] as $i => $p) {
                if (!empty($p['done']) || !empty($p['served']) || $count < $p['due']) continue;
                $t = Mistakes::twin((int) $ses['user_id'], $p['for'], $served, $p['stage'] > 1, $st['levels'] ?? null, $p['code'] ?? null, $p['max_scaffold'] ?? null, $p['min_scaffold'] ?? null);
                if ($t) {
                    $ses['state']['probes'][$i]['served'] = true;
                    $ses['state']['probes'][$i]['item'] = $t['id'];
                    return $t;
                }
                $ses['state']['probes'][$i]['done'] = true;   // no such task: nothing to ask
            }
        }
        // candidate items
        $rightHere = [];
        foreach ($st['last'] as $h) if ($h['correct'] && ($h['sc'] ?? 0) >= 1) $rightHere[$h['skill']] = true;   // a typed answer, not only a choice
        $bySkill = [];
        $paused = Reports::pausedIds(); // reported tasks wait until the teacher has decided
        foreach (Content::items() as $it) {
            if (!in_array($it['skill'], $skills, true) || isset($served[$it['id']]) || isset($paused[$it['id']])) continue;
            if ($placement && ($it['kind'] === 'write' || $it['bloom'] > 4 || !empty($it['practice_only']))) continue;   // practice only: easy first steps and tasks a hint gives away
            // open writing (the least support) only after a right typed answer on that topic in this session (teacher's scaffolding rule)
            if (!$placement && $it['kind'] === 'write' && empty($rightHere[$it['skill']])) continue;
            if (!empty($st['levels']) && !in_array($it['level'], $st['levels'], true)) continue;   // the levels the learner chose
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

        // placement: first a staircase of 3-question blocks, one full level at a time; when it has found the ceiling, questions near the ability fitted so far
        $pl = $placement ? ($st['pl'] ?? null) : null;
        $stairs = $pl && empty($pl['done']);
        $theta = 3.0;
        if ($placement && $st['last']) $theta = self::fitAbility(array_map(fn($h) => [$h['d'], $h['correct']], $st['last']));
        elseif ($placement) $theta = $st['g'];
        if ($stairs) {
            foreach ($bySkill as $s => $list) {
                $list = array_values(array_filter($list, fn($it) => substr($it['level'], 0, 2) === $pl['lv']));
                if ($list) $bySkill[$s] = $list; else unset($bySkill[$s]);
            }
            if (!$bySkill) {   // nothing left at this level: the staircase ends here
                $ses['state']['pl']['done'] = true;
                return self::pickNext($ses);
            }
        } elseif ($placement) {
            // leave out topics whose easiest task is far too hard for the ability found (unless that would leave nothing)
            $near = array_filter($bySkill, fn($list) => min(array_column($list, 'd')) <= $theta + 1.0);
            if ($near) $bySkill = $near;
        }

        // choose the skill: least used so far; in placement, skills just answered wrongly are re-checked first
        $lastWrong = [];
        foreach ($st['last'] as $h) $lastWrong[$h['skill']] = !$h['correct'];
        $missedHere = [];   // second block at a level: topics missed in the first block come back with a different sentence
        if ($stairs && $pl['bn'] >= 1) foreach ($st['last'] as $h) if ($h['level'] === $pl['lv']) $missedHere[$h['skill']] = !$h['correct'];
        $bestSkill = null;
        $bestScore = PHP_FLOAT_MAX;
        foreach ($bySkill as $s => $list) {
            $score = $skillCount[$s] * 10 + (random_int(0, 99) / 100);
            if ($stairs) { if (!empty($missedHere[$s])) $score -= 6; }
            elseif ($placement && $skillCount[$s] > 0 && !empty($lastWrong[$s])) $score -= 4;
            if ($score < $bestScore) { $bestScore = $score; $bestSkill = $s; }
        }
        // placement: every topic competes on closeness to the target level or ability, with a push towards topics not used much yet
        $soft = $placement;
        $pool = $soft ? array_merge(...array_values($bySkill)) : $bySkill[$bestSkill];

        // recent history penalty
        // how often (and how lately) the learner has met each task: new tasks come first, so the same sentences do not return again and again
        $times = [];
        $lastSeen = [];
        foreach (Db::all('SELECT item_id, COUNT(1) AS c, MAX(created_at) AS t FROM attempts WHERE user_id = ? GROUP BY item_id', [$ses['user_id']]) as $r) {
            $times[$r['item_id']] = (int) $r['c'];
            $lastSeen[$r['item_id']] = (int) $r['t'];
        }

        // tasks the learner got wrong, and tasks like them, come back now and then (never right after the mistake, never more than one in four)
        $missed = [];
        if (!$placement) {
            $recentIds = [];
            foreach (Db::all('SELECT item_id FROM attempts WHERE user_id = ? AND created_at > ?', [$ses['user_id'], time() - 1200]) as $r) $recentIds[$r['item_id']] = true;
            $inSession = 0;
            foreach ($st['served'] as $sid2) if (!empty($st['returned'][$sid2])) $inSession++;
            if ($inSession * 4 <= $count) {
                foreach (Mistakes::scan((int) $ses['user_id'])['open'] as $mid => $m) {
                    if (!isset($recentIds[$mid])) $missed[$mid] = $m;
                }
            }
        }
        // a similar mix of question types in every session: choose / drag (word order, matching, word bank) / type a word / type the sentence / open writing
        $mixCount = ['choose' => 0, 'drag' => 0, 'word' => 0, 'sentence' => 0, 'write' => 0];
        foreach ($st['served'] as $sid2) { $q = Content::item($sid2); if ($q) $mixCount[self::typeGroup($q)]++; }
        $served_n = max(1, array_sum($mixCount));
        $recentQ = [];
        foreach (array_slice($st['served'], -3) as $sid2) { $q = Content::item($sid2); if ($q) $recentQ[mb_strtolower($q['q'])] = true; }

        // target difficulty
        if (!$placement && !$smart && $count < 3) {
            $target = Content::BASE[$ses['level']] + 0.2 * $count; // diagnostic: Bloom 1, 2, 3 at the chosen level
        } else {
            if ($stairs) $target = Content::BASE[$pl['lv'] . ($pl['lv'] === $pl['ladder'][0] ? '.2' : '.1')] ?? $theta;
            elseif ($placement) $target = $theta + 0.05;   // the most informative task is one the learner has a 50-50 chance on
            else {
                $theta = $st['theta'][$bestSkill] ?? Content::BASE[$ses['level']] + 0.3;
                $target = $theta + 0.1;
            }
        }

        $contrastServed = 0;
        foreach ($st['served'] as $sid2) { $q = Content::item($sid2); if ($q && !empty($q['also']) && array_intersect($q['also'], $skills)) $contrastServed++; }
        $areaOf = fn($sid) => Content::skill($sid)['area'] ?? '';
        $areaCount = [];
        foreach ($st['last'] as $h) $areaCount[$areaOf($h['skill'])] = ($areaCount[$areaOf($h['skill'])] ?? 0) + 1;
        $areaCap = max(2, (int) ceil(0.2 * (int) $ses['target_len']));
        $best = null;
        $bestCost = PHP_FLOAT_MAX;
        foreach ($pool as $it) {
            $cost = abs($it['d'] - $target) + 0.2 * $bloomCount[$it['bloom']] + random_int(0, 25) / 100;
            if ($soft) {
                $cost += ($stairs ? 0.6 : 0.3) * $skillCount[$it['skill']];
                if (($areaCount[$areaOf($it['skill'])] ?? 0) >= $areaCap) $cost += $stairs ? 0.3 : 1.2;   // in a block, different topics come first   // one area (e.g. conditionals) not much more than a fifth of the test (teacher's feedback, 27 October)
                if ($stairs) { if (!empty($missedHere[$it['skill']])) $cost -= 1.2; }   // a topic missed a moment ago is checked again with a new sentence
                elseif ($skillCount[$it['skill']] > 0 && !empty($lastWrong[$it['skill']])) $cost -= 0.5;
                $cost -= 0.1 * $bloomCount[$it['bloom']] + random_int(0, 15) / 100;   // keep it close to the target: fewer random jumps
            }
            if (isset($missed[$it['id']])) $cost -= 0.8; // the task itself, a while later
            else if (isset($times[$it['id']])) $cost += 2.0 + 0.35 * min(3, $times[$it['id']]) + ((time() - $lastSeen[$it['id']]) < 7 * 86400 ? 0.4 : 0); // met before: only when nothing new is in reach
            if (!isset($missed[$it['id']])) foreach ($missed as $m) {
                if ($m['skill'] === $it['skill'] && !isset($times[$it['id']]) && $it['bloom'] >= $m['bloom'] - 1 && $it['bloom'] <= $m['bloom'] + 1) { $cost -= 0.4; break; } // a fresh task like it
            }
            if (isset($recentQ[mb_strtolower($it['q'])])) $cost += 0.5; // not the same instruction again and again
            // two or more topics chosen: about a third of the questions compare them (a task that names another chosen topic; teacher, 27 October)
            if (!$placement && !empty($it['also']) && array_intersect($it['also'], $skills)) $cost += $contrastServed < (int) ceil((int) $ses['target_len'] / 3) ? -0.7 : 0.2;
            if (!$placement && $count > 0) { // over its share so far: less likely; under its share: more likely
                $grp = self::typeGroup($it);
                $cost += max(-0.5, min(0.9, 2.0 * (($mixCount[$grp] + 1) / ($served_n + 1) - self::MIX[$grp]))) + ($grp === 'write' ? 0.6 : 0);
                if ($grp === 'sentence' && $mixCount['sentence'] >= (int) ceil(0.1 * ($served_n + 10))) $cost += 3.0; // typing whole sentences stays at about one in ten, even when other tasks pull the other way
            }
            if ($st['last'] && end($st['last'])['bloom'] === $it['bloom']) $cost += 0.3; // avoid the same thinking level twice in a row
            if (!$placement && !$smart && $count < 3 && $it['level'] !== $ses['level']) $cost += 0.5;
            if ($cost < $bestCost) { $bestCost = $cost; $best = $it; }
        }
        if ($best && isset($missed[$best['id']])) $ses['state']['returned'] = ($st['returned'] ?? []) + [$best['id'] => 1];
        return $best;
    }

    /**
     * Second Chance: a task that stood for a mistake is missed again = a gap. The session keeps the length the learner chose
     * (Cowork test, 26 October: 3 questions must not turn into 5 and 7); the mistake is remembered, and the optional bonus
     * question at the end is about it. Returns true for a gap.
     */
    private static function comebackGap(array &$st, array &$ses, string $itemId, bool $ok): bool
    {
        $idx = count($st['served']) - 1;
        $for = $st['queue'][$idx] ?? null;
        if ($for === null) return false;
        if (!empty($st['queue_extra'][$for])) {   // a bonus task: only noted for the evidence
            $st['probe_log'][] = ['for' => $st['queue_extra'][$for], 'item' => $itemId, 'stage' => 2, 'ok' => $ok];
            return false;
        }
        $st['probe_log'][] = ['for' => $for, 'item' => $itemId, 'stage' => 1, 'ok' => $ok];
        if ($ok) return false;
        $st['refail'][$for] = true;
        return true;
    }

    /** How many bonus questions a finished Second Chance offers: 1 after 1-3 mistakes, 2 after 4 or more (teacher's rule, 26 October). */
    private static function bonusCount(array $ses): int
    {
        $st = $ses['state'];
        if (empty($st['comeback']) || isset($st['bonus_from'])) return 0;
        $n = count(array_filter($st['queue'], fn($q) => empty($st['queue_extra'][$q]) && empty($st['review'][$q])));
        return $n >= 4 ? 2 : ($n >= 1 ? 1 : 0);
    }

    /**
     * The learner chose the bonus after Second Chance: the same session goes on with 1 or 2 more questions (double XP).
     * A mistake missed again in the session: a new sentence for that mistake. All fixed: one task of similar difficulty on the same topics.
     */
    public static function bonus(int $uid, int $sid): array
    {
        $ses = self::load($uid, $sid);
        $k = self::bonusCount($ses);
        if ($ses['ended_at'] === null || $k < 1 || (int) $ses['ended_at'] < time() - 3600) throw new ApiError('No bonus questions here.', 409);
        $st = &$ses['state'];
        $skip = array_flip($st['served']) + array_fill_keys(array_keys(Mistakes::scan($uid)['open']), true);
        $mistakes = array_values(array_filter($st['queue'], fn($q) => empty($st['queue_extra'][$q]) && empty($st['review'][$q])));
        $missed = array_values(array_filter($mistakes, fn($q) => !empty($st['refail'][$q])));
        $order = array_merge($missed, array_values(array_diff($mistakes, $missed)));
        $add = [];
        foreach ($order as $i => $mid) {
            if (count($add) >= $k) break;
            $isMissed = $i < count($missed);
            if (!$isMissed && $add) break;   // all fixed: one task of similar difficulty is enough
            $t = Mistakes::twin($uid, $mid, $skip, !$isMissed);
            if (!$t) continue;
            $skip[$t['id']] = true; $add[] = $t['id']; $st['queue_extra'][$t['id']] = $mid;
        }
        if (!$add) throw new ApiError('No bonus questions here.', 409);
        $st['bonus_from'] = count($st['served']);
        $st['queue'] = array_merge(array_slice($st['queue'], 0, count($st['served'])), $add);
        $ses['target_len'] = $ses['n'] + count($add);
        $ses['ended_at'] = null;
        $item = Content::item($add[0]);
        $st['current'] = $item['id'];
        $st['served'][] = $item['id'];
        self::save($ses);
        return ['session' => self::pub($ses), 'item' => Content::publicItem($item, $st['seed'] + count($st['served']))];
    }

    /** A wrong answer in practice: ask a task of the same kind again after one or two others (not more than a third of the session, two waiting at most). */
    /**
     * A wrong answer in practice (teacher's plan, 25 October): straight away an easier task for the same kind of mistake (more support:
     * the answer on the screen, or a clue). Not more than two extra tasks for one kind of mistake in a session, and not more than a third
     * of the session, so the learner never gets stuck on one mistake.
     */
    private static function probeSchedule(array &$st, array $item, array $codes, int $served, int $len): void
    {
        $probes = $st['probes'] ?? [];
        $itemId = $item['id'];
        if (count($probes) >= max(2, intdiv($len, 3))) return;
        foreach ($probes as $p) if (($p['for'] === $itemId && empty($p['done'])) || ($p['item'] ?? null) === $itemId) return;   // already waiting, or this task is itself a probe
        $code = null;
        foreach ($codes as $c) if (empty($st['stuck'][$c])) { $code = $c; break; }
        if ($codes && $code === null) return;   // every kind of mistake in this task was already tried twice in this session
        if ($code !== null && count(array_filter($probes, fn($p) => ($p['code'] ?? null) === $code)) >= 2) return;
        $sc = Content::scaffold($item);
        $st['probes'][] = ['for' => $itemId, 'code' => $code, 'stage' => 1, 'due' => $served, 'max_scaffold' => max(0, $sc - 1)];
    }

    /**
     * The answered task was a probe. The easier task right: a task with the same support as the missed one comes back a little later.
     * The easier task wrong: a gap. That kind of mistake is not asked again in this session (it goes to the learner's plan). Returns true for a gap.
     */
    private static function probeAnswered(array &$st, string $itemId, bool $ok, array $ses): bool
    {
        foreach ($st['probes'] ?? [] as $i => $p) {
            if (empty($p['served']) || ($p['item'] ?? null) !== $itemId || !empty($p['done'])) continue;
            $st['probes'][$i]['done'] = true;
            $st['probe_log'][] = ['for' => $p['for'], 'item' => $itemId, 'stage' => $p['stage'], 'ok' => $ok];
            $code = $p['code'] ?? null;
            if (!$ok) {
                if ($code !== null) $st['stuck'][$code] = true;
                return $p['stage'] === 1;
            }
            if ($p['stage'] === 1) {
                $orig = Content::item($p['for']);
                $st['probes'][] = ['for' => $p['for'], 'code' => $code, 'stage' => 2, 'due' => count($st['served']) + 2 + random_int(0, 1),
                                   'min_scaffold' => $orig ? Content::scaffold($orig) : 0];
            }
            return false;
        }
        return false;
    }

    /**
     * Placement staircase. A block is 3 questions at one full level, each on a different topic.
     * 2 of 3 right: up to the next level. Fewer: one more block at the same level (the topics missed come back with a new sentence);
     * the level is passed when 4 of the 6 are right, otherwise it is the ceiling and the staircase ends.
     */
    private static function plAdvance(array &$st, string $full, bool $ok): void
    {
        if (empty($st['pl']) || !empty($st['pl']['done']) || $st['pl']['lv'] !== $full) return;
        $p = &$st['pl'];
        $p['n']++; $p['nn']++;
        if ($ok) { $p['c']++; $p['cc']++; }
        if ($p['n'] < 3) return;
        $p['bn']++;
        $pass = $p['bn'] === 1 ? $p['c'] >= (!empty($p['strict']) ? 3 : 2) : $p['cc'] >= 4;   // the quick test climbs only on 3 of 3 (Cowork test, 26 October)
        if ($pass && $p['bn'] === 1 && !empty($p['long']) && $p['lv'] === $p['ladder'][0]) { $p['n'] = 0; $p['c'] = 0; return; }   // full test: a second block at the first level
        if ($pass) {
            $p['passed'][] = $p['lv'];
            $i = array_search($p['lv'], $p['ladder'], true);
            if (!isset($p['ladder'][$i + 1])) { $p['done'] = true; return; }
            $p['lv'] = $p['ladder'][$i + 1];
            $p['n'] = $p['c'] = $p['nn'] = $p['cc'] = $p['bn'] = 0;
        } elseif ($p['bn'] === 1) {
            $p['n'] = 0; $p['c'] = 0;
        } else {
            $p['done'] = true;
            $p['ceiling'] = $p['lv'];
        }
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
            // how this topic went before today's session: only shown when there is enough history to be fair
            $before = Db::all('SELECT correct FROM attempts WHERE user_id = ? AND skill = ? AND created_at < ? ORDER BY id DESC LIMIT 20', [$ses['user_id'], $s, $ses['started_at']]);
            $prev = count($before) >= 6 ? (int) round(100 * array_sum(array_column($before, 'correct')) / count($before)) : null;
            $skills[] = [
                'id' => $s, 'label' => $meta['label'], 'area' => $meta['area'], 'n' => $v['n'], 'correct' => $v['c'],
                'theta' => round($theta, 2), 'level_est' => Content::levelFromTheta($theta, $meta['levels']), 'prev_accuracy' => $prev,
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
        if ($ses['mode'] !== 'placement') {
            $m = Mistakes::scan((int) $ses['user_id']);
            $out['fixed'] = (int) ($ses['state']['fixed'] ?? 0);
            $out['comeback'] = !empty($ses['state']['comeback']);
            $out['open_after'] = count($m['open']);
            $out['fixed_total'] = $m['fixed'];
            $out['bonus'] = self::bonusCount($ses);
            $out['locked'] = (int) ($ses['state']['locked'] ?? 0);   // fixed earlier and still right a few days later
            $out['bonus_done'] = isset($ses['state']['bonus_from']);
            $q = Mistakes::queue((int) $ses['user_id'], 1);   // what comes next time: the topic of the oldest open mistake
            $nextSkill = $q ? Content::skill(Content::item($q[0])['skill']) : null;
            $out['next_topic'] = $nextSkill ? $nextSkill['label'] : null;
        }

        if ($ses['mode'] === 'placement') {
            $tested = array_column($skills, 'id');
            // The overall level is fitted to all the answers at once (not to the path the test took), so a strong learner
            // is not held back by the order in which tasks were served.
            $pts = [];
            foreach ($rows as $r) $pts[] = [Content::difficulty($r['level'], (int) $r['bloom']), (int) $r['correct']];
            $overall = $pts ? self::fitAbility($pts) : $ses['state']['g'];
            $out['overall_level'] = Content::levelFromAbility($overall);
            $out['overall_theta'] = round($overall, 2);
            // safety net: a level is not given when fewer than 40% of its questions (5 or more asked) were right: many right answers to hard
            // B1 questions must not make "about B2" when most B2 questions were missed (full test report, 25 October)
            $fullOrder = array_flip(Content::FULL_LEVELS);
            $perFull = [];
            foreach ($rows as $r) { $f = substr($r['level'], 0, 2); $perFull[$f]['n'] = ($perFull[$f]['n'] ?? 0) + 1; $perFull[$f]['c'] = ($perFull[$f]['c'] ?? 0) + (int) $r['correct']; }
            uksort($perFull, fn($a, $b) => ($fullOrder[$a] ?? 0) <=> ($fullOrder[$b] ?? 0));
            foreach ($perFull as $f => $v) {
                if ($v['n'] < 5 || $v['c'] / $v['n'] >= 0.4) continue;
                if (($fullOrder[substr($out['overall_level'], 0, 2)] ?? 0) >= ($fullOrder[$f] ?? 0)) {
                    $below = Content::FULL_LEVELS[max(0, ($fullOrder[$f] ?? 0) - 1)];
                    $out['overall_level'] = isset(Content::BASE[$below . '.2']) ? $below . '.2' : array_key_first(Content::BASE);
                }
                break;
            }
            // gaps: topics missed at or below the level found (a miss above it is simply "not yet"), most missed first, lowest level first
            $fullIdx = array_flip(Content::FULL_LEVELS);
            $top = $fullIdx[substr($out['overall_level'], 0, 2)] ?? 0;
            $by = [];
            foreach ($rows as $r) {
                $f = substr($r['level'], 0, 2);
                if (($fullIdx[$f] ?? 99) > $top) continue;
                $g = &$by[$r['skill']];
                $g['n'] = ($g['n'] ?? 0) + 1;
                if (!$r['correct']) { $g['miss'] = ($g['miss'] ?? 0) + 1; $g['low'] = min($g['low'] ?? 99, $fullIdx[$f] ?? 99); }
                unset($g);
            }
            $cand = [];
            foreach ($by as $sid => $g) if (!empty($g['miss'])) $cand[] = ['id' => $sid, 'miss' => $g['miss'], 'n' => $g['n'], 'low' => $g['low']];
            usort($cand, fn($a, $b) => [$b['miss'], $a['low']] <=> [$a['miss'], $b['low']]);
            $gaps = [];
            foreach (array_slice($cand, 0, 3) as $c) {
                $lvl = Content::FULL_LEVELS[$c['low']];
                $gaps[] = ['id' => $c['id'], 'label' => Content::skill($c['id'])['label'], 'level' => $lvl,
                    'why' => $c['miss'] === $c['n'] ? "Missed {$c['miss']} " . ($c['miss'] === 1 ? 'question' : 'questions') : "Missed {$c['miss']} of {$c['n']} questions"];
            }
            // how each level went, and how sure the result is
            $ladder = [];
            foreach ($rows as $r) {
                $f = substr($r['level'], 0, 2);
                $ladder[$f]['level'] = $f;
                $ladder[$f]['n'] = ($ladder[$f]['n'] ?? 0) + 1;
                $ladder[$f]['correct'] = ($ladder[$f]['correct'] ?? 0) + (int) $r['correct'];
            }
            uksort($ladder, fn($a, $b) => ($fullIdx[$a] ?? 0) <=> ($fullIdx[$b] ?? 0));
            $out['ladder'] = array_values($ladder);
            $info = 0.0;
            foreach ($pts as [$d, $ok]) { $p = 1 / (1 + exp(-1.7 * ($overall - $d))); $info += 2.89 * $p * (1 - $p); }
            $se = 1 / sqrt($info + 1 / 9);
            $out['sure'] = $se < 0.32 ? 'high' : ($se < 0.46 ? 'good' : 'rough');
            $pm = Mistakes::scan((int) $ses['user_id'], [(int) $ses['id'] => $out['overall_level']]);
            $out['open_after'] = count($pm['open']);
            $out['parked'] = count($pm['parked']);   // missed above the level found: kept for later, not offered now
            $pl = $ses['state']['pl'] ?? null;
            $out['basics'] = $pl && ($pl['ceiling'] ?? null) === $pl['ladder'][0];   // failed even the first level: start with its basics
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
                    $next[] = ['type' => 'level_up', 'level' => $levels[$idx + 1], 'text' => "Great accuracy! Try something harder."];
                }
            }
            $out['next'] = array_slice($next, 0, 3);
            $out['level'] = $ses['level'];
        }
        return $out;
    }
}
