from Structures.Node import Node

class Nodelist(object):

	def __init__(self, conf):
		self.conf = conf
		self.nodelist = Nodelist.read_node_file(self.conf["nodelist"]["file"])
		self.current_node_index = -1

	def get_list(self):
		return self.nodelist

	def increment_node(self):
		if self.current_node_index < len(self.nodelist)-1:
			self.current_node_index += 1
			return True
		else:
			self.current_node_index += 1
			return False

	def get_next_node(self):
		success = self.increment_node()
		if not success:
			return None
		else:
			try:
				return self.nodelist[self.current_node_index]
			except IndexError as e:
				print(self.current_node_index)
				raise e
	def all_nodes_visited(self):
		return not self.current_node_index < len(self.nodelist)


	@staticmethod
	def read_node_file(location):
		raw_json = ConfigReader.read_json(location)
		nodelist = []
		for item in raw_json["nodes"]:
			nodelist.append(Node(item))
		return nodelist