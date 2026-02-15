# Contracts

This feature is implemented as a local script (no network API surface exposed by this repository).

## I/O Contract

- **Input**: `data/repo/repos.txt` (newline-delimited GitHub repo URLs)
- **Output**: `data/releases/<repo_name>.md` (empty file for each reachable repo)
