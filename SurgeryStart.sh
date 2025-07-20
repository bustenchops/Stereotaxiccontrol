#!/bin/bash

rclone copy onedrive:'Usask Job/Targetlists' /home/bustenchops/TargetLists

cd /home/bustenchops/Stereotaxiccontrol

git pull

python StereotaxicUI.py
