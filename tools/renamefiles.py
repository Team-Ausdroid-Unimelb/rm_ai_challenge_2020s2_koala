import os
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Installing GitPython with pip.
install("gitpython")

import git

# Get the root path of the repo.
repo = git.Repo('.', search_parent_directories=True)
# print(repo.working_tree_dir)

from pathlib import Path

armour_path = Path(repo.working_tree_dir) / "src" / "images" / "200-249" / "red1 200-249 armour" / "obj_train_data"

pose_path = Path(repo.working_tree_dir) / "src" / "images" / "200-249" / "red1 200-249 pose" / "obj_train_data"

#Rename files.
for file in os.listdir(armour_path):
	os.rename(armour_path / file, armour_path / f"red_1_{file}")

for file in os.listdir(pose_path):
	os.rename(pose_path / file, pose_path / f"red_1_{file}")
