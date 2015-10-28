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


# Constants
FILE_WORK = r".\data\example.txt"
START_BLOCK = 'block_start'
END_BLOCK = 'block_end'
FILTER = "_bk: "

# lista que va a almacenar los resultados
results = list()
out = list()

# Recuperamos la lista de modulos cargados con load_modules
modules = tw.load_modules()
# Lectura i interpretacio dels fitxers de dades
tw.read_file(results, FILE_WORK, START_BLOCK, END_BLOCK, modules)

for line in results:
	if FILTER in line:
		print line
		out.append(line[1:])

print "===  All Blocks  ".ljust(80, "=")
for line in out:
	print line
print '='*80
