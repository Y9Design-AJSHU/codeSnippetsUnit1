import tkinter as tk #imports tkinter
from tkinter.ttk import * #used for styling anf other extra features of tkinter
from tkinter import ttk #used for styling anf other extra features of tkinter
from bs4 import BeautifulSoup #used for webscraping
import requests #used for http requests

def lyrics(artist, song):
	#this function scrapes the lyrics from the site and makes them presentable
	base = "https://www.azlyrics.com/" #the base of the azlyrics url
	artistNew = artist.lower().replace(" ", "") #removing spaces so the lyrics can be put into the url
	songNew = song.lower().replace(" ", "") #removing spaces so the lyrics can be put into the url
	url = base+"lyrics/"+artistNew+"/"+songNew+".html" #creates the url
	req = requests.get(url) #request from the url
	soup = BeautifulSoup(req.content, "html.parser") #opens the url for web-scraping
	lyrics = soup.find_all("div", attrs={"class": None, "id": None}) #finds all divs with no class or id
	for x in lyrics: 
		#for loop extracts all the textx
		lyrics = x.getText() 
	return lyrics #returns lyrics
	
def printLyrics():
	#this function prints the song lyrics
	songNow=songTitle.get() #assigns the variable songNow to the content of the songTitle entry
	artistNow=artistTitle.get() #assigns the variable artistNow to the artistTitle entry
	print(lyrics(artistNow,songNow)) #prints what is returned when the artistNow and songNow variables are passed as the parameters of the lyrics function

master = tk.Tk() #creates main window
style = ttk.Style() #assigns the variable style to the ttk styling
style.theme_use('default') #uses default styling

style.configure("2orange.horizontal.TEntry", foreground='#ff8f00', font=("System", 20)) #creates styling for entries
style.configure("2orange.TButton", background='#ff8f00',foreground="black", font=("System", 20)) #creates styling for buttons
style.configure("2orange.TLabel", foreground='#ff8f00',background="white", font=("System", 20)) #creates styling for labels

	
Label(master, text="Enter the Song Title:", style="2orange.TLabel").grid(row=0, column=0, pady='5px', padx='10px') #creates the "Enter Song Title:" label
Label(master, text="Enter the Artist:", style="2orange.TLabel").grid(row=1, column=0, pady='5px', padx='10px') #creates the "Enter the Artist:" label
songTitle = Entry(master, width=15,style='2orange.horizontal.TEntry',font=("System", 20)) #creates the songTitle entry
artistTitle = Entry(master, width=15,style='2orange.horizontal.TEntry',font=("System", 20)) #creates the artistTitle entry
Button(master, text="Find Lyrics", command=printLyrics, style='2orange.TButton').grid(row=3, column=0, columnspan=2, pady='10px', padx='10px') #creates the "Find Lyrics" button which runs the printLyrics function


songTitle.config(width=15) #sets the width of the songTitle entry
artistTitle.config(width=15) #sets the width of the aristTitle entry
songTitle.grid(row=0, column=1, pady='5px', padx='10px') #places the songTitle entryon the right spot on the grid
artistTitle.grid(row=1, column=1, pady='5px', padx='10px') #places the artistTitle entryon the right spot on the grid

master.mainloop() #runs the GUI

