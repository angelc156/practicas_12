print ("Programa 22. \nCalcular de temperatura\n")
temperature =  float(input("Escriba la temperatura: "))

if temperature < 20:
    if temperature < 10:
        print("Nivel azul")
    else:
        print("Nivel verde")
else:
    if temperature < 30:
        print("Nivel naranja")
    else:
        print("Nivel rojo")
        
print("\n Fin del programa  ")