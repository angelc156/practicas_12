print ("Programa 15. \n Que calcula el costo de compra de los articulos \n")

P1 = float(input("Ingrese el costo del primer articulo: "))
P2 = float(input("Ingrese el costo del segundo articulo: "))
P3 = float(input("Ingrese el costo del tercer articulo: "))

Costo = ((P1 + P2 +P3)*1.07)

print("El costo total de la compra es de: ", round(Costo,3))