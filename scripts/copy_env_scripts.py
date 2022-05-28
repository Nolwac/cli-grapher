"""
The scirpt copies the utility script for this project to the virtual environment script directory.
Warning: This script should only be called from the virtual environment
"""

import os
import shutil


def copy_files(filenames):
    env_path = os.environ["VIRTUAL_ENV"]
    destination_folder = f"{env_path}/Scripts"
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)  # creates destination folder if it does not already exist
    for filename in filenames:
        source = os.path.dirname(__file__) + f"/{filename}"  # the file to copy
        destination = f"{destination_folder}/{filename}"  # destination file
        # copy the file to the folder
        shutil.copy(source, destination)


if __name__ == "__main__":
    copy_files([])
