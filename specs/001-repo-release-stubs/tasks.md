# Tasks: Repo Release Stubs

**Input**: Design documents from `/specs/001-repo-release-stubs/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/, quickstart.md

**Tests**: Included (pytest, BDD style Given/When/Then)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the Python script + pytest test structure.

- [X] T001 Create source file `scripts/generate-release-stubs.py`
- [X] T002 Create test file `tests/test_generate_release_stubs.py`
- [X] T003 [P] Add `pytest.ini` to configure test discovery (if needed) at `pytest.ini`
- [X] T004 [P] Add `.gitignore` entries for Python artifacts (e.g., `__pycache__/`, `.pytest_cache/`) in `.gitignore`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared utilities and rules required by all user stories.

- [X] T005 Implement URL normalization helper in `scripts/generate-release-stubs.py` (strip whitespace, trailing `/`, optional `.git`)
- [X] T006 Implement repo name extraction helper in `scripts/generate-release-stubs.py` (derive `<owner>` and `<repo_name>` from normalized URL)
- [X] T007 Implement deduplication logic in `scripts/generate-release-stubs.py` (de-duplicate by normalized URL)
- [X] T008 Implement filesystem safety helpers in `scripts/generate-release-stubs.py` (ensure `data/releases/` exists; allowlisted writes only)

**Checkpoint**: Foundation ready — user story implementation can now begin.

---

## Phase 3: User Story 1 - Generate blank release notes stubs from a repo list (Priority: P1) 🎯 MVP

**Goal**: Read `data/repo/repos.txt`, keep only reachable repos, and create/overwrite a 0-byte stub for each reachable repo.

**Independent Test**: With a repo list containing reachable + unreachable entries, only reachable ones produce stub files.

### Tests for User Story 1 (pytest BDD)

- [X] T009 [P] [US1] Write BDD test (Given repos.txt with reachable+unreachable, When run, Then only reachable stubs exist) in `tests/test_generate_release_stubs.py`
- [X] T010 [P] [US1] Add HTTP reachability tests using stdlib mocking (e.g., `unittest.mock` patching `urllib.request.urlopen`) for 200/redirect/404/timeout in `tests/test_generate_release_stubs.py`

### Implementation for User Story 1

- [X] T011 [US1] Implement repo list reader in `scripts/generate-release-stubs.py` (reads `data/repo/repos.txt`, ignores empty/whitespace-only lines)
- [X] T012 [US1] Implement HTTP reachability check in `scripts/generate-release-stubs.py` using standard library HTTP and stdlib mocking-friendly structure (treat 200 or redirect-to-200 as reachable; default timeout 5 seconds)
- [X] T013 [US1] Implement stub creation for reachable repos in `scripts/generate-release-stubs.py` (create/overwrite `data/releases/<repo>.md` as 0 bytes)
- [X] T014 [US1] Wire up main entrypoint in `scripts/generate-release-stubs.py` so `python3 scripts/generate-release-stubs.py` runs end-to-end

**Checkpoint**: US1 complete — generator creates blank stubs for reachable repos.

---

## Phase 4: User Story 2 - Use repository name derived from URL for file naming (Priority: P2)

**Goal**: Ensure output file naming is correctly derived from URL and stable after normalization.

**Independent Test**: For known URLs, stub filenames match `<repo>.md`.

### Tests for User Story 2 (pytest BDD)

- [X] T015 [P] [US2] Write BDD test for naming: Given URL `https://github.com/org/repo`, When processed, Then output is `data/releases/repo.md` in `tests/test_generate_release_stubs.py`
- [X] T016 [P] [US2] Write BDD test for normalization: Given URL variants with trailing `/` and/or `.git`, When processed, Then name is still `repo.md` in `tests/test_generate_release_stubs.py`

### Implementation for User Story 2

- [X] T017 [US2] Ensure name derivation uses normalized URL path segments in `scripts/generate-release-stubs.py`
- [X] T018 [US2] Ensure URL variants are normalized before reachability + naming in `scripts/generate-release-stubs.py`

**Checkpoint**: US2 complete — file naming is consistent across URL variants.

---

## Phase 5: User Story 3 - Safe behavior when output files already exist (Priority: P3)

**Goal**: Re-running the generator overwrites existing stub files deterministically (0 bytes).

**Independent Test**: If a stub exists and contains text, it becomes empty after the run.

### Tests for User Story 3 (pytest BDD)

- [X] T019 [P] [US3] Write BDD overwrite test: Given existing `data/releases/repo.md` with content, When run, Then file becomes empty in `tests/test_generate_release_stubs.py`

### Implementation for User Story 3

- [X] T020 [US3] Implement explicit overwrite semantics for existing stub paths in `scripts/generate-release-stubs.py`

**Checkpoint**: US3 complete — overwrite behavior is confirmed and deterministic.

---

## Phase 6: User Story 4 - Fetch release notes and write them into markdown files (Priority: P1)

**Goal**: For each reachable repo, fetch up to 10 most recent published GitHub Releases via the unauthenticated GitHub API and write them into `data/releases/<repo>.md`.

**Independent Test**: Mock GitHub API responses and verify markdown output contains expected release titles and bodies.

### Tests for User Story 4 (pytest BDD)

- [X] T025 [P] [US4] Write BDD test: Given GitHub API returns 2 published releases, When run, Then markdown contains both titles and bodies in `tests/test_generate_release_stubs.py`
- [X] T026 [P] [US4] Write BDD test: Given API returns only drafts/prereleases, When run, Then markdown contains "no releases found" message in `tests/test_generate_release_stubs.py`
- [X] T027 [P] [US4] Write BDD test: Given API returns 403 rate limit (or error), When run, Then repo is skipped and other repos continue in `tests/test_generate_release_stubs.py`

### Implementation for User Story 4

- [X] T028 [US4] Add GitHub API fetch helper in `scripts/generate_release_stubs.py` (GET releases endpoint, parse JSON, handle errors)
- [X] T029 [US4] Add filtering helper for published-only releases (exclude `draft=true` and `prerelease=true`) in `scripts/generate_release_stubs.py`
- [X] T030 [US4] Add default limit behavior (up to 10 most recent published releases) in `scripts/generate_release_stubs.py`
- [X] T031 [US4] Implement markdown renderer for releases (repo header + per-release sections with title/tag/date/body) in `scripts/generate_release_stubs.py`
- [X] T032 [US4] Wire generator to write rendered markdown instead of 0-byte files (still overwrite deterministically) in `scripts/generate_release_stubs.py`

**Checkpoint**: US4 complete — generated markdown contains fetched release notes (or a clear no-releases message).

---

## Phase 7: Polish & Cross-Cutting

- [X] T033 [P] Improve error messages and exit codes for GitHub API failures (rate limits, invalid JSON) in `scripts/generate_release_stubs.py`
- [X] T034 [P] Add lightweight stdout progress logging indicating whether releases were fetched or none found in `scripts/generate_release_stubs.py`
- [X] T035 Update `README.md` and `specs/001-repo-release-stubs/quickstart.md` with release-fetch behavior and constraints
- [X] T036 Run `./.venv/bin/pytest` locally and ensure all tests pass after US4 changes

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)** → required for everything
- **Phase 2 (Foundational)** → blocks all user stories
- **US1 (Phase 3)** → depends on Phase 2
- **US2 (Phase 4)** → depends on Phase 2 (may reuse helpers from Phase 2)
- **US3 (Phase 5)** → depends on Phase 2
- **Polish (Phase 6)** → after desired user stories

### MVP Scope

- MVP is **User Story 1** (Phases 1–3).

### Parallel Opportunities

- [P] tasks can be done in parallel, especially test authoring tasks (T009, T010, T015, T016, T019) and documentation/logging tasks (T021–T023).
