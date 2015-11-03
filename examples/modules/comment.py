import txt_wrangler as tw

patterns = ('//', ';;')
storage_str = 'comment'


def main(filename, lines, line_num, current, results):
    if current.startswith(patterns):
        comment_str = current[2:].strip()
        results.append({"type": storage_str, "value": comment_str})
        return
