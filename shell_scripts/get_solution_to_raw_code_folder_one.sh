#!/bin/bash
sol_link="$1"
file_name="$2"
microsoft-edge "$sol_link" &
sleep 4
wmctrl -a thehive && xdotool mousemove 800 550 && sleep 0.5 && xdotool click 1 && sleep 0.5 && xdotool key Ctrl+a+c && sleep 0.2 && xdotool key Ctrl
xclip -o > "si_solutions/raw_code/$file_name.py"