import pygame
import math

from dictionaries import colours


x = y = 0
running = 1
width = 640
height = 480

res = (width,height)
screen = pygame.display.set_mode(res)

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	elif event.type == pygame.MOUSEBUTTONDOWN:
		(xpos,ypos) = event.pos
		#tile = xpos/32 + 1 + ypos/32*20
		xpos += -width/2
		ypos = height/2 - ypos

		totalpos = float(math.sqrt(xpos**2 + ypos**2))

		print "Mouse is at ({0}, {1}) it's distance is {2:.4f}".format(xpos,ypos,totalpos)

	screen.fill((0,0,0))

	pygame.draw.line(screen, (255,255,255), (0,height/2), (width,height/2))
	pygame.draw.line(screen, (255,255,255), (width/2,0), (width/2,height))
	

	pygame.display.flip()