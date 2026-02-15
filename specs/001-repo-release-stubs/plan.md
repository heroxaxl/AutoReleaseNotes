# Implementation Plan: Repo Release Stubs

**Branch**: `001-repo-release-stubs` | **Date**: 2026-02-15 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-repo-release-stubs/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Create a Python script that reads `data/repo/repos.txt` (one GitHub repo URL per line), checks which repos are reachable via HTTP, and generates markdown files in `data/releases/` named after each reachable repo. For each reachable repo, fetch up to 10 most recent published GitHub Releases via the unauthenticated GitHub Releases API and render them into the markdown file. Runs are deterministic and idempotent for project-controlled artifacts: duplicate repos are ignored; stub files in `data/releases/` are overwritten.

**Artifacts**:

- [research.md](./research.md)
- [data-model.md](./data-model.md)
- [quickstart.md](./quickstart.md)
- [contracts/](./contracts/)

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.14+  
**Primary Dependencies**: Standard library only (preferred)  
**Storage**: Files (reads `data/repo/repos.txt`, writes `data/releases/*.md`)  
**Testing**: pytest (BDD style: Given/When/Then)  
**Target Platform**: macOS (developer machine), should remain POSIX-friendly  
**Project Type**: Single repository utility script  
**Performance Goals**: Handle tens to hundreds of repo URLs in a single run with short per-URL timeouts  
**Constraints**: Network calls must use a short timeout; GitHub API calls must be unauthenticated; no writes outside repo root; safe overwrites limited to `data/releases/*.md`  
**Scale/Scope**: Small; focused on GitHub repo URL normalization, reachability checks, GitHub Releases API fetch, and markdown rendering

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Passes if the plan maintains:
  - Deterministic outputs for the same inputs
  - Script portability and clear prerequisite failures
  - Safety-by-default (writes limited to allowlisted output directories)
  - Idempotent behavior (re-running converges)

No constitution violations expected.

## Project Structure

### Documentation (this feature)

```text
specs/001-repo-release-stubs/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
scripts/
└── generate-release-stubs.py

tests/
└── test_generate_release_stubs.py

data/
├── repo/
│   └── repos.txt
└── releases/
    └── *.md
```

**Structure Decision**: Add a single Python generator under `scripts/` and a pytest suite under `tests/`. The generator reads from `data/repo/repos.txt` and writes to `data/releases/`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |

## Next Steps

- Run `/speckit.tasks` to generate `tasks.md` for implementation.
- After tasks are generated, run `/speckit.implement` (or implement manually) to add:
  - `scripts/generate-release-stubs.py`
  - `tests/test_generate_release_stubs.py`
