<?php
/**
 * Plugin Name: EF Practice – sign in with englishfever.com
 * Description: Lets logged-in englishfever.com users (Tutor LMS students and instructors) open the tenses practice app without registering again, adds their practice time to the "My activity" tracker (respecting their tracking choice) and shows their practice results. Shortcodes: [ef_practice_button], [ef_practice_banner], [ef_practice_results].
 * Version:     1.4.0
 * Author:      English Fever
 * License:     GPLv2 or later
 *
 * Setup (once): add these two lines to wp-config.php, above "That's all, stop editing!":
 *     define( 'EF_PRACTICE_URL',    'https://practice.englishfever.com' );   // where the app lives, no trailing slash
 *     define( 'EF_PRACTICE_SECRET', '64 random hex characters, the same as sso_secret in the app config' );
 *
 * Links (put them in menus, buttons, anywhere; the address can be any page of the site):
 *     https://YOUR-SITE/?ef_practice=open   Logged-in students are signed in automatically and land in the app.
 *                                           Visitors go to the app's welcome page, where they can start as guests.
 *                                           USE THIS ONE in menus and on the homepage.
 *     https://YOUR-SITE/?ef_practice=go     Always asks for the website login first (used by the app's "Continue with my account").
 *
 * After registering: when someone clicks "Create a free account" in the app, the app leaves a marker (cookie
 * ef_return, 3 days) and sends them to your registration form. If they are registered and logged in within 30
 * minutes, this plugin sends them straight back into the app (whatever page the form leaves them on), and the app
 * moves their guest results into the new account. If registration needs an email confirmation and they log in
 * later (up to 3 days), a "Back to your practice" bar is shown instead, with a small x to dismiss it.
 * Switch the automatic return off with  define( 'EF_PRACTICE_AUTO_RETURN', false );  to always show the bar.
 *
 * Optional, to send people who are not logged in to your own login page instead of wp-login.php:
 *     define( 'EF_PRACTICE_LOGIN_URL', 'https://englishfever.com/your-login-page/' );
 *
 * Then create a page "practice-login" with the shortcode [ef_practice_button]. In the app config, set
 *     'wp_login_url' => 'https://englishfever.com/practice-login/?ef_practice=go'
 * so the app's "Sign in with englishfever.com" button goes straight through (the page itself is never shown).
 *
 * Practice time in "My activity": the app sends each registered student's daily totals to
 *     https://YOUR-SITE/wp-json/ef-practice/v1/activity     (signed; set wp_sync_url in the app config to this address)
 * They are saved in the tracker table as one row per student per day (object_type 'practice'). Nothing is saved for
 * administrators, Tutor instructors or students who opted out of activity tracking. If a student opts out later, their
 * practice rows are deleted. [ef_practice_results] shows the student's practice results (put it under [ef_my_activity]).
 *
 * What is sent to the app: your WordPress user ID, display name, and whether the user is a teacher
 * (administrator or Tutor LMS instructor) and whether they allow activity tracking. No email address, no password.
 * The link works once and expires after 2 minutes.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function ef_practice_configured() {
	return defined( 'EF_PRACTICE_URL' ) && defined( 'EF_PRACTICE_SECRET' ) && strlen( EF_PRACTICE_SECRET ) >= 32;
}

function ef_practice_b64u( $s ) {
	return rtrim( strtr( base64_encode( $s ), '+/', '-_' ), '=' );
}

function ef_practice_token( WP_User $user ) {
	$roles   = (array) $user->roles;
	$teacher = user_can( $user, 'manage_options' ) || in_array( 'tutor_instructor', $roles, true );
	$payload = array(
		'uid'     => (int) $user->ID,
		'name'    => $user->display_name,
		'teacher' => (bool) $teacher,
		// the student's choice in the tracking consent (opt-out): true unless they said no
		'act'     => function_exists( 'ef_priv_activity_allowed' ) ? (bool) ef_priv_activity_allowed( $user->ID ) : true,
		'exp'     => time() + 120,
		'n'       => bin2hex( random_bytes( 8 ) ),
	);
	$p = ef_practice_b64u( wp_json_encode( $payload ) );
	return $p . '.' . ef_practice_b64u( hash_hmac( 'sha256', $p, EF_PRACTICE_SECRET, true ) );
}

/* ?ef_practice=open  logged in: into the app; visitors: the app's welcome page (guests allowed).
   ?ef_practice=go    always requires the website login first. */
add_action( 'template_redirect', function () {
	$mode = isset( $_GET['ef_practice'] ) ? sanitize_key( wp_unslash( $_GET['ef_practice'] ) ) : '';
	if ( 'go' !== $mode && 'open' !== $mode ) {
		return;
	}
	if ( ! ef_practice_configured() ) {
		wp_die( esc_html__( 'The practice app is not set up yet.', 'ef-practice' ), '', array( 'response' => 503 ) );
	}
	nocache_headers();
	ef_practice_clear_return();
	// wp_safe_redirect would block the other host, so allow exactly the configured one.
	add_filter( 'allowed_redirect_hosts', function ( $hosts ) {
		$hosts[] = wp_parse_url( EF_PRACTICE_URL, PHP_URL_HOST );
		return $hosts;
	} );
	if ( ! is_user_logged_in() ) {
		if ( 'open' === $mode ) {
			wp_safe_redirect( rtrim( EF_PRACTICE_URL, '/' ) . '/' );
			exit;
		}
		$back = add_query_arg( 'ef_practice', 'go', is_singular() ? get_permalink() : home_url( '/' ) );
		if ( defined( 'EF_PRACTICE_LOGIN_URL' ) && EF_PRACTICE_LOGIN_URL ) {
			wp_safe_redirect( add_query_arg( 'redirect_to', rawurlencode( $back ), EF_PRACTICE_LOGIN_URL ) );
		} else {
			wp_safe_redirect( wp_login_url( $back ) );
		}
		exit;
	}
	wp_safe_redirect( rtrim( EF_PRACTICE_URL, '/' ) . '/sso.php?token=' . rawurlencode( ef_practice_token( wp_get_current_user() ) ) );
	exit;
} );

/* ───────── back into the app after registering ───────── */

function ef_practice_clear_return() {
	if ( ! isset( $_COOKIE['ef_return'] ) ) {
		return;
	}
	$host = (string) wp_parse_url( home_url(), PHP_URL_HOST );
	$base = array( 'expires' => time() - 3600, 'path' => '/', 'secure' => is_ssl(), 'httponly' => true, 'samesite' => 'Lax' );
	foreach ( array_unique( array( '', $host, preg_replace( '/^www\./', '', $host ) ) ) as $domain ) {
		setcookie( 'ef_return', '', $base + array( 'domain' => $domain ) );
	}
	unset( $_COOKIE['ef_return'] );
}

/** Seconds since the person clicked "Create a free account" in the app (a huge number when there is no marker). */
function ef_practice_return_age() {
	$t = isset( $_COOKIE['ef_return'] ) ? (int) $_COOKIE['ef_return'] : 0;
	return $t > 0 ? max( 0, time() - $t ) : PHP_INT_MAX;
}

/** True when the app should send this person back: straight away right after registering (30 minutes), otherwise show the bar. */
function ef_practice_return_is_automatic() {
	return ! ( defined( 'EF_PRACTICE_AUTO_RETURN' ) && ! EF_PRACTICE_AUTO_RETURN ) && ef_practice_return_age() <= 1800;
}

/** True for a normal logged-in student page view that came from the app within the last 3 days. */
function ef_practice_came_from_app() {
	if ( empty( $_COOKIE['ef_return'] ) || ! ef_practice_configured() || ! is_user_logged_in() ) {
		return false;
	}
	if ( is_admin() || wp_doing_ajax() || wp_doing_cron() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) || 'GET' !== ( $_SERVER['REQUEST_METHOD'] ?? '' ) ) {
		return false;
	}
	if ( ef_practice_return_age() > 3 * DAY_IN_SECONDS ) {
		ef_practice_clear_return();
		return false;
	}
	if ( ! ef_practice_is_tracked_student( get_current_user_id() ) ) {
		ef_practice_clear_return();
		return false;
	}
	return true;
}

/* the small x on the bar: forget the marker and stay on the same page */
add_action( 'template_redirect', function () {
	if ( ! isset( $_GET['ef_practice_dismiss'] ) ) {
		return;
	}
	nocache_headers();
	ef_practice_clear_return();
	$here = ( is_ssl() ? 'https://' : 'http://' ) . wp_unslash( $_SERVER['HTTP_HOST'] ?? '' ) . wp_unslash( $_SERVER['REQUEST_URI'] ?? '/' );
	wp_safe_redirect( remove_query_arg( 'ef_practice_dismiss', esc_url_raw( $here ) ) );
	exit;
}, 5 );

add_action( 'template_redirect', function () {
	if ( isset( $_GET['ef_practice'] ) || ! ef_practice_came_from_app() || ! ef_practice_return_is_automatic() ) {
		return; // otherwise the bar below is shown
	}
	nocache_headers();
	ef_practice_clear_return();
	$here = ( is_ssl() ? 'https://' : 'http://' ) . wp_unslash( $_SERVER['HTTP_HOST'] ?? '' ) . wp_unslash( $_SERVER['REQUEST_URI'] ?? '/' );
	wp_safe_redirect( add_query_arg( 'ef_practice', 'open', esc_url_raw( $here ) ) ); // the current page + ?ef_practice=open
	exit;
}, 6 );

add_action( 'wp_footer', function () {
	if ( isset( $_GET['ef_practice'] ) || ! ef_practice_came_from_app() || ef_practice_return_is_automatic() ) {
		return;
	}
	$bar = 'position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#020101;color:#E9E5DA;padding:14px 18px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:center;font-size:16px;';
	$btn = 'background:#D82C5E;color:#fff;padding:10px 22px;border-radius:999px;font-weight:600;text-decoration:none;';
	echo '<div id="ef-return-bar" style="' . esc_attr( $bar ) . '"><span>Your account is ready.</span>'
		. '<a href="' . esc_url( ef_practice_link( 'open' ) ) . '" style="' . esc_attr( $btn ) . '">Back to your practice</a>'
		. '<a href="' . esc_url( add_query_arg( 'ef_practice_dismiss', '1' ) ) . '" aria-label="Close" style="color:#C9C4B8;text-decoration:none;font-size:22px;line-height:1;padding:4px 8px;">&times;</a></div>';
}, 99 );

/** The link for the current page, in the "open" mode (works on any front-end page). */
function ef_practice_link( $mode = 'open' ) {
	$base = is_singular() ? get_permalink() : home_url( '/' );
	return add_query_arg( 'ef_practice', 'go' === $mode ? 'go' : 'open', $base ? $base : home_url( '/' ) );
}

add_shortcode( 'ef_practice_button', function ( $atts ) {
	$atts  = shortcode_atts(
		array(
			'label' => 'Start practising',
			'class' => 'ef-practice-btn',
			'mode'  => 'open',
		),
		$atts
	);
	$href  = ef_practice_link( $atts['mode'] );
	// Styled inline so it looks right on any theme (English Fever raspberry, pill shape).
	$style = 'display:inline-block;background:#D82C5E;color:#fff;padding:14px 32px;border-radius:999px;'
		. 'font-weight:600;font-size:17px;line-height:1.2;text-decoration:none;border:0;cursor:pointer;';
	return sprintf(
		'<p style="margin:24px 0;"><a class="%s" style="%s" href="%s">%s</a></p>',
		esc_attr( $atts['class'] ),
		esc_attr( $style ),
		esc_url( $href ),
		esc_html( $atts['label'] )
	);
} );

/* [ef_practice_banner lang="en|lv"]: a ready-made homepage block. Texts can be changed with title="", text="", button="", eyebrow="". */
add_shortcode( 'ef_practice_banner', function ( $atts ) {
	$texts = array(
		'en' => array(
			'eyebrow' => 'Free · A2.1 – B1.2',
			'title'   => 'Practise English grammar',
			'text'    => 'Short tasks with clear feedback after every answer. Start with a free placement test. No registration needed.',
			'button'  => 'Start practising',
		),
		'lv' => array(
			'eyebrow' => 'Bezmaksas · A2.1 – B1.2',
			'title'   => 'Trenējiet angļu valodas gramatiku',
			'text'    => 'Īsi uzdevumi ar skaidru paskaidrojumu pēc katras atbildes. Sāciet ar bezmaksas līmeņa noteikšanas testu. Reģistrācija nav nepieciešama.',
			'button'  => 'Sākt praksi',
		),
	);
	$atts = shortcode_atts( array( 'lang' => 'en', 'eyebrow' => '', 'title' => '', 'text' => '', 'button' => '' ), $atts );
	$t    = $texts[ isset( $texts[ $atts['lang'] ] ) ? $atts['lang'] : 'en' ];
	foreach ( array( 'eyebrow', 'title', 'text', 'button' ) as $k ) {
		if ( '' !== $atts[ $k ] ) {
			$t[ $k ] = $atts[ $k ];
		}
	}
	$box = 'background:#020101;color:#E9E5DA;border-radius:20px;padding:clamp(24px,5vw,44px);margin:24px 0;display:flex;flex-wrap:wrap;gap:24px;align-items:center;justify-content:space-between;';
	$btn = 'display:inline-block;background:#D82C5E;color:#fff;padding:14px 32px;border-radius:999px;font-weight:600;font-size:17px;line-height:1.2;text-decoration:none;white-space:nowrap;';
	return '<section class="ef-practice-banner" style="' . esc_attr( $box ) . '">'
		. '<div style="flex:1 1 320px;min-width:0">'
		. '<div style="height:4px;width:48px;background:#DE3163;border-radius:4px;margin-bottom:16px"></div>'
		. '<div style="font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:#DEC17A;font-weight:700;margin-bottom:8px">' . esc_html( $t['eyebrow'] ) . '</div>'
		. '<h2 style="color:#fff;font-size:clamp(24px,4vw,32px);line-height:1.2;margin:0 0 10px">' . esc_html( $t['title'] ) . '</h2>'
		. '<p style="margin:0;color:#C9C4B8;max-width:52ch;font-size:17px;line-height:1.55">' . esc_html( $t['text'] ) . '</p>'
		. '</div>'
		. '<a href="' . esc_url( ef_practice_link( 'open' ) ) . '" style="' . esc_attr( $btn ) . '">' . esc_html( $t['button'] ) . '</a>'
		. '</section>';
} );

/* ───────── practice time -> "My activity" tracker (table wp_ef_aktivitate, snippet "Student activity tracking") ───────── */

function ef_practice_key() {
	return hash_hmac( 'sha256', 'ef-tracker-v1', EF_PRACTICE_SECRET );
}

/** Students only: the tracker never records administrators or Tutor instructors. */
function ef_practice_is_tracked_student( $uid ) {
	if ( user_can( $uid, 'manage_options' ) ) {
		return false;
	}
	if ( function_exists( 'tutor_utils' ) && tutor_utils()->is_instructor( $uid ) ) {
		return false;
	}
	return true;
}

add_action( 'rest_api_init', function () {
	register_rest_route(
		'ef-practice/v1',
		'/activity',
		array(
			'methods'             => 'POST',
			'callback'            => 'ef_practice_rest_activity',
			'permission_callback' => 'ef_practice_rest_permission',
		)
	);
} );

/** The request must be signed by the app (shared secret) and be fresh. Replays are harmless: rows are set, not added. */
function ef_practice_rest_permission( WP_REST_Request $req ) {
	if ( ! ef_practice_configured() ) {
		return new WP_Error( 'ef_not_configured', 'Not set up.', array( 'status' => 503 ) );
	}
	$time = (string) $req->get_header( 'x_ef_time' );
	$sign = (string) $req->get_header( 'x_ef_sign' );
	if ( ! ctype_digit( $time ) || abs( time() - (int) $time ) > 120 ) {
		return new WP_Error( 'ef_bad_time', 'Request too old.', array( 'status' => 403 ) );
	}
	$expected = hash_hmac( 'sha256', $time . '.' . $req->get_body(), ef_practice_key() );
	if ( ! hash_equals( $expected, $sign ) ) {
		return new WP_Error( 'ef_bad_signature', 'Bad signature.', array( 'status' => 403 ) );
	}
	return true;
}

function ef_practice_rest_activity( WP_REST_Request $req ) {
	global $wpdb;
	$data = json_decode( $req->get_body(), true );
	if ( ! is_array( $data ) || empty( $data['user'] ) || empty( $data['days'] ) || ! is_array( $data['days'] ) || count( $data['days'] ) > 31 ) {
		return new WP_Error( 'ef_bad_request', 'Bad request.', array( 'status' => 400 ) );
	}
	$uid     = (int) $data['user'];
	$user    = get_userdata( $uid );
	$results = array();

	if ( ! $user || ! ef_practice_is_tracked_student( $uid ) ) {
		foreach ( $data['days'] as $d ) {
			if ( isset( $d['day'] ) && is_string( $d['day'] ) ) {
				$results[ $d['day'] ] = 'skipped';
			}
		}
		return rest_ensure_response( array( 'results' => $results ) );
	}
	// The tracker and the consent snippets must be there, otherwise record nothing.
	if ( ! function_exists( 'ef_akt_tabula' ) || ! function_exists( 'ef_priv_activity_allowed' ) ) {
		return new WP_Error( 'ef_tracker_missing', 'The activity tracker snippets are not active.', array( 'status' => 503 ) );
	}
	$allowed = ef_priv_activity_allowed( $uid );
	$table   = ef_akt_tabula();

	foreach ( $data['days'] as $d ) {
		if ( ! is_array( $d ) || empty( $d['day'] ) || ! is_string( $d['day'] ) || ! preg_match( '/^\d{4}-\d{2}-\d{2}$/', $d['day'] ) ) {
			continue;
		}
		$day = $d['day'];
		if ( ! $allowed ) {
			$results[ $day ] = 'no_consent';
			continue;
		}
		$secs  = min( 14400, max( 1, (int) ( $d['seconds'] ?? 0 ) ) ); // a day only counts as active with seconds > 0
		$tasks = max( 0, (int) ( $d['answers'] ?? 0 ) );
		$label = sprintf( 'Grammar practice (app): %d tasks', $tasks );
		$vkey  = md5( 'ef-practice|' . $uid . '|' . $day );        // 32 hex characters, one row per student and day
		$now   = current_time( 'mysql' );                           // site time, like the tracker itself
		$row   = $wpdb->get_row( $wpdb->prepare( "SELECT id, active_seconds FROM {$table} WHERE visit_key = %s AND user_id = %d", $vkey, $uid ) );
		if ( $row ) {
			$ok = false !== $wpdb->update(
				$table,
				array( 'active_seconds' => max( (int) $row->active_seconds, $secs ), 'last_ping' => $now, 'label' => $label ),
				array( 'id' => (int) $row->id ),
				array( '%d', '%s', '%s' ),
				array( '%d' )
			);
		} else {
			$started = ( current_time( 'Y-m-d' ) === $day ) ? $now : $day . ' 12:00:00';
			$ok      = false !== $wpdb->insert(
				$table,
				array(
					'user_id'        => $uid,
					'course_id'      => 0,
					'object_id'      => 0,
					'object_type'    => 'practice',
					'event'          => 'view',
					'visit_key'      => $vkey,
					'label'          => $label,
					'started_at'     => $started,
					'last_ping'      => $now,
					'active_seconds' => $secs,
				),
				array( '%d', '%d', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%d' )
			);
		}
		if ( ! $ok ) {
			return new WP_Error( 'ef_db_error', 'Could not save.', array( 'status' => 500 ) );
		}
		$results[ $day ] = 'recorded';
	}
	return rest_ensure_response( array( 'results' => $results ) );
}

/* A student who turns tracking off loses their practice rows (the tracker's own text says new tracking stops;
   practice rows are removed as well). Both the first choice and later changes pass through user meta. */
function ef_practice_purge_on_withdrawal( $meta_id, $uid, $key, $value ) {
	if ( 'ef_priv_activity_choice' === $key && 'no' === $value && function_exists( 'ef_akt_tabula' ) ) {
		global $wpdb;
		$wpdb->delete( ef_akt_tabula(), array( 'user_id' => (int) $uid, 'object_type' => 'practice' ), array( '%d', '%s' ) );
	}
}
add_action( 'added_user_meta', 'ef_practice_purge_on_withdrawal', 10, 4 );
add_action( 'updated_user_meta', 'ef_practice_purge_on_withdrawal', 10, 4 );

/* ───────── [ef_practice_results]: the student's own practice results ───────── */

add_shortcode( 'ef_practice_results', function ( $atts ) {
	$atts = shortcode_atts(
		array(
			'title'  => 'Grammar practice',
			'button' => 'Practise tenses',
			'plain'  => '0', // 1 = no card border, for placing it inside another card
		),
		$atts
	);
	if ( ! is_user_logged_in() || ! ef_practice_configured() ) {
		return '';
	}
	$uid = get_current_user_id();
	if ( ! ef_practice_is_tracked_student( $uid ) ) {
		return '';
	}
	$cache = 'ef_practice_sum_' . $uid;
	$sum   = get_transient( $cache );
	if ( false === $sum ) {
		$time = (string) time();
		$sign = hash_hmac( 'sha256', $time . '.summary:' . $uid, ef_practice_key() );
		$resp = wp_remote_get(
			rtrim( EF_PRACTICE_URL, '/' ) . '/api.php?r=wp/summary&uid=' . $uid,
			array(
				'timeout' => 4,
				'headers' => array(
					'X-EF-Time' => $time,
					'X-EF-Sign' => $sign,
				),
			)
		);
		if ( is_wp_error( $resp ) || 200 !== (int) wp_remote_retrieve_response_code( $resp ) ) {
			return '';
		}
		$sum = json_decode( wp_remote_retrieve_body( $resp ), true );
		if ( ! is_array( $sum ) ) {
			return '';
		}
		set_transient( $cache, $sum, 300 );
	}
	$go = esc_url( ef_practice_link( 'open' ) );
	$st = ( '1' === (string) $atts['plain'] )
		? 'border-top:1px solid #e6e6e6;margin:24px 0 0;padding:20px 0 0;'
		: 'background:#fff;border:1px solid #e6e6e6;border-radius:16px;padding:24px;margin:0 0 28px;';
	$bt = 'display:inline-block;background:#D82C5E;color:#fff;padding:12px 26px;border-radius:999px;font-weight:600;text-decoration:none;';
	ob_start();
	echo '<section class="ef-practice-results" style="' . esc_attr( $st ) . '"><h2 style="font-size:' . ( '1' === (string) $atts['plain'] ? '20' : '24' ) . 'px;margin:0 0 12px;line-height:1.3">' . esc_html( $atts['title'] ) . '</h2>';
	if ( empty( $sum['practice'] ) ) {
		echo '<p style="margin:0 0 16px">You have not practised yet. A short placement test shows where to start.</p>';
		echo '<a href="' . $go . '" style="' . esc_attr( $bt ) . '">' . esc_html( $atts['button'] ) . '</a></section>';
		return ob_get_clean();
	}
	$cards = array(
		array( 'Level estimate', $sum['level'] ? '≈ ' . $sum['level'] : '–' ),
		array( 'Correct answers', null === $sum['accuracy'] ? '–' : $sum['accuracy'] . '%' ),
		array( 'Tasks done', (int) $sum['answers'] ),
		array( 'Practice streak', (int) $sum['streak'] . ( 1 === (int) $sum['streak'] ? ' day' : ' days' ) ),
	);
	if ( null !== $sum['minutes'] ) {
		$cards[] = array( 'Practice time', (int) $sum['minutes'] . ' min' );
	}
	echo '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin:0 0 16px">';
	foreach ( $cards as $c ) {
		echo '<div style="border:1px solid #e6e6e6;border-radius:12px;padding:14px 16px"><div style="font-size:13px;color:#6b6b6b">' . esc_html( $c[0] ) . '</div><div style="font-size:24px;font-weight:700;color:#1E1E2C">' . esc_html( (string) $c[1] ) . '</div></div>';
	}
	echo '</div>';
	if ( ! empty( $sum['weak'] ) ) {
		$names = array();
		foreach ( $sum['weak'] as $w ) {
			$names[] = esc_html( $w['label'] ) . ( $w['level'] ? ' (≈ ' . esc_html( $w['level'] ) . ')' : '' );
		}
		echo '<p style="margin:0 0 16px"><strong>Worth practising next:</strong> ' . implode( ', ', $names ) . '</p>';
	}
	echo '<a href="' . $go . '" style="' . esc_attr( $bt ) . '">' . esc_html( $atts['button'] ) . '</a></section>';
	return ob_get_clean();
} );

add_action( 'admin_notices', function () {
	if ( ! current_user_can( 'manage_options' ) || ef_practice_configured() ) {
		return;
	}
	echo '<div class="notice notice-warning"><p><strong>EF Practice:</strong> add EF_PRACTICE_URL and EF_PRACTICE_SECRET to wp-config.php (see the top of the plugin file).</p></div>';
} );
