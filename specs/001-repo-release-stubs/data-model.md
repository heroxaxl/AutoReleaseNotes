# Data Model: Repo Release Stubs

## Entities

### RepositoryList
- **Represents**: The newline-delimited input file at `data/repo/repos.txt`
- **Fields**:
  - `lines`: ordered list of raw strings (one per line)

### RepositoryUrl
- **Represents**: A candidate GitHub repository URL read from the list
- **Fields**:
  - `raw_url`: original string from the file
  - `normalized_url`: canonical HTTPS URL after normalization
  - `owner`: repository owner/organization (derived from URL)
  - `repo_name`: repository name (derived from URL)
  - `reachable`: boolean derived from HTTP reachability check

### ReleaseStubFile
- **Represents**: The generated output markdown file for a reachable repo
- **Fields**:
  - `path`: `data/releases/<repo_name>.md`
  - `content`: empty (0 bytes)

## Rules & Invariants

- Ignore empty/whitespace-only lines.
- Normalize URL variants (trailing slash and optional `.git` suffix).
- De-duplicate by `normalized_url` before reachability checks.
- Only write within `data/releases/`.
- If stub file already exists, overwrite it with an empty file.
