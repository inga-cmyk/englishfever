#!/usr/bin/env python3
"""Make a WordPress import file (WXR) with every lesson page: dist/wordpress/english-fever-b1-pages.xml
Import it with Tools > Import > WordPress. Run tools/build.py first."""
import glob, os, re, zipfile
from html import escape
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEVEL = os.environ.get("EF_LEVEL", "B1").upper(); LVL = LEVEL.lower()
DIST = os.path.join(ROOT, "dist") if LEVEL == "B1" else os.path.join(ROOT, "dist", LVL)
NAMES = {"1-grammar": "Grammar", "2-vocabulary": "Vocabulary", "3-reading": "Reading", "4-listening": "Listening", "5-speaking": "Speaking", "6-writing": "Writing"}
posts, pid = [], 100
def page(title, slug, content, parent=0, order=0):
    global pid; pid += 1
    posts.append(f"""<item><title>{escape(title)}</title><link>https://example.com/{slug}/</link><dc:creator><![CDATA[admin]]></dc:creator>
<guid isPermaLink="false">english-fever-{LVL}-{pid}</guid><content:encoded><![CDATA[{content}]]></content:encoded><excerpt:encoded><![CDATA[]]></excerpt:encoded>
<wp:post_id>{pid}</wp:post_id><wp:post_date><![CDATA[2026-01-01 00:00:00]]></wp:post_date><wp:post_date_gmt><![CDATA[2026-01-01 00:00:00]]></wp:post_date_gmt>
<wp:comment_status><![CDATA[closed]]></wp:comment_status><wp:ping_status><![CDATA[closed]]></wp:ping_status><wp:post_name><![CDATA[{slug}]]></wp:post_name>
<wp:status><![CDATA[draft]]></wp:status><wp:post_parent>{parent}</wp:post_parent><wp:menu_order>{order}</wp:menu_order><wp:post_type><![CDATA[page]]></wp:post_type><wp:post_password><![CDATA[]]></wp:post_password></item>""")
    return pid
course = page(f"English Fever {LEVEL}", f"english-fever-{LVL}", f"<p>English course ({LEVEL}). Choose a unit.</p>")
for ud in sorted(glob.glob(os.path.join(ROOT, f"courses/{LVL}/unit-*"))):
    n = int(ud[-2:]); title = re.search(r"# Unit \d+: (.*)", open(os.path.join(ud, "INDEX.md")).read()).group(1)
    links = []
    uid = page(f"Unit {n}: {title}", f"{LVL}-unit-{n}", "<p>Work through the six lessons in order.</p>", course, n)
    for i, f in enumerate(sorted(glob.glob(os.path.join(ud, "lesson-*.html")))):
        key = os.path.basename(f)[7:-5]
        page(f"Unit {n} · {NAMES[key]}", f"{LVL}-unit-{n}-{key.split('-')[1]}", open(f, encoding="utf-8").read(), uid, i + 1)
xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:wfw="http://wellformedweb.org/CommentAPI/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:wp="http://wordpress.org/export/1.2/">
<channel><title>English Fever</title><wp:wxr_version>1.2</wp:wxr_version>
{chr(10).join(posts)}
</channel></rss>"""
os.makedirs(os.path.join(DIST, "wordpress"), exist_ok=True)
open(os.path.join(DIST, "wordpress", f"english-fever-{LVL}-pages.xml"), "w", encoding="utf-8").write(xml)
# one zip per kind: H5P files, Tutor LMS quizzes (csv + json + description), writing assignments
def bundle(name, pattern, strip_from_unit=True):
    with zipfile.ZipFile(os.path.join(DIST, name), "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(glob.glob(os.path.join(ROOT, pattern))):
            z.write(f, os.path.basename(f) if "h5p" in name else os.path.relpath(f, os.path.join(ROOT, "courses", LVL)))
bundle("all-h5p.zip", f"{os.path.relpath(DIST, ROOT)}/h5p/*.h5p")
bundle("tutor-lms-quizzes.zip", f"courses/{LVL}/unit-*/tutor-lms/*.*")
bundle("tutor-lms-assignments.zip", f"courses/{LVL}/unit-*/assignment/*.*")
print(len(posts), "pages written")
