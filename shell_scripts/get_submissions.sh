#!/bin/bash
problem_link="$1"
microsoft-edge "$problem_link" &
sleep 6
wmctrl -a thehive && xdotool mousemove --sync 240 290 && xdotool click 1 && sleep 1 && xdotool key Ctrl+s && sleep 1 && xdotool key --clearmodifiers space
wmctrl -a all files && sleep 1 && xdotool type "hive_file_mhtml" && xdotool key Return && xdotool key Ctrl
sleep 2.5
wmctrl -c thehive

