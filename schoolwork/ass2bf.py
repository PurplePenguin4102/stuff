###################################################################
#
#   CSSE1001/7030 - Assignment 2
#
#   Student Number: s4081775
#
#   Student Name: Joseph Ray
#
###################################################################

#
# Do not change the following import
#

from assign2_support import *



####################################################################
#
# Insert your code below
#
####################################################################

class PVData(object):
	def __init__(self):
		self.date = yesterday()
		self.data = load_data(self.date)
		self._populate_powers()

	def _populate_powers(self):
		"""This function internally populates a dictionary {Array: list}
		called self.powers, this makes the call get_power less computationally
		intensive as we don't have to construct a whole dictionary just to 
		retrieve one list
		"""
		self.powers = {}		
		for arr in ARRAYS:
			self.powers[arr] = []

		for event in self.data:
			for arr in ARRAYS:
				self.powers[arr].append(event[3][ARRAYS.index(arr)])		

	def change_date(self,date):
		""" takes a date string and changes the internal value self.date,
		also fetches a fresh set of data if the date is different"""

		if self.date != date:
			self.date = date
			self.data = load_data(self.date)
			self._populate_powers()

	def get_date(self):
		"""returns the internal variable self.date"""

		return self.date

	def get_time(self, time_index):
		"""returns the time string from self.data"""

		return self.data[time_index][0]

	def get_temperature(self):
		"""constructs a list of temperatures from self.data and returns the list"""

		templist = []
		for event in self.data:
			templist.append(event[1])
		
		return templist

	def get_sunlight(self):
		"""constructs a list of sunlight values from self.data and returns the list"""

		sunlist = []
		for event in self.data:
			sunlist.append(event[2])
		
		return sunlist		

	def get_power(self,array):
		"""returns a single list from the dictionary self.powers that is constructed in
		self._populate_powers"""

		return self.powers[array]

	def get_cumulative_energy(self,array):

		ind = ARRAYS.index(array)
		answer = []
		cum_sum = 0

		for event in self.data:
			cum_sum += event[3][ind]
			answer.append(cum_sum)

		return answer

	def length(self):
		"""returns the length of self.data, useful for indexing"""

		return len(self.data)


class Plotter(Canvas):

	def __init__(self,parent,data, Options):

		Canvas.__init__(self,parent, bg = "white", width = 640, height = 480)

		topframe = Frame(parent)
		topframe.pack(side=TOP,fill=X)
		self.toplabel = Label(parent,text="")
		self.toplabel.pack(anchor=W)

		self.data = data
		self.index = self.data.length()
		self.Options = Options
		self.width = self.winfo_reqwidth()
		self.height = self.winfo_reqheight()

		self.xy = CoordinateTranslator(self.width,self.height,self.index)

		self.bind('<Button-1>', self._click_event)
		self.bind('<B1-Motion>', self._move_event)
		self.bind('<ButtonRelease-1>', self._release_event)
		self.bind('<Configure>', self._on_resize)

		self._redraw(buttpress = 1) #buttpress = 1 is the equivalent of saying "Get self.date when calling _redraw." corresponds to "apply" button in OptionsFrame

	def _format_string(self, event):

		if event:
			
			temp,sun,pwr = [None,None,None]

			ind = self.xy.get_index(event.x)
			if self.temp: temp = self.templist[ind]
			if self.sun: sun = self.sunlist[ind]
			if self.pwr: pwr = self.pwrlist[ind]

			prettystring = pretty_print_data(self.date,self.data.get_time(ind),
											temp,sun,pwr)
			print event.type
			
			if event.type=='5':	prettystring = pretty_print_data(self.date,None,None,None,None)

		else:
			prettystring = pretty_print_data(self.date,None,None,None,None)
		
		self.toplabel.config(text=prettystring)

	def _get_options(self, buttpress = None, resize = False):
		if not resize:
			if buttpress: self.date = self.Options.entry.get()
			self.pwr = self.Options.pwr.get()
			self.temp = self.Options.temp.get()
			self.sun = self.Options.sun.get()
			self.arr = self.Options.selected.get()

	def _set_date(self, resize = False):
		if not resize:
			try:
				self.data.change_date(self.date)		
			except Exception as e:
				tkMessageBox.showerror("Error",str(e))

	def _get_coords(self, resize = False):

		if resize: self.xy.resize(self.width,self.height)

		if self.pwr:
			self.pwrlist = self.data.get_power(self.arr)			
			self.pwrcoords = [self.xy.power_coords(i,self.pwrlist[i],self.arr) for i in range(self.index)]
		if self.temp:
			self.templist = self.data.get_temperature()	 
			self.tempcoords = [self.xy.temperature_coords(i,self.templist[i]) for i in range(self.index)]
		if self.sun:
	 		self.sunlist = self.data.get_sunlight()
			self.suncoords = [self.xy.sunlight_coords(i,self.sunlist[i]) for i in range(self.index)]

	def _redraw(self, event=None, buttpress = None, resize = False):
		
		if not event:
			self._get_options(buttpress,resize)
			self._set_date(resize)
			self._get_coords(resize)

		self._format_string(event)
		
		self.delete(ALL)

		if self.pwr: self.create_polygon(self.pwrcoords, fill = POWER_COLOUR)
		if self.temp: self.create_line(self.tempcoords, fill = 'red')
		if self.sun: self.create_line(self.suncoords, fill = 'orange')

	def _click_event(self,event):
		self._redraw(event)
		self.create_line((event.x,0),(event.x,self.height))

	def _move_event(self,event):
		self._redraw(event)
		self.create_line((event.x,0),(event.x,self.height))

	def _release_event(self,event):
		self._redraw(event)

	def _on_resize(self,event):
		self.width, self.height = event.width, event.height
		self._redraw(resize = True)


class OptionsFrame(Frame):
	def __init__(self,parent,plot):
		Frame.__init__(self,parent)

		entryframe = Frame(parent)
		entryframe.pack(side=BOTTOM, fill = X)
		checkframe = Frame(parent)	
		checkframe.pack(side=BOTTOM)

		self.pwr = IntVar()
		self.temp = IntVar()
		self.sun = IntVar()
		self.pwr.set(1)

		Checkbutton(checkframe, text= 'Power', variable= self.pwr, command = plot).pack(side=LEFT)
		Checkbutton(checkframe, text= 'Temperature', variable= self.temp, command = plot).pack(side=LEFT)
		Checkbutton(checkframe, text= 'Sunlight', variable= self.sun, command = plot).pack(side=LEFT)

		Label(entryframe, text = 'Choose Date:').pack(side = LEFT)
		self.entry = Entry(entryframe, width = 20)
		self.entry.insert(0,yesterday())
		self.entry.pack(side=LEFT)
		Button(entryframe, text = 'Apply', command = lambda: plot(buttpress = 1)).pack(side=LEFT)

		self.selected = StringVar(parent)
		self.selected.set(ARRAYS[-1])
		
		OptionMenu(entryframe, self.selected, *ARRAYS, command = plot).pack(side = RIGHT, anchor = E)

class PVPlotApp(object):
	def __init__(self,master):

		master.title('PV Plotter')
		data = PVData()

		Options = OptionsFrame(master,self.plot)
		Options.pack(side=BOTTOM)
		self.Plot = Plotter(master, data, Options)
		self.Plot.pack(side=TOP, expand=True, fill=BOTH)

	def plot(self, event=None, buttpress = None):
		self.Plot._redraw(buttpress = buttpress)

###################################################################
#
#WARNING: Leave the following code at the end of your code
#
#DO NOT CHANGE ANYTHING BELOW
#
###################################################################

def main():
    root = Tk()
    app = PVPlotApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
