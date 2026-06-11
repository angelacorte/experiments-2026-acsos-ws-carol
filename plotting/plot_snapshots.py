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

from plot_labels import beautify_experiment_title
from plot_palette import (
    COMM_COLOR,
    LEADER_COLOR,
    LINK_COLOR,
    OBSTACLE_COLOR,
    OBSTACLE_MARGIN_COLOR,
    OBSTACLE_MARKER_COLOR,
    ROBOT_COLOR,
    SAFE_COLOR,
    TARGET_COLOR,
)
from plot_style import NODE_LABEL_FONT_SIZE, SPATIAL_FIGSIZE, TARGET_LABEL_FONT_SIZE, apply_plot_style

apply_plot_style(plt)
ALCHEMIST_ROBOT_MARGIN_RADIUS_FACTOR = 0.5
VIEW_PADDING_FACTOR = 0.03
MIN_VIEW_PADDING = 0.5


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
    is_leader: bool = False


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
        help="Snapshot values interpreted as simulation times.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src/main/yaml"),
        help="Experiment name, YAML path, or directory containing YAML experiments. Defaults to src/main/yaml and plots all experiments found there.",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=None,
        help="Directory containing positions_node-*.csv, target-*.csv, and obstacle-*.csv.",
    )
    parser.add_argument(
        "--time",
        action="store_true",
        help="Interpret positional snapshots as simulation times (default; kept for CLI clarity).",
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
    parser.add_argument(
        "--output-format",
        choices=("pdf", "png"),
        default="pdf",
        help="Output format. Defaults to pdf; choose png to save only PNG files.",
    )
    parser.add_argument("--png", action="store_const", const="png", dest="output_format", help="Save only PNG files.")
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
        path = resolve_config_path(path)
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

def parse_configs(path: Path | None, data_dir_override: Path | None) -> list[ExperimentConfig]:
    if data_dir_override is not None:
        return [parse_config(path, data_dir_override)]

    if path is None:
        path = Path("src/main/yaml")

    if path.is_dir():
        configs: list[ExperimentConfig] = []
        for yaml_path in sorted([*path.glob("*.yml"), *path.glob("*.yaml")]):
            try:
                configs.append(parse_config(yaml_path, None))
            except Exception as error:
                print(f"Warning: skipping {yaml_path}: {error}")

        if not configs:
            raise ValueError(f"No valid experiment YAML files found in {path}")

        return configs

    return [parse_config(path, None)]

def resolve_config_path(path: Path) -> Path:
    if path.exists():
        return path
    yaml_dir = Path("src/main/yaml")
    if path.suffix in {".yml", ".yaml"}:
        candidate = yaml_dir / path.name
        if candidate.exists():
            return candidate
    else:
        for suffix in (".yml", ".yaml"):
            candidate = yaml_dir / f"{path.name}{suffix}"
            if candidate.exists():
                return candidate
    raise FileNotFoundError(f"Cannot resolve experiment config from {path}")


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


def exact_row(rows: list[dict[str, str]], value: float, by: str) -> dict[str, str]:
    if not rows:
        raise ValueError("Cannot select a snapshot from an empty CSV file.")
    for row in rows:
        if math.isclose(as_float(row, by), value):
            return row
    raise ValueError(f"Snapshot time {int(round(value))} does not exist in CSV data.")


def load_samples(
    data_dir: Path,
    snapshot: float,
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
        # Always select by the 'time' column (we do not use 'step' in plotting).
        # Do not silently fall back to the nearest available time: missing snapshots
        # must be reported to the user and skipped.
        row = exact_row(rows, snapshot_value, "time")
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
        # detect leader flag if present
        try:
            is_leader_val = row.get("isLeader")
            if is_leader_val is not None:
                robots[-1] = EntitySample(
                    kind="robot",
                    entity_id=robot_id,
                    step=as_float(row, "step"),
                    time=as_float(row, "time"),
                    x=as_float(row, "X"),
                    y=as_float(row, "Y"),
                    safe_margin=safe_margin,
                    comm_distance=as_float(row, "commDistance"),
                    is_leader=str(is_leader_val).strip().lower() in ("true", "1", "yes", "y"),
                )
        except Exception:
            pass
        selected_index = rows.index(row)
        trails[robot_id] = [(as_float(r, "X"), as_float(r, "Y")) for r in rows[: selected_index + 1]]

    for path in sorted(data_dir.glob("target-*.csv"), key=natural_key):
        row = exact_row(read_rows(path), snapshot_value, "time")
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
        row = exact_row(read_rows(path), snapshot_value, "time")
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


def draw_leader_ring(ax: plt.Axes, x: float, y: float, scale: float = 1.0, color: str = LEADER_COLOR) -> None:
    """Draw a concentric ring around point (x,y) to mark a leader."""
    try:
        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_ylim()
        r = max((x1 - x0), (y1 - y0)) * 0.02 * scale
    except Exception:
        r = 0.5 * scale
    ring = Circle((x, y), r, fill=False, edgecolor=color, linewidth=2.0, zorder=9, alpha=0.9)
    ax.add_patch(ring)


def draw_crown(ax: plt.Axes, x: float, y: float, scale: float = 1.0, color: str = LEADER_COLOR) -> None:
    """Draw a small crown-shaped polygon near (x,y) in data coordinates.

    The crown size is proportional to the current axis data range so it
    scales reasonably with different plot extents.
    """
    try:
        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_ylim()
        w = (x1 - x0) * 0.03 * scale
        h = (y1 - y0) * 0.03 * scale
    except Exception:
        w = 0.5 * scale
        h = 0.5 * scale
    base_y = y + h * 0.35
    pts = [
        (x - w / 2, base_y - h * 0.35),
        (x - w / 3, base_y + h * 0.6),
        (x - w / 8, base_y - h * 0.05),
        (x, base_y + h * 0.9),
        (x + w / 8, base_y - h * 0.05),
        (x + w / 3, base_y + h * 0.6),
        (x + w / 2, base_y - h * 0.35),
        (x + w / 2, base_y - h * 0.6),
        (x - w / 2, base_y - h * 0.6),
    ]
    poly = Polygon(pts, closed=True, facecolor=color, edgecolor="black", linewidth=0.6, zorder=9)
    ax.add_patch(poly)



def draw_snapshot(
    config: ExperimentConfig,
    snapshot: float,
    robots: list[EntitySample],
    targets: list[EntitySample],
    obstacles: list[EntitySample],
    trails: dict[int, list[tuple[float, float]]],
    limits: tuple[float, float, float, float],
    output_path: Path,
    dpi: int,
    trail_length: int,
    show: bool,
) -> None:
    fig, ax = plt.subplots(figsize=SPATIAL_FIGSIZE, constrained_layout=True)

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
        ax.scatter(obstacle.x, obstacle.y, marker="X", s=100, color=OBSTACLE_MARKER_COLOR, zorder=5)

    for robot in robots:
        add_circle(ax, robot, alchemist_robot_margin_radius(robot.safe_margin), SAFE_COLOR, 0.18)
        ax.scatter(robot.x, robot.y, s=90, color=ROBOT_COLOR, edgecolors="black", linewidths=0.7, zorder=7)
        if getattr(robot, "is_leader", False):
            draw_leader_ring(ax, robot.x, robot.y, scale=1.0)
        ax.text(robot.x, robot.y, str(robot.entity_id), ha="center", va="center", fontsize=NODE_LABEL_FONT_SIZE, color="white", zorder=8)

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
        ax.text(target.x, target.y + 0.45, f"T{target.entity_id}", ha="center", va="bottom", fontsize=TARGET_LABEL_FONT_SIZE, color=TARGET_COLOR)

    set_limits(ax, limits)
    ax.set_title(f"{beautify_experiment_title(config.title)} | simulation time={int(round(snapshot))}s")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, color="#e4e4e4", linewidth=0.8)
    ax.legend(handles=legend_handles(config, robots, targets, obstacles), loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=4, frameon=True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    save_figure(fig, output_path, dpi)
    if show:
        plt.show()
    plt.close(fig)


def sample_limits(
    robots: list[EntitySample],
    targets: list[EntitySample],
    obstacles: list[EntitySample],
) -> tuple[float, float, float, float]:
    xs: list[float] = []
    ys: list[float] = []
    for sample in [*robots, *targets, *obstacles]:
        robot_safe_margin = alchemist_robot_margin_radius(sample.safe_margin)
        padding = max(robot_safe_margin, sample.radius + sample.margin, 0.0)
        xs.extend([sample.x - padding, sample.x + padding])
        ys.extend([sample.y - padding, sample.y + padding])
    return min(xs), max(xs), min(ys), max(ys)


def common_limits(sample_sets: Iterable[tuple[list[EntitySample], list[EntitySample], list[EntitySample]]]) -> tuple[float, float, float, float]:
    x_mins: list[float] = []
    x_maxs: list[float] = []
    y_mins: list[float] = []
    y_maxs: list[float] = []
    for robots, targets, obstacles in sample_sets:
        x_min, x_max, y_min, y_max = sample_limits(robots, targets, obstacles)
        x_mins.append(x_min)
        x_maxs.append(x_max)
        y_mins.append(y_min)
        y_maxs.append(y_max)

    x_min, x_max = min(x_mins), max(x_maxs)
    y_min, y_max = min(y_mins), max(y_maxs)
    pad = max((x_max - x_min) * VIEW_PADDING_FACTOR, (y_max - y_min) * VIEW_PADDING_FACTOR, MIN_VIEW_PADDING)
    return x_min - pad, x_max + pad, y_min - pad, y_max + pad


def set_limits(ax: plt.Axes, limits: tuple[float, float, float, float]) -> None:
    ax.set_xlim(limits[0], limits[1])
    ax.set_ylim(limits[2], limits[3])


def legend_handles(
    config: ExperimentConfig,
    robots: list[EntitySample],
    targets: list[EntitySample],
    obstacles: list[EntitySample],
) -> list[Line2D]:
    handles = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=ROBOT_COLOR, markeredgecolor="black", markersize=9, label="Robots"),
        Line2D([0], [0], marker="o", color=SAFE_COLOR, alpha=0.35, markersize=9, label="Robot safety radius"),
        Line2D([0], [0], marker="o", color=COMM_COLOR, alpha=0.35, markersize=9, label="Communication radius"),
        Line2D([0], [0], color=LINK_COLOR, linewidth=2, alpha=0.65, label="Communication links"),
    ]
    if config.connect_within_distance is not None:
        handles[3].set_label("Links within communication distance")
    if targets:
        handles.append(Line2D([0], [0], marker="*", color="none", markerfacecolor=TARGET_COLOR, markeredgecolor="black", markersize=12, label="Targets"))
    if obstacles:
        handles.extend(
            [
                Line2D([0], [0], marker="X", color="none", markerfacecolor=OBSTACLE_MARKER_COLOR, markeredgecolor=OBSTACLE_MARKER_COLOR, markersize=9, label="Obstacles"),
                Line2D([0], [0], color=OBSTACLE_MARGIN_COLOR, linewidth=6, alpha=0.35, label="Obstacle safety margin"),
            ]
        )
    if any(robot.is_leader for robot in robots):
        handles.append(Line2D([0], [0], marker="o", color="none", markeredgecolor=LEADER_COLOR, markerfacecolor="none", markersize=12, linestyle="None", label="Leader"))
    return handles


def save_figure(fig: plt.Figure, output: Path, dpi: int) -> None:
    kwargs = {"bbox_inches": "tight"}
    if output.suffix.lower() == ".png":
        kwargs["dpi"] = dpi
    fig.savefig(output, **kwargs)


def output_name(prefix: str, snapshot: float, output_format: str) -> Path:
    # Always use time in output filename; do not expose 'step' labeling
    value = f"{int(round(snapshot))}"
    return Path(prefix) / f"{prefix}_time-{value}.{output_format}"


def generated_paths(paths: Iterable[Path]) -> str:
    rendered_paths = []
    for path in paths:
        rendered_paths.append(f"  - {path}")
    return "\n".join(rendered_paths)


def main() -> int:
    args = parse_args()
    configs = parse_configs(args.config, args.data_dir)

    # Snapshots are always interpreted as times; --time is only a semantic flag.
    _ = args.time

    all_outputs = []

    for base_config in configs:
        config = base_config

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
        snapshot_batches = []

        for snapshot in args.snapshots:
            path = args.output_dir / output_name(prefix, snapshot, args.output_format)

            try:
                robots, targets, obstacles, trails = load_samples(
                    config.data_dir,
                    snapshot,
                    config.robot_safe_margin,
                )
            except Exception as error:
                print(
                    f"Warning: skipping {config.title} at time {int(round(snapshot))} "
                    f"({config.data_dir}): {error}"
                )
                continue

            snapshot_batches.append((snapshot, path, robots, targets, obstacles, trails))

        if not snapshot_batches:
            continue

        limits = common_limits((robots, targets, obstacles) for _, _, robots, targets, obstacles, _ in snapshot_batches)

        for snapshot, path, robots, targets, obstacles, trails in snapshot_batches:
            try:
                draw_snapshot(
                    config,
                    snapshot,
                    robots,
                    targets,
                    obstacles,
                    trails,
                    limits,
                    path,
                    args.dpi,
                    args.trail,
                    args.show,
                )
            except Exception as error:
                print(
                    f"Warning: skipping {config.title} at time {int(round(snapshot))} "
                    f"({config.data_dir}): {error}"
                )
                continue

            all_outputs.append(path)

    print("Generated snapshot plots:")
    print(generated_paths(all_outputs))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
