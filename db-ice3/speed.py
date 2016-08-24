#!/usr/bin/python3

from urllib.request import urlopen
import json
import sys
from time import sleep
from pprint import pprint




while True:
	msg = json.loads(urlopen("http://ice.portal2/api1/rs/status").read().decode("utf-8"))
	if "speed" in msg:
		print("Speed: {} km/h\n".format(msg["speed"]))
#	pprint(msg)
	sleep(1)



""" Messages: 
wget "http://ice.portal2/api1/rs/tripInfo" -O - 2>/dev/null 
wget "http://ice.portal2/api1/rs/status" -O - 2>/dev/null 
"""
