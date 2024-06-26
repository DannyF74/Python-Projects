import tkinter as tk
from tkinter import *
import webbrowser


# Creates a new ParentWindow class and sets up a label above the text entry box
# and then sets up three buttons going to our three methods defined below.
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.enter_label = Label(self.master, text="Enter custom text or click the Default HTML Page button")
        self.enter_label.grid(row=0, column=0, padx=(10,0), pady=(10,10))
        self.enter_box = Entry(self.master, width=150)
        self.enter_box.grid(row=1, column=0, columnspan=6, padx=(10,0), pady=(10,10))
        self.default_btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=2, column=3, padx=(10,10), pady=(10,10))
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custom_btn.grid(row=2, column=4, padx=(10,10), pady=(10,10))
        self.exit_btn = Button(self.master, text="Exit", width=30, height=2, command=self.exitWindow)
        self.exit_btn.grid(row=2, column=5, padx=(10,10), pady=(10,10))

    # This button defines a method that will create a default HTML page
    def defaultHTML(self):
        # This is the text that will be written in the body of the page
        htmlText = "Stay tuned for our amazing summer sale!"
        # This creates a new HTML file with write permissions
        htmlFile = open("index.html", "w")
        # This defines the HTML content that will be written in the html file
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        # This writes the content in the html file
        htmlFile.write(htmlContent)
        # This closes the html file
        htmlFile.close()
        # This opens a new tab in a web browser to the html file.
        webbrowser.open_new_tab("index.html")

    # This method will allow the user to put in custom text to display on the web page
    def customHTML(self):
        # This gets the text that is currently written in the enter box.
        htmlText = self.enter_box.get()
        htmlFile = open("custom.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        # This deletes the text from the enter box when the web page is created.
        # This saves the user from having to delete everything when making a new
        # web page
        self.enter_box.delete(0, END)
        webbrowser.open_new_tab("custom.html")

    # This method is used when the exit button is clicked. This closes the program.
    def exitWindow(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()