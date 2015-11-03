import txt_wrangler as tw


def main(filename, lines, line_num, current, results):
    if current.startswith('//'):
        comment_str = current[2:].strip()
        results.append({"type": "comment", "value": comment_str})
        return
