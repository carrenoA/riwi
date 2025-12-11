# Crea una función invertir(texto) que retorne el texto al revés sin usar slicing.

def invertir(texto):

    array = list(texto)
    array.reverse()
    # "".join array of strings to str
    return "".join(array)

print(invertir("hola"))