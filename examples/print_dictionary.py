'''
Usage example for txt_wrangler.

A text file is read and the contents are stored within a Python dictionary.
Once the dictionary is retrieved, it is printed.
'''

import txt_wrangler as tw
import os

os.chdir(__file__.rpartition(os.sep)[0])
file_work = r".\data\main.txt"

tw.modules_folder = r'.\modules'
contents_dictionary = tw.read_file(file_work)
print contents_dictionary
