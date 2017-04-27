
#This Program fetches data from a web page and displays just text


import urllib2
from bs4 import BeautifulSoup


#function to fetch data
def fetch_data(url):
	#get html from gutenberg
	response = urllib2.urlopen(url)
	html = response.read()
	return clean_code(html)



#function to get rid of html code etc
def clean_code(html):
	#clean up text
	soup = BeautifulSoup(html, 'html.parser')
	clean_soup = (soup.get_text())
	#cut text to only the story
	start_index = clean_soup.find("I have carefully")
	end_index = clean_soup.find("End of Project")
	story = clean_soup[int(start_index):int(end_index)]
	return story



