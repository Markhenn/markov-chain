"""This is a program for the codecademy final python project
It is about building a markov chain generator"""

"""## How to use the Markov Chain text generator
1. After importing this module into your main project script, create an instance of MarkovChain and assign it to a variable. For example `mc = MarkovChain()`
2. Use one of the methods to read a local text file or a string. You can call this method multiple times to add additional data.
3. Call the `generate_text()` function on the instance of MarkovChain you created to generate text from the Markov Chain. You can call this method multiple times to generate additional data. This function will output a list of words. If your project requires a different format, you should convert the output accordingly."""


"""Planning of the prgramm parts

1) how many excerpts
2) fetch data from that book
3) generate markov chain
4) get data from chain based on how many they want
5) present the data formated

"""


#need to import markov chain class
from markov_python.cc_markov import MarkovChain
import fetch_data

mc = MarkovChain()


#this is the starter function
def start_here():
	return

#function to format data
def format_text():
	return


#create the raw text from project gutenberg
url = "http://www.gutenberg.org/files/2527/2527-h/2527-h.htm"
raw_text = fetch_data.fetch_data(url)



# RnD a string from the internet to add here
mc.add_string(raw_text)
print mc.generate_text()
print mc.generate_text()