import csv

def exportar_reporte(mes, anio):
    """
    Exporta reservas FINALIZADAS por mes y año a un CSV
    """
    nombre_archivo = f"reporte_reservas_{anio}_{mes}.csv"

    with open("reservas.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        datos = [
            r for r in reader
            if r["estado"] == "FINALIZADA" and r["mes"] == mes and r["anio"] == anio
        ]

    if not datos:
        print("⚠️ No existen reservas finalizadas para ese período")
        return

    with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=datos[0].keys())
        writer.writeheader()
        writer.writerows(datos)

    print(f"📄 Reporte generado: {nombre_archivo}")
