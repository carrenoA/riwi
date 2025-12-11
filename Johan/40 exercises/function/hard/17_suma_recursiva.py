# Crea suma_recursiva(n) que calcule la suma 1 + 2 + ... + n con recursión.

def suma_recursive(n):
    # we set limit in 1, when the function will be 1 it'll return 1
    if n == 1:
        return 1
    else:
        # we'll be decreasing from n until the limit (1) and then we plus each number
        return n + suma_recursive(n-1)

print(suma_recursive(5))