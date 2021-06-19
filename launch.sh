#!/usr/bin/env bash

STYLE="transparent"

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch the bar
polybar -q left_monitor -c "$HOME"/.config/polybar/$STYLE/config.ini &
polybar -q right_monitor -c "$HOME"/.config/polybar/$STYLE/config.ini & 