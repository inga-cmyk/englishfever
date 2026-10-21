# English Fever Practice (app)

PHP 8 + MySQL (SQLite for local testing), plain JavaScript, no build step, no third-party requests.
Setup, deployment and maintenance: see `../docs/PRACTICE-APP.md`.

    app/
      index.html, assets/      the browser app
      api.php, sso.php         JSON API and website-login landing page
      src/                     database, grading, adaptive engine, stats, auth
      content/                 question bank (generated; contains the answers, blocked from the web)
      authoring/               question bank source (Python) and the build/validate script
      wp-plugin/               the WordPress plugin for sign-in with englishfever.com
      tests/                   grader test (PHP), simulated learners and login tests (Python)
      config/                  config.sample.php (copy to config.php on the server)
