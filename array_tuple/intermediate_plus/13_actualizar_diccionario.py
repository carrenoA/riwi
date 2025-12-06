# Modifica un diccionario agregando una nueva clave con su valor.

d = {'Nombre': 'Juan', 'Edad' : 20 , 'Ciudad' : 'Medellin'}

d['Apellido'] = d.pop('Nombre')

print(d)