import requests #used for http requests
from bs4 import BeautifulSoup #used for webscraping



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
	
songInput = input("What song would you like to see the lyrics for? --> ") #asks for song title
artistInput = input("Who is the artist? --> ") #asks for artist
print() #line break
print(lyrics(artistInput,songInput)) #prints what the lyrics function returns when the artistInput and songInput are passed as the parameters