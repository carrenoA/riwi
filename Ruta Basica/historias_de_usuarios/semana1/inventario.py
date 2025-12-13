# 'nombre' input validation
while True:
    nombre = input("Ingrese el nombre del producto: ")

    # isaplha() means 'nombre' has to be string
    if nombre.isalpha():
        break
    else:
        # invalid input
        print("\nEste valor no es valido, por favor intenta nuevamente\n")

# 'precio' input validation
while True:
    try:
        # we set 'precio' as float
        precio = float(input("Ingresa el valor del producto: "))
    # if the input is not float we print a message and ask again for price
    except ValueError:
        print("\nEste valor no es valido, por favor intenta nuevamente\n")
    else:
        break

# 'cantidad' input validation
while True:
    try:
        # we set 'cantidad' as integer
        cantidad = int(input("¿Que cantidad vas a llevar de este producto?: "))
    # if the input is not integer we print a message and ask again for quantity
    except ValueError:
        print("\nEste valor no es valido, por favor intenta nuevamente\n")
    else:
        break

# final price of the whole shop
costo_total = precio * cantidad

# ',' is the dividing for thousandth, and we change it to '.'
# '.' is the dividing for decimals, and we change it to','
# before it was with USA format, we change it for Latin America format
print(f"\nProducto: {nombre}\nCantidad: {cantidad}\nPrecio: {f'{precio:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')} $")
print("-----------------------------------------------------")
print(f"El valor total de la compra es: {f'{costo_total:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')} $")


# SUMMARY
# The program requests a product name, price, and quantity with proper input validation.
# It calculates the total cost based on price and quantity and displays a formatted summary
# of the purchase, including the final amount.
