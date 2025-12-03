#Pedir un numero y decir si es par o no

num = int(input("Enter a number: "))
formula = num % 2

if formula == 0:
    print(f"{num} is even")
else:
    print("That number is odd")