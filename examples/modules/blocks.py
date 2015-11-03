import txt_wrangler as tw

start_pattern = 'block_start'
end_pattern = 'block_end'
storage_str = 'block'


def main(filename, lines, line_num, current, results):
    if current.startswith(start_pattern):
        nline = 0
        for line in lines:

            nline += 1
            if nline < line_num:
                continue
            if line.startswith(end_pattern):
                break

        block_contents = list()
        tw.read_file(filename,
                     start_line=line_num+1,
                     end_line=nline-1,
                     results=block_contents)

        results.append({"type": storage_str, "value": block_contents})
        return nline+1
