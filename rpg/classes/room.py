default_description = "You are in a small, white room. Blue gridlines spaced exactly 5 feet apart run along the floor and up the walls. The ceiling disappears into the sky."

class Room(object):
	'''a Room is the place where creatures inhabit and objects are held.'''

	def __init__(self, inventory=[], inhabs=[], floor=1, exits=[], label=""):

		self.label = label
		self.inventory = inventory
		self.inhabitants = inhabs
		self.description = default_description
		self.exits = exits
		self.active = False

	def activate_creatures(self):
		for creature in self.inhabitants:
			creature.active = True

	def make_start(self):
		self.dung_start = True
		self.exits.append(quit_room)
		self.description = "You find yourself at the start of the dungeon. You have two options at this point: give up like a little bitch, or onwards to glory!"

	def make_goal(self):
		self.dung_goal = True
		self.quest_item = True
		self.exits.append(victory_room)

	def define_exit(self,room):
		self.exits.append(room)

quit_room = Room(label="quit")
victory_room = Room(label="win")