<?php
// JSON API. One entry point: api.php?r=<route>
require __DIR__ . '/src/bootstrap.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

function out($data, int $status = 200): void
{
    http_response_code($status);
    echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}

function body(): array
{
    $raw = file_get_contents('php://input');
    $d = $raw ? json_decode($raw, true) : [];
    return is_array($d) ? $d : [];
}

try {
    $route = $_GET['r'] ?? '';
    $method = $_SERVER['REQUEST_METHOD'];
    if ($method === 'POST' && ($_SERVER['HTTP_X_EF'] ?? '') !== '1') throw new ApiError('Bad request.', 400);
    $in = $method === 'POST' ? body() : [];

    switch ($route) {
        case 'config':
            out([
                'site_name' => Config::get('site_name', 'English Fever'),
                'privacy_url' => Config::get('privacy_url', '#'),
                'wp_login_url' => Config::get('wp_login_url', ''),
                'register_url' => Config::get('register_url', ''),
                'sso' => strlen((string) Config::get('sso_secret', '')) >= 32 && Config::get('sso_secret') !== 'CHANGE-ME',
                'contact_email' => Config::get('contact_email', ''),
            ]);

        case 'meta':
            $m = Content::meta();
            out(['levels' => $m['levels'], 'skills' => $m['skills'], 'bloom' => $m['bloom'], 'placement_length' => Engine::PLACEMENT_LEN]);

        case 'me':
            $u = Auth::user();
            out(['user' => $u ? Auth::publicUser($u) : null]);

        case 'register':
            $u = Auth::register((string) ($in['nickname'] ?? ''), (string) ($in['password'] ?? ''));
            out(['user' => Auth::publicUser($u)]);

        case 'login':
            $u = Auth::attempt((string) ($in['nickname'] ?? ''), (string) ($in['password'] ?? ''));
            out(['user' => Auth::publicUser($u)]);

        case 'logout':
            Auth::logout();
            out(['ok' => true]);

        case 'account/profile':
            $u = Auth::require();
            $upd = [];
            if (isset($in['nickname']) && $in['nickname'] !== $u['nickname']) {
                $n = Auth::validNickname((string) $in['nickname']);
                $key = mb_strtolower($n);
                if (Db::val('SELECT COUNT(1) FROM users WHERE nickname_key = ? AND id <> ?', [$key, $u['id']])) throw new ApiError('This nickname is taken. Try another.', 409);
                $upd['nickname'] = $n;
                $upd['nickname_key'] = $key;
            }
            if (isset($in['nickname'])) $upd['nick_set'] = 1;
            if (isset($in['show_on_board'])) $upd['show_on_board'] = $in['show_on_board'] ? 1 : 0;
            if ($upd) Db::update('users', $upd, 'id = ?', [$u['id']]);
            out(['user' => Auth::publicUser(Db::one('SELECT * FROM users WHERE id = ?', [$u['id']]))]);

        case 'account/password':
            $u = Auth::require();
            if ($u['provider'] !== 'local') throw new ApiError('Your password is managed on englishfever.com.', 400);
            if (!password_verify((string) ($in['old'] ?? ''), (string) $u['pass_hash'])) throw new ApiError('Your current password is not correct.', 400);
            $new = (string) ($in['new'] ?? '');
            if (mb_strlen($new) < 4 || mb_strlen($new) > 100) throw new ApiError('New password: at least 4 characters.', 400);
            Db::update('users', ['pass_hash' => password_hash($new, PASSWORD_DEFAULT), 'must_change' => 0], 'id = ?', [$u['id']]);
            out(['ok' => true]);

        case 'account/delete':
            $u = Auth::require();
            if (mb_strtolower(trim((string) ($in['confirm'] ?? ''))) !== mb_strtolower($u['nickname'])) throw new ApiError('Type your nickname to confirm.', 400);
            foreach (['attempts', 'psessions', 'skill_state', 'activity'] as $t) Db::q("DELETE FROM $t WHERE user_id = ?", [$u['id']]);
            Db::q('DELETE FROM users WHERE id = ?', [$u['id']]);
            Auth::logout();
            out(['ok' => true]);

        case 'account/export':
            $u = Auth::require();
            $data = [
                'user' => ['nickname' => $u['nickname'], 'provider' => $u['provider'], 'joined' => $u['created_at']],
                'attempts' => Db::all('SELECT item_id, skill, level, bloom, correct, answer, time_ms, created_at FROM attempts WHERE user_id = ? ORDER BY id', [$u['id']]),
                'activity' => Db::all('SELECT day, seconds, answers, xp FROM activity WHERE user_id = ? ORDER BY day', [$u['id']]),
            ];
            out($data);

        case 'dashboard':
            $u = Auth::require();
            out(Stats::dashboard((int) $u['id']));

        case 'heartbeat':
            $u = Auth::require();
            $req = max(0, min(30, (int) ($in['seconds'] ?? 0)));
            $last = $_SESSION['last_hb'] ?? 0;
            $now = time();
            $credit = $last ? min($req, max(0, $now - $last + 2)) : min($req, 15);
            $_SESSION['last_hb'] = $now;
            if ($credit > 0) Stats::addActivity((int) $u['id'], $credit, 0, 0);
            out(['ok' => true]);

        case 'session/start':
            $u = Auth::require();
            out(Engine::start((int) $u['id'], (string) ($in['mode'] ?? 'practice'), (array) ($in['skills'] ?? []), $in['level'] ?? null, (int) ($in['length'] ?? 10)));

        case 'session/resume':
            $u = Auth::require();
            out(['resume' => Engine::resume((int) $u['id'])]);

        case 'session/current':
            $u = Auth::require();
            out(Engine::current((int) $u['id'], (int) ($_GET['id'] ?? 0)));

        case 'session/answer':
            $u = Auth::require();
            out(Engine::answer((int) $u['id'], (int) ($in['session_id'] ?? 0), (string) ($in['item_id'] ?? ''), $in['answer'] ?? '', (int) ($in['time_ms'] ?? 0)));

        case 'session/quit':
            $u = Auth::require();
            out(['summary' => Engine::quit((int) $u['id'], (int) ($in['session_id'] ?? 0))]);

        case 'session/summary':
            $u = Auth::require();
            out(['summary' => Engine::summary((int) $u['id'], (int) ($_GET['id'] ?? 0))]);

        case 'leaderboard':
            $u = Auth::require();
            out(Stats::leaderboard((int) $u['id'], ($_GET['period'] ?? 'week') === 'all' ? 'all' : 'week'));

        case 'teacher/students':
            Auth::requireTeacher();
            out(['students' => Stats::teacherStudents()]);

        case 'teacher/student':
            Auth::requireTeacher();
            out(Stats::teacherStudent((int) ($_GET['id'] ?? 0)));

        case 'teacher/reset-password':
            Auth::requireTeacher();
            $s = Db::one("SELECT * FROM users WHERE id = ? AND role = 'student'", [(int) ($in['user_id'] ?? 0)]);
            if (!$s) throw new ApiError('Student not found.', 404);
            if ($s['provider'] !== 'local') throw new ApiError('This student signs in with englishfever.com. Reset the password on the website.', 400);
            $alphabet = 'abcdefghjkmnpqrstuvwxyz23456789';
            $temp = '';
            for ($i = 0; $i < 6; $i++) $temp .= $alphabet[random_int(0, strlen($alphabet) - 1)];
            Db::update('users', ['pass_hash' => password_hash($temp, PASSWORD_DEFAULT), 'must_change' => 1], 'id = ?', [$s['id']]);
            out(['temp_password' => $temp, 'nickname' => $s['nickname']]);

        case 'teacher/export':
            Auth::requireTeacher();
            header('Content-Type: text/csv; charset=utf-8');
            header('Content-Disposition: attachment; filename="practice-attempts-' . date('Y-m-d') . '.csv"');
            echo "\xEF\xBB\xBF" . Stats::exportAttempts();
            exit;

        default:
            throw new ApiError('Not found.', 404);
    }
} catch (ApiError $e) {
    out(['error' => $e->getMessage()], $e->status);
} catch (Throwable $e) {
    error_log('[practice] ' . $e);
    out(['error' => 'Something went wrong. Please try again.'] + (Config::get('debug') ? ['detail' => $e->getMessage() . ' @' . $e->getFile() . ':' . $e->getLine()] : []), 500);
}
