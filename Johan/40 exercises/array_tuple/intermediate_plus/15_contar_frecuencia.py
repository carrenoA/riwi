# Dado un texto, contar cuántas veces aparece cada letra usando un diccionario.

dictionary = {}

text = input("Type a text: ")

for i in text:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(dictionary)