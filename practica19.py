def calcular_valor_total_articulos():
    print("Programa 19 \n Calcular el valor total de los artículos.\n")

    articulo1 = float(input("Ingrese el valor del artículo 1: "))
    articulo2 = float(input("Ingrese el valor del artículo 2: "))
    articulo3 = float(input("Ingrese el valor del artículo 3: "))
    articulo4 = float(input("Ingrese el valor del artículo 4: "))
    articulo5 = float(input("Ingrese el valor del artículo 5: "))

    totaldelacompra = articulo1 + articulo2 + articulo3 + articulo4 + articulo5
    compraConImpuesto = totaldelacompra * 1.07
    promedioSinImpuesto = totaldelacompra / 5

    promedioSinImpuesto = round(promedioSinImpuesto, 2)

    print("El total de la compra es:", totaldelacompra)
    print("El promedio sin impuesto es:", promedioSinImpuesto)
    print("La compra con impuesto es:", compraConImpuesto)

calcular_valor_total_articulos()
