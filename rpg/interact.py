from classes.adventurer import Adventurer
from classes.creature import Creature
from classes.dungeon import Dungeon
from classes.room import Room
from main import Main
import math, random

def create_game():
	quit_room = Room(label="quit")
	victory_room = Room(label="win")

	en_1 = Creature(desc = "a pack of mean looking bunnies", looked_at="They don't look like the petting kind", gender="collective")
	en_2 = Creature(hp=20, dmg=1, speed=3, desc = "a soft, fluffy pillow")
	en_3 = Creature(desc = "kittens wielding balloons")

	rm_1 = Room(floor=["Gold and gems"])
	rm_2 = Room(floor=["Bunny droppings", "distracting bauble"],inhabs=[en_1])
	rm_3 = Room(floor=["Feathers", "Balloon strings"],inhabs=[en_2,en_3])
	rm_4 = Room()

	roomlist = [rm_2,rm_3,rm_1,rm_4]

	dun_1 = Dungeon(1)
	dun_2 = Dungeon(2)
	dun_3 = Dungeon(3, xtra_rooms=13)
	dun_4 = Dungeon(4, roomlist=roomlist)
	dunlist = [dun_1,dun_2,dun_3,dun_4]
	return dunlist

def begin(first_time=True):
		
	Player = Adventurer(50)
	main = Main()

	if first_time is True:
		print "Why hello there, care to play a little game?"
	else:
		print "Try again :) yes/no"
	ans = raw_input()
	if ans == "yes":
		print "Be warned adventurer, the dungeons of Ark Thremar are not for the faint of heart!!"
	elif ans == "no":
		print "very well then..."
		return None
	else:
		print "What?"
		return begin(first_time=False)

	print "It is a brisk winter's morn. The hills of Ark Thremar are just ahead, \nwithin lie its dark and horrible secrets. As you approach, the \nimage of a wise old sage appears before you and offers you a mighty and terrible choice. \nChoose your destiny carefully yon adventurer, lest you meet your ruin..."
	dunlist = create_game()
	return choose_dungeon(dunlist)

def choose_dungeon(dunlist):
	print "What dungeon would you like to visit?"

	describe_dungeon(dunlist)

	ans = raw_input()
	if int(ans) not in range(1,5):
		print "Try again..."
		return choose_dungeon(dunlist)
	else:
		print "Are you sure you want", ans + "?"
		ans2 = raw_input()
		if ans2 == 'yes':
			return initiate_dungeon(dunlist[int(ans)-1])
		else:
			return choose_dungeon(dunlist)

def describe_dungeon(dunlist):
	for dun in dunlist:
		print "Dungeon", dun.identifier, "has", (len(dun.roomlist)-1), "rooms"

def initiate_dungeon(dun):
	print "Welcome to dungeon {}. Good luck... fool!".format(dun.identifier)
	end_game()

def end_game():
	print "This is as far as Joey's coded, congratulations :)"


# if __name__ == "__main__":

# 	begin()
	