#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT_DIR="$REPO_ROOT/data/releases"
OUTPUT_DIR="$REPO_ROOT/data/pdf"
CSS_FILE="$REPO_ROOT/resources/css/style-print.css"

REPO_NAME="AutoReleaseNotes"
REPO_URL="https://github.com/username/AutoReleaseNotes"

ensure_fresh_pdf_output() {
  local pdf_path="$1"

  if [[ -f "$pdf_path" ]]; then
    rm -f "$pdf_path"
  fi
}

mkdir -p "$OUTPUT_DIR"

shopt -s nullglob
md_files=("$INPUT_DIR"/*.md)

if [[ ${#md_files[@]} -eq 0 ]]; then
  echo "No .md files found in: $INPUT_DIR" >&2
  exit 1
fi

for md in "${md_files[@]}"; do
  base="$(basename "$md" .md)"
  out="$OUTPUT_DIR/$base.pdf"

  ensure_fresh_pdf_output "$out"

  tmp_html="$OUTPUT_DIR/$base.html"

  pandoc "$md" \
    --from=gfm \
    --to=html5 \
    --standalone \
    --metadata title="$REPO_NAME" \
    -o "$tmp_html"

  weasyprint \
    --base-url "$REPO_ROOT" \
    --stylesheet "$CSS_FILE" \
    "$tmp_html" \
    "$out"

  rm -f "$tmp_html"

  echo "Wrote: $out"
done
