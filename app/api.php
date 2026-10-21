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

/** At most $max hits per $window seconds for one key (counted in the login_attempts table). */
function throttle(string $key, int $max, int $window, string $message): void
{
    if ((int) Db::val('SELECT COUNT(1) FROM login_attempts WHERE akey = ? AND at > ?', [$key, time() - $window]) >= $max) throw new ApiError($message, 429);
    Db::insert('login_attempts', ['akey' => $key, 'at' => time()]);
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
                'site_url' => Config::get('site_url', ''),
                'dashboard_url' => Config::get('dashboard_url', ''),
                'sso' => strlen((string) Config::get('sso_secret', '')) >= 32 && Config::get('sso_secret') !== 'CHANGE-ME',
                'contact_email' => Config::get('contact_email', ''),
                'version' => is_file(__DIR__ . '/src/version.php') ? (string) ((require __DIR__ . '/src/version.php')['version'] ?? 'dev') : 'dev',
            ]);

        case 'meta':
            $m = Content::meta();
            out(['levels' => $m['levels'], 'areas' => $m['areas'], 'skills' => $m['skills'], 'bloom' => $m['bloom'], 'placement_length' => Engine::PLACEMENT_LEN, 'placement_sizes' => Engine::PLACEMENT_SIZES]);

        case 'me':
            $u = Auth::user();
            $welcome = null;
            if ($u && !empty($_SESSION['welcome'])) { $welcome = $_SESSION['welcome']; unset($_SESSION['welcome']); }
            out(['user' => $u ? Auth::publicUser($u) : null, 'welcome' => $welcome]);

        case 'guest':
            $u = Auth::createGuest((string) ($in['nickname'] ?? ''), (int) ($in['t'] ?? 0), (string) ($in['website'] ?? ''));
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
                if ($u['provider'] !== 'guest' && Db::val('SELECT COUNT(1) FROM users WHERE nickname_key = ? AND id <> ?', [$key, $u['id']])) throw new ApiError('This name is taken. Try another.', 409);
                $upd['nickname'] = $n;
                if ($u['provider'] !== 'guest') $upd['nickname_key'] = $key;
            }
            if (isset($in['nickname'])) $upd['nick_set'] = 1;
            if (array_key_exists('avatar', $in)) $upd['avatar'] = Auth::validAvatar($in['avatar'] === null ? null : (string) $in['avatar']);
            if (isset($in['show_on_board']) && $u['provider'] !== 'guest') $upd['show_on_board'] = $in['show_on_board'] ? 1 : 0;
            if (isset($in['lang'])) $upd['lang'] = $in['lang'] === 'lv' ? 'lv' : 'en';
            if ($upd) Db::update('users', $upd, 'id = ?', [$u['id']]);
            out(['user' => Auth::publicUser(Db::one('SELECT * FROM users WHERE id = ?', [$u['id']]))]);

        case 'account/delete':
            $u = Auth::require();
            if (empty($in['confirm'])) throw new ApiError('Please confirm.', 400);
            foreach (['attempts', 'psessions', 'skill_state', 'activity'] as $t) Db::q("DELETE FROM $t WHERE user_id = ?", [$u['id']]);
            Db::q('DELETE FROM teacher_mine WHERE student_id = ? OR teacher_id = ?', [$u['id'], $u['id']]);
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
            if ($credit > 0 && (int) $u['track_time'] === 1) Stats::addActivity((int) $u['id'], $credit, 0, 0); // opted-out learners: time is not recorded
            Wp::afterResponse((int) $u['id'], false);
            out(['ok' => true]);

        case 'session/start':
            $u = Auth::require();
            throttle('sess:' . hash('sha256', $_SERVER['REMOTE_ADDR'] ?? '?'), 150, 3600, 'Too many new sessions from this connection. Please wait a little.');
            out(Engine::start((int) $u['id'], (string) ($in['mode'] ?? 'practice'), (array) ($in['skills'] ?? []), $in['level'] ?? null, (int) ($in['length'] ?? 10)));

        case 'session/resume':
            $u = Auth::require();
            out(['resume' => Engine::resume((int) $u['id'])]);

        case 'session/current':
            $u = Auth::require();
            out(Engine::current((int) $u['id'], (int) ($_GET['id'] ?? 0)));

        case 'session/answer':
            $u = Auth::require();
            // no person answers 45 tasks in a minute; scripts do. Guests also have a daily limit that points to registering.
            if ((int) Db::val('SELECT COUNT(1) FROM attempts WHERE user_id = ? AND created_at > ?', [$u['id'], time() - 60]) >= 45) throw new ApiError('Slow down a little.', 429);
            $dayCap = $u['provider'] === 'guest' ? 600 : 3000;
            if ((int) Db::val('SELECT COUNT(1) FROM attempts WHERE user_id = ? AND created_at > ?', [$u['id'], time() - 86400]) >= $dayCap) {
                throw new ApiError($u['provider'] === 'guest' ? 'You have done a lot of practice today as a guest. Create a free account to keep going.' : 'That is a lot for one day. Come back tomorrow.', 429);
            }
            $res = Engine::answer((int) $u['id'], (int) ($in['session_id'] ?? 0), (string) ($in['item_id'] ?? ''), $in['answer'] ?? '', (int) ($in['time_ms'] ?? 0));
            Wp::afterResponse((int) $u['id'], !empty($res['done']));
            out($res);

        case 'session/quit':
            $u = Auth::require();
            $sum = Engine::quit((int) $u['id'], (int) ($in['session_id'] ?? 0));
            Wp::afterResponse((int) $u['id'], true);
            out(['summary' => $sum]);

        case 'session/summary':
            $u = Auth::require();
            out(['summary' => Engine::summary((int) $u['id'], (int) ($_GET['id'] ?? 0))]);

        case 'leaderboard':
            $u = Auth::require();
            out(Stats::leaderboard((int) $u['id'], ($_GET['period'] ?? 'week') === 'all' ? 'all' : 'week'));

        case 'wp/summary':
            $wpUid = (int) ($_GET['uid'] ?? 0);
            if (!Wp::configured() && strlen((string) Config::get('sso_secret', '')) < 32) throw new ApiError('Not set up.', 503);
            if (!Wp::verify((string) ($_SERVER['HTTP_X_EF_TIME'] ?? ''), 'summary:' . $wpUid, (string) ($_SERVER['HTTP_X_EF_SIGN'] ?? ''))) throw new ApiError('Forbidden.', 403);
            out(Wp::summary($wpUid));

        case 'teacher/sync-status':
            Auth::requireTeacher();
            out(Wp::status());

        case 'teacher/students':
            $t = Auth::requireTeacher();
            out(Stats::teacherStudents((int) $t['id']));

        case 'teacher/student':
            $t = Auth::requireTeacher();
            out(Stats::teacherStudent((int) ($_GET['id'] ?? 0), (int) $t['id']));

        case 'teacher/mine':
            $t = Auth::requireTeacher();
            $sid = (int) ($in['user_id'] ?? 0);
            if (!Db::one("SELECT id FROM users WHERE id = ? AND role = 'student'", [$sid])) throw new ApiError('Student not found.', 404);
            Db::q('DELETE FROM teacher_mine WHERE teacher_id = ? AND student_id = ?', [$t['id'], $sid]);
            if (!empty($in['mine'])) Db::insert('teacher_mine', ['teacher_id' => (int) $t['id'], 'student_id' => $sid, 'added_at' => time()]);
            out(['ok' => true]);

        case 'teacher/moderate':
            Auth::requireTeacher();
            $sid = (int) ($in['user_id'] ?? 0);
            $target = Db::one("SELECT id, provider FROM users WHERE id = ? AND role = 'student'", [$sid]);
            if (!$target) throw new ApiError('Student not found.', 404);
            if (isset($in['hide'])) Db::update('users', ['board_hidden' => $in['hide'] ? 1 : 0], 'id = ?', [$sid]);
            if (!empty($in['reset_name'])) {
                $n = 'Learner ' . random_int(1000, 9999);
                Db::update('users', ['nickname' => $n, 'nickname_key' => $target['provider'] === 'guest' ? $n . '#' . bin2hex(random_bytes(4)) : mb_strtolower($n)], 'id = ?', [$sid]);
            }
            out(['ok' => true]);

        case 'teacher/export':
            $t = Auth::requireTeacher();
            $view = in_array($_GET['view'] ?? '', ['mine', 'registered'], true) ? $_GET['view'] : 'all';
            header('Content-Type: text/csv; charset=utf-8');
            header('Content-Disposition: attachment; filename="practice-attempts-' . $view . '-' . date('Y-m-d') . '.csv"');
            echo "\xEF\xBB\xBF" . Stats::exportAttempts($view, (int) $t['id']);
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
