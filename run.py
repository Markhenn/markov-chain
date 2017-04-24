"""This is a program for the codecademy final python project
It is about building a markov chain generator"""

"""## How to use the Markov Chain text generator
1. After importing this module into your main project script, create an instance of MarkovChain and assign it to a variable. For example `mc = MarkovChain()`
2. Use one of the methods to read a local text file or a string. You can call this method multiple times to add additional data.
3. Call the `generate_text()` function on the instance of MarkovChain you created to generate text from the Markov Chain. 
You can call this method multiple times to generate additional data. This function will output a list of words. If your project requires a different format, you should convert the output accordingly."""


#need to import markov chain class
from markov_python.cc_markov import MarkovChain

mc = MarkovChain()


# RnD a string from the internet to add here
mc.add_string("test test test test eibs zwo drei vier funf.")
print mc.generate_text()
print mc.generate_text()