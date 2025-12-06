# Crea una función contar_vocales(texto) que retorne cuántas vocales tiene.

def contar_vocales(texto):

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    array = list(texto)
    n = 0

# traverse the array
    for i in array:
    # validate if array contain a vowel
        if i in vowels:
        # increase n based on the words' vowels
            n += 1
        else:
            pass
    return n


print(contar_vocales("aaaa"))
