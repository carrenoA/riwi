# welcome
print("----Inventario----\n")

# storage
inventario = []

# functions
def agregar_producto():
    
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    cantidad = int(input("Ingresa la cantidad de productos: "))

    reg = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(reg)
    print("\n-------------------")
    print("Registro agregado con éxito")
    print("-------------------\n")
    
    op = input("¿Desea agregar otro registro?: y/n-----------")

    if op == "y":
        # if the option is "yes" we are going to ask again the information
        agregar_producto()
    elif op == "n":
        pass

def mostrar_inventario():
    for i in inventario:
        print(f"Producto: {i["nombre"]} --- Precio: {i["precio"]} --- Cantidad: {i["cantidad"]}\n")
        print("---------------------------")
    print("\n") 

def calcular_estadisticas():

    cantidad_productos = len(inventario)
    total_inventario = 0

    for j in inventario:
        total_inventario += j["precio"] * j["cantidad"]

    print(f"\nTotal de productos registrados: {cantidad_productos}")
    print(f"El valor total del inventario es: {total_inventario}\n")

# menu
menu_option = [1, 2, 3, 4]
while True:
    print("1. Agregar producto\n2. Mostrar inventario\n3. Calcular estadísticas\n4. Salir")
    print("--------------")
    option = int(input("Elige una opción: "))
    print("--------------")
    
    # if the option we put is not in the menu_option[] will show a message and then ask about the option again
    if option not in menu_option:
        print("\nIngresa un opción válida\n")
    else:
        if option == 1:
            agregar_producto()
        elif option == 2:
            mostrar_inventario()
        elif option == 3:
            calcular_estadisticas()
        elif option == 4:
            break

# Target:
# How to add a dictionary to an array
# Using a menu with while loop and validate their options