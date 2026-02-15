# Fission-AI/OpenSpec

## v1.1.1 - OpenCode Command Fix
- Tag: `v1.1.1`
- Published: 2026-01-30
- URL: https://github.com/Fission-AI/OpenSpec/releases/tag/v1.1.1

## What's New in v1.1.1

A quick patch to fix OpenCode command references.

### Fixed

- **OpenCode command references** - Generated files now use the correct `/opsx-` hyphen format instead of `/opsx:` colon format, so commands work properly in OpenCode

---

## New Contributors

* @webrgp made their first contribution in https://github.com/Fission-AI/OpenSpec/pull/626

**Full Changelog**: https://github.com/Fission-AI/OpenSpec/compare/v1.1.0...v1.1.1

## v1.1.0 - Cross-Platform Fixes, Nix Improvements
- Tag: `v1.1.0`
- Published: 2026-01-30
- URL: https://github.com/Fission-AI/OpenSpec/releases/tag/v1.1.0

## What's New in v1.1.0

A stability release focused on fixing cross-platform path issues and improving the Nix build experience.

### Fixed

- **Codex global paths** - Codex adapter now resolves global paths correctly, fixing workflow file generation when run outside the project directory
- **Archive on networked/external drives** - Archive falls back to copy+remove when rename fails with EPERM or EXDEV errors
- **Windsurf workflow path** - Updated Windsurf adapter to use the correct `workflows` directory instead of the legacy `commands` path
- **Slash command hints** - Workflow completion messages now display helpful slash command hints for next steps

### Improved

- **Nix flake** - Version now read dynamically from package.json; source filtering excludes node_modules for faster builds
- **Nix CI** - Updated to latest nix-installer and magic-nix-cache actions

## New Contributors

- @jerome-benoit made their first contribution in #550
- @moe1214 made their first contribution in #601
- @CosticaPuntaru made their first contribution in #605
- @Haven-S made their first contribution in #616
- @yangjuncode made their first contribution in #610
- @CS-Tao made their first contribution in #603

## v1.0.2
- Tag: `v1.0.2`
- Published: 2026-01-27
- URL: https://github.com/Fission-AI/OpenSpec/releases/tag/v1.0.2

### Patch Changes

-   [#596](https://github.com/Fission-AI/OpenSpec/pull/596) [`e91568d`](https://github.com/Fission-AI/OpenSpec/commit/e91568deb948073f3e9d9bb2d2ab5bf8080d6cf4) Thanks [@TabishB](https://github.com/TabishB)! - ### Bug Fixes

    -   Clarified spec naming convention — Specs should be named after capabilities (`specs/<capability>/spec.md`), not changes
    -   Fixed task checkbox format guidance — Tasks now clearly require `- [ ]` checkbox format for apply phase tracking

## v1.0.1
- Tag: `v1.0.1`
- Published: 2026-01-26
- URL: https://github.com/Fission-AI/OpenSpec/releases/tag/v1.0.1

### Patch Changes

-   [#587](https://github.com/Fission-AI/OpenSpec/pull/587) [`943e0d4`](https://github.com/Fission-AI/OpenSpec/commit/943e0d41026d034de66b9442d1276c01b293eb2b) Thanks [@TabishB](https://github.com/TabishB)! - ### Bug Fixes

    -   Fixed incorrect archive path in onboarding documentation — the template now shows the correct path `openspec/changes/archive/YYYY-MM-DD-<name>/` instead of the incorrect `openspec/archive/YYYY-MM-DD--<name>/`

## v1.0.0 - The OPSX Release
- Tag: `v1.0.0`
- Published: 2026-01-26
- URL: https://github.com/Fission-AI/OpenSpec/releases/tag/v1.0.0

## What's New in v1.0.0

OpenSpec 1.0 marks the transition from experimental to stable. The workflow has been rebuilt around an action-based system where AI understands your project's state—what artifacts exist, what's ready to create, and what each action unlocks.

---

### ⚠️ Migrating from Pre-1.0

**Breaking changes:**
- Old commands removed — `/openspec:proposal`, `/openspec:apply`, `/openspec:archive` no longer exist
- Config files removed — Tool-specific files (`CLAUDE.md`, `.cursorrules`, `AGENTS.md`, `project.md`) are no longer generated

**To upgrade:** Run `openspec init`. Your existing work is safe—active changes, archived changes, and main specs are all preserved. Only obsolete config files are cleaned up (with confirmation).

→ [Migration guide](https://github.com/Fission-AI/OpenSpec/blob/main/docs/migration-guide.md)

---

### New

- **Action-based workflow** — Replaced the rigid proposal → apply → archive sequence with flexible actions. Edit any artifact anytime. The artifact graph tracks state automatically.

| Command | What it does |
| --- | --- |
| `/opsx:explore` | Think through ideas before committing to a change |
| `/opsx:new` | Start a new change |
| `/opsx:continue` | Create one artifact at a time (step-through) |
| `/opsx:ff` | Create all planning artifacts at once (fast-forward) |
| `/opsx:apply` | Implement tasks |
| `/opsx:verify` | Validate implementation matches artifacts |
| `/opsx:sync` | Sync delta specs to main specs |
| `/opsx:archive` | Archive completed change |
| `/opsx:bulk-archive` | Archive multiple changes with conflict detection |
| `/opsx:onboard` | Guided 15-minute walkthrough of complete workflow |

- **Dynamic instructions** — AI instructions are now assembled from three layers: context (your tech stack), rules (artifact-specific constraints), and templates (output structure). AI queries the CLI for real-time state instead of receiving static prompts.

- **Semantic spec syncing** — Delta specs use markers like `## ADDED Requirements` and `## MODIFIED Requirements`. Archive parses these at the requirement level, not brittle header matching.

- **Agent Skills** — Single `.claude/skills/` directory replaces 8+ scattered config files. YAML-fronted markdown files that work across Claude Code, Cursor, and Windsurf.

- **Onboarding skill** — `/opsx:onboard` walks new users through their first complete change with codebase-aware task suggestions. 11 phases, ~15 minutes.

- **Interactive setup** — `openspec init` shows animated welcome screen and searchable multi-select for tools. Pre-selects already-configured tools for easy refresh.

- **21 AI tools supported** — Claude Code, Cursor, Windsurf, Continue, Gemini CLI, GitHub Copilot, Amazon Q, Cline, RooCode, Kilo Code, Auggie, CodeBuddy, Qoder, Qwen, CoStrict, Crush, Factory, OpenCode, Antigravity, iFlow, and Codex.

- **Custom schemas** — Define custom artifact workflows in `openspec/schemas/` without touching package code.

### Fixed

- Claude Code YAML parsing failure when command names contained colons
- Task file parsing to handle trailing whitespace on checkbox lines
- JSON instruction output now separates context/rules from template (AI was copying constraint blocks into artifact files)

---

### Documentation

New guides: [Getting Started](https://github.com/Fission-AI/OpenSpec/blob/main/docs/getting-started.md) · [CLI Reference](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md) · [Commands](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md) · [Concepts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md) · [Customization](https://github.com/Fission-AI/OpenSpec/blob/main/docs/customization.md)

## v0.23.0 - Bulk Archive, Simplified Setup
- Tag: `v0.23.0`
- Published: 2026-01-21
- URL: https://github.com/Fission-AI/OpenSpec/releases/tag/v0.23.0

## What's New in v0.23.0

This release streamlines both active development and post-implementation workflows.

### New

- **Bulk archive** - Archive multiple completed changes at once with `/opsx:bulk-archive`. Validates specs, detects conflicts, and shows a single confirmation before archiving.

### Improved

- **Config setup** - Creating a new OpenSpec config now uses sensible defaults with helpful comments instead of asking questions. Get started faster.

## v0.22.0 - Project Configuration
- Tag: `v0.22.0`
- Published: 2026-01-20
- URL: https://github.com/Fission-AI/OpenSpec/releases/tag/v0.22.0

## What's New in v0.22.0

OpenSpec now supports per-project configuration, letting you customize behavior and define schemas for project-specific workflows. (Still very experimental, feedback appreciated!)

More docs available here (search for schema and/or config): https://github.com/Fission-AI/OpenSpec/blob/main/docs/experimental-workflow.md

### New

- **Project configuration** - Configure OpenSpec per-project with `openspec/config.yaml` to inject custom rules, specify context files, and control schema resolution
- **Project-local schemas** - Define custom artifact schemas in `openspec/schemas/` for project-specific workflows
- **Schema management** - Inspect and manage artifact schemas with new `openspec schema` commands (`list`, `show`, `export`, `validate`)

### Fixed

- Config loading now handles null `rules` field without errors

## v0.21.0 - Feedback Command, Nix Support
- Tag: `v0.21.0`
- Published: 2026-01-19
- URL: https://github.com/Fission-AI/OpenSpec/releases/tag/v0.21.0

## What's New in v0.21.0

This release adds better feedback tooling and Nix support, plus guardrails to keep exploration focused.

### New

- **Feedback command** - Submit feedback directly from the CLI with `openspec feedback`. Creates GitHub Issues with automatic metadata or provides a manual submission link if that fails.
- **Nix flake support** - Install and develop OpenSpec using Nix with `flake.nix`, including automated maintenance and CI validation.

### Improved

- **Change inference in `opsx apply`** - Automatically detects which change to apply from conversation context, prompts when ambiguous.
- **Archive sync assessment** - Clearer guidance on delta spec locations during sync operations.

### Fixed

- **Explore mode guardrails** - Explore mode now explicitly prevents implementation to keep focus on thinking and discovery.

## v0.20.0 - Verify Command
- Tag: `v0.20.0`
- Published: 2026-01-14
- URL: https://github.com/Fission-AI/OpenSpec/releases/tag/v0.20.0

## What's New in v0.20.0

This release adds validation tooling and fixes several workflow issues.

### New

- **Verify command** - Validate that your implementation matches the spec with `/opsx:verify`. Catches drift between what you planned and what got built.

### Fixed

- Vitest no longer spawns process storms—worker parallelism is now capped
- Agent workflows use non-interactive mode for validation commands
- PowerShell completions generator now produces valid syntax (removed trailing commas)

## v0.19.0
- Tag: `v0.19.0`
- Published: 2026-01-11
- URL: https://github.com/Fission-AI/OpenSpec/releases/tag/v0.19.0

## New Features

- **Continue IDE support** – OpenSpec now generates slash commands for [Continue](https://continue.dev/), expanding editor integration options alongside Cursor, Windsurf, Claude Code, and others
- **Shell completions for Bash, Fish, and PowerShell** – Run `openspec completion install` to set up tab completion in your preferred shell
- **`/opsx:explore` command** – A new thinking partner mode for exploring ideas and investigating problems before committing to changes
- **Codebuddy slash command improvements** – Updated frontmatter format for better compatibility

## Bug Fixes

- Shell completions now correctly offer parent-level flags (like `--help`) when a command has subcommands
- Fixed Windows compatibility issues in tests

## Other

- Added optional anonymous usage statistics to help understand how OpenSpec is used. This is **opt-out** by default – set `OPENSPEC_TELEMETRY=0` or `DO_NOT_TRACK=1` to disable. Only command names and version are collected; no arguments, file paths, or content. Automatically disabled in CI environments.
