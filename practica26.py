
print("Programa 26 \n Clasificacion de triangulos\n")
A = int(input("Escriba el valor del lado A del triangulo: "))
B = int(input("Escriba el valor del lado B del triangulo: "))
C = int(input("Escriba el valor del lado C del triangulo: "))

if A == B and B == C: 
    print("Es un triangulo equilatero")

elif A == B or B == C or A == C  :
    print("Es un triangulo isósceles")

else:
    print("El triangulo es escaleno")

print("\n Fin del programa  ")
