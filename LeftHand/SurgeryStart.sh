#!/bin/bash

rclone copy onedrive:'Usask Job/Targetlists' /home/bustenchops/TargetLists -P

cd /home/bustenchops/Stereotaxiccontrol

git pull

python StereotaxicUI.py
