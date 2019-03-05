"""This is the GUI for the ecsu

validation research chimera plug-in.
"""

__version__ = '1.0'
__author__ = 'Mitchell Sheep'

import Tkinter as tk
from Tkinter import *

class PlugIn(Frame):

    def createWidgets(self):

        #here it is
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "CLOSE"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Run",
        #self.hi_there["command"] = "Pull"

        self.hi_there.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = tk.Tk()
root.title('ECSU Validation Tool')
root.geometry('300x200')
app = PlugIn(master=root)
app.mainloop()
root.destroy()
