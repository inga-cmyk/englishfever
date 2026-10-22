<?php
// PDO wrapper. Works with SQLite (local testing) and MySQL (Hostinger).

final class Db
{
    public static PDO $pdo;
    public static string $driver;

    public static function connect(array $cfg): void
    {
        self::$driver = $cfg['driver'];
        if (self::$driver === 'sqlite') {
            $path = $cfg['sqlite'];
            @mkdir(dirname($path), 0775, true);
            self::$pdo = new PDO('sqlite:' . $path);
            self::$pdo->exec('PRAGMA foreign_keys = ON');
            self::$pdo->exec('PRAGMA journal_mode = WAL');
            self::$pdo->exec('PRAGMA busy_timeout = 5000');
        } else {
            $m = $cfg['mysql'];
            self::$pdo = new PDO(
                "mysql:host={$m['host']};dbname={$m['name']};charset=utf8mb4",
                $m['user'],
                $m['pass']
            );
        }
        self::$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        self::$pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
        self::$pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
    }

    public static function q(string $sql, array $p = []): PDOStatement
    {
        $st = self::$pdo->prepare($sql);
        $st->execute($p);
        return $st;
    }

    public static function all(string $sql, array $p = []): array
    {
        return self::q($sql, $p)->fetchAll();
    }

    public static function one(string $sql, array $p = []): ?array
    {
        $r = self::q($sql, $p)->fetch();
        return $r === false ? null : $r;
    }

    public static function val(string $sql, array $p = [])
    {
        $r = self::q($sql, $p)->fetch(PDO::FETCH_NUM);
        return $r === false ? null : $r[0];
    }

    public static function insert(string $table, array $row): int
    {
        $cols = array_keys($row);
        $sql = "INSERT INTO $table (" . implode(',', $cols) . ') VALUES (' . implode(',', array_fill(0, count($cols), '?')) . ')';
        self::q($sql, array_values($row));
        return (int) self::$pdo->lastInsertId();
    }

    public static function update(string $table, array $row, string $where, array $wp = []): void
    {
        $set = implode(',', array_map(fn($c) => "$c = ?", array_keys($row)));
        self::q("UPDATE $table SET $set WHERE $where", array_merge(array_values($row), $wp));
    }

    public static function ensureColumn(string $table, string $col, string $ddl): void
    {
        if (self::$driver === 'mysql') {
            $has = (int) self::val('SELECT COUNT(1) FROM information_schema.columns WHERE table_schema = DATABASE() AND table_name = ? AND column_name = ?', [$table, $col]);
        } else {
            $has = 0;
            foreach (self::all("PRAGMA table_info($table)") as $r) if ($r['name'] === $col) $has = 1;
        }
        if (!$has) self::$pdo->exec("ALTER TABLE $table ADD COLUMN $col $ddl");
    }

    public static function kvGet(string $k): ?string
    {
        $v = self::val('SELECT v FROM kv WHERE k = ?', [$k]);
        return $v === null ? null : (string) $v;
    }

    public static function kvSet(string $k, ?string $v): void
    {
        if (self::val('SELECT COUNT(1) FROM kv WHERE k = ?', [$k])) self::q('UPDATE kv SET v = ? WHERE k = ?', [$v, $k]);
        else self::q('INSERT INTO kv (k, v) VALUES (?, ?)', [$k, $v]);
    }

    /** Create tables if they do not exist yet. Safe to run on every request. */
    public static function migrate(): void
    {
        $my = self::$driver === 'mysql';
        $pk = $my ? 'BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY' : 'INTEGER PRIMARY KEY AUTOINCREMENT';
        $tail = $my ? ' ENGINE=InnoDB DEFAULT CHARSET=utf8mb4' : '';
        $str = $my ? 'VARCHAR(191)' : 'TEXT';
        $big = $my ? 'BIGINT' : 'INTEGER';
        $int = $my ? 'INT' : 'INTEGER';
        $txt = $my ? 'MEDIUMTEXT' : 'TEXT';

        $tables = [
            "CREATE TABLE IF NOT EXISTS users (
                id $pk,
                provider $str NOT NULL,
                external_id $str NULL,
                nickname $str NOT NULL,
                nickname_key $str NOT NULL,
                pass_hash $str NULL,
                full_name $str NULL,
                role $str NOT NULL DEFAULT 'student',
                show_on_board $int NOT NULL DEFAULT 1,
                nick_set $int NOT NULL DEFAULT 1,
                must_change $int NOT NULL DEFAULT 0,
                track_time $int NOT NULL DEFAULT 1,
                sso_at $big NOT NULL DEFAULT 0,
                board_hidden $int NOT NULL DEFAULT 0,
                avatar $str NULL,
                lang $str NULL,
                research $int NOT NULL DEFAULT 0,
                research_at $big NOT NULL DEFAULT 0,
                research_base $int NOT NULL DEFAULT 0,
                created_at $big NOT NULL,
                last_seen $big NOT NULL DEFAULT 0
            )$tail",
            "CREATE TABLE IF NOT EXISTS psessions (
                id $pk,
                user_id $big NOT NULL,
                mode $str NOT NULL,
                skills $txt NOT NULL,
                level $str NULL,
                target_len $int NOT NULL,
                n $int NOT NULL DEFAULT 0,
                n_correct $int NOT NULL DEFAULT 0,
                xp $int NOT NULL DEFAULT 0,
                state $txt NOT NULL,
                started_at $big NOT NULL,
                ended_at $big NULL
            )$tail",
            "CREATE TABLE IF NOT EXISTS attempts (
                id $pk,
                user_id $big NOT NULL,
                psession_id $big NOT NULL,
                item_id $str NOT NULL,
                skill $str NOT NULL,
                level $str NOT NULL,
                bloom $int NOT NULL,
                correct $int NOT NULL,
                answer $txt NULL,
                time_ms $int NOT NULL DEFAULT 0,
                xp $int NOT NULL DEFAULT 0,
                created_at $big NOT NULL
            )$tail",
            "CREATE TABLE IF NOT EXISTS skill_state (
                user_id $big NOT NULL,
                skill $str NOT NULL,
                theta DOUBLE PRECISION NOT NULL,
                n $int NOT NULL DEFAULT 0,
                n_correct $int NOT NULL DEFAULT 0,
                updated_at $big NOT NULL,
                PRIMARY KEY (user_id, skill)
            )$tail",
            "CREATE TABLE IF NOT EXISTS activity (
                user_id $big NOT NULL,
                day $str NOT NULL,
                seconds $int NOT NULL DEFAULT 0,
                answers $int NOT NULL DEFAULT 0,
                xp $int NOT NULL DEFAULT 0,
                PRIMARY KEY (user_id, day)
            )$tail",
            "CREATE TABLE IF NOT EXISTS login_attempts (
                id $pk,
                akey $str NOT NULL,
                at $big NOT NULL
            )$tail",
            "CREATE TABLE IF NOT EXISTS sync_wp (
                user_id $big NOT NULL,
                day $str NOT NULL,
                seconds $int NOT NULL DEFAULT 0,
                answers $int NOT NULL DEFAULT 0,
                base_seconds $int NOT NULL DEFAULT 0,
                synced_at $big NOT NULL,
                PRIMARY KEY (user_id, day)
            )$tail",
            "CREATE TABLE IF NOT EXISTS teacher_mine (
                teacher_id $big NOT NULL,
                student_id $big NOT NULL,
                added_at $big NOT NULL,
                PRIMARY KEY (teacher_id, student_id)
            )$tail",
            "CREATE TABLE IF NOT EXISTS conditions (
                user_id $big NOT NULL,
                factor $str NOT NULL,
                arm $str NOT NULL,
                seq $int NOT NULL DEFAULT 0,
                assigned_at $big NOT NULL,
                PRIMARY KEY (user_id, factor)
            )$tail",
            "CREATE TABLE IF NOT EXISTS reports (
                id $pk,
                user_id $big NOT NULL,
                item_id $str NOT NULL,
                reason $str NOT NULL,
                comment $txt NULL,
                answer $txt NULL,
                correct $int NULL,
                status $str NOT NULL DEFAULT 'new',
                created_at $big NOT NULL,
                updated_at $big NOT NULL
            )$tail",
            "CREATE TABLE IF NOT EXISTS custom_items (
                id $pk,
                item_id $str NOT NULL UNIQUE,
                skill $str NOT NULL,
                level $str NOT NULL,
                bloom $int NOT NULL,
                kind $str NOT NULL,
                data $txt NOT NULL,
                status $str NOT NULL DEFAULT 'draft',
                created_at $big NOT NULL,
                updated_at $big NOT NULL
            )$tail",
            "CREATE TABLE IF NOT EXISTS kv (
                k $str NOT NULL PRIMARY KEY,
                v $txt NULL
            )$tail",
            "CREATE TABLE IF NOT EXISTS sso_used (
                nonce $str NOT NULL PRIMARY KEY,
                exp $big NOT NULL
            )$tail",
        ];
        foreach ($tables as $sql) {
            self::$pdo->exec($sql);
        }
        self::ensureColumn('users', 'track_time', "$int NOT NULL DEFAULT 1"); // databases created before these columns existed
        self::ensureColumn('users', 'sso_at', "$big NOT NULL DEFAULT 0");
        self::ensureColumn('users', 'board_hidden', "$int NOT NULL DEFAULT 0");
        self::ensureColumn('users', 'avatar', "$str NULL");
        self::ensureColumn('users', 'lang', "$str NULL");
        self::ensureColumn('users', 'research', "$int NOT NULL DEFAULT 0");
        self::ensureColumn('users', 'research_at', "$big NOT NULL DEFAULT 0");
        self::ensureColumn('users', 'research_base', "$int NOT NULL DEFAULT 0");
        $indexes = [
            ['users', 'ux_users_nick', 'nickname_key', true],
            ['users', 'ix_users_ext', 'provider, external_id', false],
            ['attempts', 'ix_att_user', 'user_id, created_at', false],
            ['attempts', 'ix_att_sess', 'psession_id', false],
            ['psessions', 'ix_ps_user', 'user_id, started_at', false],
            ['login_attempts', 'ix_la', 'akey, at', false],
        ];
        foreach ($indexes as [$t, $n, $cols, $uniq]) {
            $u = $uniq ? 'UNIQUE ' : '';
            try {
                if ($my) {
                    $exists = self::val("SELECT COUNT(1) FROM information_schema.statistics WHERE table_schema = DATABASE() AND table_name = ? AND index_name = ?", [$t, $n]);
                    if (!$exists) self::$pdo->exec("CREATE {$u}INDEX $n ON $t ($cols)");
                } else {
                    self::$pdo->exec("CREATE {$u}INDEX IF NOT EXISTS $n ON $t ($cols)");
                }
            } catch (Throwable $e) {
                // index already exists or cannot be created; the app still works
            }
        }
    }
}
