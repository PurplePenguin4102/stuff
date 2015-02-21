##Code golf for February 21, task is to flip fifty distinct shades of grey on screen. Final solution: 12 lines ##

import sys, pygame
pygame.init()
variables = width, height, running = 32*7, 32*8, True

screen = pygame.display.set_mode((width,height))

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	for n in range(1,51):
		rect = pygame.Rect(((n%7)*32,(n/7)*32),(32,32))
		colour = (n*4,n*4,n*4)
		pygame.draw.rect(screen,colour,rect)
	pygame.display.flip()