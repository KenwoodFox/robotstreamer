#!/bin/bash

#uncomment the next line to disable this command
#exit 0;
[ -e camcontrols.txt ] || ./getinfo.sh;
source camcontrols.txt;
./increment.sh sharpness;
v4l2-ctl -d "$device" -C sharpness;
