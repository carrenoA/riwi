# Dada una lista de nombres, contar cuántas veces aparece un nombre específico.

names=["Juan", "Juan", "Alberto", "Carlos", "Juan"]

n=0

for i in names:
    if i == "Juan":
        n+=1

print(n)