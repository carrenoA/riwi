# Dada una lista de números, crear una nueva lista con solo los números pares.

allNumbers = [1,2,3,4,5,6,7,8,9,10]

evenArray = []

for i in allNumbers:
    if i % 2 == 0:
        evenArray.append(i)
    else:
        pass

print(evenArray)