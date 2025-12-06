# Dado un diccionario que contiene listas como valores, contar cuántos elementos totales hay entre
# todas las listas internas.

dictionary = {
    "Nombre": ["Juan", "Carlos", "Michelle"],
    "Edad": [20, 30]
}
total = 0
# we traverse key, value for each item in the dictionary
for k, v in dictionary.items():
    total += len(v)

print(total)
