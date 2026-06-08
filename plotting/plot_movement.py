#!/usr/bin/env python3
"""Plot experiment movement for devices, targets, and obstacles."""

from __future__ import annotations

import argparse
import csv
import os
import re
from dataclasses import dataclass
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path("charts/.matplotlib").resolve()))
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
os.environ.setdefault("XDG_CACHE_HOME", str(Path("charts/.cache").resolve()))
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import to_rgba
from matplotlib.lines import Line2D
from matplotlib.patches import Circle


DEVICE_COLORS = ["#1f77b4", "#007f5f", "#d62728", "#6f4eb5", "#ff7f0e", "#17becf"]
TARGET_COLOR = "#2ca02c"
OBSTACLE_COLOR = "#d62728"
OBSTACLE_MARGIN_COLOR = "#f2cf3a"
COMM_COLOR = "#b8b8b8"
SAFE_COLOR = "#666666"
ALCHEMIST_ROBOT_MARGIN_RADIUS_FACTOR = 0.5


@dataclass(frozen=True)
class ExperimentConfig:
    data_dir: Path
    title: str


@dataclass(frozen=True)
class Trajectory:
    entity_id: int
    label: str
    time: np.ndarray
    x: np.ndarray
    y: np.ndarray
    safe_margin: np.ndarray
    comm_distance: np.ndarray
    radius: np.ndarray
    margin: np.ndarray

    @property
    def final_x(self) -> float:
        return float(self.x[-1])

    @property
    def final_y(self) -> float:
        return float(self.y[-1])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Plot full experiment movement. It writes one clean trajectory image and one "
            "sampled margin-evolution image."
        )
    )
    parser.add_argument("--config", type=Path, default=None, help="Experiment YAML, used to infer dataPath.")
    parser.add_argument("--data-dir", type=Path, default=None, help="Directory containing exported CSV files.")
    parser.add_argument("--output-dir", type=Path, default=Path("charts/movement"), help="Output directory.")
    parser.add_argument("--output-prefix", default=None, help="Filename prefix. Defaults to the data directory name.")
    parser.add_argument("--title", default=None, help="Plot title. Defaults to YAML stem or data directory name.")
    parser.add_argument("--max-points", type=int, default=2500, help="Maximum points per trajectory after downsampling.")
    parser.add_argument(
        "--margin-samples",
        type=int,
        default=12,
        help="Number of temporal rings per moving entity in the margin-evolution image.",
    )
    parser.add_argument("--dpi", type=int, default=220, help="Output image DPI.")
    return parser.parse_args()


def parse_config(path: Path | None, data_dir_override: Path | None, title_override: str | None) -> ExperimentConfig:
    data_dir = data_dir_override
    title = title_override
    if path:
        text = path.read_text(encoding="utf-8")
        data_path = re.search(r'^\s{2}dataPath:\s*&dataPath\s+"?([^"\n#]+)"?', text, re.MULTILINE)
        if data_dir is None and data_path:
            data_dir = Path(data_path.group(1).strip())
        if title is None:
            title = path.stem
    if data_dir is None:
        raise ValueError("Pass --config or --data-dir.")
    if title is None:
        title = data_dir.name
    return ExperimentConfig(data_dir=data_dir, title=title)


def parse_id(path: Path) -> int:
    match = re.search(r"-(\d+)", path.name)
    if not match:
        raise ValueError(f"Cannot parse id from {path}")
    return int(match.group(1))


def sort_key(path: Path) -> tuple[str, int]:
    return re.sub(r"-\d+$", "-", path.stem), parse_id(path)


def downsample_rows(rows: list[dict[str, float]], max_points: int) -> list[dict[str, float]]:
    if max_points <= 0 or len(rows) <= max_points:
        return rows
    indexes = np.linspace(0, len(rows) - 1, max_points, dtype=int)
    return [rows[index] for index in np.unique(indexes)]


def numeric_rows(path: Path) -> list[dict[str, float]]:
    rows = []
    with path.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            parsed = {}
            for column, value in row.items():
                try:
                    parsed[column] = float(value)
                except (TypeError, ValueError):
                    parsed[column] = float("nan")
            # Always round the 'time' column to integer ticks for plotting.
            if not np.isnan(parsed.get("time", float("nan"))):
                parsed["time"] = float(round(parsed["time"]))
            if not np.isnan(parsed.get("time", float("nan"))):
                rows.append(parsed)
    return rows


def column(rows: list[dict[str, float]], name: str, default: float = 0.0) -> np.ndarray:
    return np.array([row.get(name, default) for row in rows], dtype=float)


def read_devices(data_dir: Path, max_points: int) -> list[Trajectory]:
    trajectories = []
    for path in sorted(data_dir.glob("positions_node-*.csv"), key=sort_key):
        rows = downsample_rows(numeric_rows(path), max_points)
        if not rows:
            continue
        device_id = int(rows[0].get("nodeId", parse_id(path)))
        trajectories.append(
            Trajectory(
                entity_id=device_id,
                label=f"Device {device_id}",
                time=column(rows, "time"),
                x=column(rows, "X"),
                y=column(rows, "Y"),
                safe_margin=column(rows, "safeMargin"),
                comm_distance=column(rows, "commDistance"),
                radius=np.zeros(len(rows), dtype=float),
                margin=np.zeros(len(rows), dtype=float),
            )
        )
    if not trajectories:
        raise FileNotFoundError(f"No positions_node-*.csv files found in {data_dir}")
    return trajectories


def read_targets(data_dir: Path, max_points: int) -> list[Trajectory]:
    trajectories = []
    for path in sorted(data_dir.glob("target-*.csv"), key=sort_key):
        rows = downsample_rows(numeric_rows(path), max_points)
        if not rows:
            continue
        target_id = int(rows[0].get("id", parse_id(path)))
        trajectories.append(
            Trajectory(
                entity_id=target_id,
                label=f"Target {target_id}",
                time=column(rows, "time"),
                x=column(rows, "x"),
                y=column(rows, "y"),
                safe_margin=np.zeros(len(rows), dtype=float),
                comm_distance=np.zeros(len(rows), dtype=float),
                radius=np.zeros(len(rows), dtype=float),
                margin=np.zeros(len(rows), dtype=float),
            )
        )
    return trajectories


def read_obstacles(data_dir: Path, max_points: int) -> list[Trajectory]:
    trajectories = []
    for path in sorted(data_dir.glob("obstacle-*.csv"), key=sort_key):
        rows = downsample_rows(numeric_rows(path), max_points)
        if not rows:
            continue
        obstacle_id = int(rows[0].get("id", parse_id(path)))
        trajectories.append(
            Trajectory(
                entity_id=obstacle_id,
                label=f"Obstacle {obstacle_id}",
                time=column(rows, "time"),
                x=column(rows, "x"),
                y=column(rows, "y"),
                safe_margin=np.zeros(len(rows), dtype=float),
                comm_distance=np.zeros(len(rows), dtype=float),
                radius=column(rows, "radius"),
                margin=column(rows, "margin"),
            )
        )
    return trajectories


def add_fading_line(
    ax: plt.Axes,
    x: np.ndarray,
    y: np.ndarray,
    color: str,
    linewidth: float,
    min_alpha: float,
    max_alpha: float,
    linestyle: str = "solid",
    zorder: int = 2,
) -> None:
    points = np.column_stack([x, y])
    if len(points) < 2:
        ax.scatter(x, y, color=color, s=80, zorder=zorder + 1)
        return
    segments = np.stack([points[:-1], points[1:]], axis=1)
    rgba = np.tile(to_rgba(color), (len(segments), 1))
    progress = np.linspace(0.0, 1.0, len(segments))
    rgba[:, 3] = min_alpha + (progress**1.8) * (max_alpha - min_alpha)
    ax.add_collection(LineCollection(segments, colors=rgba, linewidths=linewidth, linestyles=linestyle, zorder=zorder))


def add_circle(ax: plt.Axes, x: float, y: float, radius: float, color: str, alpha: float, zorder: int) -> None:
    if radius > 0:
        ax.add_patch(Circle((x, y), radius, color=color, alpha=alpha, linewidth=0, zorder=zorder))


def robot_margin_radius(safe_margin: float) -> float:
    return safe_margin * ALCHEMIST_ROBOT_MARGIN_RADIUS_FACTOR


def sampled_indexes(length: int, samples: int) -> np.ndarray:
    if length == 0 or samples <= 0:
        return np.array([], dtype=int)
    return np.unique(np.linspace(0, length - 1, min(length, samples), dtype=int))


def draw_clean_movement(
    devices: list[Trajectory],
    targets: list[Trajectory],
    obstacles: list[Trajectory],
    output: Path,
    dpi: int,
    title: str,
) -> None:
    fig, ax = plt.subplots(figsize=(12, 8), constrained_layout=True)

    for index, device in enumerate(devices):
        color = DEVICE_COLORS[index % len(DEVICE_COLORS)]
        add_fading_line(ax, device.x, device.y, color, linewidth=2.0, min_alpha=0.015, max_alpha=0.82)
        add_circle(ax, device.final_x, device.final_y, robot_margin_radius(float(device.safe_margin[-1])), SAFE_COLOR, 0.22, 4)
        ax.scatter(device.final_x, device.final_y, s=95, color=color, edgecolors="black", linewidths=0.8, zorder=6)
        ax.text(device.final_x, device.final_y, str(device.entity_id), ha="center", va="center", fontsize=8, color="white", zorder=7)

    for target in targets:
        add_fading_line(ax, target.x, target.y, TARGET_COLOR, linewidth=2.2, min_alpha=0.02, max_alpha=0.48, linestyle="dashed", zorder=1)
        ax.scatter(target.final_x, target.final_y, marker="*", s=260, color=TARGET_COLOR, edgecolors="black", linewidths=0.7, zorder=5)
        ax.text(target.final_x, target.final_y + 0.45, f"T{target.entity_id}", ha="center", va="bottom", fontsize=9, color="#1d5d1d")

    draw_final_obstacles(ax, obstacles)
    finish_axes(ax, title, devices, targets, obstacles, legend_handles_clean(devices), output, dpi)


def draw_margin_evolution(
    devices: list[Trajectory],
    targets: list[Trajectory],
    obstacles: list[Trajectory],
    output: Path,
    dpi: int,
    title: str,
    margin_samples: int,
) -> None:
    fig, ax = plt.subplots(figsize=(12, 8), constrained_layout=True)

    for target in targets:
        add_fading_line(ax, target.x, target.y, TARGET_COLOR, linewidth=1.8, min_alpha=0.015, max_alpha=0.32, linestyle="dashed", zorder=1)
        ax.scatter(target.final_x, target.final_y, marker="*", s=220, color=TARGET_COLOR, edgecolors="black", linewidths=0.7, zorder=5)

    for index, device in enumerate(devices):
        color = DEVICE_COLORS[index % len(DEVICE_COLORS)]
        add_fading_line(ax, device.x, device.y, color, linewidth=1.3, min_alpha=0.012, max_alpha=0.52, zorder=2)
        ring_indexes = sampled_indexes(len(device.x), margin_samples)
        for ring_number, point_index in enumerate(ring_indexes):
            progress = ring_number / max(len(ring_indexes) - 1, 1)
            add_circle(
                ax,
                float(device.x[point_index]),
                float(device.y[point_index]),
                robot_margin_radius(float(device.safe_margin[point_index])),
                color,
                alpha=0.08 + 0.14 * progress,
                zorder=3,
            )
        ax.scatter(device.final_x, device.final_y, s=90, color=color, edgecolors="black", linewidths=0.8, zorder=6)
        ax.text(device.final_x, device.final_y, str(device.entity_id), ha="center", va="center", fontsize=8, color="white", zorder=7)

    for obstacle in obstacles:
        add_fading_line(ax, obstacle.x, obstacle.y, OBSTACLE_COLOR, linewidth=1.2, min_alpha=0.012, max_alpha=0.3, zorder=1)
        ring_indexes = sampled_indexes(len(obstacle.x), margin_samples)
        sampled_states = {
            (
                round(float(obstacle.x[point_index]), 6),
                round(float(obstacle.y[point_index]), 6),
                round(float(obstacle.radius[point_index]), 6),
                round(float(obstacle.margin[point_index]), 6),
            )
            for point_index in ring_indexes
        }
        if len(sampled_states) <= 1:
            add_circle(ax, obstacle.final_x, obstacle.final_y, float(obstacle.radius[-1] + obstacle.margin[-1]), OBSTACLE_MARGIN_COLOR, 0.24, 1)
            add_circle(ax, obstacle.final_x, obstacle.final_y, float(obstacle.radius[-1]), OBSTACLE_COLOR, 0.58, 2)
        else:
            for ring_number, point_index in enumerate(ring_indexes):
                progress = ring_number / max(len(ring_indexes) - 1, 1)
                x = float(obstacle.x[point_index])
                y = float(obstacle.y[point_index])
                radius = float(obstacle.radius[point_index])
                margin = float(obstacle.margin[point_index])
                add_circle(ax, x, y, radius + margin, OBSTACLE_MARGIN_COLOR, 0.06 + 0.10 * progress, 1)
                add_circle(ax, x, y, radius, OBSTACLE_COLOR, 0.08 + 0.16 * progress, 2)
        ax.scatter(obstacle.final_x, obstacle.final_y, marker="X", s=120, color="#7a0b0b", zorder=6)

    finish_axes(ax, title, devices, targets, obstacles, legend_handles_margins(devices), output, dpi)


def draw_final_obstacles(ax: plt.Axes, obstacles: list[Trajectory]) -> None:
    for obstacle in obstacles:
        add_fading_line(ax, obstacle.x, obstacle.y, OBSTACLE_COLOR, linewidth=1.2, min_alpha=0.012, max_alpha=0.28, zorder=1)
        add_circle(
            ax,
            obstacle.final_x,
            obstacle.final_y,
            float(obstacle.radius[-1] + obstacle.margin[-1]),
            OBSTACLE_MARGIN_COLOR,
            0.25,
            2,
        )
        add_circle(ax, obstacle.final_x, obstacle.final_y, float(obstacle.radius[-1]), OBSTACLE_COLOR, 0.65, 3)
        ax.scatter(obstacle.final_x, obstacle.final_y, marker="X", s=120, color="#7a0b0b", zorder=6)


def finish_axes(
    ax: plt.Axes,
    title: str,
    devices: list[Trajectory],
    targets: list[Trajectory],
    obstacles: list[Trajectory],
    legend_handles: list[Line2D],
    output: Path,
    dpi: int,
) -> None:
    set_limits(ax, devices, targets, obstacles)
    ax.set_title(title, fontsize=18, pad=12)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    ax.set_aspect("equal", adjustable="box")
    ax.legend(handles=legend_handles, loc="upper center", bbox_to_anchor=(0.5, -0.04), ncol=3, frameon=True, fontsize=15)
    for spine in ax.spines.values():
        spine.set_edgecolor("black")
        spine.set_linewidth(1.8)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig = ax.figure
    fig.savefig(output, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def set_limits(
    ax: plt.Axes,
    devices: list[Trajectory],
    targets: list[Trajectory],
    obstacles: list[Trajectory],
) -> None:
    x_values: list[np.ndarray] = []
    y_values: list[np.ndarray] = []
    for trajectory in [*devices, *targets, *obstacles]:
        x_values.append(trajectory.x)
        y_values.append(trajectory.y)
    for device in devices:
        padding = np.array([robot_margin_radius(v) for v in device.safe_margin])
        x_values.append(device.x - padding)
        x_values.append(device.x + padding)
        y_values.append(device.y - padding)
        y_values.append(device.y + padding)
    for obstacle in obstacles:
        padding = obstacle.radius + obstacle.margin
        x_values.append(obstacle.x - padding)
        x_values.append(obstacle.x + padding)
        y_values.append(obstacle.y - padding)
        y_values.append(obstacle.y + padding)
    xs = np.concatenate(x_values)
    ys = np.concatenate(y_values)
    x_min, x_max = float(np.nanmin(xs)), float(np.nanmax(xs))
    y_min, y_max = float(np.nanmin(ys)), float(np.nanmax(ys))
    pad = max((x_max - x_min) * 0.05, (y_max - y_min) * 0.05, 0.75)
    ax.set_xlim(x_min - pad, x_max + pad)
    ax.set_ylim(y_min - pad, y_max + pad)


def legend_handles_clean(devices: list[Trajectory]) -> list[Line2D]:
    handles = [
        Line2D([0], [0], color=DEVICE_COLORS[0], lw=3, marker="o", markersize=9, label="Devices"),
        Line2D([0], [0], color=SAFE_COLOR, lw=2, marker="o", alpha=0.35, markersize=9, label="Final safety radius"),
        Line2D([0], [0], color=TARGET_COLOR, lw=2, ls="--", marker="*", markersize=12, label="Targets"),
        Line2D([0], [0], color=OBSTACLE_COLOR, lw=2, marker="X", markersize=9, label="Obstacles"),
    ]
    if len(devices) > 1:
        handles[0].set_label(f"Devices ({len(devices)})")
    return handles


def legend_handles_margins(devices: list[Trajectory]) -> list[Line2D]:
    handles = legend_handles_clean(devices)
    handles[1].set_label("Sampled safety radii")
    handles.append(Line2D([0], [0], color=OBSTACLE_MARGIN_COLOR, lw=6, alpha=0.35, label="Obstacle margins"))
    return handles


def output_paths(output_dir: Path, prefix: str) -> tuple[Path, Path]:
    return output_dir / f"{prefix}_movement.png", output_dir / f"{prefix}_movement_margins.png"


def main() -> int:
    args = parse_args()
    config = parse_config(args.config, args.data_dir, args.title)
    prefix = args.output_prefix or config.data_dir.name.rstrip("/") or config.title

    devices = read_devices(config.data_dir, args.max_points)
    targets = read_targets(config.data_dir, args.max_points)
    obstacles = read_obstacles(config.data_dir, args.max_points)

    clean_output, margins_output = output_paths(args.output_dir, prefix)
    draw_clean_movement(devices, targets, obstacles, clean_output, args.dpi, f"{config.title} movement")
    draw_margin_evolution(
        devices,
        targets,
        obstacles,
        margins_output,
        args.dpi,
        f"{config.title} margin evolution",
        args.margin_samples,
    )

    print(f"Loaded {len(devices)} devices, {len(targets)} targets, {len(obstacles)} obstacles.")
    print(f"Wrote {clean_output}")
    print(f"Wrote {margins_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
