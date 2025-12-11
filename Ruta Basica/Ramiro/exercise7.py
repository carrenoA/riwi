#Validar si es mayor de edad

age = int(input("Enter your age: "))
adult = int(input("How old in your country you gotta be to be considered as adult?: "))

if age >= adult:
    print("You're an adult")
else:
    print("You're still young")