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

# Consigue todos los bloques del archivo de texto 'example.txt'
blocks = tw.get_blocks_in_file(file_name='example.txt',
                               start_pattern='block_start',
                               end_pattern='block_end')

# De todos los bloques, coge el segundo (El indice tiene base 0)
second_block = blocks[1]

# imprime todos los bloques
print "===  All Blocks  ".ljust(80, "=")
for line in blocks:
   	print line
print '='*80
# imprime solo el segundo bloque
print "===  2nd Block  ".ljust(80, "=")
for line in second_block:
    print line
print '='*80