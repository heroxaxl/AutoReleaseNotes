## AutoReleaseNotes


## Overview

This repository contains sample release notes (GitHub-flavored Markdown) and a simple conversion pipeline to generate print-ready PDFs.

## Repository Structure

- **`data/releases/`**
  - Sample release notes markdown files.
- **`data/pdf/`**
  - Generated PDF outputs.
- **`resources/css/style-print.css`**
  - Print stylesheet (A4 sizing/margins and paged-media rules for header/footer/page numbers).
- **`scripts/convert-releases-to-pdf.sh`**
  - Converts every markdown file in `data/releases/` to a PDF in `data/pdf/`.

## Sample Data

- **`data/releases/sample-release-notes.md`**
  - A multi-version imaginary release notes dataset.
- **`data/releases/fantasy-software-release-notes.md`**
  - Includes a table, emojis, and mixed English/Thai/Japanese notes.

## Generate PDFs

### Requirements

- `pandoc`
- `weasyprint`

On macOS (Homebrew):

```sh
brew install pandoc weasyprint
```

### Convert all release notes

```sh
bash scripts/convert-releases-to-pdf.sh
```

This will:

- Read every `*.md` in `data/releases/`
- Delete any existing matching `data/pdf/<name>.pdf` before converting
- Produce `data/pdf/<name>.pdf` using `resources/css/style-print.css`

## Generate release notes from GitHub repos

This feature reads `data/repo/repos.txt` (one GitHub repository URL per line) and creates/overwrites markdown files under `data/releases/` named after each reachable repo. For each reachable repo, it fetches up to 10 most recent published GitHub Releases via the unauthenticated GitHub Releases API and renders them into markdown.

### Requirements

- Python 3.14+

### Run

```sh
python3 scripts/generate-release-stubs.py
```

### Test

If `pytest` is not on your PATH, use a local virtual environment:

```sh
python3 -m venv .venv
./.venv/bin/python -m pip install -U pip pytest
./.venv/bin/pytest
```


