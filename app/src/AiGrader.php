<?php
// AI check of open writing tasks (teacher, 3 November): the smallest Claude model reads the learner's sentence, compares it
// with the task and the model answer, and answers in the app's own feedback style: right or not, and the changed words only.
// It adds to the pattern check; it never replaces it. Without an API key, or when the call fails, the app grades as before.

final class AiGrader
{
    private const SYSTEM = <<<TXT
You check one short answer to an English grammar writing task for adult learners (A2-C1).
Judge grammar only: verb forms, subject-verb agreement, word order, articles, prepositions, and the form the task asks for.
Do not judge content, facts, style or spelling of names. A sentence that is grammatical and does the task is correct,
even if it is different from the model answer.
Answer with JSON only:
- correct: true or false.
- fixes: at most 3 changes, each {"wrong": the learner's exact words, "right": the corrected words}; only the changed words, never the whole sentence.
- tip: one short sentence in plain English for the learner (max 15 words), or "" when correct.
- tip_lv: the same tip in natural Latvian, or "" when correct.
TXT;

    public static function enabled(): bool
    {
        return self::key() !== '' && class_exists('\Anthropic\Client');
    }

    /** The key from config.php ('ai_key'); for the dry run on a computer also the ANTHROPIC_API_KEY environment variable. */
    private static function key(): string
    {
        return (string) (Config::get('ai_key', '') ?: getenv('ANTHROPIC_API_KEY') ?: '');
    }

    /** @return array{correct: bool, fixes: array<int, array{wrong: string, right: string}>, tip: string, tip_lv: string, model: string}|null  null = no AI verdict */
    public static function check(array $item, string $answer): ?array
    {
        if (!self::enabled() || trim($answer) === '') return null;
        $model = (string) Config::get('ai_model', 'claude-haiku-5-5');
        $user = "Task: " . ($item['q'] ?? '') . "\nModel answer: " . ($item['model'] ?? '') . "\nLearner's answer: " . mb_substr($answer, 0, 600);
        try {
            $client = new \Anthropic\Client(apiKey: self::key(), requestOptions: ['timeout' => 8.0, 'maxRetries' => 1]);
            $msg = $client->messages->create(
                model: $model,
                maxTokens: 1024,
                system: self::SYSTEM,
                messages: [['role' => 'user', 'content' => $user]],
                outputConfig: ['effort' => 'low', 'format' => ['type' => 'json_schema', 'schema' => [
                    'type' => 'object', 'additionalProperties' => false,
                    'required' => ['correct', 'fixes', 'tip', 'tip_lv'],
                    'properties' => [
                        'correct' => ['type' => 'boolean'],
                        'fixes' => ['type' => 'array', 'items' => ['type' => 'object', 'additionalProperties' => false, 'required' => ['wrong', 'right'],
                            'properties' => ['wrong' => ['type' => 'string'], 'right' => ['type' => 'string']]]],
                        'tip' => ['type' => 'string'],
                        'tip_lv' => ['type' => 'string'],
                    ],
                ]]],
            );
            if (($msg->stopReason ?? '') === 'refusal') return null;
            $text = '';
            foreach ($msg->content as $block) if ($block->type === 'text') { $text = $block->text; break; }
            $j = json_decode($text, true);
            if (!is_array($j) || !isset($j['correct'])) return null;
            $fixes = [];
            foreach (array_slice((array) ($j['fixes'] ?? []), 0, 3) as $f) {
                $w = trim((string) ($f['wrong'] ?? '')); $r = trim((string) ($f['right'] ?? ''));
                if ($w !== '' && $r !== '' && mb_strtolower($w) !== mb_strtolower($r)) $fixes[] = ['wrong' => mb_substr($w, 0, 80), 'right' => mb_substr($r, 0, 80)];
            }
            return ['correct' => (bool) $j['correct'] && !$fixes, 'fixes' => $fixes, 'tip' => mb_substr((string) ($j['tip'] ?? ''), 0, 160),
                    'tip_lv' => mb_substr((string) ($j['tip_lv'] ?? ''), 0, 200), 'model' => $model];
        } catch (\Throwable $e) {
            return null;   // no key, network, rate limit, refusal: grade without AI
        }
    }

    /** The feedback line in the app's style: "Check this: **he are** → **he is**." */
    public static function line(array $v, bool $lv = false): string
    {
        $parts = array_map(fn($f) => '*' . $f['wrong'] . '* → *' . $f['right'] . '*', $v['fixes']);
        $head = $parts ? ($lv ? 'Pārbaudi: ' : 'Check this: ') . implode(', ', $parts) . '.' : '';
        $tip = $lv ? $v['tip_lv'] : $v['tip'];
        return trim($head . ($tip !== '' ? ' ' . $tip : ''));
    }
}
