# -*- coding: utf-8 -*-
"""
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
"""

input("Por favor ingrese los valores para analizarlos" + '\n')

neg=0
pos=0
m15=0
pares=0
suma=0

for f in range (10):
    n=int(input("Por favor ingrese el Nro. " + str(f) + '='))
    if n<0:
        neg=neg + 1
    if n>0:
        pos=pos + 1 
    if n%15==0:
        m15=m15 + 1
    if n%2==0:
        suma=suma + n
        
input("La suma de los números pares es= " + str(suma))
input("La cantidad de los números negativos es= " + str(neg))
input("La cantiad de los números positivos es= " + str(pos))
input("La cantiad de los números multiplso de 15 es= " + str(m15))