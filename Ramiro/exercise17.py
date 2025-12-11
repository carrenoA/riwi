#pide un numero e imprime su tabla de multiplicar hasta el 10

num = int(input("Enter a number: "))
n = 1
for i in range(1,11):
    times = num * n
    n = n + 1
    print(times)