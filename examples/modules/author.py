import txt_wrangler as tw
find_str = "author"

def main(filename, lines, line_num, current, results):
    if current.startswith(find_str):
        value_str = current.rpartition('=')[2].strip().strip("'")
        results.append({"type": find_str, "value": value_str})
        return
