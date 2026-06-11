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
from matplotlib.colors import to_rgba, Normalize
from matplotlib.lines import Line2D
from matplotlib.patches import Circle

from plot_labels import beautify_experiment_title
from plot_palette import (
    DEVICE_COLORS,
    LEADER_COLOR,
    OBSTACLE_COLOR,
    OBSTACLE_MARGIN_COLOR,
    OBSTACLE_MARKER_COLOR,
    SAFE_COLOR,
    TARGET_COLOR,
)
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
    is_leader: np.ndarray
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
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src/main/yaml"),
        help="Experiment name, YAML path, or directory containing YAML experiments. Defaults to src/main/yaml and plots all experiments found there.",
    )
    parser.add_argument("--data-dir", type=Path, default=None, help="Directory containing exported CSV files.")
    parser.add_argument("--output-dir", type=Path, default=Path("charts/movement"), help="Output directory.")
    parser.add_argument("--output-prefix", default=None, help="Filename prefix. Defaults to the data directory name.")
    parser.add_argument("--title", default=None, help="Plot title. Defaults to YAML stem or data directory name.")
    parser.add_argument("--max-points", type=int, default=2500, help="Maximum points per trajectory after downsampling.")
    parser.add_argument(
        "--margin-samples",
        type=int,
        default=20,
        help="Number of temporal rings per moving entity in the margin-evolution image.",
    )
    parser.add_argument("--dpi", type=int, default=220, help="Output image DPI.")
    parser.add_argument(
        "--output-format",
        choices=("pdf", "png"),
        default="pdf",
        help="Output format. Defaults to pdf; choose png to save only PNG files.",
    )
    parser.add_argument("--png", action="store_const", const="png", dest="output_format", help="Save only PNG files.")
    return parser.parse_args()


def parse_config(path: Path | None, data_dir_override: Path | None, title_override: str | None) -> ExperimentConfig:
    data_dir = data_dir_override
    title = title_override
    if path:
        path = resolve_config_path(path)
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
        with path.open(newline="", encoding="utf-8") as stream:
            raw_rows = list(csv.DictReader(stream))
        if not raw_rows:
            continue
        # Downsample by selecting indexes evenly spaced if requested
        if max_points > 0 and len(raw_rows) > max_points:
            idxs = np.unique(np.linspace(0, len(raw_rows) - 1, max_points, dtype=int))
            rows = [raw_rows[i] for i in idxs]
        else:
            rows = raw_rows
        device_id = int(float(rows[0].get("nodeId", parse_id(path))))
        def to_float(val, default=0.0):
            try:
                return float(val)
            except Exception:
                return default

        times = np.array([float(round(to_float(r.get("time", "nan")))) for r in rows], dtype=float)
        xs = np.array([to_float(r.get("X")) for r in rows], dtype=float)
        ys = np.array([to_float(r.get("Y")) for r in rows], dtype=float)
        safe_m = np.array([to_float(r.get("safeMargin")) for r in rows], dtype=float)
        comm_d = np.array([to_float(r.get("commDistance")) for r in rows], dtype=float)
        # parse isLeader if present; accept true/1/yes
        def parse_bool(v: str) -> bool:
            if v is None:
                return False
            vs = str(v).strip().lower()
            return vs in ("true", "1", "yes", "y")

        is_leader_arr = np.array([parse_bool(r.get("isLeader")) for r in rows], dtype=bool)

        trajectories.append(
            Trajectory(
                entity_id=device_id,
                label=f"Device {device_id}",
                time=times,
                x=xs,
                y=ys,
                safe_margin=safe_m,
                comm_distance=comm_d,
                is_leader=is_leader_arr,
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
                is_leader=np.zeros(len(rows), dtype=bool),
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
                is_leader=np.zeros(len(rows), dtype=bool),
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
def draw_leader_ring(
        ax: plt.Axes,
        x: float,
        y: float,
        scale: float = 1.0,
        color: str = LEADER_COLOR,
        alpha: float = 0.9,
) -> None:
    """Draw a concentric ring around point (x,y) to mark a leader.

    The ring radius is computed relative to the axis range so it remains
    visible at different zoom levels.
    """
    try:
        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_ylim()
        r = max((x1 - x0), (y1 - y0)) * 0.02 * scale
    except Exception:
        r = 0.5 * scale
    ring = Circle((x, y), r, fill=False, edgecolor=color, linewidth=2.0, zorder=9, alpha=alpha)
    ax.add_patch(ring)


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
        # mark leader: find the most recent sample where is_leader==True and
        # draw a conspicuous concentric ring at that position. This highlights
        # the actual location/time where the node acted as leader.
        try:
            leader_idxs = np.where(device.is_leader)[0]
            if leader_idxs.size > 0:
                last_idx = int(leader_idxs[-1])
                lx = float(device.x[last_idx])
                ly = float(device.y[last_idx])
                draw_leader_ring(ax, lx, ly, scale=1.25)
        except Exception:
            pass

    for target in targets:
        add_fading_line(ax, target.x, target.y, TARGET_COLOR, linewidth=2.2, min_alpha=0.02, max_alpha=0.48, linestyle="dashed", zorder=1)
        ax.scatter(target.final_x, target.final_y, marker="*", s=260, color=TARGET_COLOR, edgecolors="black", linewidths=0.7, zorder=5)
        ax.text(target.final_x, target.final_y + 0.45, f"T{target.entity_id}", ha="center", va="bottom", fontsize=9, color=TARGET_COLOR)

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
    # Compute a global set of equally-spaced sample times (integer ticks) so that
    # rings belonging to the same sampled time across different entities share
    # the same visual cue (color). This makes it easy to identify which drawn
    # circles correspond to the same snapshot in time.
    all_times = np.concatenate([d.time for d in [*devices, *targets, *obstacles] if len(d.time) > 0]) if any(
        len(d.time) > 0 for d in [*devices, *targets, *obstacles]
    ) else np.array([])
    if all_times.size == 0:
        # Nothing to draw
        finish_axes(ax, title, devices, targets, obstacles, legend_handles_margins(devices), output, dpi)
        return

    min_t = float(np.nanmin(all_times))
    max_t = float(np.nanmax(all_times))
    if margin_samples <= 0:
        sample_times = [int(round(min_t))]
    else:
        sample_times = np.unique(np.round(np.linspace(min_t, max_t, margin_samples))).astype(int).tolist()

    # Build a discrete colormap for sample times. Use viridis (blu-verde-giallo)
    # so progression is visually intuitive from cold->warm.
    cmap = plt.get_cmap("viridis", max(1, len(sample_times)))

    def find_nearest_index(times: np.ndarray, target: int) -> int:
        if times.size == 0:
            return -1
        return int(np.argmin(np.abs(times - float(target))))

    # Draw targets (trajectories) with dashed lines as before
    for target in targets:
        add_fading_line(ax, target.x, target.y, TARGET_COLOR, linewidth=1.8, min_alpha=0.15, max_alpha=0.52, linestyle="dashed", zorder=1)
        ax.scatter(target.final_x, target.final_y, marker="*", s=220, color=TARGET_COLOR, edgecolors="black", linewidths=0.7, zorder=5)

    # Draw devices: for each global sample time try to find the nearest point
    # of this device and draw a sampled safety-radius circle using a color
    # that is shared across all entities for that same snapshot time.
    for index, device in enumerate(devices):
        base_color = DEVICE_COLORS[index % len(DEVICE_COLORS)]
        add_fading_line(ax, device.x, device.y, base_color, linewidth=1.3, min_alpha=0.12, max_alpha=0.72, zorder=2)
        for s_idx, st in enumerate(sample_times):
            idx_found = find_nearest_index(device.time, st)
            if idx_found < 0:
                continue
            # Accept the nearest point only if it is reasonably close to the
            # sampled tick (times are integer ticks): allow a tolerance of 0.5
            if abs(device.time[idx_found] - st) > 0.5:
                continue
            progress = s_idx / max(len(sample_times) - 1, 1)
            color = cmap(s_idx)
            add_circle(
                ax,
                float(device.x[idx_found]),
                float(device.y[idx_found]),
                robot_margin_radius(float(device.safe_margin[idx_found])),
                color=color,
                alpha=0.08 + 0.14 * progress,
                zorder=3,
            )
            # if device was leader at this sampled tick, mark it with a small ring.
            # Keep past leader rings subtle, but make the latest sampled leader ring clear.
            try:
                if bool(device.is_leader[idx_found]):
                    is_latest_sample = s_idx == len(sample_times) - 1
                    draw_leader_ring(
                        ax,
                        float(device.x[idx_found]),
                        float(device.y[idx_found]),
                        scale=0.9 if is_latest_sample else 0.7,
                        color=LEADER_COLOR,
                        alpha=0.9 if is_latest_sample else 0.35,
                    )
            except Exception:
                pass
        ax.scatter(device.final_x, device.final_y, s=90, color=base_color, edgecolors="black", linewidths=0.8, zorder=6)
        ax.text(device.final_x, device.final_y, str(device.entity_id), ha="center", va="center", fontsize=8, color="white", zorder=7)

    # Draw obstacles sampled at the same global times. If there is little
    # variation across sampled states, draw just the final circles as before.
    for obstacle in obstacles:
        add_fading_line(ax, obstacle.x, obstacle.y, OBSTACLE_COLOR, linewidth=1.2, min_alpha=0.012, max_alpha=0.3, zorder=1)
        sampled_states = set()
        sampled_points = []  # (s_idx, idx_found)
        for s_idx, st in enumerate(sample_times):
            idx_found = find_nearest_index(obstacle.time, st)
            if idx_found < 0:
                continue
            if abs(obstacle.time[idx_found] - st) > 0.5:
                continue
            sampled_states.add((round(float(obstacle.x[idx_found]), 6), round(float(obstacle.y[idx_found]), 6), round(float(obstacle.radius[idx_found]), 6), round(float(obstacle.margin[idx_found]), 6)))
            sampled_points.append((s_idx, idx_found))

        if len(sampled_states) <= 1:
            add_circle(ax, obstacle.final_x, obstacle.final_y, float(obstacle.radius[-1] + obstacle.margin[-1]), OBSTACLE_MARGIN_COLOR, 0.24, 1)
            add_circle(ax, obstacle.final_x, obstacle.final_y, float(obstacle.radius[-1]), OBSTACLE_COLOR, 0.58, 2)
        else:
            for s_idx, idx_found in sampled_points:
                progress = s_idx / max(len(sample_times) - 1, 1)
                color = cmap(s_idx)
                x = float(obstacle.x[idx_found])
                y = float(obstacle.y[idx_found])
                radius = float(obstacle.radius[idx_found])
                margin = float(obstacle.margin[idx_found])
                add_circle(ax, x, y, radius + margin, color, 0.06 + 0.10 * progress, 1)
                add_circle(ax, x, y, radius, color, 0.08 + 0.16 * progress, 2)
        ax.scatter(obstacle.final_x, obstacle.final_y, marker="X", s=120, color=OBSTACLE_MARKER_COLOR, zorder=6)

    # Add a vertical colorbar on the right which maps color->time (ticks).
    # Use a ScalarMappable with Normalize over the sampled time range so that
    # the bar shows the continuous progression; ticks will be the integer
    # sample times so the user can read which color corresponds to which tick.
    if len(sample_times) > 0 and "multipleobstacles" not in title.lower():
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=sample_times[0], vmax=sample_times[-1]))
        sm.set_array([])
        cbar = fig.colorbar(sm, ax=ax, orientation="vertical", pad=0.02)
        # show only start and end labels on the colorbar (min and max time)
        cbar.set_label("Simulation time", rotation=270, labelpad=18)
        start_tick = int(sample_times[0])
        end_tick = int(sample_times[-1])
        cbar.set_ticks([start_tick, end_tick])
        cbar.set_ticklabels([str(start_tick), str(end_tick)])

        leader_change_time = first_two_to_one_leader_time(devices)
        if leader_change_time is not None and start_tick <= leader_change_time <= end_tick:
            cbar.ax.axhline(leader_change_time, color="red", linewidth=2.2)

    finish_axes(ax, title, devices, targets, obstacles, legend_handles_margins(devices), output, dpi)


def first_two_to_one_leader_time(devices: list[Trajectory]) -> float | None:
    leader_counts_by_time: dict[float, int] = {}

    for device in devices:
        for time, is_leader in zip(device.time, device.is_leader):
            rounded_time = float(round(float(time)))
            leader_counts_by_time.setdefault(rounded_time, 0)
            if bool(is_leader):
                leader_counts_by_time[rounded_time] += 1

    previous_count = None
    for time in sorted(leader_counts_by_time):
        current_count = leader_counts_by_time[time]
        if previous_count == 2 and current_count == 1:
            return time
        previous_count = current_count

    return None

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
        ax.scatter(obstacle.final_x, obstacle.final_y, marker="X", s=120, color=OBSTACLE_MARKER_COLOR, zorder=6)


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
    save_figure(fig, output, dpi)
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
        Line2D([0], [0], color=DEVICE_COLORS[0], lw=3, marker="o", markersize=9, label="Robot trajectories"),
        Line2D([0], [0], color=SAFE_COLOR, lw=2, marker="o", alpha=0.35, markersize=9, label="Final robot safety radius"),
        Line2D([0], [0], color=TARGET_COLOR, lw=2, ls="--", marker="*", markersize=12, label="Target trajectories"),
        Line2D(
            [0],
            [0],
            color=OBSTACLE_COLOR,
            lw=2,
            marker="X",
            markerfacecolor=OBSTACLE_MARKER_COLOR,
            markeredgecolor=OBSTACLE_MARKER_COLOR,
            markersize=9,
            label="Obstacle trajectories",
        ),
        Line2D([0], [0], color=OBSTACLE_MARGIN_COLOR, lw=6, alpha=0.35, label="Obstacle safety margin"),
    ]
    if len(devices) > 1:
        handles[0].set_label(f"Robot trajectories ({len(devices)})")
    # If any device has leader samples, add a legend handle for the leader ring
    try:
        if any(np.any(d.is_leader) for d in devices):
            handles.append(Line2D([0], [0], marker="o", color="none", markeredgecolor=LEADER_COLOR, markerfacecolor="none", markersize=12, linestyle="None", label="Leader"))
    except Exception:
        pass
    return handles


def legend_handles_margins(devices: list[Trajectory]) -> list[Line2D]:
    handles = legend_handles_clean(devices)
    handles[1].set_label("Sampled robot safety radii")
    handles[4].set_label("Sampled obstacle safety margins")
    return handles


def save_figure(fig: plt.Figure, output: Path, dpi: int) -> None:
    kwargs = {"bbox_inches": "tight"}
    if output.suffix.lower() == ".png":
        kwargs["dpi"] = dpi
    fig.savefig(output, **kwargs)


def output_paths(output_dir: Path, prefix: str, output_format: str) -> tuple[Path, Path]:
    experiment_output_dir = output_dir / prefix
    suffix = f".{output_format}"
    return experiment_output_dir / f"{prefix}_movement{suffix}", experiment_output_dir / f"{prefix}_movement_margins{suffix}"


def main() -> int:
    args = parse_args()
    configs = parse_configs(args.config, args.data_dir, args.title)

    for config in configs:
        prefix = args.output_prefix or config.data_dir.name.rstrip("/") or config.title

        try:
            devices = read_devices(config.data_dir, args.max_points)
            targets = read_targets(config.data_dir, args.max_points)
            obstacles = read_obstacles(config.data_dir, args.max_points)
        except Exception as error:
            print(f"Warning: skipping {config.title} ({config.data_dir}): {error}")
            continue

        clean_output, margins_output = output_paths(args.output_dir, prefix, args.output_format)

        draw_clean_movement(
            devices,
            targets,
            obstacles,
            clean_output,
            args.dpi,
            f"{beautify_experiment_title(config.title)} movement",
        )

        draw_margin_evolution(
            devices,
            targets,
            obstacles,
            margins_output,
            args.dpi,
            beautify_experiment_title(config.title),
            args.margin_samples,
        )

        print(f"Loaded {len(devices)} devices, {len(targets)} targets, {len(obstacles)} obstacles for {config.title}.")
        print(f"Wrote {clean_output}")
        print(f"Wrote {margins_output}")

    return 0


if __name__ == "__main__":
    #python3 plotting/plot_movement.py --config src/main/yaml/followLeader.yml
    raise SystemExit(main())
