<?php
// Landing page for "Sign in with englishfever.com". The WordPress plugin sends a signed, single-use token.
require __DIR__ . '/src/bootstrap.php';

header('Cache-Control: no-store');
try {
    Auth::ssoLogin((string) ($_GET['token'] ?? ''));
    header('Location: ./#/home');
    exit;
} catch (ApiError $e) {
    http_response_code($e->status);
    header('Content-Type: text/html; charset=utf-8');
    $msg = htmlspecialchars($e->getMessage(), ENT_QUOTES);
    echo '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        . '<title>Sign in</title><body style="font-family:system-ui;background:#F7F5EE;color:#1E1E2C;display:grid;place-items:center;min-height:100vh;margin:0">'
        . '<div style="max-width:420px;padding:32px"><h1 style="font-size:22px">We could not sign you in</h1><p>' . $msg . '</p>'
        . '<p><a style="color:#C42554" href="./">Go to the practice app</a></p></div>';
}
