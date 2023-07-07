print ("Programa 7. \n que calcula el volumen de un prisma rectangular \n")

i1 = input("Escriba el valor de el largo: ")
i2 = input("Escriba el valor de el ancho: ")
i3 = input("Escriba el valor de la altura: ")

Largo= float(i1)
Ancho= float(i2)
Altura= float(i3)

V= Largo * Ancho * Altura 
VR =round(V,4)

print("El volumen de un prisma rectangular es: ", VR)