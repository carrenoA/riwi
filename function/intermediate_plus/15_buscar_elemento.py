# Crea buscar(lista, objetivo) que retorne el índice del objetivo o -1 si no existe.

def buscar(lista, objetivo):

    # way to traverse array index "range(len(array))"
    # for i in range(len(lista)):
    #     if lista[i] == objetivo:
    #         return i

    # "enumerate" traverse array with two values at the same time
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i

    return -1

print(buscar([1, 2, 3, 4, 5], 2))