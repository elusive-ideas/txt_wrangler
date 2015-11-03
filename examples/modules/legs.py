pattern = 'legs'
storage_str = 'legs'


def main(filename, lines, line_num, current, results):
    if current.startswith(pattern):
        value = int(current.rpartition('=')[2].strip())
        results.append({"type": storage_str, "value": value})
        return
