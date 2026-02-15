# Quickstart: Repo Release Stubs

## Prerequisites

- Python 3.14+
- pytest

## Inputs

- `data/repo/repos.txt` contains one GitHub repository URL per line.

## Run

From the repository root:

```sh
python3 scripts/generate-release-stubs.py
```

## Outputs

- Creates/overwrites markdown files under:
  - `data/releases/<repo_name>.md`

Each output file contains up to 10 most recent published releases fetched from GitHub (title/tag/date and body preserved as markdown).

## Test

```sh
./.venv/bin/pytest
```
