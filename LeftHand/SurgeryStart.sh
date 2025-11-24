#!/bin/bash
cd ..

source ./venv1/bin/activate

rclone copy -P onedrive:'**fulldirectory/finalfolder**' /home/**rest_of_directory_to**/TargetLists

cd /home/**rest_of_directory_to**/Stereotaxiccontrol

git pull

# Pick one and uncomment it
# cd /RightHand
# cd /LeftHand

python StereotaxicUI.py

read -p "press enter to exit..."