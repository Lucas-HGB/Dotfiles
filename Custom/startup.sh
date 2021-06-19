#!/usr/bin/env bash
num=$(( $RANDOM % 4 ))
if [ $num -gt 1 ] ; then
	styli -w 4480 -h 1080 -c --no-xinerama
	~/.config/polybar/pywal.sh ./wallpaper
else
	feh --random /media/Storage/Pictures/Wallpapers --bg-scale --no-xinerama &
fi
flameshot 
