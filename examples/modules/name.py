pattern = 'name'
storage_str = 'name'


def main(filename, lines, line_num, current, results):
    if current.startswith(pattern):
        value_str = current.rpartition('=')[2].strip().strip("'")
        results.append({"type": storage_str, "value": value_str})
        return
