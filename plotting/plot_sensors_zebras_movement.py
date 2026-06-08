#!/usr/bin/env python3
"""Plot moving sensor and zebra trajectories on the same 2D chart."""

from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path("charts/.matplotlib").resolve()))
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.collections import LineCollection
from matplotlib.colors import to_rgba
from matplotlib.lines import Line2D


DEFAULT_ZEBRA_FILES = [
    Path("src/main/resources/zebras-trajectories/flights/flight_1_zebras/zebra_035.csv"),
    Path("src/main/resources/zebras-trajectories/flights/flight_1_zebras/zebra_037.csv"),
    Path("src/main/resources/zebras-trajectories/flights/flight_1_zebras/zebra_038.csv"),
]


@dataclass(frozen=True)
class Trajectory:
    label: str
    x: np.ndarray
    y: np.ndarray


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Load moving sensor position CSVs and selected zebra CSVs, then plot "
            "their 2D trajectories with one color per entity group."
        )
    )
    parser.add_argument(
        "--sensors-dir",
        type=Path,
        default=Path("data/movingSensorsNB-withpos"),
        help="Directory containing positions_node-* CSV files.",
    )
    parser.add_argument(
        "--sensor-glob",
        default="positions_node-*_node-*_errorOnPosition.csv",
        help="Glob used inside --sensors-dir to select sensor position CSVs.",
    )
    parser.add_argument(
        "--zebra-files",
        type=Path,
        nargs="*",
        default=DEFAULT_ZEBRA_FILES,
        help="Zebra trajectory CSV files to plot.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("charts/movingSensorsNB-withpos/sensors_zebras_movement.png"),
        help="Output chart path. The extension selects the saved image format.",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=10.0,
        help="Divide coordinates by this value before plotting. Use 1 for raw data.",
    )
    parser.add_argument("--dpi", type=int, default=220, help="Output image DPI.")
    parser.add_argument("--title", default="")
    return parser.parse_args()


def require_columns(frame: pd.DataFrame, columns: tuple[str, str], path: Path) -> None:
    missing = [column for column in columns if column not in frame.columns]
    if missing:
        raise ValueError(f"{path}: missing required columns: {', '.join(missing)}")


def read_trajectory(path: Path, x_column: str, y_column: str, scale: float) -> Trajectory:
    frame = pd.read_csv(path)
    require_columns(frame, (x_column, y_column), path)
    frame = frame[[x_column, y_column]].apply(pd.to_numeric, errors="coerce").dropna()
    if frame.empty:
        raise ValueError(f"{path}: no valid coordinate rows found")

    return Trajectory(
        label=path.stem,
        x=frame[x_column].to_numpy(dtype=float) / scale,
        y=frame[y_column].to_numpy(dtype=float) / scale,
    )


def sensor_sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"positions_node-(\d+)_", path.name)
    if match:
        return int(match.group(1)), path.name
    return 10**9, path.name


def load_sensor_trajectories(sensors_dir: Path, sensor_glob: str, scale: float) -> list[Trajectory]:
    files = sorted(sensors_dir.glob(sensor_glob), key=sensor_sort_key)
    if not files:
        raise FileNotFoundError(f"No sensor position CSV files found in {sensors_dir}")
    return [read_trajectory(path, "estimatedX", "estimatedY", scale) for path in files]


def load_zebra_trajectories(zebra_files: list[Path], scale: float) -> list[Trajectory]:
    missing = [path for path in zebra_files if not path.exists()]
    if missing:
        missing_paths = "\n".join(str(path) for path in missing)
        raise FileNotFoundError(f"Missing zebra CSV files:\n{missing_paths}")
    return [read_trajectory(path, "x", "y", scale) for path in zebra_files]


def add_fading_line(
    ax: plt.Axes,
    trajectory: Trajectory,
    color: str,
    linewidth: float,
    min_alpha: float,
    max_alpha: float,
) -> None:
    points = np.column_stack([trajectory.x, trajectory.y])
    if len(points) < 2:
        ax.scatter(trajectory.x, trajectory.y, color=color, s=90, zorder=4)
        return

    segments = np.stack([points[:-1], points[1:]], axis=1)
    rgba = np.tile(to_rgba(color), (len(segments), 1))
    rgba[:, 3] = np.linspace(min_alpha, max_alpha, len(segments))
    ax.add_collection(LineCollection(segments, colors=rgba, linewidths=linewidth, zorder=1))


def plot_group(
    ax: plt.Axes,
    trajectories: list[Trajectory],
    color: str,
    linewidth: float,
    min_alpha: float,
    max_alpha: float,
    point_size: float,
) -> None:
    for trajectory in trajectories:
        add_fading_line(ax, trajectory, color, linewidth, min_alpha, max_alpha)
        ax.scatter(
            trajectory.x[-1],
            trajectory.y[-1],
            s=120,
            color=color,
            alpha=0.95,
            edgecolors="#3a3a3a",
            linewidths=0.7,
            zorder=4,
        )


def set_limits(ax: plt.Axes, trajectories: list[Trajectory]) -> None:
    x_values = np.concatenate([trajectory.x for trajectory in trajectories])
    y_values = np.concatenate([trajectory.y for trajectory in trajectories])
    x_min, x_max = float(x_values.min()), float(x_values.max())
    y_min, y_max = float(y_values.min()), float(y_values.max())
    x_pad = max((x_max - x_min) * 0.05, 0.5)
    y_pad = max((y_max - y_min) * 0.05, 0.5)
    ax.set_xlim(x_min - x_pad, x_max + x_pad)
    ax.set_ylim(y_min - y_pad, y_max + y_pad)


def make_chart(
    sensors: list[Trajectory],
    zebras: list[Trajectory],
    output: Path,
    dpi: int,
    title: str,
) -> None:
    sensor_color = "#1f77b4"
    zebra_color = "#d6278b"

    fig, ax = plt.subplots(figsize=(12, 8), constrained_layout=True)
    plot_group(
        ax,
        sensors,
        sensor_color,
        linewidth=1.8,
        min_alpha=0.04,
        max_alpha=0.24,
        point_size=78,
    )
    plot_group(
        ax,
        zebras,
        zebra_color,
        linewidth=2.6,
        min_alpha=0.08,
        max_alpha=0.34,
        point_size=96,
    )

    set_limits(ax, sensors + zebras)
    if title:
        ax.set_title(title, fontsize=18, pad=12)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    ax.set_aspect("equal", adjustable="box")

    legend_handles = [
        Line2D([0], [0], color=sensor_color, lw=3, marker="o", markersize=9, label="Moving sensors"),
        Line2D([0], [0], color=zebra_color, lw=3, marker="o", markersize=9, label="Zebras"),
    ]
    ax.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.04),
        ncol=2,
        frameon=True,
        fontsize=22,
    )

    for spine in plt.gca().spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(2)

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    args = parse_args()
    if args.scale == 0:
        raise SystemExit("--scale cannot be 0")

    sensors = load_sensor_trajectories(args.sensors_dir, args.sensor_glob, args.scale)
    zebras = load_zebra_trajectories(args.zebra_files, args.scale)
    make_chart(sensors, zebras, args.output, args.dpi, args.title)

    print(f"Loaded {len(sensors)} sensor trajectories and {len(zebras)} zebra trajectories.")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
