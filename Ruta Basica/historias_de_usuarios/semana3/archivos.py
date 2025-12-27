import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("El inventario está vacío, no se puede guardar")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([
                    p["nombre"],
                    p["precio"],
                    p["cantidad"]
                ])

        print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        print("No tienes permisos para escribir el archivo")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")



def cargar_csv(ruta):
    inventario_cargado = []
    filas_invalidas = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            header = next(reader, None)
            if header != ["nombre", "precio", "cantidad"]:
                print("El archivo CSV no tiene el encabezado correcto")
                return None

            for fila in reader:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    inventario_cargado.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except ValueError:
                    filas_invalidas += 1

        print(f"Archivo cargado. Filas inválidas omitidas: {filas_invalidas}")
        return inventario_cargado

    except FileNotFoundError:
        print("El archivo no existe")
    except UnicodeDecodeError:
        print("Error de codificación del archivo")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return None