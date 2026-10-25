<?php
// Where each learner stands with each kind of mistake (docs/ERROR-TYPES.md). Background only: learners never see the names.
// Worked out from the answers (attempts.err), so a change of the rules applies to the whole history at once.
//
//   new        answered only right so far, not yet enough to count as mastered
//   learn      a mistake: needs learning
//   practise   right again since the last mistake, not yet for sure
//   mastered   right in 3 different tasks, on at least 2 days, at least once without a clue (Content::scaffold >= 2) since the last mistake
//   kept       mastered, and right again at the check 14 days or more later
//
// A wrong answer moves one step back (kept/mastered -> practise, practise/new -> learn). Review is due 1, 3 and 7 days after the
// right answers while the mistake is being learnt, and 14 days after it is mastered.

final class ErrorModel
{
    public const DAYS = 180;
    private const SPACING = [1, 3, 7];
    private const CHECK_AFTER = 14;

    /** @return array<string, array{state:string, right:int, wrong:int, last:int, due:?int}> */
    public static function scan(int $uid, ?int $now = null): array
    {
        $now = $now ?? time();
        $rows = Db::all('SELECT item_id, correct, err, created_at FROM attempts WHERE user_id = ? AND created_at > ? ORDER BY id ASC', [$uid, $now - self::DAYS * 86400]);
        $out = [];
        foreach ($rows as $r) {
            $codes = $r['err'] !== null && $r['err'] !== '' ? explode(',', (string) $r['err']) : null;
            $it = Content::item((string) $r['item_id']);
            if ($codes === null) $codes = $it ? Content::errors($it) : [];   // answers given before error types were stored
            $t = (int) $r['created_at'];
            $day = date('Y-m-d', $t);
            $sc = $it ? Content::scaffold($it) : 0;
            foreach ($codes as $c) {
                $e = $out[$c] ?? ['state' => 'new', 'right' => 0, 'wrong' => 0, 'last' => 0, 'due' => null, 'ev' => [], 'mastered_at' => null];
                $e['last'] = $t;
                if (!(int) $r['correct']) {
                    $e['wrong']++;
                    $e['state'] = in_array($e['state'], ['kept', 'mastered'], true) ? 'practise' : 'learn';
                    $e['ev'] = [];
                    $e['mastered_at'] = null;
                    $e['due'] = $t + 86400;
                } else {
                    $e['right']++;
                    $e['ev'][(string) $r['item_id']] = ['day' => $day, 'sc' => $sc];
                    if ($e['state'] === 'mastered' && $e['mastered_at'] !== null && $t - $e['mastered_at'] >= self::CHECK_AFTER * 86400) {
                        $e['state'] = 'kept';
                        $e['due'] = null;
                    } elseif ($e['state'] === 'learn' || $e['state'] === 'practise' || $e['state'] === 'new') {
                        if ($e['state'] === 'learn') $e['state'] = 'practise';
                        if (self::proven($e['ev'])) {
                            $e['state'] = 'mastered';
                            $e['mastered_at'] = $t;
                            $e['due'] = $t + self::CHECK_AFTER * 86400;
                        } elseif ($e['state'] === 'practise') {
                            $k = min(count($e['ev']), count(self::SPACING)) - 1;
                            $e['due'] = $t + self::SPACING[max(0, $k)] * 86400;
                        }
                    }
                }
                $out[$c] = $e;
            }
        }
        foreach ($out as $c => $e) {
            unset($out[$c]['ev'], $out[$c]['mastered_at']);
            if ($e['state'] === 'new') $out[$c]['due'] = null;
        }
        return $out;
    }

    /** 3 different tasks, on 2 or more days, at least one without a clue. */
    private static function proven(array $ev): bool
    {
        if (count($ev) < 3) return false;
        $days = array_unique(array_column($ev, 'day'));
        $free = array_filter($ev, fn($x) => $x['sc'] >= 2);
        return count($days) >= 2 && count($free) >= 1;
    }

    /** Kinds of mistake that are due for review now, the most urgent first. @return string[] */
    public static function due(int $uid, ?int $now = null): array
    {
        $now = $now ?? time();
        $list = array_filter(self::scan($uid, $now), fn($e) => $e['due'] !== null && $e['due'] <= $now);
        uasort($list, fn($a, $b) => [$a['state'] === 'learn' ? 0 : 1, $a['due']] <=> [$b['state'] === 'learn' ? 0 : 1, $b['due']]);
        return array_keys($list);
    }
}
