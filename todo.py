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

class Gui(object):
	def __init__(self,master):

		buttonframe = Frame(master)
		buttonframe.pack()
		listframe = Frame(master, bg="white")
		listframe.pack(fill=BOTH)

		self.entry = Entry(buttonframe)
		self.entry.pack(side=LEFT)
		self.button = Button(buttonframe, text="Quit", fg="red")
		self.button.pack(side=LEFT)

		self.listbox = Listbox(listframe)
		self.listbox.pack()

		self.listbox.insert(END, "a list entry")

		for item in ['one','two','three','four']:
			self.listbox.insert(END, item)
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

	root.mainloop()