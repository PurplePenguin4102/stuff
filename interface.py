import pyglet

pyglet.lib.load_library('avbin')
pyglet.have_avbin=True

music = pyglet.media.load('C:\work\\song.mp3')
music.play()
# window = pyglet.window.Window()



# label = pyglet.text.Label('Hiya!!',
# 						  font_name = 'Times New Roman',
# 						  font_size = 36,
# 						  x=window.width//2, y=window.height//2,
# 						  anchor_x = 'center', anchor_y='center')

# @window.event
# def on_draw():
# 	window.clear()
# 	label.draw()

pyglet.app.run()