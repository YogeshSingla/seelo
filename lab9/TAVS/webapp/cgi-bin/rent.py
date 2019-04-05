#!/usr/bin/python
import cgi

#add my module
import sys
sys.path.insert(0, '/home/kirito/TODO/seelo/lab9/TAVS/webapp/mymodule/')
import User

import io
import csv
import os


PATH='/home/kirito/TODO/seelo/lab9/TAVS/webapp/mymodule/data_storage/'
FILENAME = 'bookings.csv'
FILEPATH = PATH + FILENAME
u_id = 0


def form_to_json(form_data):
	#customer conversion function from passed form data to stored json data
	data = [0,0,0,0,0,0]
	#modify the global u_id variable to allow value access to data_storage()
	global u_id
	u_id = form_data['driving_license_number'].value
	data[0] = form_data['u_name'].value
	data[1] = form_data['driving_license_number'].value
	data[2] = form_data['vehicle_booked'].value
	data[3] = form_data['aadhaar'].value
	data[4] = form_data['pickup_time'].value
	data[5] = form_data['return_time'].value
	
	return data

def data_storage(data):
	#store data in json format
	if (os.path.isfile(FILEPATH) and os.access(PATH, os.R_OK)):
		#print("File exists and is readable")
		data_list = []
		u_id = data[1]
		isAllowedBooking = True
		with open(FILEPATH, 'rt') as csvfile:
			read_obj = csv.reader(csvfile, delimiter = ',')
			for row in read_obj:
				data_list.append(row)
				#field_headings = data_list[0]
				#data_list.remove(data_list[0])
		for record in data_list:
			if u_id == record[1]:
				print("ERROR #2: Please return the booked vehicle.")
				isAllowedBooking = False
		if(isAllowedBooking):
			with open(FILEPATH, 'at') as csvfile:
				write_obj = csv.writer(csvfile, delimiter = ',')	
				write_obj.writerow(data)
				print("Success")
	else:
		print ("Either file is missing or is not readable, creating file...")
		with open(FILEPATH, 'wt') as csvfile:
			write_obj = csv.writer(csvfile, delimiter = ',')
			write_obj.writerow(data)

form = cgi.FieldStorage()
print('Content-type: text/html')
# parse form data
# plus blank line
html = """
<TITLE>rent</TITLE>
<H1>Server Response</H1>
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



