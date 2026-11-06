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
        ['b2_conj', 'Contrast, purpose, reason and result', 'B2', ['conj_b2', 'conj_clauses']],
        // C1: the C1 list
        ['c1_pspc', 'Advanced present simple and continuous', 'C1', ['present_simple', 'present_continuous']],
        ['c1_past', 'Advanced past tenses', 'C1', ['past_simple', 'past_continuous', 'past_perfect']],
        ['c1_perf', 'The perfect tenses', 'C1', ['present_perfect', 'present_perfect_continuous', 'past_perfect']],
        ['c1_mod', 'Advanced modal verbs', 'C1', ['modal_verbs', 'more_modals']],
        ['c1_agr', 'Subject-verb agreement', 'C1', ['agreement']],
        ['c1_ca', 'Conditionals, inversion, wish', 'C1', ['cond_advanced', 'cond_mixed']],
        ['c1_unreal', 'Unreal time and preferences', 'C1', ['unreal_time']],   // it's high time, I'd rather (teacher, 4 November)
        ['c1_rv', 'Reporting verbs, indirect questions', 'C1', ['rep_verbs', 'ind_advanced']],
    ];
    /** the task levels of each band; a step's level for the "below the placement level" check is the first two letters */
    private const BANDS = ['A2.1' => ['A2.1'], 'A2.2' => ['A2.2'], 'B1' => ['B1.1', 'B1.2'], 'B1+' => ['B1.2', 'B2.1'],
                           'B2' => ['B2.1', 'B2.2'], 'C1' => ['C1.1', 'C1.2']];
    private const HALVES = ['A2.1', 'A2.2', 'B1.1', 'B1.2', 'B2.1', 'B2.2', 'C1.1', 'C1.2'];
    private const LEVELS = ['A2', 'B1', 'B2', 'C1'];
    private const FRESH_DAYS = 21;   // a mastered topic asks for a refresh after three weeks without practice

    /** The topics of a full level (A2, B1, B2, C1) in the order of My learning path: the level test asks them in this order (teacher, 3 November). */
    public static function topicOrder(string $level): array
    {
        $out = [];
        foreach (self::STEPS as [$id, $title, $band, $topics]) if (substr($band, 0, 2) === $level) foreach ($topics as $t) $out[$t] ??= count($out);
        return $out;
    }

    /** The levels a topic uses in a band: its own levels there, else the nearest lower level that has tasks (null: none). */
    public static function topicLevels(string $skill, string $band, array $byHalf): ?array
    {
        $own = array_values(array_filter(self::BANDS[$band], fn($h) => !empty($byHalf[$skill][$h])));
        if ($own) return $own;
        $start = array_search(self::BANDS[$band][0], self::HALVES, true);
        for ($i = $start - 1; $i >= 0; $i--) if (!empty($byHalf[$skill][self::HALVES[$i]])) return [self::HALVES[$i]];
        return null;
    }

    /**
     * Mastery of a topic at some levels (teacher, 3 November, rule "1a"): evidence, not the size of the topic.
     * Only check and use tasks count (Content::role); mistakes on corrected tasks do not count (rule C).
     * learned  = at least 10 different tasks answered right, 80% or more of the last 12 answers right, recognise + use +
     *            one typed answer among the right ones, right answers on two different days;
     * mastered = learned, and later (3+ days) three tasks the learner had never seen, all right;
     * confirmed = a quick check passed: the last 3 evidence answers right, on 3 different tasks (used when the topic is
     *            probably known already, e.g. from a higher level or the level test);
     * progress = the green line: different right tasks out of 10, held back while accuracy is under 80%.
     * A topic with fewer than 10 check / use tasks at these levels cannot be learned yet ("almost there").
     */
    public const LEARN_N = 10;
    public static function mastery(int $uid, string $skill, ?array $levels = null): array
    {
        $lv = $levels ? ' AND level IN (' . implode(',', array_fill(0, count($levels), '?')) . ')' : '';
        $p = array_merge([$uid, $skill], $levels ?: []);
        $corrected = Reports::correctedIds();
        $rows = [];   // oldest first, evidence only
        foreach (Db::all("SELECT item_id, correct, created_at FROM attempts WHERE user_id = ? AND skill = ?$lv ORDER BY id ASC", $p) as $r) {
            $it = Content::item((string) $r['item_id']);
            if (!$it || Content::role($it) === 'learn') continue;
            if (!(int) $r['correct'] && isset($corrected[$r['item_id']])) continue;
            $r['it'] = $it; $rows[] = $r;
        }
        $n = count($rows);
        $last = array_slice($rows, -12);
        $acc = $last ? array_sum(array_map(fn($r) => (int) $r['correct'], $last)) / count($last) : 0.0;
        $right = []; $cats = []; $typed = false; $days = []; $firstSeen = [];
        foreach ($rows as $r) {
            $id = preg_replace('/-r\d+$/', '', (string) $r['item_id']);
            $firstSeen[$id] ??= (int) $r['created_at'];
            if (!(int) $r['correct']) continue;
            $right[$id] = true;
            $cats[Content::taskCat($r['it'])] = true;
            if (Content::role($r['it']) === 'use') $typed = true;
            $days[date('Y-m-d', (int) $r['created_at'])] = true;
        }
        static $banks = [];   // check / use tasks per topic and level
        if (!$banks) foreach (Content::items() as $it) if (Content::role($it) !== 'learn') $banks[$it['skill']][$it['level']] = ($banks[$it['skill']][$it['level']] ?? 0) + 1;
        $bank = 0;
        foreach ($banks[$skill] ?? [] as $l => $c) if (!$levels || in_array($l, $levels, true)) $bank += $c;
        $distinct = count($right);
        $learned = $bank >= self::LEARN_N && $distinct >= self::LEARN_N && $acc >= 0.8 && isset($cats['recognise']) && (isset($cats['use']) || isset($cats['write'])) && $typed && count($days) >= 2;
        $mastered = false;
        if ($learned) {   // the day it became learned: the 10th different right task
            $seen = []; $at = null;
            foreach ($rows as $r) { if ((int) $r['correct']) { $seen[preg_replace('/-r\d+$/', '', (string) $r['item_id'])] = true; if (count($seen) >= self::LEARN_N) { $at = (int) $r['created_at']; break; } } }
            $later = array_values(array_filter($rows, fn($r) => $at !== null && (int) $r['created_at'] >= $at + 3 * 86400 && $firstSeen[preg_replace('/-r\d+$/', '', (string) $r['item_id'])] >= $at + 3 * 86400));
            $mastered = count($later) >= 3 && !in_array(0, array_map(fn($r) => (int) $r['correct'], array_slice($later, -3)), true);
        }
        $tail = array_slice($rows, -3);
        $confirmed = count($tail) === 3 && !in_array(0, array_map(fn($r) => (int) $r['correct'], $tail), true)
                     && count(array_unique(array_map(fn($r) => preg_replace('/-r\d+$/', '', (string) $r['item_id']), $tail))) === 3;
        $failedCheck = (bool) array_filter($tail, fn($r) => !(int) $r['correct']);
        $progress = $learned ? 1.0 : min($bank >= self::LEARN_N ? 0.95 : 0.9, ($distinct / self::LEARN_N) * ($acc >= 0.8 || !$last ? 1 : $acc / 0.8));
        $allRow = Db::one("SELECT COUNT(1) AS n, SUM(correct) AS c, MAX(created_at) AS last FROM attempts WHERE user_id = ? AND skill = ?$lv", $p);
        $fresh = $allRow && (int) $allRow['last'] > time() - self::FRESH_DAYS * 86400;
        return ['n' => (int) ($allRow['n'] ?? 0), 'pct' => (int) ($allRow['n'] ?? 0) ? (int) round(100 * (int) $allRow['c'] / (int) $allRow['n']) : null,
                'evidence' => $n, 'distinct' => $distinct, 'acc' => round($acc, 2), 'bank' => $bank,
                'learned' => $learned, 'mastered' => $mastered, 'confirmed' => $confirmed, 'failed_check' => $failedCheck, 'progress' => round($progress, 2),
                'done' => $learned && $fresh, 'stale' => $learned && !$fresh];
    }

    public static function forUser(int $uid): array
    {
        $byHalf = Content::levelCounts()['by_half'];
        $placed = null; $plRight = []; $plWrong = [];
        $pr = Db::one("SELECT id, state FROM psessions WHERE user_id = ? AND mode = 'placement' AND ended_at IS NOT NULL ORDER BY id DESC LIMIT 1", [$uid]);
        if ($pr) {
            $st = json_decode((string) $pr['state'], true);
            if (!empty($st['report']['overall_level'])) $placed = substr($st['report']['overall_level'], 0, 2);
            foreach (Db::all('SELECT skill, correct FROM attempts WHERE psession_id = ?', [(int) $pr['id']]) as $a) { if ((int) $a['correct']) $plRight[$a['skill']] = true; else $plWrong[$a['skill']] = true; }
        }
        $self = false;
        if ($placed === null) {   // no level test yet: start from the level the learner gave (teacher, 6 November)
            $sl = (string) Db::val('SELECT self_level FROM users WHERE id = ?', [$uid]);
            if (in_array($sl, self::LEVELS, true)) { $placed = $sl; $self = true; }
        }
        $placedIdx = $placed === null ? -1 : array_search($placed, self::LEVELS, true);
        // evidence per topic above a level: right answers at higher levels make the lower level probably known (teacher, 3 November)
        $high = [];
        foreach (Db::all('SELECT skill, level, correct, item_id FROM attempts WHERE user_id = ?', [$uid]) as $a) {
            if (Content::role(Content::item((string) $a['item_id'])) === 'learn') continue;
            $h = &$high[$a['skill']][$a['level']]; $h = $h ?? [0, 0]; $h[0]++; $h[1] += (int) $a['correct']; unset($h);
        }
        $strongAbove = function (string $t, array $levels) use ($high): bool {
            $top = max(array_map(fn($l) => (int) array_search($l, self::HALVES, true), $levels));
            $n = 0; $c = 0;
            foreach ($high[$t] ?? [] as $l => [$nn, $cc]) if ((int) array_search($l, self::HALVES, true) > $top) { $n += $nn; $c += $cc; }
            return $n >= 5 && $c / $n >= 0.8;
        };
        $m = [];
        $steps = [];
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
            $bandIdx = array_search(substr($band, 0, 2), self::LEVELS, true);
            $below = $placedIdx > $bandIdx;
            $all = ['learned' => true, 'mastered' => true, 'known' => true, 'likely' => true, 'stale' => false, 'failed' => false];
            $n = 0; $prog = 0.0; $pctSum = 0; $pctN = 0;
            foreach ($topics as $t) {
                $k = $t . '|' . implode(',', $levels);
                $mm = $m[$k] ??= self::mastery($uid, $t, $levels);
                $n += $mm['n']; $prog += $mm['progress']; if ($mm['pct'] !== null) { $pctSum += $mm['pct']; $pctN++; }
                // probably known: below the level found, right in the level test (and not missed there), or strong at a higher level
                $likely = !isset($plWrong[$t]) && ($below || ($placedIdx >= $bandIdx && isset($plRight[$t])) || $strongAbove($t, $levels));
                // not asked in the level test, at or above the level found: a quick check first (teacher, 3 November); passed = known
                $checked = !$likely && $placedIdx >= 0 && $bandIdx >= $placedIdx && !isset($plWrong[$t]) && $mm['evidence'] <= 5 && $mm['confirmed'];
                $all['learned'] = $all['learned'] && $mm['learned'];
                $all['mastered'] = $all['mastered'] && $mm['mastered'];
                $all['known'] = $all['known'] && ($mm['learned'] || ($likely && $mm['confirmed']) || $checked);
                $all['likely'] = $all['likely'] && ($mm['learned'] || $likely);
                $all['stale'] = $all['stale'] || $mm['stale'];
                $all['failed'] = $all['failed'] || ($likely && !$mm['learned'] && $mm['failed_check'] && $mm['evidence'] >= 3);
            }
            $progress = round($prog / count($topics), 2);
            $status = $all['mastered'] ? 'mastered'
                : ($all['learned'] ? ($all['stale'] ? 'refresh' : 'learned')
                : ($all['known'] ? 'known'
                : ($all['failed'] ? 'strengthen'
                : ($all['likely'] ? 'likely' : ($n ? 'work' : 'new')))));
            $done = in_array($status, ['mastered', 'learned', 'known'], true);
            $steps[] = ['id' => $id, 'label' => $label, 'level' => $band, 'levels' => $levels, 'topics' => $topics, 'fallback' => $fallback, 'needs' => null, 'best_after' => [],
                        'done' => $done, 'answers' => $n, 'pct' => $pctN ? (int) round($pctSum / $pctN) : null, 'progress' => $done ? 1.0 : $progress,
                        'stale' => $status === 'refresh', 'status' => $status, 'weak' => $status === 'strengthen',
                        'below' => $status === 'likely', 'band_idx' => $bandIdx,
                        'check' => in_array($status, ['likely', 'new'], true) && $placedIdx >= 0 && $bandIdx >= $placedIdx];   // starts as a 5-task quick check
        }
        // the recommended step (teacher, 3 November): the first logical one, in the order of the path from the level found, even when the
        // level test did not ask it (then it starts as a quick check); a step whose quick check failed comes first.
        $current = null;
        foreach ($steps as $x) if ($x['status'] === 'strengthen') { $current = $x['id']; break; }
        if ($current === null) foreach ($steps as $x) if ($x['band_idx'] >= max(0, $placedIdx) && !$x['done']) { $current = $x['id']; break; }
        if ($current === null) foreach ($steps as $x) if (!$x['done']) { $current = $x['id']; break; }
        foreach ($steps as &$x) unset($x['band_idx']);
        unset($x);
        return ['placed' => $placed, 'placed_by' => $placed === null ? null : ($self ? 'self' : 'test'), 'current' => $current, 'steps' => $steps,
                'done' => count(array_filter($steps, fn($s) => $s['done'])), 'total' => count($steps)];
    }

    /**
     * The mix of a session from My learning path or Surprise me (teacher, 2 November; Vygotsky's zone of proximal development):
     * about 60% the step being learnt at its level, 25% review (weak steps below the learner's level first, then topics with a
     * mistake fixed 2-7 days ago, then steps practised before), 15% the same topics half a level higher.
     * @return array{main: array, review: ?array, stretch: ?array, plan: string[]}
     */
    public static function sessionMix(int $uid, array $skills, array $levels, int $len, ?array $path = null): array
    {
        $path ??= self::forUser($uid);
        $byHalf = Content::levelCounts()['by_half'];
        $ids = array_column($path['steps'], 'id');
        $curPos = false;   // the step being practised (the one started), else the recommended step
        foreach ($path['steps'] as $k => $x) if (!array_diff($skills, $x['topics']) && array_intersect($levels, $x['levels'])) { $curPos = $k; break; }
        if ($curPos === false) $curPos = array_search($path['current'], $ids, true);
        $review = []; $rLevels = [];
        $add = function ($topics, $lv) use (&$review, &$rLevels, $skills) {
            foreach ($topics as $t) if (!in_array($t, $skills, true) && !isset($review[$t]) && count($review) < 3) { $review[$t] = true; $rLevels = array_merge($rLevels, $lv); }
        };
        foreach ($path['steps'] as $x) if ($x['weak']) $add($x['topics'], $x['levels']);   // strengthen the basics
        foreach ($path['steps'] as $x) if ($x['status'] === 'likely') $add($x['topics'], $x['levels']);   // probably known: confirm with a few tasks
        $solid = Mistakes::scan($uid)['solid'] ?? [];
        foreach ($solid as $sv) {   // fixed 2-7 days ago: check it is still right
            $age = (time() - strtotime($sv['day'])) / 86400;
            if ($age >= 2 && $age <= 7) $add([$sv['skill']], [$sv['level']]);
        }
        if ($curPos !== false) foreach (array_reverse(array_slice($path['steps'], 0, (int) $curPos)) as $x) if ($x['answers'] > 0) $add($x['topics'], $x['levels']);   // practised before
        $halves = ['A2.1', 'A2.2', 'B1.1', 'B1.2', 'B2.1', 'B2.2', 'C1.1', 'C1.2'];
        $top = max(array_map(fn($l) => (int) array_search($l, $halves, true), $levels ?: ['A2.1']));
        $up = $halves[$top + 1] ?? null;
        $stretch = $up ? array_values(array_filter($skills, fn($t) => !empty($byHalf[$t][$up]))) : [];
        $n = max(5, $len);
        $nS = $stretch ? max(1, (int) floor(0.15 * $n)) : 0;   // 10 tasks: 6 step, 3 review, 1 step up
        $nR = $review ? (int) round(0.25 * $n) : 0;
        $nM = $n - $nS - $nR;
        // the first two tasks are the step itself; review and stretch are spread through the rest
        $plan = array_merge(array_fill(0, $nM, 'main'));
        $extra = array_merge(array_fill(0, $nR, 'review'), array_fill(0, $nS, 'stretch'));
        if ($extra) {
            $step = ($n - 2) / count($extra);
            $out = array_fill(0, $n, null);
            foreach ($extra as $k => $e) { $pos = 2 + (int) floor($k * $step + $step / 2); while ($pos < $n && $out[$pos] !== null) $pos++; if ($pos >= $n) $pos = array_search(null, $out, true); $out[$pos] = $e; }
            foreach ($out as $k => $v) if ($v === null) $out[$k] = 'main';
            $plan = $out;
        }
        $rLevels = array_values(array_unique($rLevels)); sort($rLevels);
        return ['main' => ['skills' => $skills, 'levels' => $levels], 'review' => $review ? ['skills' => array_keys($review), 'levels' => $rLevels] : null,
                'stretch' => $stretch ? ['skills' => $stretch, 'levels' => [$up]] : null, 'plan' => $plan];
    }
}
