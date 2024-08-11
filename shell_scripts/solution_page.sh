xdotool getmouselocation
xdotool mousemove 1200 600
wmctrl -r <window_spec> -e <action>
# <MVARG> = [x, y, width, height]

wmctrl -r thehive -e "0,945,0,990,1070"
xdotool mousemove 1400 600 && xdotool click 1
xdotool key Ctrl+a && xdotool key Ctrl+c
xclip -o > file.txt

