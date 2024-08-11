wmctrl -a meta && sleep 0.1 && xdotool key g key i && sleep 0.1 && xdotool key --repeat 2 BackSpace
wmctrl -a meta && sleep 0.1 && xdotool key g+i && sleep 0.1 && xdotool key --repeat 2 BackSpace && xdotool key ctrl+v
xclip -selection clipboard -f < /path/to/file && xdotool key ctrl+v

