import pygame

colours = {'blue' : (0,0,255),
	 	   'black' : (0,0,0),
	 	   'white' : (255,255,255),
	 	   'red' : (255,0,0),
	 	   'green' : (0,255,0)}

y = 0
direc = 1
running = 1
width = 500
height = 500
barheight = 124
res = (width,height)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(res)
linecolour = colours['red']
bgcolour = colours['black']

barcolour = []
for i in range(1,63):
	barcolour.append((0, i*4, i*4))
for i in range(1,63):
	barcolour.append((0, 255-i*4, 255-i*4))

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print "quit!!"
			running = 0
		print event.type

	screen.fill(bgcolour)
	for i in range(0,barheight):
		pygame.draw.line(screen, barcolour[i], (0,y+i), (width, y+i))
	#pygame.draw.line(screen, linecolour, (0,y), (width-1,y))

	y += direc
	if (y + barheight > height) or (y < 0):
		direc *= -1

	clock.tick(500)
	pygame.display.flip()