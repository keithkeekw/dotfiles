#!/bin/sh
picom --experimental-backend &
lxsession-default &
blueman-applet &
dropbox &
autorandr -c &
nitrogen --restore --set-scaled 
