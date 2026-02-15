# Feature Specification: Repo Release Stubs

**Feature Branch**: `001-repo-release-stubs`  
**Created**: 2026-02-15  
**Status**: Draft  
**Input**: User description: "Create a script to read data/repo/repos.txt, validate reachable GitHub repo URLs, and create blank markdown release files in data/releases named after each repo"

## Clarifications

### Session 2026-02-15

- Q: How should the script determine whether a GitHub repo URL is "reachable"? → A: HTTP check repo page (200 or redirect to 200) with a short timeout.
- Q: What should the script do if the target stub file already exists? → A: Overwrite existing file.
- Q: Which GitHub URL formats should the script accept and normalize? → A: Normalize HTTPS variants (trailing slash, optional `.git`).
- Q: What should the generated markdown stub contain? → A: Completely empty file (0 bytes).
- Q: How should the script handle duplicate repositories in `data/repo/repos.txt`? → A: Ignore duplicates.
- Q: What technology stack should be used? → A: Python 3.14+ with pytest (BDD style).
- Q: Should the generator fetch and write actual release notes? → A: Yes; fetch via unauthenticated GitHub Releases API.
- Q: Which releases should be included? → A: Published only (exclude drafts and prereleases).
- Q: How many releases should be included? → A: Default 10 most recent published releases.

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.
  
  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Generate blank release notes stubs from a repo list (Priority: P1)

As a maintainer, I want to generate a blank release notes markdown file per reachable GitHub repository listed in `data/repo/repos.txt`, so I can quickly start writing release notes for multiple repos.

**Why this priority**: This is the core value of the feature and enables the rest of the workflow.

**Independent Test**: Can be tested by providing a `repos.txt` containing a mix of reachable and unreachable URLs and verifying that only reachable repos produce new blank `.md` files in `data/releases/`.

**Acceptance Scenarios**:

1. **Given** `data/repo/repos.txt` contains multiple GitHub repository URLs, **When** the generator is run, **Then** it creates one blank markdown file per reachable repository in `data/releases/`.
2. **Given** `data/repo/repos.txt` includes an unreachable or invalid URL, **When** the generator is run, **Then** that entry is ignored and no file is created for it.

---

### User Story 2 - Use repository name derived from URL for file naming (Priority: P2)

As a maintainer, I want the generator to name each markdown file based on the repository name derived from the URL, so output files are predictable and easy to find.

**Why this priority**: Ensures the output is usable without manual renaming.

**Independent Test**: Can be tested by including known repo URLs and verifying that filenames match the expected repo names.

**Acceptance Scenarios**:

1. **Given** a URL like `https://github.com/org/repo`, **When** the generator creates the stub, **Then** the file is named `repo.md` in `data/releases/`.

---

### User Story 3 - Safe behavior when output files already exist (Priority: P3)

As a maintainer, I want the generator to overwrite existing stub files, so I can easily regenerate a clean set of stubs.

**Why this priority**: Enables repeatable generation without manual cleanup.

**Independent Test**: Can be tested by pre-creating an output file with known content and verifying the generator overwrites it.

**Acceptance Scenarios**:

1. **Given** `data/releases/repo.md` already exists, **When** the generator is run, **Then** it overwrites the file with a blank stub.

---

### User Story 4 - Fetch release notes and write them into markdown files (Priority: P1)

As a maintainer, I want the generator to fetch the latest published GitHub Releases for each reachable repository and write them into the corresponding markdown file, so the output contains real release notes instead of an empty stub.

**Why this priority**: This is the primary value for automation once reachability and naming are correct.

**Independent Test**: Can be tested by mocking GitHub API responses for a repo and verifying the generated markdown contains the expected release titles and bodies.

**Acceptance Scenarios**:

1. **Given** a reachable public repository, **When** the generator is run, **Then** `data/releases/<repo>.md` contains the most recent published releases formatted as markdown.
2. **Given** the repository has no published releases, **When** the generator is run, **Then** the output markdown file is created but contains a clear “no releases found” message.
3. **Given** the GitHub API returns a rate-limit or error response, **When** the generator is run, **Then** the repository is treated as unreachable for release fetching and processing continues for other entries.

---

[Add more user stories as needed, each with an assigned priority]

### Edge Cases

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right edge cases.
-->

- `data/repo/repos.txt` contains blank lines or surrounding whitespace.
- `data/repo/repos.txt` contains duplicate URLs.
- A URL is for GitHub but not a repository (e.g., org page).
- A URL includes a trailing slash or `.git` suffix.
- `data/releases/` directory is missing.
- Repo page is not reachable but its releases page is reachable.
- Repo has zero published releases.
- GitHub API rate limit is hit mid-run.

## Requirements *(mandatory)*

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right functional requirements.
-->

### Functional Requirements

- **FR-001**: The system MUST read `data/repo/repos.txt` as a newline-delimited list of GitHub repository URLs.
- **FR-002**: The system MUST ignore empty lines and leading/trailing whitespace in `data/repo/repos.txt`.
- **FR-002a**: The system MUST accept and normalize common GitHub HTTPS URL variants, including an optional trailing slash and an optional `.git` suffix.
- **FR-002b**: The system MUST ignore duplicated repositories by de-duplicating the normalized repository URLs before processing.
- **FR-003**: The system MUST check whether each repository URL is reachable by performing an HTTP request to the repository page and treating it as reachable if it returns 200 or redirects (301/302) to a page that returns 200, using a default timeout of 5 seconds per URL.
- **FR-003a**: If the repository page is not reachable, the system MUST retry reachability by appending `/releases` to the normalized repository URL and treating the repository as reachable if that page returns 200 (or redirects to 200) within the same timeout.
- **FR-004**: The system MUST ignore unreachable repositories and continue processing remaining entries.
- **FR-005**: For each reachable repository URL, the system MUST derive the repository name and create/overwrite a markdown file at `data/releases/<repo_name>.md`.
- **FR-005a**: The system MUST fetch the latest published releases for each reachable repository using the unauthenticated GitHub Releases API endpoint `https://api.github.com/repos/<owner>/<repo>/releases`.
- **FR-005b**: The system MUST include only published releases by excluding items where `draft=true` or `prerelease=true`.
- **FR-005c**: The system MUST include up to 10 most recent published releases per repository by default.
- **FR-005d**: The system MUST write the fetched release notes into the markdown file using headings and sections per release (title/tag/date/body), and MUST preserve the release body as markdown.
- **FR-006**: If `data/releases/<repo_name>.md` already exists, the system MUST overwrite it deterministically with the newly generated content.
- **FR-007**: The system MUST create the `data/releases/` directory if it does not exist.

### Key Entities *(include if feature involves data)*

- **Repository List**: The newline-delimited input file containing candidate GitHub repository URLs.
- **Repository URL**: A string identifying a GitHub repository; used to derive the repository name.
- **Release Stub File**: A blank markdown file created per reachable repository.

### Implementation Constraints

- The implementation MUST target Python 3.14+.
- Automated tests MUST use pytest and follow a BDD style (Given/When/Then).
- The implementation SHOULD use standard library HTTP and JSON parsing.

## Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable success criteria.
  These must be technology-agnostic and measurable.
-->

### Measurable Outcomes

- **SC-001**: For a `repos.txt` containing at least 1 reachable repo URL, running the generator creates at least 1 new stub file in `data/releases/`.
- **SC-002**: For a `repos.txt` containing at least 1 unreachable repo URL, the generator completes successfully and still processes reachable entries.
- **SC-003**: For a pre-existing output file `data/releases/<repo_name>.md`, running the generator overwrites it with a blank stub.
- **SC-004**: Output filenames match the repository name derived from each reachable repository URL.
- **SC-005**: For a repository with at least 1 published release, the generated markdown file contains the release title and body for at least the most recent release.
