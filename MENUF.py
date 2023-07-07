def intercambiar_variables():
    print("Programa 1\nprimer programa\n")
    A = 7
    B = 0
    C = 0
    B = A
    C = B
    A = A

    print(A, B, C)
    
def transformar_valores():
    print("programa 2\ntransformar_valores\n")
    A = 10
    B = 20
    AUX = 0

    AUX = A
    A = B
    B = AUX

    print(A, B, AUX)

    
def imprimir_tipos_de_dato():
    print("Programa 3\n tercer programa\n")
   
    A = float(input("leer A: "))
    B = float(input("leer B: "))
    C = float(input("leer C: "))
    
    D = (A + B + C) / 3
    
    print("El resultado es:", round(D, 2))
    return D

def calcular_area_triangulo():
    print("Programa 4.\nCalcula el área de un triángulo.\n")
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))

    def areaTriangulo(base, altura):
        area = (base * altura) / 2
        return area

    area = areaTriangulo(base, altura)

    print("El área del triángulo es:", area)
    
def calcular_perimetro_rectangulo():
    print("Programa 5.\nCalcula el perímetro de un rectángulo.\n")
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))

    def perimetroRectangulo(base, altura):
        perimetro = 2 * (base + altura)
        return perimetro

    perimetro = perimetroRectangulo(base, altura)

    print("El perímetro del rectángulo es:", perimetro)

def calcula_perimetro_de_rectangulo():
    print("Programa 6.\ncalcula_perimetro_de_rectangulo.\n")
    base1 = float(input("Escriba el valor de base 1: "))
    base2 = float(input("Escriba el valor de base 2: "))
    altura = float(input("Escriba el valor de la altura: "))

    area = ((base1 + base2) * altura) / 2
    area_redondeada = round(area, 2)

    print("El área de un trapecio es:", area_redondeada)

def calcular_volumen_prisma_rectangular():
    print("Programa 7.\nCalcula el volumen de un prisma rectangular.\n")
    largo = float(input("Escriba el valor del largo: "))
    ancho = float(input("Escriba el valor del ancho: "))
    altura = float(input("Escriba el valor de la altura: "))

    volumen = largo * ancho * altura
    volumen_redondeado = round(volumen, 4)

    print("El volumen de un prisma rectangular es:", volumen_redondeado)

def resolver_ecuaciones():
    print("Programa 8.\nPrograma que resuelve ecuaciones.\n")
    x1 = input("Escriba el valor de x: ")
    x = float(x1)

    A = 20 - (7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 + (9 * x) + 18
    D = (6 * x) - 5 - (8 * x) + 2
    E = ((5 * x) + 78) / 28
    F = (((6 * x) - 7) / 4) + (((3 * 7) - 5) / 7)

    variables = [A, B, C, D, E, F]

    for variable in variables:
        print("El resultado es", round(variable, 2))
    
def valores_para_x_y():
    print("Programa 9.\nPrograma que resuelve ecuaciones.\n")
    a1 = input("Escriba el valor de a: ")
    b2 = input("Escriba el valor de b: ")
    c3 = input("Escriba el valor de c: ")

    a = float(a1)
    b = float(b2)
    c = float(c3)

    c1 = (4 * a) + (3 * b)
    c2 = (21 * a) - 18 + (8 * b) - 5
    c3 = (4 * a) + (3 * b) + 7
    c4 = (2 * a) + (3 * b) - (c ** 5)
    c5 = (2 * a) + (3 * b) - (c ** 2)

    variables = [c1, c2, c3, c4, c5]

    for i, variable in enumerate(variables, start=1):
        print("El valor de c{} es: {}".format(i, round(variable, 2)))
    
def resolver_conversiones_unidades():
    print("Programa 10.\nQue resuelve conversiones de unidades.\n")
    m = input("Ingrese la cantidad de metros: ")
    m1 = float(m)

    pies = m1 * 3.28
    pulgadas = m1 * 39.37

    print("La conversión de metros a pies es de:", round(pies, 2))
    print("La conversión de metros a pulgadas es de:", round(pulgadas, 2))
    
def resolver_regla_de_tres():
    print("Programa 11.\nQue resuelve una regla de tres.\n")
    a = input("Ingrese el primer valor: ")
    b = input("Ingrese el segundo valor: ")
    c = input("Ingrese el tercer valor: ")

    a1 = float(a)
    b1 = float(b)
    c1 = float(c)

    D = (c1 * b1) / a1
    d = int(D)

    print("El valor de D es:", d)
    
def calcular_interes_prestamo():
    print("Programa 12.\nCalcula el interés de un préstamo.\n")
    prestamo = int(input("Ingrese la cantidad del préstamo: "))
    tasa_mensual = float(input("Ingrese la tasa mensual: "))
    plazo = int(input("Ingrese la cantidad de meses para pagar el préstamo: "))

    porcentaje_tasa = tasa_mensual * 100
    tasa_mes = int(porcentaje_tasa)
    tasa_mensual = tasa_mes / 12

    cuota = prestamo * (tasa_mensual / (1 - (1 + tasa_mensual) ** (-plazo)))
    interes_mensual = cuota * plazo - prestamo
    capital_mensual = cuota - interes_mensual

    print("La cuota a pagar por mes es de:", cuota)
    print("El interés mensual es de:", interes_mensual)
    print("El capital mensual es de:", capital_mensual)

def salario_de_neto_trabajador():
    print("Programa 13 \n calcular el salario neto de los trabajadores")

    salario = float(input("Ingrese su salario mensual: "))

    saldos_a_pagar = {
        "Seguro social": salario * 0.0514,
        "Seguro educativo": salario * 0.02,
        "Préstamo": 50
        }

    total_saldos_a_pagar = 0
    for saldo, valor in saldos_a_pagar.items():
            print(f"Su saldo a pagar de {saldo} es de: {valor}")
            total_saldos_a_pagar += valor

    salario_neto = salario - total_saldos_a_pagar
    print("El salario neto es de:", round(salario_neto, 2))

def calcular_costo_gasolina():
    print("Programa 14.\nQue calcula el costo de compra de gasolina.\n")
    
    litros = float(input("Valor de la cantidad de litros: "))
    costo_total = round(((0.98 * litros) * 1.07), 2)
    
    print("El costo total es:", costo_total)

def calcular_costo_compra():
    print("Programa 15.\nQue calcula el costo de compra de los artículos.\n")
    
    P1 = float(input("Ingrese el costo del primer artículo: "))
    P2 = float(input("Ingrese el costo del segundo artículo: "))
    P3 = float(input("Ingrese el costo del tercer artículo: "))
    
    costo_total = ((P1 + P2 + P3) * 1.07)
    
    print("El costo total de la compra es de:", round(costo_total, 3))

def calcular_nota_final():
    print("Programa 16.\nQue calcula la nota final.\n")
    
    N1 = float(input("Ingresa la primera evaluación: "))
    N2 = float(input("Ingresa la segunda evaluación: "))
    N3 = float(input("Ingresa la tercera evaluación: "))
    N4 = float(input("Ingresa la cuarta evaluación: "))
    N5 = float(input("Ingresa la quinta evaluación: "))
    
    NF = (N1 + N2 + N3 + N4 + N5) / 100
    
    print("Su nota final es:", round(NF, 2))
    
    
def convertir_unidades():
    print("Programa 17.\nConversión de cantidades de unidades.\n")
    
    kg = float(input("Ingrese el valor en kilogramos: "))
    g = kg * 1000
    print("El resultado es:", g, "gramos")
    
    g = float(input("Ingrese el valor en gramos: "))
    kg = g * 0.001
    print("El resultado es:", kg, "kilogramos")
    
    m = float(input("Ingrese el valor en metros: "))
    cm = m * 100
    print("El resultado es:", cm, "centímetros")
    
    cm = float(input("Ingrese el valor en centímetros: "))
    m = cm * 0.01
    print("El resultado es:", m, "metros")
    
def calcular_interes_compuesto():
    print("Programa 18 \n para calcular el interés compuesto.\n")
    
    monto_inicial = float(input("Ingrese el monto inicial: "))
    tasa_interes = float(input("Ingrese la tasa de interés anual (%): "))
    periodo = int(input("Ingrese el número de períodos: "))
    
    tasa_interes_decimal = tasa_interes / 100
    monto_final = monto_inicial * (1 + tasa_interes_decimal) ** periodo
    
    print("\nEl monto final es:", monto_final)
    
    
def calcular_valor_total():
    print("Programa 19 \n calcular el valor total de los artículos.\n")
    
    articulo1 = float(input("Ingrese el valor del artículo 1: "))
    articulo2 = float(input("Ingrese el valor del artículo 2: "))
    articulo3 = float(input("Ingrese el valor del artículo 3: "))
    articulo4 = float(input("Ingrese el valor del artículo 4: "))
    articulo5 = float(input("Ingrese el valor del artículo 5: "))
    
    totaldelacompra = articulo1 + articulo2 + articulo3 + articulo4 + articulo5
    compraConImpuesto = totaldelacompra * 1.07
    promedioSinImpuesto = totaldelacompra / 5
    
    promedioSinImpuesto = round(promedioSinImpuesto, 2)
    
    print("El total de la compra es:", totaldelacompra)
    print("El promedio sin impuesto es:", promedioSinImpuesto)
    print("La compra con impuesto es:", compraConImpuesto)

def calcular_salario_neto():
    print("Programa 20.\nCalcular el salario neto de un empleado.\n")
    
    sb = float(input("Ingrese el salario bruto del empleado: "))
    
    ss = sb * 0.08
    se = sb * 0.02
    i = sb * 0.15
    p = 100
    
    sn = sb - ss - se - i - p
    
    print("El salario neto a pagar es:", sn)

def calcular_impuestos():
    print("Programa 21.\nCalcular si una persona paga impuestos.\n")
    
    salario = float(input("Escriba el salario: "))
    
    if salario < 300:
        impuesto = salario * 1.07
        print("Esta persona debe abonar impuestos:", impuesto)
    else:
        print("No debe abonar impuestos")
    
    print("\nFin del programa")

def calcular_nivel_temperatura():
    print("Programa 22.\nCalcular nivel de temperatura.\n")
    
    temperature = float(input("Escriba la temperatura: "))
    
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
    
    print("\nFin del programa")
    
def calcular_mayor_edad():
    print("Programa 23.\nCalcular si es mayor de edad.\n")
    valor = float(input("Escriba su edad: "))

    if valor >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")

    print("\nFin del programa")
    
def calcular_el_numero_mayor():
    print("Programa 24.\nCalcular cuál es el número mayor.\n")

    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    c = int(input("Ingrese el tercer valor: "))

    if a > b and a > c:
        print("El número mayor es a:", a)
    elif b > a and b > c:
        print("El número mayor es b:", b)
    elif c > a and c > b:
        print("El número mayor es c:", c)
    else:
        print("Los números son iguales.")
        
def calculadora_descuento():
    print("programa 25. \n calculadora_descuento.\n")
    precio_original = float(input("Ingrese el precio original del producto: "))
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

    descuento = precio_original * (porcentaje_descuento / 100)
    precio_con_descuento = precio_original - descuento

    print("El precio con descuento es:", precio_con_descuento)

def clasificar_triangulo():
    print("Programa 26\nClasificación de triángulos\n")
    A = int(input("Escriba el valor del lado A del triángulo: "))
    B = int(input("Escriba el valor del lado B del triángulo: "))
    C = int(input("Escriba el valor del lado C del triángulo: "))

    if A == B and B == C: 
        print("Es un triángulo equilátero")
    elif A == B or B == C or A == C:
        print("Es un triángulo isósceles")
    else:
        print("Es un triángulo escaleno")

    print("\nFin del programa")

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
    
def romper_en_siete():
    print("Programa 29 \n  for que rompe en 7\n ")
    for i in range(10):
        if i == 7:
            break
        print(i)

    print("Fin del programa")
    
def imprimir_impares():
    print("Programa 30 \n impresión de números impares\n :")
    num = 1
    while num <= 50:
        print(num)
        num += 2

    print("Fin del programa")


def imprimir_impares_hasta_7():
    print("programa 31 \n imprimir_impares_hasta 7\n")
    value = 1
    while value <= 10:
        if value == 8:
            break
        print(value)
        value += 1
        
def imprimir_numeros():
    print("programa 32")
    for x in range(1, 11):
        if x == 12:
            break
        print(x)

def calcular_total_compra():
    print("programa 33")
    precio = 1
    subtotal = 0

    while precio <= 5:
        articulo = float(input("Ingrese el precio del artículo " + str(precio) + ": "))
        subtotal += articulo
        precio += 1

    impuesto = subtotal * 0.07
    total = subtotal + impuesto

    print("Subtotal: ", subtotal)
    print("Impuesto : ", impuesto)
    print("Total: ", total)

def imprimir_numeros_pares_impares():
    print("programa 34 \nimprimir_numeros_pares_impares\n")
    a = 0
    while a <= 16:
        if a % 2 == 0:
            print(a, "es par")
        else:
            print(a, "es impar")
        a += 1

def clasificar_numeros():
    print("programa 35\nclasificar_numeros\n")
    for e in range(1, 11):
        if e > 5:
            print(e, "es mayor a 5")
        elif e <= 0:
            print(e, "es menor a 5")
        else:
            print(e, "es menor o igual a 0")
        if e == 9:
            break

def calcular_precio_con_impuesto():
    print("programa 36\ncalcular_precio_con_impuesto")
    a = 1
    while a <= 5:
        precio = float(input("Escribir el precio: "))
        if precio <= 0:
            print("El precio debe ser mayor a cero")
        precio_con_impuesto = precio * 0.93
        if precio_con_impuesto > 100:
            print("Precio:", precio)
        elif precio_con_impuesto < 50:
            print(precio)
        else:
            print(precio)
        a += 1
    print("Precio con impuesto:", precio_con_impuesto)

def calcular_total_impuesto():
    print("programa 37 \ncalcular_total_impuesto\n")
    contador = 0
    total = 0

    while contador < 5:
        precio = float(input("Ingrese el precio del artículo: "))
        impuesto = precio * 0.07
        total += impuesto
        contador += 1

    return total


    print("El total de impuesto a pagar es:", total_impuesto)
    
def encontrar_numero_mayor():
    print("programa 38\n encontrar_numero_mayor\n")
    numeros = []
    r = 1

    while r <= 3:
        numero = float(input("Ingrese un número: "))
        numeros.append(numero)
        r += 1

    if numeros[0] > numeros[1] and numeros[0] > numeros[2]:
        print("El número mayor es:", numeros[0])
    elif numeros[1] > numeros[0] and numeros[1] > numeros[2]:
        print("El número mayor es:", numeros[1])
    else:
        print("El número mayor es:", numeros[2])
    #------------------------------------------------------------------------------------------------------------------------------------
import time

def mostrar_menu():
    menu = {
        "1": "intercambiar_variables",
        "2": "transformar_valores",
        "3": "imprimir_tipos_de_dato",
        "4": "calcular_area_triangulo",
        "5": "calcular_perimetro_rectangulo",
        "6": "calcula_perimetro_de_rectangulo",
        "7": "calcular_volumen_prisma_rectangular",
        "8": "resolver_ecuaciones",
        "9": "resolver_x_y",
        "10": "resolver_conversiones_unidades",
        "11": "resolver_regla_de_tres",
        "12": "calcular_interes_prestamo",
        "13": "calcular_salario_neto",
        "14": "calcular_costo_gasolina",
        "15": "calcular_costo_compra",
        "16": "calcular_nota_final",
        "17": "convertir_unidades",
        "18": "calcular_interes_compuesto",
        "19": "calcular_valor_total",
        "20": "calcular_salario_neto",
        "21": "calcular_impuestos",
        "22": "calcular_nivel_temperatura",
        "23": "calcular_mayor_edad",
        "24": "calcular_el_numero_mayor",
        "25": "calculadora_descuento",
        "26": "clasificar_triangulo",
        "27": "determinar_si_es__positivo_negativo",
        "28": "sacar_calificaciones",
        "29": "romper_en_siete",
        "30": "imprimir_impares",
        "31": "imprimir_impares_hasta_7",
        "32": "imprimir_numeros",
        "33": "calcular_total_compra",
        "34": "imprimir_numeros_pares_impares",
        "35": "clasificar_numeros",
        "36": "calcular_precio_con_impuesto",
        "37": "calcular_total_impuesto",
        "38": "encontrar_numero_mayor"
    }

    print("=========================================== Menú =================================")
    for key, value in menu.items():
        print(f"{key}. {value}")
    print("0. Salir")
    print("==================================================================================")
    return input("Selecciona una opción: ")

def delay(seconds):
    time.sleep(seconds)
    

menu = {
    "1": intercambiar_variables,
    "2": transformar_valores,
    "3": imprimir_tipos_de_dato,
    "4": calcular_area_triangulo,
    "5": calcular_perimetro_rectangulo,
    "6": calcula_perimetro_de_rectangulo,
    "7": calcular_volumen_prisma_rectangular,
    "8": resolver_ecuaciones,
    "9": valores_para_x_y,
    "10": resolver_conversiones_unidades,
    "11": resolver_regla_de_tres,
    "12": calcular_interes_prestamo,
    "13": salario_de_neto_trabajador,
    "14": calcular_costo_gasolina,
    "15": calcular_costo_compra,
    "16": calcular_nota_final,
    "17": convertir_unidades,
    "18": calcular_interes_compuesto,
    "19": calcular_valor_total,
    "20": calcular_salario_neto,
    "21": calcular_impuestos,
    "22": calcular_nivel_temperatura,
    "23": calcular_mayor_edad,
    "24": calcular_el_numero_mayor,
    "25": calculadora_descuento,
    "26": clasificar_triangulo,
    "27": determinar_si_es__positivo_negativo,
    "28": sacar_calificaciones,
    "29": romper_en_siete,
    "30": imprimir_impares,
    "31": imprimir_impares_hasta_7,
    "32": imprimir_numeros,
    "33": calcular_total_compra,
    "34": imprimir_numeros_pares_impares,
    "35": clasificar_numeros,
    "36": calcular_precio_con_impuesto,
    "37": calcular_total_impuesto,
    "38": encontrar_numero_mayor
}
while True:
    opcion = mostrar_menu()


    if opcion == "0":
        print("Hasta luego")
        break
    if opcion in menu:
        menu[opcion]()
        delay(5)

#-------------------------------------------------------------------------------------------------------------------------
    elif opcion == "38": # código a ejecutar si la condición es verdadera
        if int(opcion) > 40:
            for i in range(1, 8, 2):
                print(i)
                


