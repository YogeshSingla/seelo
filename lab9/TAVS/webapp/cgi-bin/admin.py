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


def write_vehicle(v_id,data):
	isUpdated = False
	if (os.path.isfile(FILEPATH) and os.access(PATH, os.R_OK)):
		with open(FILEPATH, 'rt') as csvfile:
			read_obj = csv.reader(csvfile, delimiter = ',')
			for row in read_obj:
				if v_id != row[3]:
					data_list.append(row)
				else:
					data_list.append(data)
					isUpdated = True

		with open(FILEPATH, 'wt') as csvfile:
			write_obj = csv.writer(csvfile, delimiter = ',')	
			for row in data_list:
				write_obj.writerow(row)
		if not isUpdated:
			print("ERROR #5: Updated failed!")

	else:
		print("ERROR #6: Vehicle file missing.")



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
	<tr>
	<td>%s</td>
	<td>%s</td>
	<td>%s</td>
	<td>%s</td>
	<td>%s</td>
	<td>%s</td>
	<td>%s</td>
	<td>%s</td>
	<td>%s</td>
	<tr>
	"""%(rent,status,last_rent_time,vehicle_id,v_name.strip('\''),miles_run,cost_incurred,price,fuel_consumed)

	content_html = content_html + vehicle_html


html = """
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="/css/w3.css" />
<link rel="stylesheet" type="text/css" href="/css/style.css" />
<link rel="stylesheet" type="text/css" href="/css/rent.css" />
<link rel="stylesheet" type="text/css" href="/css/admin_table.css" />

</head>
<body>

<h2>Admin Panel</h2>

<table id="t01">
  <tr>
    <th>rent</th>
    <th>status</th>
    <th>last_rent_time</th>
    <th>vehicle_id</th>
    <th>v_name</th>
    <th>miles_run</th>
    <th>cost_incurred</th>
    <th>price</th>
    <th>fuel_consumed</th>
  </tr>
    %s
</table>


</body>
</html>

"""

print('Content-type: text/html')
print(html%content_html)
