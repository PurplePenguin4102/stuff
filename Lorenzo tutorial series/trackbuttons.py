import pygame, random

from dictionaries import colours

(x,y,xval,yval) = (0,0,0,0)
colour = ['black','black']
width = 320
height = 200
res = (width, height)
running = 1
LEFT = 1

colourkeys = colours.keys()
screen = pygame.display.set_mode(res)

while running:
	
	event = pygame.event.poll()
	screen.fill((0,0,0))	
	
	if event.type == pygame.QUIT:
		running = 0
	
	elif event.type == pygame.MOUSEMOTION:
		(xval,yval) = event.pos

	elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
		(x,y) = event.pos
		colour[0] = 'red'
		print "You pressed the mouse at (%d,%d)" % event.pos
	
	elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
		colour[0] = 'black'
		print "you released the mouse at (%d,%d)" % event.pos

	pygame.draw.line(screen, colours[colour[0]], (xval-20,yval), (xval+20,yval))
	pygame.draw.line(screen, colours[colour[0]], (xval,yval-20), (xval,yval+20))

	pygame.display.flip()