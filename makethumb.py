import os, sys
from PIL import Image

size = (100,100)

print os.getcwd()
files = os.listdir('.')

for f in files:
	thumbcheck = f.split('.')
	print thumbcheck
	if thumbcheck[0][:3:-1] != 'bmuht':
		im = Image.open(f)
		im.thumbnail(size)
		im.save(thumbcheck[0] + "thumb." + thumbcheck[1], "JPEG")
	else:
		print "Already a thumbnail"
