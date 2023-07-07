print ("Programa 12. \n calcula el interes de un prestamo \n")

Prestamo = int(input("Ingrese la cantidad del prestamo: "))
Tmensual = float(input("Ingrese la tasa mensual: "))
Plazo = int(input("Ingresa la cantidad de meses para pagar el prestamo: "))

PorcentajeTasa = Tmensual * 100
Tasames = int(PorcentajeTasa)
Tasamensual = Tasames / 12

cuota= Prestamo * (Tasamensual / (1 -(1 +Tasamensual )* (-Plazo)))
Interesmensual = Prestamo * Tasamensual
IM= float(Interesmensual)
Capitalmensual = IM - Prestamo

print("La cuota a pagar por mes es de:", cuota)
print("El interes mensual es de:", Interesmensual)
print("El capital mensual es de:", Capitalmensual)
