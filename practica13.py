print ("Programa 13. \n Que calcula salario neto de los trabajadores \n")

Salario = float(input("Ingresa su salario mensual: "))

SeguroSocial = Salario * 0.0514
SeguroEducativo = Salario * 0.02
Prestamo = 50

Pago = Salario - SeguroSocial - SeguroEducativo - Prestamo

print("Su saldo a pagar de seguro social es de:", SeguroSocial)
print("Su saldo a pagar de seguro educativo es de:", SeguroEducativo)
print("Su saldo a pagar de prestamo es de:", Prestamo)

print("El salario a pagar es de:", round(Pago,2))