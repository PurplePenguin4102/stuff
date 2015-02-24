import math

def pixel_to_xy((pix_x,pix_y),(width,height)):
	'''Takes a 2 tuple with pixel coordinates and converts it to x, y 
	coordinates centered at the center of the screen'''

	x = pix_x - width/2
	y = height/2 - pix_y

	return (x,y)

def xy_to_pixel((x,y),(width,height)):
	'''inverts pixel_to_xy'''

	pix_x = x + width/2
	pix_y = height/2 - y

	return (int(pix_x),int(pix_y))

def originspin((x_0,y_0),theta):
	'''Spins a line originating at (0,0) by theta
	'''

	hyp = float(math.sqrt(x_0**2 + y_0**2))

	y_1 = math.sin(theta) * hyp
	x_1 = math.cos(theta) * hyp

	return (x_1,y_1)

def spinstep((x_0,y_0), (x_1,y_1), theta):
	'''Spins a line that starts at x_0,y_0 and terminates at x_1,y_1
	by theta and returns a new start and terminate point'''

	pass
	