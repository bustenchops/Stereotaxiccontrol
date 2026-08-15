#!/bin/bash
cd ..

source ./venv1/bin/activate

rclone copy -P onedrive:'/Usask Job/Targetlists' /home/lhm403/TargetLists

cd /home/lhm403/Stereotaxiccontrol

git pull

# Pick one and uncomment it
cd RightHand
# cd /LeftHand

python StereotaxicUI.py

read -p "press enter to exit..."