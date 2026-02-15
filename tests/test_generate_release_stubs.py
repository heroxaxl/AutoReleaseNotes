from __future__ import annotations

from pathlib import Path
from urllib.error import HTTPError, URLError
from unittest.mock import Mock

import pytest

import scripts.generate_release_stubs as gen


def _make_repo(tmp_path: Path, urls: list[str]) -> Path:
    (tmp_path / "data" / "repo").mkdir(parents=True, exist_ok=True)
    (tmp_path / "data" / "releases").mkdir(parents=True, exist_ok=True)
    (tmp_path / "data" / "repo" / "repos.txt").write_text("\n".join(urls) + "\n", encoding="utf-8")
    return tmp_path


def test_us1_given_mixed_repos_when_run_then_only_reachable_written(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # Given
    repo = _make_repo(
        tmp_path,
        [
            "https://github.com/org/reachable",
            "https://github.com/org/unreachable",
            "   ",
        ],
    )

    def fake_is_reachable(url: str, timeout_seconds: int = gen.DEFAULT_TIMEOUT_SECONDS) -> bool:
        return url.endswith("/reachable")

    monkeypatch.setattr(gen, "is_repo_reachable", fake_is_reachable)
    monkeypatch.setattr(
        gen,
        "fetch_github_releases",
        lambda owner, repo_name, timeout_seconds=gen.DEFAULT_TIMEOUT_SECONDS: [
            {
                "draft": False,
                "prerelease": False,
                "name": "v1.0.0",
                "tag_name": "v1.0.0",
                "published_at": "2026-02-15T00:00:00Z",
                "body": "Hello",
                "html_url": f"https://github.com/{owner}/{repo_name}/releases/tag/v1.0.0",
            }
        ],
    )

    # When
    written = gen.generate_release_stubs(repo)

    # Then
    assert (repo / "data" / "releases" / "reachable.md").exists()
    assert not (repo / "data" / "releases" / "unreachable.md").exists()
    assert written == [repo / "data" / "releases" / "reachable.md"]
    content = (repo / "data" / "releases" / "reachable.md").read_text(encoding="utf-8")
    assert "# org/reachable" in content
    assert "## v1.0.0" in content


def test_us1_given_repo_unreachable_when_releases_page_reachable_then_writes_stub(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given
    repo = _make_repo(tmp_path, ["https://github.com/org/repo"])  # noqa: S106

    def fake_is_reachable(url: str, timeout_seconds: int = gen.DEFAULT_TIMEOUT_SECONDS) -> bool:
        return url.endswith("/releases")

    monkeypatch.setattr(gen, "is_repo_reachable", fake_is_reachable)
    monkeypatch.setattr(
        gen,
        "fetch_github_releases",
        lambda owner, repo_name, timeout_seconds=gen.DEFAULT_TIMEOUT_SECONDS: [],
    )

    # When
    written = gen.generate_release_stubs(repo)

    # Then
    assert written == [repo / "data" / "releases" / "repo.md"]
    assert (repo / "data" / "releases" / "repo.md").exists()


def test_us1_given_repo_page_reachable_then_does_not_require_releases_fallback(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given
    repo = _make_repo(tmp_path, ["https://github.com/org/repo"])  # noqa: S106
    calls: list[str] = []

    def fake_is_reachable(url: str, timeout_seconds: int = gen.DEFAULT_TIMEOUT_SECONDS) -> bool:
        calls.append(url)
        return True

    monkeypatch.setattr(gen, "is_repo_reachable", fake_is_reachable)
    monkeypatch.setattr(
        gen,
        "fetch_github_releases",
        lambda owner, repo_name, timeout_seconds=gen.DEFAULT_TIMEOUT_SECONDS: [],
    )

    # When
    written = gen.generate_release_stubs(repo)

    # Then
    assert written == [repo / "data" / "releases" / "repo.md"]
    assert calls == ["https://github.com/org/repo"]


def test_us2_given_standard_github_url_when_processed_then_filename_is_repo_name(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # Given
    repo = _make_repo(tmp_path, ["https://github.com/org/repo"])  # noqa: S106

    monkeypatch.setattr(gen, "is_repo_reachable", lambda *_args, **_kwargs: True)
    monkeypatch.setattr(
        gen,
        "fetch_github_releases",
        lambda owner, repo_name, timeout_seconds=gen.DEFAULT_TIMEOUT_SECONDS: [
            {
                "draft": False,
                "prerelease": False,
                "name": "v1.0.0",
                "tag_name": "v1.0.0",
                "published_at": "2026-02-15T00:00:00Z",
                "body": "Hello",
                "html_url": f"https://github.com/{owner}/{repo_name}/releases/tag/v1.0.0",
            }
        ],
    )

    # When
    written = gen.generate_release_stubs(repo)

    # Then
    assert written == [repo / "data" / "releases" / "repo.md"]
    assert (repo / "data" / "releases" / "repo.md").exists()


def test_us2_given_url_variants_when_processed_then_normalizes_and_names_consistently(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given
    repo = _make_repo(
        tmp_path,
        [
            "https://github.com/org/repo/",
            "https://github.com/org/repo.git",
            "https://github.com/org/repo/",
        ],
    )

    monkeypatch.setattr(gen, "is_repo_reachable", lambda *_args, **_kwargs: True)
    monkeypatch.setattr(
        gen,
        "fetch_github_releases",
        lambda owner, repo_name, timeout_seconds=gen.DEFAULT_TIMEOUT_SECONDS: [],
    )

    # When
    written = gen.generate_release_stubs(repo)

    # Then
    assert written == [repo / "data" / "releases" / "repo.md"]
    assert (repo / "data" / "releases" / "repo.md").exists()


def test_us3_given_existing_stub_with_content_when_run_then_overwrites_to_empty(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given
    repo = _make_repo(tmp_path, ["https://github.com/org/repo"])  # noqa: S106
    target = repo / "data" / "releases" / "repo.md"
    target.write_text("not empty", encoding="utf-8")

    monkeypatch.setattr(gen, "is_repo_reachable", lambda *_args, **_kwargs: True)
    monkeypatch.setattr(
        gen,
        "fetch_github_releases",
        lambda owner, repo_name, timeout_seconds=gen.DEFAULT_TIMEOUT_SECONDS: [],
    )

    # When
    written = gen.generate_release_stubs(repo)

    # Then
    assert written == [target]
    assert target.exists()
    assert "No published releases found" in target.read_text(encoding="utf-8")


def test_us4_given_api_returns_two_published_releases_when_run_then_markdown_contains_titles_and_bodies(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given
    repo = _make_repo(tmp_path, ["https://github.com/org/repo"])  # noqa: S106
    monkeypatch.setattr(gen, "is_repo_reachable", lambda *_args, **_kwargs: True)

    monkeypatch.setattr(
        gen,
        "fetch_github_releases",
        lambda owner, repo_name, timeout_seconds=gen.DEFAULT_TIMEOUT_SECONDS: [
            {
                "draft": False,
                "prerelease": False,
                "name": "v2.0.0",
                "tag_name": "v2.0.0",
                "published_at": "2026-02-15T00:00:00Z",
                "body": "Body 2",
                "html_url": f"https://github.com/{owner}/{repo_name}/releases/tag/v2.0.0",
            },
            {
                "draft": False,
                "prerelease": False,
                "name": "v1.0.0",
                "tag_name": "v1.0.0",
                "published_at": "2026-02-14T00:00:00Z",
                "body": "Body 1",
                "html_url": f"https://github.com/{owner}/{repo_name}/releases/tag/v1.0.0",
            },
        ],
    )

    # When
    written = gen.generate_release_stubs(repo)

    # Then
    assert written == [repo / "data" / "releases" / "repo.md"]
    content = (repo / "data" / "releases" / "repo.md").read_text(encoding="utf-8")
    assert "## v2.0.0" in content
    assert "Body 2" in content
    assert "## v1.0.0" in content
    assert "Body 1" in content


def test_us4_given_api_returns_only_drafts_or_prereleases_when_run_then_no_releases_message(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given
    repo = _make_repo(tmp_path, ["https://github.com/org/repo"])  # noqa: S106
    monkeypatch.setattr(gen, "is_repo_reachable", lambda *_args, **_kwargs: True)

    monkeypatch.setattr(
        gen,
        "fetch_github_releases",
        lambda *_args, **_kwargs: [
            {"draft": True, "prerelease": False, "name": "draft"},
            {"draft": False, "prerelease": True, "name": "pre"},
        ],
    )

    # When
    written = gen.generate_release_stubs(repo)

    # Then
    assert written == [repo / "data" / "releases" / "repo.md"]
    content = (repo / "data" / "releases" / "repo.md").read_text(encoding="utf-8")
    assert "No published releases found" in content


def test_us4_given_api_error_for_one_repo_when_run_then_skips_that_repo_and_continues(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given
    repo = _make_repo(
        tmp_path,
        [
            "https://github.com/org/bad",
            "https://github.com/org/good",
        ],
    )
    monkeypatch.setattr(gen, "is_repo_reachable", lambda *_args, **_kwargs: True)

    def fake_fetch(owner: str, repo_name: str, timeout_seconds: int = gen.DEFAULT_TIMEOUT_SECONDS):
        if repo_name == "bad":
            return None
        return [
            {
                "draft": False,
                "prerelease": False,
                "name": "v1.0.0",
                "tag_name": "v1.0.0",
                "published_at": "2026-02-15T00:00:00Z",
                "body": "Hello",
                "html_url": f"https://github.com/{owner}/{repo_name}/releases/tag/v1.0.0",
            }
        ]

    monkeypatch.setattr(gen, "fetch_github_releases", fake_fetch)

    # When
    written = gen.generate_release_stubs(repo)

    # Then
    assert written == [repo / "data" / "releases" / "good.md"]
    assert not (repo / "data" / "releases" / "bad.md").exists()


def test_us1_http_reachability_with_stdlib_mocking(monkeypatch: pytest.MonkeyPatch) -> None:
    # Given
    url = "https://github.com/org/repo"

    response = Mock()
    response.__enter__ = Mock(return_value=response)
    response.__exit__ = Mock(return_value=None)
    response.status = 200
    response.getcode = Mock(return_value=200)

    monkeypatch.setattr(gen.urllib_request, "urlopen", Mock(return_value=response))

    # When
    reachable = gen.is_repo_reachable(url, timeout_seconds=1)

    # Then
    assert reachable is True


@pytest.mark.parametrize(
    "exc",
    [
        HTTPError(url="https://github.com/org/repo", code=404, msg="Not Found", hdrs=None, fp=None),
        URLError("timed out"),
    ],
)
def test_us1_http_reachability_errors_return_false(monkeypatch: pytest.MonkeyPatch, exc: Exception) -> None:
    # Given
    url = "https://github.com/org/repo"

    def raise_exc(*_args, **_kwargs):  # type: ignore[no-untyped-def]
        raise exc

    monkeypatch.setattr(gen.urllib_request, "urlopen", raise_exc)

    # When / Then
    assert gen.is_repo_reachable(url, timeout_seconds=1) is False
