"""Escribir un programa en el cual: dada una lista de tres valores numéricos distintos
se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)"""

n1= int(input("Ingrese el  Nro. 1= " + '\n'))
n2= int(input("Ingrese el  Nro. 2= " + '\n'))
n3= int(input("Ingrese el  Nro. 2= " + '\n'))

if n1>n2 and n1>n3:
    print("El número mayor es el Nro.1= " , n1)
else:
    if n2>n1 and n2>n3:
        print("El número mayor es el Nro. 2= " , n2)
    else:
        print("El número mayor es el Nro. 3= ", n3)

print("Ahora veamos cual es el número menor")

if n1<n2 and n1<n3:
    print("El número menor es el Nro. 1= " , n1)
else:
    if n2<n1 and n2<n3:
        print("El número menor es el Nro.2= " , n2)
    else:
        print("El número menor es el Nro.3= " , n3)