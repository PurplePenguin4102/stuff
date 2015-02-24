import pygame
import random
from dictionaries import *

class Worm(object):
	"""A worm"""

	def __init__(self,surface,x,y,length):
		self.surface = surface
		self.x = x
		self.y = y
		self.length = length
		self.dir_x = 0
		self.dir_y = -1
		self.body = []
		self.crashed = False

	def key_event(self,event):
		"""Handle key events that affect the worm."""
		if event.key in wormcommands:
			(self.dir_x,self.dir_y) = wormcommands[event.key]

	def move(self):
		"""Move the worm"""
		self.x += self.dir_x
		self.y += self.dir_y

		r,g,b,a = self.surface.get_at((self.x, self.y))
		if (r,g,b) != (0,0,0):
			self.crashed = True

		self.body.insert(0,(self.x,self.y))

		if len(self.body) > self.length:
			self.body.pop()

	def draw(self):
		colour = (255,255,255)
		for x,y in self.body:
			self.surface.set_at((x,y),colour)

	def getlonger(self):
		self.length += 50

def newcol(colour,string1):

	if string1 == 'white':
		return (colour[0],colour[1]-1,colour[2]-1)
	if string1 == 'red':
		return (colour[0]-1,colour[1]+1,colour[2])
	if string1 == 'green':
		return (colour[0],colour[1]-1,colour[2]+1)
	if string1 == 'blue':
		return (colour[0]+1,colour[1]+1,colour[2])