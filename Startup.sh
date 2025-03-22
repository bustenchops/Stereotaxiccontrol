#!/bin/bash

rclone copy onedrive:'Usask Job/Targetlists' /home/bustenchops/Stereotaxiccontrol/TargetLists

cd /home/bustenchops/Videos

git pull
