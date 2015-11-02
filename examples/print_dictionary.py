'''
Usage example for txt_wrangler.

A text file is read and the contents are stored within a Python dictionary.
Once the dictionary is retrieved, it is printed.
'''

import txt_wrangler as tw
import os

# Defines path to the main file to analyse as well as the modules path
os.chdir(__file__.rpartition(os.sep)[0])
main_file = r".\data\main.txt"
tw.modules_folder = r'.\modules'

# Reads the file using text_wrangler
contents_dictionary = tw.read_file(main_file)

# Prints the results
print contents_dictionary
