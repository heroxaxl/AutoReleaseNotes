from __future__ import annotations

import sys
from dataclasses import dataclass
import json
from datetime import datetime
from pathlib import Path
from typing import Iterable

import urllib.request as urllib_request
from urllib.error import HTTPError, URLError


DEFAULT_TIMEOUT_SECONDS = 5
DEFAULT_RELEASE_LIMIT = 10


@dataclass(frozen=True)
class RepoRef:
    raw_url: str
    normalized_url: str
    owner: str
    repo_name: str


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def read_repo_urls(repos_file: Path) -> list[str]:
    if not repos_file.exists():
        raise FileNotFoundError(f"Missing repo list: {repos_file}")

    urls: list[str] = []
    for line in repos_file.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s:
            continue
        urls.append(s)
    return urls


def warn(msg: str) -> None:
    print(msg, file=sys.stderr)


def normalize_github_https_url(url: str) -> str:
    s = url.strip()
    while s.endswith("/"):
        s = s[:-1]
    if s.endswith(".git"):
        s = s[: -len(".git")]
    return s


def parse_repo_ref(url: str) -> RepoRef | None:
    from urllib.parse import urlparse

    normalized = normalize_github_https_url(url)
    parsed = urlparse(normalized)

    if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
        return None

    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2:
        return None

    owner, repo = parts[0], parts[1]
    return RepoRef(raw_url=url, normalized_url=normalized, owner=owner, repo_name=repo)


def dedupe_by_normalized_url(urls: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for u in urls:
        nu = normalize_github_https_url(u)
        if nu in seen:
            continue
        seen.add(nu)
        result.append(u)
    return result


def ensure_output_dir(root: Path) -> Path:
    out_dir = root / "data" / "releases"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def ensure_allowlisted_output(path: Path, out_dir: Path) -> None:
    try:
        path.resolve().relative_to(out_dir.resolve())
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"Refusing to write outside allowlisted dir: {out_dir}") from exc


def is_repo_reachable(repo_url: str, timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS) -> bool:
    req = urllib_request.Request(
        repo_url,
        headers={"User-Agent": "AutoReleaseNotes-RepoStubber/1.0"},
        method="GET",
    )

    try:
        with urllib_request.urlopen(req, timeout=timeout_seconds) as resp:
            code = getattr(resp, "status", None) or resp.getcode()
            return int(code) == 200
    except HTTPError:
        return False
    except URLError:
        return False


def is_repo_reachable_with_releases_fallback(
    repo_url: str, timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS
) -> bool:
    if is_repo_reachable(repo_url, timeout_seconds=timeout_seconds):
        return True

    releases_url = f"{repo_url}/releases"
    return is_repo_reachable(releases_url, timeout_seconds=timeout_seconds)


def github_releases_api_url(owner: str, repo_name: str) -> str:
    return f"https://api.github.com/repos/{owner}/{repo_name}/releases"


def fetch_github_releases(
    owner: str,
    repo_name: str,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> list[dict] | None:
    api_url = github_releases_api_url(owner, repo_name)
    req = urllib_request.Request(
        api_url,
        headers={
            "User-Agent": "AutoReleaseNotes-RepoStubber/1.0",
            "Accept": "application/vnd.github+json",
        },
        method="GET",
    )

    try:
        with urllib_request.urlopen(req, timeout=timeout_seconds) as resp:
            code = getattr(resp, "status", None) or resp.getcode()
            if int(code) != 200:
                warn(f"GitHub API non-200 for {owner}/{repo_name}: {code}")
                return None
            raw = resp.read()
    except HTTPError as exc:
        warn(f"GitHub API HTTPError for {owner}/{repo_name}: {getattr(exc, 'code', 'unknown')}")
        return None
    except URLError:
        warn(f"GitHub API URLError for {owner}/{repo_name}")
        return None

    try:
        data = json.loads(raw.decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        warn(f"GitHub API invalid JSON for {owner}/{repo_name}: {exc}")
        return None

    if not isinstance(data, list):
        warn(f"GitHub API unexpected payload for {owner}/{repo_name}")
        return None

    return data


def published_only(releases: list[dict]) -> list[dict]:
    result: list[dict] = []
    for r in releases:
        if r.get("draft") is True:
            continue
        if r.get("prerelease") is True:
            continue
        result.append(r)
    return result


def limit_releases(releases: list[dict], limit: int = DEFAULT_RELEASE_LIMIT) -> list[dict]:
    if limit < 0:
        return releases
    return releases[:limit]


def _fmt_date(s: str | None) -> str:
    if not s:
        return ""
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return dt.date().isoformat()
    except Exception:  # noqa: BLE001
        return s


def render_releases_markdown(ref: RepoRef, releases: list[dict]) -> str:
    if not releases:
        return f"# {ref.owner}/{ref.repo_name}\n\nNo published releases found.\n"

    lines: list[str] = [f"# {ref.owner}/{ref.repo_name}", ""]

    for r in releases:
        name = r.get("name") or ""
        tag = r.get("tag_name") or ""
        published_at = _fmt_date(r.get("published_at"))
        body = r.get("body") or ""
        html_url = r.get("html_url") or ""

        title = name if name else (tag if tag else "Release")
        lines.append(f"## {title}")
        if tag:
            lines.append(f"- Tag: `{tag}`")
        if published_at:
            lines.append(f"- Published: {published_at}")
        if html_url:
            lines.append(f"- URL: {html_url}")
        lines.append("")
        if body:
            lines.append(body.rstrip())
        else:
            lines.append("(No release notes body.)")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_repo_markdown(out_dir: Path, repo_name: str, content: str) -> Path:
    out_path = out_dir / f"{repo_name}.md"
    ensure_allowlisted_output(out_path, out_dir)
    out_path.write_text(content, encoding="utf-8")
    return out_path


def generate_release_stubs(root: Path) -> list[Path]:
    repos_file = root / "data" / "repo" / "repos.txt"
    urls = read_repo_urls(repos_file)
    urls = dedupe_by_normalized_url(urls)

    out_dir = ensure_output_dir(root)

    written: list[Path] = []
    for raw in urls:
        ref = parse_repo_ref(raw)
        if ref is None:
            warn(f"Skipping unsupported URL: {raw}")
            continue

        if not is_repo_reachable_with_releases_fallback(
            ref.normalized_url, timeout_seconds=DEFAULT_TIMEOUT_SECONDS
        ):
            warn(f"Unreachable repo (also tried /releases): {ref.normalized_url}")
            continue

        api_releases = fetch_github_releases(
            ref.owner, ref.repo_name, timeout_seconds=DEFAULT_TIMEOUT_SECONDS
        )
        if api_releases is None:
            warn(f"Skipping repo due to GitHub API error: {ref.owner}/{ref.repo_name}")
            continue

        releases = limit_releases(published_only(api_releases), DEFAULT_RELEASE_LIMIT)
        content = render_releases_markdown(ref, releases)
        written.append(write_repo_markdown(out_dir, ref.repo_name, content))

    return written


def main(argv: list[str]) -> int:
    _ = argv
    try:
        written = generate_release_stubs(repo_root())
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    for p in written:
        print(f"Wrote: {p}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
