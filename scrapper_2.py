#!/usr/bin/python3

from func import commands 

from tkinter import *
from tkinter import ttk

root = Tk()
main_frame = ttk.Frame(root, padding = (5, 12))
website_label = ttk.Label(main_frame, text = "Enter website URL:")
website_url = StringVar()
website_input_box = ttk.Entry(main_frame, textvariable = website_url)
path_label = ttk.Label(main_frame, text = "Enter download location:")
path = StringVar()
path_input_box = ttk.Entry(main_frame, textvariable = path)
browse_button = ttk.Button(main_frame, text = "Browse...")
populate_list = ttk.Button(main_frame, text = "Populate file list", command = get_list(website_url))
links_list = ttk.Frame(main_frame)


main_frame.grid(column = 0, row = 0)
website_label.grid(column = 0, row = 0, sticky = "W")
website_input_box.grid(column = 1, row = 0, columnspan = 2, pady = 5, sticky = "EW")
path_label.grid(column = 0, row = 1, sticky = "W")
path_input_box.grid(column = 1, row = 1, pady = 5)
browse_button.grid(column = 2, row = 1, sticky = "W E")
populate_list.grid(column = 2, row = 1, sticky = "E", columnspan = 2)

root.columnconfigure(1, weight = 1)


root.mainloop()