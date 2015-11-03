'''
Usage example for txt_wrangler.

A text file is read and the contents are stored within a Python dictionary.
Once the dictionary is retrieved, it is printed.
'''

import txt_wrangler as tw
import os

# ###################################################################
tab = 0

def f_dict(datos):
    global tab
    for par, val in datos.items():
        print "    "*(tab), par, ":",
        if isinstance(val, list):
            tab += 1
            f_lista(val)
            tab -= 1
        elif isinstance(val, dict):
            f_dict(val)
        else:
            print val

def f_lista(datos):
    print
    for val in datos:
        if isinstance(val, list):
            f_lista(val)
        elif isinstance(val, dict):
            f_dict(val)
        else:
            print val
# ###################################################################


# Defines path to the main file to analyse as well as the modules path
os.chdir(__file__.rpartition(os.sep)[0])
main_file = r".\data\main.txt"
tw.modules_folder = r'.\modules'

# Reads the file using text_wrangler
contents_dictionary = tw.read_file(main_file)

# Prints the results
# Presenta los resultados del test
print "===  Results  ".ljust(80, "=")
print contents_dictionary
print "===  Formated results  ".ljust(80, "=")
f_dict(contents_dictionary)
print '='*80
