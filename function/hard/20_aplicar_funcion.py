# Crea aplicar(lista, funcion) que aplique una función a todos los elementos de la lista:
# Ejemplo: aplicar([1,2,3], lambda x: x*2) → [2,4,6]

def aplicar(lista, funcion):
        # between [] bc we need an array
        # from right to left, "for i in lista", we traverse for each item in the array with i
        # "funcion(i)" then for each value we use function (this case lambda)
        return [funcion(i) for i in lista]

print(aplicar([10,20,30], lambda x:x/2))