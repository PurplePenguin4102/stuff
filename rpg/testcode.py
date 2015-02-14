### code testing area ###

from classes.adventurer import Adventurer
from classes.creature import Creature
from classes.dungeon import Dungeon
from classes.room import Room
from main import Main
import math, random

Charlie = Adventurer(25)

quit_room = Room(label="quit")
victory_room = Room(label="win")

Player = Adventurer(50)
main = Main()

Randy = Player

enemy1 = Creature(desc = "a pack of mean looking bunnies", looked_at="They don't look like the petting kind", gender="collective")
enemy2 = Creature(hp=20, dmg=1, speed=3, desc = "a soft, fluffy pillow")
enemy3 = Creature(desc = "kittens wielding balloons")

room1 = Room(floor=["Gold and gems"])
room2 = Room(floor=["Bunny droppings", "distracting bauble"],inhabs=[enemy1])
room3 = Room(floor=["Feathers", "Balloon strings"],inhabs=[enemy2,enemy3])
room4 = Room()

roomlist = [room2,room3,room1,room4]

d = Dungeon(1)
e = Dungeon(2)
f = Dungeon(3, xtra_rooms=13)
g = Dungeon(4, roomlist=roomlist)

# crelist = [Randy, enemy1, enemy2, enemy3]

# #This is an example of a player's decisions

# main.start_game(d)
# Randy.enter_room()
# print Randy.look_around()
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

