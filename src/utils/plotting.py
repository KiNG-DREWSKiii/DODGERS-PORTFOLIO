"""Shared plotting helpers built on matplotlib."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def apply_base_style() -> None:
    """Apply a simple, readable default plotting style."""
    plt.style.use("default")
    plt.rcParams.update(
        {
            "figure.figsize": (8, 6),
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "font.size": 11,
        }
    )


def save_figure(path: str | Path, dpi: int = 150) -> None:
    """Save the active figure and close it."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close()
