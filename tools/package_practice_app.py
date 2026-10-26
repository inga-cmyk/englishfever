#!/usr/bin/env python3
"""Build the two files you upload:
    dist/practice-app.zip         the whole practice app (first install)
    dist/practice-app-update.zip  the same without config/ and var/ (use this to update a running app)
    dist/ef-practice-sso.zip   the WordPress plugin (Plugins > Add New > Upload)

    python3 tools/package_practice_app.py
Runs the content build and the grading test first, so a broken question bank is never packaged.
"""
import os, subprocess, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.join(ROOT, "app")
DIST = os.path.join(ROOT, "dist")

subprocess.run([sys.executable, os.path.join(APP, "authoring", "build.py")], check=True, stdout=subprocess.DEVNULL)
env = dict(os.environ, EF_DEV="1")
subprocess.run([sys.executable, os.path.join(APP, "tests", "bank_integrity_test.py")], check=True)
subprocess.run(["php", os.path.join(APP, "tests", "grader_test.php")], check=True, env=env)
subprocess.run(["php", os.path.join(APP, "tests", "bank_update_test.php")], check=True, env=env)

EXCLUDE_DIRS = {"authoring", "tests", "wp-plugin", "__pycache__", ".git"}
EXCLUDE_FILES = {"config/config.php", "config/config.local.php", "sso-demo.php", "README.md", "content/items.json", "content/meta.json", "content/retired.json"}
os.makedirs(DIST, exist_ok=True)
out = os.path.join(DIST, "practice-app.zip")
n = 0
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for base, dirs, files in os.walk(APP):
        rel_base = os.path.relpath(base, APP)
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDE_DIRS)
        if rel_base == "var":
            dirs[:] = []
        for f in sorted(files):
            rel = os.path.normpath(os.path.join(rel_base, f))
            if rel in EXCLUDE_FILES or f.endswith((".sqlite", ".sqlite-wal", ".sqlite-shm", ".pyc")):
                continue
            if rel_base == "var" and f not in (".htaccess",):
                continue
            z.write(os.path.join(base, f), rel)
            n += 1
    # the prepared question drafts, so the Questions page can add them all with one button
    import glob as _glob
    for f in sorted(_glob.glob(os.path.join(APP, "..", "docs", "task-drafts", "*.csv"))):
        z.write(f, "content/drafts/" + os.path.basename(f)); n += 1
    # an empty writable folder for PHP sessions, protected by .htaccess
    z.writestr("var/sessions/.keep", "")
    # which package is live (shown in the footer of the app)
    import time
    stamp = time.strftime("%Y-%m-%d %H:%M")
    z.writestr("src/version.php", "<?php\nreturn ['version' => '" + stamp + "'];\n")
    n += 1
print(f"{out}: {n} files, version {stamp}")

# The update zip: the same code without config/ and var/ (they already exist on the server), so extracting it over a running
# app creates no duplicate folders and cannot touch the settings or the data.
upd = os.path.join(DIST, "practice-app-update.zip")
with zipfile.ZipFile(out) as zin, zipfile.ZipFile(upd, "w", zipfile.ZIP_DEFLATED) as zout:
    for name in zin.namelist():
        if name.startswith(("config/", "var/")) or name == ".gitignore":
            continue
        zout.writestr(name, zin.read(name))
print(f"{upd}: update only (no config/, no var/)")

plug = os.path.join(DIST, "ef-practice-sso.zip")
src = os.path.join(APP, "wp-plugin", "ef-practice-sso")
with zipfile.ZipFile(plug, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(os.listdir(src)):
        z.write(os.path.join(src, f), os.path.join("ef-practice-sso", f))
print(plug)
