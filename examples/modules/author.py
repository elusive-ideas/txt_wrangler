pattern = 'author'
storage_str = 'author'


def main(filename, lines, line_num, current, results):
    if current.startswith(pattern):
        value = current.rpartition('=')[2].strip().strip("'")
        results.append({"type": storage_str, "value": value})
        return
