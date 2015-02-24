import pygame

width = 320
height = 200
running = 1 
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = 0
		else:
			print event.type
	clock.tick(20)