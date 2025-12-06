# Crea una función fibonacci(n) que retorne la serie hasta n elementos.

def fibonacci(n):

    a = 0
    b = 1

    for i in range(0, n):
        resultado = a + b
        a = b
        b = resultado

    return a

print(fibonacci(7))