#Pide dos números y muestra cuál es mayor o si son iguales.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 < num2:
    print(f"{num1} is lower than {num2}")
elif num2 < num1:
    print(f"{num1} is higher than {num2}")
else:
    print("Both numbers are the same")