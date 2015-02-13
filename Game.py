import random

import math

possible_jobs = ["Warrior", "Tinker", "Tailor", "Soldier", "Spy", "Archer", "Mage"]
default_description = "You are in a small, white room. Blue gridlines spaced exactly 5 feet apart run along the floor and up the walls. The ceiling disappears into the sky."

class Main(object):
	'''The Main class handles all global effects that happen across turns. 
	   It also handles combat, the turn ticker and global rolling. Only have 
	   one main class active at a time, unless you have a death wish
	'''

	def __init__(self):
		
		self.turn = 1
		self.is_combat = False
		self.combat_turn = 0

	def next_turn(self):

		self.turn += 1
		active_creatures = 0

		if not self.is_combat:
			for cre in crelist:
				if cre.active:
					active_creatures += 1
			if active_creatures > 1:
				self.is_combat = True
		else:
			self.combat_turn += 1
			self.combat(self.combat_turn)

		print "It is turn {}".format(self.turn)

	def roll(self, DC=0, modifier=0, crit_rate=0):
		'''The core mechanic of this game system, the "roll" is where two 
		random numbers are generated and compared.'''

		world_roll = random.randint(1,10+DC)
		player_roll = random.randint(1,10+DC)
		result = math.fabs(world_roll-player_roll)

		if result <= crit_rate:
			return "crit"
		else:
			return result-modifier

	def combat(self, combat_turn=0):
		combat_creatures = {}
		for cre in crelist:
			if cre.active:
				combat_creatures[cre] = cre.speed 

		for speed in xrange(1,10):
			print "now testing speed", 10 - speed
			for cre in combat_creatures:
				if combat_creatures[cre] == 10 - speed:
					print "Have at thee!!", "It is", cre.description, "'s turn"
					if cre.combat_action == None:
						pass
					elif cre.combat_action == "attack":
						print "They attack!"
						cre.attack_enemy()
						cre.attack(cre.combat_enemy)

		print "you have been in combat", combat_turn, "turn(s)"

	def start_game(self, dungeon):
		print "Welcome to the dungeons of Ark Thremar! What do you do?"
		print "It is turn 1"
		Player.active_room = dungeon.roomlist[0]
		dungeon.roomlist[0].active = True

class Creature(object):
	'''Creatures are the basic inhabitants of the world. They have
	various inherent properties like hit points and damage, and can
	do things like manipulate items, attack each other and level up'''

	def __init__(self, hp=10, dmg=2, speed=5, desc="A nondescript creature",
				 room="The Nether", is_active=False, 
				 looked_at="Sure looks deadly...", gender="neutral"):

		self.gender = gender
		self.active = is_active
		self.description = desc
		self.hp = hp
		self.damage = dmg
		self.inventory = []
		self.speed = speed
		self.looked_at = looked_at
		self.combat_action = "attack"

	def attack(self, cre1):
		cre1.hp += self.damage*-1

	def attack_enemy(self):
		self.combat_enemy = Randy

class Adventurer(Creature):
	'''Adventurer is a type of Creature, the additional functions
	of adventurer are all related to the job system (whatever that
	may be)'''

	def __init__(self, hp):
		Creature.__init__(self, hp, is_active = True, desc="a noble hero")
		self.job = "warrior"

	def attack_enemy(self, cre):
		combat_action = "attack"
		combat_enemy = cre

	def enter_room(self, room=None):
		if not room:
			print "You gotta pick a way to go boss..."
			return
		self.active_room.activate_creatures()
		main.next_turn()

	def pickup(self, item=0, choose=False):
		if len(self.active_room.inventory) == 0:
			print "Nothing here boss..."
			return

		if (len(self.active_room.inventory) > 1) and not choose:
			print "ya gotta be specific boss..."
			return

		if main.is_combat:
			print "You attempt to pick it up..."
			self.combat_action = None
			main.next_turn()
		
		else:
			print "You gleefully acquire the {} on the floor".format(self.active_room.inventory[item]) 
			self.inventory.append(self.active_room.inventory[item])
			main.next_turn()

	def look_around(self):
		final_description = self.description
		if len(self.inhabitants) > 0:
			final_description += " Inhabiting the room is "
			for i in self.inhabitants:
				final_description += "{0}, and ".format(i.description)
			final_description = final_description[:-6] + "."
		return final_description

	def look_at_stats(self):
		print "hp: {0}, dmg: {1}".format(self.hp, self.damage)

	def look_at(self,thing):
		genders = {"male" : "He is",
				   "female" : "She is",
				   "neutral" : "It is",
				   "collective" : "They are"}
		print thing.looked_at, "({} hostile)".format(genders[thing.gender])

class Dungeon(object):
	'''a dungeon is a generator class which defines which rooms should be linked and whether or not there are secret passages or whatever'''

	def __init__(self, roomlist=[], xtra_rooms=-1, xtra_floors=-1,
				 underground=True):

		if xtra_rooms == -1: xtra_rooms = random.randint(1,10)+2
		if xtra_floors == -1: xtra_floors = random.randint(1,3)
		self.roomlist = roomlist
		
		if roomlist == []:
			for n in range(xtra_rooms):
				self.roomlist.append(Room())
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

class Room(object):
	'''a Room is the place where creatures inhabit and objects are held.'''

	def __init__(self, inventory=[], inhabs=[], floor=1, exits=[]):

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

	def make_goal(self):
		self.dung_goal = True
		self.quest_item = True
		self.exits.append(victory_room)

	def define_exit(self,room):
		self.exits.append(room)

quit_room = Room()
victory_room = Room()
Player = Adventurer(50)

main = Main()


# class Game(object):
# 	'''Game is a gui and the main human interface for playing the 
# 	game.'''

# 	def __init__(self,master):

# 		self.label1 = Label(master, text="Hello")
# 		self.label1.pack()

# if __name__ == "__main__":

# 	root = Tk(screenName="Kreldor")
# 	hajime = Game(root)
# 	root.mainloop()



### Test code ### Put if __name__ == "__main__": here later maybe

#This is an example of a generated game

Randy = Player

enemy1 = Creature(desc = "a pack of mean looking bunnies", looked_at="They don't look like the petting kind", gender="collective")
enemy2 = Creature(hp=20, dmg=1, speed=3, desc = "a soft, fluffy pillow")
enemy3 = Creature(desc = "kittens wielding balloons")

d = Dungeon()


# room1 = Room(floor=["Gold and gems"])
# room2 = Room(floor=["Bunny droppings", "distracting bauble"],inhabs=[enemy1])
# room3 = Room(floor=["Feathers", "Balloon strings"],inhabs=[enemy2,enemy3])
# room4 = Room()

# roomlist = [room2,room3,room1,room4]

crelist = [Randy, enemy1, enemy2, enemy3]

#This is an example of a player's decisions

main.start_game(d)
Randy.enter_room()
# print "player looks at bunnies"
# Randy.look_at(enemy1)
# print "player wants to pick up bauble"
# Randy.pickup()
# print "player tries again"
# Randy.pickup(1,True)
# Randy.look_at_stats()
# Randy.enter_room()
# Randy.look_at(enemy2)
# Randy.look_at_stats()

# adjectives = ["mean looking", "Robot", "laser wielding", "incredibly muscular", "tall", "evil"]
# nouns = ["bunnies", "kittens", "puppies"]


# print adjectives[random.randint(0,4)], adjectives[random.randint(0,4)], nouns[random.randint(0,2)]

