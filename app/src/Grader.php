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
                if ($ok && $item['kind'] === 'text') {
                    $notes = array_merge($notes, self::capitalNotes($given[0], $blanks[0][0]));
                }
                if (!$ok) {
                    $notes = [];
                    $hay = [mb_strtolower(implode(' / ', $given), 'UTF-8'), self::norm(implode(' / ', $given))];
                    foreach ($item['hints'] ?? [] as [$pattern, $msg]) {
                        foreach ($hay as $h) {
                            if (@preg_match(self::rx($pattern), $h) === 1) {
                                $specific = $msg;
                                break 2;
                            }
                        }
                    }
                    if ($specific === null && trim(implode('', $given)) === '') {
                        $specific = 'You did not type an answer.';
                    }
                }
                return ['correct' => $ok, 'show' => $show, 'specific' => $specific, 'notes' => array_values(array_unique($notes))];

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
                foreach ($item['must'] as [$pattern, $msg]) {
                    if (@preg_match(self::rx($pattern), $text) !== 1) {
                        $msgs[] = $msg;
                    }
                }
                return [
                    'correct' => count($msgs) === 0,
                    'show' => $item['model'],
                    'specific' => count($msgs) ? implode(' ', $msgs) : null,
                    'notes' => count($msgs) ? [] : $notes,
                ];
        }
        return ['correct' => false, 'show' => '', 'specific' => null, 'notes' => []];
    }

    /** Words the learner can see in the task (they may be copied, so a typo in them is just a typo). */
    private static function promptWords(string $q): array
    {
        $set = [];
        foreach (preg_split('/[^\p{L}\p{N}\']+/u', mb_strtolower($q, 'UTF-8'), -1, PREG_SPLIT_NO_EMPTY) as $w) $set[$w] = true;
        return $set;
    }

    /** @return array|null  null = no match; otherwise a list of spelling tips (empty when exact) */
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
        foreach ($variants($g) as $v) {
            if (in_array($v, $acc, true)) return [];
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
                if (in_array($v, $acc, true)) return $notes;
            }
            $g = $g2;
        }
        foreach ($variants($g) as $v) {
            foreach ($acc as $a) {
                $t = self::typoMatch($v, $a, $prompt);
                if ($t !== null) return array_merge($notes, $t);
            }
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
