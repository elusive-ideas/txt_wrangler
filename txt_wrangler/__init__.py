import os.path
import module_mgr as mm
import txt_wrangler as tw

module_manager = mm.Manager()
modules_folders = None
file_folders = None


def load_modules():
    module_manager.register_paths([modules_folders])
    registered_paths = module_manager.registered_paths()
    module_manager.add_folders_to_pythonpath(registered_paths)
    modules_discovered = module_manager.discover_modules()
    modules_loaded = module_manager.load_modules(modules_discovered)
    return modules_loaded


def read_file(filename, results=list(), start_line=None, end_line=None):
    filepath = tw.file_folders+'\\'+filename
    assert os.path.isfile(filepath), ("The file specified does not exist: "
                                      "'%s'" % filepath)

    dict_from_file = None
    whole_file = True
    if start_line is not None and end_line is not None:
        whole_file = False

    modules = tw.load_modules()

    with open(filepath, 'r') as f:
        all_lines = f.readlines()

    line_num = 0
    test = None
    for current in all_lines:
        line_num += 1
        if test:
            if line_num < test:
                continue
        if whole_file is False:
            if line_num < start_line:
                continue
            if line_num > end_line:
                break

        current = current.strip()
        if not modules:
            return {"type": "txt_file", "file": filename, "value": []}

        for module in modules:
            try:
                test = module.main(filename,
                                   all_lines,
                                   line_num,
                                   current,
                                   results)

                if test:
                    break
            except Exception, e:
                print "An exception has ocurred:", e

    if whole_file:
        dict_from_file = {"type": "txt_file", "file": filename, "value": results}

    else:
        dict_from_file = results

    return dict_from_file
