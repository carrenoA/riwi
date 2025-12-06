# Dado un diccionario, crear otro donde claves y valores estén invertidos.

dictionary = {'Name' : 'Juan', 'Age' : 20}
newDictionary = {}

#dictionary.items() give us (key, value)
for key, value in dictionary.items():
        #we change value for key
        newDictionary[value] = key

print (newDictionary)