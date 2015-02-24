import pygame
import math

from dictionaries import *

xpos = ypos = xposr = yposr = y = x = 0

running = 1
width = 320
height = 200

blueval = 0
bluedir = 1

colour = colours['black']

res = (width,height)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

while running:
	
	screen.fill(colours['black'])

	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	elif event.type == pygame.MOUSEMOTION:
		(xpos,ypos) = event.pos

	elif event.type == pygame.MOUSEBUTTONDOWN:
		(x,y) = event.pos
		x += -width/2
		y = height/2 - y
		if x <= 0 and y >= 0: 
			colour = colours['red']
		elif x > 0 and y >= 0:
			colour = colours['green']
		elif x <= 0 and y < 0:
			colour = colours['blue']
		elif x > 0 and y < 0:
			colour = colours['cyan']
		print "(x,y) = ({0}, {1})".format(x,y)
		xposr, yposr = xpos, ypos
	
	pygame.draw.line(screen, colour, (xposr-50,yposr), (xposr+50,yposr))
	pygame.draw.line(screen, colours['white'], (width,height), (xpos,ypos))
	pygame.draw.line(screen, colours['white'], (0,height), (xpos,ypos))


	pygame.draw.line(screen, colours['white'], 
				     (0,height/2), (width, height/2))
	pygame.draw.line(screen, colours['white'],
					 (width/2,0), (width/2,height))

	pygame.draw.line(screen, (0,0,blueval), (xpos,ypos-10), (xpos,ypos+10))
	pygame.draw.line(screen, (0,0,blueval), (xpos-10,ypos), (xpos+10,ypos))
	
	blueval += bluedir
	if blueval == 255 or blueval == 0:
		bluedir *= -1

	pygame.display.flip()