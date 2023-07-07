
print ("Programa 21. \n Calcular si una persona paga impuestos\n")
salario = float(input("Escriba el Salario: "))

if salario < 300:
    impuesto = salario * 1.07
    print("Esta Persona debe abonar impuestos", impuesto)
else:
    print("No Debe abonar impuestos")
    print("\n Fin del programa  ")