#!/usr/bin/env bash

STYLES_LIST=("transparent" "nordic" "angles")

style="nordic" ## Only used if, for some reason, function below doesn't work

function random_pick_from_list() {
	len_list=${#STYLES_LIST[@]}
	num=$(( $RANDOM % $len_list ))
	style=${STYLES_LIST[$num]}
}


random_pick_from_list


# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch the bar
polybar -q left_monitor -c "$HOME"/.config/polybar/$style/config.ini &
polybar -q right_monitor -c "$HOME"/.config/polybar/$style/config.ini & 
