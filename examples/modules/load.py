import txt_wrangler as tw

pattern = 'load_file'


def main(filename, lines, line_num, current, results):

    if current.startswith(pattern):
        new_filename = current.rpartition('"')[0].rpartition('"')[2]

        dict_from_file = tw.read_file(new_filename, results=list())
        results.append(dict_from_file)
    return
