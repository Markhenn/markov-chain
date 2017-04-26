
#use the first.py programm to pull data from project gutenberg


"""
Help to get data from project gutenberg

import urllib2

response = urllib2.urlopen("http://www.gutenberg.org/files/135/135-h/135-h.htm")
html = response.read()

sad = 0

list_of_words = html.split(' ')

for word in list_of_words:
	if word == "sad":
		sad += 1

print sad"""

import urllib2
from bs4 import BeautifulSoup


#function to fetch data
def fetch_data(url):
	#get html from gutenberg
	response = urllib2.urlopen(url)
	html = response.read()
	#clean up text
	soup = BeautifulSoup(html, 'html.parser')
	clean_soup = (soup.get_text())
	#cut text to only the story
	start_index = clean_soup.find("I have carefully")
	end_index = clean_soup.find("End of Project")
	story = clean_soup[int(start_index):int(end_index)]



#add to code that you only get the stuff between PREFACE and End of Project Gutenberg's The Sorrows of Young Werther, by J.W. von Goethe - num_preface = soup.find_all(string="Werther")
	return story



#function to get rid of html code etc
def clean_code():
	return

url = "http://www.gutenberg.org/files/2527/2527-h/2527-h.htm"

print fetch_data(url)

