#!/usr/bin/env bash

# Add this script to your wm startup file.

DIR="$HOME/.config/polybar/hack"

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch the bar
polybar -q left_monitor -c "$DIR"/config.ini &
polybar -q right_monitor -c "$DIR"/config.ini &
