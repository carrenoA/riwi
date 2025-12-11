# Crea eliminar_duplicados(lista) que retorne una lista sin repetir elementos (sin usar set()).

def eliminar_duplicados(lista):

    newList=[]

    for i in lista:
        # "not in" = it's not, if it's not in the array it'll be added, if it is it will continue with the
        # next one
        if i not in newList:
            newList.append(i)

    return newList

print(eliminar_duplicados([1,1,1,3,3,3,2,2]))