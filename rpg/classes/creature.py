class Creature(object):
	'''Creatures are the basic inhabitants of the world. They have
	various inherent properties like hit points and damage, and can
	do things like manipulate items, attack each other and level up'''

	def __init__(self, hp=10, dmg=2, speed=5, desc="A nondescript creature",
				 room="The Nether", is_active=False, 
				 looked_at="Sure looks deadly...", gender="neutral", internal=""):

		self.internal = internal
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
		print "placeholder string"