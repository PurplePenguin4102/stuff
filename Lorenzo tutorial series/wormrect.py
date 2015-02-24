import pygame
from wormsupp import Worm

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width,height))

running = True
while running:

	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()