"""Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio
 e imprima alguno de estos mensajes:
Si el promedio es >=7 mostrar "Promocionado".
Si el promedio es >=4 y <7 mostrar "Regular".
Si el promedio es <4 mostrar "Reprobado"."""


n1=float(input("Por favor ingrese la nota Nro. 1 " + '\n'))
n2=float(input("Por favor ingrese la nota Nro. 2 " + '\n'))
n3=float(input("Por favor ingrese la nota Nro. 3 " + '\n'))

suma= n1 + n2 + n3

promedio= suma / 3

if promedio >= 7:
    print("Promocionado")
else:
    if promedio >= 4 and promedio<7:
        print("Regular")
    else:
        print("Reprobado")

