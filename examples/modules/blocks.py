import txt_wrangler as tw

start_block = 'block_start'
end_block = 'block_end'


def main(filename, lines, line_num, current, results):
    if current.startswith(start_block):
        nline = 0
        for line in lines:

            nline += 1
            if nline < line_num:
                continue
            if line.startswith(end_block):
                break

        nested_result = list()
        tw.read_file(filename,
                     start_line=line_num+1,
                     end_line=nline-1,
                     results=nested_result)

        results.append({"Block": nested_result})
        return nline+1
