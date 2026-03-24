#!/usr/bin/env python3
import sys
import os
import subprocess

print("[RestartScript] Starting restart process...")
print("[RestartScript] Current working directory:", os.getcwd())

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
print("[RestartScript] Script directory:", current_dir)
print("[RestartScript] Python interpreter:", sys.executable)

experiment_path = os.path.join(current_dir, "experiment.py")
if os.path.exists(experiment_path):
    print("[RestartScript] Found experiment.py at:", experiment_path)
else:
    print("[RestartScript] ERROR: experiment.py not found at:", experiment_path)
    sys.exit(1)

exp_name = os.environ.get("DMTS_RESTART_EXPERIMENT", "exp_27_08_2025")
print("Restarting experiment automatically...")
print(f"Experiment name: {exp_name}")

cmd = [sys.executable, experiment_path, "--restart", exp_name]
print("[RestartScript] Running:", " ".join(cmd))

os.chdir(current_dir)
result = subprocess.run(cmd, cwd=current_dir).returncode
print(f"[RestartScript] Command completed with result: {result}")
