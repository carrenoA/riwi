from servicios import agregar_producto
from servicios import mostrar_inventario
from servicios import buscar_producto
from servicios import actualizar_producto
from servicios import eliminar_producto
from servicios import calcular_estadisticas
from archivos import guardar_csv
from archivos import cargar_csv


# menu
print("----------Bienvenido----------")

options = range(1, 10)
    
inventario = []
    
while True:
    try:
        op = int(input(
            "1. Agregar producto\n"
            "2. Mostrar inventario\n"
            "3. Buscar producto\n"
            "4. Actualizar producto\n"
            "5. Eliminar producto\n"
            "6. Calcular estadísticas\n"
            "7. Guardar inventario en CSV\n"
            "8. Cargar inventario en CSV\n"
            "9. Salir\n"
            "> "
        ))

        if op not in options:
            print("\n------------------------------------------------")
            print("Por favor ingresa una opción válida del menú (1-9)")
            print("--------------------------------------------------\n")
            continue
        
    except ValueError:
        print("\n--------------------------------------------")
        print("Por favor ingresa una opción válida del menú")
        print("--------------------------------------------\n")
        continue
    else:
        if op == 1:
            nombre = input("Ingrese el nombre del producto a agregar: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            agregar_producto(inventario, nombre, precio, cantidad)

        elif op == 2:
            mostrar_inventario(inventario)
            
        elif op == 3:
            nombre = input("Ingresa el nombre del registro que deseas buscar: ")
            buscar_producto(inventario, nombre)
            
        elif op == 4:
            nombre = input("Ingresa el nombre del producto que deseas actualizar: ")
            
            preciot = input("Nuevo precio (Enter para no cambiar): ")
            # strip() delete spaces between words
            if preciot.strip() == "":
                nuevo_precio = None
            else:
                nuevo_precio = float(preciot)

            cantidadt = input("Nueva cantidad (Enter para no cambiar): ")
            if cantidadt.strip() == "":
                nueva_cantidad = None
            else:
                nueva_cantidad = int(cantidadt)
                
            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
            
        elif op == 5:
            nombre = input("Ingresa el nombre del producto a eliminar: ")
            eliminar_producto(inventario, nombre)
            
        elif op == 6:
            calcular_estadisticas(inventario)
            
        elif op == 7:
            guardar_csv(inventario, "inventario.csv")
            
        elif op == 8:
            inventario_cargado = cargar_csv("inventario.csv")

            # Si no se cargó nada (archivo vacío o error)
            if not inventario_cargado:
                continue

            opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()

            if opcion == "S":
                inventario = inventario_cargado
                print("\nInventario sobrescrito correctamente.\n")

            elif opcion == "N":
                for p in inventario_cargado:
                    inventario.append(p)
                print("\nInventario fusionado correctamente.\n")

            else:
                print("\nOpción inválida. No se realizaron cambios.\n")

        elif op == 9:
            break