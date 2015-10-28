######
FILTER = "_bk: "


# Requeriments: lines, line_num, current, start_block, end_block... results.
def main(lines, line_num, current, start_block, end_block, results, modules):
    if start_block in current:
        out = list()
        nline = 0
        for line in lines:
            nline += 1
            if nline < line_num:
                continue
            if nline == line_num:
                out.append(FILTER)
            line = line.rstrip()
            out.append(line)
            if end_block in line:
               break
        results.extend([out])
        # Make sure the end_block exist
        if not (end_block in line):
            raise ValueError('Lines out of boundaries..')
