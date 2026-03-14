"""Path helpers for the repository."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
DOCS_DIR = REPO_ROOT / "docs"
FIGURES_DIR = REPO_ROOT / "figures"
REPORTS_DIR = REPO_ROOT / "reports"
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"


def ensure_repo_dirs() -> None:
    """Create commonly used project directories if they do not exist."""
    for directory in (RAW_DATA_DIR, PROCESSED_DATA_DIR, FIGURES_DIR, REPORTS_DIR):
        directory.mkdir(parents=True, exist_ok=True)
