import subprocess
import os
import sys

if __name__ == '__main__':

    animation_script = "plotting/plot_animation.py"
    distances_script = "plotting/plot_distances.py"
    movement_script = "plotting/plot_movement.py"
    snapshots_script = "plotting/plot_snapshots.py"

    output_directory = "charts"
    os.makedirs(output_directory, exist_ok=True)

    snapshot_times = [str(value) for value in range(0, 81, 5)]

    script_choices = {
        "A": ("animation", animation_script, []),
        "D": ("distances", distances_script, []),
        "M": ("movement", movement_script, []),
        "S": ("snapshots", snapshots_script, snapshot_times),
    }

    requested_choices = [arg.strip().upper() for arg in sys.argv[1:] if arg.strip()]
    if not requested_choices:
        selected_choices = ["A", "D", "M", "S"]
    else:
        selected_choices = []
        for choice in requested_choices:
            if choice in script_choices and choice not in selected_choices:
                selected_choices.append(choice)
            elif choice not in script_choices:
                print(f"Warning: ignored unknown selector '{choice}'. Use A, D, M, or S.")

        if not selected_choices:
            print("No valid selectors provided. Use A, D, M, or S, or omit arguments to run all scripts.")
            raise SystemExit(1)

    processes = []

    for choice in ["A", "D", "M", "S"]:
        if choice not in selected_choices:
            continue

        name, script, extra_args = script_choices[choice]
        process = subprocess.Popen(["python3", script, *extra_args])
        processes.append((name, process))
        print(f"Launched {name} plotter script.")

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
