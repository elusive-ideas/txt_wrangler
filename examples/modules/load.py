import txt_wrangler as tw


def main(filename, lines, line_num, current, results):

    if current.startswith('load_file'):
        new_filename = current.rpartition('"')[0].rpartition('"')[2]

        dict_from_file = tw.read_file(new_filename, results=list())
        results.append(dict_from_file)
    return
