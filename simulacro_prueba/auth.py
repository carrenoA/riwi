import csv

def login():
    """
    Valida el inicio de sesión del administrador.

    - Lee el archivo usuarios.csv
    - Permite máximo 3 intentos
    - Finaliza el programa si falla

    Retorna:
        bool: True si el login es exitoso, False en caso contrario
    """
    intentos = 3

    while intentos > 0:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")

        with open("usuarios.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                if fila["usuario"] == usuario and fila["contrasena"] == contrasena:
                    print("✅ Acceso concedido\n")
                    return True

        intentos -= 1
        print(f"❌ Credenciales incorrectas. Intentos restantes: {intentos}")

    print("🚫 Acceso bloqueado")
    return False
