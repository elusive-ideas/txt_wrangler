import txt_wrangler as tw
find_str = "name"

def main(filename, lines, line_num, current, results):
    if current.startswith(find_str):
        value_str = current.rpartition('=')[2].strip().strip("'")
        results.append({find_str: value_str})
        return
