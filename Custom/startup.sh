#!/usr/bin/env bash
. ~/.config/polybar/launch.sh ## Sources polybar launch script, which contains function to start polybar

function pick_random_wallpaper() {
	len_list=${#WALLPAPERS[@]}
	num=$(( $RANDOM % $len_list ))
	chosen_wallpaper=${WALLPAPERS[$num]}
	chosen_wallpaper="$wallpapers_folder/$chosen_wallpaper"
}

function pick_random_style() {
	len_list=${#STYLES_LIST[@]}
	num=$(( $RANDOM % $len_list ))
	style=${STYLES_LIST[$num]}
}

STYLES_LIST=("angles" "blocks" "hack" "nordic" "transparent")
style="blocks" # Fallback value

wallpapers_folder="/media/Storage/Pictures/Wallpapers"
chosen_wallpaper="./wallpaper" # Only used if wallpaper is set via styli
mapfile -t WALLPAPERS < <( /usr/bin/ls $wallpapers_folder ) # Creates list with wallpapers found in folder

if [ $(( $RANDOM % 3 )) -eq 0 ] ; then
	pick_random_wallpaper
	feh "$chosen_wallpaper" --bg-scale --no-xinerama &
else
	echo "Downloading Wallpaper"
	styli -w 4480 -h 1080 -c --no-xinerama &
fi

pick_random_style # If uncommented, will choose random style from above list
start_polybar $style & # Starts polybar, passing style as arg
~/.config/polybar/$style/scripts/pywal.sh "$chosen_wallpaper" & # 
# Sets polybar color-scheme to wallpaper color-scheme, if pywal is available for such theme
flameshot 
