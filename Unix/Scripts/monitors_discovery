#!/usr/bin/env bash
SetConfigLine() {
    ## Gets line to get best config from
    if [[ ${xrandrLines[$index]:1:1} == *":"* ]] ; then
        line=${xrandrLines[$index]:0:1}
    else
        line=${xrandrLines[$index]:0:2}
    fi
}

SetName() {
    name=$(echo ${xrandrLines[$index]} | awk '{ print $1 }' | awk -F: '{ print $2 }')
}

SetResolution() {
    resolution=$(echo ${monitorConfigs[$index]} | awk '{ print $1 }')
}

SetRate() {
    rate=$(echo ${monitorConfigs[$index]} | awk '{ print $3 }' | tr "*" " ")
    if [[ $rate == "+" ]] ; then
        rate=$(echo ${monitorConfigs[$index]} | awk '{ print $4 }' | tr "*" " ")
    fi
}

Main() {
    monitorConfigs=()
    commands=()
    mapfile -t xrandrLines < <( xrandr | grep -n "\bconnected\b" )
    for index in $(seq ${#xrandrLines[@]}) ; do
        index=$(( index -= 1 )) 
        SetConfigLine
        # Gets configs for monitor and keeps only lines needed
        monitorConfigs[$index]=$(xrandr | head -n $(( line + 1 )) | tail -n 1)
        SetName
        SetResolution
        SetRate
        echo "Name: $name"
        echo "Resolution: $resolution"
        echo "Refresh Rate: $rate"
        echo "-----"
        if [[ $index -eq 0 ]] ; then
            xrandr --output $name --mode $resolution --rate $rate
        else
            xrandr --output $name --mode $resolution --rate $rate --primary --left-of $lastMonitorName
        fi
        lastMonitorName=$name
    done
}

Main
