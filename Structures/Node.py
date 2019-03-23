from Structures.Coordinate import Coordinate

class Node(object):

	def __init__(self, json_object):
		self.json_object = json_object
		self.coordinate = self.create_coordinate(json_object)
		self.throttle = json_object["throttle"]

	def get_coordinate(self):
		return self.coordinate

	def get_throttle(self):
		return self.throttle

	def create_coordinate(self, json_object):
		coordinate = json_object["coordinate"]
		return Coordinate(coordinate["latitude"],coordinate["longitude"])

	def __str__(self):
		return "{},{}".format(self.coordinate,self.throttle)