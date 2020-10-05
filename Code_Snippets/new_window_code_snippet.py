import tkinter as tk #imports tkinter as tk

def create_window():
	#this function just creates a new window
	window = tk.Toplevel(master)

master = tk.Tk() #the main window is created

tk.Button(master, text="Create new window", command=create_window).grid(column=0,row=0) #a button has the text "Create new window" and executes the function create_window

master.mainloop() #runs the GUI