def sacar_calificaciones():
    print('Programa 28 \n calificación\n')
    cal = float(input('Puntos obtenidos: '))

    if cal >= 90 and cal <= 100:
        print('Es una A')
    elif cal >= 80 and cal <= 89:
        print('Es una B')
    elif cal >= 70 and cal <= 79:
        print('Es una C')
    elif cal >= 60 and cal <= 69:
        print('Es una D')
    else:
        print('Es una F')

    print('Fin del programa')
sacar_calificaciones()