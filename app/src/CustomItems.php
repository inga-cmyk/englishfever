<?php
// Tasks the teacher adds by uploading a spreadsheet (CSV). They are checked row by row, stored as drafts, and served only after the
// teacher approves them. They join the built-in bank (Content::items) and work with reports, pausing and grading like any other task.

final class CustomItems
{
    public const STATUSES = ['draft', 'approved', 'retired'];
    private const TYPES = ['mcq' => 'mcq', 'multiple choice' => 'mcq', 'gap' => 'gap', 'gap fill' => 'gap', 'text' => 'text', 'rewrite' => 'text', 'typed' => 'text',
        'order' => 'order', 'word order' => 'order', 'match' => 'match', 'matching' => 'match'];
    private const SUBORDINATORS = ['if', 'unless', 'when', 'after', 'before', 'as soon as', 'while', 'because', 'although', 'until', 'once'];

    // ───────── what the app reads ─────────

    /** Approved tasks, in the same shape as the built-in bank. */
    public static function approved(): array
    {
        if (!isset(Db::$pdo)) return [];
        try { $rows = Db::all("SELECT * FROM custom_items WHERE status = 'approved' ORDER BY id"); } catch (Throwable $e) { return []; }
        return array_map([self::class, 'fromRow'], $rows);
    }

    /** Any custom task by id (also drafts and retired ones: reports and old answers keep pointing at them). */
    public static function find(string $id): ?array
    {
        if (!isset(Db::$pdo) || strncmp($id, 'c-', 2) !== 0) return null;
        try { $r = Db::one('SELECT * FROM custom_items WHERE item_id = ?', [$id]); } catch (Throwable $e) { return null; }
        return $r ? self::fromRow($r) : null;
    }

    private static function fromRow(array $r): array
    {
        $it = json_decode((string) $r['data'], true) ?: [];
        return ['id' => $r['item_id'], 'skill' => $r['skill'], 'level' => $r['level'], 'bloom' => (int) $r['bloom'], 'kind' => $r['kind']] + $it;
    }

    // ───────── the teacher's list ─────────

    public static function listAll(): array
    {
        $out = ['draft' => [], 'approved' => [], 'retired' => []];
        foreach (Db::all('SELECT * FROM custom_items ORDER BY id DESC') as $r) {
            $it = self::fromRow($r);
            $skill = Content::skill($it['skill']);
            $out[$r['status']][] = ['id' => $it['id'], 'skill' => $skill['label'] ?? $it['skill'], 'level' => $it['level'], 'kind' => $it['kind'], 'q' => $it['q'], 'key' => self::keyOf($it), 'options' => $it['kind'] === 'mcq' ? $it['wrong'] : null, 'why' => $it['why'] ?? '', 'why_lv' => $it['why_lv'] ?? ''];
        }
        return $out;
    }

    public static function keyOf(array $it): string
    {
        switch ($it['kind']) {
            case 'mcq': return $it['correct'];
            case 'gap': case 'text': return implode(' / ', array_map(fn($b) => implode('  |  ', $b), $it['answers']));
            case 'order': return $it['sentence'];
            case 'match': return implode('; ', array_map(fn($p) => $p[0] . ' = ' . $p[1], $it['pairs']));
        }
        return '';
    }

    public static function setStatus(array $ids, string $status): int
    {
        if (!in_array($status, self::STATUSES, true)) throw new ApiError('Unknown status.', 400);
        $n = 0;
        foreach ($ids as $id) {
            $r = Db::one('SELECT id FROM custom_items WHERE item_id = ?', [(string) $id]);
            if (!$r) continue;
            Db::update('custom_items', ['status' => $status, 'updated_at' => time()], 'id = ?', [$r['id']]);
            $n++;
        }
        return $n;
    }

    public static function template(): string
    {
        $fh = fopen('php://temp', 'w+');
        fputcsv($fh, ['topic', 'level', 'type', 'task', 'correct answer', 'wrong options / checks', 'explanation shown to learner', 'explanation in Latvian'], ',', '"', '\\');
        $rows = [
            ['Present simple', 'A2', 'mcq', 'Choose the correct form: My sister ___ coffee in the morning.', 'drinks', 'drink | is drink | drinking', 'With he, she and it we add -s to the verb: she drinks.', ''],
            ['Present simple', 'A2', 'gap', 'Tom ___ to school by bus. (go)', 'goes', '', 'With he, she, it we add -es to go: he goes.', ''],
            ['Present simple', 'A2', 'gap', '___ your brother ___ English? (speak)', 'Does / speak', '', 'Question: does + subject + base verb.', ''],
            ['Present simple', 'A2', 'text', 'Make it negative: She likes fish.', "She doesn't like fish. | She does not like fish.", '', "With she we use doesn't + base verb.", ''],
            ['Present simple', 'A2', 'order', 'Put the words in order.', 'my mother works in a shop', '', 'Subject + verb with -s + place.', ''],
            ['Present simple', 'A2', 'match', 'Match each beginning with the right ending.', 'He plays = tennis on Sundays. ; She works = in a bank. ; They live = in Riga.', '', 'He/she/it: verb + -s. They: base verb.', ''],
        ];
        foreach ($rows as $r) fputcsv($fh, $r, ',', '"', '\\');
        rewind($fh); $csv = stream_get_contents($fh); fclose($fh);
        return "\xEF\xBB\xBF" . $csv;
    }

    // ───────── reading the spreadsheet ─────────

    /**
     * Checks every row. Returns ['rows' => [['line', 'ok', 'errors', 'warnings', 'q', 'kind', 'skill', 'level', 'item']...], 'ok' => n, 'bad' => n].
     * With $save the correct rows are stored as drafts.
     */
    public static function import(string $csv, bool $save): array
    {
        if (strlen($csv) > 600000) throw new ApiError('The file is too big (600 KB at most).', 400);
        if (!mb_check_encoding($csv, 'UTF-8')) $csv = mb_convert_encoding($csv, 'UTF-8', 'Windows-1257'); // Excel in Latvia
        $csv = preg_replace('/^\xEF\xBB\xBF/', '', $csv);
        $first = strtok($csv, "\n");
        $delim = substr_count((string) $first, ';') > substr_count((string) $first, ',') ? ';' : (substr_count((string) $first, "\t") > substr_count((string) $first, ',') ? "\t" : ',');
        $fh = fopen('php://temp', 'w+'); fwrite($fh, $csv); rewind($fh);
        $head = fgetcsv($fh, 0, $delim, '"', '\\');
        if (!$head) throw new ApiError('The file is empty.', 400);
        $col = [];
        foreach ($head as $i => $h) {
            $h = mb_strtolower(trim((string) $h));
            $key = null;
            if ($h === 'topic' || $h === 'skill') $key = 'topic';
            elseif ($h === 'level') $key = 'level';
            elseif ($h === 'type' || $h === 'kind') $key = 'type';
            elseif ($h === 'task' || $h === 'question') $key = 'task';
            elseif ($h === 'correct answer' || $h === 'answer') $key = 'correct';
            elseif (strpos($h, 'wrong options') === 0 || $h === 'options') $key = 'wrong';
            elseif ($h === 'replaces') $key = 'replaces';   // optional: the old correct answer of a matching task this row corrects
            elseif (strpos($h, 'explanation in latvian') === 0 || $h === 'latvian') $key = 'why_lv';
            elseif (strpos($h, 'explanation') === 0 || $h === 'why') $key = 'why';
            elseif (strpos($h, 'thinking level') === 0) $key = 'bloom';
            if ($key && !isset($col[$key])) $col[$key] = $i;
        }
        foreach (['topic', 'level', 'type', 'task', 'correct', 'why'] as $need) {
            if (!isset($col[$need])) throw new ApiError("The first row must have these columns: topic, level, type, task, correct answer, explanation (missing: $need). Download the template to see them.", 400);
        }
        $skills = Content::meta()['skills'];
        $existing = [];
        $rel = Content::relabelled(); // a task given a lower level as a copy may be imported again at that level
        foreach (Content::items() as $it) if (!isset($rel[$it['id']])) $existing[self::dupKey($it)] = true;
        $mine = []; $byContent = []; $byOld = [];   // tasks already added from a file: the same task again is left alone; the same content with new wording updates the wording
        foreach (Db::all("SELECT item_id, skill, level, kind, data FROM custom_items WHERE status <> 'retired'") as $r) {
            $d = json_decode($r['data'], true);
            if (empty($d['q'])) continue;
            $d += ['skill' => $r['skill'], 'level' => $r['level'], 'kind' => $r['kind']];
            $existing[self::dupKey($d)] = true; $mine[self::dupKey($d)] = ['id' => $r['item_id'], 'data' => json_encode(array_diff_key($d, ['skill' => 1, 'level' => 1, 'kind' => 1, 'bloom' => 1]), JSON_UNESCAPED_UNICODE)];
            if (self::contentKey($d) !== '') $byContent[self::contentKey($d)] = ['id' => $r['item_id'], 'q' => $d['q']];
            $byOld[self::oldKey($d)] = $r['item_id'];
        }
        $rows = []; $line = 1; $ok = 0; $bad = 0; $seen = []; $upd = 0; $same = 0;
        while (($r = fgetcsv($fh, 0, $delim, '"', '\\')) !== false) {
            $line++;
            if (count(array_filter($r, fn($c) => trim((string) $c) !== '')) === 0) continue;
            if (count($rows) >= 500) { throw new ApiError('At most 500 tasks per file.', 400); }
            $get = fn($k) => isset($col[$k], $r[$col[$k]]) ? trim(preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F]/', '', (string) $r[$col[$k]])) : '';
            $res = ['line' => $line, 'ok' => false, 'errors' => [], 'warnings' => [], 'q' => $get('task'), 'kind' => '', 'skill' => '', 'level' => '', 'item' => null];
            try {
                $item = self::buildRow($get, $skills, $res);
                $dup = self::dupKey($item);
                $ck = self::contentKey($item);
                if ($item['kind'] === 'match' && $get('replaces') !== '') {   // a corrected matching task: the older version (if it was added) is retired
                    $oldPairs = [];
                    foreach (self::split($get('replaces'), ';') as $p) { $x = explode('=', $p, 2); if (count($x) === 2) $oldPairs[] = [trim($x[0]), trim($x[1])]; }
                    $ok2 = self::contentKey(['skill' => $item['skill'], 'level' => $item['level'], 'kind' => 'match', 'pairs' => $oldPairs]);
                    if (isset($byContent[$ok2])) { $res['replaces'] = $byContent[$ok2]['id']; $res['warnings'][] = 'Replaces an older version of this question, which is retired.'; }
                }
                if ($item['kind'] !== 'match' && $get('replaces') !== '') {   // another corrected task: the older version (the old correct option, sentence or task text) is retired
                    $ok3 = self::oldKey(['skill' => $item['skill'], 'level' => $item['level'], 'kind' => $item['kind'], 'q' => $get('replaces'), 'correct' => $get('replaces'), 'sentence' => $get('replaces')]);
                    if (isset($byOld[$ok3])) { $res['replaces'] = $byOld[$ok3]; $res['warnings'][] = 'Replaces an older version of this question, which is retired.'; }
                }
                if (isset($seen[$dup])) throw new ApiError('This task is twice in the file.', 400);
                if (isset($mine[$dup])) {                                   // added from a file before
                    $now = json_encode(array_diff_key($item, ['skill' => 1, 'level' => 1, 'kind' => 1, 'bloom' => 1]), JSON_UNESCAPED_UNICODE);
                    if ($now === $mine[$dup]['data']) {                       // nothing changed
                        $res['ok'] = true; $res['same'] = true; $res['warnings'] = []; $same++;
                    } else {                                                  // corrected answers, options or explanations: updated where it is (status and results stay)
                        $res['ok'] = true; $res['update'] = $mine[$dup]['id']; $res['item'] = $item; $res['warnings'] = ['Already added: the corrected answers, options or explanations are updated.']; $upd++;
                    }
                    $seen[$dup] = true; $rows[] = $res; continue;
                }
                if ($ck !== '' && isset($byContent[$ck]) && $byContent[$ck]['q'] !== $item['q']) {   // same task, new wording: update it where it is
                    $res['ok'] = true; $res['update'] = $byContent[$ck]['id']; $res['item'] = $item; $res['warnings'][] = 'Already added: the wording is updated.'; $upd++;
                    $seen[$dup] = true; $rows[] = $res; continue;
                }
                if (isset($existing[$dup])) throw new ApiError('This task is already in the bank (same topic and text).', 400);
                $seen[$dup] = true;
                $res['ok'] = true; $res['item'] = $item;
            } catch (ApiError $e) { $res['errors'][] = $e->getMessage(); }
            $res['ok'] ? $ok++ : $bad++;
            $rows[] = $res;
        }
        fclose($fh);
        if ($save) {
            foreach ($rows as &$row) {
                if (!$row['ok'] || !empty($row['same'])) continue;
                $it = $row['item'];
                if (!empty($row['replaces'])) Db::update('custom_items', ['status' => 'retired', 'updated_at' => time()], 'item_id = ?', [$row['replaces']]);
                if (!empty($row['update'])) {
                    $cur = Db::one('SELECT data FROM custom_items WHERE item_id = ?', [$row['update']]);
                    $d = json_decode((string) ($cur['data'] ?? ''), true);
                    if (is_array($d)) { $nd = $it; unset($nd['skill'], $nd['level'], $nd['bloom'], $nd['kind']); Db::update('custom_items', ['data' => json_encode($nd, JSON_UNESCAPED_UNICODE), 'bloom' => $it['bloom'], 'updated_at' => time()], 'item_id = ?', [$row['update']]); }
                    $row['id'] = $row['update'];
                    continue;
                }
                $next = (int) Db::val('SELECT COALESCE(MAX(id), 0) + 1 FROM custom_items');
                $id = 'c-' . str_pad((string) $next, 4, '0', STR_PAD_LEFT);
                $data = $it; unset($data['skill'], $data['level'], $data['bloom'], $data['kind']);
                Db::insert('custom_items', ['item_id' => $id, 'skill' => $it['skill'], 'level' => $it['level'], 'bloom' => $it['bloom'], 'kind' => $it['kind'],
                    'data' => json_encode($data, JSON_UNESCAPED_UNICODE), 'status' => 'draft', 'created_at' => time(), 'updated_at' => time()]);
                $row['id'] = $id;
            }
            unset($row);
        }
        foreach ($rows as &$row) unset($row['item']);
        return ['rows' => $rows, 'ok' => $ok, 'bad' => $bad, 'saved' => $save, 'updated' => $upd, 'same' => $same];
    }

    private static function split(string $s, string $sep): array
    {
        return array_values(array_filter(array_map('trim', explode($sep, $s)), fn($x) => $x !== ''));
    }

    private static function buildRow(callable $get, array $skills, array &$res): array
    {
        // topic: id, full name, or the name before the bracket ("Zero conditional")
        $t = mb_strtolower($get('topic')); $skill = null;
        foreach ($skills as $s) {
            $label = mb_strtolower($s['label']); $short = trim(preg_replace('/\s*[(:].*$/u', '', $label)); // the name before a bracket or a colon
            if ($t !== '' && ($t === $s['id'] || $t === $label || $t === $short)) { $skill = $s; break; }
        }
        if (!$skill) throw new ApiError("Unknown topic \"{$get('topic')}\". Use a topic name from the list on this page.", 400);
        $res['skill'] = $skill['label'];
        // level: A2.1 ... C1.2, or just A2, B1, B2, C1 (the first half-level of it that the topic has)
        $lv = strtoupper(str_replace(' ', '', $get('level')));
        if (preg_match('/^(A2|B1|B2|C1)$/', $lv)) {
            $cand = array_values(array_filter($skill['levels'], fn($x) => strpos($x, $lv) === 0));
            if (!$cand) throw new ApiError("This topic has no $lv tasks (it covers " . self::range($skill['levels']) . ').', 400);
            $lv = $cand[0];
        } elseif (!in_array($lv, $skill['levels'], true)) {
            throw new ApiError('Level "' . $get('level') . '" is not available for this topic (it covers ' . self::range($skill['levels']) . ').', 400);
        }
        $res['level'] = $lv;
        $kind = self::TYPES[mb_strtolower($get('type'))] ?? null;
        if (!$kind) throw new ApiError('Type "' . $get('type') . '" is not supported. Use: mcq, gap, text, order, match.', 400);
        $res['kind'] = $kind;
        $q = preg_replace('/\s+/u', ' ', $get('task'));
        $why = $get('why');
        if ($q === '' || mb_strlen($q) > 300) throw new ApiError('The task text is empty or longer than 300 characters.', 400);
        if ($why === '') throw new ApiError('The explanation is empty. Add one short sentence.', 400);
        if (mb_strlen($why) > 400) throw new ApiError('The explanation is longer than 400 characters.', 400);
        $bloom = preg_match('/^[1-6]/', $get('bloom'), $m) ? (int) $m[0] : ($kind === 'mcq' ? 2 : 3);
        $correct = $get('correct'); $wrong = $get('wrong');
        $item = ['skill' => $skill['id'], 'level' => $lv, 'bloom' => $bloom, 'kind' => $kind, 'q' => $q, 'why' => $why];
        if ($get('why_lv') !== '') $item['why_lv'] = $get('why_lv');
        if ($correct === '') throw new ApiError('The correct answer is empty.', 400);
        switch ($kind) {
            case 'mcq':
                $w = self::split($wrong, '|');
                if (count($w) < 2) throw new ApiError('Give at least 2 wrong options, separated by | .', 400);
                $all = array_merge([$correct], $w);
                if (count(array_unique(array_map('mb_strtolower', $all))) !== count($all)) throw new ApiError('Two options are the same.', 400);
                foreach ($all as $o) if (mb_strlen($o) > 200) throw new ApiError('An option is longer than 200 characters.', 400);
                $longest = max(array_map('mb_strlen', $w));
                if (mb_strlen($correct) > 35 && mb_strlen($correct) > 1.5 * $longest) $res['warnings'][] = 'The correct option is much longer than the others, so it stands out.';
                foreach ($all as $o) if (preg_match('/^(Say|Use|Write|Choose)\b/u', $o)) { $res['warnings'][] = 'An option starts with an instruction word (' . strtok($o, ' ') . ').'; break; }
                $item += ['correct' => $correct, 'wrong' => $w, 'wrong_why' => new stdClass()];
                $item['wrong_why'] = [];
                break;
            case 'gap':
                $blanks = substr_count($q, '___');
                if ($blanks < 1) throw new ApiError('A gap task needs ___ in the task text.', 400);
                $groups = array_map(fn($g) => self::split($g, '|'), self::split($correct, '/'));
                if (count($groups) !== $blanks || in_array([], $groups, true)) throw new ApiError("The task has $blanks blank" . ($blanks > 1 ? 's' : '') . ' but the correct answer has ' . count($groups) . ' part' . (count($groups) === 1 ? '' : 's') . '. Separate the answers for each blank with " / ".', 400);
                $item += ['answers' => $groups, 'hints' => []];
                if (preg_match('/^\s*(word )?bank\s*:\s*(.+)$/iu', $wrong, $m)) {
                    $bank = self::split($m[2], '|');
                    foreach ($groups as $g) if (count($g) > 1) throw new ApiError('A word-bank gap takes one answer per blank.', 400);
                    $firsts = array_map(fn($g) => $g[0], $groups);
                    if (count(array_unique($bank)) !== count($bank)) throw new ApiError('The word bank has the same word twice.', 400);
                    foreach ($firsts as $a) if (!in_array($a, $bank, true)) throw new ApiError("The word bank does not contain the answer \"$a\".", 400);
                    if (count($bank) < count($firsts) + 1) throw new ApiError('The word bank needs at least one extra word.', 400);
                    $item['bank'] = $bank;
                }
                break;
            case 'text':
                $a = self::split($correct, '|');
                $a = self::withVariants($a);
                $item += ['answers' => [$a], 'hints' => []];
                break;
            case 'order':
                $s = trim(preg_replace('/\s+/u', ' ', $correct));
                $tok = explode(' ', $s);
                if (count($tok) < 4 || count($tok) > 16) throw new ApiError('A word-order task needs 4 to 16 words.', 400);
                sort($tok);
                $extra = self::split(preg_replace('/^\s*also accepted\s*:\s*/iu', '', $wrong), '|');
                foreach ($extra as $e) { $t = explode(' ', trim(preg_replace('/\s+/u', ' ', $e))); sort($t); if ($t !== $tok) throw new ApiError("The other accepted order \"$e\" must use exactly the same words.", 400); }
                $item += ['sentence' => $s, 'answers' => [array_merge([$s], array_map(fn($e) => trim(preg_replace('/\s+/u', ' ', $e)), $extra))]];
                break;
            case 'match':
                $pairs = [];
                foreach (self::split($correct, ';') as $p) {
                    $x = explode('=', $p, 2);
                    if (count($x) !== 2 || trim($x[0]) === '' || trim($x[1]) === '') throw new ApiError('Write each pair as: beginning = ending, and separate pairs with ; .', 400);
                    $pairs[] = [trim($x[0]), trim($x[1])];
                }
                if (count($pairs) < 3 || count($pairs) > 6) throw new ApiError('A matching task needs 3 to 6 pairs.', 400);
                if (count(array_unique(array_column($pairs, 0))) !== count($pairs) || count(array_unique(array_column($pairs, 1))) !== count($pairs)) throw new ApiError('The cards in a matching task must all be different.', 400);
                $item += ['pairs' => $pairs];
                break;
        }
        return $item;
    }

    /**
     * Same topic, same text and same content is a duplicate. Instructions are plain and shared ("Which sentence is NOT correct?",
     * "Put the words in order."), so what makes a task its own is the sentence of a word-order task, the correct option of a
     * multiple-choice task and the pairs of a matching task.
     */
    private static function dupKey(array $it): string
    {
        $pairs = isset($it['pairs']) ? json_encode($it['pairs'], JSON_UNESCAPED_UNICODE) : '';
        return mb_strtolower($it['q']) . '|' . $it['skill'] . (isset($it['sentence']) ? '|' . mb_strtolower($it['sentence']) : '')
            . (isset($it['correct']) && is_string($it['correct']) ? '|' . mb_strtolower($it['correct']) : '') . ($pairs !== '' ? '|' . mb_strtolower($pairs) : '');
    }

    /** How a corrected task names the older version it replaces: the correct option (choose), the sentence (word order) or the task text (the rest). Same topic and level. */
    private static function oldKey(array $it): string
    {
        $k = $it['kind'] === 'mcq' ? ($it['correct'] ?? '') : ($it['kind'] === 'order' ? ($it['sentence'] ?? '') : ($it['q'] ?? ''));
        return $it['skill'] . '|' . $it['level'] . '|' . $it['kind'] . '|' . mb_strtolower(trim((string) $k));
    }

    /** What a multiple-choice, word-order or matching task is, apart from its wording ('' for other kinds). */
    private static function contentKey(array $it): string
    {
        switch ($it['kind'] ?? '') {
            case 'mcq': if (strpos((string) ($it['q'] ?? ''), '___') !== false) return ''; /* the sentence is in the stem: the wording is the task */ $w = array_map('mb_strtolower', (array) ($it['wrong'] ?? [])); sort($w); $c = mb_strtolower((string) ($it['correct'] ?? '')) . '#' . implode('|', $w); break;
            case 'order': $c = mb_strtolower((string) ($it['sentence'] ?? '')); break;
            case 'match': $c = mb_strtolower(json_encode($it['pairs'] ?? [], JSON_UNESCAPED_UNICODE)); break;
            default: return '';
        }
        return $it['skill'] . '|' . $it['level'] . '|' . $it['kind'] . '|' . $c;
    }

    private static function range(array $levels): string
    {
        $a = preg_replace('/\.\d$/', '', $levels[0]); $b = preg_replace('/\.\d$/', '', end($levels));
        return $a === $b ? $a : "$a–$b";
    }

    /** Typed answers: add the other clause order (if / unless / when ... , ...) and both spellings of practise / practice, so correct answers are not marked wrong. */
    private static function withVariants(array $answers): array
    {
        $out = $answers;
        foreach ($answers as $a) {
            if (preg_match('/^(' . implode('|', array_map('preg_quote', self::SUBORDINATORS)) . ')\b([^,]+),\s*(.+?)([.!?]?)$/iu', $a, $m)) {
                $out[] = trim($m[3]) . ' ' . mb_strtolower(substr($m[1], 0, 1)) . substr($m[1], 1) . $m[2] . $m[4];
            }
        }
        foreach ($answers as $a) {   // the other way round: "I went home after I finished work." also as "After I finished work, I went home."
            if (preg_match('/^(?!(?:could|can|would|do|does|did|i wonder|i don\'t know|i do not know|i\'d like)\b)([^,]+?)\s+(' . implode('|', array_map('preg_quote', self::SUBORDINATORS)) . ')\s+([^,]+?)([.!?]?)$/iu', $a, $m)) {
                $main = preg_match('/^I\b/u', $m[1]) ? $m[1] : mb_strtolower(mb_substr($m[1], 0, 1)) . mb_substr($m[1], 1);
                $out[] = ucfirst($m[2]) . ' ' . $m[3] . ', ' . $main . $m[4];
            }
        }
        foreach ($out as $a) {
            if (stripos($a, 'practise') !== false) $out[] = str_ireplace('practise', 'practice', $a);
            elseif (stripos($a, 'practice') !== false) $out[] = str_ireplace('practice', 'practise', $a);
        }
        return array_values(array_unique($out));
    }
}
