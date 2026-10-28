<?php
/**
 * My learning path (teacher, 28 October; docs/LEARNING-PATH.md).
 * A fixed topic order from the course books, combined with what the learner has shown:
 * a step is done only when every topic in it is mastered (80% of the last 10 answers, a recognise task
 * and a use/write task among the right ones, one of them typed, right answers on two different days).
 * Steps below the placement level are not skipped: they ask for a short check first.
 * Combination steps (two tenses mixed) open when the steps they need are done.
 */
final class Path
{
    /** [id, label, level, topics, needs (combination steps only)] */
    private const STEPS = [
        ['ps1', 'Present simple', 'A2', ['present_simple']],
        ['ps2', 'He works, she doesn\'t', 'A2', ['agreement']],
        ['pl', 'Plurals', 'A2', ['irregular_plurals']],
        ['art1', 'A, an, some, any', 'A2', ['articles', 'quantity']],
        ['freq', 'Always, usually, never', 'A2', ['adverbs']],
        ['ing1', 'Like, love, hate + -ing', 'A2', ['verb_patterns']],
        ['ptp', 'In, on, at', 'A2', ['prep_time_place']],
        ['pa', 'Past simple', 'A2', ['past_simple']],
        ['pc', 'Past continuous', 'A2', ['past_continuous']],
        ['soq', 'Questions: word order', 'A2', ['subject_object_q']],
        ['prc', 'Present continuous', 'A2', ['present_continuous']],
        ['cmp', 'Comparison', 'A2', ['comparison']],
        ['mod', 'Should, must, have to', 'A2', ['modal_verbs']],
        ['fut1', 'Going to, will', 'A2', ['future']],
        ['pp', 'Present perfect', 'A2', ['present_perfect']],
        ['c01', 'Zero and first conditional', 'A2', ['cond_zero', 'cond_first']],
        ['dep', 'Listen to, good at', 'A2', ['dep_prepositions']],
        ['two', 'Give me, tell her', 'A2', ['two_objects']],
        ['psp', 'Present simple passive', 'A2', ['present_simple_passive']],
        ['ut', 'Used to', 'B1', ['used_to']],
        ['ppc', 'Present perfect continuous', 'B1', ['present_perfect_continuous']],
        ['ind', 'Someone, anything, nobody', 'B1', ['indefinite_pronouns']],
        ['rel', 'Relative clauses', 'B1', ['relative_clauses']],
        ['tc', 'Time clauses', 'B1', ['time_clauses']],
        ['mm', 'Might, could, be able to', 'B1', ['more_modals']],
        ['c2', 'Second conditional', 'B1', ['cond_second']],
        ['qt', 'Question tags', 'B1', ['question_tags']],
        ['pap', 'Past perfect', 'B1', ['past_perfect']],
        ['pas', 'Passive in other tenses', 'B1', ['past_simple_passive', 'present_continuous_passive', 'present_perfect_passive', 'future_passive']],
        ['pmod', 'Passive with modals', 'B1', ['passive_modals']],
        ['rs', 'Reported statements', 'B1', ['rep_statements']],
        ['rq', 'Reported questions', 'B1', ['rep_questions']],
        ['iq', 'Indirect questions', 'B1', ['ind_polite']],
        ['caus', 'Have something done', 'B1', ['causative']],
        ['adj', 'Bored or boring, adjective order', 'B1', ['adj_ed_ing', 'adj_order']],
        ['ss', 'So and such', 'B1', ['so_such']],
        ['c3', 'Third conditional', 'B1', ['cond_third']],
        ['rv', 'Reporting verbs', 'B2', ['rep_verbs']],
        ['ia', 'Indirect questions, more', 'B2', ['ind_advanced']],
        ['cm', 'Mixed conditionals', 'B2', ['cond_mixed']],
        ['ca', 'Wish, unless, inversion', 'B2', ['cond_advanced']],
        // combination steps: open when the steps in "needs" are done
        ['x_pspc', 'Present simple or continuous', 'A2', ['present_simple', 'present_continuous'], ['ps1', 'prc']],
        ['x_papc', 'Past simple or continuous', 'A2', ['past_simple', 'past_continuous'], ['pa', 'pc']],
        ['x_pppa', 'Present perfect or past simple', 'B1', ['present_perfect', 'past_simple'], ['pp', 'pa']],
        ['x_c012', 'Zero, first or second conditional', 'B1', ['cond_zero', 'cond_first', 'cond_second'], ['c01', 'c2']],
        ['x_ppc', 'Present perfect simple or continuous', 'B1', ['present_perfect', 'present_perfect_continuous'], ['pp', 'ppc']],
        ['x_narr', 'Telling a story (narrative tenses)', 'B1', ['past_simple', 'past_continuous', 'past_perfect'], ['pa', 'pc', 'pap']],
        ['x_rep', 'Reported speech, all of it', 'B1', ['rep_statements', 'rep_questions'], ['rs', 'rq']],
        ['x_c23m', 'Second, third or mixed conditional', 'B2', ['cond_second', 'cond_third', 'cond_mixed'], ['c2', 'c3', 'cm']],
    ];
    private const LEVELS = ['A2', 'B1', 'B2', 'C1'];
    private const FRESH_DAYS = 21;   // a mastered topic asks for a refresh after three weeks without practice

    /** Mastery of one topic from the learner's last 10 answers in it. */
    public static function mastery(int $uid, string $skill): array
    {
        $rows = Db::all('SELECT item_id, correct, bloom, created_at FROM attempts WHERE user_id = ? AND skill = ? ORDER BY id DESC LIMIT 10', [$uid, $skill]);
        $n = count($rows);
        $ok = 0; $recognise = false; $use = false; $typed = false; $days = [];
        foreach ($rows as $r) {
            if (!(int) $r['correct']) continue;
            $ok++;
            $it = Content::item((string) $r['item_id']);
            if (Content::taskCat($it) === 'recognise') $recognise = true; else $use = true;
            if ($it && in_array($it['kind'], ['text', 'write'], true)) $typed = true;
            if ($it && $it['kind'] === 'gap' && empty($it['bank'])) $typed = true;
            $days[date('Y-m-d', (int) $r['created_at'])] = true;
        }
        $pct = $n ? (int) round(100 * $ok / $n) : null;
        $met = $n >= 8 && $pct >= 80 && $recognise && $use && $typed && count($days) >= 2;
        $all = Db::one('SELECT COUNT(1) AS n, SUM(correct) AS c, MAX(created_at) AS last FROM attempts WHERE user_id = ? AND skill = ?', [$uid, $skill]);
        $fresh = $all && (int) $all['last'] > time() - self::FRESH_DAYS * 86400;
        // accuracy for the colour: every answer in the topic; mastery fades when the topic has not been practised for a while (teacher, 28 October)
        return ['n' => (int) ($all['n'] ?? 0), 'pct' => (int) ($all['n'] ?? 0) ? (int) round(100 * (int) $all['c'] / (int) $all['n']) : null,
                'done' => $met && $fresh, 'stale' => $met && !$fresh];
    }

    public static function forUser(int $uid): array
    {
        $counts = Content::levelCounts()['by_skill'];
        $placed = null;
        $pr = Db::one("SELECT state FROM psessions WHERE user_id = ? AND mode = 'placement' AND ended_at IS NOT NULL ORDER BY id DESC LIMIT 1", [$uid]);
        if ($pr) { $st = json_decode((string) $pr['state'], true); if (!empty($st['report']['overall_level'])) $placed = substr($st['report']['overall_level'], 0, 2); }
        $placedIdx = $placed === null ? -1 : array_search($placed, self::LEVELS, true);
        $m = [];
        $steps = [];
        $doneIds = [];
        foreach (self::STEPS as $s) {
            $topics = array_values(array_filter($s[3], fn($t) => !empty($counts[$t])));   // only topics that have tasks
            if (!$topics) continue;
            foreach ($topics as $t) if (!isset($m[$t])) $m[$t] = self::mastery($uid, $t);
            $n = 0; $pctSum = 0; $pctN = 0; $done = true; $stale = false;
            foreach ($topics as $t) { $n += $m[$t]['n']; if ($m[$t]['pct'] !== null) { $pctSum += $m[$t]['pct']; $pctN++; } $done = $done && $m[$t]['done']; $stale = $stale || $m[$t]['stale']; }
            $needs = $s[4] ?? null;
            if ($done) $doneIds[$s[0]] = true;
            $steps[] = ['id' => $s[0], 'label' => $s[1], 'level' => $s[2], 'topics' => $topics, 'needs' => $needs, 'done' => $done,
                        'answers' => $n, 'pct' => $pctN ? (int) round($pctSum / $pctN) : null, 'stale' => !$done && $stale,
                        'below' => $placedIdx > array_search($s[2], self::LEVELS, true)];
        }
        // order: the main steps, each combination step right after the last step it needs; status from the order
        $main = array_values(array_filter($steps, fn($s) => !$s['needs']));
        $combo = array_values(array_filter($steps, fn($s) => (bool) $s['needs']));
        $pos = array_flip(array_column($main, 'id'));
        $ordered = [];
        foreach ($main as $i => $s) {
            $ordered[] = $s;
            foreach ($combo as $c) {   // after the last of its parts in the main order
                $last = max(array_map(fn($id) => $pos[$id] ?? -1, $c['needs']));
                if ($last === $i) $ordered[] = $c;
            }
        }
        // every step can be opened; the path only recommends (teacher, 28 October): the first step in the book order that is not done
        $labels = array_column($main, 'label', 'id');
        $current = null;
        foreach ($ordered as &$s) {
            $s['best_after'] = $s['needs'] ? array_values(array_map(fn($id) => $labels[$id] ?? $id, array_diff($s['needs'], array_keys($doneIds)))) : [];
            $s['status'] = $s['done'] ? 'done' : ($s['stale'] ? 'refresh' : ($s['answers'] ? 'work' : 'new'));
            if ($current === null && !$s['done'] && !$s['best_after'] && ($s['pct'] === null || $s['pct'] < 80 || $s['stale'])) $current = $s['id'];   // weak, untried or due for a refresh
        }
        unset($s);
        return ['placed' => $placed, 'current' => $current, 'steps' => $ordered,
                'done' => count(array_filter($ordered, fn($s) => $s['status'] === 'done')), 'total' => count($ordered)];
    }
}
