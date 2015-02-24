"""resolutiongui summons a Tkinter gui and defines 2 variables xpos and ypos from user
input and stores them as integers. Default values for xpos and ypos are 640x480
"""

from Tkinter import *

class Gui:

    def __init__(self,master):

        master.title('Resolution/colour Input')

#we define 2 parent frames, the left side will be resolution, the right will be colour
##################################################################################
        Leftframe = Frame(master)                                               ##
        Rightframe = Frame(master)                                              ##
        BUTTFRAME = Frame(master)                                               ##
##################################################################################
                                                                                ##
        GFRAME = Frame(Rightframe)                                              ##                                      
        RFRAME = Frame(Rightframe)                                              ##
        BFRAME = Frame(Rightframe)                                              ##
        SETFRAME = Frame(Rightframe)                                            ##
        SETFRAME.pack(side=BOTTOM)                                              ##
        RFRAME.pack(side=LEFT)                                                  ##
        GFRAME.pack(side=LEFT)                                                  ##
        BFRAME.pack(side=LEFT)                                                  ##
                                                                                ##
##################################################################################
                                                                                ##
        YFRAME = Frame(Leftframe)                                               ##                                      
        XFRAME = Frame(Leftframe)                                               ##
        YFRAME.pack(side=BOTTOM)                                                ##
        XFRAME.pack(side=TOP)                                                   ##
                                                                                ##
##################################################################################
        BUTTFRAME.pack(side= BOTTOM)                                            ##
        Leftframe.pack(side = LEFT)                                             ##
        Rightframe.pack(side = RIGHT)                                           ##
##################################################################################

        self.label = Label(XFRAME, text='xpos: ')           #XFRAME's label
        self.label.pack(side=LEFT)

        self.xentry = Entry(XFRAME, width=20)               #XFRAME's entry field
        self.xentry.insert(0,640)
        self.xentry.pack(side=LEFT)

##################################################################################

        self.label = Label(YFRAME, text='ypos: ')           #YFRAME's label
        self.label.pack(side=LEFT)

        self.yentry = Entry(YFRAME, width=20)               #YFRAME's entry field
        self.yentry.insert(0,480)
        self.yentry.pack(side=LEFT)

##################################################################################
        self.label = Label(RFRAME, text='R: ')              #RFRAME's label
        self.label.pack(side=LEFT)

        self.rentry = Entry(RFRAME, width=5)               #RFRAME's entry field
        self.rentry.pack(side=LEFT)

##################################################################################

        self.label = Label(GFRAME, text='G: ')              #GFRAME's label
        self.label.pack(side=LEFT)

        self.gentry = Entry(GFRAME, width=5)               #GFRAME's entry field
        self.gentry.pack(side=LEFT)

##################################################################################

        self.label = Label(BFRAME, text='B: ')              #BFRAME's label
        self.label.pack(side=LEFT)

        self.bentry = Entry(BFRAME, width=5)               #BFRAME's entry field
        self.bentry.pack(side=LEFT)

##################################################################################
#These buttons are quick selections for colour                                   #
##################################################################################
        self.setwhite = Button(SETFRAME, text="White", fg = "white", bg = "brown",
                               command=lambda: self.setcol(values = (255,255,255)))
        self.setwhite.pack(side=LEFT)


        self.setblue = Button(SETFRAME, text="Blue", fg = "blue",
                               command=lambda: self.setcol((0,0,255)))
        self.setblue.pack(side=LEFT)


        self.setgreen = Button(SETFRAME, text="Green", fg = "green", bg = 'brown',
                               command=lambda: self.setcol((0,255,0)))
        self.setgreen.pack(side=LEFT)


        self.setred = Button(SETFRAME, text="Red", fg = "red",
                               command=lambda: self.setcol((255,0,0)))
        self.setred.pack(side=LEFT)


        self.setcyan = Button(SETFRAME, text="Cyan", fg = "cyan", bg = "brown",
                               command=lambda: self.setcol((0,255,255)))
        self.setcyan.pack(side=LEFT)


        self.setblack = Button(SETFRAME, text="Black", fg = "black",
                               command=lambda: self.setcol((0,0,0)))
        self.setblack.pack(side=LEFT)

##################################################################################
#This button will get all the data in the entry fields and return them to global #
#variables                                                                       #
##################################################################################

        self.getit = Button(BUTTFRAME, text="Start Game!", command=self.getall)
        self.getit.pack(side=LEFT)

##################################################################################
    def getall(self):
        """Stores all text fields with their displayed values as integers and makes
        a bunch of global variables

        getall(None) -> None
        xpos -> int
        ypos -> int
        (R,G,B) -> (int, int, int) 

        """
        yget = self.yentry.get()
        xget = self.xentry.get()

        global ypos 
        global xpos

        ypos = eval(yget)
        xpos = eval(xget)

        rget = self.rentry.get()
        gget = self.gentry.get()
        bget = self.bentry.get()

        global R 
        global G
        global B

        R, G, B = int(rget), int(gget), int(bget)

        global root
        root.quit()
        return

    def setcol(self,values = (0,0,0)):
        """takes a tuple of three values from 0 to 255 and inserts those values
        into the entry fields for R, G and B

        setcol((int,int,int)) -> None
        """
        self.rentry.delete(0,END)
        self.gentry.delete(0,END)
        self.bentry.delete(0,END)

        self.rentry.insert(0,values[0])
        self.gentry.insert(0,values[1])
        self.bentry.insert(0,values[2])

        return

root = Tk()

gui = Gui(root)

root.mainloop()
