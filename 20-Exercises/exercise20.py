#pide numeros y sumalos hasta que ingrese 0
a = True
total = 0
list = []

while a == True:
    data = float(input("Enter a number: "))
    list.append(data)
    total = sum(list)
    if data == 0:
        a = False
    else:
        a = True

print(f"The total sum is: {total}")