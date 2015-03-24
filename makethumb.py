#Small script for creating thumbnails from jpegs! Requires Pillow to be installed 
#on the machine. Requires Python and pip (though you should already have these 
#if you're using pillow). Simply move the jpgs you wish to convert into the same
#folder as the script and run the script. Change the size parameter if you want 
#something other than thumbs that are 100xA or Ax100 dimensions (A < 100)
#TODO: subdirectory support, GUI, portability, filetype support for non jpg.

import os, sys
from PIL import Image

size = (100,100) #Change this to change thumbnail size

print os.getcwd()
files = os.listdir('.')
for f in files:
	if f.split('.')[1] != 'jpg':
		files.remove(f)

for f in files:
	thumbcheck = f.split('.')
	print thumbcheck
	if thumbcheck[0][-5:] != 'thumb':
		im = Image.open(f)
		im.thumbnail(size)
		im.save(thumbcheck[0] + "thumb." + thumbcheck[1], "JPEG")
	elif thumbcheck[0] == 'thumb':
		im = Image.open(f)
		im.thumbnail(size)
		im.save(thumbcheck[0] + "thumb." + thumbcheck[1], "JPEG")		
	else:
		print "Already a thumbnail"
