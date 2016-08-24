#!/usr/bin/python3

import sys
from time import sleep,time
from urllib.request import urlopen
import json

from pprint import pprint

first = True

#log_name = "rj.log"

#log = open(log_name,"a")

while True:

	pos_url = "http://cdwifi.cz/portal/api/vehicle/realtimes/0?locale=cs_CZ&distances=km&temperatures=c"
	route_url = "http://cdwifi.cz/portal/api/timetable/connexion/current?locale=cs_CZ"

	pos = json.loads(urlopen(pos_url).read().decode("utf-8"))

	print("Speed: {} km/h\n".format(pos["speed"]))
	sleep(1)
	
#	log.write("{},{},{}\n".format(time(),pos["gpsLat"],pos["gpsLng"]))
#	log.flush()

	if not first:
		continue

	route = json.loads(urlopen(route_url).read().decode("utf-8"))
	first = False
	with open("pos.json","w") as posf:
		json.dump(pos,posf)
	with open("route.json","w") as posf:
		json.dump(route,posf)

