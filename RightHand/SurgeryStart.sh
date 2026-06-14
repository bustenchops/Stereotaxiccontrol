#!/bin/bash
cd ..

source ./venv1/bin/activate

rclone copy -P onedrive:'Usask Job/Targetlists' /home/pi/TargetLists

cd /home/pi//Stereotaxiccontrol

git pull

# Pick one and uncomment it
RightHand
# cd /LeftHand

python StereotaxicUI.py

read -p "press enter to exit..."