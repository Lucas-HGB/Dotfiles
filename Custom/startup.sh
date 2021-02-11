#!/usr/bin/env bash
~/.config/polybar/launch.sh
nitrogen --restore &
flameshot &
rclone mount OneDrive:Coding ~/OneDrive/Coding &
rclone mount OneDrive:Documentos ~/OneDrive/Documentos &
rclone mount OneDrive:Important ~/OneDrive/Important
