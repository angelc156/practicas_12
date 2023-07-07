precio = 1
subtotal = 0

while precio <= 5:
    articulo = float(input("Ingrese el precio del artículo " + str(precio) + ": "))
    subtotal += articulo
    precio += 1

impuesto = subtotal * 0.07
total = subtotal + impuesto

print("Subtotal: ", subtotal)
print("Impuesto (1.07): ", impuesto)
print("Total: ", total)
