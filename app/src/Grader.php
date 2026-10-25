<?php
// Grades answers on the server. The browser never sees the correct answers.
//
// Spelling policy (config 'spelling', default 'forgiving'):
//   - capital letters never matter (a tip is shown for names, days and "I")
//   - a missing apostrophe (dont, isnt, im) is accepted, with a tip
//   - a typo is accepted only in a word the learner can copy from the task, or in the form of a verb given in the task
//     ("arrive" -> arriving: ariving), only as one slip INSIDE the word, in or next to the stem
//     (never at its end, where grammar lives: finish/finished, likes/liked, has/had), with a tip
//   'strict' accepts none of the last two.

final class Grader
{
    /** Apostrophe-less forms that cannot be anything else (so not "were", "ill", "its", "hes"). */
    private const APOSTROPHE = [
        'dont' => "don't", 'doesnt' => "doesn't", 'didnt' => "didn't", 'isnt' => "isn't", 'arent' => "aren't",
        'wasnt' => "wasn't", 'werent' => "weren't", 'hasnt' => "hasn't", 'havent' => "haven't", 'hadnt' => "hadn't",
        'wont' => "won't", 'cant' => "can't", 'couldnt' => "couldn't", 'wouldnt' => "wouldn't", 'shouldnt' => "shouldn't",
        'mustnt' => "mustn't", 'im' => "I'm", 'ive' => "I've", 'youre' => "you're", 'theyre' => "they're",
        'weve' => "we've", 'youve' => "you've", 'theyve' => "they've",
    ];

    public static function forgiving(): bool
    {
        return Config::get('spelling', 'forgiving') !== 'strict';
    }

    public static function norm(string $s): string
    {
        $s = mb_strtolower($s, 'UTF-8');
        $s = str_replace(["\u{2019}", "\u{2018}", "\u{00B4}", '`'], "'", $s);
        $s = preg_replace('/\bwon\'t\b/u', 'will not', $s);
        $s = preg_replace('/\bcan\'t\b/u', 'cannot', $s);
        $s = preg_replace('/\bshan\'t\b/u', 'shall not', $s);
        $s = preg_replace('/n\'t\b/u', ' not', $s);
        $s = preg_replace('/\'m\b/u', ' am', $s);
        $s = preg_replace('/\'re\b/u', ' are', $s);
        $s = preg_replace('/\'ve\b/u', ' have', $s);
        $s = preg_replace('/\'ll\b/u', ' will', $s);
        $s = str_replace(',', ' ', $s);
        $s = preg_replace('/[.!?;:]+\s*$/u', '', trim($s));
        $s = preg_replace('/\s+/u', ' ', $s);
        return trim($s);
    }

    private static function rx(string $pattern): string
    {
        return '~' . str_replace('~', '\~', $pattern) . '~iu';
    }

    /** dont -> don't, im -> I'm ... Returns [text with apostrophes, list of the corrected forms]. */
    public static function restoreApostrophes(string $s): array
    {
        $fixed = [];
        $out = preg_replace_callback('/(?<![\p{L}\'])([\p{L}]+)(?![\p{L}\'])/u', function ($m) use (&$fixed) {
            $k = mb_strtolower($m[1], 'UTF-8');
            if (isset(self::APOSTROPHE[$k])) {
                $fixed[] = self::APOSTROPHE[$k];
                return self::APOSTROPHE[$k];
            }
            return $m[1];
        }, str_replace(["\u{2019}", "\u{2018}"], "'", $s));
        return [$out, array_values(array_unique($fixed))];
    }

    /**
     * @param array $item  full item from the bank
     * @param mixed $answer string (mcq/text/write) or array of strings (gap)
     * @return array{correct:bool, show:string, specific:?string, notes:array}
     */
    public static function grade(array $item, $answer): array
    {
        switch ($item['kind']) {
            case 'mcq':
                $ok = is_string($answer) && $answer === $item['correct'];
                return [
                    'correct' => $ok,
                    'show' => $item['correct'],
                    'specific' => (!$ok && is_string($answer)) ? ($item['wrong_why'][$answer] ?? null) : null,
                    'specific_lv' => (!$ok && is_string($answer)) ? ($item['wrong_why_lv'][$answer] ?? null) : null,
                    'err' => (!$ok && is_string($answer)) ? ($item['wrong_err'][$answer] ?? null) : null,   // the error type of this wrong option, when the task names one
                    'notes' => [],
                ];

            case 'gap':
            case 'text':
                $given = is_array($answer) ? array_map('strval', $answer) : [(string) $answer];
                $blanks = $item['answers'];
                $prompt = self::promptWords($item['q']);
                $notes = [];
                $ok = count($given) === count($blanks);
                if ($ok) {
                    foreach ($blanks as $i => $accepted) {
                        $m = self::matchBlank($given[$i], $accepted, $item['kind'] === 'gap', $prompt);
                        if ($m === null) {
                            $ok = false;
                            break;
                        }
                        $notes = array_merge($notes, $m);
                    }
                }
                $show = implode(' / ', array_map(fn($b) => $b[0], $blanks));
                $specific = null;
                $specificLv = null;
                $err = null;
                $near = false;
                if ($ok && $item['kind'] === 'text') {
                    $notes = array_merge($notes, self::capitalNotes($given[0], $blanks[0][0]));
                    // Keep punctuation tolerance, but teach a supplementary which-clause's comma.
                    // Inspect the matched answer, not just the model: another accepted version
                    // may have a different structure and need no comma before which.
                    foreach ($blanks[0] as $accepted) {
                        if (self::norm($given[0]) !== self::norm($accepted)) continue;
                        if (preg_match('/,\s*which\b/iu', $accepted)
                            && preg_match('/\bwhich\b/iu', $given[0])
                            && !preg_match('/,\s*which\b/iu', $given[0])) {
                            $notes[] = 'Add a comma before which to separate the extra-information clause.';
                        }
                        break;
                    }
                }
                if (!$ok) {
                    $notes = [];
                    $hay = [mb_strtolower(implode(' / ', $given), 'UTF-8'), self::norm(implode(' / ', $given))];
                    foreach ($item['hints'] ?? [] as $hint) {
                        foreach ($hay as $h) {
                            if (@preg_match(self::rx($hint[0]), $h) === 1) {
                                $specific = $hint[1];
                                $specificLv = $hint[2] ?? null;
                                $err = $hint[3] ?? null;   // the error type this hint recognises, when it names one
                                break 2;
                            }
                        }
                    }
                    if ($specific === null && trim(implode('', $given)) === '') {
                        $specific = 'You did not type an answer.';
                    }
                    // a whole sentence that is right except for one word: say which word, instead of explaining the grammar again
                    if ($specific === null && $item['kind'] === 'text' && count($given) === 1 && ($nm = self::nearMiss($given[0], $blanks[0])) !== null) {
                        $near = true;
                        $specific = "Almost: your sentence is right except for one word. You wrote “{$nm[0]}”, the answer has “{$nm[1]}”.";
                        $specificLv = "Gandrīz: teikums ir pareizs, izņemot vienu vārdu. Tu uzrakstīji “{$nm[0]}”, atbildē ir “{$nm[1]}”.";
                    }
                }
                return ['correct' => $ok, 'show' => $show, 'specific' => $specific, 'specific_lv' => $specificLv, 'err' => $err, 'near' => $near, 'notes' => array_values(array_unique($notes))];

            case 'order':
                // the learner drags cards into order: the same cards must all be used once, and the sentence must be an accepted one
                $given = is_array($answer) ? array_map('strval', $answer) : preg_split('/\s+/u', trim((string) $answer), -1, PREG_SPLIT_NO_EMPTY);
                $want = explode(' ', $item['sentence']);
                $a = array_map(fn($x) => mb_strtolower($x, 'UTF-8'), $given); $b = array_map(fn($x) => mb_strtolower($x, 'UTF-8'), $want); sort($a); sort($b);   // the cards show proper names with a capital: compare without case
                $nice = $item['display_answer'] ?? self::nice($item['sentence']);
                if ($a !== $b) return ['correct' => false, 'show' => $nice, 'specific' => 'Use every card once.', 'specific_lv' => 'Izmanto katru kartīti vienu reizi.', 'notes' => []];
                $acc = array_map([self::class, 'norm'], $item['answers'][0]);
                return ['correct' => in_array(self::norm(implode(' ', $given)), $acc, true), 'show' => $nice, 'specific' => null, 'notes' => []];

            case 'match':
                $given = is_array($answer) ? array_map('strval', array_values($answer)) : [];
                $marks = [];
                foreach ($item['pairs'] as $i => $p) $marks[] = (($given[$i] ?? null) === $p[1]);
                $ok = count($given) === count($item['pairs']) && !in_array(false, $marks, true);
                $bad = [];
                foreach ($item['pairs'] as $i => $p) if (!$marks[$i]) $bad[] = $p[0];
                return [
                    'correct' => $ok, 'marks' => $marks,
                    'show' => implode(' | ', array_map(fn($p) => $p[0] . ' = ' . $p[1], $item['pairs'])),
                    'specific' => (!$ok && count($given) === count($item['pairs'])) ? 'Look again at: ' . implode(' / ', array_slice($bad, 0, 3)) . '.' : null,
                    'notes' => [],
                ];

            case 'write':
                $text = trim((string) (is_array($answer) ? ($answer[0] ?? '') : $answer));
                $words = preg_split('/\s+/u', $text, -1, PREG_SPLIT_NO_EMPTY);
                if (count($words) < 3) {
                    return ['correct' => false, 'show' => $item['model'], 'specific' => 'Write a full sentence (at least 3 words).', 'notes' => []];
                }
                $notes = [];
                if (self::forgiving()) {
                    [$text, $fixed] = self::restoreApostrophes($text);
                    foreach ($fixed as $f) $notes[] = "Use an apostrophe: $f.";
                }
                $msgs = [];
                $msgsLv = [];
                foreach ($item['must'] as $m) {
                    if (@preg_match(self::rx($m[0]), $text) !== 1) {
                        $msgs[] = $m[1];
                        $msgsLv[] = $m[2] ?? null;
                    }
                }
                return [
                    'correct' => count($msgs) === 0,
                    'show' => $item['model'],
                    'specific' => count($msgs) ? implode(' ', $msgs) : null,
                    'specific_lv' => (count($msgs) && !in_array(null, $msgsLv, true)) ? implode(' ', $msgsLv) : null,
                    'notes' => count($msgs) ? [] : $notes,
                ];
        }
        return ['correct' => false, 'show' => '', 'specific' => null, 'notes' => []];
    }

    /** Words that are always written with a capital letter. A word-order task is stored lower case, so they are put back when it is shown. */
    private const PROPER = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'mondays', 'tuesdays', 'wednesdays', 'thursdays', 'fridays', 'saturdays', 'sundays',
        'january', 'february', 'march', 'april', 'june', 'july', 'august', 'september', 'october', 'november', 'december',
        'latvia', 'latvian', 'riga', 'london', 'paris', 'rome', 'berlin', 'madrid', 'spain', 'spanish', 'italy', 'italian', 'germany', 'german', 'france', 'french', 'english', 'ecuador', 'canada', 'brazil',
        'japan', 'japanese', 'asia', 'europe', 'america', 'australia', 'china', 'chinese', 'india', 'korea', 'korean', 'netherlands', 'poland', 'russian', 'estonia', 'lithuania', 'sweden', 'finland',
        'picasso', 'adele', 'eiffel', 'everest', 'alps', 'baltic', 'atlantic', 'christmas', 'tom', 'ben', 'anna', 'sam', 'maria', 'kate', 'lena', 'jon', 'max', 'mia', 'mark', 'jack', 'ziya', 'mo', 'jo', 'tim', 'dan', 'lucy', 'novak'];

    /** One word of an order task as it is written in a sentence (not the first word: that gets its capital in nice()). */
    public static function properCase(string $w): string
    {
        $l = mb_strtolower($w, 'UTF-8');
        if (preg_match('/^i(\'(m|ll|ve|d))?$/u', $l)) return 'I' . mb_substr($l, 1, null, 'UTF-8');
        if (in_array($l, ['uk', 'usa', 'un', 'eu'], true)) return mb_strtoupper($l, 'UTF-8');
        if (in_array($l, self::PROPER, true)) return mb_strtoupper(mb_substr($l, 0, 1, 'UTF-8'), 'UTF-8') . mb_substr($l, 1, null, 'UTF-8');
        return $w;
    }

    /** A word-order answer is stored lower case without punctuation. Show it as a normal sentence. */
    private static function nice(string $s): string
    {
        $q = preg_match('/^(could|can|do|does|did|would|will|is|are|was|were|have|has|what|where|when|why|how|who|which)\b/i', $s);
        $s = implode(' ', array_map([self::class, 'properCase'], explode(' ', $s)));
        return mb_strtoupper(mb_substr($s, 0, 1, 'UTF-8'), 'UTF-8') . mb_substr($s, 1, null, 'UTF-8') . ($q ? '?' : '.');
    }

    /** Words the learner can see in the task (they may be copied, so a typo in them is just a typo). */
    private static function promptWords(string $q): array
    {
        $set = [];
        foreach (preg_split('/[^\p{L}\p{N}\']+/u', mb_strtolower($q, 'UTF-8'), -1, PREG_SPLIT_NO_EMPTY) as $w) $set[$w] = true;
        return $set;
    }

    /** @return array|null  null = no match; otherwise a list of spelling tips (empty when exact) */
    /** Every reading of a contracted answer: 'd = would / had, 's = is / has (only after a pronoun, so a possessive like Tom's is left alone). */
    private static function forms(string $s): array
    {
        $out = [$s];
        foreach ([['/\b(i|you|he|she|it|we|they|that|there|who|what)\'d\b/u', ['would', 'had']], ['/\b(he|she|it|that|there|who|what|where|how|here)\'s\b/u', ['is', 'has']]] as [$rx, $alts]) {
            $guard = 0;
            while ($guard++ < 6) {
                $next = []; $changed = false;
                foreach ($out as $x) {
                    if (preg_match($rx, $x, $m, PREG_OFFSET_CAPTURE)) {
                        $changed = true;
                        foreach ($alts as $alt) $next[] = substr($x, 0, $m[0][1]) . $m[1][0] . ' ' . $alt . substr($x, $m[0][1] + strlen($m[0][0]));
                    } else {
                        $next[] = $x;
                    }
                }
                $out = array_values(array_unique($next));
                if (!$changed || count($out) > 32) break;
            }
        }
        return $out;
    }

    private static function matchBlank(string $given, array $accepted, bool $isGap, array $prompt): ?array
    {
        $g = self::norm($given);
        if ($g === '') {
            return null;
        }
        $variants = static function (string $s) use ($isGap): array {
            $v = [$s];
            if ($isGap) {
                // A learner who retypes the pronoun that is already in the sentence is not wrong.
                $stripped = preg_replace('/^(i|you|he|she|it|we|they)\s+/u', '', $s);
                if ($stripped !== $s) $v[] = $stripped;
            }
            return $v;
        };
        $acc = array_map([self::class, 'norm'], $accepted);
        $accAll = [];   // 'd is would or had, 's is is or has: both the answer and the key are read both ways, so I'd known / I had known match
        foreach ($acc as $a) foreach (self::forms($a) as $f) $accAll[] = $f;
        $hit = static function (string $x) use ($accAll): bool {
            foreach (self::forms($x) as $f) if (in_array($f, $accAll, true)) return true;
            return false;
        };
        foreach ($variants($g) as $v) {
            if ($hit($v)) return [];
        }
        if (!self::forgiving()) {
            return null;
        }

        $notes = [];
        [$fixedText, $fixed] = self::restoreApostrophes($given);
        if ($fixed) {
            $g2 = self::norm($fixedText);
            foreach ($fixed as $f) $notes[] = "Use an apostrophe: $f.";
            foreach ($variants($g2) as $v) {
                if ($hit($v)) return $notes;
            }
            $g = $g2;
        }
        foreach ($variants($g) as $v) {
            foreach ($acc as $k => $a) {
                $t = self::typoMatch($v, $a, $prompt);
                if ($t === null && !$isGap) $t = self::pluralSlip($v, $a, $prompt, $accepted[$k]);
                if ($t !== null) return array_merge($notes, $t);
            }
        }
        return null;
    }

    public const PREPOSITIONS = ['on', 'in', 'at', 'for', 'with', 'by', 'from', 'about', 'of', 'during', 'after', 'before', 'without', 'near'];
    public const DETERMINERS = ['the', 'my', 'your', 'his', 'her', 'our', 'their', 'these', 'those'];

    /**
     * A plural -s left off a noun that the task already contains and that follows a preposition ("on sunday" for "on Sundays") is a
     * copying slip, not a grammar error. Only there: after a preposition (with or without the, my ...) the word is never the subject,
     * so a missing -s cannot hide a verb-agreement mistake.
     * @return array|null a tip, or null when the answers differ in anything else
     */
    private static function pluralSlip(string $given, string $accepted, array $prompt, string $acceptedRaw): ?array
    {
        $g = explode(' ', $given);
        $a = explode(' ', $accepted);
        if (count($g) !== count($a)) return null;
        $diff = [];
        foreach ($a as $i => $w) if ($g[$i] !== $w) $diff[] = $i;
        if (count($diff) !== 1) return null;
        $i = $diff[0];
        $w = $a[$i];
        if (mb_strlen($w, 'UTF-8') < 5 || !isset($prompt[$w]) || !in_array($w, [$g[$i] . 's', $g[$i] . 'es'], true)) return null;
        $prev = $a[$i - 1] ?? '';
        $prev2 = $a[$i - 2] ?? '';
        $afterPreposition = in_array($prev, self::PREPOSITIONS, true) || (in_array($prev, self::DETERMINERS, true) && in_array($prev2, self::PREPOSITIONS, true));
        return $afterPreposition ? ["Check the ending: {$g[$i]} → " . self::shown($w, $acceptedRaw) . '.'] : null;
    }

    /** The word as it is written in the accepted answer (capital letter kept), for messages. */
    private static function shown(string $token, string $raw): string
    {
        foreach (preg_split('/\s+/u', $raw, -1, PREG_SPLIT_NO_EMPTY) as $x) {
            $x = trim($x, '.,?!;:"');
            if (mb_strtolower($x, 'UTF-8') === $token) return $x;
        }
        return $token;
    }

    /** The accepted answer that differs from the given one in exactly one word: [what was written, what the answer has], or null. */
    private static function nearMiss(string $given, array $accepted): ?array
    {
        $g = explode(' ', self::norm($given));
        foreach ($accepted as $raw) {
            $a = explode(' ', self::norm($raw));
            if (count($a) !== count($g)) continue;
            $diff = [];
            foreach ($a as $i => $w) if ($g[$i] !== $w) $diff[] = $i;
            if (count($diff) === 1) return [$g[$diff[0]], self::shown($a[$diff[0]], $raw)];
        }
        return null;
    }

    /** Same words except for at most two typos in words copied from the task. Null if not. */
    private static function typoMatch(string $given, string $accepted, array $prompt): ?array
    {
        $g = explode(' ', $given);
        $a = explode(' ', $accepted);
        if (count($g) !== count($a)) return null;
        $notes = [];
        foreach ($a as $i => $word) {
            if ($g[$i] === $word) continue;
            $at = mb_strlen($word, 'UTF-8') >= 5 ? self::oneTypo($g[$i], $word) : -1;
            if ($at >= 0 && (isset($prompt[$word]) || $at <= self::stemLength($word, $prompt))) {
                $notes[] = "Spelling: {$g[$i]} → $word.";
                continue;
            }
            return null;
        }
        return ($notes && count($notes) <= 2) ? $notes : null;
    }

    /**
     * How much of a correct word is the stem of a verb that the task gives ("arrive" gives the stem "arriv" of arriving,
     * "play" gives "play" of played, "stop" gives "stop" of stopped). 0 when no word of the task shares at least 4 letters.
     */
    private static function stemLength(string $word, array $prompt): int
    {
        $best = 0;
        foreach (array_keys($prompt) as $p) {
            $p = (string) $p;
            if (mb_strlen($p, 'UTF-8') < 4) continue;
            $n = 0;
            $max = min(mb_strlen($p, 'UTF-8'), mb_strlen($word, 'UTF-8'));
            while ($n < $max && mb_substr($p, $n, 1, 'UTF-8') === mb_substr($word, $n, 1, 'UTF-8')) $n++;
            if ($n >= 4) $best = max($best, $n);
        }
        return $best;
    }

    /**
     * One adjacent swap, or one letter wrong/missing/extra that is NOT the last letter of the correct word.
     * @return int the position of the slip, or -1 when the words are not one typo apart
     */
    private static function oneTypo(string $s, string $t): int
    {
        $s = preg_split('//u', $s, -1, PREG_SPLIT_NO_EMPTY);
        $t = preg_split('//u', $t, -1, PREG_SPLIT_NO_EMPTY);
        $ls = count($s);
        $lt = count($t);
        if (abs($ls - $lt) > 1) return -1;
        $i = 0;
        while ($i < min($ls, $lt) && $s[$i] === $t[$i]) $i++;
        if ($i === $ls && $i === $lt) return -1;
        if ($ls === $lt) {
            if ($i + 1 < $lt && $s[$i] === $t[$i + 1] && $s[$i + 1] === $t[$i] && array_slice($s, $i + 2) === array_slice($t, $i + 2)) return $i; // swap
            return ($i < $lt - 1 && array_slice($s, $i + 1) === array_slice($t, $i + 1)) ? $i : -1;                                                 // wrong letter
        }
        if ($ls === $lt + 1) return ($i < $ls - 1 && array_slice($s, $i + 1) === array_slice($t, $i)) ? $i : -1;                                   // extra letter
        return ($i < $lt - 1 && array_slice($s, $i) === array_slice($t, $i + 1)) ? $i : -1;                                                         // missing letter
    }

    /** Tips for capital letters in names, days, months and "I" (never a mistake). */
    private static function capitalNotes(string $given, string $accepted): array
    {
        $notes = [];
        $given = str_replace(["\u{2019}", "\u{2018}"], "'", $given);
        $accepted = str_replace(["\u{2019}", "\u{2018}"], "'", $accepted);
        $inner = preg_replace('/^\s*\S+/u', '', $accepted);                  // not the first word
        $inner = preg_replace('/[.!?]\s+\S+/u', ' ', $inner);               // not a word after a full stop
        if (preg_match_all('/(?<![\p{L}])([\p{Lu}][\p{L}]+)(?![\p{L}])/u', $inner, $m)) {
            foreach (array_unique($m[1]) as $w) {
                $lc = mb_strtolower($w, 'UTF-8');
                if (!preg_match('/(?<![\p{L}])' . preg_quote($w, '/') . '(?![\p{L}])/u', $given)
                    && preg_match('/(?<![\p{L}])' . preg_quote($lc, '/') . '(?![\p{L}])/u', $given)) {
                    $notes[] = "Capital letter: $w.";
                }
            }
        }
        if (preg_match('/(?<![\p{L}])I(?![\p{L}])/u', $accepted) && preg_match('/(?<![\p{L}])i(?![\p{L}])/u', $given)) {
            $notes[] = 'Write I with a capital letter.';
        }
        return $notes;
    }
}
