# Crea un diccionario que almacene un nombre, edad y ciudad, e imprime cada valor.
name = input("Enter a name: ")
age = int(input("Enter an age: "))
city = input("Enter a city: ")

dictionary = {}
dictionary["Nombre"] = name
dictionary["Edad"] = age
dictionary["Ciudad"] = city

print(dictionary["Nombre"], dictionary["Edad"], dictionary["Ciudad"])