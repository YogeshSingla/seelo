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
		#TODO Add rent module

	def return_vehicle():
		pass
		#TODO Add return module