#!/usr/bin/python3
# hello_tkinter.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# import the tkinter module - everything
from tkinter import *

# call the Tk constructor and build a top level window assign it to root.
root = Tk()

#create a label and place it in the window via pack
Label(root, text="Hello, Tkinter!").pack()

# call the mainloop method
root.mainloop()
