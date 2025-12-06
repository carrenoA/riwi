# Crea frecuencia(texto) que retorne un diccionario con cada carácter y su cantidad.

#output:
# ("a": 32)
# ("b": 21)

def frecuencia(texto):

    dictionary = {}

    # traverse letter by letter in the text and that's the value for i
    for i in texto:
        # if that letter is in the dictionary will increase 1 each time
        if i in dictionary:
            dictionary[i] += 1
        # if that letter is in the dictionary just once it will take the value of 1
        else:
            dictionary[i] = 1

    return dictionary

print(frecuencia("holllla"))