### Hierarchy of example.txt

# Este es un fichero de ejemplo que utiliza el codigo que tengo hasta ahora.
# Como puedes ver, lo unico que necesitas por ahora es utilizar la funcion
# 'tw.get_blocks_in_file' para conseguir todos los bloques de un archivo.
#
# Deberias ser capaz de utilizar este fichero para probar las dos funciones
# que vas a estar mirando. 'mover' y 'duplicar'.
#
# Como siempre, si tienes alguna duda, comentamelo

# Importamos txt_wrangler (mi modulo) y definimos en namespace tw para no tener
# que escribirlo cada vez. Eso significa que para utilizar funcionalidad de mi
# modulo escribes tw seguido de un punto y el nombre de la funcion
import txt_wrangler as tw
from cue.obj.hitem import HItem


# Constants
FILE_WORK = r".\data\example.txt"
START_BLOCK = 'block_start'
END_BLOCK = 'block_end'
FILTER = "_hchy: "

# lista que va a almacenar los resultados
results = list()

# Recuperamos la lista de modulos cargados con load_modules
modules = tw.load_modules()
# Lectura i interpretacio dels fitxers de dades
tw.read_file(results, FILE_WORK, START_BLOCK, END_BLOCK, modules)

root = HItem(name=FILE_WORK.rpartition('\\')[2])
for line in results:
	if FILTER in line:
		section = line.rpartition('\'')[0].rpartition('\'')[2]
		HItem(name=section, parent=root)

print "===  Hierarchy  ".ljust(80, "=")
print root
print '='*80
