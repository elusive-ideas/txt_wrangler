import os.path
import block
import cmd
#comment Tomas

def get_block_lines(file_name, start_pattern, end_pattern, from_line=1):
    '''
    Get the first and last line of a block that meets the pattern provided in
    the file specified (starting from the line provided).

    Input:
        file_name:      String  - Name of the file
        start_pattern:  String  - Pattern that defines the block start
        end_pattern:    String  - Pattern that defines the block end
        from_line:      Integer - Line from which the block is being searched

    Output:
        Tuple with 2 integers - First and Last line of the block found

    '''

    all_lines = list()
    first = 0
    last = 0

    # Check file existence
    assert os.path.isfile(file_name), ("The file specified does not exist: "
                                       "'%s'" % file_name)

    # Make sure that 'from_line' is higher or equal to 1
    assert from_line >=1, ("The value for 'from_line' must be higher or equal "
                           "to 1. Current value: %s" % from_line)

    with open(file_name,'r') as f:
        all_lines = f.readlines()

    line_num = 1
    for line in all_lines:
        if line_num < from_line:
            line_num += 1
            continue
        line = line.strip()
        if not first:
            if line.endswith('\n'):
                line = line[:-1]
            if line == start_pattern:
                first = line_num
                continue

        if first and not last:
            if line.endswith('\n'):
                line = line[:-1]
            if line == end_pattern:
                last = line_num+1

        line_num += 1

    return first, last


def get_lines(file_name, first=1, last=1):
    ''' Get lines from a text file

    Input:
        file_name:   String  - Name of the file
        first:       Integer - First line to be read
        last:        Integer - Last line to be read

    Output:
        List of strings

    '''

    # Check file existence
    assert os.path.isfile(file_name), ("The file specified does not exist: "
                                       "'%s'" % file_name)

    # Make sure that 'first' is higher or equal to 1
    assert first >=1, ("The value for 'first' must be higher or equal "
                       "to 1. Current value: %s" % first)

    # Make sure that 'last' is never smaller than 'first'
    assert last >= first, ("The value of 'last' should never be lower than "
                           "'first'.")

    extracted_lines = list()

    with open(file_name,'r') as f:
        all_lines = f.readlines()
        number_of_lines = len(all_lines) + 1

        # Make sure the requested lines fall within the length of the file
        if not (first >= 0 and (last >= first and last <= number_of_lines)):
            raise ValueError('Lines out of boundaries..')

        current_line_num = 1
        for line in all_lines:
            if current_line_num >= first and current_line_num <= last:
                if line.endswith('\n'):
                    extracted_lines.append(line[:-1])
                else:
                    extracted_lines.append(line)
            current_line_num +=1


    return extracted_lines


def get_blocks_in_file(file_name, start_pattern, end_pattern):
    ''' Get all blocks that meet the pattern provided in the file specified.

    Input:
        file_name:      String  - Name of the file
        start_pattern:  String  - Pattern that defines the block start
        end_pattern:    String  - Pattern that defines the block end

    Output:
        List of lists of strings

    '''

    blocks = list()

    first, last = get_block_lines(file_name=file_name,
                                  start_pattern=start_pattern,
                                  end_pattern=end_pattern)

    while first:
        if not first and not last:
            break

        block = get_lines(file_name, first, last)
        blocks.append(block)
        first, last = get_block_lines(file_name=file_name,
                                      start_pattern=start_pattern,
                                      end_pattern=end_pattern,
                                      from_line=last+1)

    return blocks
