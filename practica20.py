def calcular_salario_neto():
    print("Programa 20.\nCalcular el salario neto de un empleado.\n")
    
    sb = float(input("Ingrese el salario bruto del empleado: "))
    
    ss = sb * 0.08
    se = sb * 0.02
    i = sb * 0.15
    p = 100
    
    sn = sb - ss - se - i - p
    
    print("El salario neto a pagar es:", sn)
calcular_salario_neto()