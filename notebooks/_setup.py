"""Path bootstrap for lab notebooks.

Resolves the repo root (where `app/`, `scripts/`, `data/` live) regardless of
where Jupyter was launched from. Used by all 4 notebooks:

    import _setup  # noqa: F401   -- adds repo root to sys.path

In plain `.py` imports, ``__file__`` pins `notebooks/_setup.py` → parent.parent.
In Jupyter (``.ipynb``), ``__file__`` may be missing — we walk up from ``cwd``
until we find ``app/`` + ``data/`` or ``scripts/``.
"""
from __future__ import annotations

import sys
from pathlib import Path


def _find_repo_root() -> Path:
    try:
        here = Path(__file__).resolve()
        cand = here.parent.parent
        if (cand / "app").is_dir():
            return cand
    except NameError:
        pass
    start = Path.cwd().resolve()
    for p in (start, *start.parents):
        if (p / "app").is_dir() and ((p / "data").is_dir() or (p / "scripts").is_dir()):
            return p
    return start


_REPO_ROOT = _find_repo_root()
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))
