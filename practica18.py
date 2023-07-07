print("Programa que calcule el interés compuesto: \n")

Ci = float(input("Ingrese el capital inicial: "))
i = float(input("Ingrese la tasa de interés (%): "))
n = float(input("Ingrese el período del ahorro: "))

ti = i / 100

Cf = Ci * (1 + ti) ** n

print("El capital final es: ", Cf)