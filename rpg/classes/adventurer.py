from creature import Creature

class Adventurer(Creature):
	'''Adventurer is a type of Creature, the additional functions
	of adventurer are all related to the job system (whatever that
	may be)
	
	I should point out that for some reason at the moment the Adventurer
	class is also masquerading as the player class which contains all of the
	player's movement and combat options... fix this later'''

	def __init__(self, hp):
		Creature.__init__(self, hp, is_active = True, desc="a noble hero")
		self.job = "warrior"
		self.active_room = None
		self.name = "Randy"

	def attack_enemy(self, cre):
		combat_action = "attack"
		combat_enemy = cre

	def enter_room(self, room=None, main=None):
		if room is None:
			print "You gotta pick a way to go boss..."
			return
		elif room not in self.active_room.exits:
			print "No way there boss..."
			return
		elif room in self.active_room.exits:
			self.active_room = room
		else:
			pass
		
		self.active_room.activate_creatures()
		main.next_turn()

	def pickup(self, item=0, choose=False, main=None):
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

	def look_around(self, room=None):

		if room is None: room = self.active_room
		
		final_description = room.description
		if len(room.inhabitants) > 0:
			final_description += " Inhabiting the room is "
			for cre in room.inhabitants:
				final_description += "{0}, and ".format(cre.description)
			final_description = final_description[:-6] + "."

		final_description += " There are {} exits to this room:".format(len(room.exits))
		for rm in room.exits:
			final_description += rm.label + " "
		return final_description

	def look_at_stats(self):
		print "hp: {0}, dmg: {1}".format(self.hp, self.damage)

	def look_at(self,thing):
		genders = {"male" : "He is",
				   "female" : "She is",
				   "neutral" : "It is",
				   "collective" : "They are"}
		print thing.looked_at, "({} hostile)".format(genders[thing.gender])