import csv
from datetime import date

def registrar_espacio():
    """
    Registra un nuevo espacio académico en espacios.csv
    """
    espacio_id = input("ID del espacio: ")
    nombre = input("Nombre del espacio: ")
    tipo = input("Tipo (AULA / LABORATORIO / SALA_ESPECIAL): ")
    capacidad = int(input("Capacidad: "))

    with open("espacios.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            espacio_id,
            nombre,
            tipo,
            capacidad,
            "DISPONIBLE",
            date.today()
        ])

    print("✅ Espacio registrado correctamente\n")

def listar_espacios():
    """
    Lista todos los espacios registrados
    """
    with open("espacios.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for espacio in reader:
            print(espacio)
