# Fusionar dos diccionarios, sumando valores si la clave existe en ambos.

dictionary1 = {"Nombre":"Juan", "Edad":20}
dictionary2 = {"Nombre":"Michelle", "Ciudad":"Medellin"}

wholeDictionary = {}

# we colect key and value for both dictionaries in d
for d in (dictionary1, dictionary2):
    # we traverse key, value for d.items (previous key, value)
    for key, value in d.items():
        # if key it's not in the empty dictionary we add it with the value
        if key not in wholeDictionary:
            wholeDictionary[key] = [value]
        else:
            # if the key's in the dictionary we add just the value in the key that is repeated
            wholeDictionary[key].append(value)


print(wholeDictionary)
