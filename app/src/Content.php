<?php
// Loads the question bank (content/items.json, content/meta.json).

final class Content
{
    private static ?array $items = null;
    private static ?array $meta = null;
    private static ?array $byId = null;

    public const BASE = ['A2.1' => 1.0, 'A2.2' => 2.0, 'B1.1' => 3.0, 'B1.2' => 4.0, 'B2.1' => 5.0, 'B2.2' => 6.0];

    public static function items(): array
    {
        if (self::$items === null) {
            self::$items = json_decode(file_get_contents(__DIR__ . '/../content/items.json'), true);
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
        return self::$meta ??= json_decode(file_get_contents(__DIR__ . '/../content/meta.json'), true);
    }

    public static function item(string $id): ?array
    {
        self::items();
        return self::$byId[$id] ?? null;
    }

    public static function difficulty(string $level, int $bloom): float
    {
        return self::BASE[$level] + ($bloom - 1) * 0.2;
    }

    public static function levelFromTheta(float $theta, ?array $allowed = null): string
    {
        // boundaries calibrated with simulated learners (tests/sim.py): estimates run slightly low at the top and high at the bottom
        $lv = $theta < 1.8 ? 'A2.1' : ($theta < 2.5 ? 'A2.2' : ($theta < 3.5 ? 'B1.1' : 'B1.2'));
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
            'voice' => $skill['voice'] ?? 'active',
        ];
        if ($it['kind'] === 'mcq') {
            $opts = array_merge([$it['correct']], $it['wrong']);
            mt_srand(($seed ?? random_int(1, 1 << 30)) ^ crc32($it['id']));
            for ($i = count($opts) - 1; $i > 0; $i--) {
                $j = mt_rand(0, $i);
                [$opts[$i], $opts[$j]] = [$opts[$j], $opts[$i]];
            }
            mt_srand();
            $out['options'] = $opts;
        }
        if ($it['kind'] === 'gap') {
            $out['blanks'] = count($it['answers']);
        }
        return $out;
    }
}
