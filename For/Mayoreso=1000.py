"""Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000
(n se carga por teclado)
Este tipo de problemas también se puede resolver empleando la estructura repetitiva for. Lo primero que se hace es
cargar una variable que indique la cantidad de valores a ingresar. Dicha variable se carga antes de entrar a la
estructura repetitiva for."""

n=int(input("Por favor ingrese la cantidad de números a analizar= "))
m1000=0
men1000=0

for x in range (n):
    ns=int(input("Por favor ingrese el Nro." + str(x) + '= '))
    if ns>=1000:
        m1000= m1000 + 1
    if ns<1000:
        men1000=men1000 + 1

input("La cantidad de números mayores o iguales a 1000 son= " + str(m1000))
input("La cantidad de números menores a 1000 son= " + str(men1000))
