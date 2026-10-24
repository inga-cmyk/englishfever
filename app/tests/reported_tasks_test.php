<?php
// Regression checks for the 24 October reports. In-memory DB only; no learner data.
putenv('EF_DEV=1');
foreach (['Auth', 'Db', 'Content', 'Grader', 'CustomItems'] as $name) require __DIR__ . '/../src/' . $name . '.php';
Config::load();
Db::connect(['driver' => 'sqlite', 'sqlite' => ':memory:']);
Db::migrate();
$n = 0;
function expect_report(bool $ok, string $message): void {
    global $n;
    $n++;
    if (!$ok) throw new RuntimeException($message);
}
$drafts = [];
foreach (glob(__DIR__ . '/../../docs/task-drafts/*.csv') as $path) {
    $res = CustomItems::import(file_get_contents($path), true);
    expect_report($res['bad'] === 0, basename($path) . ': invalid CSV row');
}
foreach (Db::all('SELECT data, kind FROM custom_items') as $row) $drafts[] = json_decode($row['data'], true) + ['kind' => $row['kind']];
function draft_report(string $field, string $value): array {
    global $drafts;
    foreach ($drafts as $it) if (($it[$field] ?? null) === $value) return $it;
    throw new RuntimeException('Draft not found: ' . $value);
}
foreach ([
    ["she didn't use to enjoy cooking but now she loves it", "she didn't use to enjoy cooking but she loves it now"],
    ['the man who called you is my boss', 'my boss is the man who called you'],
    ['the woman whose car was stolen called the police', 'the police called the woman whose car was stolen'],
] as [$model, $answer]) {
    expect_report(Grader::grade(draft_report('sentence', $model), explode(' ', $answer))['correct'], 'Valid unrestricted word order rejected');
}
$which = draft_report('q', 'Join the two sentences: She passed her driving test. This surprised everyone.');
$missing = Grader::grade($which, 'She passed her driving test which surprised everyone.');
expect_report($missing['correct'] && count($missing['notes']) === 1 && strpos($missing['notes'][0], 'comma before which') !== false, 'Missing supplementary comma needs a tip');
$punctuated = Grader::grade($which, 'She passed her driving test, which surprised everyone.');
expect_report($punctuated['correct'] && !$punctuated['notes'], 'Correct comma should not get a warning');
$defining = $which;
$defining['answers'] = [['The book which I bought is here.']];
expect_report(!Grader::grade($defining, 'The book which I bought is here.')['notes'], 'Defining which-clause must not get a comma warning');
$alternatives = $which;
$alternatives['answers'][0][] = 'Everyone was surprised that she passed her driving test.';
expect_report(!Grader::grade($alternatives, 'Everyone was surprised that she passed her driving test.')['notes'], 'Alternative without which must not get a comma warning');
expect_report(strpos(draft_report('correct', 'The book which I bought it was boring.')['why'], 'repeat') !== false, 'Feedback must explain the repeated object');
$condition = Content::item('ct-B22-3a-r2');
foreach (["hadn't driven", 'had not driven', "hadn't been driving", 'had not been driving'] as $first) {
    expect_report(Grader::grade($condition, [$first, "wouldn't have lost"])['correct'], 'Valid third-conditional variant rejected');
}
expect_report(!Grader::grade(Content::item('ia-C11-3a-r4'), 'I wonder who made the decision.')['correct'], 'A grammatical change of meaning is not a valid combination');
expect_report(Grader::grade(Content::item('ia-C11-3a-r4'), "It's unclear who made the decision.")['correct'], 'Unclear is a valid equivalent');
expect_report(!Grader::grade(Content::item('ct-B22-4a-r4'), 'Had I known about the traffic, I would have left earlier.')['correct'], 'Correct formal inversion must not be selected as needing editing');
echo "OK: $n report and draft-import regression checks; " . count($drafts) . " draft rows validated\n";
