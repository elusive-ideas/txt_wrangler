'''
Usage example for txt_wrangler.

A text file is read and the contents are stored within a Python dictionary.
Once the dictionary is retrieved, it is printed.
'''

import txt_wrangler as tw
import os

# Defines path to the modules to be used
tw.files_relative_to = r'data'
tw.modules_folders = r'modules'
main_file = r'main.txt'

# Defines path to the main file to analyse as well as the modules path
os.chdir(__file__.rpartition(os.sep)[0])

# Reads the file using text_wrangler
contents_dictionary = tw.read_file(main_file)
import json
print json.dumps(contents_dictionary, indent=4)
