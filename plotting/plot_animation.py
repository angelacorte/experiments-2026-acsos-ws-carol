#!/usr/bin/env python3
"""Generate GIF animations of experiment snapshots over time."""

from __future__ import annotations

import argparse
import csv
import math
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
from matplotlib.animation import FuncAnimation, PillowWriter
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
from plot_style import (
    NODE_LABEL_FONT_SIZE,
    SPATIAL_FIGSIZE,
    TARGET_LABEL_FONT_SIZE,
    TITLE_FONT_SIZE,
    apply_plot_style,
)

apply_plot_style(plt)
ALCHEMIST_ROBOT_MARGIN_RADIUS_FACTOR = 0.5
VIEW_PADDING_FACTOR = 0.03
MIN_VIEW_PADDING = 0.5


@dataclass(frozen=True)
class ExperimentConfig:
    data_dir: Path
    title: str
    connect_within_distance: float | None
    robot_safe_margin: float | None
    max_comm_distance: float | None


@dataclass(frozen=True)
class RobotState:
    entity_id: int
    x: float
    y: float
    safe_margin: float
    comm_distance: float
    is_leader: bool


@dataclass(frozen=True)
class TargetState:
    entity_id: int
    x: float
    y: float


@dataclass(frozen=True)
class ObstacleState:
    entity_id: int
    x: float
    y: float
    radius: float
    margin: float


@dataclass(frozen=True)
class ExperimentData:
    robots: dict[int, dict[float, RobotState]]
    targets: dict[int, dict[float, TargetState]]
    obstacles: dict[int, dict[float, ObstacleState]]
    frame_times: list[float]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate GIF animations from exported simulation CSV data."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src/main/yaml"),
        help="Experiment name, YAML path, or directory containing YAML experiments. Defaults to src/main/yaml.",
    )
    parser.add_argument("--data-dir", type=Path, default=None, help="Directory containing exported CSV files.")
    parser.add_argument("--output-dir", type=Path, default=Path("charts/gifs"), help="Output directory.")
    parser.add_argument("--output-prefix", default=None, help="Filename prefix. Defaults to the data directory name.")
    parser.add_argument("--title", default=None, help="Animation title. Defaults to YAML stem or data directory name.")
    parser.add_argument("--until", type=float, default=None, help="Last simulation time to include. Defaults to all data.")
    parser.add_argument("--frame-step", type=int, default=1, help="Keep one frame every N available time ticks.")
    parser.add_argument("--fps", type=int, default=8, help="GIF frames per second.")
    parser.add_argument("--dpi", type=int, default=120, help="GIF rendering DPI.")
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


def parse_config(path: Path | None, data_dir_override: Path | None, title_override: str | None) -> ExperimentConfig:
    variables: dict[str, str | float] = {}
    data_dir = data_dir_override
    title = title_override

    if path:
        path = resolve_config_path(path)
        text = path.read_text(encoding="utf-8")
        title = title or path.stem
        for match in re.finditer(r"^\s{2}([A-Za-z0-9_]+):\s*&([A-Za-z0-9_]+)\s+(.+)$", text, re.MULTILINE):
            name, anchor, raw_value = match.groups()
            value = parse_scalar(raw_value)
            variables[name] = value
            variables[anchor] = value

    yaml_data_dir = variables.get("dataPath")
    if data_dir is None and isinstance(yaml_data_dir, str):
        data_dir = Path(yaml_data_dir)
    if data_dir is None:
        raise ValueError("Pass --config or --data-dir.")
    if title is None:
        title = data_dir.name

    return ExperimentConfig(
        data_dir=data_dir,
        title=title,
        connect_within_distance=resolve_number("*connectWithinDistance", variables),
        robot_safe_margin=resolve_number("*robotSafeMargin", variables),
        max_comm_distance=resolve_number("*maxCommDistance", variables),
    )


def parse_configs(path: Path | None, data_dir_override: Path | None, title_override: str | None) -> list[ExperimentConfig]:
    if data_dir_override is not None:
        return [parse_config(path, data_dir_override, title_override)]

    if path is None:
        path = Path("src/main/yaml")

    if path.is_dir():
        configs: list[ExperimentConfig] = []
        for yaml_path in sorted([*path.glob("*.yml"), *path.glob("*.yaml")]):
            try:
                configs.append(parse_config(yaml_path, None, title_override))
            except Exception as error:
                print(f"Warning: skipping {yaml_path}: {error}")
        if not configs:
            raise ValueError(f"No valid experiment YAML files found in {path}")
        return configs

    return [parse_config(path, None, title_override)]


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


def parse_id(path: Path) -> int:
    match = re.search(r"-(\d+)", path.name)
    if not match:
        raise ValueError(f"Cannot parse id from {path}")
    return int(match.group(1))


def sort_key(path: Path) -> tuple[str, int]:
    return re.sub(r"-\d+$", "-", path.stem), parse_id(path)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def as_float(row: dict[str, str], column: str, default: float = 0.0) -> float:
    value = row.get(column)
    if value in (None, ""):
        return default
    return float(value)


def as_bool(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"true", "1", "yes", "y"}


def rounded_time(row: dict[str, str]) -> float:
    return float(round(as_float(row, "time")))


def read_experiment_data(config: ExperimentConfig, until: float | None, frame_step: int) -> ExperimentData:
    robots: dict[int, dict[float, RobotState]] = {}
    targets: dict[int, dict[float, TargetState]] = {}
    obstacles: dict[int, dict[float, ObstacleState]] = {}

    safe_default = config.robot_safe_margin or 0.0
    comm_default = config.max_comm_distance or 0.0

    for path in sorted(config.data_dir.glob("positions_node-*.csv"), key=sort_key):
        robot_id = parse_id(path)
        series: dict[float, RobotState] = {}
        for row in read_rows(path):
            time = rounded_time(row)
            if until is not None and time > round(until):
                continue
            robot_id = int(as_float(row, "nodeId", robot_id))
            series[time] = RobotState(
                entity_id=robot_id,
                x=as_float(row, "X"),
                y=as_float(row, "Y"),
                safe_margin=as_float(row, "safeMargin", safe_default),
                comm_distance=as_float(row, "commDistance", comm_default),
                is_leader=as_bool(row.get("isLeader")),
            )
        if series:
            robots[robot_id] = series

    if not robots:
        raise FileNotFoundError(f"No positions_node-*.csv data found in {config.data_dir}")

    for path in sorted(config.data_dir.glob("target-*.csv"), key=sort_key):
        target_id = parse_id(path)
        series: dict[float, TargetState] = {}
        for row in read_rows(path):
            time = rounded_time(row)
            if until is not None and time > round(until):
                continue
            target_id = int(as_float(row, "id", target_id))
            series[time] = TargetState(target_id, as_float(row, "x"), as_float(row, "y"))
        if series:
            targets[target_id] = series

    for path in sorted(config.data_dir.glob("obstacle-*.csv"), key=sort_key):
        obstacle_id = parse_id(path)
        series: dict[float, ObstacleState] = {}
        for row in read_rows(path):
            time = rounded_time(row)
            if until is not None and time > round(until):
                continue
            obstacle_id = int(as_float(row, "id", obstacle_id))
            series[time] = ObstacleState(
                obstacle_id,
                as_float(row, "x"),
                as_float(row, "y"),
                as_float(row, "radius"),
                as_float(row, "margin"),
            )
        if series:
            obstacles[obstacle_id] = series

    common_robot_times = sorted(set.intersection(*(set(series) for series in robots.values())))
    if not common_robot_times:
        raise ValueError(f"Robot CSV files in {config.data_dir} do not share common times.")

    frame_step = max(frame_step, 1)
    frame_times = common_robot_times[::frame_step]
    if common_robot_times[-1] not in frame_times:
        frame_times.append(common_robot_times[-1])

    return ExperimentData(robots, targets, obstacles, frame_times)


def robot_margin_radius(safe_margin: float) -> float:
    return safe_margin * ALCHEMIST_ROBOT_MARGIN_RADIUS_FACTOR


def state_at_or_before(series: dict[float, RobotState | TargetState | ObstacleState], time: float):
    if time in series:
        return series[time]
    previous_times = [candidate for candidate in series if candidate <= time]
    if not previous_times:
        return None
    return series[max(previous_times)]


def add_circle(ax: plt.Axes, x: float, y: float, radius: float, color: str, alpha: float, zorder: int) -> None:
    if radius > 0:
        ax.add_patch(Circle((x, y), radius, color=color, alpha=alpha, linewidth=0, zorder=zorder))


def compute_limits(config: ExperimentConfig, data: ExperimentData) -> tuple[float, float, float, float]:
    xs: list[float] = []
    ys: list[float] = []

    for series in data.robots.values():
        for state in series.values():
            padding = max(robot_margin_radius(state.safe_margin), 0.0)
            xs.extend([state.x - padding, state.x + padding])
            ys.extend([state.y - padding, state.y + padding])

    for series in data.targets.values():
        for state in series.values():
            xs.append(state.x)
            ys.append(state.y)

    for series in data.obstacles.values():
        for state in series.values():
            padding = state.radius + state.margin
            xs.extend([state.x - padding, state.x + padding])
            ys.extend([state.y - padding, state.y + padding])

    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    pad = max((x_max - x_min) * VIEW_PADDING_FACTOR, (y_max - y_min) * VIEW_PADDING_FACTOR, MIN_VIEW_PADDING)
    return x_min - pad, x_max + pad, y_min - pad, y_max + pad


def draw_frame(
    ax: plt.Axes,
    config: ExperimentConfig,
    data: ExperimentData,
    time: float,
    limits: tuple[float, float, float, float],
    has_leader: bool,
) -> None:
    ax.clear()
    robots = [
        state_at_or_before(series, time)
        for _, series in sorted(data.robots.items())
    ]
    robots = [robot for robot in robots if robot is not None]

    for robot in robots:
        add_circle(ax, robot.x, robot.y, robot.comm_distance, COMM_COLOR, 0.15, 1)

    for index, left in enumerate(robots):
        for right in robots[index + 1 :]:
            if config.connect_within_distance is None:
                linked = True
            else:
                linked = math.dist((left.x, left.y), (right.x, right.y)) <= config.connect_within_distance
            if linked:
                ax.plot([left.x, right.x], [left.y, right.y], color=LINK_COLOR, linewidth=1.4, alpha=0.5, zorder=2)

    for _, series in sorted(data.obstacles.items()):
        obstacle = state_at_or_before(series, time)
        if obstacle is None:
            continue
        add_circle(ax, obstacle.x, obstacle.y, obstacle.radius + obstacle.margin, OBSTACLE_MARGIN_COLOR, 0.25, 3)
        add_circle(ax, obstacle.x, obstacle.y, obstacle.radius, OBSTACLE_COLOR, 0.65, 4)
        ax.scatter(obstacle.x, obstacle.y, marker="X", s=95, color=OBSTACLE_MARKER_COLOR, zorder=8)

    for robot in robots:
        add_circle(ax, robot.x, robot.y, robot_margin_radius(robot.safe_margin), SAFE_COLOR, 0.18, 5)
        ax.scatter(robot.x, robot.y, s=90, color=ROBOT_COLOR, edgecolors="black", linewidths=0.7, zorder=9)
        ax.text(robot.x, robot.y, str(robot.entity_id), ha="center", va="center", fontsize=NODE_LABEL_FONT_SIZE, color="white", zorder=10)
        if robot.is_leader:
            ax.scatter(robot.x, robot.y, s=160, facecolors="none", edgecolors=LEADER_COLOR, linewidths=2.0, zorder=11)

    for _, series in sorted(data.targets.items()):
        target = state_at_or_before(series, time)
        if target is None:
            continue
        ax.scatter(target.x, target.y, marker="*", s=220, color=TARGET_COLOR, edgecolors="black", linewidths=0.6, zorder=7)
        ax.text(target.x, target.y + 0.45, f"T{target.entity_id}", ha="center", va="bottom", fontsize=TARGET_LABEL_FONT_SIZE, color=TARGET_COLOR)

    ax.set_xlim(limits[0], limits[1])
    ax.set_ylim(limits[2], limits[3])
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, color="#e4e4e4", linewidth=0.8)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"{beautify_experiment_title(config.title)} | simulation time={int(round(time))}s", fontsize=TITLE_FONT_SIZE, pad=10)
    ax.legend(handles=legend_handles(config, data, has_leader), loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=4, frameon=True)


def legend_handles(config: ExperimentConfig, data: ExperimentData, has_leader: bool) -> list[Line2D]:
    handles = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=ROBOT_COLOR, markeredgecolor="black", markersize=8, label="Robots"),
        Line2D([0], [0], marker="o", color=SAFE_COLOR, alpha=0.35, markersize=8, label="Robot safety radius"),
        Line2D([0], [0], marker="o", color=COMM_COLOR, alpha=0.35, markersize=8, label="Communication radius"),
        Line2D([0], [0], color=LINK_COLOR, linewidth=2, alpha=0.65, label="Communication links"),
    ]
    if config.connect_within_distance is not None:
        handles[3].set_label("Links within communication distance")
    if data.targets:
        handles.append(Line2D([0], [0], marker="*", color="none", markerfacecolor=TARGET_COLOR, markeredgecolor="black", markersize=11, label="Targets"))
    if data.obstacles:
        handles.extend(
            [
                Line2D([0], [0], marker="X", color="none", markerfacecolor=OBSTACLE_MARKER_COLOR, markeredgecolor=OBSTACLE_MARKER_COLOR, markersize=8, label="Obstacles"),
                Line2D([0], [0], color=OBSTACLE_MARGIN_COLOR, linewidth=6, alpha=0.35, label="Obstacle safety margin"),
            ]
        )
    if has_leader:
        handles.append(Line2D([0], [0], marker="o", color="none", markeredgecolor=LEADER_COLOR, markerfacecolor="none", markersize=11, linestyle="None", label="Leader"))
    return handles


def output_path(output_dir: Path, prefix: str) -> Path:
    return output_dir / prefix / f"{prefix}.gif"


def make_gif(config: ExperimentConfig, data: ExperimentData, output: Path, fps: int, dpi: int) -> None:
    limits = compute_limits(config, data)
    has_leader = any(state.is_leader for series in data.robots.values() for state in series.values())
    fig, ax = plt.subplots(figsize=SPATIAL_FIGSIZE)
    fig.subplots_adjust(left=0.09, right=0.98, top=0.88, bottom=0.28)

    def update(time: float):
        draw_frame(ax, config, data, time, limits, has_leader)
        return []

    animation = FuncAnimation(fig, update, frames=data.frame_times, interval=1000 / max(fps, 1), blit=False)
    output.parent.mkdir(parents=True, exist_ok=True)
    animation.save(output, writer=PillowWriter(fps=max(fps, 1)), dpi=dpi)
    plt.close(fig)


def main() -> int:
    args = parse_args()
    configs = parse_configs(args.config, args.data_dir, args.title)

    for config in configs:
        prefix = args.output_prefix or config.data_dir.name.rstrip("/") or config.title
        try:
            data = read_experiment_data(config, args.until, args.frame_step)
        except Exception as error:
            print(f"Warning: skipping {config.title} ({config.data_dir}): {error}")
            continue

        output = output_path(args.output_dir, prefix)
        make_gif(config, data, output, args.fps, args.dpi)
        print(f"Loaded {len(data.robots)} robots, {len(data.targets)} targets, {len(data.obstacles)} obstacles for {config.title}.")
        print(f"Rendered {len(data.frame_times)} frames.")
        print(f"Wrote {output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
