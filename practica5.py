print ("Programa 5. \n que calcula el perimetro de un rectangulo \n")

i1 = input("Escriba el valor de AB: ")
i2 = input("Escriba el valor de BC: ")
i3 = input("Escriba el valor de CD: ")
i4 = input("Escriba el valor de DA: ")

AB = float(i1)
BC = float(i2)
CD = float(i3)
DA = float(i4)

p = AB+ BC + CD + DA
PR= round (p, 2)
print("El area de un rectangulo es: ",p,PR)