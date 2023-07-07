numeros = []
r = 1

while r <= 3:
    numeros = float(input("ingrese el numero"))
    r += 1

    if numeros[0] > numeros[1] and numeros[0] > numeros[2]:
        print("el numero mayor es:", numeros[0])
    elif numeros[1] > numeros[0] and numeros[1] > numeros[2]:
        print("el numero mayor es:", numeros[1] )
    else:
        print("el numero mayor es:", numeros[2])