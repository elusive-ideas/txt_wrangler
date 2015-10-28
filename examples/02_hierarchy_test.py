### Hierarchy of example.txt

import txt_wrangler as tw

root, sections = tw.get_hierarchy_from_file(file_name='D:\Python\examples\data\example.txt',
                                            start_pattern='block_start',
                                            end_pattern='block_end')
print root
