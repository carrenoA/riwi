# Crea una función aplanar(lista) que convierta listas anidadas en una sola lista:
# Ejemplo: [1, [2, 3], [4, [5]]] → [1,2,3,4,5]

def aplanar(lista):

    newList = []

    # we traverse first for item by item in the whole array
    for i in lista:
        # isinstance() help us to identify if that "i" is in another array
        if isinstance(i, list):
            # we traverse the new array
            for o in i:
                newList.append(o)
        else:
            # we add the item in the original list
            newList.append(i)

    return newList

print(aplanar([1, 2, 2, [2, 3, 5],[1]]))