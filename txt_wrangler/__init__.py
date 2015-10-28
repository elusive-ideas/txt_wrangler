# Library
import os.path
import module_mgr as mm

# Constants
DIR_MODULES = r'.\modules'


def load_modules():
    # Registramos una lista con carpetas en las que se van a buscar modulos.
    mm.register_paths([DIR_MODULES])

    # Guardamos las carpetas registradas en una lista.
    registered_paths = mm.registered_paths()

    # Anhadimos las carpetas registradas a PYTHONPATH de manera que podamos
    # importar modulos de ellas desde nuestro codigo.
    mm.add_folders_to_pythonpath(registered_paths)

    # Descubrimos modulos en las carpetas registradas (basicamente una lista
    # de ficheros que podremos importar).
    modules_discovered = mm.discover_modules()

    # Importamos los modulos y guardamos una referencia en una lista llamada
    # modules_loaded.
    modules_loaded = mm.load_modules(modules_discovered)

    # Devolvemos la lista de modulos que hemos importado (de manera que pueden
    # ser utilizados desde otro procedimiento)
    return modules_loaded


def read_file(results, filename, start_block, end_block, modules):

    # Check file existence
    assert os.path.isfile(filename), ("The file specified does not exist: "
                                      "'%s'" % filename)

    # Abrimos el fichero
    with open(filename, 'r') as f:
        # Leemos lineas del fichero
        all_lines = f.readlines()

    line_num = 0
    for current in all_lines:
        current = current.strip()
        line_num += 1
        # Si se han encontrado modulos a cargar dinamicamente
        if modules:
            # Por cada uno de esos modulos..
            for module in modules:
                # Llamamos a main.
                # En el caso de que no se pueda ejecutar (por ejemplo al no
                # estar implementada la funcion Main), cazamos la excepcion
                # para que eso nodetenga el programa. Es decir, seguira
                # ejecutando otros modulos encontrados tras mostrar el error
                try:
                    module.main(all_lines, line_num, current, start_block, end_block, results, modules)
                except Exception, e:    
                    print "An exception has ocurred:", e
