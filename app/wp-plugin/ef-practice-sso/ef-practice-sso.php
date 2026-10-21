<?php
/**
 * Plugin Name: EF Practice – sign in with englishfever.com
 * Description: Lets logged-in englishfever.com users (Tutor LMS students and instructors) open the tenses practice app without registering again. Adds the [ef_practice_button] shortcode.
 * Version:     1.0.1
 * Author:      English Fever
 * License:     GPLv2 or later
 *
 * Setup (once): add these two lines to wp-config.php, above "That's all, stop editing!":
 *     define( 'EF_PRACTICE_URL',    'https://practice.englishfever.com' );   // where the app lives, no trailing slash
 *     define( 'EF_PRACTICE_SECRET', '64 random hex characters, the same as sso_secret in the app config' );
 *
 * Then put [ef_practice_button] on a page, for example "Practice". Use that page's address as wp_login_url in the app config.
 *
 * What is sent to the app: your WordPress user ID, display name, and whether the user is a teacher
 * (administrator or Tutor LMS instructor). No email address, no password. The link works once and expires after 2 minutes.
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
		'exp'     => time() + 120,
		'n'       => bin2hex( random_bytes( 8 ) ),
	);
	$p = ef_practice_b64u( wp_json_encode( $payload ) );
	return $p . '.' . ef_practice_b64u( hash_hmac( 'sha256', $p, EF_PRACTICE_SECRET, true ) );
}

/* The button points at the same page with ?ef_practice=go. This handler sends the visitor on. */
add_action( 'template_redirect', function () {
	if ( ! isset( $_GET['ef_practice'] ) || 'go' !== $_GET['ef_practice'] ) {
		return;
	}
	if ( ! ef_practice_configured() ) {
		wp_die( esc_html__( 'The practice app is not set up yet.', 'ef-practice' ), '', array( 'response' => 503 ) );
	}
	if ( ! is_user_logged_in() ) {
		$back = add_query_arg( 'ef_practice', 'go', is_singular() ? get_permalink() : home_url( '/' ) );
		wp_safe_redirect( wp_login_url( $back ) );
		exit;
	}
	$url = rtrim( EF_PRACTICE_URL, '/' ) . '/sso.php?token=' . rawurlencode( ef_practice_token( wp_get_current_user() ) );
	// wp_safe_redirect would block the other host, so allow exactly the configured one.
	add_filter( 'allowed_redirect_hosts', function ( $hosts ) {
		$hosts[] = wp_parse_url( EF_PRACTICE_URL, PHP_URL_HOST );
		return $hosts;
	} );
	wp_safe_redirect( $url );
	exit;
} );

add_shortcode( 'ef_practice_button', function ( $atts ) {
	$atts  = shortcode_atts(
		array(
			'label' => 'Start practising',
			'class' => 'ef-practice-btn',
		),
		$atts
	);
	$href  = add_query_arg( 'ef_practice', 'go', get_permalink() );
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

add_action( 'admin_notices', function () {
	if ( ! current_user_can( 'manage_options' ) || ef_practice_configured() ) {
		return;
	}
	echo '<div class="notice notice-warning"><p><strong>EF Practice:</strong> add EF_PRACTICE_URL and EF_PRACTICE_SECRET to wp-config.php (see the top of the plugin file).</p></div>';
} );
