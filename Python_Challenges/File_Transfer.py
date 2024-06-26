import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta

# Setting up the GUI window

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")
        
        # Creates a button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        # Positions the source button in the GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        # Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        # Positions entry in the GUI using tkinter grid() padx and pady
        # are the same as the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        # Creates a button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        # Positions the destination button in the GUI using tkinter grid()
        # on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        # Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        # Positions entry in the GUI using tkinter grid() padx and pady
        # are the same as the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        # Creates a button to transfer files.
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        # Positions transfer files button
        self.transfer_btn.grid(row=2,column=1, padx=(200,0), pady=(0,15))

        # Creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        # Positions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    # Creating a new function to select source directory 
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the Entry widget,
        # this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0, END)
        # The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    # Creating a new function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the Entry widget,
        # this allows the path to be inserted into the Entry widget properly.
        self.destination_dir.delete(0, END)
        # The .insert method will insert the user selection to the source_dir Entry
        self.destination_dir.insert(0, selectDestDir)

    # Creating a new function to transfer files from one directory to another
    def transferFiles(self):
        # Gets source directory
        source = self.source_dir.get()
        # Gets destination directory
        destination = self.destination_dir.get()
        # Gets a list of files in the source directory
        source_files = os.listdir(source)
        # Gets the current date and time
        now = datetime.now()
        # Sets the threshold of now minus 24 hours
        threshold = now - timedelta(hours=24)
        # Sets up a for loop to check each file in the source files        
        for file_name in source_files:
            # Joins the file name to the directory
            file_path = os.path.join(source, file_name)
            # Checks the modified time of the file path
            file_mtime = os.path.getmtime(file_path)
            # converts the modified time from float to datetime datatype
            file_mtime_dt = datetime.fromtimestamp(file_mtime)
            # If the file is older than the threshold, move the file and
            #print that the file has been moved.
            if file_mtime_dt < threshold:
                shutil.move(source + '/' + file_name, destination)
                print(file_name + ' was successfully transferred.')        

    # Creating a function to exit the program
    def exit_program(self):
        # root is the main GUI window, the Tkinter destroy method
        # tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()