# Ordena una lista de números de forma ascendente sin usar sort() (usar lógica propia).

# PEDIR EXPLICACION, COPY PASTE

lista = [5, 2, 9, 1, 7]

for i in range(len(lista)):
    lowest = i
    for j in range(i+1, len(lista)):
        if lista[j] < lista[lowest]:
            lowest = j
    lista[i], lista[lowest] = lista[lowest], lista[i]

print(lista)
