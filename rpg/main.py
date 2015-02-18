import math, random

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

		# if not self.is_combat:
		# 	for cre in crelist:
		# 		if cre.active:
		# 			active_creatures += 1
		# 	if active_creatures > 1:
		# 		self.is_combat = True
		# else:
		# 	self.combat_turn += 1
		# 	self.combat(self.combat_turn)

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

	def start_game(self, dungeon, adventurer):
		print "Welcome to the dungeons of Ark Thremar! What do you do?"
		print "It is turn 1"
		adventurer.active_room = dungeon.roomlist[0]
		dungeon.roomlist[0].active = True