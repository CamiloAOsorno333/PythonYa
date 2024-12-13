"""Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de
los valores ingresados y su promedio."""

print("Por favor ingrese los números para sacar el promedio")

x=1
suma=0
while x<10:
    n=int(input("Ingrese el número Nro. " + str(x) + '='))
    x= x+1
    suma=suma + n
    promedio= suma/10

print("La suma es= " + str(suma))
##print(suma)
print("El promedio es= " + str(promedio))
##print(promedio)
