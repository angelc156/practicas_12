print("Programa 24 \n calcular cual es el numero mayor \n")

a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
c = int(input("Ingrese el tercer valor: "))

if a > b and a > c:
    print("El numero mayor es a: ", a)
if b > a and b > c:
    print("El número mayor es b:", b)
if c > a and c > b:
    print("El número mayor es c:", c)
