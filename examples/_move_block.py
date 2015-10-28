### MOVE BLOCK

# LIBRARY ............................................................
def move_block(blocks, source, target):
    ''' Move a block from source to target.
    Input:
        blocks:         list of strings - diferents blocks
        source:         Integer         - Position of the initial block (1...)
        target:         Integer         - Position of the final block (1...)
    Output:
        blocks:         List of strings - Original modified
    '''
    # Make sure that 1st argument is a list
    assert isinstance(blocks, list), "The argument 'Blocks' is not a list"
    # Make sure that 2nd argument is a number
    assert isinstance(source, int), "The argument 'Source' is not a number"
    # Make sure that 3rd argument is a number
    assert isinstance(target, int), "The argument 'Target' is not a number"
    # Make sure that 2nd argument is a number between 1 and the maxim number of blocks
    assert source >= 1 and source <= len(blocks), "The value 'Source' is out of range: 1...MaximNumBlock"
    # Make sure that 3rd argument is a number between 1 and the maxim number of blocks
    assert target >= 1 and target <= len(blocks), "The value 'Target' is out of range: 1...MaximNumBlock"
    # Make sure that 2nd and 3rd arguments are diferents
    assert source is not target, "The values 'Source' and 'Target' are the same"

    source -= 1
    target -= 1

    block_to_move = blocks[source]
    del blocks[source]
    blocks.insert(target, block_to_move)
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

# MUEVE un bloque de posicion (1,3) (3,1) (1,1) (4,1) (1,4)
move_block(blocks, 3, 1)

# imprime el bloque despues de ...
printtest("FINALY ", blocks)
