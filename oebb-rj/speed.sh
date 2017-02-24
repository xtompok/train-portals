#!/bin/bash

while true
do
	wget "http://railnet.oebb.at/api/speed" -O - 2>/dev/null
	echo " km/h"
	sleep 5
done
