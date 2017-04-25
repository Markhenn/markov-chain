
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
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	clean_soup = (soup.get_text())


#add to code that you only get the stuff between PREFACE and End of Project Gutenberg's The Sorrows of Young Werther, by J.W. von Goethe
	return clean_soup



#function to get rid of html code etc
def clean_code():
	return

url = "http://www.gutenberg.org/files/2527/2527-h/2527-h.htm"

print fetch_data(url)

