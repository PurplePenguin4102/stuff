class Dungeon(object):
	'''a dungeon is a generator class which defines which rooms should be linked
	and whether or not there are secret passages or whatever'''

	def __init__(self, roomlist=[], xtra_rooms=-1, xtra_floors=-1,
				 underground=True):

		if xtra_rooms == -1: xtra_rooms = random.randint(1,10)+2
		if xtra_floors == -1: xtra_floors = random.randint(1,3)
		self.roomlist = roomlist
		
		if roomlist == []:
			for n in range(xtra_rooms):
				self.roomlist.append(Room(label="Room {}".format(n)))
		else:
			self.roomlist = roomlist

		self.make_start_end()
		self.link_rooms()

		print "Made a dungeon", len(self.roomlist), "rooms long"

	def make_start_end(self):
		self.roomlist[0].make_start()
		self.roomlist[0].define_exit(self.roomlist[1])

		self.roomlist[-1].make_goal()
		self.roomlist[-1].define_exit(self.roomlist[-2])

	def link_rooms(self, max_exits=3):
		workinglist = self.roomlist[1:-1]
		
		for room in workinglist:
			workinglist.remove(room)
			exits = random.randint(2,max_exits)
			while len(room.exits) < exits:
				room.define_exit(workinglist[random.randint(0,len(workinglist))])