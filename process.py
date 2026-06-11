import subprocess
import os

if __name__ == '__main__':

    animation_script = "plotting/plot_animation.py"
    distances_script = "plotting/plot_distances.py"
    movement_script = "plotting/plot_movement.py"
    snapshots_script = "plotting/plot_snapshots.py"

    output_directory = "charts"
    os.makedirs(output_directory, exist_ok=True)

    snapshot_times = [str(value) for value in range(0, 81, 5)]

    processes = []

    process1 = subprocess.Popen(["python3", animation_script])
    processes.append(("animation", process1))
    print("Launched animation plotter script.")
    process2 = subprocess.Popen(["python3", distances_script])
    processes.append(("distances", process2))
    print("Launched distances plotter script.")
    process3 = subprocess.Popen(["python3", movement_script])
    processes.append(("movement", process3))
    print("Launched movement script.")
    process4 = subprocess.Popen(["python3", snapshots_script, *snapshot_times])
    processes.append(("snapshots", process4))
    print("Launched snapshots plotter.")

    print("All chart generator scripts have been launched.")

    failed_processes = []
    for name, process in processes:
        return_code = process.wait()
        if return_code != 0:
            failed_processes.append((name, return_code))

    if failed_processes:
        failures = ", ".join(f"{name} exited with code {return_code}" for name, return_code in failed_processes)
        print(f"All chart generator scripts have finished, but some failed: {failures}.")
    else:
        print("All chart generator scripts have finished successfully.")
