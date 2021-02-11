#!/usr/bin/env bash
pacman=$(pacman -Qu)
yay=$(yay -Qu)
#pacman=5
#yay=5
if [ ${#pacman} -gt 0 ] || [ ${#yay} -gt 0 ] ; then
	all=$(( $pacman + $yay ))
else
	all=0
fi
echo $all 
