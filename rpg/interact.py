from classes.adventurer import Adventurer
from classes.creature import Creature
from classes.dungeon import Dungeon
from classes.room import Room
from main import Main
import math, random

def begin():
	print "Why hello there, care to play a little game?"
	ans = raw_input()
	if ans == "yes":
		print "Well then, why don't you sit down and CODE IT CORRECTLY?!"
	else:
		print "Hey fuck you too buddy!"