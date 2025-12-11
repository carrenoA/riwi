#validar si un numero esta dentro del 1 y el 100

num = float(input("Enter a number: "))

if num in range(1,101):
    print(f"{num} is in range")
else:
    print(f"{num} is not in range")