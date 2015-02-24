from dictionaries import *

class MovingPixel:
	"""A moving pixel class"""

	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.hdir = 0
		self.vdir = -1

	def direction(self,direc):
		"""Change the pixel's direction"""
		self.hdir, self.vdir = direc

	def move(self):
		"""moves the pixel."""
		self.x += self.hdir
		self.y += self.vdir

	def draw(self,surface):
		surface.set_at((self.x,self.y), colours['white'])

class Movingbox:
	"""A moving pixel class"""

	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.hdir = 0
		self.vdir = -1
		self.boxlist = []
		self.stored = []
		self.length = 10000

	def makesquare(self):
		"""Makes a square centered at x_0,y_0"""
		i = 0
		while i < 10:
			x = self.x + (5 - i)
			k = 0
			while k < 10:
				y = self.y + (5 - k)
				self.boxlist.append((x,y))
				k += 1
			i += 1

	def direction(self,direc):
		"""Change the pixel's direction"""
		self.hdir, self.vdir = direc

	def move(self):
		"""moves the pixel."""
		self.x += self.hdir
		self.y += self.vdir

	def draw(self,surface):
		for pix in self.stored:
			surface.set_at(pix, colours['red'])
		for pix in self.boxlist:
			surface.set_at(pix, colours['white'])

		self.stored += self.boxlist
		self.boxlist = []
		if len(self.stored) >= self.length:
			self.stored = self.stored[100:]

