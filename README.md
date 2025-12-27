texto.strip() eliminar espacios

🧪 TRY / EXCEPT (manejo de errores)
1️⃣ Error al convertir a número
try:
    edad = int(input("Edad: "))
except ValueError:
    print("Debes ingresar un número")

2️⃣ Validar número dentro de un rango
try:
    op = int(input("Opción: "))
    if op < 1 or op > 9:
        print("Opción fuera de rango")
except ValueError:
    print("Entrada inválida")

3️⃣ Archivo que no existe
try:
    with open("datos.csv", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe")

4️⃣ Capturar cualquier error (último recurso)
try:
    x = int("abc")
except Exception as e:
    print("Ocurrió un error:", e)

🧮 SUBTOTAL Y CÁLCULOS
Subtotal de UN producto
subtotal = producto["precio"] * producto["cantidad"]

Subtotal usando lambda
subtotal = lambda p: p["precio"] * p["cantidad"]
valor = subtotal(producto)

Valor total de TODO el inventario
valor_total = 0
for p in inventario:
    valor_total += p["precio"] * p["cantidad"]

📁 ARCHIVOS CSV
1️⃣ Crear / sobrescribir un archivo CSV
import csv

with open("productos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["nombre", "precio", "cantidad"])  # encabezado


📌 "w" → sobrescribe
📌 "a" → agrega sin borrar

2️⃣ Escribir una lista de diccionarios en CSV
inventario = [
    {"nombre": "Laptop", "precio": 1000, "cantidad": 2},
    {"nombre": "Mouse", "precio": 20, "cantidad": 5}
]

with open("productos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["nombre", "precio", "cantidad"]
    )
    writer.writeheader()
    writer.writerows(inventario)

3️⃣ Leer un CSV con encabezados
with open("productos.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        print(fila["nombre"], fila["precio"])

4️⃣ Agregar una fila sin borrar el archivo
with open("productos.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Teclado", 50, 3])

📄 ENCABEZADOS CSV (concepto clave)

El encabezado:

nombre,precio,cantidad


Permite:

Leer cada fila como diccionario

Acceder por nombre de campo

Validar formato del archivo

⚠️ Sin encabezado → DictReader no funciona bien.

📂 ARCHIVOS JSON
1️⃣ Crear / guardar un JSON
import json

config = {
    "limites_por_tipo": {
        "ESTUDIANTE": 2,
        "DOCENTE": 4
    }
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

2️⃣ Leer un JSON
with open("config.json", encoding="utf-8") as f:
    datos = json.load(f)

print(datos["limites_por_tipo"]["ESTUDIANTE"])

3️⃣ Reescribir un JSON (actualizar datos)
with open("config.json", encoding="utf-8") as f:
    datos = json.load(f)

datos["limites_por_tipo"]["ESTUDIANTE"] = 3

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4)


📌 JSON siempre se reescribe completo.

📤 EXPORTAR DATOS (CSV)
Exportar solo ciertos registros
finalizadas = []

with open("reservas.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        if r["estado"] == "FINALIZADA":
            finalizadas.append(r)

with open("reporte.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=finalizadas[0].keys())
    writer.writeheader()
    writer.writerows(finalizadas)

🔐 VALIDAR INVENTARIO VACÍO
if not inventario:
    print("No hay datos")
    return
