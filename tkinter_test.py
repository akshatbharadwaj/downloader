#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

root = Tk()
content = ttk.Frame(root, padding = "3 3 12 12", width = 640, height = 480).grid(column = 5, row = 5)
button = ttk.Button(content, text = "Hello").grid(column = 2, row = 3)
root.mainloop()
