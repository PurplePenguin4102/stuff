import pygame

colours = {'blue' : (0,0,255),
	 	   'black' : (0,0,0),
	 	   'white' : (255,255,255),
	 	   'red' : (255,0,0),
	 	   'green' : (0,255,0),
	 	   'cyan' : (0,255,255)}

screen_pos = {'topl' : lambda width, height: (0, 0),
		      'topr' : lambda width, height: (width, 0),
		      'topc' : lambda width, height: (width/2, 0),
		      'botl' : lambda width, height: (height, 0),
		      'botr' : lambda width, height: (width, height),
		      'botc' : lambda width, height: (width/2, height),
		      'leftmid' : lambda width, height: (0,height/2),
		      'rightmid' : lambda width, height: (width, height/2),
		      'center' : lambda width, height: (width/2, height/2)}


corners = {'topleft' : lambda i, width, height: [colours['white'], (i,0), (0, height - i)],
          'topright' : lambda i, width, height: [colours['red'], (width,i), (i, 0)],
          'botleft'  : lambda i, width, height: [colours['green'], (width,height-i), (i, height)],
          'botright' : lambda i, width, height: [colours['blue'], (0,height - i), (width - i , height)]}

boxcommands = {pygame.K_UP: 'box.direction(UP)',
			pygame.K_q: 'box.direction(LUP)',
			pygame.K_w: 'box.direction(RUP)',
			pygame.K_a: 'box.direction(LOWN)',
			pygame.K_s: 'box.direction(ROWN)',
			pygame.K_DOWN: 'box.direction(DOWN)',
			pygame.K_LEFT: 'box.direction(LEFT)',
			pygame.K_RIGHT: 'box.direction(RIGHT)'}

wormcommands = {pygame.K_UP : (0,-1),
				pygame.K_DOWN : (0,1),
				pygame.K_LEFT : (-1,0),
				pygame.K_RIGHT : (1,0), }