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

    process1 = subprocess.Popen(["python3", animation_script])
    print("Launched animation plotter script.")
    process2 = subprocess.Popen(["python3", distances_script])
    print("Launched distances plotter script.")
    process3 = subprocess.Popen(["python3", movement_script])
    print("Launched movement script.")
    process4 = subprocess.Popen(["python3", snapshots_script, *snapshot_times])
    print("Launched snapshots plotter.")

    print("All chart generator scripts have been launched.")