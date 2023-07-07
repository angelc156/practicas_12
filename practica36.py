a = 1

while a <= 5:
    precio = float(input("escribir el precio: "))
    if precio <= 0:
        print("el precio debe ser myor a cero")
    precio_con_impuesto = precio * 0.93
    if precio_con_impuesto > 100:
        print("precio", precio)
    elif precio_con_impuesto < 50:
        print(precio)
    else:
        print(precio)
    a +=1
print("precio_con_impuesto",precio_con_impuesto)
    