#!/usr/bin/env python3
"""Plot minimum and maximum pairwise distances between devices over time."""

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
import numpy as np
from matplotlib.lines import Line2D

from plot_palette import COMM_COLOR, DEVICE_COLORS, ROBOT_COLOR, SAFE_COLOR

DISTANCE_COLOR = ROBOT_COLOR
SAFE_MARGIN_COLOR = SAFE_COLOR
COMMUNICATION_COLOR = COMM_COLOR
DISTANCE_SCOPE = "after-communication"


@dataclass(frozen=True)
class ExperimentConfig:
    data_dir: Path
    title: str
    connect_within_distance: float | None
    robot_safe_margin: float | None
    max_comm_distance: float | None


@dataclass(frozen=True)
class DeviceTrajectory:
    entity_id: int
    time: np.ndarray
    x: np.ndarray
    y: np.ndarray
    safe_margin: np.ndarray
    comm_distance: np.ndarray


@dataclass(frozen=True)
class DistanceSeries:
    time: np.ndarray
    d_inf: np.ndarray
    d_sup: np.ndarray
    safe_margin: np.ndarray
    comm_distance: np.ndarray


@dataclass(frozen=True)
class PerDeviceDistanceSeries:
    time: np.ndarray
    d_inf_by_device: dict[int, np.ndarray]
    d_sup_by_device: dict[int, np.ndarray]
    safe_margin: np.ndarray
    comm_distance: np.ndarray


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Plot pairwise device distances over simulation time. It writes one chart for "
            "d_inf=min_ij ||p_i-p_j|| and one chart for d_sup=max_ij ||p_i-p_j||."
        )
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src/main/yaml"),
        help="Experiment name, YAML path, or directory containing YAML experiments. Defaults to src/main/yaml.",
    )
    parser.add_argument("--data-dir", type=Path, default=None, help="Directory containing positions_node-*.csv files.")
    parser.add_argument("--output-dir", type=Path, default=Path("charts/distances"), help="Output directory.")
    parser.add_argument("--output-prefix", default=None, help="Filename prefix. Defaults to the data directory name.")
    parser.add_argument("--title", default=None, help="Plot title. Defaults to YAML stem or data directory name.")
    parser.add_argument("--max-points", type=int, default=2500, help="Maximum plotted time samples after downsampling.")
    parser.add_argument("--dpi", type=int, default=220, help="Output image DPI.")
    parser.add_argument(
        "--output-format",
        choices=("pdf", "png"),
        default="pdf",
        help="Output format. Defaults to pdf; choose png to save only PNG files.",
    )
    parser.add_argument("--png", action="store_const", const="png", dest="output_format", help="Save only PNG files.")
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


def read_device(path: Path, config: ExperimentConfig) -> DeviceTrajectory:
    rows: list[dict[str, str]] = []
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if not rows:
        raise ValueError(f"{path}: empty CSV")

    def as_float(row: dict[str, str], column: str, default: float = 0.0) -> float:
        value = row.get(column)
        if value in (None, ""):
            return default
        return float(value)

    device_id = int(as_float(rows[0], "nodeId", parse_id(path)))
    safe_default = config.robot_safe_margin or 0.0
    comm_default = config.max_comm_distance or 0.0

    return DeviceTrajectory(
        entity_id=device_id,
        time=np.array([float(round(as_float(row, "time"))) for row in rows], dtype=float),
        x=np.array([as_float(row, "X") for row in rows], dtype=float),
        y=np.array([as_float(row, "Y") for row in rows], dtype=float),
        safe_margin=np.array([as_float(row, "safeMargin", safe_default) for row in rows], dtype=float),
        comm_distance=np.array([as_float(row, "commDistance", comm_default) for row in rows], dtype=float),
    )


def read_devices(config: ExperimentConfig) -> list[DeviceTrajectory]:
    devices = [read_device(path, config) for path in sorted(config.data_dir.glob("positions_node-*.csv"), key=sort_key)]
    if len(devices) < 2:
        raise FileNotFoundError(f"Need at least two positions_node-*.csv files in {config.data_dir}")
    return devices


def trajectory_by_time(device: DeviceTrajectory) -> dict[float, tuple[float, float, float, float]]:
    return {
        time: (float(x), float(y), float(safe_margin), float(comm_distance))
        for time, x, y, safe_margin, comm_distance in zip(
            device.time,
            device.x,
            device.y,
            device.safe_margin,
            device.comm_distance,
        )
    }


def compute_distances(
    devices: list[DeviceTrajectory],
    config: ExperimentConfig,
    distance_scope: str,
) -> DistanceSeries:
    by_device = [trajectory_by_time(device) for device in devices]
    common_times = sorted(set.intersection(*(set(device.keys()) for device in by_device)))
    if not common_times:
        raise ValueError("Device CSV files do not share any common simulation time.")

    times: list[float] = []
    min_distances: list[float] = []
    max_distances: list[float] = []
    safe_thresholds: list[float] = []
    comm_thresholds: list[float] = []

    active_pairs: set[tuple[int, int]] = set()

    for time in common_times:
        samples = [device[time] for device in by_device]
        pair_distances = []
        pair_safe_thresholds = []
        pair_comm_thresholds = []
        for left_index, left in enumerate(samples):
            for right_index, right in enumerate(samples[left_index + 1 :], start=left_index + 1):
                distance = math.dist((left[0], left[1]), (right[0], right[1]))
                pair = (left_index, right_index)
                if can_communicate(distance, config):
                    active_pairs.add(pair)
                if not include_pair(pair, distance_scope, active_pairs):
                    continue
                pair_distances.append(distance)
                pair_safe_thresholds.append(max(left[2], right[2]))
                pair_comm_thresholds.append(min_positive(left[3], right[3]))

        times.append(time)
        min_distances.append(min(pair_distances) if pair_distances else float("nan"))
        max_distances.append(max(pair_distances) if pair_distances else float("nan"))
        safe_thresholds.append(
            config.robot_safe_margin
            if config.robot_safe_margin is not None
            else (max(pair_safe_thresholds) if pair_safe_thresholds else 0.0)
        )
        comm_thresholds.append(
            config.max_comm_distance
            if config.max_comm_distance is not None
            else (max(pair_comm_thresholds) if pair_comm_thresholds else 0.0)
        )

    return DistanceSeries(
        time=np.array(times, dtype=float),
        d_inf=np.array(min_distances, dtype=float),
        d_sup=np.array(max_distances, dtype=float),
        safe_margin=np.array(safe_thresholds, dtype=float),
        comm_distance=np.array(comm_thresholds, dtype=float),
    )


def compute_per_device_distances(
    devices: list[DeviceTrajectory],
    config: ExperimentConfig,
    distance_scope: str,
) -> PerDeviceDistanceSeries:
    by_device = [trajectory_by_time(device) for device in devices]
    common_times = sorted(set.intersection(*(set(device.keys()) for device in by_device)))
    if not common_times:
        raise ValueError("Device CSV files do not share any common simulation time.")

    d_inf_by_device: dict[int, list[float]] = {device.entity_id: [] for device in devices}
    d_sup_by_device: dict[int, list[float]] = {device.entity_id: [] for device in devices}
    safe_thresholds: list[float] = []
    comm_thresholds: list[float] = []

    active_pairs: set[tuple[int, int]] = set()

    for time in common_times:
        samples = [device[time] for device in by_device]
        pair_distances_by_device: dict[int, list[float]] = {device.entity_id: [] for device in devices}

        for left_index, left in enumerate(samples):
            for right_index, right in enumerate(samples[left_index + 1 :], start=left_index + 1):
                distance = math.dist((left[0], left[1]), (right[0], right[1]))
                pair = (left_index, right_index)
                if can_communicate(distance, config):
                    active_pairs.add(pair)
                if not include_pair(pair, distance_scope, active_pairs):
                    continue
                pair_distances_by_device[devices[left_index].entity_id].append(distance)
                pair_distances_by_device[devices[right_index].entity_id].append(distance)

        for index, sample in enumerate(samples):
            device_id = devices[index].entity_id
            distances = pair_distances_by_device[device_id]
            d_inf_by_device[device_id].append(min(distances) if distances else float("nan"))
            d_sup_by_device[device_id].append(max(distances) if distances else float("nan"))

        safe_values = [sample[2] for sample in samples]
        comm_values = [sample[3] for sample in samples if sample[3] > 0]
        safe_thresholds.append(config.robot_safe_margin if config.robot_safe_margin is not None else max(safe_values))
        comm_thresholds.append(config.max_comm_distance if config.max_comm_distance is not None else (min(comm_values) if comm_values else 0.0))

    return PerDeviceDistanceSeries(
        time=np.array(common_times, dtype=float),
        d_inf_by_device={device_id: np.array(values, dtype=float) for device_id, values in d_inf_by_device.items()},
        d_sup_by_device={device_id: np.array(values, dtype=float) for device_id, values in d_sup_by_device.items()},
        safe_margin=np.array(safe_thresholds, dtype=float),
        comm_distance=np.array(comm_thresholds, dtype=float),
    )


def min_positive(left: float, right: float) -> float:
    positives = [value for value in (left, right) if value > 0]
    return min(positives) if positives else 0.0


def can_communicate(distance: float, config: ExperimentConfig) -> bool:
    return config.connect_within_distance is None or distance <= config.connect_within_distance


def include_pair(pair: tuple[int, int], distance_scope: str, active_pairs: set[tuple[int, int]]) -> bool:
    if distance_scope == "after-communication":
        return pair in active_pairs
    raise ValueError(f"Unknown distance scope: {distance_scope}")


def downsample_series(series: DistanceSeries, max_points: int) -> DistanceSeries:
    if max_points <= 0 or len(series.time) <= max_points:
        return series
    indexes = np.unique(np.linspace(0, len(series.time) - 1, max_points, dtype=int))
    return DistanceSeries(
        time=series.time[indexes],
        d_inf=series.d_inf[indexes],
        d_sup=series.d_sup[indexes],
        safe_margin=series.safe_margin[indexes],
        comm_distance=series.comm_distance[indexes],
    )


def downsample_per_device_series(series: PerDeviceDistanceSeries, max_points: int) -> PerDeviceDistanceSeries:
    if max_points <= 0 or len(series.time) <= max_points:
        return series
    indexes = np.unique(np.linspace(0, len(series.time) - 1, max_points, dtype=int))
    return PerDeviceDistanceSeries(
        time=series.time[indexes],
        d_inf_by_device={device_id: values[indexes] for device_id, values in series.d_inf_by_device.items()},
        d_sup_by_device={device_id: values[indexes] for device_id, values in series.d_sup_by_device.items()},
        safe_margin=series.safe_margin[indexes],
        comm_distance=series.comm_distance[indexes],
    )


def threshold_label(values: np.ndarray, name: str) -> str:
    finite = values[np.isfinite(values)]
    positive = finite[finite > 0]
    if positive.size == 0:
        return name
    if np.allclose(positive, positive[0]):
        return f"{name} = {positive[0]:g}"
    return name


def draw_distance_chart(
    time: np.ndarray,
    distance: np.ndarray,
    threshold: np.ndarray,
    output: Path,
    dpi: int,
    title: str,
    ylabel: str,
    threshold_name: str,
    threshold_color: str,
) -> None:
    fig, ax = plt.subplots(figsize=(11, 6), constrained_layout=True)
    ax.plot(time, distance, color=DISTANCE_COLOR, linewidth=2.2, label=ylabel)

    positive_threshold = threshold[threshold > 0]
    if positive_threshold.size > 0:
        if np.allclose(positive_threshold, positive_threshold[0]):
            ax.axhline(
                float(positive_threshold[0]),
                color=threshold_color,
                linewidth=1.8,
                linestyle="--",
                label=threshold_label(threshold, threshold_name),
            )
        else:
            ax.plot(
                time,
                threshold,
                color=threshold_color,
                linewidth=1.8,
                linestyle="--",
                label=threshold_name,
            )

    ax.set_title(title, fontsize=18, pad=12)
    ax.set_xlabel("simulation time")
    ax.set_ylabel("distance")
    ax.grid(True, color="#e4e4e4", linewidth=0.8)
    ax.legend(loc="best", frameon=True, fontsize=12)
    ax.set_xlim(float(np.nanmin(time)), float(np.nanmax(time)))
    ax.set_ylim(bottom=0)
    for spine in ax.spines.values():
        spine.set_edgecolor("black")
        spine.set_linewidth(1.4)

    output.parent.mkdir(parents=True, exist_ok=True)
    save_figure(fig, output, dpi)
    plt.close(fig)


def scope_title(distance_scope: str) -> str:
    if distance_scope == "after-communication":
        return "after first communication"
    return distance_scope


def formula_scope(distance_scope: str) -> str:
    if distance_scope == "after-communication":
        return r"i,j \in A(t)"
    return "i,j"


def draw_per_device_distance_chart(
    time: np.ndarray,
    distances_by_device: dict[int, np.ndarray],
    threshold: np.ndarray,
    output: Path,
    dpi: int,
    title: str,
    threshold_name: str,
    threshold_color: str,
) -> None:
    fig, ax = plt.subplots(figsize=(11, 6), constrained_layout=True)

    for index, device_id in enumerate(sorted(distances_by_device)):
        ax.plot(
            time,
            distances_by_device[device_id],
            color=DEVICE_COLORS[index % len(DEVICE_COLORS)],
            linewidth=2.0,
            label=f"robot {device_id}",
        )

    positive_threshold = threshold[threshold > 0]
    if positive_threshold.size > 0:
        if np.allclose(positive_threshold, positive_threshold[0]):
            ax.axhline(
                float(positive_threshold[0]),
                color=threshold_color,
                linewidth=1.8,
                linestyle="--",
                label=threshold_label(threshold, threshold_name),
            )
        else:
            ax.plot(
                time,
                threshold,
                color=threshold_color,
                linewidth=1.8,
                linestyle="--",
                label=threshold_name,
            )

    ax.set_title(title, fontsize=18, pad=12)
    ax.set_xlabel("simulation time")
    ax.set_ylabel("distance")
    ax.grid(True, color="#e4e4e4", linewidth=0.8)
    ax.legend(loc="best", frameon=True, fontsize=12)
    ax.set_xlim(float(np.nanmin(time)), float(np.nanmax(time)))
    ax.set_ylim(bottom=0)
    for spine in ax.spines.values():
        spine.set_edgecolor("black")
        spine.set_linewidth(1.4)

    output.parent.mkdir(parents=True, exist_ok=True)
    save_figure(fig, output, dpi)
    plt.close(fig)


def save_figure(fig: plt.Figure, output: Path, dpi: int) -> None:
    kwargs = {"bbox_inches": "tight"}
    if output.suffix.lower() == ".png":
        kwargs["dpi"] = dpi
    fig.savefig(output, **kwargs)


def output_paths(output_dir: Path, prefix: str, output_format: str) -> tuple[Path, Path, Path, Path]:
    experiment_output_dir = output_dir / prefix
    suffix = f".{output_format}"
    return (
        experiment_output_dir / f"{prefix}_distance_inf{suffix}",
        experiment_output_dir / f"{prefix}_distance_sup{suffix}",
        experiment_output_dir / f"{prefix}_distance_inf_by_device{suffix}",
        experiment_output_dir / f"{prefix}_distance_sup_by_device{suffix}",
    )


def main() -> int:
    args = parse_args()
    configs = parse_configs(args.config, args.data_dir, args.title)

    for config in configs:
        prefix = args.output_prefix or config.data_dir.name.rstrip("/") or config.title
        try:
            devices = read_devices(config)
        except Exception as error:
            print(f"Warning: skipping {config.title} ({config.data_dir}): {error}")
            continue

        print(f"Loaded {len(devices)} devices for {config.title}.")

        try:
            series = downsample_series(compute_distances(devices, config, DISTANCE_SCOPE), args.max_points)
            per_device_series = downsample_per_device_series(
                compute_per_device_distances(devices, config, DISTANCE_SCOPE),
                args.max_points,
            )
        except Exception as error:
            print(f"Warning: skipping {config.title}: {error}")
            continue

        inf_output, sup_output, inf_by_device_output, sup_by_device_output = output_paths(
            args.output_dir,
            prefix,
            args.output_format,
        )
        draw_distance_chart(
            series.time,
            series.d_inf,
            series.safe_margin,
            inf_output,
            args.dpi,
            f"{config.title} minimum {scope_title(DISTANCE_SCOPE)} distance",
            rf"$d_{{inf}}(t) = \min_{{{formula_scope(DISTANCE_SCOPE)}}}\|p_i - p_j\|$",
            "safe margin",
            SAFE_MARGIN_COLOR,
        )
        draw_distance_chart(
            series.time,
            series.d_sup,
            series.comm_distance,
            sup_output,
            args.dpi,
            f"{config.title} maximum {scope_title(DISTANCE_SCOPE)} distance",
            rf"$d_{{sup}}(t) = \max_{{{formula_scope(DISTANCE_SCOPE)}}}\|p_i - p_j\|$",
            "max communication radius",
            COMMUNICATION_COLOR,
        )
        draw_per_device_distance_chart(
            per_device_series.time,
            per_device_series.d_inf_by_device,
            per_device_series.safe_margin,
            inf_by_device_output,
            args.dpi,
            f"{config.title} minimum {scope_title(DISTANCE_SCOPE)} distance by robot",
            "safe margin",
            SAFE_MARGIN_COLOR,
        )
        draw_per_device_distance_chart(
            per_device_series.time,
            per_device_series.d_sup_by_device,
            per_device_series.comm_distance,
            sup_by_device_output,
            args.dpi,
            f"{config.title} maximum {scope_title(DISTANCE_SCOPE)} distance by robot",
            "max communication radius",
            COMMUNICATION_COLOR,
        )

        print(f"Wrote {inf_output}")
        print(f"Wrote {sup_output}")
        print(f"Wrote {inf_by_device_output}")
        print(f"Wrote {sup_by_device_output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
