from auth import login
from espacios import registrar_espacio, listar_espacios
from reservas import registrar_reserva
from reportes import exportar_reporte

def menu():
    """
    Muestra el menú principal del sistema
    """
    print("""
1. Registrar espacio
2. Listar espacios
3. Registrar reserva
4. Exportar reporte CSV
5. Salir
""")

if not login():
    exit()

while True:
    menu()
    try:
        opcion = int(input("> "))
    except ValueError:
        print("❌ Opción inválida")
        continue

    if opcion == 1:
        registrar_espacio()
    elif opcion == 2:
        listar_espacios()
    elif opcion == 3:
        registrar_reserva()
    elif opcion == 4:
        mes = input("Mes (MM): ")
        anio = input("Año (YYYY): ")
        exportar_reporte(mes, anio)
    elif opcion == 5:
        print("👋 Saliendo del sistema")
        break
