<?php
// Loads the question bank (content/items.json, content/meta.json).

final class Content
{
    private static ?array $items = null;
    private static ?array $meta = null;
    private static ?array $byId = null;
    private static ?array $retired = null;

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
            self::$byId = [];
            foreach (self::$items as $i => $it) {
                self::$items[$i]['d'] = self::difficulty($it['level'], $it['bloom']);
                self::$byId[$it['id']] = &self::$items[$i];
            }
        }
        return self::$items;
    }

    public static function meta(): array
    {
        return self::$meta ??= self::load('meta');
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
        return self::$retired[$id] ?? self::customById($id);
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
        $lv = $theta < 1.8 ? 'A2.1' : ($theta < 2.5 ? 'A2.2' : ($theta < 3.5 ? 'B1.1' : ($theta < 4.5 ? 'B1.2' : ($theta < 5.5 ? 'B2.1' : ($theta < 6.5 ? 'B2.2' : ($theta < 7.5 ? 'C1.1' : 'C1.2'))))));
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
    public static function levelFromAbility(float $theta): string
    {
        $out = 'A2.1';
        foreach (self::BASE as $lv => $base) {
            if ($theta >= $base - 0.5 + ($lv === 'A2.1' ? 99 : 0)) $out = $lv;
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
            $out['tokens'] = self::shuffled(explode(' ', $it['sentence']), $seed);
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
