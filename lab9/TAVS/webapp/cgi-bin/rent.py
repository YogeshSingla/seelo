#!/usr/bin/python
import cgi

#add my module
import sys
sys.path.insert(0, '/home/kirito/TODO/seelo/lab9/TAVS/webapp/mymodule/')
import User

import io
import json
import os


PATH='/home/kirito/TODO/seelo/lab9/TAVS/webapp/mymodule/data_storage/'
FILENAME = 'bookings.json'
FILEPATH = PATH + FILENAME
u_id = 0


def form_to_json(form_data):
	#customer conversion function from passed form data to stored json data
	json_data = {}
	#modify the global u_id variable to allow value access to data_storage()
	global u_id
	u_id = form_data['driving_license_number'].value
	json_data[u_id] = {}
	json_data[u_id]['u_name'] = form_data['u_name'].value
	json_data[u_id]['driving_license_number'] = form_data['driving_license_number'].value
	json_data[u_id]['vehicle_booked'] = form_data['vehicle_booked'].value
	json_data[u_id]['aadhaar'] = form_data['aadhaar'].value
	json_data[u_id]['pickup_time'] = form_data['pickup_time'].value
	json_data[u_id]['return_time'] = form_data['return_time'].value
	
	return json_data

def data_storage(data):
	#store data in json format
	if (os.path.isfile(FILEPATH) and os.access(PATH, os.R_OK)):
		#print("File exists and is readable")
		bookings = json.loads(open(FILEPATH).read())
		if u_id in bookings:
			print("ERROR #2: Please return the booked vehicle.")
		else:
			with open(FILEPATH, 'a') as outfile:
				json.dump(data,outfile)

	else:
		print ("Either file is missing or is not readable, creating file...")
		with open(FILEPATH, 'w') as outfile:
			json.dump(data, outfile)

form = cgi.FieldStorage()
print('Content-type: text/html')
# parse form data
# plus blank line
html = """
<TITLE>rent</TITLE>
<H1>Successful</H1>
<HR>
<P>%s</P>
<HR>"""
if not 'vehicle_booked' in form:
	print(html % 'ERROR #1: Invalid Booking Request: Vehicle not found')
else:
	print(html % ('Sending Booking Request for:  %s.' % form['vehicle_booked'].value))

#print form



data = form_to_json(form)

data_storage(data)



