# GPS Coordinate class

class Coordinate(object):

	def __init__(self, latitude, longitude, timestamp=None):
		self.latitude = latitude
		self.longitude = longitude
		self.timestamp = timestamp

	def __str__(self):
		return "{},{},{}".format(self.latitude,self.longitude,self.timestamp)