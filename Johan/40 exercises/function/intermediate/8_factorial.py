# Crea una función factorial(n) que calcule el factorial de un número.

def factorial(n):

    resultado = 1
    # we set the range between 1 and the number plus 1
    for i in range(1, n + 1):
        # Multiply the result by each number from 1 to n.
        resultado *= i
    return resultado

# 10*9*8*7*6*5*4*3*2*1=3.628.800
print(factorial(10))