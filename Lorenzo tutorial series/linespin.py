import pygame
import time

from dictionaries import *
from linespinsupport import *

width = height = 500

screen = pygame.display.set_mode((width,height))

(x_0,y_0) = screen_pos['center'](width,height)
(x_1,y_1) = width/2 + 1000, height/2
theta = math.pi/180

while True:

	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	
	screen.fill(colours['black'])

	pygame.draw.line(screen, colours['white'], screen_pos['topc'](width,height), screen_pos['botc'](width,height))
	pygame.draw.line(screen, colours['white'], screen_pos['leftmid'](width,height), screen_pos['rightmid'](width,height))

	
	pygame.draw.line(screen, colours['red'], screen_pos['center'](width,height), (x_1, y_1))	
	
	(x_1,y_1) = pixel_to_xy((x_1,y_1),(width,height))
	(x_1,y_1) = originspin((x_1,y_1), theta)
	(x_1,y_1) = xy_to_pixel((x_1,y_1),(width,height))
	
	theta += math.pi/90
	
	time.sleep(.05)

	pygame.display.flip()