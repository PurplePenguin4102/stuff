import pygame

from combogui import * #defines R,G,B,xpos,ypos

colour = (R,G,B)
res = (xpos,ypos)

screen = pygame.display.set_mode(res)

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    screen.fill(colour)
    pygame.display.flip()