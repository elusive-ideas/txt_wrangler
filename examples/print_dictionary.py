'''
Usage example for txt_wrangler.

A text file is read and the contents are stored within a Python dictionary.
Once the dictionary is retrieved, it is printed.

{'file': [
         {'filename': '.\\data\\example.txt'},
         {'content': [
                     {'Comment': 'Comment in block'},
                     {'Block': []},
                     {'Comment': 'Comment in block (in file)'},
                     {'file': [
                              {'filename': '.\\data\\2File.txt'},
                              {'content': [
                                          {'Block': []},
                                          {'Comment': 'Comment between blocks (in file)'},
                                          {'Block': []},
                                          {'file': [
                                                   {'filename': '.\\data\\3File.txt'},
                                                   {'content': [
                                                               {'Block': []},
                                                               {'Block': []},
                                                               {'Block': []}
                                                               ]
                                                    }
                                                    ]
                                           },
                                           {'Block': []}
                                           ]
                                }
                                ]
                    },
                    {'Block': []},
                    {'Comment': 'Comment between blocks'},
                    {'Block': []}
                    ]
            }
            ]
}

{'file': [
         {'filename': '.\\data\\main.txt'},
         {'content': [
                     {'Block': [
                               {'Comment': 'Comment in block'}
                               ]
                     },
                     {'file': [
                              {'filename': '.\\data\\2nd.txt'},
                              {'content': [
                                          {'Block': []},
                                          {'Comment': 'Comment between blocks (in file)'},
                                          {'Block': []},
                                          {'file': [
                                                   {'filename': '.\\data\\3rd.txt'},
                                                   {'content': [
                                                               {'Block': []},
                                                               {'Block': []},
                                                               {'Block': [
                                                                         {'Comment': 'Comment in block (in file)'}
                                                                         ]
                                                               }
                                                               ]
                                                   }
                                                   ]
                                          },
                                          {'Block': []}
                                          ]
                              }
                              ]
                     },
                     {'Block': []},
                     {'Comment': 'Comment between blocks'},
                     {'Block': []}
                     ]
         }
         ]
}

'''

import txt_wrangler as tw
import os

os.chdir(__file__.rpartition(os.sep)[0])
file_work = r".\data\main.txt"

tw.modules_folder = r'.\modules'
contents_dictionary = tw.read_file(file_work)
print contents_dictionary
