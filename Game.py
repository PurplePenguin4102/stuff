import random

class Adventurer(object):
	def __init__(self):
		self.hp = 50
		self.job = "warrior"
		self.damage = 2
		self.inventory = []

	def pickup(self):
		possible_loot = World_objects()
		self.inventory.append(possible_loot.drop())

	def look_at_gear(self):
		return self.inventory

class World_objects(object):
	def __init__(self):
		sword_of_truth = "A cool sword"
		potion_of_might = "A tasty drink"
		leet_loot = "shiny"

		self.loot_table = [sword_of_truth, potion_of_might, leet_loot]

	def drop(self):
		r = random.randint(0,2)
		return self.loot_table[r]



Randy = Adventurer()
Susan = Adventurer()

print Randy.look_at_gear()
Randy.pickup()
print Randy.look_at_gear()