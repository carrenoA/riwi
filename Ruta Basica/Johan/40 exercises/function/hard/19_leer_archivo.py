# Crea leer_archivo(nombre) que retorne la cantidad de líneas que tiene un archivo .txt.

def leer_archivo(nombre):

    # open(nombre, 'r', encoding='utf-8') opening .txt file
    # nombre = file name, r = opening mode (reading), encoding='utf-8'= interpret most of the characters

    #sum(1 for _ in ...) add 1 by each line
    #sum=add, 1=increase value, _=iterate line by line, in=to specify which file

    total_lines = sum(2 for _ in open(nombre, 'r', encoding='utf-8'))
    return total_lines

print(leer_archivo("/home/caki/hola.txt"))