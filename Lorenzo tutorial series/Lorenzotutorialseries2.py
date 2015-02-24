import pygame

colours = {'blue' : (0,0,255),
	 	   'black' : (0,0,0),
	 	   'white' : (255,255,255),
	 	   'red' : (255,0,0),
	 	   'green' : (0,255,0)}

width = 640
height = 480

res = (width,height)

screen = pygame.display.set_mode(res)

while 1:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    screen.fill(colours['black'])
    pygame.draw.line(screen, colours['red'], (0,0), (width,height))
    pygame.draw.aaline(screen, colours['blue'], (width,0), (0,height))

    pygame.draw.line(screen, colours['green'], (width/2,0), (width/2,height))
    pygame.draw.line(screen, colours['white'], (0,height/2), (width,height/2))

    pygame.display.flip()