#!/bin/sh
picom --experimental-backend &
lxsession-default &
blueman-applet &
dropbox &
autorandr -c &
sleep 3 & 
nitrogen --restore 
