"""Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo
(los primeros 12 términos)
Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36."""

input("Hoy veremos la tabla sorpresa de multiplicar, haz tu la elección...😁")

n=int(input("Por favor ingresa el número de la tabla que te guataria ver, recuerda es del 1 al 10=  "))
suma=0

for x in range (12):
    suma= suma + x
    input(str(n) + "x" + str(x) + '=' +str(suma) )
