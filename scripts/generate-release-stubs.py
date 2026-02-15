#!/usr/bin/env python3
from __future__ import annotations

import sys

from pathlib import Path


_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT))

from scripts.generate_release_stubs import main


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
