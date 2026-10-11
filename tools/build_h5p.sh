#!/usr/bin/env bash
# Zips each <unit>/h5p/<activity>/ folder into dist/<unit>-<activity>.h5p
# Note: a package holding only h5p.json + content/content.json has no library code.
# Upload to WordPress; if the H5P plugin reports missing libraries, install the
# content type from the H5P Hub first (H5P Content > Libraries).
set -euo pipefail
unit="${1:?usage: build_h5p.sh courses/<level>/<unit>}"
mkdir -p dist
for dir in "$unit"/h5p/*/; do
  [ -f "$dir/h5p.json" ] || continue
  name="$(basename "$dir")"
  tmp="$(mktemp -d)"
  cp "$dir/h5p.json" "$tmp/"
  mkdir "$tmp/content" && cp "$dir/content.json" "$tmp/content/"
  out="$PWD/dist/$(basename "$unit")-$name.h5p"
  (cd "$tmp" && zip -qr "$out" .)
  rm -rf "$tmp"; echo "built $out"
done
