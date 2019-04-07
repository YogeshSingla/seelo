#!/usr/bin/python
import cgi

#add my module
import sys
sys.path.insert(0, '/home/kirito/TODO/seelo/lab9/TAVS/webapp/mymodule/')
import Admin

import io
import csv
import os


PATH='/home/kirito/TODO/seelo/lab9/TAVS/webapp/mymodule/data_storage/'
FILENAME = 'admins.csv'
FILEPATH = PATH + FILENAME


def form_to_json(form_data):
	data = [0,'']
	data[0] = form_data['a_id'].value
	data[1] = form_data['password'].value
	return data

def check_credentials(data):
	#store data in json format
	isAllowedLogin = False
	if (os.path.isfile(FILEPATH) and os.access(PATH, os.R_OK)):
		#print("File exists and is readable")
		data_list = []
		
		with open(FILEPATH, 'rt') as csvfile:
			read_obj = csv.reader(csvfile, delimiter = ',')
			for row in read_obj:
				data_list.append(row)
				if row[0] == data[0] and row[1] == data[1]:
					isAllowedLogin = True
	else:
		print("ERROR #7 : admin file missing")

	return isAllowedLogin

form = cgi.FieldStorage()


data = form_to_json(form)

html_wrapper = """
<HTML>
<HEAD>
<TITLE>%s</TITLE>
<BODY>
%s
</BODY>
</HTML>
"""
html_success = """
<H1>Admin Access Successful</H1>
<H3><A href="/cgi-bin/admin.py">Click here</A></H3>
<HR>
<HR>"""

html_failed = """
<H1>Incorrect Credentials</H1>
<H3><A href="/index.html">Click here to go to home page</A></H3>
<HR>
<HR>"""

print('Content-type: text/html')
if(check_credentials(data)):
	#print(html_wrapper%('SUCCESS',html_success))
	import admin
else:
	print(html_wrapper%('FAILED',html_failed))
