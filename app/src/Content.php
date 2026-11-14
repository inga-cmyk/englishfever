<?php
// Loads the question bank (content/items.json, content/meta.json).

final class Content
{
    private static ?array $items = null;
    private static ?array $meta = null;
    private static ?array $byId = null;
    private static ?array $retired = null;
    private static array $hidden = [];

    public const BASE = ['A2.1' => 1.0, 'A2.2' => 2.0, 'B1.1' => 3.0, 'B1.2' => 4.0, 'B2.1' => 5.0, 'B2.2' => 6.0, 'C1.1' => 7.0, 'C1.2' => 8.0];

    /** content/<name>.php (production, never downloadable) or content/<name>.json (development). */
    private static function load(string $name): array
    {
        $php = __DIR__ . '/../content/' . $name . '.php';
        if (is_file($php)) return require $php;
        return json_decode(file_get_contents(__DIR__ . '/../content/' . $name . '.json'), true);
    }

    public static function items(): array
    {
        if (self::$items === null) {
            self::$items = self::load('items');
            if (class_exists('CustomItems', false)) self::$items = array_merge(self::$items, CustomItems::approved()); // tasks the teacher added and approved
            foreach (self::$items as $i => $it) if (strncmp((string) $it['level'], 'C1', 2) === 0) self::$items[$i]['level'] = 'B2.2';   // no C1 level in the app (teacher, 12 November, U3 A): prepared C1 tasks are B2.2
            self::hideRelabelled();
            self::hideDuplicates();
            self::$byId = [];
            foreach (self::$items as $i => $it) {
                self::$items[$i]['d'] = self::difficulty($it['level'], $it['bloom']);
                self::$items[$i]['scaffold'] = self::scaffold($it);
                self::$items[$i]['err'] = self::errors($it);
                self::$byId[$it['id']] = &self::$items[$i];
            }
        }
        return self::$items;
    }

    /** The grammar map (content/map.php, made by authoring/build.py from docs/GRAMMAR-MAP*): points with level and prerequisites, and each task's point. */
    public static function map(): array
    {
        static $m = null;
        if ($m === null) { $f = __DIR__ . '/../content/map.php'; $m = is_file($f) ? (require $f) : ['points' => [], 'builtin' => [], 'tasks' => []]; }
        return $m;
    }

    /** The key of a task in the map, as docs/grammar-map-src and app/tests/item_gates_test.py write it, without the level. */
    public static function mapKey(array $it): string
    {
        $body = '';
        if (isset($it['correct']) && is_string($it['correct']) && $it['correct'] !== '') $body = $it['correct'];
        elseif (!empty($it['sentence'])) $body = (string) $it['sentence'];
        elseif (!empty($it['pairs'])) $body = implode(' ; ', array_map(fn($p) => $p[0] . ' = ' . $p[1], $it['pairs']));
        return implode(' | ', [(string) $it['skill'], (string) $it['kind'], (string) ($it['q'] ?? ''), $body]);
    }

    /** The grammar point of a task (14 November, C1), or null when the map does not know the task. */
    public static function point(?array $it): ?string
    {
        if (!$it) return null;
        $m = self::map();
        $base = preg_replace('/-r\d+$/', '', (string) ($it['id'] ?? ''));
        return $m['builtin'][$base] ?? $m['tasks'][self::mapKey($it)] ?? null;
    }

    /** One point of the map: level, needs (prerequisite points), name, topics; null for an unknown id. */
    public static function mapPoint(string $id): ?array
    {
        return self::map()['points'][$id] ?? null;
    }

    /** Tests only: read the bank again (after prepared tasks were imported into the test database). */
    public static function reset(): void { self::$items = null; self::$byId = []; }

    /** Tests only: add tasks to the loaded bank. */
    public static function addTest(array $tasks): void
    {
        self::items();
        foreach ($tasks as $t) { $t['d'] = self::difficulty($t['level'], $t['bloom']); self::$items[] = $t; self::$byId[$t['id']] = &self::$items[count(self::$items) - 1]; }
    }

    /**
     * Two active tasks with the same text and the same answer are one task (report of 14 November: the same *the elderly* gap was
     * served twice, an older copy in another topic had not been retired on the server). The later one stays.
     */
    private static function hideDuplicates(): void
    {
        $seen = [];
        foreach (self::$items as $i => $it) {
            $body = $it['correct'] ?? $it['sentence'] ?? (isset($it['answers']) ? json_encode($it['answers']) : (isset($it['pairs']) ? json_encode($it['pairs']) : ''));
            $k = $it['kind'] . '|' . mb_strtolower(trim((string) $it['q'])) . '|' . mb_strtolower((string) $body);
            if (isset($seen[$k])) unset(self::$items[$seen[$k]]);
            $seen[$k] = $i;
        }
        self::$items = array_values(self::$items);
    }

    /** Built-in tasks that were given a lower level as a copy (content/relabelled.php): ids => true. */
    public static function relabelled(): array
    {
        static $ids = null;
        if ($ids === null) {
            $f = __DIR__ . '/../content/relabelled.php';
            $ids = is_file($f) ? array_fill_keys(require $f, true) : [];
        }
        return $ids;
    }

    /**
     * A task that was relabelled (for example B1 to A2) leaves the active pool as soon as its approved copy exists at the lower level.
     * The original stays readable, so every old answer and unfinished session keeps working.
     */
    private static function hideRelabelled(): void
    {
        $rel = self::relabelled();
        if (!$rel || !class_exists('CustomItems', false)) return;
        $copies = [];
        foreach (CustomItems::approved() as $c) if (strpos($c['level'], 'A2') === 0) $copies[$c['skill'] . '|' . mb_strtolower($c['q'])] = true;
        if (!$copies) return;
        $keep = [];
        foreach (self::$items as $it) {
            if (isset($rel[$it['id']]) && isset($copies[$it['skill'] . '|' . mb_strtolower($it['q'])])) {
                $it['d'] = self::difficulty($it['level'], $it['bloom']);
                self::$hidden[$it['id']] = $it;
                continue;
            }
            $keep[] = $it;
        }
        self::$items = $keep;
    }


    /**
     * How much support a task gives (teacher's plan, 25 October): a task with less support comes only after the learner has managed
     * one with more. 0 = choose or drag (the answer is on the screen), 1 = type with a clue (a verb in brackets, a named form, word order),
     * 2 = type without a clue, 3 = open writing. A task may set its own value.
     */
    public static function scaffold(array $it): int
    {
        if (isset($it['scaffold'])) return (int) $it['scaffold'];
        switch ($it['kind']) {
            case 'mcq': case 'match': return 0;
            case 'order': return 1;
            case 'gap':
                if (!empty($it['bank'])) return 0;
                return (preg_match('/\([^)]*\)\s*$/u', $it['q']) || preg_match('/^(Use|Complete with|Make|Give)\b/u', $it['q'])) ? 1 : 2;
            case 'text': return 2;
            default: return 3;
        }
    }

    /** The error types a task trains (docs/ERROR-TYPES.md): its own list, else the usual ones of its topic. Never shown to learners. */
    public static function errors(array $it): array
    {
        if (!empty($it['err'])) return array_values((array) $it['err']);
        return self::meta()['skill_err'][$it['skill']] ?? [];
    }

    public static function meta(): array
    {
        return self::$meta ??= self::load('meta');
    }

    /** The topics learners see: only those that have tasks (a topic the teacher adds starts empty until tasks are approved). */
    public static function liveMeta(): array
    {
        $m = self::meta();
        $have = [];
        foreach (self::items() as $it) $have[$it['skill']] = true;
        $m['skills'] = array_values(array_filter($m['skills'], fn($s) => isset($have[$s['id']])));
        $areas = array_flip(array_column($m['skills'], 'area'));
        $m['areas'] = array_values(array_filter($m['areas'], fn($a) => isset($areas[$a['id']])));
        return $m;
    }

    public const FULL_LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

    /** How many live questions there are per full level (A2, B1 ...), in all and per topic: what the practice picker shows. */
    public static function levelCounts(): array
    {
        $all = array_fill_keys(self::FULL_LEVELS, 0);
        $by = []; $half = [];
        foreach (self::items() as $it) {
            $full = substr($it['level'], 0, 2);
            $all[$full] = ($all[$full] ?? 0) + 1;
            $by[$it['skill']][$full] = ($by[$it['skill']][$full] ?? 0) + 1;
            $half[$it['skill']][$it['level']] = ($half[$it['skill']][$it['level']] ?? 0) + 1;
        }
        return ['all' => $all, 'by_skill' => $by, 'by_half' => $half];
    }

    /**
     * What a task is for (teacher, 3 November): "learn" builds understanding and can be solved from the meaning alone
     * (matching by context, "Which sentence means …?", a hint gives it away); "check" depends on the form (a choice with
     * ungrammatical wrong options, a gap, word order); "use" asks the learner to write the form or the sentence.
     * Only check and use count as evidence (mastery, the knowledge model, the level test). An item may set 'role' itself.
     */
    public static function role(?array $it): string
    {
        if (!$it) return 'check';
        if (!empty($it['role']) && in_array($it['role'], ['learn', 'check', 'use'], true)) return $it['role'];
        // matching forms stays a learning step (the pairs can be guessed from how the words look; teacher, 27 October and 6 November);
        // these two choice tasks need the form itself (teacher, 6 November)
        $over = ['rs-B12-2a' => 'check'];   // ip-B12-1a stays practice only: its wrong options miss the typical mistake (27 October)
        $base = preg_replace('/-r\d+$/', '', (string) ($it['id'] ?? ''));
        if (isset($over[$base])) return $over[$base];
        if (!empty($it['practice_only'])) return 'learn';
        if ($it['kind'] === 'match') return 'learn';
        if (in_array($it['kind'], ['text', 'write'], true)) return 'use';
        if ($it['kind'] === 'gap' && empty($it['bank'])) return 'use';
        if ($it['kind'] === 'mcq' && preg_match('/^(Which sentence (means|is about|tells|is a |describes|shows|imagines|expresses|uses|does NOT express|has a finished|is passive)|What is the difference|What usually happens|Which (words|word) usually|Which verb is normally)/i', (string) ($it['q'] ?? ''))) return 'learn';
        if ($it['kind'] === 'mcq' && preg_match('/What does (it|this|that) (say|mean)\?/i', (string) ($it['q'] ?? ''))) return 'learn';
        // meaning questions whose wrong options are correct sentences with another meaning (teacher, 12 November, U2 A, read one by one)
        static $learnQ = [
            "A colleague says: 'If I had a better memory, I would have remembered your birthday.' Choose the correct comment about the grammar." => true,   // 14 November: wrong options are correct sentences with another meaning
            "Which word can replace 'if' here? 'If it rains, the street floods.'" => true,   // 14 November: wrong options are correct sentences with another meaning
            "You see dark clouds. Which sentence is a prediction from what you can see now?" => true,   // 14 November: wrong options are correct sentences with another meaning
            "Which sentence is an arrangement (fixed time and place in your diary)?" => true,   // 14 November: wrong options are correct sentences with another meaning
            "You want to mention a mistake politely, without blaming anyone. Choose the correct option." => true,   // 14 November: wrong options are correct sentences with another meaning
            "Is this statement true? 'I'm living with my parents at the moment' sounds more temporary than 'I live with my parents.'" => true,   // 14 November: wrong options are correct sentences with another meaning
            "Which sentence sounds like news that is important right now?" => true,   // 14 November: wrong options are correct sentences with another meaning
            "Which word(s) do we use to report a yes/no question?" => true,   // 14 November: wrong options are correct sentences with another meaning
            "The officer's words: 'I'm not going to tell you who did it.' Which word says what the officer did?" => true,   // 14 November: wrong options are correct sentences with another meaning
            "'Were I more experienced, I would have applied for the director role last year.' What does 'Were I' replace?" => true,   // 14 November: wrong options are correct sentences with another meaning
            "'If we had booked earlier, we would have got a cheaper flight.' What really happened?" => true,   // 14 November: wrong options are correct sentences with another meaning
            "Which sentence gives a scheduled departure, rather than a hope, a past event or an action happening now?" => true,   // 14 November: wrong options are correct sentences with another meaning
            "Why do we say 'Tickets are sold here'?" => true,   // 14 November: wrong options are correct sentences with another meaning
            "The teacher's words: 'The Earth goes round the Sun.' Why can we report them as 'The teacher said the Earth goes round the Sun'?" => true,   // 14 November: wrong options are correct sentences with another meaning
            "'I have no idea how to start.' What does 'how to start' mean?" => true,
            "'If he hadn't been so rude, we might have signed the deal.' What does 'might have' show?" => true,
            "'Whatever he says, don't sign it.' What does 'whatever' mean here?" => true,
            "A technician is still working on your computer. Choose the correct option." => true,
            "Choose the correct meaning: 'Mum has gone to the shop.'" => true,
            "Choose the correct meaning: 'Our guests have arrived.'" => true,
            "Choose the sentence that keeps the meaning: I did not take that job, so I am not rich now." => true,
            "Compare 'The bridge was closed' and 'The bridge has been closed'. Which one tells us the bridge is probably still closed now?" => true,
            "In 'The report is checked by the manager', what is the focus?" => true,
            "Which sentence compares two things?" => true,
            "Which sentence focuses on a recent event with a result now?" => true,
            "Which sentence focuses on the activity, not the result?" => true,
            "Which sentence focuses on the result or number (not the activity)?" => true,
            "Which sentence has the same meaning as 'The police arrested two men'?" => true,
            "Which sentence puts the focus on the data, not on the person?" => true,
            "Which sentence says that people grow rice in Asia, without saying who?" => true,
            "Which sentence says that someone broke the window, without saying who?" => true,
        ];
        if ($it['kind'] === 'mcq' && isset($learnQ[(string) ($it['q'] ?? '')])) return 'learn';
        // questions about meaning (what a sentence tells us, which action came first) can be answered without forming the tense (teacher, 12 November, U2 A)
        if ($it['kind'] === 'mcq' && preg_match("/^(What does .{2,80} (mean|tell us)\\??|What does this sentence mean\\?|In (the story )?'.+', which (action|thing)? ?(started|happened) first\\?|Which sentence says (how long|the difference|the train was missed|that she first))/i", (string) ($it['q'] ?? ''))) return 'learn';
        return 'check';
    }

    /**
     * The sentence behind a task, so that the same sentence in a choice, a word bank and a word order counts once towards Learned
     * (teacher, 12 November, U4 A): the correct sentence with the gaps filled, lower case, letters and digits only.
     */
    public static function sentenceKey(array $it): string
    {
        $q = (string) ($it['q'] ?? '');
        $q = preg_replace('/^[^:]{0,90}:\s*/u', '', $q);   // without the instruction
        switch ($it['kind']) {
            case 'order': $s = (string) ($it['sentence'] ?? ''); break;
            case 'text': $s = (string) ($it['answers'][0][0] ?? $q); break;
            case 'write': $s = (string) ($it['model'] ?? $q); break;
            case 'match': $s = (string) ($it['id'] ?? ''); break;
            case 'gap':
                $i = 0; $s = preg_replace_callback('/___/', function () use ($it, &$i) { return (string) ($it['answers'][$i++][0] ?? ''); }, $q); break;
            default:   // mcq: the option in the gap, or the correct sentence
                $s = strpos($q, '___') !== false ? str_replace('___', (string) ($it['correct'] ?? ''), $q) : (string) ($it['correct'] ?? $q);
        }
        $s = preg_replace('/\([^)]*\)/u', '', $s);
        return trim(preg_replace('/[^a-z0-9]+/u', ' ', mb_strtolower($s, 'UTF-8')));
    }

    /** The kind of task a learner sees (teacher, 28 October): recognise = choose or match, use = fill in, word bank, word order, write = typed sentence or open writing. */
    public static function taskCat(?array $it): string
    {
        if (!$it) return 'recognise';
        if (in_array($it['kind'], ['mcq', 'match'], true)) return 'recognise';
        if (in_array($it['kind'], ['text', 'write'], true)) return 'write';
        return 'use';   // gap (typed word or word bank), order
    }
    /** Right / all answers per kind of task, from attempts rows that have item_id and correct. */
    public static function catCounts(array $rows): array
    {
        $out = ['recognise' => ['n' => 0, 'correct' => 0], 'use' => ['n' => 0, 'correct' => 0], 'write' => ['n' => 0, 'correct' => 0]];
        foreach ($rows as $r) { $c = self::taskCat(self::item((string) $r['item_id'])); $out[$c]['n']++; $out[$c]['correct'] += (int) $r['correct']; }
        return $out;
    }

    public static function item(string $id): ?array
    {
        self::items();
        if (isset(self::$byId[$id])) return self::$byId[$id];
        // Historical answers and sessions already in progress keep the exact item
        // they originally used. Retired items never enter items()/pickNext().
        if (self::$retired === null) {
            self::$retired = [];
            foreach (self::load('retired') as $it) {
                $it['d'] = self::difficulty($it['level'], $it['bloom']);
                self::$retired[$it['id']] = $it;
            }
        }
        return self::$retired[$id] ?? self::$hidden[$id] ?? self::customById($id);
    }

    /** The ids of built-in tasks that have a corrected version (retired.json). */
    public static function retiredIds(): array
    {
        return array_column(self::load('retired'), 'id');
    }

    /** A custom task that is not (or no longer) approved: reports and old answers still point at it. */
    private static function customById(string $id): ?array
    {
        if (!class_exists('CustomItems', false)) return null;
        $it = CustomItems::find($id);
        if ($it) $it['d'] = self::difficulty($it['level'], $it['bloom']);
        return $it;
    }

    public static function difficulty(string $level, int $bloom): float
    {
        return self::BASE[$level] + ($bloom - 1) * 0.2;
    }

    public static function levelFromTheta(float $theta, ?array $allowed = null): string
    {
        // boundaries calibrated with simulated learners (tests/sim.py): estimates run slightly low at the top and high at the bottom
        $lv = $theta < 1.8 ? 'A2.1' : ($theta < 2.5 ? 'A2.2' : ($theta < 3.5 ? 'B1.1' : ($theta < 4.5 ? 'B1.2' : ($theta < 5.5 ? 'B2.1' : 'B2.2'))));   // B2.2 is the top (U3 A)
        if ($allowed) {
            $order = array_keys(self::BASE);
            $idx = array_search($lv, $order);
            $best = $allowed[0];
            foreach ($allowed as $a) {
                if (abs(array_search($a, $order) - $idx) < abs(array_search($best, $order) - $idx)) $best = $a;
            }
            return $best;
        }
        return $lv;
    }

    /** The level for an ability fitted to all answers at once (placement): the boundaries sit halfway between the level bases. */
    /**
     * The level a placement result is given: the highest level whose typical task (thinking level 3, difficulty base + 0.4) the learner
     * gets right at least half of the time (theta >= base + 0.4). Before 25 October the bar was base - 0.5, so a learner who got most
     * tasks of a level wrong could still be given that level (full test report: "about B2" with 3 of 8 B2 questions right).
     */
    public static function levelFromAbility(float $theta): string
    {
        $out = 'A2.1';
        foreach (self::BASE as $lv => $base) {
            if ($lv !== 'A2.1' && strncmp($lv, 'C1', 2) !== 0 && $theta >= $base + 0.4) $out = $lv;   // never C1: B2.2 is the top (U3 A)
        }
        return $out;
    }

    public static function skill(string $id): ?array
    {
        foreach (self::meta()['skills'] as $s) {
            if ($s['id'] === $id) return $s;
        }
        return null;
    }

    /** What the browser may see: no answers. */
    public static function publicItem(array $it, ?int $seed = null): array
    {
        $skill = self::skill($it['skill']);
        $out = [
            'id' => $it['id'], 'kind' => $it['kind'], 'q' => $it['q'], 'bloom' => $it['bloom'],
            'level' => $it['level'], 'skill' => $it['skill'], 'skill_label' => $skill['label'] ?? $it['skill'],
            'area' => $skill['area'] ?? 'active',
        ];
        $seed = ($seed ?? random_int(1, 1 << 30)) ^ crc32($it['id']);
        if ($it['kind'] === 'mcq') {
            $out['options'] = self::shuffled(array_merge([$it['correct']], $it['wrong']), $seed);
        }
        if ($it['kind'] === 'gap') {
            $out['blanks'] = count($it['answers']);
            if (!empty($it['bank'])) $out['bank'] = self::shuffled($it['bank'], $seed);
        }
        if ($it['kind'] === 'order') {
            $out['tokens'] = self::shuffled(array_map(['Grader', 'properCase'], explode(' ', $it['sentence'])), $seed);
        }
        if ($it['kind'] === 'match') {
            $out['lefts'] = array_column($it['pairs'], 0);
            $out['rights'] = self::shuffled(array_column($it['pairs'], 1), $seed);
        }
        return $out;
    }

    /** A repeatable shuffle (the same task shows the same order after a reload). Never returns the original order. */
    private static function shuffled(array $list, int $seed): array
    {
        $orig = array_values($list);
        $a = $orig;
        mt_srand($seed);
        for ($i = count($a) - 1; $i > 0; $i--) {
            $j = mt_rand(0, $i);
            [$a[$i], $a[$j]] = [$a[$j], $a[$i]];
        }
        mt_srand();
        if ($a === $orig && count($a) > 1) $a = array_merge(array_slice($a, 1), [$a[0]]);
        return $a;
    }
}
