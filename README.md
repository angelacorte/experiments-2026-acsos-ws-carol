# CAROL: Coordinated Aggregate Robotics with Online control Lyapunov and barrier functions

[![Kotlin](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fangelacorte%2Fcarol-experiments%2Fmaster%2Fgradle%2Flibs.versions.toml&query=%24.versions.kotlin&label=Kotlin&color=blue)](https://kotlinlang.org)
[![Collektive](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fangelacorte%2Fcarol-experiments%2Fmaster%2Fgradle%2Flibs.versions.toml&query=%24.versions.collektive&label=Collektive&color=purple)](https://github.com/Collektive/collektive)
[![CI/CD](https://github.com/angelacorte/carol-experiments/actions/workflows/dispatcher.yml/badge.svg?branch=master)](https://github.com/angelacorte/carol-experiments/actions/workflows/dispatcher.yml)
[![Gurobi](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fangelacorte%2Fcarol-experiments%2Fmaster%2Fgradle%2Flibs.versions.toml&query=%24.versions.gurobi&label=Gurobi&color=orange)](https://www.gurobi.com/)
[![Release](https://img.shields.io/github/v/release/angelacorte/carol-experiments?sort=semver)](https://github.com/angelacorte/carol-experiments/releases)
[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://github.com/angelacorte/carol-experiments)

**CAROL** is a fully distributed, multi-robot control framework written in Kotlin. It bridges the gap between **Aggregate Programming** (via the Collektive framework) and **Optimization-based Control** using Control Lyapunov Functions (CLFs) and Control Barrier Functions (CBFs).

By leveraging the **Alternating Direction Method of Multipliers (ADMM)**, CAROL allows a swarm of robots to negotiate safe and optimal trajectories in a fully distributed manner, ensuring goal convergence, obstacle avoidance, inter-robot collision avoidance, and communication range maintenance.



## ✨ Key Features

* **Distributed Consensus (ADMM)**: Solves coupled multi-agent Quadratic Programs (QPs) using local and pairwise micro-iterations, eliminating the need for a central coordinator.
* **Safety & Connectivity (CBFs)**:
    * *Obstacle Avoidance*: Hard constraints to dodge static environment hazards.
    * *Collision Avoidance*: Hard constraints to maintain a minimum safe distance between neighbors.
    * *Communication Range*: Soft constraints (with L1 penalty) to maintain network connectivity without causing solver freezing when physical boundaries force a split.
* **Goal Tracking (CLFs)**: Proportional nominal controllers paired with CLFs to ensure asymptotic convergence to target destinations.
* **Zero-Order Hold (ZOH) Discretization**: Exact discrete-time robustification of continuous-time dynamics, ensuring the QP solver remains strictly affine and mathematically sound.
* **Stateless Architecture**: Completely thread-safe and immutable constraint definitions, ready for parallelized processing and coroutines.

## Current experiments

Scenarios are under `src/main/yaml/` and have matching effects in `effects/`.

| Experiment | Brief description | YAML | Entrypoint | Active CBFs |
| --- | --- | --- | --- | --- |
| No obstacle, split targets | Two robot groups track two different targets in free space; focuses on coordination and collision/speed safety without obstacle constraints. | `noObstacle.yml` | `NoObstacleKt.noObstacleEntrypoint` | `MaxSpeedCBF`, `CollisionAvoidanceCBF` |
| Common moving target | All robots track one moving target while avoiding a static obstacle and preserving connectivity when possible. | `followTarget.yml` | `CommonTargetKt.commonTargetEntrypoint` | `ObstacleAvoidanceCBF`, `MaxSpeedCBF`, `CollisionAvoidanceCBF`, `CommunicationRangeCBF` |
| Leader-follower | A distributedly elected leader follows the target; neighbors follow the leader while respecting obstacle, collision, and range constraints. | `followLeader.yml` | `FollowLeaderKt.followLeaderEntrypoint` | `ObstacleAvoidanceCBF`, `MaxSpeedCBF`, `CollisionAvoidanceCBF`, `CommunicationRangeCBF` |
| Different targets | Robots are assigned different `TargetID` values and split toward separate goals with obstacle and pairwise safety constraints. | `differentTargets.yml` | `MultipleTargetsKt.multipleTargetEntrypoint` | `ObstacleAvoidanceCBF`, `MaxSpeedCBF`, `CollisionAvoidanceCBF` |

## 🏗️ Project Structure

```text
src/main/
├── yaml/                                   Alchemist simulation scenarios
└── kotlin/it/unibo/
    ├── alchemist/                          Custom Alchemist actions/effects
    └── collektive/
        ├── entrypoints/                    Scenario entrypoints (NoObstacle, FollowLeader, ...)
        ├── admm/                           ADMM state/core/objectives
        ├── control/                        CLF/CBF definitions and nominal control
        ├── alchemist/device/               Sensors + environment bridge + QP settings
        ├── solver/gurobi/                  Gurobi integration, constraints, license setup
        ├── mathutils/                      Vector and numeric utilities
        └── model/                          Domain models (Device, Target, Obstacle, ...)
```

## 🚀 Prerequisites

- JDK 17+ (project compiles on JVM 17).
- Gurobi Optimizer installed.
- A valid `gurobi.lic` license file.

### Gurobi license resolution

The runtime searches for license in this order:

1. `GRB_LICENSE_FILE` environment variable.
2. `GRB_LICENSE_FILE` JVM system property.
3. `~/Library/gurobi/gurobi.lic` (macOS default fallback).

If your license is not set globally, pass it explicitly to Gradle using an env variable.

```bash
GRB_LICENSE_FILE="/absolute/path/to/gurobi.lic" ./gradlew runNoObstacleGraphic
GRB_LICENSE_FILE="/absolute/path/to/gurobi.lic" ./gradlew runAllBatch
```

## 🛠️ Configuration and Usage

Common molecules/parameters used by entrypoints:

- `TargetID`: target to track for each robot.
- `MaxSpeed`: robot max speed bound.
- `SafeMargin`: robot safety margin (and obstacle margin where applicable).
- `ControlPeriodMS`: control loop period used by ADMM step execution.
- `PrimalTolerance` / `DualTolerance`: ADMM stopping tolerances.
- `CommunicationDistance`: required in scenarios using communication-range constraints (`followTarget`, `followLeader`).
- `RhoADMM` (default `10.0`)
- `RhoResidual` (default `0.5`)
- `RhoSlack` (default `2.0`)
- `LogEnabled` (default `false`)

Base environment/scheduler values are defined in each YAML `variables` section (`timeDistribution`, network distance, obstacle radius/margin, trigger times, etc.).

### Running the Simulation
Ensure your Gurobi license is properly set up.
Run one scenario (examples):

```bash
./gradlew runFollowTargetGraphic
```

Gradle auto-generates `run<Name>Graphic` tasks from every `.yml` file in `src/main/yaml/`.

## 🧪 Mathematical Details

The control model is discrete-time with zero-order hold (ZOH):

```text
p(k+1) = p(k) + Delta_t * u(k)
```

At each control step, each robot solves a local QP that keeps control close to a nominal command while enforcing safety and consensus terms. A simplified objective is:

```text
min_u,s   ||u - u_nom||^2 + rho_slack * ||s||_1 + ADMM augmented terms
```

- CLF terms push the state toward the assigned target (goal convergence).
- CBF terms impose forward-invariance-style inequalities for safety (speed, obstacle, and pairwise collision limits).
- Communication range (when enabled) is relaxed via slack `s` to degrade gracefully instead of making the QP infeasible.

ADMM terminates when primal and dual residuals are below `PrimalTolerance` and `DualTolerance` (per robot molecules), or when scenario iteration/time limits are reached.
