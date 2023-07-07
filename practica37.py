def calcular_total_impuesto():
    print("programa 37 \ncalcular_total_impuesto\n")
    contador = 0
    total = 0

    while contador < 5:
        precio = float(input("Ingrese el precio del artículo: "))
        impuesto = precio * 0.07
        total += impuesto
        contador += 1

    return total


    print("El total de impuesto a pagar es:", total_impuesto)
calcular_total_impuesto()
