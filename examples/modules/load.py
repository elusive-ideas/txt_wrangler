######

# Requeriments: current, modules... results.
def main(lines, line_num, current, start_block, end_block, results, modules):
    import txt_wrangler as tw

    if 'load_file' in current:
        # Buscamos comillas desde la derecha y nos
        # quedamos con lo que hay a la izquierda. Acto
        # seguido buscamos comillas de nuevo en el
        # resultado y nos quedamos con lo de la derecha
        # Es decir: el nombre del fichero
        new_filename = current.rpartition('"')[0].rpartition('"')[2]

        # Para cada fichero encontrado, llamamos a esta
        # misma funcion.
        tw.read_file(results, new_filename, start_block, end_block, modules)
