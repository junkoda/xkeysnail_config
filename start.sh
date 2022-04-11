#!/usr/bin/env bash
#exec >> $HOME/.xkeysnail/stdout.log 2>&1

#xhost +SI:localuser:xkeysnail
#sudo -u xkeysnail DISPLAY=$DISPLAY /usr/local/bin/xkeysnail -q $HOME/.xkeysnail/config.py &

#xkeysnail=/home/junkoda/.local/bin/xkeysnail
#xkeysnail=xkeysnail

#sudo DISPLAY=$DISPLAY $xkeysnail
#xhost +SI:localuser:root
#xkeysnail -q /home/junkoda/.xkeysnail/config.py &

xhost +SI:localuser:root
sudo xkeysnail -q $HOME/.xkeysnail/config.py &
