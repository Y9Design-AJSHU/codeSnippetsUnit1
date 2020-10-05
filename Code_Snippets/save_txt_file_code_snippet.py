from tkinter import * #imports everything from tkinter
import tkinter.filedialog as tkFileDialog #imports the tkinter.filedialog (the prompt to save files) as tkFileDialog

def saveas():
	#this function asks the user to create a name for the file and pick a destination
	savelocation=tkFileDialog.asksaveasfilename(defaultextension=".txt") #assigns the variable savelocation to where the user chose the save the file
	file1=open(savelocation, "w") #opens the saved empty text file to write
	file1.write("THIS IS WHAT WILL BE IN THE TEXT FILE (WILL BE REPLACED BY LYRICS)") #writes a string (will be lyrics in the actual app)
	file1.close() #closes the file

root=Tk()  #the main window is created
button=Button(root, text="Save", command=saveas).pack() #button with the text "Save" and that runs the function saveas
root.mainloop() #runs the GUI
