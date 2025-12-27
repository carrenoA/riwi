def agregar_producto(inventario, nombre, precio, cantidad):
    
    dict = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    inventario.append(dict)
    print("\n----------------------------")
    print("Producto agregado con éxito")
    print("------------------------------\n")

def mostrar_inventario(inventario):
    # if the list is empty show the message
    if not inventario:
        print("El inventario está vacío")
        return
    
    print("-------------------------------------------------------------------------------")
    n = 1
    
    for i in inventario:
        print(f"N° {n} | Nombre del producto: {i["nombre"]} | Precio del producto: {i["precio"]} | Cantidad del producto: {i["cantidad"]}")
        print("-------------------------------------------------------------------------------")
        n += 1

def buscar_producto(inventario, nombre):
    # if the list is empty show the message
    if not inventario:
        print("El inventario está vacío")
        return
    
    for j in inventario:
        if j["nombre"] == nombre:
            print(inventario)
        else:
            print("Lo siento, ese registro no existe (ten cuidado con las mayúsculas)")

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    # if the list is empty show the message
    if not inventario:
        print("El inventario está vacío")
        return
    
    for p in inventario:
        if p["nombre"] == nombre:
            
            if nuevo_precio is not None:
                p["precio"] = nuevo_precio
            
            if nueva_cantidad is not None:
                p["cantidad"] = nueva_cantidad
                    
            print("\n----------------------------")
            print("Producto actualizado con éxito")
            print("----------------------------\n")
            return

        print("\n----------------------------")
        print("Producto no encontrado")
        print("----------------------------\n")
            
def eliminar_producto(inventario, nombre):
    for l in inventario:
        if l["nombre"] == nombre:
            inventario.remove(l)
        else:
            print("\n----------------------------")
            print("Producto no encontrado")
            print("----------------------------\n")

def calcular_estadisticas(inventario):
    # if the list is empty show the message
    if not inventario:
        print("El inventario está vacío")
        return
    
    unidades_totales = 0
    
    valor_total = 0
    
    producto_mas_caro = inventario[0]["precio"]
    producto_mas_caro_nombre = ""
    
    producto_mayor_stock = inventario[0]["cantidad"]
    producto_mayor_stock_nombre = ""
    
    for e in inventario:
        unidades_totales += e["cantidad"]
        
        valor_total += e["precio"] * e["cantidad"]
        
        if e["precio"] > producto_mas_caro:
            producto_mas_caro = e["precio"]
            producto_mas_caro_nombre = e["nombre"]
            
        if e["cantidad"] > producto_mayor_stock:
            producto_mayor_stock = e["cantidad"]
            producto_mayor_stock_nombre = e["nombre"]

    print("\n-------------------------------------------------------------")    
    print(f"Total unidades inventario: {unidades_totales}")
    print("-------------------------------------------------------------")
    print(f"Total valor del inventario: {valor_total}$")
    print("-------------------------------------------------------------")
    print(f"Producto más caro es: {producto_mas_caro_nombre} con {producto_mas_caro}$")
    print("-------------------------------------------------------------")
    print(f"Producto con más stock es: {producto_mayor_stock_nombre} con {producto_mayor_stock}")
    print("-------------------------------------------------------------\n")