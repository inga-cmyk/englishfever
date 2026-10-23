<?php
// The login page styling hook with stand-ins for WordPress: php app/tests/wp_login_style_test.php  (no WordPress needed)
define('ABSPATH','/x/'); define('DAY_IN_SECONDS',86400);
define('EF_PRACTICE_URL','https://practice.example'); define('EF_PRACTICE_SECRET',str_repeat('a',64));
$H=[]; function add_action($n,$f,$p=10,$a=1){global $H;$H['a'][$n][]=$f;} function add_filter($n,$f,$p=10,$a=1){global $H;$H['f'][$n][]=$f;}
function __call_stub(){}
foreach(['add_shortcode','register_activation_hook','register_deactivation_hook','add_option','load_plugin_textdomain'] as $f) if(!function_exists($f)) eval("function $f(){}");
function esc_html__($t){return htmlspecialchars($t);} function wp_unslash($x){return $x;} function home_url($p=''){return 'https://site.example'.$p;}
require __DIR__ . '/../wp-plugin/ef-practice-sso/ef-practice-sso.php';
function run($label){ global $H; echo "== $label\n"; ob_start(); foreach($H['a']['login_head'] as $f) $f(); $css=ob_get_clean();
  echo ' style: ', strlen($css)?'yes':'no', ' | title: ', $H['f']['login_headertext'][0]('Powered by WordPress'), ' | url: ', $H['f']['login_headerurl'][0]('https://wordpress.org/'), ' | msg: ', substr(strip_tags($H['f']['login_message'][0]('')),0,40), "\n"; }
$_REQUEST=[]; $_COOKIE=[]; run('plain login');
$_REQUEST=['redirect_to'=>'https%3A%2F%2Fsite.example%2F%3Fef_practice%3Dgo']; run('from the app (redirect_to)');
$_REQUEST=[]; $_COOKIE=['ef_return'=>'123']; run('from the app (cookie)');

// where a visitor signs in
echo "== login page\n";
echo ' default: ', ef_practice_login_page(), "\n";
