from cre_templates import *
import random

class Creature(object):
	'''Creatures are the basic inhabitants of the world. They have
	various inherent properties like hit points and damage, and can
	do things like manipulate items, attack each other and level up'''

	def __init__(self, hp=10, dmg=2, speed=5, desc="A nondescript creature",
				 room="The Nether", is_active=False, 
				 looked_at="Sure looks deadly...", gender="neutral", internal="", level = 0):

		self.level = level
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

	def make_random(self):
		'''Sets a random description variable, internal, and other features'''

		self.description = ""

		if self.level == 0: no_mods = random.randint(1,3)
		else: no_mods = random.randint(1,self.level+3)
		
		mods = []
		avail_mods = [cre_adjective, cre_mood, cre_nationality, cre_weapon]

		for n in range(no_mods):
			mod_type = random.choice(avail_mods)
			if mod_type == cre_nationality:
				avail_mods.remove(cre_nationality)
			elif mod_type == cre_mood:
				avail_mods.remove(cre_mood)
			
			mods.append(random.choice(mod_type)) 

		if len(mods) < self.level+3:
			if ("gummy" or "gingerbread") in mods:
				amount = random.choice(cre_amount[-4:])
			else: amount = random.choice(cre_amount[:4])
		else: amount = (1, "a")

		(number, no_desc) = amount

		noun = random.choice(cre_noun)
		self.internal = noun

		if number > 1: 
			self.gender = "collective"
			
			self.description += no_desc + " of "
			if noun[-3:] == "man":
				noun = noun[:-3] + "men"
				self.internal = "strongmen"
			elif noun == "bunny":
				noun = "bunnies"
				self.internal = noun
			else:
				noun += "s"
				self.internal += "s"

		list(set(mods))

		for mod in mods:
			if mod in cre_mood: 
				self.description += mod + ", "

		for mod in mods:
			if mod in cre_nationality: 
				self.description += mod + ", "

		for mod in mods:
			if mod in cre_adjective: 
				self.description += mod + ", "

		self.description = self.description[:-2] + " " + noun

		for mod in mods:
			if mod in cre_weapon: self.description += ", wielding " + mod



		




		# apply modifiers to base creature
		# describe result
		# set description, internal, gender
