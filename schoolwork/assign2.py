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
		self.powers = dict([(a,[elem[3][ARRAYS.index(a)] for elem in self.data]) for a in ARRAYS])

	def change_date(self,date):
		if self.date != date:
			self.data = load_data(date)
			self.date = date
			self._populate_powers()

	def get_date(self): 
		return self.date

	def get_time(self, time_index): 
		return self.data[time_index][0]

	def get_temperature(self): 
		return [elem[1] for elem in self.data]

	def get_sunlight(self):	
		return [elem[2] for elem in self.data]	

	def get_power(self,array):
		return self.powers[array]

	def get_cumulative_energy(self,array):
		return [sum(self.powers[array][:i+1]) for i in xrange(len(self.powers[array]))]

	def length(self):
		return len(self.data)

class Plotter(Canvas):

	def __init__(self,parent,data,Options):

		Canvas.__init__(self,parent, bg='white', width=640, height=480)

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
		self.bind('<B1-Motion>', self._click_event)
		self.bind('<ButtonRelease-1>', self._release_event)
		self.bind('<Configure>', self._on_resize)

		#setting buttpress to 1 changes the date on redraw
		self._redraw(buttpress=1) 

	def _format_header(self,event):

		if event:
			
			temp,sun,pwr = [None,None,None]
			ind = self.xy.get_index(event.x)
			
			if self.temp: temp = self.templist[ind]
			if self.sun: sun = self.sunlist[ind]
			if self.pwr: pwr = self.pwrlist[ind]

			# event.type '5' corresponds to mousebutton-1 release. 
			if event.type == '5': header = pretty_print_data(self.date,None,None,None,None)
			else: header = pretty_print_data(self.date,self.data.get_time(ind),temp,sun,pwr)

		else: header = pretty_print_data(self.date,None,None,None,None)
		
		self.toplabel.config(text=header)

	def _get_options(self, resize=False):

		if not resize:
			self.pwr = self.Options.pwr.get()
			self.temp = self.Options.temp.get()
			self.sun = self.Options.sun.get()
			self.arr = self.Options.selected.get()

	def _change_date(self):

		tempdate = self.Options.entry.get()
		try:
			self.data.change_date(tempdate)
			self.date = tempdate
		except Exception as e:
			tkMessageBox.showerror("Error",str(e))		

	def _get_coords(self, resize=False):

		if resize: self.xy.resize(self.width,self.height)

		if self.pwr:
			self.pwrlist = self.data.get_power(self.arr)			
			self.pwrcoords = [self.xy.power_coords(i,self.pwrlist[i],self.arr) 
													for i in range(self.index)]
		if self.temp:
			self.templist = self.data.get_temperature()	 
			self.tempcoords = [self.xy.temperature_coords(i,self.templist[i])
													for i in range(self.index)]
		if self.sun:
	 		self.sunlist = self.data.get_sunlight()
			self.suncoords = [self.xy.sunlight_coords(i,self.sunlist[i]) 
													for i in range(self.index)]

	def _redraw(self, event=None, buttpress=None, resize=False):
		
		if not event:
			if buttpress: self._change_date()
			self._get_options(resize)
			self._get_coords(resize)

		self._format_header(event)
		
		self.delete(ALL)

		if self.pwr: self.create_polygon(self.pwrcoords, fill=POWER_COLOUR)
		if self.temp: self.create_line(self.tempcoords, fill='red')
		if self.sun: self.create_line(self.suncoords, fill='orange')

	def _click_event(self,event):
		self._redraw(event)
		self.create_line((event.x,0),(event.x,self.height))

	def _release_event(self,event):
		self._redraw(event)

	def _on_resize(self,event):
		self.width, self.height = event.width, event.height
		self._redraw(resize=True)

class OptionsFrame(Frame):

	def __init__(self,parent,plot):

		Frame.__init__(self,parent)
		
		self.parent = parent
		self.plot = plot

		self._make_entryfields()
		self._make_checkbuttons()

	def _make_checkbuttons(self):

		checkframe = Frame(self.parent)	
		checkframe.pack(side=BOTTOM)

		self.pwr = IntVar()
		self.temp = IntVar()
		self.sun = IntVar()
		self.pwr.set(1)

		Checkbutton(checkframe, text='Power', variable=self.pwr, 
											command=self.plot).pack(side=LEFT)
		Checkbutton(checkframe, text='Temperature', variable=self.temp, 
											command=self.plot).pack(side=LEFT)
		Checkbutton(checkframe, text='Sunlight', variable=self.sun, 
											command=self.plot).pack(side=LEFT)

	def _make_entryfields(self):

		entryframe = Frame(self.parent)
		entryframe.pack(side=BOTTOM, fill=X)

		Label(entryframe, text='Choose Date:').pack(side=LEFT)
		self.entry = Entry(entryframe, width=20)
		self.entry.insert(0,yesterday())
		self.entry.pack(side=LEFT)
		Button(entryframe, text='Apply', 
						command=lambda: self.plot(buttpress=1)).pack(side=LEFT)

		self.selected = StringVar(self.parent)
		self.selected.set(ARRAYS[-1])

		OptionMenu(entryframe, self.selected, *ARRAYS, 
								command=self.plot).pack(side=RIGHT, anchor=E)

class PVPlotApp(object):

	def __init__(self,master):

		master.title('PV Plotter')
		data = PVData()

		Options = OptionsFrame(master,self.plot)
		Options.pack(side=BOTTOM)
		self.Drawing = Plotter(master, data, Options)
		self.Drawing.pack(side=TOP, expand=True, fill=BOTH)

	def plot(self, event=None, buttpress=None):
		self.Drawing._redraw(buttpress=buttpress)

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
