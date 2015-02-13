import pyglet


pyglet.options['debug_lib'] = True 

# music = pyglet.media.load('/home/Penguin/Downloads/song.mp3')
# music.play()
window = pyglet.window.Window()



label = pyglet.text.Label('Pyglet is gay',
						  font_name = 'Times New Roman',
						  font_size = 36,
						  x=window.width//2, y=window.height//2,
						  anchor_x = 'center', anchor_y='center')

@window.event
def on_draw():
	window.clear()
	label.draw()

pyglet.app.run()