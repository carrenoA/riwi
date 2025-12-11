# Crea validar_password(password) con reglas:
#     • +8 caracteres
#     • al menos 1 mayúscula
#     • al menos 1 número
# Retornar "Válida" o "Inválida".

def validar_password(password):

    for i in password:
        # isupper() for have at least a uppercase
        # isalnum() needs to be alphanumeric
        if i.isupper() and len(password) > 8 and i.isalnum():
            return ("Valida")
    return ("Invalida")

print(validar_password("123456789kK"))
