######
FILTER = "_hchy: "

# Requeriments: lines, line_num, start_pattern, end_pattern... results.
def main(lines, line_num, current, start_block, end_block, results, modules):
    if start_block in current:
        nline = 0
        for line in lines:
            nline += 1
            if nline < line_num:
                continue
            if 'name' in line:
                results.append(FILTER+"\'"+line.rpartition('\'')[0].rpartition('\'')[2]+"\'")
            if end_block in line:
                break
        # Make sure the end_block exist
        if not (end_block in line):
            raise ValueError('Lines out of boundaries..')
