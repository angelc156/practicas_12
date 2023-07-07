print ("Programa 16. \n Que calcula la nota final \n")

N1 = float(input("Ingresa la primera evaluación: "))
N2 = float(input("Ingresa la segunda evaluación: "))
N3 = float(input("Ingresa la tercera evaluación: "))
N4 = float(input("Ingresa la cuarta evaluación: "))
N5 = float(input("Ingresa la quinta evaluación: "))

NF = (N1 + N2 + N3 + N4 +N5) /100

print("Su notal final es: ", round(NF,2))