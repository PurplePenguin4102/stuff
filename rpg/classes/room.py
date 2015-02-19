default_description = "You are in a small, white room. Blue gridlines spaced exactly 5 feet apart run along the floor and up the walls. The ceiling disappears into the sky."

class Room(object):
	'''a Room is the place where creatures inhabit and objects are held.'''

	def __init__(self, inventory=None, inhabs=None, floor=1, exits=None, label=""):

		self.label = label
		self.description = default_description

		if inventory is None: self.inventory = []
		else: self.inventory = inventory
		if inhabs is None: self.inhabitants = []
		else: self.inhabitants = inhabs
		if exits is None: self.exits = []
		else: self.exits = exits
		
		self.active = False

	def activate_creatures(self):
		for creature in self.inhabitants: creature.active = True

	def make_start(self):
		self.dung_start = True
		self.exits.append(quit_room)
		self.description = "You find yourself at the start of the dungeon. You have two options at this point: give up, or onwards to glory!"

	def make_goal(self):
		self.dung_goal = True
		self.quest_item = True
		self.exits.append(victory_room)

	def define_exit(self,room):
		self.exits.append(room)
		room.exits.append(self)

quit_room = Room(label="quit")
victory_room = Room(label="win")

if __name__ == "__main__":

	quit_room = Room(label="quit")
	victory_room = Room(label="win")

	rm_1 = Room(inventory=["Gold and gems"], label="room 1")
	rm_2 = Room(inventory=["Bunny droppings", "distracting bauble"], label="room 2")
	rm_3 = Room(inventory=["Feathers", "Balloon strings"], label="room 3")
	rm_4 = Room(label="room 4")

	rm_1.make_start()
	rm_4.make_goal()

	rm_1.define_exit(rm_2)
	rm_1.define_exit(rm_3)
	rm_2.define_exit(rm_1)
	rm_2.define_exit(rm_4)
	rm_2.define_exit(rm_3)
	rm_3.define_exit(rm_1)
	rm_3.define_exit(rm_2)
	rm_4.define_exit(rm_2)

	roomlist = [quit_room, victory_room, rm_1, rm_2, rm_3, rm_4]

	for room in roomlist:
		print room.inventory

	# for room in roomlist:
	# 	print room.label

	if rm_2.exits is rm_1.exits:
		print "it's broken"