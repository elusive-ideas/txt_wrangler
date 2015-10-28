### Read File of example.txt

# Library
import txt_wrangler as tw
# Constants
FILE_WORK = r".\data\example.txt"
START_BLOCK = 'block_start'
END_BLOCK = 'block_end'

# lista que va a almacenar los resultados
results = list()

# Recuperamos la lista de modulos cargados con load_modules
modules = tw.load_modules()
# Lectura i interpretacio dels fitxers de dades
tw.read_file(results, FILE_WORK, START_BLOCK, END_BLOCK, modules)

print "===  Results  ".ljust(80, "=")
for line in results:
	print line
print '='*80
