# Research: Repo Release Stubs

## Decisions

### Decision: Reachability check method
- **Chosen**: HTTP check of the GitHub repository page URL
- **Definition of reachable**: 200 OK, or 301/302 redirect chain ending in 200 OK
- **Timeout**: short timeout per URL (exact value determined during implementation)
- **Rationale**: Avoids API keys/tokens, works for public repos, and is fast enough for a repo list.
- **Alternatives considered**:
  - GitHub REST API lookup (subject to rate limits; token handling adds complexity)
  - No network check (would generate stubs for invalid/unreachable repos)

### Decision: Fetch release notes source
- **Chosen**: GitHub Releases REST API (unauthenticated)
- **Endpoint**: `https://api.github.com/repos/<owner>/<repo>/releases`
- **Included releases**: Published only (exclude `draft=true` and `prerelease=true`)
- **Default limit**: 10 most recent published releases
- **Rationale**: Stable structured data, preserves markdown bodies, avoids HTML parsing, and keeps dependencies in the standard library.

### Decision: URL normalization
- **Chosen**: Normalize GitHub HTTPS variants
- **Rules**:
  - Strip trailing `/`
  - Strip optional `.git` suffix
  - Canonical form: `https://github.com/<owner>/<repo>`
- **Rationale**: Handles common copy/paste variants while keeping scope focused.

### Decision: Handling duplicates
- **Chosen**: Ignore duplicates
- **How**: De-duplicate by normalized repo URL before processing
- **Rationale**: Deterministic output and avoids redundant network calls.

### Decision: Existing output stubs
- **Chosen**: Overwrite existing `data/releases/<repo>.md`
- **Rationale**: Supports "regenerate clean stubs" workflow.

### Decision: Stub content
- **Chosen**: Completely empty markdown file (0 bytes)
- **Rationale**: Unambiguous interpretation of "blank".

### Decision: Technology stack
- **Chosen**: Python 3.14+
- **Testing**: pytest with BDD-style Given/When/Then structure
- **Rationale**: Aligns with project direction and keeps implementation/test ergonomics strong.

## Notes / Implementation Guidance (non-normative)

- Prefer standard library HTTP (`urllib.request`) unless requirements change.
- Use a small, well-scoped user agent and follow redirects.
- Keep filesystem writes allowlisted to `data/releases/`.
