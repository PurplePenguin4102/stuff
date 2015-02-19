from classes.adventurer import Adventurer
from classes.creature import Creature
from classes.dungeon import Dungeon
from classes.room import Room
from main import Main
import math, random, re

Player = Adventurer(50)
main = Main()

def create_game():
	quit_room = Room(label="quit")
	victory_room = Room(label="win")

	en_1 = Creature(desc = "a pack of mean looking bunnies", looked_at="They don't look like the petting kind", gender="collective", internal="bunnies")
	en_2 = Creature(hp=20, dmg=1, speed=3, desc = "a soft, fluffy pillow", internal="pillow")
	en_3 = Creature(desc = "kittens wielding balloons", gender="collective", internal="kittens")
	en_4 = Creature(desc = "Angry German Gingerbread warriors", looked_at="They're adorable... and terrifying.", gender="collective", internal="warriors")
	en_5 = Creature(desc = get_adj()+" Zombie", gender="male", internal="zombie")
	en_6 = Creature(desc = "Friendly looking Gremlins", looked_at="They look friendly... at least for gremlins", gender="collective", internal="gremlins")

	enlist = [en_1,en_2,en_3,en_4,en_5,en_6]

	rm_1 = Room(floor=["Gold and gems"])
	rm_2 = Room(floor=["Bunny droppings", "distracting bauble"],inhabs=[en_1])
	rm_3 = Room(floor=["Feathers", "Balloon strings"],inhabs=[en_2,en_3])
	rm_4 = Room()

	roomlist = [rm_2,rm_3,rm_1,rm_4]

	dun_1 = Dungeon(1, inhabs=enlist)
	dun_2 = Dungeon(2, inhabs=enlist)
	dun_3 = Dungeon(3, xtra_rooms=13, inhabs=enlist)
	dun_4 = Dungeon(4, roomlist=roomlist, inhabs=enlist)
	dunlist = [dun_1,dun_2,dun_3,dun_4]
	return dunlist

def get_adj():
	adj_list = ["legal", "biscuit", "toothless", "funny lookin'", "robot"]
	return random.choice(adj_list)

def begin(first_time=True):
		
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
		print "Dungeon", dun.identifier, "has", (len(dun.roomlist)-1), "rooms", len(dun.inhabitants), "enemies."

def initiate_dungeon(dun, player = Player, main = main):
	print "You have chosen dungeon {}. Good luck... fool!".format(dun.identifier)

	main.start_game(dun,player)
	
	return play_dungeon(dun,player)

def play_dungeon(dun, player, main=main):

	print "You are at the entrance to the dungeon, you can 'look around', 'look self', and 'enter room'. \nIf you see a creature you can 'look at' it."

	while True:
		ans = raw_input("Your choice, hero: ")
		if ans == 'look around':
			print player.look_around()
		elif ans == 'look self':
			print "Your name is %s, your job is %s, you have %shp, and you're currently standing in room %s"%(player.name, player.job, player.hp, player.active_room.label)		
		elif valid_room(ans):
			room_id = int(ans[10:])
			room = dun.roomlist[room_id]
			player.enter_room(room, main)	
		elif (ans[:7] == "look at"):
			cre_internal = ans[8:]
			for cre in player.active_room.inhabitants:
				if cre.internal == cre_internal:
					print cre.looked_at

		elif ans == 'exit':
			return end_game()
		else:
			print "Invalid input"

		print "You can 'look around', 'look self', and 'enter room'"
		
def valid_room(usr_in):
	if (usr_in[:10] == "enter room") and (type(int(usr_in[10:])) is int):
		return True
	else:
		return False

def end_game():
	print "This is as far as Joey's coded, congratulations :)"


if __name__ == "__main__":

	# print "testing parser"
	# ans = raw_input()
	# valid_room(ans)
	begin()
	