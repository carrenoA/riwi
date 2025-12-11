#pide al usuario que escriba una contraseña. Si coincide con “python123”, muestra “Acceso concedido”, de lo contrario, “Acceso denegado”.

pasw = input("Enter a password: ")

if pasw == "python123":
    print("Acceso concedido")
else:
    print("Acceso denegado")