def determinar_si_es__positivo_negativo():
    print('Programa 27 \n solicita al usuario si es positivo, negativo o cero\n')
    num = float(input('Ingrese un número: '))

    if num > 0:
        print('Es un número positivo')
    elif num == 0:
        print('Es igual a 0')
    else:
        print('Es un número negativo')

    print('Fin del programa')
determinar_si_es__positivo_negativo()