# Dada una lista con elementos repetidos, genera una nueva lista sin duplicados.

newList = []
list = [1, 1, 1, 1, 2, 3, 5, 5, 5, 5, 7, 7, 8]

for i in list:
    if i not in newList:
        newList.append(i)
    else: pass

print(newList)