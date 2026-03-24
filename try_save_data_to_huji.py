import os
import shutil

_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

folder_name= "exp_01_09_2025"
folder_path = os.path.join(os.getcwd(), "experiments",folder_name)
remote_folder = os.environ.get("DMTS_REMOTE_FOLDER", os.path.join(_PROJECT_ROOT, "remote_upload"))
try:
    src = folder_path
    dst = os.path.join(remote_folder, os.path.basename(src))
    shutil.copytree(src, dst, dirs_exist_ok=True)
    print("data updated")

except PermissionError:
    print("PermissionError")
except FileNotFoundError:
    print("FileNotFoundError")
except Exception as e:
    print(f"Exception: {e}")
