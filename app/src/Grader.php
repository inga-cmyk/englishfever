<?php
// Grades answers on the server. The browser never sees the correct answers.

final class Grader
{
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

    /**
     * @param array $item  full item from the bank
     * @param mixed $answer string (mcq/text/write) or array of strings (gap)
     * @return array{correct:bool, show:string, specific:?string}
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
                ];

            case 'gap':
            case 'text':
                $given = is_array($answer) ? array_map('strval', $answer) : [(string) $answer];
                $blanks = $item['answers'];
                $ok = count($given) === count($blanks);
                if ($ok) {
                    foreach ($blanks as $i => $accepted) {
                        if (!self::matchBlank($given[$i], $accepted, $item['kind'] === 'gap')) {
                            $ok = false;
                            break;
                        }
                    }
                }
                $show = implode(' / ', array_map(fn($b) => $b[0], $blanks));
                $specific = null;
                if (!$ok) {
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
                return ['correct' => $ok, 'show' => $show, 'specific' => $specific];

            case 'write':
                $text = trim((string) (is_array($answer) ? ($answer[0] ?? '') : $answer));
                $words = preg_split('/\s+/u', $text, -1, PREG_SPLIT_NO_EMPTY);
                if (count($words) < 3) {
                    return ['correct' => false, 'show' => $item['model'], 'specific' => 'Write a full sentence (at least 3 words).'];
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
                ];
        }
        return ['correct' => false, 'show' => '', 'specific' => null];
    }

    private static function matchBlank(string $given, array $accepted, bool $isGap): bool
    {
        $g = self::norm($given);
        if ($g === '') {
            return false;
        }
        foreach ($accepted as $a) {
            if ($g === self::norm($a)) {
                return true;
            }
        }
        if ($isGap) {
            // A learner who retypes the pronoun that is already in the sentence is not wrong.
            $stripped = preg_replace('/^(i|you|he|she|it|we|they)\s+/u', '', $g);
            if ($stripped !== $g) {
                foreach ($accepted as $a) {
                    if ($stripped === self::norm($a)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
