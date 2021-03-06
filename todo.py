from Tkinter import *
import sys, os

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

	def save(self, name):
		f = open("%s.txt" % name, 'w')
		f.write("### This list brought to you by todo.py ###\n\n")
		for item in self.list:
			f.write("{0}, {1}\n".format(str(item[0]), item[1]))
		f.close()

	def load(self, name):
		self.list = []
		f = open("%s.txt" %name, 'rU')
		contents = f.read()
		lines = contents.splitlines()
		lines = lines[2:]
		lines = lines[::-1]
		for line in lines:
			item = line.split(', ')
			self.additem(item[1])
		f.close()

class Menu(Frame):
	
	def __init__(self,parent):
		Frame.__init__(self, parent)

		top_menu = Frame(parent)
		top_menu.pack(side=TOP)

		action_area = Frame(parent)
		action_area.pack(side=TOP)

		new = Button(top_menu, text="new")
		new.pack(side=LEFT)
		save = Button(top_menu, text="save", command=lambda:self.save_to_file())
		save.pack(side=LEFT)
		load = Button(top_menu, text="load", command=lambda:self.import_from_file())
		load.pack(side=LEFT)

		self.entry = Entry(action_area, )
		self.entry.pack(side=LEFT)
		self.entry.insert(0,"type entry here")

		add = Button(action_area, text="add", command=lambda:self.add_to_list())
		add.pack(side=LEFT)

	def save_to_file(self):
		todo.save("todolist")

	def import_from_file(self):
		todo.load("todolist")
		for task in todo.list:
			gui.add_item(task)

	def add_to_list(self):
		item = self.entry.get()
		todo_tasks = [task[1].lower() for task in todo.list]
		if item == "type entry here":
			pass
		if item.lower() in todo_tasks:
			self.entry.delete(0,END)
			self.entry.insert(0,"type entry here")			
			pass
		else:
			todo.additem(item)
			gui.clear()
			for task in todo.list:
				gui.add_item(task)
			self.entry.delete(0,END)
			self.entry.insert(0,"type entry here")

class Gui(object):
	def __init__(self,master):

		menuframe = Frame(master)
		menuframe.pack(side=TOP)

		listboxframe = Frame(master)
		listboxframe.pack(side=TOP)

		self.menu = Menu(menuframe)
		self.menu.pack(side=TOP)
		self.mainview = Listbox(listboxframe)
		self.mainview.pack(side=TOP)

	def add_item(self,item):
		self.mainview.insert(END,item)

	def clear(self):
		self.mainview.delete(0,END)

if __name__ == "__main__":

	todo = Todo()
	root = Tk()
	gui = Gui(root)
	mainloop()