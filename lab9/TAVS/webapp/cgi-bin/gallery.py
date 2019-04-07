#!/usr/bin/python

"""
This script helps display entire gallery programmatically
"""

#add my module
import sys
sys.path.insert(0, '/home/kirito/TODO/seelo/lab9/TAVS/webapp/mymodule/')
import os
import csv

import FleetVehicle

PATH='/home/kirito/TODO/seelo/lab9/TAVS/webapp/mymodule/data_storage/'
FILENAME = 'fleet_vehicles.csv'
FILEPATH = PATH + FILENAME
v_id = 0


def read_vehicle():
	#read from persistent storage
	if (os.path.isfile(FILEPATH) and os.access(PATH, os.R_OK)):
		data_list = []
		with open(FILEPATH, 'rt') as csvfile:
			read_obj = csv.reader(csvfile, delimiter = ',')
			for row in read_obj:
				data_list.append(row)
		return data_list
	else:
		print ("ERROR#4: Either file is missing or is not readable, Please ask admin to add vehicles first")
		return [0]*12



vehicles = read_vehicle()


content_html = """ """

for vehicle in vehicles:
	rent = vehicle[0]
	status = vehicle[1]
	last_rent_time = vehicle[2]
	vehicle_id = vehicle[3]
	isAC = vehicle[4]
	v_name = vehicle[5]
	miles_run = vehicle[6]
	cost_incurred = vehicle[7]
	price = vehicle[8]
	fuel_consumed = vehicle[9]
	isOwned = vehicle[10]
	photo_name = vehicle[11]

	print(photo_name)

	vehicle_html = """
	<div class="gallery">
	<a target="_blank" href="/images/vehicles/%s">
	<img src="/images/vehicles/%s" alt="%s" width="600" height="400">
	</a>
	<div class="desc">%s
	<hr>
	Rs %s /hour</div>
	</div>
	"""%(photo_name.strip('\''),photo_name.strip('\''),v_name.strip('\''),v_name.strip('\''),rent)

	content_html = content_html + vehicle_html


html = """
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="/css/w3.css" />
<link rel="stylesheet" type="text/css" href="/css/style.css" />
<link rel="stylesheet" type="text/css" href="/css/rent.css" />

<title>Rent</title>
</head>

<body>
  <div>
%s
<br>
<br>
<br>


</div>
</body>
</html> 

"""

print('Content-type: text/html')
print(html%content_html)
