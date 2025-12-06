# Crea una función max_lista(lista) sin usar max().

def max_lista(lista):

    lista.sort(reverse=True)
    return lista[0]


print(max_lista([1, 2, 3, 4]))
