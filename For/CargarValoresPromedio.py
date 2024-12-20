"""Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de
los valores ingresados y su promedio."""


x=0
suma=0
promedio=0

for x in range (10):
    valor=int(input("Por favor ingrese el Nro." + str(x) + '='))
    suma=suma + valor

    promedio= suma/10

input("El total de la suma de los valores es ingresados es= " + str(suma))
input("El promedio de los valores es ingresados es= " + str(promedio))