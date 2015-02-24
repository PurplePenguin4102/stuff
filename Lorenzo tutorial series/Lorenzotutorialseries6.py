
import pygame
from dictionaries import *
from worm import Worm

#Dimensions
width = 640
height = 400

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True
timer = 0

#our worm
w = Worm(screen,width/2, height/2,200)
#w2 = Worm(screen,width/2+ 20, height/2 + 20,200)

while running:
	screen.fill(colours['black'])
	w.draw()
	w.move()

#	w2.move()
#	w2.draw()

	if timer%1000 == 0:
		timer = 0
		w.getlonger()
#		w2.getlonger()

	if w.crashed or w.x <=0 or w.x >= width or w.y <= 0 or w.y >= height:
		print "crash!"
		running = False
#	if w2.crashed or w2.x <=0 or w2.x >= width or w2.y <= 0 or w2.y >= height:
#		print "crash!"
#		running = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			w.key_event(event)
#			w2.key_event(event)

	pygame.display.flip()
	clock.tick(400)
	timer += 1
