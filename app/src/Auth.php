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
            'show_on_board' => (bool) $u['show_on_board'], 'nick_set' => (bool) $u['nick_set'], 'must_change' => (bool) $u['must_change'],
        ];
    }

    public static function validNickname(string $n): string
    {
        $n = trim($n);
        if (!preg_match('/^[\p{L}\p{N}_.\-]{3,20}$/u', $n)) {
            throw new ApiError('Nickname: 3 to 20 letters, numbers, dots, dashes or underscores. No spaces.', 400);
        }
        if (preg_match('/^(admin|teacher|administrator|moderator|english ?fever|learner-\d+)$/iu', $n)) {
            throw new ApiError('Please choose another nickname.', 400);
        }
        return $n;
    }

    public static function register(string $nick, string $pass): array
    {
        $nick = self::validNickname($nick);
        if (mb_strlen($pass) < 4 || mb_strlen($pass) > 100) throw new ApiError('Password: at least 4 characters.', 400);
        $key = mb_strtolower($nick);
        if (Db::val('SELECT COUNT(1) FROM users WHERE nickname_key = ?', [$key])) throw new ApiError('This nickname is taken. Try another.', 409);
        $id = Db::insert('users', [
            'provider' => 'local', 'nickname' => $nick, 'nickname_key' => $key, 'pass_hash' => password_hash($pass, PASSWORD_DEFAULT),
            'role' => 'student', 'created_at' => time(), 'last_seen' => time(),
        ]);
        self::login($id);
        return Db::one('SELECT * FROM users WHERE id = ?', [$id]);
    }

    public static function attempt(string $nick, string $pass): array
    {
        $ip = $_SERVER['REMOTE_ADDR'] ?? '?';
        $key = hash('sha256', $ip . '|' . mb_strtolower(trim($nick)));
        $since = time() - 600;
        $fails = (int) Db::val('SELECT COUNT(1) FROM login_attempts WHERE akey = ? AND at > ?', [$key, $since]);
        if ($fails >= 8) throw new ApiError('Too many tries. Please wait 10 minutes and try again.', 429);
        $u = Db::one('SELECT * FROM users WHERE nickname_key = ? AND provider = ?', [mb_strtolower(trim($nick)), 'local']);
        if (!$u || !$u['pass_hash'] || !password_verify($pass, $u['pass_hash'])) {
            Db::insert('login_attempts', ['akey' => $key, 'at' => time()]);
            Db::q('DELETE FROM login_attempts WHERE at < ?', [time() - 86400]);
            throw new ApiError('Nickname or password is not correct.', 401);
        }
        Db::q('DELETE FROM login_attempts WHERE akey = ?', [$key]);
        self::login((int) $u['id']);
        return $u;
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

        $ext = (string) (int) $p['uid'];
        $role = !empty($p['teacher']) ? 'teacher' : 'student';
        $full = mb_substr(trim((string) ($p['name'] ?? '')), 0, 150);
        $u = Db::one('SELECT * FROM users WHERE provider = ? AND external_id = ?', ['wp', $ext]);
        if ($u) {
            Db::update('users', ['role' => $role, 'full_name' => $full], 'id = ?', [$u['id']]);
            $id = (int) $u['id'];
        } else {
            do {
                $nick = 'learner-' . random_int(1000, 9999);
            } while (Db::val('SELECT COUNT(1) FROM users WHERE nickname_key = ?', [$nick]));
            $id = Db::insert('users', [
                'provider' => 'wp', 'external_id' => $ext, 'nickname' => $nick, 'nickname_key' => $nick, 'full_name' => $full,
                'role' => $role, 'nick_set' => $role === 'teacher' ? 1 : 0, 'created_at' => time(), 'last_seen' => time(),
            ]);
            if ($role === 'teacher') {
                $tn = self::uniqueNick($full ?: 'teacher');
                Db::update('users', ['nickname' => $tn, 'nickname_key' => mb_strtolower($tn)], 'id = ?', [$id]);
            }
        }
        self::login($id);
        return Db::one('SELECT * FROM users WHERE id = ?', [$id]);
    }

    private static function uniqueNick(string $base): string
    {
        $base = preg_replace('/[^\p{L}\p{N}_.\-]+/u', '', $base) ?: 'teacher';
        $base = mb_substr($base, 0, 16);
        if (mb_strlen($base) < 3) $base .= 'xyz';
        $try = $base;
        $i = 1;
        while (Db::val('SELECT COUNT(1) FROM users WHERE nickname_key = ?', [mb_strtolower($try)])) $try = $base . (++$i);
        return $try;
    }
}
