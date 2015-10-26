### DUPLICATE BLOCK

# LIBRARY ............................................................
def dup_block(blocks, index):
    ''' Duplicate a block from and to index.
    Input:
        blocks:      	list of strings - diferents blocks
        index:  	    Integer         - Block and position for duplicate (1...)
     Output:
        blocks:			List of strings - Original modified
    '''
    # Make sure that 1st argument is a list of blocks
    assert isinstance(blocks, list), "The argument 'Blocks' is not a List"
    # Make sure that 2nd argument is a number
    assert isinstance(index, int), "The argument 'Index' is not a number"
    # Make sure that 2nd argument is a number between 1 and the maxim number of blocks
    assert index >= 1 and index <= len(blocks), "The value 'Index' is out of range: 1...MaximNumBlock"

    index -= 1

    block_to_duplicate = blocks[index]
    blocks.insert(index, block_to_duplicate)
# TEST ...............................................................
def printtest(head, cont):
    ''' Print Blocks ... for test
    Input:
        head:           Head of the print
        conty:          list of strings - diferents blocks
    Output:
        SCREEN          Head, Lines of Blocks, End
    '''
    print head + '='*(80-len(head))
    for line in cont:
        print line
    print '='*80
# ....................................................................

import txt_wrangler as tw

# Consigue todos los bloques del archivo de texto 'example.txt'
blocks = tw.get_blocks_in_file(file_name='_example.txt',
                               start_pattern='block_start',
                               end_pattern='block_end')

# imprime el bloque antes de ...
printtest("INITIALY ", blocks)

# MUEVE un bloque de posicion (1) (3) (5)
dup_block(blocks, 1)

# imprime el bloque despues de ...
printtest("FINALY ", blocks)
