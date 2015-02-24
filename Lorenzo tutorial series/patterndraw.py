import pygame

from dictionaries import *

width = 500
height = 500

res = (width,height)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

while 1:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    screen.fill(colours['black'])
    
    for key in corners:

        i = 5
        while (height - i) > 0:
            pygame.draw.line(screen, corners[key](i,width,height)[0], corners[key](i,width,height)[1], 
                             corners[key](i,width,height)[2])
            i += 5

    #pygame.draw.line(screen, colours['red'], (0,0), (width,height))
    #pygame.draw.aaline(screen, colours['blue'], (width,0), (0,height))

    #pygame.draw.line(screen, colours['green'], (width/2,0), (width/2,height))
    #pygame.draw.line(screen, colours['white'], (0,height/2), (width,height/2))

    pygame.display.flip()
