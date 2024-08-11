wmctrl -a meta && sleep 0.1 && xdotool key g key i && sleep 0.1 && xdotool key --repeat 2 BackSpace
wmctrl -a meta && sleep 0.1 && xdotool key g+i && sleep 0.1 && xdotool key --repeat 2 BackSpace && xdotool key ctrl+v
xclip -selection clipboard -f < /path/to/file && xdotool key ctrl+v

wmctrl -a thehive && sleep 0.05 && xdotool key --delay 50 f+s+a && sleep 0.05 && xdotool key Ctrl+s
wmctrl -a all files && sleep 0.05 && xdotool type "hive_file_mhtml" && xdotool key Return
wmctrl - c thehive

