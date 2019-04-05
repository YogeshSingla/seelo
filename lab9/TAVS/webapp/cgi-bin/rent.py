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
	
def form_to_json(form_data):
	#customer conversion function from passed form data to stored json data
	json_data = {}
	json_data['u_name'] = form_data['u_name'].value
	json_data['driving_license_number'] = form_data['driving_license_number'].value
	json_data['vehicle_booked'] = form_data['vehicle_booked'].value
	json_data['aadhaar'] = form_data['aadhaar'].value
	json_data['pickup_time'] = form_data['pickup_time'].value
	json_data['return_time'] = form_data['return_time'].value
	
	return json_data

def data_storage(data):
	#temp
	if (os.path.isfile(FILEPATH) and os.access(PATH, os.R_OK)):
		print("File exists and is readable")
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
if not 'cars' in form:
	print(html % 'Invalid')
else:
	print(html % ('Booking %s.' % form['vehicle_booked'].value))

print form



data = form_to_json(form)

data_storage(data)



