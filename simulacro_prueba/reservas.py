import csv
import json
from datetime import date

def cargar_configuracion():
    """
    Carga los límites por tipo de usuario desde configuracion.json
    """
    with open("configuracion.json", encoding="utf-8") as f:
        return json.load(f)["limites_por_tipo"]

def registrar_reserva():
    """
    Registra una solicitud de reserva validando:
    - Estado del espacio
    - Límite de horas según tipo de usuario
    """
    limites = cargar_configuracion()

    espacio_id = input("ID del espacio: ")
    usuario = input("Nombre del solicitante: ")
    tipo_usuario = input("Tipo (ESTUDIANTE / DOCENTE / ADMINISTRATIVO): ")
    fecha_reserva = input("Fecha reserva (YYYY-MM-DD): ")
    horas = int(input("Horas solicitadas: "))

    if horas > limites[tipo_usuario]:
        print("❌ Excede el límite permitido")
        return

    with open("reservas.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "", espacio_id, "", usuario, tipo_usuario,
            date.today(), fecha_reserva,
            horas, "", "NO", "PENDIENTE",
            fecha_reserva.split("-")[1],
            fecha_reserva.split("-")[0]
        ])

    print("✅ Reserva registrada como PENDIENTE\n")
