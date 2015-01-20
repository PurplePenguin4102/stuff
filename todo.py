from Tkinter import *

class Todo(object):
	def __init__(self):
		self.list = []

	def additem(self,item):
		self.list.insert(0, (0,item))
		self.orderlist()

	def orderlist(self):
		for item in self.list:
			itemdex = self.list.index(item)
			item = (itemdex+1, item[1])
			self.list[itemdex] = item

	def viewlist(self):
		return self.list

	def removeitem(self, itemnumber):
		self.list.pop(itemnumber - 1)
		self.orderlist()

	def reorder(self, item1, item2):
		templist = self.list[:]
		templist[self.list.index(item1)] = item2
		templist[self.list.index(item2)] = item1
		self.list = templist
		self.orderlist()

	def getitem(self, number):
		return self.list[number]


class Menu(Frame):
	
	def __init__(self,parent):
		Frame.__init__(self, parent)

		top_menu = Frame(parent)
		top_menu.pack(side=TOP)

		action_area = Frame(parent)
		action_area.pack(side=TOP)

		new = Button(top_menu)
		new.pack(side=LEFT)
		save = Button(top_menu)
		save.pack(side=LEFT)
		load = Button(top_menu)
		load.pack(side=LEFT)

		entry = Entry(action_area)
		entry.pack(side=LEFT)
		add = Button(action_area)
		add.pack(side=LEFT)

class Multibox(Listbox):
	def __init__(self,parent):
		Listbox.__init__(self,parent)



class Gui(object):
	def __init__(self,master):

		menu = Menu(master)
		menu.pack(side=TOP)
		mainview = Multibox(master)
		mainview.pack(side=TOP)


		# self.entry = Entry(buttonframe)
		# self.entry.pack(side=LEFT)
		# self.button = Button(buttonframe, text="Quit", fg="red")
		# self.button.pack(side=LEFT)

		# self.listbox = Listbox(listframe)
		# self.listbox.pack()

		# self.listbox.insert(END, "a list entry")

		# for item in ['one','two','three','four']:
		# 	self.listbox.insert(END, item)





if __name__ == "__main__":

	thingy = Todo()
	thingy.additem("lol")
	thingy.additem("kill the president")
	thingy.additem("do laundry")
	print thingy.viewlist()

	thingy.reorder((thingy.getitem(0)),(thingy.getitem(2)))

	print thingy.viewlist()

	thingy.removeitem(1)

	print thingy.viewlist()

	root = Tk()
	gui = Gui(root)
root
	.mainloop()