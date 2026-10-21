<?php
final class ApiError extends Exception
{
    public int $status;
    public function __construct(string $msg, int $status = 400)
    {
        parent::__construct($msg);
        $this->status = $status;
    }
}

final class Config
{
    private static array $cfg = [];
    public static function load(): void
    {
        $file = __DIR__ . '/../config/config.php';
        if (is_file($file)) {
            self::$cfg = require $file;
        } elseif (PHP_SAPI === 'cli-server' || getenv('EF_DEV') === '1' || PHP_SAPI === 'cli') {
            self::$cfg = require __DIR__ . '/../config/config.local.php';
        } else {
            http_response_code(500);
            header('Content-Type: application/json');
            echo json_encode(['error' => 'Not configured: create config/config.php (see config.sample.php).']);
            exit;
        }
    }
    public static function get(string $key, $default = null)
    {
        return self::$cfg[$key] ?? $default;
    }
    public static function all(): array
    {
        return self::$cfg;
    }
}

final class Auth
{
    public static function user(): ?array
    {
        static $cache = false;
        if ($cache !== false) return $cache;
        $id = $_SESSION['uid'] ?? null;
        if (!$id) return $cache = null;
        $u = Db::one('SELECT * FROM users WHERE id = ?', [$id]);
        if (!$u) {
            unset($_SESSION['uid']);
            return $cache = null;
        }
        if (time() - (int) $u['last_seen'] > 60) {
            Db::update('users', ['last_seen' => time()], 'id = ?', [$u['id']]);
        }
        return $cache = $u;
    }

    public static function require(): array
    {
        $u = self::user();
        if (!$u) throw new ApiError('Please sign in.', 401);
        return $u;
    }

    public static function requireTeacher(): array
    {
        $u = self::require();
        if ($u['role'] !== 'teacher') throw new ApiError('Teachers only.', 403);
        return $u;
    }

    public static function publicUser(array $u): array
    {
        return [
            'id' => (int) $u['id'], 'nickname' => $u['nickname'], 'role' => $u['role'], 'provider' => $u['provider'],
            'guest' => $u['provider'] === 'guest',
            'show_on_board' => (bool) $u['show_on_board'], 'nick_set' => (bool) $u['nick_set'],
        ];
    }

    /** A name others can see: a nickname or a real name. 2-30 characters, single spaces allowed. */
    public static function validNickname(string $n): string
    {
        $n = trim(preg_replace('/\s+/u', ' ', $n));
        if (!preg_match('/^[\p{L}\p{N}][\p{L}\p{N} ._\'\-]{1,29}$/u', $n)) {
            throw new ApiError('Use 2 to 30 letters or numbers.', 400);
        }
        if (preg_match('/^(admin|teacher|administrator|moderator|english ?fever|learner-\d+)$/iu', $n)) {
            throw new ApiError('Please choose another name.', 400);
        }
        return $n;
    }

    /** Guests need only a nickname. Their results live in this browser's session, so they can be lost. */
    public static function createGuest(string $nick): array
    {
        $nick = self::validNickname($nick);
        $ip = $_SERVER['REMOTE_ADDR'] ?? '?';
        $key = 'guest:' . hash('sha256', $ip);
        if ((int) Db::val('SELECT COUNT(1) FROM login_attempts WHERE akey = ? AND at > ?', [$key, time() - 3600]) >= 100) {
            throw new ApiError('Too many new guests from this connection. Please try again later.', 429);
        }
        Db::insert('login_attempts', ['akey' => $key, 'at' => time()]);
        Db::q('DELETE FROM login_attempts WHERE at < ?', [time() - 86400]);
        // the random suffix lets two guests use the same nickname without clashing with registered names
        $id = Db::insert('users', [
            'provider' => 'guest', 'nickname' => $nick, 'nickname_key' => mb_strtolower($nick) . '#' . bin2hex(random_bytes(4)),
            'role' => 'student', 'show_on_board' => 0, 'created_at' => time(), 'last_seen' => time(),
        ]);
        self::login($id);
        return Db::one('SELECT * FROM users WHERE id = ?', [$id]);
    }

    /** Move everything a guest did into a registered account, then remove the guest. */
    public static function mergeGuest(int $guestId, int $toId): void
    {
        $g = Db::one('SELECT id, provider FROM users WHERE id = ?', [$guestId]);
        if (!$g || $g['provider'] !== 'guest' || $guestId === $toId) return;
        Db::q('UPDATE attempts SET user_id = ? WHERE user_id = ?', [$toId, $guestId]);
        Db::q('UPDATE psessions SET user_id = ? WHERE user_id = ?', [$toId, $guestId]);
        foreach (Db::all('SELECT * FROM skill_state WHERE user_id = ?', [$guestId]) as $r) {
            $mine = Db::one('SELECT * FROM skill_state WHERE user_id = ? AND skill = ?', [$toId, $r['skill']]);
            if ($mine) {
                $n = (int) $mine['n'] + (int) $r['n'];
                $theta = $n ? (((float) $mine['theta'] * (int) $mine['n']) + ((float) $r['theta'] * (int) $r['n'])) / $n : (float) $mine['theta'];
                Db::update('skill_state', ['theta' => $theta, 'n' => $n, 'n_correct' => (int) $mine['n_correct'] + (int) $r['n_correct'], 'updated_at' => time()], 'user_id = ? AND skill = ?', [$toId, $r['skill']]);
            } else {
                Db::update('skill_state', ['user_id' => $toId], 'user_id = ? AND skill = ?', [$guestId, $r['skill']]);
            }
        }
        foreach (Db::all('SELECT * FROM activity WHERE user_id = ?', [$guestId]) as $r) {
            $mine = Db::one('SELECT day FROM activity WHERE user_id = ? AND day = ?', [$toId, $r['day']]);
            if ($mine) {
                Db::q('UPDATE activity SET seconds = seconds + ?, answers = answers + ?, xp = xp + ? WHERE user_id = ? AND day = ?', [$r['seconds'], $r['answers'], $r['xp'], $toId, $r['day']]);
            } else {
                Db::update('activity', ['user_id' => $toId], 'user_id = ? AND day = ?', [$guestId, $r['day']]);
            }
        }
        Db::q('DELETE FROM skill_state WHERE user_id = ?', [$guestId]);
        Db::q('DELETE FROM activity WHERE user_id = ?', [$guestId]);
        Db::q('DELETE FROM users WHERE id = ?', [$guestId]);
    }

    /** Guests who have not come back for 60 days are deleted together with their results. */
    public static function purgeGuests(): void
    {
        $old = Db::all("SELECT id FROM users WHERE provider = 'guest' AND last_seen < ?", [time() - 60 * 86400]);
        foreach ($old as $u) {
            foreach (['attempts', 'psessions', 'skill_state', 'activity'] as $t) Db::q("DELETE FROM $t WHERE user_id = ?", [$u['id']]);
            Db::q('DELETE FROM users WHERE id = ?', [$u['id']]);
        }
    }

    public static function login(int $id): void
    {
        session_regenerate_id(true);
        $_SESSION['uid'] = $id;
    }

    public static function logout(): void
    {
        $_SESSION = [];
        session_destroy();
    }

    // ───────── englishfever.com login (signed token from the WordPress plugin) ─────────

    public static function b64u(string $s): string
    {
        return rtrim(strtr(base64_encode($s), '+/', '-_'), '=');
    }

    public static function unb64u(string $s): string
    {
        return (string) base64_decode(strtr($s, '-_', '+/'));
    }

    public static function signToken(array $payload, string $secret): string
    {
        $p = self::b64u(json_encode($payload));
        return $p . '.' . self::b64u(hash_hmac('sha256', $p, $secret, true));
    }

    public static function ssoLogin(string $token): array
    {
        $secret = (string) Config::get('sso_secret', '');
        if (strlen($secret) < 32 || $secret === 'CHANGE-ME') throw new ApiError('Login with englishfever.com is not set up yet.', 503);
        $parts = explode('.', $token);
        if (count($parts) !== 2) throw new ApiError('Invalid login link.', 400);
        $expected = self::b64u(hash_hmac('sha256', $parts[0], $secret, true));
        if (!hash_equals($expected, $parts[1])) throw new ApiError('Invalid login link.', 400);
        $p = json_decode(self::unb64u($parts[0]), true);
        if (!is_array($p) || empty($p['uid']) || empty($p['exp']) || empty($p['n'])) throw new ApiError('Invalid login link.', 400);
        if ($p['exp'] < time() || $p['exp'] > time() + 600) throw new ApiError('This login link has expired. Please click the button on englishfever.com again.', 400);
        Db::q('DELETE FROM sso_used WHERE exp < ?', [time()]);
        if (Db::val('SELECT COUNT(1) FROM sso_used WHERE nonce = ?', [(string) $p['n']])) throw new ApiError('This login link was already used. Please click the button on englishfever.com again.', 400);
        Db::insert('sso_used', ['nonce' => (string) $p['n'], 'exp' => (int) $p['exp']]);

        $guestId = !empty($_SESSION['uid']) ? (int) $_SESSION['uid'] : 0; // a guest in this browser keeps their results
        $ext = (string) (int) $p['uid'];
        $role = !empty($p['teacher']) ? 'teacher' : 'student';
        $full = mb_substr(trim((string) ($p['name'] ?? '')), 0, 150);
        $u = Db::one('SELECT * FROM users WHERE provider = ? AND external_id = ?', ['wp', $ext]);
        if ($u) {
            Db::update('users', ['role' => $role, 'full_name' => $full], 'id = ?', [$u['id']]);
            $id = (int) $u['id'];
        } else {
            // suggest the learner's own name (they can change it on the next screen)
            $nick = self::uniqueNick($full);
            $id = Db::insert('users', [
                'provider' => 'wp', 'external_id' => $ext, 'nickname' => $nick, 'nickname_key' => mb_strtolower($nick), 'full_name' => $full,
                'role' => $role, 'nick_set' => $role === 'teacher' ? 1 : 0, 'created_at' => time(), 'last_seen' => time(),
            ]);
        }
        if ($guestId && $role === 'student') self::mergeGuest($guestId, $id);
        self::login($id);
        return Db::one('SELECT * FROM users WHERE id = ?', [$id]);
    }

    /** A free display name based on a real name or nickname. */
    private static function uniqueNick(string $base): string
    {
        $base = trim(preg_replace('/\s+/u', ' ', preg_replace('/[^\p{L}\p{N} ._\'\-]+/u', '', $base)));
        $base = mb_substr($base, 0, 26);
        if (mb_strlen($base) < 2) $base = 'learner-' . random_int(1000, 9999);
        $try = $base;
        $i = 1;
        while (Db::val('SELECT COUNT(1) FROM users WHERE nickname_key = ?', [mb_strtolower($try)])) $try = $base . ' ' . (++$i);
        return $try;
    }
}
