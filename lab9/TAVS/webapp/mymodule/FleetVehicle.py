#!/usr/bin/python

#add my module
import sys
sys.path.insert(0, '/home/kirito/TODO/seelo/lab9/TAVS/webapp/mymodule/')

import Vehicle

UNSOLD = 0
AVAILABLE = 1
BOOKED = 2
REPAIR = 3

class FleetVehicle(Vehicle.Vehicle):
	"""
	FleetVehicle(self, rent = 0, status = UNSOLD, last_rent_time = 0, vehicle_id = 0, isAC = False, v_name = 'unnamed', miles_run = 0, cost_incurred = 0, price = -1, fuel_consumed = 0, isOwned = False):
	"""
	def __init__(self, rent = 0, status = UNSOLD, last_rent_time = 0, vehicle_id = 0, isAC = False, v_name = 'unnamed', miles_run = 0, cost_incurred = 0, price = -1, fuel_consumed = 0, isOwned = False):
		self.rent = rent
		self.status = status
		self.last_rent_time = last_rent_time
		Vehicle.__init__(self, vehicle_id, isAC, v_name, miles_run, cost_incurred, price, fuel_consumed, isOwned)

	def rent_vehicle():
		pass
		#TODO: Integrate this module
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


	def return_vehicle():
		pass
		#TODO: Integrate this module
		#store data in json format
		if (os.path.isfile(FILEPATH) and os.access(PATH, os.R_OK)):
			#print("File exists and is readable")
			data_list = []
			u_id = data[1]
			isAllowedReturn = False
			return_record = []
			with open(FILEPATH, 'rt') as csvfile:
				read_obj = csv.reader(csvfile, delimiter = ',')
				for row in read_obj:
					data_list.append(row)
					#field_headings = data_list[0]
					#data_list.remove(data_list[0])
			for record in data_list:
				if u_id == record[1]:
					isAllowedReturn = True
					return_record = record
			data_list = []
			if(isAllowedReturn):
				with open(FILEPATH, 'rt') as csvfile:
					read_obj = csv.reader(csvfile, delimiter = ',')
					for row in read_obj:
						if u_id != row[1]:
							data_list.append(row)
					
				with open(FILEPATH, 'wt') as csvfile:
					write_obj = csv.writer(csvfile, delimiter = ',')	
					for row in data_list:
						write_obj.writerow(row)
				print("Return Successful")
			else:
				print("ERROR #3: Please book a vehicle first.")
		else:
			print ("ERROR #3: Please book a vehicle first.")
		#TODO Add return module