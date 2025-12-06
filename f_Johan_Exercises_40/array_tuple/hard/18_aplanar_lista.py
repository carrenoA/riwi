# Dada una lista con listas internas, convertirla en una sola lista sin anidación.

array = [1,2,3, [4,5,6]]
newArray = []

for i in array:
    if isinstance(i, list):
        for o in i:
            newArray.append(o)
    else:
        newArray.append(i)

print(newArray)