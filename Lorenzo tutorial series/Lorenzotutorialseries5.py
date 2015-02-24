import pygame
import random

from dictionaries import *
from movepix import *

#these are used for directions.
UP = (0,-1)
LUP = (-1,-1)
RUP = (1,-1)
DOWN = (0,1)
LOWN = (-1,1)
ROWN = (1,1)
LEFT = (-1,0)
RIGHT = (1,0)

#Initialise the screen
width = 640
height = 400
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
running = True

#rand = lambda i: random.randint(0,i)

#pixel_position
box = Movingbox(width/2,height/2)

while running:
	box.move()

	if box.x <= 0 or box.y <= 0 or box.x >= width or box.y >= height:
		print "Crash!"
		running = False

	screen.fill(colours['black'])
	box.makesquare()
	box.draw(screen)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		elif event.type == pygame.KEYDOWN:
			if event.key in boxcommands:
				eval(boxcommands[event.key])

	clock.tick(120)
	pygame.display.flip()

'''what follows was originally written by Lorenzo for his pygame tutorial series. Above is my own work based on his

# while running:
# 	pix.move()

# 	if pix.x <= 0 or pix.x >= width or pix.y <= 0 or pix.y >= height:
# 		print "Crash!"
# 		running = False

# 	screen.fill(colours['black'])
# 	pix.draw(screen)

# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			running = False
		
# 		elif event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_UP:
# 				pix.direction(UP)
# 			if event.key == pygame.K_DOWN:
# 				pix.direction(DOWN)
# 			if event.key == pygame.K_LEFT:
# 				pix.direction(LEFT)
# 			if event.key == pygame.K_RIGHT:
# 				pix.direction(RIGHT)

# 	clock.tick(120)
# 	pygame.display.flip()



# while running:
# 	x = rand(width)
# 	y = rand(height)
# 	(R,G,B) = (rand(255),rand(255),rand(255))

# 	screen.set_at((x,y),(R,G,B))

# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			running = False
# 		elif event.type == pygame.MOUSEBUTTONDOWN:
# 			x_0,y_0 = event.pos
# 			screen.set_at((x_0,y_0),(R,G,B))

# 	pygame.display.flip()
# 	clock.tick(50) '''