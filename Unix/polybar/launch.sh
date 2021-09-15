#!/usr/bin/env bash

function start_polybar() {

	# Terminate already running bar instances
	killall -q polybar

	# Wait until the processes have been shut down
	while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

	# Launch the bar
	if [[ ! $2 == *"single"* ]] ; then
		polybar -q left_monitor -c "$HOME"/.config/polybar/$1/config.ini &
	fi
	polybar -q right_monitor -c "$HOME"/.config/polybar/$1/config.ini & 
	
}

if [ $1 ] ; then
	start_polybar $1 $2
fi
