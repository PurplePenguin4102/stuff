import math, random 
from room import Room

quit_room = Room(label="quit")
victory_room = Room(label="win")

class Dungeon(object):
	'''a dungeon is a generator class which defines which rooms should be linked
	and whether or not there are secret passages or whatever'''

	def __init__(self, internal_no, roomlist=None, xtra_rooms=-1, xtra_floors=-1,
				 underground=True, inhabs=None):

		self.identifier = internal_no
		
		if xtra_rooms == -1: xtra_rooms = random.randint(1,10)+2
		if xtra_floors == -1: xtra_floors = random.randint(1,3)
		if roomlist is None: self.roomlist = [Room(label="Room {}".format(n)) for n in range(xtra_rooms)]
		else: self.roomlist = roomlist
		if inhabs is None: self.inhabitants = []
		else: self.inhabitants = inhabs

		# print "Made a dungeon", (len(self.roomlist)-1), "rooms long"

		self.make_start_end()
		self.link_rooms()
		self.populate_rooms()

		# print "Made a dungeon", len(self.roomlist), "rooms long"

	def make_start_end(self):
		self.roomlist[0].make_start()
		self.roomlist[0].define_exit(self.roomlist[1])

		self.roomlist[-1].make_goal()
		self.roomlist[-1].define_exit(self.roomlist[-2])

	def link_rooms(self, max_exits=3):
		workinglist = self.roomlist[:]
		
		for room in workinglist:
			workinglist.remove(room)
			exits = random.randint(2,max_exits)
			while len(room.exits) < exits:
				room.define_exit(random.choice(workinglist))

	def populate_rooms(self):
		for cre in self.inhabitants:
			random.choice(self.roomlist[1:]).inhabitants.append(cre)

