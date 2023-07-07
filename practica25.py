
print("Programa 25 \n Calculadora de descuentos\n")
P= float(input("Escriba el precio del producto: "))
D= float(input("Escriba el valor del descuento: "))

Des= D/100
PP = P * Des
PF = P- PP

print("El precio final del producto es:", round(PF,2))

if  PF < 50:
    print("¡Oferta especial!")

print("\n Fin del programa  ")


