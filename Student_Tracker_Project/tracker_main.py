# Python Ver:      3.11.7
#
# Author:          Danny Firth
#
# Purpose:         Student Tracker Application. Learning OOP, Tkinter GUI module,
#                  using Tkinter Parent and Child relationships.
#
# Tested OS:       This code was written and tested to work with Windows 11.

from tkinter import *
import tkinter as tk

import tracker_gui
import tracker_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,350)
        self.master.maxsize(500,350)

        tracker_func.center_window(self,500,350)
        self.master.title("Student Tracker Program")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: tracker_func.ask_quit(self))

        tracker_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()