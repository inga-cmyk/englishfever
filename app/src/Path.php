<?php
/**
 * My learning path (teacher, 2 November; docs/LEVEL-LISTS-test-english.md).
 * One path per level, in the order of the test-english.com lists the teacher gave: the A1 list is our A2.1 basics, then
 * A2 (A2.2), B1, B1+ (B1.2-B2.1), B2 and C1. A topic comes back at a higher level with that level's tasks.
 * Every step uses only the tasks of its level; a topic without tasks there uses the nearest lower level that has some
 * (listed as "needs tasks"); a topic the app does not have yet is left out until it has tasks.
 * A step is done when every topic in it is mastered at that level (80% of the last 10 answers at those levels, a
 * recognise task and a use/write task among the right ones, one of them typed, right answers on two different days).
 * Steps below the placement level are not skipped: they ask for a short check first.
 */
final class Path
{
    /** [id, label, band, topics]; the band decides the task levels (BANDS) */
    private const STEPS = [
        // A2.1: the A1 list (basics)
        ['a1_ps', 'Present simple', 'A2.1', ['present_simple', 'agreement']],
        ['a1_pc', 'Present continuous', 'A2.1', ['present_continuous']],
        ['a1_pspc', 'Present simple or continuous', 'A2.1', ['present_simple', 'present_continuous']],
        ['a1_pa', 'Was, were and the past simple', 'A2.1', ['past_simple']],
        ['a1_fut', 'Will and going to', 'A2.1', ['future']],
        ['a1_can', 'Can, can\'t', 'A2.1', ['modal_verbs']],
        ['a1_ing', 'Like, love + -ing or to', 'A2.1', ['verb_patterns']],
        ['a1_art', 'A / an, the, plurals', 'A2.1', ['articles', 'irregular_plurals']],
        ['a1_qty', 'A, some, any, much, many', 'A2.1', ['quantity']],
        ['a1_adv', 'Adjectives and adverbs, always, usually', 'A2.1', ['adverbs']],
        ['a1_cmp', 'Comparatives and superlatives', 'A2.1', ['comparison']],
        ['a1_conj', 'And, but, or, so, because', 'A2.1', ['conj_basic']],
        ['a1_ptp', 'At, in, on', 'A2.1', ['prep_time_place']],
        ['a1_q', 'Questions: word order', 'A2.1', ['subject_object_q', 'aux_verbs']],
        // A2.2: the A2 list
        ['a2_pspc', 'Present simple or continuous', 'A2.2', ['present_simple', 'present_continuous']],
        ['a2_pp', 'Present perfect', 'A2.2', ['present_perfect']],
        ['a2_pppa', 'Present perfect or past simple', 'A2.2', ['cmp_pp_ps']],
        ['a2_papc', 'Past continuous and past simple', 'A2.2', ['cmp_ps_pc', 'past_continuous']],
        ['a2_pap', 'Past perfect', 'A2.2', ['past_perfect']],
        ['a2_fut', 'Will or going to; plans', 'A2.2', ['future']],
        ['a2_rev', 'Review of all tenses A2', 'A2.2', ['present_simple', 'present_continuous', 'past_simple', 'past_continuous', 'present_perfect', 'future']],
        ['a2_mod', 'Have to, must, should', 'A2.2', ['modal_verbs']],
        ['a2_might', 'Might, may', 'A2.2', ['more_modals']],
        ['a2_ut', 'Used to', 'A2.2', ['used_to']],
        ['a2_two', 'Verbs with two objects', 'A2.2', ['two_objects']],
        ['a2_c1', 'First conditional and time clauses', 'A2.2', ['cond_zero', 'cond_first', 'time_clauses']],
        ['a2_c2', 'Second conditional', 'A2.2', ['cond_second']],
        ['a2_pas', 'Present and past simple passive', 'A2.2', ['present_simple_passive', 'past_simple_passive']],
        ['a2_rep', 'Reported speech', 'A2.2', ['rep_statements']],
        ['a2_ing', 'Infinitives and gerunds', 'A2.2', ['verb_patterns']],
        ['a2_ind', 'Something, anything, nothing', 'A2.2', ['indefinite_pronouns']],
        ['a2_qty', 'Much, many, few, too, enough', 'A2.2', ['quantity']],
        ['a2_rel', 'Defining relative clauses', 'A2.2', ['relative_clauses']],
        ['a2_aux', 'Auxiliary verbs do, be, have', 'A2.2', ['aux_verbs']],
        ['a2_cmp', 'Comparatives and superlatives', 'A2.2', ['comparison']],
        ['a2_conj', 'However, although, because, so, time connectors', 'A2.2', ['conj_linkers']],
        ['a2_q', 'Questions and subject questions', 'A2.2', ['subject_object_q']],
        // B1: the B1 list
        ['b1_pspc', 'Present simple or continuous', 'B1', ['present_simple', 'present_continuous']],
        ['b1_fut', 'Future forms', 'B1', ['future']],
        ['b1_pppa', 'Past simple or present perfect', 'B1', ['cmp_pp_ps', 'present_perfect', 'past_simple']],
        ['b1_ppc', 'Present perfect simple and continuous', 'B1', ['present_perfect', 'present_perfect_continuous']],
        ['b1_cmp', 'Comparatives and superlatives', 'B1', ['comparison']],
        ['b1_art', 'A(n), the, no article', 'B1', ['articles', 'articles_b1']],
        ['b1_can', 'Can, could, be able to', 'B1', ['more_modals']],
        ['b1_mod', 'Have to, must, should', 'B1', ['modal_verbs']],
        ['b1_adj', '-ed and -ing adjectives', 'B1', ['adj_ed_ing']],
        ['b1_narr', 'Past simple, past continuous, past perfect', 'B1', ['cmp_ps_pc', 'past_perfect', 'narrative']],
        ['b1_rev', 'Review of all tenses B1', 'B1', ['present_simple', 'present_continuous', 'past_simple', 'past_continuous', 'present_perfect', 'present_perfect_continuous', 'past_perfect', 'future']],
        ['b1_ut', 'Usually, used to, be used to', 'B1', ['used_to']],
        ['b1_pas', 'Passive', 'B1', ['present_simple_passive', 'past_simple_passive', 'present_continuous_passive', 'present_perfect_passive', 'future_passive']],
        ['b1_c1', 'First conditional and time clauses', 'B1', ['cond_zero', 'cond_first', 'time_clauses']],
        ['b1_c2', 'Second conditional', 'B1', ['cond_second']],
        ['b1_c12', 'First and second conditionals', 'B1', ['cond_first', 'cond_second']],
        ['b1_c3', 'Third conditional', 'B1', ['cond_third']],
        ['b1_rep', 'Reported speech', 'B1', ['rep_statements', 'rep_questions']],
        ['b1_ing', 'Gerund or infinitive', 'B1', ['verb_patterns']],
        ['b1_qty', 'Much, many, a lot, little, few', 'B1', ['quantity']],
        ['b1_ind', 'Any, no, none, someone, nobody', 'B1', ['indefinite_pronouns']],
        ['b1_so', 'So, such', 'B1', ['so_such']],
        ['b1_rel', 'Defining and non-defining relative clauses', 'B1', ['relative_clauses']],
        ['b1_qt', 'Question tags', 'B1', ['question_tags']],
        ['b1_conj', 'Contrast, purpose and reason', 'B1', ['conj_clauses']],
        ['b1_dep', 'Verb and adjective + preposition', 'B1', ['dep_prepositions']],
        // B1+: the B1+ list
        ['bp_ppc', 'Present perfect simple or continuous', 'B1+', ['present_perfect', 'present_perfect_continuous']],
        ['bp_narr', 'Narrative tenses', 'B1+', ['narrative', 'narrative_b2']],
        ['bp_ut', 'Used to, be used to, get used to', 'B1+', ['used_to']],
        ['bp_c1', 'Zero and first conditional, time clauses', 'B1+', ['cond_zero', 'cond_first', 'time_clauses']],
        ['bp_c23', 'Second and third conditionals', 'B1+', ['cond_second', 'cond_third']],
        ['bp_wish', 'I wish, if only', 'B1+', ['cond_advanced']],
        ['bp_pas', 'Passive: all tenses', 'B1+', ['present_simple_passive', 'past_simple_passive', 'present_continuous_passive', 'present_perfect_passive', 'future_passive', 'passive_modals']],
        ['bp_caus', 'Have something done', 'B1+', ['causative']],
        ['bp_ing', 'Gerund or infinitive', 'B1+', ['verb_patterns']],
        ['bp_rv', 'Reporting verbs', 'B1+', ['rep_verbs']],
        ['bp_adj', '-ed and -ing adjectives, adjective order', 'B1+', ['adj_ed_ing', 'adj_order']],
        ['bp_so', 'So, such', 'B1+', ['so_such']],
        ['bp_conj', 'Clauses of contrast and purpose', 'B1+', ['conj_clauses']],
        ['bp_q', 'Questions: different types', 'B1+', ['subject_object_q', 'question_tags']],
        ['bp_iq', 'Indirect questions', 'B1+', ['ind_polite']],
        // B2: the B2 list
        ['b2_narr', 'Narrative tenses, used to, would', 'B2', ['narrative_b2', 'used_to']],
        ['b2_fut', 'Future forms', 'B2', ['future']],
        ['b2_mod', 'Modal verbs: permission, obligation, necessity', 'B2', ['modal_verbs', 'more_modals']],
        ['b2_cm', 'Mixed conditionals', 'B2', ['cond_mixed', 'cond_third']],
        ['b2_wish', 'Wish, if only, it\'s time; unless, provided', 'B2', ['cond_advanced']],
        ['b2_vp', 'Verb + object + infinitive or -ing', 'B2', ['verb_patterns', 'rep_verbs']],
        ['b2_rel', 'Relative clauses', 'B2', ['relative_clauses']],
        ['b2_rep', 'Reported questions, indirect questions', 'B2', ['rep_questions', 'ind_advanced']],
        ['b2_cmp', 'Modifying comparatives', 'B2', ['comparison']],
        ['b2_conj', 'Contrast, purpose, reason and result', 'B2', ['conj_clauses']],
        // C1: the C1 list
        ['c1_pspc', 'Advanced present simple and continuous', 'C1', ['present_simple', 'present_continuous']],
        ['c1_past', 'Advanced past tenses', 'C1', ['past_simple', 'past_continuous', 'past_perfect']],
        ['c1_perf', 'The perfect tenses', 'C1', ['present_perfect', 'present_perfect_continuous', 'past_perfect']],
        ['c1_mod', 'Advanced modal verbs', 'C1', ['modal_verbs', 'more_modals']],
        ['c1_agr', 'Subject-verb agreement', 'C1', ['agreement']],
        ['c1_ca', 'Conditionals, inversion, wish', 'C1', ['cond_advanced', 'cond_mixed']],
        ['c1_rv', 'Reporting verbs, indirect questions', 'C1', ['rep_verbs', 'ind_advanced']],
    ];
    /** the task levels of each band; a step's level for the "below the placement level" check is the first two letters */
    private const BANDS = ['A2.1' => ['A2.1'], 'A2.2' => ['A2.2'], 'B1' => ['B1.1', 'B1.2'], 'B1+' => ['B1.2', 'B2.1'],
                           'B2' => ['B2.1', 'B2.2'], 'C1' => ['C1.1', 'C1.2']];
    private const HALVES = ['A2.1', 'A2.2', 'B1.1', 'B1.2', 'B2.1', 'B2.2', 'C1.1', 'C1.2'];
    private const LEVELS = ['A2', 'B1', 'B2', 'C1'];
    private const FRESH_DAYS = 21;   // a mastered topic asks for a refresh after three weeks without practice

    /** The levels a topic uses in a band: its own levels there, else the nearest lower level that has tasks (null: none). */
    public static function topicLevels(string $skill, string $band, array $byHalf): ?array
    {
        $own = array_values(array_filter(self::BANDS[$band], fn($h) => !empty($byHalf[$skill][$h])));
        if ($own) return $own;
        $start = array_search(self::BANDS[$band][0], self::HALVES, true);
        for ($i = $start - 1; $i >= 0; $i--) if (!empty($byHalf[$skill][self::HALVES[$i]])) return [self::HALVES[$i]];
        return null;
    }

    public static function mastery(int $uid, string $skill, ?array $levels = null): array
    {
        $lv = $levels ? ' AND level IN (' . implode(',', array_fill(0, count($levels), '?')) . ')' : '';   // mastery at these levels only: a topic comes back at a higher level
        $p = array_merge([$uid, $skill], $levels ?: []);
        $rows = Db::all("SELECT item_id, correct, bloom, created_at FROM attempts WHERE user_id = ? AND skill = ?$lv ORDER BY id DESC LIMIT 10", $p);
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
        $all = Db::one("SELECT COUNT(1) AS n, SUM(correct) AS c, MAX(created_at) AS last FROM attempts WHERE user_id = ? AND skill = ?$lv", $p);
        $fresh = $all && (int) $all['last'] > time() - self::FRESH_DAYS * 86400;
        // accuracy for the colour: every answer in the topic; mastery fades when the topic has not been practised for a while (teacher, 28 October)
        return ['n' => (int) ($all['n'] ?? 0), 'pct' => (int) ($all['n'] ?? 0) ? (int) round(100 * (int) $all['c'] / (int) $all['n']) : null,
                'done' => $met && $fresh, 'stale' => $met && !$fresh];
    }

    public static function forUser(int $uid): array
    {
        $byHalf = Content::levelCounts()['by_half'];
        $placed = null;
        $pr = Db::one("SELECT state FROM psessions WHERE user_id = ? AND mode = 'placement' AND ended_at IS NOT NULL ORDER BY id DESC LIMIT 1", [$uid]);
        if ($pr) { $st = json_decode((string) $pr['state'], true); if (!empty($st['report']['overall_level'])) $placed = substr($st['report']['overall_level'], 0, 2); }
        $placedIdx = $placed === null ? -1 : array_search($placed, self::LEVELS, true);
        $m = [];
        $steps = [];
        $current = null;
        foreach (self::STEPS as $s) {
            [$id, $label, $band, $want] = $s;
            $topics = []; $levels = []; $fallback = [];
            foreach ($want as $t) {
                $tl = self::topicLevels($t, $band, $byHalf);
                if ($tl === null) continue;   // not in the app yet
                $topics[] = $t; $levels = array_merge($levels, $tl);
                if (!array_intersect($tl, self::BANDS[$band])) $fallback[] = $t;
            }
            if (!$topics) continue;
            $levels = array_values(array_unique($levels)); sort($levels);
            $n = 0; $pctSum = 0; $pctN = 0; $done = true; $stale = false;
            foreach ($topics as $t) {
                $k = $t . '|' . implode(',', $levels);
                $m[$k] ??= self::mastery($uid, $t, $levels);
                $n += $m[$k]['n']; if ($m[$k]['pct'] !== null) { $pctSum += $m[$k]['pct']; $pctN++; }
                $done = $done && $m[$k]['done']; $stale = $stale || $m[$k]['stale'];
            }
            $pct = $pctN ? (int) round($pctSum / $pctN) : null;
            $status = $done ? 'done' : ($stale ? 'refresh' : ($n ? 'work' : 'new'));
            if ($current === null && !$done && ($pct === null || $pct < 80 || $stale)) $current = $id;   // the first step in the book order that is weak, untried or due for a refresh
            $steps[] = ['id' => $id, 'label' => $label, 'level' => $band, 'levels' => $levels, 'topics' => $topics, 'fallback' => $fallback, 'needs' => null, 'best_after' => [],
                        'done' => $done, 'answers' => $n, 'pct' => $pct, 'stale' => !$done && $stale, 'status' => $status,
                        'below' => $placedIdx > array_search(substr($band, 0, 2), self::LEVELS, true)];
        }
        return ['placed' => $placed, 'current' => $current, 'steps' => $steps,
                'done' => count(array_filter($steps, fn($s) => $s['status'] === 'done')), 'total' => count($steps)];
    }
}
