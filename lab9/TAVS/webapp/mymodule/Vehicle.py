#!/usr/bin/python

class Vehicle:
	"Stores every vehicle detail"
	def __init__(self, vehicle_id = 0, isAC = False, v_name = 'unnamed', miles_run = 0, cost_incurred = 0, price = -1, fuel_consumed = 0, isOwned = False):
		self.v_id = vehicle_id
		self.isAC = isAC
		self.v_name = v_name
		self.miles_run = miles_run
		self.cost_incurred = cost_incurred
		self.price = price
		self.fuel_consumed = fuel_consumed
		self.isOwned = isOwned
	
	def getDetails(self, v_id, vehicle_details):
		if v_id == self.v_id:
			vehicle_details.append(self.v_name)
			vehicle_details.append(self.price)
			vehicle_details.append(self.isAC)
			return True
		else:
			return False
