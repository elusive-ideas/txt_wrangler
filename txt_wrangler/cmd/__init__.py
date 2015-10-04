class Cmd(object):
    def __init__(self):
        '''Base class for Cmd.

        Defines a common interface to be used by all commands.

        '''

    def print_output(self):
        '''Print the command using the correct representation instead of the
        one that might exist in the original file.
        '''
        pass
