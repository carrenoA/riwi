# Crea contar_palabras(frase) que retorne cuántas palabras tiene una frase.

def contar_palabras(frase):
    # split frase by spaces, inside of () we set which character we'll use to split the string, default is space
    palabra = frase.split()
    return len(palabra)

print(contar_palabras("Hola chao, jajaja"))