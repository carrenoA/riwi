# Crea una función es_primo(n) que retorne True o False.

def es_primo(n):
    # all() internal python function, every condition inside of all() return a boolean

    # "for" is to give a value for "i", then if "i" number divided by n is != 0 is odd, so that's "True" bc
    # prime numbers are odd except number 2
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


print(es_primo(1))
