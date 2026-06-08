#!/usr/bin/env python3
"""Plot simulation snapshots from exported Alchemist CSV files."""

from __future__ import annotations

import argparse
import csv
import math
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

os.environ.setdefault("MPLCONFIGDIR", str(Path("charts/.matplotlib").resolve()))
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
os.environ.setdefault("XDG_CACHE_HOME", str(Path("charts/.cache").resolve()))
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle


ROBOT_COLOR = "#1f77b4"
TARGET_COLOR = "#2ca02c"
OBSTACLE_COLOR = "#d62728"
LINK_COLOR = "#4a4a4a"
COMM_COLOR = "#b8b8b8"
SAFE_COLOR = "#7f7f7f"
OBSTACLE_MARGIN_COLOR = "#f2cf3a"
ALCHEMIST_ROBOT_MARGIN_RADIUS_FACTOR = 0.5


@dataclass(frozen=True)
class ExperimentConfig:
    data_dir: Path
    connect_within_distance: float | None
    robot_safe_margin: float | None
    title: str


@dataclass(frozen=True)
class EntitySample:
    kind: str
    entity_id: int
    step: float
    time: float
    x: float
    y: float
    safe_margin: float = 0.0
    comm_distance: float = 0.0
    radius: float = 0.0
    margin: float = 0.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Plot one or more simulation snapshots showing robot positions, safety "
            "margins, communication ranges, communication links, targets, and obstacles."
        )
    )
    parser.add_argument(
        "snapshots",
        type=float,
        nargs="+",
        help="Snapshot values. Interpreted as times by default, or as steps with --by step.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Experiment YAML. Used to infer data directory and link radius.",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=None,
        help="Directory containing positions_node-*.csv, target-*.csv, and obstacle-*.csv.",
    )
    parser.add_argument(
        "--by",
        choices=("time", "step"),
        default="time",
        help="Interpret positional snapshots as simulation times or simulation steps.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("charts/snapshots"),
        help="Directory where generated images are written.",
    )
    parser.add_argument(
        "--output-prefix",
        default=None,
        help="Filename prefix. Defaults to the data directory name.",
    )
    parser.add_argument(
        "--connect-within-distance",
        type=float,
        default=None,
        help="Override YAML network-model distance used to draw communication links.",
    )
    parser.add_argument(
        "--robot-safe-margin",
        type=float,
        default=None,
        help="Fallback safe margin for robot CSVs that do not contain safeMargin.",
    )
    parser.add_argument(
        "--trail",
        type=int,
        default=0,
        help="Draw the last N samples of each robot trajectory before the snapshot.",
    )
    parser.add_argument("--dpi", type=int, default=220, help="Output image DPI.")
    parser.add_argument("--show", action="store_true", help="Show figures instead of only saving them.")
    return parser.parse_args()


def parse_scalar(raw_value: str) -> str | float:
    value = raw_value.split("#", 1)[0].strip().strip(",")
    if value.startswith("[") and value.endswith("]"):
        return value
    value = value.strip("'\"")
    try:
        return float(value)
    except ValueError:
        return value


def parse_config(path: Path | None, data_dir_override: Path | None) -> ExperimentConfig:
    variables: dict[str, str | float] = {}
    connect_within_distance: float | None = None
    title = data_dir_override.name if data_dir_override else "snapshot"

    if path:
        text = path.read_text(encoding="utf-8")
        title = path.stem
        for match in re.finditer(r"^\s{2}([A-Za-z0-9_]+):\s*&([A-Za-z0-9_]+)\s+(.+)$", text, re.MULTILINE):
            name, anchor, raw_value = match.groups()
            value = parse_scalar(raw_value)
            variables[name] = value
            variables[anchor] = value

        network_match = re.search(
            r"network-model:\s*\n(?:\s+.+\n)*?\s+parameters:\s*\[\s*([^\]]+)\s*\]",
            text,
        )
        if network_match:
            connect_within_distance = resolve_number(network_match.group(1), variables)

    yaml_data_dir = variables.get("dataPath")
    data_dir = data_dir_override
    if data_dir is None and isinstance(yaml_data_dir, str):
        data_dir = Path(yaml_data_dir)
    if data_dir is None:
        raise ValueError("Pass --config or --data-dir so the CSV directory can be found.")

    robot_safe_margin = resolve_number("*robotSafeMargin", variables)
    return ExperimentConfig(
        data_dir=data_dir,
        connect_within_distance=connect_within_distance,
        robot_safe_margin=robot_safe_margin,
        title=title,
    )


def resolve_number(raw_value: str, variables: dict[str, str | float]) -> float | None:
    value = raw_value.strip().strip("[]").strip()
    if value.startswith("*"):
        resolved = variables.get(value[1:])
        return float(resolved) if isinstance(resolved, (int, float)) else None
    try:
        return float(value)
    except ValueError:
        return None


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def as_float(row: dict[str, str], column: str, default: float = 0.0) -> float:
    value = row.get(column)
    if value in (None, ""):
        return default
    return float(value)


def nearest_row(rows: list[dict[str, str]], value: float, by: str) -> dict[str, str]:
    if not rows:
        raise ValueError("Cannot select a snapshot from an empty CSV file.")
    return min(rows, key=lambda row: abs(as_float(row, by) - value))


def load_samples(
    data_dir: Path,
    snapshot: float,
    by: str,
    fallback_robot_safe_margin: float | None,
) -> tuple[list[EntitySample], list[EntitySample], list[EntitySample], dict[int, list[tuple[float, float]]]]:
    robots: list[EntitySample] = []
    targets: list[EntitySample] = []
    obstacles: list[EntitySample] = []
    trails: dict[int, list[tuple[float, float]]] = {}

    # Interpret requested snapshot times as integer ticks (round).
    snapshot_value = float(round(snapshot))

    for path in sorted(data_dir.glob("positions_node-*.csv"), key=natural_key):
        rows = read_rows(path)
        # Always select by the 'time' column (we do not use 'step' in plotting)
        row = nearest_row(rows, snapshot_value, "time")
        robot_id = int(as_float(row, "nodeId", parse_id(path.name)))
        safe_margin = as_float(row, "safeMargin", fallback_robot_safe_margin or 0.0)
        robots.append(
            EntitySample(
                kind="robot",
                entity_id=robot_id,
                step=as_float(row, "step"),
                time=as_float(row, "time"),
                x=as_float(row, "X"),
                y=as_float(row, "Y"),
                safe_margin=safe_margin,
                comm_distance=as_float(row, "commDistance"),
            )
        )
        selected_index = rows.index(row)
        trails[robot_id] = [(as_float(r, "X"), as_float(r, "Y")) for r in rows[: selected_index + 1]]

    for path in sorted(data_dir.glob("target-*.csv"), key=natural_key):
        row = nearest_row(read_rows(path), snapshot_value, "time")
        targets.append(
            EntitySample(
                kind="target",
                entity_id=int(as_float(row, "id", parse_id(path.name))),
                step=as_float(row, "step"),
                time=as_float(row, "time"),
                x=as_float(row, "x"),
                y=as_float(row, "y"),
            )
        )

    for path in sorted(data_dir.glob("obstacle-*.csv"), key=natural_key):
        row = nearest_row(read_rows(path), snapshot_value, "time")
        obstacles.append(
            EntitySample(
                kind="obstacle",
                entity_id=int(as_float(row, "id", parse_id(path.name))),
                step=as_float(row, "step"),
                time=as_float(row, "time"),
                x=as_float(row, "x"),
                y=as_float(row, "y"),
                radius=as_float(row, "radius"),
                margin=as_float(row, "margin"),
            )
        )

    if not robots:
        raise FileNotFoundError(f"No positions_node-*.csv files found in {data_dir}")
    return robots, targets, obstacles, trails


def parse_id(filename: str) -> int:
    match = re.search(r"-(\d+)", filename)
    if not match:
        raise ValueError(f"Cannot parse entity id from {filename}")
    return int(match.group(1))


def natural_key(path: Path) -> tuple[str, int]:
    return re.sub(r"-\d+$", "-", path.stem), parse_id(path.name)


def communication_links(robots: list[EntitySample], distance: float | None) -> list[tuple[EntitySample, EntitySample]]:
    if distance is None or distance <= 0:
        return []
    links = []
    for index, left in enumerate(robots):
        for right in robots[index + 1 :]:
            if math.dist((left.x, left.y), (right.x, right.y)) <= distance:
                links.append((left, right))
    return links


def add_circle(ax: plt.Axes, sample: EntitySample, radius: float, color: str, alpha: float, **kwargs: object) -> None:
    if radius <= 0:
        return
    ax.add_patch(Circle((sample.x, sample.y), radius, color=color, alpha=alpha, linewidth=0, **kwargs))


def alchemist_robot_margin_radius(safe_margin: float) -> float:
    """Match DrawObstacleRadius.drawRobot, where SafeMargin is rendered as the oval diameter."""
    return safe_margin * ALCHEMIST_ROBOT_MARGIN_RADIUS_FACTOR


def draw_snapshot(
    config: ExperimentConfig,
    snapshot: float,
    by: str,
    output_path: Path,
    dpi: int,
    trail_length: int,
    show: bool,
) -> None:
    robots, targets, obstacles, trails = load_samples(
        config.data_dir,
        snapshot,
        by,
        config.robot_safe_margin,
    )

    fig, ax = plt.subplots(figsize=(9, 8), constrained_layout=True)

    for robot in robots:
        add_circle(ax, robot, robot.comm_distance, COMM_COLOR, 0.2)
    for left, right in communication_links(robots, config.connect_within_distance):
        ax.plot([left.x, right.x], [left.y, right.y], color=LINK_COLOR, linewidth=1.6, alpha=0.55, zorder=2)

    if trail_length > 0:
        for robot in robots:
            points = trails[robot.entity_id][-trail_length:]
            if len(points) >= 2:
                xs, ys = zip(*points)
                ax.plot(xs, ys, color=ROBOT_COLOR, alpha=0.25, linewidth=1.4, zorder=1)

    for obstacle in obstacles:
        add_circle(ax, obstacle, obstacle.radius + obstacle.margin, OBSTACLE_MARGIN_COLOR, 0.25)
        add_circle(ax, obstacle, obstacle.radius, OBSTACLE_COLOR, 0.65)
        ax.scatter(obstacle.x, obstacle.y, marker="X", s=100, color="#7a0b0b", zorder=5)

    for robot in robots:
        add_circle(ax, robot, alchemist_robot_margin_radius(robot.safe_margin), SAFE_COLOR, 0.18)
        ax.scatter(robot.x, robot.y, s=90, color=ROBOT_COLOR, edgecolors="black", linewidths=0.7, zorder=7)
        ax.text(robot.x, robot.y, str(robot.entity_id), ha="center", va="center", fontsize=8, color="white", zorder=8)

    for target in targets:
        ax.scatter(
            target.x,
            target.y,
            marker="*",
            s=220,
            color=TARGET_COLOR,
            edgecolors="black",
            linewidths=0.6,
            zorder=6,
        )
        ax.text(target.x, target.y + 0.45, f"T{target.entity_id}", ha="center", va="bottom", fontsize=9, color="#1d5d1d")

    set_limits(ax, robots, targets, obstacles)
    ax.set_title(f"{config.title} | simulation time={int(round(snapshot))}s")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, color="#e4e4e4", linewidth=0.8)
    ax.legend(handles=legend_handles(config), loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=3, frameon=True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
    if show:
        plt.show()
    plt.close(fig)


def set_limits(
    ax: plt.Axes,
    robots: list[EntitySample],
    targets: list[EntitySample],
    obstacles: list[EntitySample],
) -> None:
    xs: list[float] = []
    ys: list[float] = []
    for sample in [*robots, *targets, *obstacles]:
        robot_safe_margin = alchemist_robot_margin_radius(sample.safe_margin)
        padding = max(robot_safe_margin, sample.comm_distance, sample.radius + sample.margin, 0.0)
        xs.extend([sample.x - padding, sample.x + padding])
        ys.extend([sample.y - padding, sample.y + padding])
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    pad = max((x_max - x_min) * 0.06, (y_max - y_min) * 0.06, 1.0)
    ax.set_xlim(x_min - pad, x_max + pad)
    ax.set_ylim(y_min - pad, y_max + pad)


def legend_handles(config: ExperimentConfig) -> list[Line2D]:
    handles = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=ROBOT_COLOR, markeredgecolor="black", markersize=9, label="Robot"),
        Line2D([0], [0], marker="o", color=SAFE_COLOR, alpha=0.35, markersize=9, label="Safe margin"),
        Line2D([0], [0], marker="*", color="none", markerfacecolor=TARGET_COLOR, markeredgecolor="black", markersize=12, label="Target"),
        Line2D([0], [0], color=LINK_COLOR, linewidth=2, alpha=0.65, label="Communication link"),
    ]
    if config.connect_within_distance is not None:
        handles[-1].set_label(f"Linking distance")
    handles.extend(
        [
            Line2D([0], [0], marker="o", color=COMM_COLOR, alpha=0.35, markersize=9, label="Max communication distance"),
            Line2D([0], [0], marker="X", color="none", markerfacecolor=OBSTACLE_COLOR, markersize=9, label="Obstacle"),
        ]
    )
    return handles


def output_name(prefix: str, by: str, snapshot: float) -> str:
    # Always use time in output filename; do not expose 'step' labeling
    value = f"{int(round(snapshot))}"
    return f"{prefix}_time-{value}.png"


def generated_paths(paths: Iterable[Path]) -> str:
    return "\n".join(f"  - {path}" for path in paths)


def main() -> int:
    args = parse_args()
    config = parse_config(args.config, args.data_dir)
    if args.connect_within_distance is not None:
        config = ExperimentConfig(
            data_dir=config.data_dir,
            connect_within_distance=args.connect_within_distance,
            robot_safe_margin=config.robot_safe_margin,
            title=config.title,
        )
    if args.robot_safe_margin is not None:
        config = ExperimentConfig(
            data_dir=config.data_dir,
            connect_within_distance=config.connect_within_distance,
            robot_safe_margin=args.robot_safe_margin,
            title=config.title,
        )

    prefix = args.output_prefix or config.data_dir.name.rstrip("/") or config.title
    outputs = []
    for snapshot in args.snapshots:
        path = args.output_dir / output_name(prefix, args.by, snapshot)
        draw_snapshot(config, snapshot, args.by, path, args.dpi, args.trail, args.show)
        outputs.append(path)

    print("Generated snapshot plots:")
    print(generated_paths(outputs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
