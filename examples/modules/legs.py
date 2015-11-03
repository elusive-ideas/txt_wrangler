import txt_wrangler as tw
find_str = "legs"

def main(filename, lines, line_num, current, results):
    if current.startswith(find_str):
        value = int(current.rpartition('=')[2].strip())
        results.append({"type": find_str, "value": value})
        return
